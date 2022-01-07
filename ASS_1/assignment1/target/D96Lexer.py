# Generated from main/d96/parser/D96.g4 by ANTLR 4.9.2
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
    from typing import TextIO
else:
    from typing.io import TextIO


from lexererr import *



def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2\26")
        buf.write("\u00ab\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7")
        buf.write("\t\7\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r")
        buf.write("\4\16\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23")
        buf.write("\t\23\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30")
        buf.write("\3\2\3\2\3\2\3\2\3\2\3\3\3\3\3\3\3\3\3\4\3\4\3\4\3\4\3")
        buf.write("\4\3\5\6\5A\n\5\r\5\16\5B\3\6\6\6F\n\6\r\6\16\6G\3\7\3")
        buf.write("\7\3\b\3\b\3\t\3\t\3\n\3\n\3\13\3\13\7\13T\n\13\f\13\16")
        buf.write("\13W\13\13\3\f\3\f\3\f\3\f\3\f\3\f\5\f_\n\f\3\r\3\r\3")
        buf.write("\16\3\16\3\17\3\17\3\20\6\20h\n\20\r\20\16\20i\3\20\3")
        buf.write("\20\3\21\3\21\3\21\3\21\7\21r\n\21\f\21\16\21u\13\21\3")
        buf.write("\21\3\21\3\21\3\21\3\21\3\22\3\22\7\22~\n\22\f\22\16\22")
        buf.write("\u0081\13\22\3\22\5\22\u0084\n\22\3\22\3\22\3\23\3\23")
        buf.write("\7\23\u008a\n\23\f\23\16\23\u008d\13\23\3\23\3\23\3\23")
        buf.write("\3\24\3\24\5\24\u0094\n\24\3\25\3\25\3\25\3\26\3\26\3")
        buf.write("\26\5\26\u009c\n\26\3\27\3\27\3\27\3\30\3\30\3\30\3\30")
        buf.write("\7\30\u00a5\n\30\f\30\16\30\u00a8\13\30\3\30\3\30\4s\u00a6")
        buf.write("\2\31\3\3\5\4\7\5\t\6\13\7\r\b\17\t\21\n\23\13\25\f\27")
        buf.write("\r\31\16\33\17\35\20\37\21!\22#\23%\24\'\2)\2+\2-\25/")
        buf.write("\26\3\2\13\4\2C\\c|\3\2\62;\5\2C\\aac|\6\2\62;C\\aac|")
        buf.write("\5\2\13\f\17\17\"\"\7\3\n\f\16\17$$))^^\7\2\n\f\16\17")
        buf.write("$$))^^\n\2$$))^^ddhhppttvv\3\2^^\2\u00b2\2\3\3\2\2\2\2")
        buf.write("\5\3\2\2\2\2\7\3\2\2\2\2\t\3\2\2\2\2\13\3\2\2\2\2\r\3")
        buf.write("\2\2\2\2\17\3\2\2\2\2\21\3\2\2\2\2\23\3\2\2\2\2\25\3\2")
        buf.write("\2\2\2\27\3\2\2\2\2\31\3\2\2\2\2\33\3\2\2\2\2\35\3\2\2")
        buf.write("\2\2\37\3\2\2\2\2!\3\2\2\2\2#\3\2\2\2\2%\3\2\2\2\2-\3")
        buf.write("\2\2\2\2/\3\2\2\2\3\61\3\2\2\2\5\66\3\2\2\2\7:\3\2\2\2")
        buf.write("\t@\3\2\2\2\13E\3\2\2\2\rI\3\2\2\2\17K\3\2\2\2\21M\3\2")
        buf.write("\2\2\23O\3\2\2\2\25Q\3\2\2\2\27^\3\2\2\2\31`\3\2\2\2\33")
        buf.write("b\3\2\2\2\35d\3\2\2\2\37g\3\2\2\2!m\3\2\2\2#{\3\2\2\2")
        buf.write("%\u0087\3\2\2\2\'\u0093\3\2\2\2)\u0095\3\2\2\2+\u009b")
        buf.write("\3\2\2\2-\u009d\3\2\2\2/\u00a0\3\2\2\2\61\62\7o\2\2\62")
        buf.write("\63\7c\2\2\63\64\7k\2\2\64\65\7p\2\2\65\4\3\2\2\2\66\67")
        buf.write("\7k\2\2\678\7p\2\289\7v\2\29\6\3\2\2\2:;\7x\2\2;<\7q\2")
        buf.write("\2<=\7k\2\2=>\7f\2\2>\b\3\2\2\2?A\t\2\2\2@?\3\2\2\2AB")
        buf.write("\3\2\2\2B@\3\2\2\2BC\3\2\2\2C\n\3\2\2\2DF\t\3\2\2ED\3")
        buf.write("\2\2\2FG\3\2\2\2GE\3\2\2\2GH\3\2\2\2H\f\3\2\2\2IJ\7*\2")
        buf.write("\2J\16\3\2\2\2KL\7+\2\2L\20\3\2\2\2MN\7}\2\2N\22\3\2\2")
        buf.write("\2OP\7\177\2\2P\24\3\2\2\2QU\t\4\2\2RT\t\5\2\2SR\3\2\2")
        buf.write("\2TW\3\2\2\2US\3\2\2\2UV\3\2\2\2V\26\3\2\2\2WU\3\2\2\2")
        buf.write("XY\7x\2\2YZ\7c\2\2Z_\7n\2\2[\\\7x\2\2\\]\7c\2\2]_\7t\2")
        buf.write("\2^X\3\2\2\2^[\3\2\2\2_\30\3\2\2\2`a\7=\2\2a\32\3\2\2")
        buf.write("\2bc\7.\2\2c\34\3\2\2\2de\7<\2\2e\36\3\2\2\2fh\t\6\2\2")
        buf.write("gf\3\2\2\2hi\3\2\2\2ig\3\2\2\2ij\3\2\2\2jk\3\2\2\2kl\b")
        buf.write("\20\2\2l \3\2\2\2mn\7%\2\2no\7%\2\2os\3\2\2\2pr\13\2\2")
        buf.write("\2qp\3\2\2\2ru\3\2\2\2st\3\2\2\2sq\3\2\2\2tv\3\2\2\2u")
        buf.write("s\3\2\2\2vw\7%\2\2wx\7%\2\2xy\3\2\2\2yz\b\21\2\2z\"\3")
        buf.write("\2\2\2{\177\7$\2\2|~\5\'\24\2}|\3\2\2\2~\u0081\3\2\2\2")
        buf.write("\177}\3\2\2\2\177\u0080\3\2\2\2\u0080\u0083\3\2\2\2\u0081")
        buf.write("\177\3\2\2\2\u0082\u0084\t\7\2\2\u0083\u0082\3\2\2\2\u0084")
        buf.write("\u0085\3\2\2\2\u0085\u0086\b\22\3\2\u0086$\3\2\2\2\u0087")
        buf.write("\u008b\7$\2\2\u0088\u008a\5\'\24\2\u0089\u0088\3\2\2\2")
        buf.write("\u008a\u008d\3\2\2\2\u008b\u0089\3\2\2\2\u008b\u008c\3")
        buf.write("\2\2\2\u008c\u008e\3\2\2\2\u008d\u008b\3\2\2\2\u008e\u008f")
        buf.write("\5+\26\2\u008f\u0090\b\23\4\2\u0090&\3\2\2\2\u0091\u0094")
        buf.write("\n\b\2\2\u0092\u0094\5)\25\2\u0093\u0091\3\2\2\2\u0093")
        buf.write("\u0092\3\2\2\2\u0094(\3\2\2\2\u0095\u0096\7^\2\2\u0096")
        buf.write("\u0097\t\t\2\2\u0097*\3\2\2\2\u0098\u0099\7^\2\2\u0099")
        buf.write("\u009c\n\t\2\2\u009a\u009c\n\n\2\2\u009b\u0098\3\2\2\2")
        buf.write("\u009b\u009a\3\2\2\2\u009c,\3\2\2\2\u009d\u009e\13\2\2")
        buf.write("\2\u009e\u009f\b\27\5\2\u009f.\3\2\2\2\u00a0\u00a1\7%")
        buf.write("\2\2\u00a1\u00a2\7%\2\2\u00a2\u00a6\3\2\2\2\u00a3\u00a5")
        buf.write("\13\2\2\2\u00a4\u00a3\3\2\2\2\u00a5\u00a8\3\2\2\2\u00a6")
        buf.write("\u00a7\3\2\2\2\u00a6\u00a4\3\2\2\2\u00a7\u00a9\3\2\2\2")
        buf.write("\u00a8\u00a6\3\2\2\2\u00a9\u00aa\b\30\6\2\u00aa\60\3\2")
        buf.write("\2\2\17\2BGU^is\177\u0083\u008b\u0093\u009b\u00a6\7\b")
        buf.write("\2\2\3\22\2\3\23\3\3\27\4\3\30\5")
        return buf.getvalue()


