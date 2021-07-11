# Generated from ./grammar/Kaleidoscope.g4 by ANTLR 4.9
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO


def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3\24")
        buf.write("K\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\3\2\3\2\3\2\3\2\3\2")
        buf.write("\3\2\3\2\3\2\3\2\3\2\3\2\7\2\26\n\2\f\2\16\2\31\13\2\5")
        buf.write("\2\33\n\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\5\2%\n\2\3\3")
        buf.write("\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\7\3\63\n")
        buf.write("\3\f\3\16\3\66\13\3\3\4\3\4\3\4\7\4;\n\4\f\4\16\4>\13")
        buf.write("\4\3\4\3\4\3\5\3\5\3\5\3\5\3\5\3\5\3\5\5\5I\n\5\3\5\2")
        buf.write("\3\4\6\2\4\6\b\2\3\3\2\13\f\2R\2$\3\2\2\2\4&\3\2\2\2\6")
        buf.write("\67\3\2\2\2\bH\3\2\2\2\n%\7\24\2\2\13\f\7\3\2\2\f\r\5")
        buf.write("\4\3\2\r\16\7\4\2\2\16%\3\2\2\2\17%\7\23\2\2\20\21\7\23")
        buf.write("\2\2\21\32\7\3\2\2\22\27\5\4\3\2\23\24\7\5\2\2\24\26\5")
        buf.write("\4\3\2\25\23\3\2\2\2\26\31\3\2\2\2\27\25\3\2\2\2\27\30")
        buf.write("\3\2\2\2\30\33\3\2\2\2\31\27\3\2\2\2\32\22\3\2\2\2\32")
        buf.write("\33\3\2\2\2\33\34\3\2\2\2\34%\7\4\2\2\35\36\7\16\2\2\36")
        buf.write("\37\5\4\3\2\37 \7\17\2\2 !\5\4\3\2!\"\7\20\2\2\"#\5\4")
        buf.write("\3\2#%\3\2\2\2$\n\3\2\2\2$\13\3\2\2\2$\17\3\2\2\2$\20")
        buf.write("\3\2\2\2$\35\3\2\2\2%\3\3\2\2\2&\'\b\3\1\2\'(\5\2\2\2")
        buf.write("(\64\3\2\2\2)*\f\6\2\2*+\7\n\2\2+\63\5\4\3\7,-\f\5\2\2")
        buf.write("-.\t\2\2\2.\63\5\4\3\6/\60\f\4\2\2\60\61\7\r\2\2\61\63")
        buf.write("\5\4\3\5\62)\3\2\2\2\62,\3\2\2\2\62/\3\2\2\2\63\66\3\2")
        buf.write("\2\2\64\62\3\2\2\2\64\65\3\2\2\2\65\5\3\2\2\2\66\64\3")
        buf.write("\2\2\2\678\7\23\2\28<\7\3\2\29;\7\23\2\2:9\3\2\2\2;>\3")
        buf.write("\2\2\2<:\3\2\2\2<=\3\2\2\2=?\3\2\2\2><\3\2\2\2?@\7\4\2")
        buf.write("\2@\7\3\2\2\2AB\7\7\2\2BC\5\6\4\2CD\5\4\3\2DI\3\2\2\2")
        buf.write("EF\7\b\2\2FI\5\6\4\2GI\5\4\3\2HA\3\2\2\2HE\3\2\2\2HG\3")
        buf.write("\2\2\2I\t\3\2\2\2\t\27\32$\62\64<H")
        return buf.getvalue()


