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
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3\26")
        buf.write("X\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\3\2\3\2\3\2\3\2\3\2")
        buf.write("\3\2\3\2\3\2\3\2\3\2\3\2\7\2\26\n\2\f\2\16\2\31\13\2\5")
        buf.write("\2\33\n\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2")
        buf.write("\3\2\3\2\3\2\3\2\3\2\5\2-\n\2\3\2\3\2\3\2\5\2\62\n\2\3")
        buf.write("\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\7\3@\n")
        buf.write("\3\f\3\16\3C\13\3\3\4\3\4\3\4\7\4H\n\4\f\4\16\4K\13\4")
        buf.write("\3\4\3\4\3\5\3\5\3\5\3\5\3\5\3\5\3\5\5\5V\n\5\3\5\2\3")
        buf.write("\4\6\2\4\6\b\2\3\3\2\13\f\2a\2\61\3\2\2\2\4\63\3\2\2\2")
        buf.write("\6D\3\2\2\2\bU\3\2\2\2\n\62\7\26\2\2\13\f\7\3\2\2\f\r")
        buf.write("\5\4\3\2\r\16\7\4\2\2\16\62\3\2\2\2\17\62\7\25\2\2\20")
        buf.write("\21\7\25\2\2\21\32\7\3\2\2\22\27\5\4\3\2\23\24\7\5\2\2")
        buf.write("\24\26\5\4\3\2\25\23\3\2\2\2\26\31\3\2\2\2\27\25\3\2\2")
        buf.write("\2\27\30\3\2\2\2\30\33\3\2\2\2\31\27\3\2\2\2\32\22\3\2")
        buf.write("\2\2\32\33\3\2\2\2\33\34\3\2\2\2\34\62\7\4\2\2\35\36\7")
        buf.write("\16\2\2\36\37\5\4\3\2\37 \7\17\2\2 !\5\4\3\2!\"\7\20\2")
        buf.write("\2\"#\5\4\3\2#\62\3\2\2\2$%\7\21\2\2%&\7\25\2\2&\'\7\t")
        buf.write("\2\2\'(\5\4\3\2()\7\5\2\2),\5\4\3\2*+\7\5\2\2+-\5\4\3")
        buf.write("\2,*\3\2\2\2,-\3\2\2\2-.\3\2\2\2./\7\22\2\2/\60\5\4\3")
        buf.write("\2\60\62\3\2\2\2\61\n\3\2\2\2\61\13\3\2\2\2\61\17\3\2")
        buf.write("\2\2\61\20\3\2\2\2\61\35\3\2\2\2\61$\3\2\2\2\62\3\3\2")
        buf.write("\2\2\63\64\b\3\1\2\64\65\5\2\2\2\65A\3\2\2\2\66\67\f\6")
        buf.write("\2\2\678\7\n\2\28@\5\4\3\79:\f\5\2\2:;\t\2\2\2;@\5\4\3")
        buf.write("\6<=\f\4\2\2=>\7\r\2\2>@\5\4\3\5?\66\3\2\2\2?9\3\2\2\2")
        buf.write("?<\3\2\2\2@C\3\2\2\2A?\3\2\2\2AB\3\2\2\2B\5\3\2\2\2CA")
        buf.write("\3\2\2\2DE\7\25\2\2EI\7\3\2\2FH\7\25\2\2GF\3\2\2\2HK\3")
        buf.write("\2\2\2IG\3\2\2\2IJ\3\2\2\2JL\3\2\2\2KI\3\2\2\2LM\7\4\2")
        buf.write("\2M\7\3\2\2\2NO\7\7\2\2OP\5\6\4\2PQ\5\4\3\2QV\3\2\2\2")
        buf.write("RS\7\b\2\2SV\5\6\4\2TV\5\4\3\2UN\3\2\2\2UR\3\2\2\2UT\3")
        buf.write("\2\2\2V\t\3\2\2\2\n\27\32,\61?AIU")
        return buf.getvalue()