class D96Lexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    T__0 = 1
    INTTYPE = 2
    VOIDTYPE = 3
    ID = 4
    INTLIT = 5
    LB = 6
    RB = 7
    LP = 8
    RP = 9
    IDEN_NAME = 10
    VAR = 11
    SEMI = 12
    COMMA = 13
    COLON = 14
    WS = 15
    BLOCK_COMMENT = 16
    UNCLOSE_STRING = 17
    ILLEGAL_ESCAPE = 18
    ERROR_CHAR = 19
    UNTERMINATED_COMMENT = 20

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'main'", "'int'", "'void'", "'('", "')'", "'{'", "'}'", "';'", 
            "','", "':'" ]

    symbolicNames = [ "<INVALID>",
            "INTTYPE", "VOIDTYPE", "ID", "INTLIT", "LB", "RB", "LP", "RP", 
            "IDEN_NAME", "VAR", "SEMI", "COMMA", "COLON", "WS", "BLOCK_COMMENT", 
            "UNCLOSE_STRING", "ILLEGAL_ESCAPE", "ERROR_CHAR", "UNTERMINATED_COMMENT" ]

    ruleNames = [ "T__0", "INTTYPE", "VOIDTYPE", "ID", "INTLIT", "LB", "RB", 
                  "LP", "RP", "IDEN_NAME", "VAR", "SEMI", "COMMA", "COLON", 
                  "WS", "BLOCK_COMMENT", "UNCLOSE_STRING", "ILLEGAL_ESCAPE", 
                  "STR_CHAR", "ESC_SEQ", "ESC_ILLEGAL", "ERROR_CHAR", "UNTERMINATED_COMMENT" ]

    grammarFileName = "D96.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.9.2")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


    def action(self, localctx:RuleContext, ruleIndex:int, actionIndex:int):
        if self._actions is None:
            actions = dict()
            actions[16] = self.UNCLOSE_STRING_action 
            actions[17] = self.ILLEGAL_ESCAPE_action 
            actions[21] = self.ERROR_CHAR_action 
            actions[22] = self.UNTERMINATED_COMMENT_action 
            self._actions = actions
        action = self._actions.get(ruleIndex, None)
        if action is not None:
            action(localctx, actionIndex)
        else:
            raise Exception("No registered action for:" + str(ruleIndex))


    def UNCLOSE_STRING_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 0:

            		y = str(self.text)
            		possible = ['\b', '\t', '\n', '\f', '\r', '"', "'", '\\']
            		if y[-1] in possible:
            			raise UncloseString(y[1:-1])
            		else:
            			raise UncloseString(y[1:])
            	
     

    def ILLEGAL_ESCAPE_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 1:

            		y = str(self.text)
            		raise IllegalEscape(y[1:])
            	
     

    def ERROR_CHAR_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 2:

            		raise ErrorToken(self.text)
            	
     

    def UNTERMINATED_COMMENT_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 3:

            	print('UNTERMINATED_COMMENT');

     


