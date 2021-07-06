from antlr4 import CommonTokenStream, InputStream

from grammar.KaleidoscopeLexer import KaleidoscopeLexer
from grammar.KaleidoscopeParser import KaleidoscopeParser
from grammar.KaleidoscopeVisitor import KaleidoscopeVisitor

from kaleidoscope.ast import (
    BinaryExprAST,
    ExternalDeclaration,
    FunctionAST,
    NumberExprAST,
    Program,
    PrototypeAST,
    VariableExprAST,
    CallExprAST,
)


def parse(program: str) -> Program:
    lexer = KaleidoscopeLexer(InputStream(program))
    stream = CommonTokenStream(lexer)
    parser = KaleidoscopeParser(stream)

    tree = parser.program()

    return ParserVisitor().visitProgram(tree)


class ParserVisitor(KaleidoscopeVisitor):
    def visitNumberExpression(self, ctx: KaleidoscopeParser.NumberExpressionContext):
        return NumberExprAST(float(ctx.Number().getText()))

    def visitParenExpression(self, ctx: KaleidoscopeParser.ParenExpressionContext):
        return self.visitExpression(ctx.expression())

    def visitIdentifierExpression(
        self, ctx: KaleidoscopeParser.IdentifierExpressionContext
    ):
        return VariableExprAST(ctx.Identifier().getText())

    def visitCallExpression(self, ctx: KaleidoscopeParser.CallExpressionContext):
        name = ctx.Identifier().getText()
        args = [self.visit(expression) for expression in ctx.expression()]
        return CallExprAST(name, args)

    def visitExpression(self, ctx: KaleidoscopeParser.ExpressionContext):
        bop = ctx.bop
        if bop:
            lhs = self.visit(ctx.lhs)
            rhs = self.visit(ctx.rhs)
            return BinaryExprAST(bop.text, lhs, rhs)
        else:
            return self.visit(ctx.primaryExpression())

    def visitFunctionPrototype(self, ctx: KaleidoscopeParser.FunctionPrototypeContext):
        name = ctx.Identifier()[0].getText()
        args = [arg.getText() for arg in ctx.Identifier()[1:]]
        return PrototypeAST(name, args)

    def visitFunctionDefinition(
        self, ctx: KaleidoscopeParser.FunctionDefinitionContext
    ):
        prototype = self.visit(ctx.prototype())
        body = self.visit(ctx.expression())
        return FunctionAST(prototype, body)

    def visitExternalDeclaration(
        self, ctx: KaleidoscopeParser.ExternalDeclarationContext
    ):
        return ExternalDeclaration(proto=self.visit(ctx.prototype()))

    def visitTopLevelExpression(
        self, ctx: KaleidoscopeParser.TopLevelExpressionContext
    ):
        return self.visit(ctx.expression())

    def visitProgram(self, ctx: KaleidoscopeParser.ProgramContext):
        return Program([self.visit(top) for top in ctx.top()])
