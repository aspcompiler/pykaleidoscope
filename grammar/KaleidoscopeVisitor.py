# Generated from ./grammar/Kaleidoscope.g4 by ANTLR 4.9
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .KaleidoscopeParser import KaleidoscopeParser
else:
    from KaleidoscopeParser import KaleidoscopeParser

# This class defines a complete generic visitor for a parse tree produced by KaleidoscopeParser.

class KaleidoscopeVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by KaleidoscopeParser#NumberExpression.
    def visitNumberExpression(self, ctx:KaleidoscopeParser.NumberExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by KaleidoscopeParser#ParenExpression.
    def visitParenExpression(self, ctx:KaleidoscopeParser.ParenExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by KaleidoscopeParser#IdentifierExpression.
    def visitIdentifierExpression(self, ctx:KaleidoscopeParser.IdentifierExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by KaleidoscopeParser#CallExpression.
    def visitCallExpression(self, ctx:KaleidoscopeParser.CallExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by KaleidoscopeParser#IfExpression.
    def visitIfExpression(self, ctx:KaleidoscopeParser.IfExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by KaleidoscopeParser#expression.
    def visitExpression(self, ctx:KaleidoscopeParser.ExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by KaleidoscopeParser#FunctionPrototype.
    def visitFunctionPrototype(self, ctx:KaleidoscopeParser.FunctionPrototypeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by KaleidoscopeParser#FunctionDefinition.
    def visitFunctionDefinition(self, ctx:KaleidoscopeParser.FunctionDefinitionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by KaleidoscopeParser#ExternalDeclaration.
    def visitExternalDeclaration(self, ctx:KaleidoscopeParser.ExternalDeclarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by KaleidoscopeParser#TopLevelExpression.
    def visitTopLevelExpression(self, ctx:KaleidoscopeParser.TopLevelExpressionContext):
        return self.visitChildren(ctx)



del KaleidoscopeParser