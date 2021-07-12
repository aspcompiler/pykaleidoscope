import llvmlite.ir as ir

from kaleidoscope.ast_visitor import ASTVisitor
from kaleidoscope.ast import (
    BinaryExprAST,
    CallExprAST,
    ForExprAST,
    FunctionAST,
    IfExprAST,
    NumberExprAST,
    PrototypeAST,
    VariableExprAST,
)


class CodegenError(Exception):
    pass


class CodeGen(ASTVisitor):
    def __init__(self):
        self.module = ir.Module()
        self.builder = None
        self.func_symtab = {}

    def visit_NumberExprAST(self, node: NumberExprAST):
        return ir.Constant(ir.DoubleType(), float(node.val))

    def visit_VariableExprAST(self, node: VariableExprAST):
        return self.func_symtab[node.name]

    def visit_BinaryExprAST(self, node: BinaryExprAST):
        lhs = self.visit(node.lhs)
        rhs = self.visit(node.rhs)

        if node.op == "+":
            return self.builder.fadd(lhs, rhs, "addtmp")
        elif node.op == "-":
            return self.builder.fsub(lhs, rhs, "subtmp")
        elif node.op == "*":
            return self.builder.fmul(lhs, rhs, "multmp")
        elif node.op == "<":
            cmp = self.builder.fcmp_unordered("<", lhs, rhs, "cmptmp")
            return self.builder.uitofp(cmp, ir.DoubleType(), "booltmp")
        else:
            raise CodegenError("Unknown binary operator", node.op)

    def visit_CallExprAST(self, node: CallExprAST):
        callee_func = self.module.globals.get(node.callee, None)
        if callee_func is None or not isinstance(callee_func, ir.Function):
            raise CodegenError("Call to unknown function", node.callee)

        if len(callee_func.args) != len(node.args):
            raise CodegenError("Call argument length mismatch", node.callee)

        call_args = [self.visit(arg) for arg in node.args]
        return self.builder.call(callee_func, call_args, "calltmp")

    def visit_PrototypeAST(self, node: PrototypeAST):
        func_name = node.name
        func_type = ir.FunctionType(ir.DoubleType(), [ir.DoubleType()] * len(node.args))

        # if a unction with this name already existed in the module
        if func_name in self.module.globals:
            raise CodegenError("Function/Global name collision", func_name)
        else:
            func = ir.Function(self.module, func_type, func_name)

            for i, arg in enumerate(func.args):
                arg.name = node.args[i]
                self.func_symtab[arg.name] = arg
            return func

    def visit_FunctionAST(self, node: FunctionAST):
        # Initialize the function symbol table
        self.func_symtab = {}

        func = self.visit(node.proto)
        basic_block_entry = func.append_basic_block("entry")
        self.builder = ir.IRBuilder(basic_block_entry)
        retval = self.visit(node.body)
        self.builder.ret(retval)
        return func

    def visit_IfExprAST(self, node: IfExprAST):
        cond_val = self.visit(node.cond)

        # Convert condition to a bool by comparing non-equal to 0.0.
        cond_val = self.builder.fcmp_ordered(
            "!=", cond_val, ir.Constant(ir.DoubleType(), 0.0), "ifcond"
        )

        # Create blocks for the then and else cases.  Insert the 'then' block at the end of the function.
        then_bb = self.builder.function.append_basic_block("then")
        else_bb = ir.Block(self.builder.function, "else")
        merge_bb = ir.Block(self.builder.function, "ifcont")
        self.builder.cbranch(cond_val, then_bb, else_bb)

        # Emit then value.
        self.builder.position_at_start(then_bb)
        then_val = self.visit(node.then_expr)
        self.builder.branch(merge_bb)
        # Codegen of 'Then' can change the current block, update ThenBB for the PHI.
        then_bb = self.builder.block

        # Emit else block.
        self.builder.function.basic_blocks.append(else_bb)
        self.builder.position_at_start(else_bb)
        else_val = self.visit(node.else_expr)
        self.builder.branch(merge_bb)
        # codegen of 'Else' can change the current block, update ElseBB for the PHI.
        else_bb = self.builder.block

        # Emit merge block.
        self.builder.function.basic_blocks.append(merge_bb)
        self.builder.position_at_start(merge_bb)
        phi = self.builder.phi(ir.DoubleType(), "iftmp")
        phi.add_incoming(then_val, then_bb)
        phi.add_incoming(else_val, else_bb)
        return phi

    def visit_ForExprAST(self, node: ForExprAST):
        # Emit the start expr first, without the variable in scope.
        start_val = self.visit(node.start)

        # Make the new basic block for the loop header, inserting after current block
        preheader_bb = self.builder.block
        loop_bb = self.builder.function.append_basic_block("loop")

        # Insert an explicit fall through from the current block to loop_bb
        self.builder.branch(loop_bb)

        # Start insertion in LoopBB.
        self.builder.position_at_start(loop_bb)

        # Start the PHI node with an entry for start
        variable = self.builder.phi(ir.DoubleType(), node.var_name)
        variable.add_incoming(start_val, preheader_bb)

        # Within the loop, the variable is defined equal to the PHI node. If it
        # shadows an existing variable, we have to restore it, so save it now.
        old_val = self.func_symtab.get(node.var_name)
        self.func_symtab[node.var_name] = variable

        # Emit the body of the loop.  This, like any other expr, can change the
        # current BB.  Note that we ignore the value computed by the body, but don't
        # allow an error.
        self.visit(node.body)

        # Emit the step value.
        step_val = (
            self.visit(node.step) if node.step else ir.Constant(ir.DoubleType(), 1.0)
        )
        next_var = self.builder.fadd(variable, step_val, "nextvar")

        # Compute the end condition.
        end_cond = self.visit(node.end)

        # Convert condition to a bool by comparing non-equal to 0.0.
        end_cond = self.builder.fcmp_ordered(
            "!=", end_cond, ir.Constant(ir.DoubleType(), 0.0), "loopcond"
        )

        # Create the "after loop" block and insert it.
        loop_end_bb = self.builder.block
        after_bb = self.builder.function.append_basic_block("afterloop")

        # Insert the conditional branch into the end of LoopEndBB.
        self.builder.cbranch(end_cond, loop_bb, after_bb)

        # Any new code will be inserted in AfterBB.
        self.builder.position_at_start(after_bb)

        # Add a new entry to the PHI node for the backedge.
        variable.add_incoming(next_var, loop_end_bb)

        # Restore the unshadowed variable.
        if old_val:
            self.func_symtab[node.var_name] = old_val
        else:
            del self.func_symtab[node.var_name]

        # We deviate from the tutorial and return next_var
        return next_var
