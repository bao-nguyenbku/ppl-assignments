# Generated from e:\HCMUT\PRINCIPLES_OF_PROGRAMMING_LANGUAGE\ASSIGNMENT\ASS_1\assignment1\src\main\d96\parser\D96.g4 by ANTLR 4.8
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
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3F")
        buf.write("(\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\3\2\3\2\3\2")
        buf.write("\3\2\3\2\3\2\5\2\23\n\2\3\2\3\2\3\2\3\3\3\3\3\4\3\4\3")
        buf.write("\4\3\5\3\5\5\5\37\n\5\3\6\3\6\3\6\5\6$\n\6\3\6\3\6\3\6")
        buf.write("\2\2\7\2\4\6\b\n\2\3\4\2\n\n\f\f\2%\2\f\3\2\2\2\4\27\3")
        buf.write("\2\2\2\6\31\3\2\2\2\b\36\3\2\2\2\n \3\2\2\2\f\r\5\4\3")
        buf.write("\2\r\16\7\3\2\2\16\17\7\26\2\2\17\20\7\27\2\2\20\22\7")
        buf.write("\30\2\2\21\23\5\6\4\2\22\21\3\2\2\2\22\23\3\2\2\2\23\24")
        buf.write("\3\2\2\2\24\25\7\31\2\2\25\26\7\2\2\3\26\3\3\2\2\2\27")
        buf.write("\30\t\2\2\2\30\5\3\2\2\2\31\32\5\n\6\2\32\33\7\34\2\2")
        buf.write("\33\7\3\2\2\2\34\37\5\n\6\2\35\37\7\20\2\2\36\34\3\2\2")
        buf.write("\2\36\35\3\2\2\2\37\t\3\2\2\2 !\7\21\2\2!#\7\26\2\2\"")
        buf.write("$\5\b\5\2#\"\3\2\2\2#$\3\2\2\2$%\3\2\2\2%&\7\27\2\2&\13")
        buf.write("\3\2\2\2\5\22\36#")
        return buf.getvalue()


