import llvmlite.ir as ir

from kaleidoscope.ast_visitor import ASTVisitor
from kaleidoscope.ast import (
    BinaryExprAST,
    CallExprAST,
    FunctionAST,
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
