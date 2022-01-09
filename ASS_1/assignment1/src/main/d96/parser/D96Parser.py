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
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3]")
        buf.write("/\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\3\2\3\2\3\2")
        buf.write("\3\2\3\2\3\2\5\2\23\n\2\3\2\3\2\3\2\6\2\30\n\2\r\2\16")
        buf.write("\2\31\3\2\5\2\35\n\2\3\3\3\3\3\4\3\4\3\4\3\5\3\5\5\5&")
        buf.write("\n\5\3\6\3\6\3\6\5\6+\n\6\3\6\3\6\3\6\2\2\7\2\4\6\b\n")
        buf.write("\2\3\4\2\13\13\17\17\2.\2\34\3\2\2\2\4\36\3\2\2\2\6 \3")
        buf.write("\2\2\2\b%\3\2\2\2\n\'\3\2\2\2\f\r\5\4\3\2\r\16\7\3\2\2")
        buf.write("\16\17\7-\2\2\17\20\7.\2\2\20\22\7/\2\2\21\23\5\6\4\2")
        buf.write("\22\21\3\2\2\2\22\23\3\2\2\2\23\24\3\2\2\2\24\25\7\60")
        buf.write("\2\2\25\35\3\2\2\2\26\30\7\4\2\2\27\26\3\2\2\2\30\31\3")
        buf.write("\2\2\2\31\27\3\2\2\2\31\32\3\2\2\2\32\33\3\2\2\2\33\35")
        buf.write("\7\2\2\3\34\f\3\2\2\2\34\27\3\2\2\2\35\3\3\2\2\2\36\37")
        buf.write("\t\2\2\2\37\5\3\2\2\2 !\5\n\6\2!\"\7\63\2\2\"\7\3\2\2")
        buf.write("\2#&\5\n\6\2$&\7\23\2\2%#\3\2\2\2%$\3\2\2\2&\t\3\2\2\2")
        buf.write("\'(\7W\2\2(*\7-\2\2)+\5\b\5\2*)\3\2\2\2*+\3\2\2\2+,\3")
        buf.write("\2\2\2,-\7.\2\2-\13\3\2\2\2\7\22\31\34%*")
        return buf.getvalue()