class D96Parser ( Parser ):

    grammarFileName = "D96.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'main'", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "'Int'", "<INVALID>", 
                     "'Void'", "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "'val'", "'var'", "'class'", "'$'", "'('", 
                     "')'", "'{'", "'}'", "'['", "']'", "';'", "','", "':'", 
                     "'..'", "'Break'", "'Foreach'", "'Boolean'", "'Null'", 
                     "'Continue'", "'True'", "'False'", "'string'", "'if'", 
                     "'elseif'", "'Array Int'", "'Else'", "<INVALID>", "'return'", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "'+'", "'+.'", 
                     "'-'", "'*'", "'/'", "'%'", "'!'", "'!='", "'=='", 
                     "'==.'", "'&&'", "'>'", "'||'", "'<='", "'='", "'>='" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "CLASS_DECLARE", "VAR_DECLARE", 
                      "MEMBER", "LIST_DATA", "ID_LIST", "METHODS", "INT_TYPE", 
                      "BOOL_TYPE", "VOID_TYPE", "ARRAY_TYPE", "FLOAT_TYPE", 
                      "PRIMITIVE_TYPE", "INTLIT", "ID", "VAL", "VAR", "CLASS", 
                      "DOLLAR", "LP", "RP", "LCB", "RCB", "LSB", "RSB", 
                      "SEMI", "COMMA", "COLON", "DOTDOT", "BREAK", "FOREACH", 
                      "BOOLEAN", "NULL", "CONTINUE", "TRUE", "FALSE", "STRING", 
                      "IF", "ELSEIF", "ARRAYINT", "ELSE", "FLOAT", "RETURN", 
                      "INTEGER_LITERAL", "STRING_LITERAL", "REAL_LITERAL", 
                      "ADD", "ADD_STR", "SUB", "MUL", "DIV", "MOD", "NOT", 
                      "NOTEQUAL", "EQUAL", "EQUAL_STR", "AND", "GT", "OR", 
                      "LTE", "ASSIGN", "GTE", "WS", "BLOCK_COMMENT", "UNCLOSE_STRING", 
                      "ILLEGAL_ESCAPE", "ERROR_CHAR", "UNTERMINATED_COMMENT" ]

    RULE_program = 0
    RULE_mptype = 1
    RULE_body = 2
    RULE_exp = 3
    RULE_funcall = 4

    ruleNames =  [ "program", "mptype", "body", "exp", "funcall" ]

    EOF = Token.EOF
    T__0=1
    CLASS_DECLARE=2
    VAR_DECLARE=3
    MEMBER=4
    LIST_DATA=5
    ID_LIST=6
    METHODS=7
    INT_TYPE=8
    BOOL_TYPE=9
    VOID_TYPE=10
    ARRAY_TYPE=11
    FLOAT_TYPE=12
    PRIMITIVE_TYPE=13
    INTLIT=14
    ID=15
    VAL=16
    VAR=17
    CLASS=18
    DOLLAR=19
    LP=20
    RP=21
    LCB=22
    RCB=23
    LSB=24
    RSB=25
    SEMI=26
    COMMA=27
    COLON=28
    DOTDOT=29
    BREAK=30
    FOREACH=31
    BOOLEAN=32
    NULL=33
    CONTINUE=34
    TRUE=35
    FALSE=36
    STRING=37
    IF=38
    ELSEIF=39
    ARRAYINT=40
    ELSE=41
    FLOAT=42
    RETURN=43
    INTEGER_LITERAL=44
    STRING_LITERAL=45
    REAL_LITERAL=46
    ADD=47
    ADD_STR=48
    SUB=49
    MUL=50
    DIV=51
    MOD=52
    NOT=53
    NOTEQUAL=54
    EQUAL=55
    EQUAL_STR=56
    AND=57
    GT=58
    OR=59
    LTE=60
    ASSIGN=61
    GTE=62
    WS=63
    BLOCK_COMMENT=64
    UNCLOSE_STRING=65
    ILLEGAL_ESCAPE=66
    ERROR_CHAR=67
    UNTERMINATED_COMMENT=68

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.8")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ProgramContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def mptype(self):
            return self.getTypedRuleContext(D96Parser.MptypeContext,0)


        def LP(self):
            return self.getToken(D96Parser.LP, 0)

        def RP(self):
            return self.getToken(D96Parser.RP, 0)

        def LCB(self):
            return self.getToken(D96Parser.LCB, 0)

        def RCB(self):
            return self.getToken(D96Parser.RCB, 0)

        def EOF(self):
            return self.getToken(D96Parser.EOF, 0)

        def body(self):
            return self.getTypedRuleContext(D96Parser.BodyContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_program




    def program(self):

        localctx = D96Parser.ProgramContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_program)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 10
            self.mptype()
            self.state = 11
            self.match(D96Parser.T__0)
            self.state = 12
            self.match(D96Parser.LP)
            self.state = 13
            self.match(D96Parser.RP)
            self.state = 14
            self.match(D96Parser.LCB)
            self.state = 16
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==D96Parser.ID:
                self.state = 15
                self.body()


            self.state = 18
            self.match(D96Parser.RCB)
            self.state = 19
            self.match(D96Parser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class MptypeContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def INT_TYPE(self):
            return self.getToken(D96Parser.INT_TYPE, 0)

        def VOID_TYPE(self):
            return self.getToken(D96Parser.VOID_TYPE, 0)

        def getRuleIndex(self):
            return D96Parser.RULE_mptype




    def mptype(self):

        localctx = D96Parser.MptypeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_mptype)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 21
            _la = self._input.LA(1)
            if not(_la==D96Parser.INT_TYPE or _la==D96Parser.VOID_TYPE):
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

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def funcall(self):
            return self.getTypedRuleContext(D96Parser.FuncallContext,0)


        def SEMI(self):
            return self.getToken(D96Parser.SEMI, 0)

        def getRuleIndex(self):
            return D96Parser.RULE_body




    def body(self):

        localctx = D96Parser.BodyContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_body)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 23
            self.funcall()
            self.state = 24
            self.match(D96Parser.SEMI)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExpContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def funcall(self):
            return self.getTypedRuleContext(D96Parser.FuncallContext,0)


        def INTLIT(self):
            return self.getToken(D96Parser.INTLIT, 0)

        def getRuleIndex(self):
            return D96Parser.RULE_exp




    def exp(self):

        localctx = D96Parser.ExpContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_exp)
        try:
            self.state = 28
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [D96Parser.ID]:
                self.enterOuterAlt(localctx, 1)
                self.state = 26
                self.funcall()
                pass
            elif token in [D96Parser.INTLIT]:
                self.enterOuterAlt(localctx, 2)
                self.state = 27
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

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(D96Parser.ID, 0)

        def LP(self):
            return self.getToken(D96Parser.LP, 0)

        def RP(self):
            return self.getToken(D96Parser.RP, 0)

        def exp(self):
            return self.getTypedRuleContext(D96Parser.ExpContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_funcall




    def funcall(self):

        localctx = D96Parser.FuncallContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_funcall)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 30
            self.match(D96Parser.ID)
            self.state = 31
            self.match(D96Parser.LP)
            self.state = 33
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==D96Parser.INTLIT or _la==D96Parser.ID:
                self.state = 32
                self.exp()


            self.state = 35
            self.match(D96Parser.RP)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





