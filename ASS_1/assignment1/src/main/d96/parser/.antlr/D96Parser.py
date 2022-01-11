# Generated from e:\HCMUT\PRINCIPLES_OF_PROGRAMMING_LANGUAGE\ppl-assignments\ASS_1\assignment1\src\main\d96\parser\D96.g4 by ANTLR 4.8
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
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3P")
        buf.write(".\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\3\2\3\2\3\2")
        buf.write("\3\2\3\2\3\2\5\2\23\n\2\3\2\3\2\3\2\6\2\30\n\2\r\2\16")
        buf.write("\2\31\3\2\5\2\35\n\2\3\3\3\3\3\4\3\4\3\5\3\5\5\5%\n\5")
        buf.write("\3\6\3\6\3\6\5\6*\n\6\3\6\3\6\3\6\2\2\7\2\4\6\b\n\2\3")
        buf.write("\4\2\n\n\16\16\2-\2\34\3\2\2\2\4\36\3\2\2\2\6 \3\2\2\2")
        buf.write("\b$\3\2\2\2\n&\3\2\2\2\f\r\5\4\3\2\r\16\7\3\2\2\16\17")
        buf.write("\7\37\2\2\17\20\7 \2\2\20\22\7!\2\2\21\23\5\6\4\2\22\21")
        buf.write("\3\2\2\2\22\23\3\2\2\2\23\24\3\2\2\2\24\25\7\"\2\2\25")
        buf.write("\35\3\2\2\2\26\30\7\4\2\2\27\26\3\2\2\2\30\31\3\2\2\2")
        buf.write("\31\27\3\2\2\2\31\32\3\2\2\2\32\33\3\2\2\2\33\35\7\2\2")
        buf.write("\3\34\f\3\2\2\2\34\27\3\2\2\2\35\3\3\2\2\2\36\37\t\2\2")
        buf.write("\2\37\5\3\2\2\2 !\7\21\2\2!\7\3\2\2\2\"%\5\n\6\2#%\7\21")
        buf.write("\2\2$\"\3\2\2\2$#\3\2\2\2%\t\3\2\2\2&\'\7K\2\2\')\7\37")
        buf.write("\2\2(*\5\b\5\2)(\3\2\2\2)*\3\2\2\2*+\3\2\2\2+,\7 \2\2")
        buf.write(",\13\3\2\2\2\7\22\31\34$)")
        return buf.getvalue()


