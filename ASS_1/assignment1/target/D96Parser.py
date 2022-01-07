# Generated from main/d96/parser/D96.g4 by ANTLR 4.9.2
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
        buf.write("A\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7\4\b")
        buf.write("\t\b\4\t\t\t\3\2\3\2\3\2\3\2\3\2\3\2\5\2\31\n\2\3\2\3")
        buf.write("\2\3\2\3\3\3\3\3\4\3\4\3\4\3\4\5\4$\n\4\3\5\3\5\5\5(\n")
        buf.write("\5\3\6\3\6\3\6\5\6-\n\6\3\6\3\6\3\7\3\7\3\7\3\b\3\b\3")
        buf.write("\b\7\b\67\n\b\f\b\16\b:\13\b\3\t\3\t\3\t\3\t\3\t\3\t\2")
        buf.write("\2\n\2\4\6\b\n\f\16\20\2\3\3\2\4\5\2=\2\22\3\2\2\2\4\35")
        buf.write("\3\2\2\2\6#\3\2\2\2\b\'\3\2\2\2\n)\3\2\2\2\f\60\3\2\2")
        buf.write("\2\16\63\3\2\2\2\20;\3\2\2\2\22\23\5\4\3\2\23\24\7\3\2")
        buf.write("\2\24\25\7\b\2\2\25\26\7\t\2\2\26\30\7\n\2\2\27\31\5\6")
        buf.write("\4\2\30\27\3\2\2\2\30\31\3\2\2\2\31\32\3\2\2\2\32\33\7")
        buf.write("\13\2\2\33\34\7\2\2\3\34\3\3\2\2\2\35\36\t\2\2\2\36\5")
        buf.write("\3\2\2\2\37 \5\n\6\2 !\7\16\2\2!$\3\2\2\2\"$\5\20\t\2")
        buf.write("#\37\3\2\2\2#\"\3\2\2\2$\7\3\2\2\2%(\5\n\6\2&(\7\7\2\2")
        buf.write("\'%\3\2\2\2\'&\3\2\2\2(\t\3\2\2\2)*\7\6\2\2*,\7\b\2\2")
        buf.write("+-\5\b\5\2,+\3\2\2\2,-\3\2\2\2-.\3\2\2\2./\7\t\2\2/\13")
        buf.write("\3\2\2\2\60\61\5\16\b\2\61\62\7\20\2\2\62\r\3\2\2\2\63")
        buf.write("8\7\6\2\2\64\65\7\17\2\2\65\67\7\6\2\2\66\64\3\2\2\2\67")
        buf.write(":\3\2\2\28\66\3\2\2\289\3\2\2\29\17\3\2\2\2:8\3\2\2\2")
        buf.write(";<\7\r\2\2<=\5\f\7\2=>\7\4\2\2>?\7\16\2\2?\21\3\2\2\2")
        buf.write("\7\30#\',8")
        return buf.getvalue()