class D96Parser ( Parser ):

    grammarFileName = "D96.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'main'", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "'Int'", "'Float'", "'string'", "<INVALID>", "'Void'", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "'Array'", "'val'", 
                     "'var'", "'class'", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "'$'", "'('", "')'", "'{'", 
                     "'}'", "'['", "']'", "';'", "','", "':'", "'..'", "'Break'", 
                     "'Foreach'", "'Boolean'", "'Null'", "'Continue'", "'True'", 
                     "'False'", "'if'", "'elseif'", "'Array Int'", "'Else'", 
                     "'self'", "'return'", "'new'", "'+'", "'+.'", "'-'", 
                     "'*'", "'/'", "'%'", "'!'", "'!='", "'=='", "'==.'", 
                     "'&&'", "'||'", "'>'", "'<='", "'<'", "'>='", "'='" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "CLASS_DECLARE", "MEMBER", 
                      "METHODS", "BLOCK_STATEMENT", "LIST_PARAM", "LIST_METHOD", 
                      "VAR_DECLARE", "INT_TYPE", "FLOAT_TYPE", "STRING", 
                      "BOOL_TYPE", "VOID_TYPE", "ARRAY_TYPE", "ARRAY_LIST", 
                      "PRIMITIVE_TYPE", "INTEGER_LITERAL", "HEX_TYPE", "OCT_TYPE", 
                      "BIN_TYPE", "DEC_TYPE", "STRING_LITERAL", "REAL_LITERAL", 
                      "LITERAL", "ARRAY", "VAL", "VAR", "CLASS", "EXP0", 
                      "EXP1", "EXP2", "EXP3", "EXP4", "EXP5", "EXP6", "EXP7", 
                      "EXP8", "EXP9", "EXP10", "EXP11", "LIST_EXP", "DOLLAR", 
                      "LP", "RP", "LCB", "RCB", "LSB", "RSB", "SEMI", "COMMA", 
                      "COLON", "DOTDOT", "BREAK", "FOREACH", "BOOLEAN", 
                      "NULL", "CONTINUE", "TRUE", "FALSE", "IF", "ELSEIF", 
                      "ARRAYINT", "ELSE", "SELF", "RETURN", "NEW", "ADD", 
                      "ADD_STR", "SUB", "MUL", "DIV", "MOD", "NOT", "NOTEQUAL", 
                      "EQUAL", "EQUAL_STR", "AND", "OR", "GT", "LTE", "LT", 
                      "GTE", "ASSIGN", "ID_LIST", "ID", "WS", "BLOCK_COMMENT", 
                      "UNCLOSE_STRING", "ILLEGAL_ESCAPE", "ERROR_CHAR", 
                      "UNTERMINATED_COMMENT" ]

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
    VAR_DECLARE=8
    INT_TYPE=9
    FLOAT_TYPE=10
    STRING=11
    BOOL_TYPE=12
    VOID_TYPE=13
    ARRAY_TYPE=14
    ARRAY_LIST=15
    PRIMITIVE_TYPE=16
    INTEGER_LITERAL=17
    HEX_TYPE=18
    OCT_TYPE=19
    BIN_TYPE=20
    DEC_TYPE=21
    STRING_LITERAL=22
    REAL_LITERAL=23
    LITERAL=24
    ARRAY=25
    VAL=26
    VAR=27
    CLASS=28
    EXP0=29
    EXP1=30
    EXP2=31
    EXP3=32
    EXP4=33
    EXP5=34
    EXP6=35
    EXP7=36
    EXP8=37
    EXP9=38
    EXP10=39
    EXP11=40
    LIST_EXP=41
    DOLLAR=42
    LP=43
    RP=44
    LCB=45
    RCB=46
    LSB=47
    RSB=48
    SEMI=49
    COMMA=50
    COLON=51
    DOTDOT=52
    BREAK=53
    FOREACH=54
    BOOLEAN=55
    NULL=56
    CONTINUE=57
    TRUE=58
    FALSE=59
    IF=60
    ELSEIF=61
    ARRAYINT=62
    ELSE=63
    SELF=64
    RETURN=65
    NEW=66
    ADD=67
    ADD_STR=68
    SUB=69
    MUL=70
    DIV=71
    MOD=72
    NOT=73
    NOTEQUAL=74
    EQUAL=75
    EQUAL_STR=76
    AND=77
    OR=78
    GT=79
    LTE=80
    LT=81
    GTE=82
    ASSIGN=83
    ID_LIST=84
    ID=85
    WS=86
    BLOCK_COMMENT=87
    UNCLOSE_STRING=88
    ILLEGAL_ESCAPE=89
    ERROR_CHAR=90
    UNTERMINATED_COMMENT=91

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
                if _la==D96Parser.ID:
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
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def INT_TYPE(self):
            return self.getToken(D96Parser.INT_TYPE, 0)

        def VOID_TYPE(self):
            return self.getToken(D96Parser.VOID_TYPE, 0)

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
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def funcall(self):
            return self.getTypedRuleContext(D96Parser.FuncallContext,0)


        def SEMI(self):
            return self.getToken(D96Parser.SEMI, 0)

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
            self.enterOuterAlt(localctx, 1)
            self.state = 30
            self.funcall()
            self.state = 31
            self.match(D96Parser.SEMI)
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


        def INTEGER_LITERAL(self):
            return self.getToken(D96Parser.INTEGER_LITERAL, 0)

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
            self.state = 35
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [D96Parser.ID]:
                self.enterOuterAlt(localctx, 1)
                self.state = 33
                self.funcall()
                pass
            elif token in [D96Parser.INTEGER_LITERAL]:
                self.enterOuterAlt(localctx, 2)
                self.state = 34
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
        __slots__ = 'parser'

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
            self.state = 37
            self.match(D96Parser.ID)
            self.state = 38
            self.match(D96Parser.LP)
            self.state = 40
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==D96Parser.INTEGER_LITERAL or _la==D96Parser.ID:
                self.state = 39
                self.exp()


            self.state = 42
            self.match(D96Parser.RP)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