class D96Parser ( Parser ):

    grammarFileName = "D96.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'main'", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "'Int'", "'Float'", 
                     "'String'", "<INVALID>", "'Void'", "'class'", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "'Array'", "'val'", "'var'", 
                     "'$'", "'('", "')'", "'{'", "'}'", "'['", "']'", "';'", 
                     "','", "':'", "'::'", "'..'", "'.'", "'Break'", "'Foreach'", 
                     "'Boolean'", "'Null'", "'Continue'", "'True'", "'False'", 
                     "'If'", "'Elseif'", "'Else'", "'self'", "'In'", "'By'", 
                     "'return'", "'new'", "'+'", "'-'", "'*'", "'/'", "'%'", 
                     "'!'", "'&&'", "'||'", "'=='", "'='", "'!='", "'>'", 
                     "'>='", "'<='", "'<'", "'==.'", "'+.'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "CLASS_DECLARE", "MEMBER", 
                      "METHODS", "BLOCK_STATEMENT", "LIST_PARAM", "LIST_METHOD", 
                      "INT_TYPE", "FLOAT_TYPE", "STRING", "BOOL_TYPE", "VOID_TYPE", 
                      "CLASS", "PRIMITIVE_TYPE", "INTEGER_LITERAL", "HEX_TYPE", 
                      "OCT_TYPE", "BIN_TYPE", "DEC_TYPE", "STRING_LITERAL", 
                      "ILLEGAL_ESCAPE", "UNCLOSE_STRING", "REAL_LITERAL", 
                      "LITERAL", "ARRAY", "VAL", "VAR", "DOLLAR", "LP", 
                      "RP", "LCB", "RCB", "LSB", "RSB", "SEMI", "COMMA", 
                      "COLON", "SCOPE", "DOTDOT", "DOT", "BREAK", "FOREACH", 
                      "BOOLEAN", "NULL", "CONTINUE", "TRUE", "FALSE", "IF", 
                      "ELSEIF", "ELSE", "SELF", "IN", "BY", "RETURN", "NEW", 
                      "ADD", "SUB", "MUL", "DIV", "MOD", "NOT", "AND", "OR", 
                      "EQUAL", "ASSIGN", "NOTEQUAL", "GT", "GTE", "LTE", 
                      "LT", "EQUAL_STR", "ADD_STR", "ID", "ID_LIST", "WS", 
                      "BLOCK_COMMENT", "UNTERMINATED_COMMENT", "ERROR_CHAR" ]

    RULE_program = 0
    RULE_mptype = 1
    RULE_body = 2
    RULE_exp = 3
    RULE_funcall = 4

    ruleNames =  [ "program", "mptype", "body", "exp", "funcall" ]

    EOF = Token.EOF
    T__0=1
    CLASS_DECLARE=2
    MEMBER=3
    METHODS=4
    BLOCK_STATEMENT=5
    LIST_PARAM=6
    LIST_METHOD=7
    INT_TYPE=8
    FLOAT_TYPE=9
    STRING=10
    BOOL_TYPE=11
    VOID_TYPE=12
    CLASS=13
    PRIMITIVE_TYPE=14
    INTEGER_LITERAL=15
    HEX_TYPE=16
    OCT_TYPE=17
    BIN_TYPE=18
    DEC_TYPE=19
    STRING_LITERAL=20
    ILLEGAL_ESCAPE=21
    UNCLOSE_STRING=22
    REAL_LITERAL=23
    LITERAL=24
    ARRAY=25
    VAL=26
    VAR=27
    DOLLAR=28
    LP=29
    RP=30
    LCB=31
    RCB=32
    LSB=33
    RSB=34
    SEMI=35
    COMMA=36
    COLON=37
    SCOPE=38
    DOTDOT=39
    DOT=40
    BREAK=41
    FOREACH=42
    BOOLEAN=43
    NULL=44
    CONTINUE=45
    TRUE=46
    FALSE=47
    IF=48
    ELSEIF=49
    ELSE=50
    SELF=51
    IN=52
    BY=53
    RETURN=54
    NEW=55
    ADD=56
    SUB=57
    MUL=58
    DIV=59
    MOD=60
    NOT=61
    AND=62
    OR=63
    EQUAL=64
    ASSIGN=65
    NOTEQUAL=66
    GT=67
    GTE=68
    LTE=69
    LT=70
    EQUAL_STR=71
    ADD_STR=72
    ID=73
    ID_LIST=74
    WS=75
    BLOCK_COMMENT=76
    UNTERMINATED_COMMENT=77
    ERROR_CHAR=78

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

        def body(self):
            return self.getTypedRuleContext(D96Parser.BodyContext,0)


        def EOF(self):
            return self.getToken(D96Parser.EOF, 0)

        def CLASS_DECLARE(self, i:int=None):
            if i is None:
                return self.getTokens(D96Parser.CLASS_DECLARE)
            else:
                return self.getToken(D96Parser.CLASS_DECLARE, i)

        def getRuleIndex(self):
            return D96Parser.RULE_program




    def program(self):

        localctx = D96Parser.ProgramContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_program)
        self._la = 0 # Token type
        try:
            self.state = 26
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [D96Parser.INT_TYPE, D96Parser.VOID_TYPE]:
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
                if _la==D96Parser.INTEGER_LITERAL:
                    self.state = 15
                    self.body()


                self.state = 18
                self.match(D96Parser.RCB)
                pass
            elif token in [D96Parser.CLASS_DECLARE]:
                self.enterOuterAlt(localctx, 2)
                self.state = 21 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while True:
                    self.state = 20
                    self.match(D96Parser.CLASS_DECLARE)
                    self.state = 23 
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if not (_la==D96Parser.CLASS_DECLARE):
                        break

                self.state = 25
                self.match(D96Parser.EOF)
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
            self.state = 28
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

        def INTEGER_LITERAL(self):
            return self.getToken(D96Parser.INTEGER_LITERAL, 0)

        def getRuleIndex(self):
            return D96Parser.RULE_body




    def body(self):

        localctx = D96Parser.BodyContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_body)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 30
            self.match(D96Parser.INTEGER_LITERAL)
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


        def INTEGER_LITERAL(self):
            return self.getToken(D96Parser.INTEGER_LITERAL, 0)

        def getRuleIndex(self):
            return D96Parser.RULE_exp




    def exp(self):

        localctx = D96Parser.ExpContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_exp)
        try:
            self.state = 34
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [D96Parser.ID]:
                self.enterOuterAlt(localctx, 1)
                self.state = 32
                self.funcall()
                pass
            elif token in [D96Parser.INTEGER_LITERAL]:
                self.enterOuterAlt(localctx, 2)
                self.state = 33
                self.match(D96Parser.INTEGER_LITERAL)
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
            self.state = 36
            self.match(D96Parser.ID)
            self.state = 37
            self.match(D96Parser.LP)
            self.state = 39
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==D96Parser.INTEGER_LITERAL or _la==D96Parser.ID:
                self.state = 38
                self.exp()


            self.state = 41
            self.match(D96Parser.RP)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