class D96Parser ( Parser ):

    grammarFileName = "D96.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'main'", "'int'", "'void'", "<INVALID>", 
                     "<INVALID>", "'('", "')'", "'{'", "'}'", "<INVALID>", 
                     "<INVALID>", "';'", "','", "':'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "INTTYPE", "VOIDTYPE", "ID", 
                      "INTLIT", "LB", "RB", "LP", "RP", "IDEN_NAME", "VAR", 
                      "SEMI", "COMMA", "COLON", "WS", "BLOCK_COMMENT", "UNCLOSE_STRING", 
                      "ILLEGAL_ESCAPE", "ERROR_CHAR", "UNTERMINATED_COMMENT" ]

    RULE_program = 0
    RULE_mptype = 1
    RULE_body = 2
    RULE_exp = 3
    RULE_funcall = 4
    RULE_ids_list_with_colon = 5
    RULE_ids_list = 6
    RULE_var_declare = 7

    ruleNames =  [ "program", "mptype", "body", "exp", "funcall", "ids_list_with_colon", 
                   "ids_list", "var_declare" ]

    EOF = Token.EOF
    T__0=1
    INTTYPE=2
    VOIDTYPE=3
    ID=4
    INTLIT=5
    LB=6
    RB=7
    LP=8
    RP=9
    IDEN_NAME=10
    VAR=11
    SEMI=12
    COMMA=13
    COLON=14
    WS=15
    BLOCK_COMMENT=16
    UNCLOSE_STRING=17
    ILLEGAL_ESCAPE=18
    ERROR_CHAR=19
    UNTERMINATED_COMMENT=20

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.9.2")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ProgramContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def mptype(self):
            return self.getTypedRuleContext(D96Parser.MptypeContext,0)


        def LB(self):
            return self.getToken(D96Parser.LB, 0)

        def RB(self):
            return self.getToken(D96Parser.RB, 0)

        def LP(self):
            return self.getToken(D96Parser.LP, 0)

        def RP(self):
            return self.getToken(D96Parser.RP, 0)

        def EOF(self):
            return self.getToken(D96Parser.EOF, 0)

        def body(self):
            return self.getTypedRuleContext(D96Parser.BodyContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_program

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitProgram" ):
                return visitor.visitProgram(self)
            else:
                return visitor.visitChildren(self)




    def program(self):

        localctx = D96Parser.ProgramContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_program)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 16
            self.mptype()
            self.state = 17
            self.match(D96Parser.T__0)
            self.state = 18
            self.match(D96Parser.LB)
            self.state = 19
            self.match(D96Parser.RB)
            self.state = 20
            self.match(D96Parser.LP)
            self.state = 22
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==D96Parser.ID or _la==D96Parser.VAR:
                self.state = 21
                self.body()


            self.state = 24
            self.match(D96Parser.RP)
            self.state = 25
            self.match(D96Parser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class MptypeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def INTTYPE(self):
            return self.getToken(D96Parser.INTTYPE, 0)

        def VOIDTYPE(self):
            return self.getToken(D96Parser.VOIDTYPE, 0)

        def getRuleIndex(self):
            return D96Parser.RULE_mptype

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMptype" ):
                return visitor.visitMptype(self)
            else:
                return visitor.visitChildren(self)




    def mptype(self):

        localctx = D96Parser.MptypeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_mptype)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 27
            _la = self._input.LA(1)
            if not(_la==D96Parser.INTTYPE or _la==D96Parser.VOIDTYPE):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class BodyContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def funcall(self):
            return self.getTypedRuleContext(D96Parser.FuncallContext,0)


        def SEMI(self):
            return self.getToken(D96Parser.SEMI, 0)

        def var_declare(self):
            return self.getTypedRuleContext(D96Parser.Var_declareContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_body

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBody" ):
                return visitor.visitBody(self)
            else:
                return visitor.visitChildren(self)




    def body(self):

        localctx = D96Parser.BodyContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_body)
        try:
            self.state = 33
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [D96Parser.ID]:
                self.enterOuterAlt(localctx, 1)
                self.state = 29
                self.funcall()
                self.state = 30
                self.match(D96Parser.SEMI)
                pass
            elif token in [D96Parser.VAR]:
                self.enterOuterAlt(localctx, 2)
                self.state = 32
                self.var_declare()
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


    class ExpContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def funcall(self):
            return self.getTypedRuleContext(D96Parser.FuncallContext,0)


        def INTLIT(self):
            return self.getToken(D96Parser.INTLIT, 0)

        def getRuleIndex(self):
            return D96Parser.RULE_exp

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExp" ):
                return visitor.visitExp(self)
            else:
                return visitor.visitChildren(self)




    def exp(self):

        localctx = D96Parser.ExpContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_exp)
        try:
            self.state = 37
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [D96Parser.ID]:
                self.enterOuterAlt(localctx, 1)
                self.state = 35
                self.funcall()
                pass
            elif token in [D96Parser.INTLIT]:
                self.enterOuterAlt(localctx, 2)
                self.state = 36
                self.match(D96Parser.INTLIT)
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


    class FuncallContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(D96Parser.ID, 0)

        def LB(self):
            return self.getToken(D96Parser.LB, 0)

        def RB(self):
            return self.getToken(D96Parser.RB, 0)

        def exp(self):
            return self.getTypedRuleContext(D96Parser.ExpContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_funcall

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFuncall" ):
                return visitor.visitFuncall(self)
            else:
                return visitor.visitChildren(self)




    def funcall(self):

        localctx = D96Parser.FuncallContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_funcall)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 39
            self.match(D96Parser.ID)
            self.state = 40
            self.match(D96Parser.LB)
            self.state = 42
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==D96Parser.ID or _la==D96Parser.INTLIT:
                self.state = 41
                self.exp()


            self.state = 44
            self.match(D96Parser.RB)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Ids_list_with_colonContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ids_list(self):
            return self.getTypedRuleContext(D96Parser.Ids_listContext,0)


        def COLON(self):
            return self.getToken(D96Parser.COLON, 0)

        def getRuleIndex(self):
            return D96Parser.RULE_ids_list_with_colon

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIds_list_with_colon" ):
                return visitor.visitIds_list_with_colon(self)
            else:
                return visitor.visitChildren(self)




    def ids_list_with_colon(self):

        localctx = D96Parser.Ids_list_with_colonContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_ids_list_with_colon)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 46
            self.ids_list()
            self.state = 47
            self.match(D96Parser.COLON)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Ids_listContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self, i:int=None):
            if i is None:
                return self.getTokens(D96Parser.ID)
            else:
                return self.getToken(D96Parser.ID, i)

        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(D96Parser.COMMA)
            else:
                return self.getToken(D96Parser.COMMA, i)

        def getRuleIndex(self):
            return D96Parser.RULE_ids_list

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIds_list" ):
                return visitor.visitIds_list(self)
            else:
                return visitor.visitChildren(self)




    def ids_list(self):

        localctx = D96Parser.Ids_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_ids_list)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 49
            self.match(D96Parser.ID)
            self.state = 54
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==D96Parser.COMMA:
                self.state = 50
                self.match(D96Parser.COMMA)
                self.state = 51
                self.match(D96Parser.ID)
                self.state = 56
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Var_declareContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def VAR(self):
            return self.getToken(D96Parser.VAR, 0)

        def ids_list_with_colon(self):
            return self.getTypedRuleContext(D96Parser.Ids_list_with_colonContext,0)


        def INTTYPE(self):
            return self.getToken(D96Parser.INTTYPE, 0)

        def SEMI(self):
            return self.getToken(D96Parser.SEMI, 0)

        def getRuleIndex(self):
            return D96Parser.RULE_var_declare

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVar_declare" ):
                return visitor.visitVar_declare(self)
            else:
                return visitor.visitChildren(self)




    def var_declare(self):

        localctx = D96Parser.Var_declareContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_var_declare)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 57
            self.match(D96Parser.VAR)
            self.state = 58
            self.ids_list_with_colon()
            self.state = 59
            self.match(D96Parser.INTTYPE)
            self.state = 60
            self.match(D96Parser.SEMI)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