class KaleidoscopeParser ( Parser ):

    grammarFileName = "Kaleidoscope.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'('", "')'", "','", "';'", "'def'", "'extern'", 
                     "'='", "'*'", "'+'", "'-'", "'<'", "'if'", "'then'", 
                     "'else'", "'for'", "'in'" ]

    symbolicNames = [ "<INVALID>", "LPAREN", "RPAREN", "COMMA", "SEMICOLON", 
                      "DEF", "EXTERN", "ASSIGN", "ASTERISK", "PLUS", "MINUS", 
                      "LEFTANGLE", "IF", "THEN", "ELSE", "FOR", "IN", "LineComment", 
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
    FOR=15
    IN=16
    LineComment=17
    WhiteSpace=18
    Identifier=19
    Number=20

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


    class ForExpressionContext(PrimaryExpressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a KaleidoscopeParser.PrimaryExpressionContext
            super().__init__(parser)
            self.start = None # ExpressionContext
            self.end = None # ExpressionContext
            self.step = None # ExpressionContext
            self.body = None # ExpressionContext
            self.copyFrom(ctx)

        def FOR(self):
            return self.getToken(KaleidoscopeParser.FOR, 0)
        def Identifier(self):
            return self.getToken(KaleidoscopeParser.Identifier, 0)
        def ASSIGN(self):
            return self.getToken(KaleidoscopeParser.ASSIGN, 0)
        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(KaleidoscopeParser.COMMA)
            else:
                return self.getToken(KaleidoscopeParser.COMMA, i)
        def IN(self):
            return self.getToken(KaleidoscopeParser.IN, 0)
        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(KaleidoscopeParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(KaleidoscopeParser.ExpressionContext,i)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterForExpression" ):
                listener.enterForExpression(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitForExpression" ):
                listener.exitForExpression(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitForExpression" ):
                return visitor.visitForExpression(self)
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
            self.state = 47
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,3,self._ctx)
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
                if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << KaleidoscopeParser.LPAREN) | (1 << KaleidoscopeParser.IF) | (1 << KaleidoscopeParser.FOR) | (1 << KaleidoscopeParser.Identifier) | (1 << KaleidoscopeParser.Number))) != 0):
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

            elif la_ == 6:
                localctx = KaleidoscopeParser.ForExpressionContext(self, localctx)
                self.enterOuterAlt(localctx, 6)
                self.state = 34
                self.match(KaleidoscopeParser.FOR)
                self.state = 35
                self.match(KaleidoscopeParser.Identifier)
                self.state = 36
                self.match(KaleidoscopeParser.ASSIGN)
                self.state = 37
                localctx.start = self.expression(0)
                self.state = 38
                self.match(KaleidoscopeParser.COMMA)
                self.state = 39
                localctx.end = self.expression(0)
                self.state = 42
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==KaleidoscopeParser.COMMA:
                    self.state = 40
                    self.match(KaleidoscopeParser.COMMA)
                    self.state = 41
                    localctx.step = self.expression(0)


                self.state = 44
                self.match(KaleidoscopeParser.IN)
                self.state = 45
                localctx.body = self.expression(0)
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
            self.state = 50
            self.primaryExpression()
            self._ctx.stop = self._input.LT(-1)
            self.state = 63
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,5,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 61
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,4,self._ctx)
                    if la_ == 1:
                        localctx = KaleidoscopeParser.ExpressionContext(self, _parentctx, _parentState)
                        localctx.lhs = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 52
                        if not self.precpred(self._ctx, 4):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 4)")
                        self.state = 53
                        localctx.bop = self.match(KaleidoscopeParser.ASTERISK)
                        self.state = 54
                        localctx.rhs = self.expression(5)
                        pass

                    elif la_ == 2:
                        localctx = KaleidoscopeParser.ExpressionContext(self, _parentctx, _parentState)
                        localctx.lhs = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 55
                        if not self.precpred(self._ctx, 3):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 3)")
                        self.state = 56
                        localctx.bop = self._input.LT(1)
                        _la = self._input.LA(1)
                        if not(_la==KaleidoscopeParser.PLUS or _la==KaleidoscopeParser.MINUS):
                            localctx.bop = self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 57
                        localctx.rhs = self.expression(4)
                        pass

                    elif la_ == 3:
                        localctx = KaleidoscopeParser.ExpressionContext(self, _parentctx, _parentState)
                        localctx.lhs = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 58
                        if not self.precpred(self._ctx, 2):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                        self.state = 59
                        localctx.bop = self.match(KaleidoscopeParser.LEFTANGLE)
                        self.state = 60
                        localctx.rhs = self.expression(3)
                        pass

             
                self.state = 65
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,5,self._ctx)

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
            self.state = 66
            self.match(KaleidoscopeParser.Identifier)
            self.state = 67
            self.match(KaleidoscopeParser.LPAREN)
            self.state = 71
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==KaleidoscopeParser.Identifier:
                self.state = 68
                self.match(KaleidoscopeParser.Identifier)
                self.state = 73
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 74
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
            self.state = 83
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [KaleidoscopeParser.DEF]:
                localctx = KaleidoscopeParser.FunctionDefinitionContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 76
                self.match(KaleidoscopeParser.DEF)
                self.state = 77
                self.prototype()
                self.state = 78
                self.expression(0)
                pass
            elif token in [KaleidoscopeParser.EXTERN]:
                localctx = KaleidoscopeParser.ExternalDeclarationContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 80
                self.match(KaleidoscopeParser.EXTERN)
                self.state = 81
                self.prototype()
                pass
            elif token in [KaleidoscopeParser.LPAREN, KaleidoscopeParser.IF, KaleidoscopeParser.FOR, KaleidoscopeParser.Identifier, KaleidoscopeParser.Number]:
                localctx = KaleidoscopeParser.TopLevelExpressionContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 82
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
         




