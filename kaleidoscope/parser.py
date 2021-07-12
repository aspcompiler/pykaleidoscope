from antlr4 import CommonTokenStream, InputStream

from grammar.KaleidoscopeLexer import KaleidoscopeLexer
from grammar.KaleidoscopeParser import KaleidoscopeParser
from grammar.KaleidoscopeVisitor import KaleidoscopeVisitor

from kaleidoscope.ast import (
    BinaryExprAST,
    ExprAST,
    ExternalDeclaration,
    ForExprAST,
    FunctionAST,
    IfExprAST,
    NumberExprAST,
    PrototypeAST,
    TopLevel,
    VariableExprAST,
    CallExprAST,
)


def parse(program: str) -> TopLevel:
    lexer = KaleidoscopeLexer(InputStream(program))
    stream = CommonTokenStream(lexer)
    parser = KaleidoscopeParser(stream)

    tree = parser.topLevel()

    return ParserVisitor().visit(tree)


_anonymous_function_counter = 0


def make_anonymous(expr: ExprAST):
    global _anonymous_function_counter
    _anonymous_function_counter += 1
    proto = PrototypeAST(f"__anon_expr{_anonymous_function_counter}", [])
    return FunctionAST(proto, expr)


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

    def visitIfExpression(self, ctx: KaleidoscopeParser.IfExpressionContext):
        return IfExprAST(
            self.visit(ctx.cond), self.visit(ctx.then_expr), self.visit(ctx.else_expr)
        )

    def visitForExpression(self, ctx: KaleidoscopeParser.ForExpressionContext):
        return ForExprAST(
            ctx.Identifier().getText(),
            self.visit(ctx.start),
            self.visit(ctx.end),
            self.visit(ctx.step) if ctx.step else None,
            self.visit(ctx.body),
        )

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
        expression = self.visit(ctx.expression())
        return make_anonymous(expression)
