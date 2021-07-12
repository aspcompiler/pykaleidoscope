# Generated from ./grammar/Kaleidoscope.g4 by ANTLR 4.9
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .KaleidoscopeParser import KaleidoscopeParser
else:
    from KaleidoscopeParser import KaleidoscopeParser

# This class defines a complete listener for a parse tree produced by KaleidoscopeParser.
class KaleidoscopeListener(ParseTreeListener):

    # Enter a parse tree produced by KaleidoscopeParser#NumberExpression.
    def enterNumberExpression(self, ctx:KaleidoscopeParser.NumberExpressionContext):
        pass

    # Exit a parse tree produced by KaleidoscopeParser#NumberExpression.
    def exitNumberExpression(self, ctx:KaleidoscopeParser.NumberExpressionContext):
        pass


    # Enter a parse tree produced by KaleidoscopeParser#ParenExpression.
    def enterParenExpression(self, ctx:KaleidoscopeParser.ParenExpressionContext):
        pass

    # Exit a parse tree produced by KaleidoscopeParser#ParenExpression.
    def exitParenExpression(self, ctx:KaleidoscopeParser.ParenExpressionContext):
        pass


    # Enter a parse tree produced by KaleidoscopeParser#IdentifierExpression.
    def enterIdentifierExpression(self, ctx:KaleidoscopeParser.IdentifierExpressionContext):
        pass

    # Exit a parse tree produced by KaleidoscopeParser#IdentifierExpression.
    def exitIdentifierExpression(self, ctx:KaleidoscopeParser.IdentifierExpressionContext):
        pass


    # Enter a parse tree produced by KaleidoscopeParser#CallExpression.
    def enterCallExpression(self, ctx:KaleidoscopeParser.CallExpressionContext):
        pass

    # Exit a parse tree produced by KaleidoscopeParser#CallExpression.
    def exitCallExpression(self, ctx:KaleidoscopeParser.CallExpressionContext):
        pass


    # Enter a parse tree produced by KaleidoscopeParser#IfExpression.
    def enterIfExpression(self, ctx:KaleidoscopeParser.IfExpressionContext):
        pass

    # Exit a parse tree produced by KaleidoscopeParser#IfExpression.
    def exitIfExpression(self, ctx:KaleidoscopeParser.IfExpressionContext):
        pass


    # Enter a parse tree produced by KaleidoscopeParser#ForExpression.
    def enterForExpression(self, ctx:KaleidoscopeParser.ForExpressionContext):
        pass

    # Exit a parse tree produced by KaleidoscopeParser#ForExpression.
    def exitForExpression(self, ctx:KaleidoscopeParser.ForExpressionContext):
        pass


    # Enter a parse tree produced by KaleidoscopeParser#expression.
    def enterExpression(self, ctx:KaleidoscopeParser.ExpressionContext):
        pass

    # Exit a parse tree produced by KaleidoscopeParser#expression.
    def exitExpression(self, ctx:KaleidoscopeParser.ExpressionContext):
        pass


    # Enter a parse tree produced by KaleidoscopeParser#FunctionPrototype.
    def enterFunctionPrototype(self, ctx:KaleidoscopeParser.FunctionPrototypeContext):
        pass

    # Exit a parse tree produced by KaleidoscopeParser#FunctionPrototype.
    def exitFunctionPrototype(self, ctx:KaleidoscopeParser.FunctionPrototypeContext):
        pass


    # Enter a parse tree produced by KaleidoscopeParser#FunctionDefinition.
    def enterFunctionDefinition(self, ctx:KaleidoscopeParser.FunctionDefinitionContext):
        pass

    # Exit a parse tree produced by KaleidoscopeParser#FunctionDefinition.
    def exitFunctionDefinition(self, ctx:KaleidoscopeParser.FunctionDefinitionContext):
        pass


    # Enter a parse tree produced by KaleidoscopeParser#ExternalDeclaration.
    def enterExternalDeclaration(self, ctx:KaleidoscopeParser.ExternalDeclarationContext):
        pass

    # Exit a parse tree produced by KaleidoscopeParser#ExternalDeclaration.
    def exitExternalDeclaration(self, ctx:KaleidoscopeParser.ExternalDeclarationContext):
        pass


    # Enter a parse tree produced by KaleidoscopeParser#TopLevelExpression.
    def enterTopLevelExpression(self, ctx:KaleidoscopeParser.TopLevelExpressionContext):
        pass

    # Exit a parse tree produced by KaleidoscopeParser#TopLevelExpression.
    def exitTopLevelExpression(self, ctx:KaleidoscopeParser.TopLevelExpressionContext):
        pass



del KaleidoscopeParser