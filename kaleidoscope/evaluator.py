from ctypes import CFUNCTYPE, c_double

import llvmlite.binding as llvm

from kaleidoscope.ast import FunctionAST
from kaleidoscope.parser import parse
from kaleidoscope.code_gen import CodeGen


class Evaluator:
    def __init__(self):
        llvm.initialize()
        llvm.initialize_native_target()
        llvm.initialize_native_asmprinter()

        self.codegen = CodeGen()
        self.target = llvm.Target.from_default_triple()

    def evaluate(self, codestr, optimize=True, llvmdump=False):
        ast = parse(codestr)
        self.codegen.visit(ast)

        if llvmdump:
            print("======== Unoptimized LLVM IR")
            print(str(self.codegen.module))

        if not (
            isinstance(ast, FunctionAST) and ast.proto.name.startswith("__anon_expr")
        ):
            return None

        llvmmod = llvm.parse_assembly(str(self.codegen.module))

        if optimize:
            pmb = llvm.create_pass_manager_builder()
            pmb.opt_level = 2
            pm = llvm.create_module_pass_manager()
            pmb.populate(pm)
            pm.run(llvmmod)

            if llvmdump:
                print("======== Optimized LLVM IR")
                print(str(llvmmod))

        target_machine = self.target.create_target_machine()
        with llvm.create_mcjit_compiler(llvmmod, target_machine) as ee:
            ee.finalize_object()

            if llvmdump:

                print("======== Machine code")
                print(target_machine.emit_assembly(llvmmod))

            fptr = CFUNCTYPE(c_double)(ee.get_function_address(ast.proto.name))

            result = fptr()
            return result