class KaleidoscopeParser ( Parser ):

    grammarFileName = "Kaleidoscope.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'('", "')'", "','", "';'", "'def'", "'extern'", 
                     "'='", "'*'", "'+'", "'-'", "'<'", "'if'", "'then'", 
                     "'else'" ]

    symbolicNames = [ "<INVALID>", "LPAREN", "RPAREN", "COMMA", "SEMICOLON", 
                      "DEF", "EXTERN", "ASSIGN", "ASTERISK", "PLUS", "MINUS", 
                      "LEFTANGLE", "IF", "THEN", "ELSE", "LineComment", 
                      "WhiteSpace", "Identifier", "Number" ]

    RULE_primaryExpression = 0
    RULE_expression = 1
    RULE_prototype = 2
    RULE_topLevel = 3

    ruleNames =  [ "primaryExpression", "expression", "prototype", "topLevel" ]

    EOF = Token.EOF
    LPAREN=1
    RPAREN=2
    COMMA=3
    SEMICOLON=4
    DEF=5
    EXTERN=6
    ASSIGN=7
    ASTERISK=8
    PLUS=9
    MINUS=10
    LEFTANGLE=11
    IF=12
    THEN=13
    ELSE=14
    LineComment=15
    WhiteSpace=16
    Identifier=17
    Number=18

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.9")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class PrimaryExpressionContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return KaleidoscopeParser.RULE_primaryExpression

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class IfExpressionContext(PrimaryExpressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a KaleidoscopeParser.PrimaryExpressionContext
            super().__init__(parser)
            self.cond = None # ExpressionContext
            self.then_expr = None # ExpressionContext
            self.else_expr = None # ExpressionContext
            self.copyFrom(ctx)

        def IF(self):
            return self.getToken(KaleidoscopeParser.IF, 0)
        def THEN(self):
            return self.getToken(KaleidoscopeParser.THEN, 0)
        def ELSE(self):
            return self.getToken(KaleidoscopeParser.ELSE, 0)
        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(KaleidoscopeParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(KaleidoscopeParser.ExpressionContext,i)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterIfExpression" ):
                listener.enterIfExpression(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitIfExpression" ):
                listener.exitIfExpression(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIfExpression" ):
                return visitor.visitIfExpression(self)
            else:
                return visitor.visitChildren(self)


    class ParenExpressionContext(PrimaryExpressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a KaleidoscopeParser.PrimaryExpressionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def LPAREN(self):
            return self.getToken(KaleidoscopeParser.LPAREN, 0)
        def expression(self):
            return self.getTypedRuleContext(KaleidoscopeParser.ExpressionContext,0)

        def RPAREN(self):
            return self.getToken(KaleidoscopeParser.RPAREN, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterParenExpression" ):
                listener.enterParenExpression(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitParenExpression" ):
                listener.exitParenExpression(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitParenExpression" ):
                return visitor.visitParenExpression(self)
            else:
                return visitor.visitChildren(self)


    class NumberExpressionContext(PrimaryExpressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a KaleidoscopeParser.PrimaryExpressionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def Number(self):
            return self.getToken(KaleidoscopeParser.Number, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterNumberExpression" ):
                listener.enterNumberExpression(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitNumberExpression" ):
                listener.exitNumberExpression(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitNumberExpression" ):
                return visitor.visitNumberExpression(self)
            else:
                return visitor.visitChildren(self)


    class CallExpressionContext(PrimaryExpressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a KaleidoscopeParser.PrimaryExpressionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def Identifier(self):
            return self.getToken(KaleidoscopeParser.Identifier, 0)
        def LPAREN(self):
            return self.getToken(KaleidoscopeParser.LPAREN, 0)
        def RPAREN(self):
            return self.getToken(KaleidoscopeParser.RPAREN, 0)
        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(KaleidoscopeParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(KaleidoscopeParser.ExpressionContext,i)

        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(KaleidoscopeParser.COMMA)
            else:
                return self.getToken(KaleidoscopeParser.COMMA, i)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCallExpression" ):
                listener.enterCallExpression(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCallExpression" ):
                listener.exitCallExpression(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitCallExpression" ):
                return visitor.visitCallExpression(self)
            else:
                return visitor.visitChildren(self)


    class IdentifierExpressionContext(PrimaryExpressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a KaleidoscopeParser.PrimaryExpressionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def Identifier(self):
            return self.getToken(KaleidoscopeParser.Identifier, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterIdentifierExpression" ):
                listener.enterIdentifierExpression(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitIdentifierExpression" ):
                listener.exitIdentifierExpression(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIdentifierExpression" ):
                return visitor.visitIdentifierExpression(self)
            else:
                return visitor.visitChildren(self)



    def primaryExpression(self):

        localctx = KaleidoscopeParser.PrimaryExpressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_primaryExpression)
        self._la = 0 # Token type
        try:
            self.state = 34
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,2,self._ctx)
            if la_ == 1:
                localctx = KaleidoscopeParser.NumberExpressionContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 8
                self.match(KaleidoscopeParser.Number)
                pass

            elif la_ == 2:
                localctx = KaleidoscopeParser.ParenExpressionContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 9
                self.match(KaleidoscopeParser.LPAREN)
                self.state = 10
                self.expression(0)
                self.state = 11
                self.match(KaleidoscopeParser.RPAREN)
                pass

            elif la_ == 3:
                localctx = KaleidoscopeParser.IdentifierExpressionContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 13
                self.match(KaleidoscopeParser.Identifier)
                pass

            elif la_ == 4:
                localctx = KaleidoscopeParser.CallExpressionContext(self, localctx)
                self.enterOuterAlt(localctx, 4)
                self.state = 14
                self.match(KaleidoscopeParser.Identifier)

                self.state = 15
                self.match(KaleidoscopeParser.LPAREN)
                self.state = 24
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << KaleidoscopeParser.LPAREN) | (1 << KaleidoscopeParser.IF) | (1 << KaleidoscopeParser.Identifier) | (1 << KaleidoscopeParser.Number))) != 0):
                    self.state = 16
                    self.expression(0)
                    self.state = 21
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    while _la==KaleidoscopeParser.COMMA:
                        self.state = 17
                        self.match(KaleidoscopeParser.COMMA)
                        self.state = 18
                        self.expression(0)
                        self.state = 23
                        self._errHandler.sync(self)
                        _la = self._input.LA(1)



                self.state = 26
                self.match(KaleidoscopeParser.RPAREN)
                pass

            elif la_ == 5:
                localctx = KaleidoscopeParser.IfExpressionContext(self, localctx)
                self.enterOuterAlt(localctx, 5)
                self.state = 27
                self.match(KaleidoscopeParser.IF)
                self.state = 28
                localctx.cond = self.expression(0)
                self.state = 29
                self.match(KaleidoscopeParser.THEN)
                self.state = 30
                localctx.then_expr = self.expression(0)
                self.state = 31
                self.match(KaleidoscopeParser.ELSE)
                self.state = 32
                localctx.else_expr = self.expression(0)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExpressionContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.lhs = None # ExpressionContext
            self.bop = None # Token
            self.rhs = None # ExpressionContext

        def primaryExpression(self):
            return self.getTypedRuleContext(KaleidoscopeParser.PrimaryExpressionContext,0)


        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(KaleidoscopeParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(KaleidoscopeParser.ExpressionContext,i)


        def ASTERISK(self):
            return self.getToken(KaleidoscopeParser.ASTERISK, 0)

        def PLUS(self):
            return self.getToken(KaleidoscopeParser.PLUS, 0)

        def MINUS(self):
            return self.getToken(KaleidoscopeParser.MINUS, 0)

        def LEFTANGLE(self):
            return self.getToken(KaleidoscopeParser.LEFTANGLE, 0)

        def getRuleIndex(self):
            return KaleidoscopeParser.RULE_expression

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExpression" ):
                listener.enterExpression(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExpression" ):
                listener.exitExpression(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpression" ):
                return visitor.visitExpression(self)
            else:
                return visitor.visitChildren(self)



    def expression(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = KaleidoscopeParser.ExpressionContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 2
        self.enterRecursionRule(localctx, 2, self.RULE_expression, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 37
            self.primaryExpression()
            self._ctx.stop = self._input.LT(-1)
            self.state = 50
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,4,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 48
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,3,self._ctx)
                    if la_ == 1:
                        localctx = KaleidoscopeParser.ExpressionContext(self, _parentctx, _parentState)
                        localctx.lhs = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 39
                        if not self.precpred(self._ctx, 4):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 4)")
                        self.state = 40
                        localctx.bop = self.match(KaleidoscopeParser.ASTERISK)
                        self.state = 41
                        localctx.rhs = self.expression(5)
                        pass

                    elif la_ == 2:
                        localctx = KaleidoscopeParser.ExpressionContext(self, _parentctx, _parentState)
                        localctx.lhs = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 42
                        if not self.precpred(self._ctx, 3):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 3)")
                        self.state = 43
                        localctx.bop = self._input.LT(1)
                        _la = self._input.LA(1)
                        if not(_la==KaleidoscopeParser.PLUS or _la==KaleidoscopeParser.MINUS):
                            localctx.bop = self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 44
                        localctx.rhs = self.expression(4)
                        pass

                    elif la_ == 3:
                        localctx = KaleidoscopeParser.ExpressionContext(self, _parentctx, _parentState)
                        localctx.lhs = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 45
                        if not self.precpred(self._ctx, 2):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                        self.state = 46
                        localctx.bop = self.match(KaleidoscopeParser.LEFTANGLE)
                        self.state = 47
                        localctx.rhs = self.expression(3)
                        pass

             
                self.state = 52
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,4,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class PrototypeContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return KaleidoscopeParser.RULE_prototype

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class FunctionPrototypeContext(PrototypeContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a KaleidoscopeParser.PrototypeContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def Identifier(self, i:int=None):
            if i is None:
                return self.getTokens(KaleidoscopeParser.Identifier)
            else:
                return self.getToken(KaleidoscopeParser.Identifier, i)
        def LPAREN(self):
            return self.getToken(KaleidoscopeParser.LPAREN, 0)
        def RPAREN(self):
            return self.getToken(KaleidoscopeParser.RPAREN, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFunctionPrototype" ):
                listener.enterFunctionPrototype(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFunctionPrototype" ):
                listener.exitFunctionPrototype(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFunctionPrototype" ):
                return visitor.visitFunctionPrototype(self)
            else:
                return visitor.visitChildren(self)



    def prototype(self):

        localctx = KaleidoscopeParser.PrototypeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_prototype)
        self._la = 0 # Token type
        try:
            localctx = KaleidoscopeParser.FunctionPrototypeContext(self, localctx)
            self.enterOuterAlt(localctx, 1)
            self.state = 53
            self.match(KaleidoscopeParser.Identifier)
            self.state = 54
            self.match(KaleidoscopeParser.LPAREN)
            self.state = 58
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==KaleidoscopeParser.Identifier:
                self.state = 55
                self.match(KaleidoscopeParser.Identifier)
                self.state = 60
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 61
            self.match(KaleidoscopeParser.RPAREN)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class TopLevelContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return KaleidoscopeParser.RULE_topLevel

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class ExternalDeclarationContext(TopLevelContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a KaleidoscopeParser.TopLevelContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def EXTERN(self):
            return self.getToken(KaleidoscopeParser.EXTERN, 0)
        def prototype(self):
            return self.getTypedRuleContext(KaleidoscopeParser.PrototypeContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExternalDeclaration" ):
                listener.enterExternalDeclaration(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExternalDeclaration" ):
                listener.exitExternalDeclaration(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExternalDeclaration" ):
                return visitor.visitExternalDeclaration(self)
            else:
                return visitor.visitChildren(self)


    class TopLevelExpressionContext(TopLevelContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a KaleidoscopeParser.TopLevelContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expression(self):
            return self.getTypedRuleContext(KaleidoscopeParser.ExpressionContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTopLevelExpression" ):
                listener.enterTopLevelExpression(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTopLevelExpression" ):
                listener.exitTopLevelExpression(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitTopLevelExpression" ):
                return visitor.visitTopLevelExpression(self)
            else:
                return visitor.visitChildren(self)


    class FunctionDefinitionContext(TopLevelContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a KaleidoscopeParser.TopLevelContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def DEF(self):
            return self.getToken(KaleidoscopeParser.DEF, 0)
        def prototype(self):
            return self.getTypedRuleContext(KaleidoscopeParser.PrototypeContext,0)

        def expression(self):
            return self.getTypedRuleContext(KaleidoscopeParser.ExpressionContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFunctionDefinition" ):
                listener.enterFunctionDefinition(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFunctionDefinition" ):
                listener.exitFunctionDefinition(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFunctionDefinition" ):
                return visitor.visitFunctionDefinition(self)
            else:
                return visitor.visitChildren(self)



    def topLevel(self):

        localctx = KaleidoscopeParser.TopLevelContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_topLevel)
        try:
            self.state = 70
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [KaleidoscopeParser.DEF]:
                localctx = KaleidoscopeParser.FunctionDefinitionContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 63
                self.match(KaleidoscopeParser.DEF)
                self.state = 64
                self.prototype()
                self.state = 65
                self.expression(0)
                pass
            elif token in [KaleidoscopeParser.EXTERN]:
                localctx = KaleidoscopeParser.ExternalDeclarationContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 67
                self.match(KaleidoscopeParser.EXTERN)
                self.state = 68
                self.prototype()
                pass
            elif token in [KaleidoscopeParser.LPAREN, KaleidoscopeParser.IF, KaleidoscopeParser.Identifier, KaleidoscopeParser.Number]:
                localctx = KaleidoscopeParser.TopLevelExpressionContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 69
                self.expression(0)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx



    def sempred(self, localctx:RuleContext, ruleIndex:int, predIndex:int):
        if self._predicates == None:
            self._predicates = dict()
        self._predicates[1] = self.expression_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def expression_sempred(self, localctx:ExpressionContext, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 4)
         

            if predIndex == 1:
                return self.precpred(self._ctx, 3)
         

            if predIndex == 2:
                return self.precpred(self._ctx, 2)
         




