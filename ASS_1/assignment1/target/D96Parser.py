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
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3H")
        buf.write("\u01ad\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
        buf.write("\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r\4\16")
        buf.write("\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23\t\23")
        buf.write("\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30\4\31")
        buf.write("\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36\t\36")
        buf.write("\4\37\t\37\4 \t \4!\t!\4\"\t\"\4#\t#\4$\t$\4%\t%\4&\t")
        buf.write("&\4\'\t\'\4(\t(\4)\t)\4*\t*\4+\t+\3\2\3\2\3\2\3\3\3\3")
        buf.write("\3\3\3\3\3\3\3\3\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3")
        buf.write("\4\3\4\3\4\3\4\3\4\3\4\3\4\5\4p\n\4\3\5\3\5\3\5\5\5u\n")
        buf.write("\5\3\6\3\6\3\6\3\6\3\6\3\6\3\6\3\7\3\7\3\7\5\7\u0081\n")
        buf.write("\7\3\b\3\b\3\b\3\b\3\b\5\b\u0088\n\b\3\t\3\t\5\t\u008c")
        buf.write("\n\t\3\n\3\n\3\n\3\n\3\n\3\n\3\13\3\13\3\13\3\13\3\13")
        buf.write("\3\f\3\f\3\f\3\f\3\f\3\f\3\r\3\r\3\r\3\r\3\r\3\r\5\r\u00a5")
        buf.write("\n\r\3\16\3\16\5\16\u00a9\n\16\3\16\3\16\3\16\3\17\3\17")
        buf.write("\3\17\3\17\3\20\3\20\3\20\3\20\5\20\u00b6\n\20\3\21\3")
        buf.write("\21\3\21\3\21\3\22\3\22\3\22\5\22\u00bf\n\22\3\23\3\23")
        buf.write("\3\23\3\24\3\24\3\24\5\24\u00c7\n\24\3\24\3\24\3\25\3")
        buf.write("\25\3\25\5\25\u00ce\n\25\3\25\3\25\3\25\5\25\u00d3\n\25")
        buf.write("\3\25\3\25\3\26\3\26\3\26\3\27\3\27\3\27\3\27\3\27\3\30")
        buf.write("\3\30\3\30\3\30\3\30\3\30\5\30\u00e5\n\30\3\31\3\31\3")
        buf.write("\31\3\31\3\31\3\31\3\31\3\32\3\32\3\32\3\32\3\32\3\32")
        buf.write("\5\32\u00f4\n\32\3\33\3\33\3\33\3\33\3\33\5\33\u00fb\n")
        buf.write("\33\3\34\3\34\3\34\3\34\3\34\3\34\3\34\5\34\u0104\n\34")
        buf.write("\3\35\3\35\3\35\3\35\3\35\3\35\3\35\3\35\3\35\3\35\3\35")
        buf.write("\3\35\3\35\3\35\3\35\3\35\3\35\3\35\3\35\3\35\3\35\3\35")
        buf.write("\3\35\3\35\3\35\5\35\u011f\n\35\3\36\3\36\3\36\3\36\3")
        buf.write("\36\3\36\3\36\3\36\3\36\7\36\u012a\n\36\f\36\16\36\u012d")
        buf.write("\13\36\3\37\3\37\3\37\3\37\3\37\3\37\3\37\3\37\3\37\7")
        buf.write("\37\u0138\n\37\f\37\16\37\u013b\13\37\3 \3 \3 \3 \3 \3")
        buf.write(" \3 \3 \3 \3 \3 \3 \7 \u0149\n \f \16 \u014c\13 \3!\3")
        buf.write("!\3!\5!\u0151\n!\3\"\3\"\3\"\5\"\u0156\n\"\3#\3#\3#\3")
        buf.write("#\5#\u015c\n#\3$\3$\3$\3$\3$\3$\3$\3$\3$\5$\u0167\n$\3")
        buf.write("%\3%\3%\3%\3%\3%\3%\3%\5%\u0171\n%\3%\5%\u0174\n%\3%\3")
        buf.write("%\3%\3%\3%\5%\u017b\n%\3%\5%\u017e\n%\7%\u0180\n%\f%\16")
        buf.write("%\u0183\13%\3&\3&\3&\3&\5&\u0189\n&\3&\3&\5&\u018d\n&")
        buf.write("\3\'\3\'\3\'\3\'\3\'\5\'\u0194\n\'\3(\3(\3(\3(\3)\3)\3")
        buf.write(")\3)\3)\5)\u019f\n)\3*\3*\3*\3*\5*\u01a5\n*\3+\3+\3+\3")
        buf.write("+\5+\u01ab\n+\3+\2\6:<>H,\2\4\6\b\n\f\16\20\22\24\26\30")
        buf.write("\32\34\36 \"$&(*,.\60\62\64\668:<>@BDFHJLNPRT\2\4\3\2")
        buf.write("DE\3\2\22\23\2\u01c1\2V\3\2\2\2\4Y\3\2\2\2\6o\3\2\2\2")
        buf.write("\bt\3\2\2\2\nv\3\2\2\2\f\u0080\3\2\2\2\16\u0087\3\2\2")
        buf.write("\2\20\u008b\3\2\2\2\22\u008d\3\2\2\2\24\u0093\3\2\2\2")
        buf.write("\26\u0098\3\2\2\2\30\u00a4\3\2\2\2\32\u00a8\3\2\2\2\34")
        buf.write("\u00ad\3\2\2\2\36\u00b5\3\2\2\2 \u00b7\3\2\2\2\"\u00be")
        buf.write("\3\2\2\2$\u00c0\3\2\2\2&\u00c3\3\2\2\2(\u00ca\3\2\2\2")
        buf.write("*\u00d6\3\2\2\2,\u00d9\3\2\2\2.\u00e4\3\2\2\2\60\u00e6")
        buf.write("\3\2\2\2\62\u00f3\3\2\2\2\64\u00fa\3\2\2\2\66\u0103\3")
        buf.write("\2\2\28\u011e\3\2\2\2:\u0120\3\2\2\2<\u012e\3\2\2\2>\u013c")
        buf.write("\3\2\2\2@\u0150\3\2\2\2B\u0155\3\2\2\2D\u015b\3\2\2\2")
        buf.write("F\u0166\3\2\2\2H\u0168\3\2\2\2J\u018c\3\2\2\2L\u0193\3")
        buf.write("\2\2\2N\u0195\3\2\2\2P\u019e\3\2\2\2R\u01a4\3\2\2\2T\u01aa")
        buf.write("\3\2\2\2VW\5P)\2WX\7\2\2\3X\3\3\2\2\2YZ\7\35\2\2Z[\7\3")
        buf.write("\2\2[\\\7\26\2\2\\]\5\6\4\2]^\7\27\2\2^\5\3\2\2\2_`\7")
        buf.write("\4\2\2`a\7\24\2\2ab\7\25\2\2bc\7\26\2\2cd\5\b\5\2de\7")
        buf.write("\27\2\2ep\3\2\2\2fg\5\16\b\2gh\7\4\2\2hi\7\24\2\2ij\7")
        buf.write("\25\2\2jk\7\26\2\2kl\5\b\5\2lm\7\27\2\2mn\5\16\b\2np\3")
        buf.write("\2\2\2o_\3\2\2\2of\3\2\2\2p\7\3\2\2\2qu\5(\25\2ru\5&\24")
        buf.write("\2su\3\2\2\2tq\3\2\2\2tr\3\2\2\2ts\3\2\2\2u\t\3\2\2\2")
        buf.write("vw\7\35\2\2wx\7D\2\2xy\5\f\7\2yz\7\26\2\2z{\5\16\b\2{")
        buf.write("|\7\27\2\2|\13\3\2\2\2}~\7\34\2\2~\u0081\7D\2\2\177\u0081")
        buf.write("\3\2\2\2\u0080}\3\2\2\2\u0080\177\3\2\2\2\u0081\r\3\2")
        buf.write("\2\2\u0082\u0088\5\20\t\2\u0083\u0084\5\20\t\2\u0084\u0085")
        buf.write("\5\16\b\2\u0085\u0088\3\2\2\2\u0086\u0088\3\2\2\2\u0087")
        buf.write("\u0082\3\2\2\2\u0087\u0083\3\2\2\2\u0087\u0086\3\2\2\2")
        buf.write("\u0088\17\3\2\2\2\u0089\u008c\5(\25\2\u008a\u008c\5\26")
        buf.write("\f\2\u008b\u0089\3\2\2\2\u008b\u008a\3\2\2\2\u008c\21")
        buf.write("\3\2\2\2\u008d\u008e\7+\2\2\u008e\u008f\7\24\2\2\u008f")
        buf.write("\u0090\5\30\r\2\u0090\u0091\7\25\2\2\u0091\u0092\5\34")
        buf.write("\17\2\u0092\23\3\2\2\2\u0093\u0094\7,\2\2\u0094\u0095")
        buf.write("\7\24\2\2\u0095\u0096\7\25\2\2\u0096\u0097\5\34\17\2\u0097")
        buf.write("\25\3\2\2\2\u0098\u0099\t\2\2\2\u0099\u009a\7\24\2\2\u009a")
        buf.write("\u009b\5\30\r\2\u009b\u009c\7\25\2\2\u009c\u009d\5\34")
        buf.write("\17\2\u009d\27\3\2\2\2\u009e\u00a5\5\32\16\2\u009f\u00a0")
        buf.write("\5\32\16\2\u00a0\u00a1\7\32\2\2\u00a1\u00a2\5\30\r\2\u00a2")
        buf.write("\u00a5\3\2\2\2\u00a3\u00a5\3\2\2\2\u00a4\u009e\3\2\2\2")
        buf.write("\u00a4\u009f\3\2\2\2\u00a4\u00a3\3\2\2\2\u00a5\31\3\2")
        buf.write("\2\2\u00a6\u00a9\5R*\2\u00a7\u00a9\5T+\2\u00a8\u00a6\3")
        buf.write("\2\2\2\u00a8\u00a7\3\2\2\2\u00a9\u00aa\3\2\2\2\u00aa\u00ab")
        buf.write("\7\34\2\2\u00ab\u00ac\5\62\32\2\u00ac\33\3\2\2\2\u00ad")
        buf.write("\u00ae\7\26\2\2\u00ae\u00af\5\36\20\2\u00af\u00b0\7\27")
        buf.write("\2\2\u00b0\35\3\2\2\2\u00b1\u00b6\5(\25\2\u00b2\u00b6")
        buf.write("\5 \21\2\u00b3\u00b6\5&\24\2\u00b4\u00b6\3\2\2\2\u00b5")
        buf.write("\u00b1\3\2\2\2\u00b5\u00b2\3\2\2\2\u00b5\u00b3\3\2\2\2")
        buf.write("\u00b5\u00b4\3\2\2\2\u00b6\37\3\2\2\2\u00b7\u00b8\5\"")
        buf.write("\22\2\u00b8\u00b9\79\2\2\u00b9\u00ba\5\66\34\2\u00ba!")
        buf.write("\3\2\2\2\u00bb\u00bf\7D\2\2\u00bc\u00bf\7E\2\2\u00bd\u00bf")
        buf.write("\5$\23\2\u00be\u00bb\3\2\2\2\u00be\u00bc\3\2\2\2\u00be")
        buf.write("\u00bd\3\2\2\2\u00bf#\3\2\2\2\u00c0\u00c1\t\2\2\2\u00c1")
        buf.write("\u00c2\5F$\2\u00c2%\3\2\2\2\u00c3\u00c4\t\2\2\2\u00c4")
        buf.write("\u00c6\7\24\2\2\u00c5\u00c7\5\66\34\2\u00c6\u00c5\3\2")
        buf.write("\2\2\u00c6\u00c7\3\2\2\2\u00c7\u00c8\3\2\2\2\u00c8\u00c9")
        buf.write("\7\25\2\2\u00c9\'\3\2\2\2\u00ca\u00cd\t\3\2\2\u00cb\u00ce")
        buf.write("\5R*\2\u00cc\u00ce\5T+\2\u00cd\u00cb\3\2\2\2\u00cd\u00cc")
        buf.write("\3\2\2\2\u00ce\u00cf\3\2\2\2\u00cf\u00d0\7\34\2\2\u00d0")
        buf.write("\u00d2\5\62\32\2\u00d1\u00d3\5*\26\2\u00d2\u00d1\3\2\2")
        buf.write("\2\u00d2\u00d3\3\2\2\2\u00d3\u00d4\3\2\2\2\u00d4\u00d5")
        buf.write("\7\32\2\2\u00d5)\3\2\2\2\u00d6\u00d7\79\2\2\u00d7\u00d8")
        buf.write("\5P)\2\u00d8+\3\2\2\2\u00d9\u00da\7&\2\2\u00da\u00db\7")
        buf.write("\24\2\2\u00db\u00dc\5.\30\2\u00dc\u00dd\7\25\2\2\u00dd")
        buf.write("-\3\2\2\2\u00de\u00df\5\64\33\2\u00df\u00e0\7\33\2\2\u00e0")
        buf.write("\u00e1\5.\30\2\u00e1\u00e5\3\2\2\2\u00e2\u00e5\5\64\33")
        buf.write("\2\u00e3\u00e5\3\2\2\2\u00e4\u00de\3\2\2\2\u00e4\u00e2")
        buf.write("\3\2\2\2\u00e4\u00e3\3\2\2\2\u00e5/\3\2\2\2\u00e6\u00e7")
        buf.write("\7&\2\2\u00e7\u00e8\7\30\2\2\u00e8\u00e9\5\62\32\2\u00e9")
        buf.write("\u00ea\7\33\2\2\u00ea\u00eb\7\t\2\2\u00eb\u00ec\7\31\2")
        buf.write("\2\u00ec\61\3\2\2\2\u00ed\u00f4\7\5\2\2\u00ee\u00f4\7")
        buf.write("\b\2\2\u00ef\u00f4\7\6\2\2\u00f0\u00f4\5\60\31\2\u00f1")
        buf.write("\u00f4\7\7\2\2\u00f2\u00f4\7\35\2\2\u00f3\u00ed\3\2\2")
        buf.write("\2\u00f3\u00ee\3\2\2\2\u00f3\u00ef\3\2\2\2\u00f3\u00f0")
        buf.write("\3\2\2\2\u00f3\u00f1\3\2\2\2\u00f3\u00f2\3\2\2\2\u00f4")
        buf.write("\63\3\2\2\2\u00f5\u00fb\7\t\2\2\u00f6\u00fb\7\5\2\2\u00f7")
        buf.write("\u00fb\7\21\2\2\u00f8\u00fb\7\16\2\2\u00f9\u00fb\5,\27")
        buf.write("\2\u00fa\u00f5\3\2\2\2\u00fa\u00f6\3\2\2\2\u00fa\u00f7")
        buf.write("\3\2\2\2\u00fa\u00f8\3\2\2\2\u00fa\u00f9\3\2\2\2\u00fb")
        buf.write("\65\3\2\2\2\u00fc\u00fd\7\16\2\2\u00fd\u00fe\7?\2\2\u00fe")
        buf.write("\u0104\7\16\2\2\u00ff\u0100\7\16\2\2\u0100\u0101\7@\2")
        buf.write("\2\u0101\u0104\7\16\2\2\u0102\u0104\58\35\2\u0103\u00fc")
        buf.write("\3\2\2\2\u0103\u00ff\3\2\2\2\u0103\u0102\3\2\2\2\u0104")
        buf.write("\67\3\2\2\2\u0105\u0106\5:\36\2\u0106\u0107\7=\2\2\u0107")
        buf.write("\u0108\5:\36\2\u0108\u011f\3\2\2\2\u0109\u010a\5:\36\2")
        buf.write("\u010a\u010b\7>\2\2\u010b\u010c\5:\36\2\u010c\u011f\3")
        buf.write("\2\2\2\u010d\u010e\5:\36\2\u010e\u010f\7;\2\2\u010f\u0110")
        buf.write("\5:\36\2\u0110\u011f\3\2\2\2\u0111\u0112\5:\36\2\u0112")
        buf.write("\u0113\7<\2\2\u0113\u0114\5:\36\2\u0114\u011f\3\2\2\2")
        buf.write("\u0115\u0116\5:\36\2\u0116\u0117\78\2\2\u0117\u0118\5")
        buf.write(":\36\2\u0118\u011f\3\2\2\2\u0119\u011a\5:\36\2\u011a\u011b")
        buf.write("\7:\2\2\u011b\u011c\5:\36\2\u011c\u011f\3\2\2\2\u011d")
        buf.write("\u011f\5:\36\2\u011e\u0105\3\2\2\2\u011e\u0109\3\2\2\2")
        buf.write("\u011e\u010d\3\2\2\2\u011e\u0111\3\2\2\2\u011e\u0115\3")
        buf.write("\2\2\2\u011e\u0119\3\2\2\2\u011e\u011d\3\2\2\2\u011f9")
        buf.write("\3\2\2\2\u0120\u0121\b\36\1\2\u0121\u0122\5<\37\2\u0122")
        buf.write("\u012b\3\2\2\2\u0123\u0124\f\5\2\2\u0124\u0125\7\66\2")
        buf.write("\2\u0125\u012a\5<\37\2\u0126\u0127\f\4\2\2\u0127\u0128")
        buf.write("\7\67\2\2\u0128\u012a\5<\37\2\u0129\u0123\3\2\2\2\u0129")
        buf.write("\u0126\3\2\2\2\u012a\u012d\3\2\2\2\u012b\u0129\3\2\2\2")
        buf.write("\u012b\u012c\3\2\2\2\u012c;\3\2\2\2\u012d\u012b\3\2\2")
        buf.write("\2\u012e\u012f\b\37\1\2\u012f\u0130\5> \2\u0130\u0139")
        buf.write("\3\2\2\2\u0131\u0132\f\5\2\2\u0132\u0133\7\60\2\2\u0133")
        buf.write("\u0138\5> \2\u0134\u0135\f\4\2\2\u0135\u0136\7\61\2\2")
        buf.write("\u0136\u0138\5> \2\u0137\u0131\3\2\2\2\u0137\u0134\3\2")
        buf.write("\2\2\u0138\u013b\3\2\2\2\u0139\u0137\3\2\2\2\u0139\u013a")
        buf.write("\3\2\2\2\u013a=\3\2\2\2\u013b\u0139\3\2\2\2\u013c\u013d")
        buf.write("\b \1\2\u013d\u013e\5@!\2\u013e\u014a\3\2\2\2\u013f\u0140")
        buf.write("\f\6\2\2\u0140\u0141\7\62\2\2\u0141\u0149\5@!\2\u0142")
        buf.write("\u0143\f\5\2\2\u0143\u0144\7\63\2\2\u0144\u0149\5@!\2")
        buf.write("\u0145\u0146\f\4\2\2\u0146\u0147\7\64\2\2\u0147\u0149")
        buf.write("\5@!\2\u0148\u013f\3\2\2\2\u0148\u0142\3\2\2\2\u0148\u0145")
        buf.write("\3\2\2\2\u0149\u014c\3\2\2\2\u014a\u0148\3\2\2\2\u014a")
        buf.write("\u014b\3\2\2\2\u014b?\3\2\2\2\u014c\u014a\3\2\2\2\u014d")
        buf.write("\u014e\7\65\2\2\u014e\u0151\5@!\2\u014f\u0151\5B\"\2\u0150")
        buf.write("\u014d\3\2\2\2\u0150\u014f\3\2\2\2\u0151A\3\2\2\2\u0152")
        buf.write("\u0153\7\61\2\2\u0153\u0156\5B\"\2\u0154\u0156\5D#\2\u0155")
        buf.write("\u0152\3\2\2\2\u0155\u0154\3\2\2\2\u0156C\3\2\2\2\u0157")
        buf.write("\u0158\5H%\2\u0158\u0159\5F$\2\u0159\u015c\3\2\2\2\u015a")
        buf.write("\u015c\5H%\2\u015b\u0157\3\2\2\2\u015b\u015a\3\2\2\2\u015c")
        buf.write("E\3\2\2\2\u015d\u015e\7\30\2\2\u015e\u015f\5\66\34\2\u015f")
        buf.write("\u0160\7\31\2\2\u0160\u0167\3\2\2\2\u0161\u0162\7\30\2")
        buf.write("\2\u0162\u0163\5\66\34\2\u0163\u0164\7\31\2\2\u0164\u0165")
        buf.write("\5F$\2\u0165\u0167\3\2\2\2\u0166\u015d\3\2\2\2\u0166\u0161")
        buf.write("\3\2\2\2\u0167G\3\2\2\2\u0168\u0169\b%\1\2\u0169\u016a")
        buf.write("\5J&\2\u016a\u0181\3\2\2\2\u016b\u016c\f\5\2\2\u016c\u016d")
        buf.write("\7A\2\2\u016d\u0173\t\2\2\2\u016e\u0170\7\24\2\2\u016f")
        buf.write("\u0171\5P)\2\u0170\u016f\3\2\2\2\u0170\u0171\3\2\2\2\u0171")
        buf.write("\u0172\3\2\2\2\u0172\u0174\7\25\2\2\u0173\u016e\3\2\2")
        buf.write("\2\u0173\u0174\3\2\2\2\u0174\u0180\3\2\2\2\u0175\u0176")
        buf.write("\f\4\2\2\u0176\u0177\7C\2\2\u0177\u017d\t\2\2\2\u0178")
        buf.write("\u017a\7\24\2\2\u0179\u017b\5P)\2\u017a\u0179\3\2\2\2")
        buf.write("\u017a\u017b\3\2\2\2\u017b\u017c\3\2\2\2\u017c\u017e\7")
        buf.write("\25\2\2\u017d\u0178\3\2\2\2\u017d\u017e\3\2\2\2\u017e")
        buf.write("\u0180\3\2\2\2\u017f\u016b\3\2\2\2\u017f\u0175\3\2\2\2")
        buf.write("\u0180\u0183\3\2\2\2\u0181\u017f\3\2\2\2\u0181\u0182\3")
        buf.write("\2\2\2\u0182I\3\2\2\2\u0183\u0181\3\2\2\2\u0184\u0185")
        buf.write("\7-\2\2\u0185\u0186\7D\2\2\u0186\u0188\7\24\2\2\u0187")
        buf.write("\u0189\5P)\2\u0188\u0187\3\2\2\2\u0188\u0189\3\2\2\2\u0189")
        buf.write("\u018a\3\2\2\2\u018a\u018d\7\25\2\2\u018b\u018d\5L\'\2")
        buf.write("\u018c\u0184\3\2\2\2\u018c\u018b\3\2\2\2\u018dK\3\2\2")
        buf.write("\2\u018e\u0194\5\64\33\2\u018f\u0194\7D\2\2\u0190\u0194")
        buf.write("\7E\2\2\u0191\u0194\7/\2\2\u0192\u0194\5N(\2\u0193\u018e")
        buf.write("\3\2\2\2\u0193\u018f\3\2\2\2\u0193\u0190\3\2\2\2\u0193")
        buf.write("\u0191\3\2\2\2\u0193\u0192\3\2\2\2\u0194M\3\2\2\2\u0195")
        buf.write("\u0196\7\24\2\2\u0196\u0197\5\66\34\2\u0197\u0198\7\25")
        buf.write("\2\2\u0198O\3\2\2\2\u0199\u019f\5\66\34\2\u019a\u019b")
        buf.write("\5\66\34\2\u019b\u019c\7\33\2\2\u019c\u019d\5P)\2\u019d")
        buf.write("\u019f\3\2\2\2\u019e\u0199\3\2\2\2\u019e\u019a\3\2\2\2")
        buf.write("\u019fQ\3\2\2\2\u01a0\u01a5\7D\2\2\u01a1\u01a2\7D\2\2")
        buf.write("\u01a2\u01a3\7\33\2\2\u01a3\u01a5\5R*\2\u01a4\u01a0\3")
        buf.write("\2\2\2\u01a4\u01a1\3\2\2\2\u01a5S\3\2\2\2\u01a6\u01ab")
        buf.write("\7E\2\2\u01a7\u01a8\7E\2\2\u01a8\u01a9\7\33\2\2\u01a9")
        buf.write("\u01ab\5T+\2\u01aa\u01a6\3\2\2\2\u01aa\u01a7\3\2\2\2\u01ab")
        buf.write("U\3\2\2\2)ot\u0080\u0087\u008b\u00a4\u00a8\u00b5\u00be")
        buf.write("\u00c6\u00cd\u00d2\u00e4\u00f3\u00fa\u0103\u011e\u0129")
        buf.write("\u012b\u0137\u0139\u0148\u014a\u0150\u0155\u015b\u0166")
        buf.write("\u0170\u0173\u017a\u017d\u017f\u0181\u0188\u018c\u0193")
        buf.write("\u019e\u01a4\u01aa")
        return buf.getvalue()


class D96Parser ( Parser ):

    grammarFileName = "D96.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'Program'", "'main'", "<INVALID>", "'Float'", 
                     "'String'", "'Int'", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "'Val'", "'Var'", "'('", 
                     "')'", "'{'", "'}'", "'['", "']'", "';'", "','", "':'", 
                     "'Class'", "'Break'", "'Continue'", "'If'", "'Elseif'", 
                     "'Else'", "'Foreach'", "'True'", "'False'", "'Array'", 
                     "'In'", "'Boolean'", "'Return'", "'Null'", "'Constructor'", 
                     "'Destructor'", "'New'", "'By'", "'Self'", "'+'", "'-'", 
                     "'*'", "'/'", "'%'", "'!'", "'&&'", "'||'", "'=='", 
                     "'='", "'!='", "'>'", "'>='", "'<'", "'<='", "'==.'", 
                     "'+.'", "'.'", "'..'", "'::'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "BOOL_TYPE", 
                      "FLOAT_TYPE", "STRING", "INT_TYPE", "INTEGER_LITERAL", 
                      "HEX_TYPE", "OCT_TYPE", "BIN_TYPE", "DEC_TYPE", "STRING_LITERAL", 
                      "ILLEGAL_ESCAPE", "UNCLOSE_STRING", "REAL_LITERAL", 
                      "VAL", "VAR", "LP", "RP", "LCB", "RCB", "LSB", "RSB", 
                      "SEMI", "COMMA", "COLON", "CLASS", "BREAK", "CONTINUE", 
                      "IF", "ELSEIF", "ELSE", "FOREACH", "TRUE", "FALSE", 
                      "ARRAY", "IN", "BOOLEAN", "RETURN", "NULL", "CONSTRUCTOR", 
                      "DESTRUCTOR", "NEW", "BY", "SELF", "ADD", "SUB", "MUL", 
                      "DIV", "MOD", "NOT", "AND", "OR", "EQUAL", "ASSIGN", 
                      "NOTEQUAL", "GT", "GTE", "LT", "LTE", "EQUAL_STR", 
                      "ADD_STR", "DOT", "DOTDOT", "SCOPE", "NORMAL_ID", 
                      "DOLLAR_ID", "WS", "BLOCK_COMMENT", "ERROR_CHAR" ]

    RULE_program = 0
    RULE_class_program = 1
    RULE_class_program_member = 2
    RULE_body_main = 3
    RULE_class_declare = 4
    RULE_extend = 5
    RULE_member_list = 6
    RULE_member = 7
    RULE_constructor_method = 8
    RULE_destructor_method = 9
    RULE_method = 10
    RULE_param_list = 11
    RULE_parameter = 12
    RULE_block_statement = 13
    RULE_statement = 14
    RULE_assign_statement = 15
    RULE_lhs = 16
    RULE_index = 17
    RULE_function_call = 18
    RULE_var_declare = 19
    RULE_init_value = 20
    RULE_array_list = 21
    RULE_literal_list = 22
    RULE_array_type = 23
    RULE_primitive_type = 24
    RULE_literal = 25
    RULE_exp = 26
    RULE_exp0 = 27
    RULE_exp1 = 28
    RULE_exp2 = 29
    RULE_exp3 = 30
    RULE_exp4 = 31
    RULE_exp5 = 32
    RULE_exp6 = 33
    RULE_index_operator = 34
    RULE_exp7 = 35
    RULE_exp8 = 36
    RULE_exp9 = 37
    RULE_exp10 = 38
    RULE_list_exp = 39
    RULE_normal_id_list = 40
    RULE_dollar_id_list = 41

    ruleNames =  [ "program", "class_program", "class_program_member", "body_main", 
                   "class_declare", "extend", "member_list", "member", "constructor_method", 
                   "destructor_method", "method", "param_list", "parameter", 
                   "block_statement", "statement", "assign_statement", "lhs", 
                   "index", "function_call", "var_declare", "init_value", 
                   "array_list", "literal_list", "array_type", "primitive_type", 
                   "literal", "exp", "exp0", "exp1", "exp2", "exp3", "exp4", 
                   "exp5", "exp6", "index_operator", "exp7", "exp8", "exp9", 
                   "exp10", "list_exp", "normal_id_list", "dollar_id_list" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    BOOL_TYPE=3
    FLOAT_TYPE=4
    STRING=5
    INT_TYPE=6
    INTEGER_LITERAL=7
    HEX_TYPE=8
    OCT_TYPE=9
    BIN_TYPE=10
    DEC_TYPE=11
    STRING_LITERAL=12
    ILLEGAL_ESCAPE=13
    UNCLOSE_STRING=14
    REAL_LITERAL=15
    VAL=16
    VAR=17
    LP=18
    RP=19
    LCB=20
    RCB=21
    LSB=22
    RSB=23
    SEMI=24
    COMMA=25
    COLON=26
    CLASS=27
    BREAK=28
    CONTINUE=29
    IF=30
    ELSEIF=31
    ELSE=32
    FOREACH=33
    TRUE=34
    FALSE=35
    ARRAY=36
    IN=37
    BOOLEAN=38
    RETURN=39
    NULL=40
    CONSTRUCTOR=41
    DESTRUCTOR=42
    NEW=43
    BY=44
    SELF=45
    ADD=46
    SUB=47
    MUL=48
    DIV=49
    MOD=50
    NOT=51
    AND=52
    OR=53
    EQUAL=54
    ASSIGN=55
    NOTEQUAL=56
    GT=57
    GTE=58
    LT=59
    LTE=60
    EQUAL_STR=61
    ADD_STR=62
    DOT=63
    DOTDOT=64
    SCOPE=65
    NORMAL_ID=66
    DOLLAR_ID=67
    WS=68
    BLOCK_COMMENT=69
    ERROR_CHAR=70

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

        def list_exp(self):
            return self.getTypedRuleContext(D96Parser.List_expContext,0)


        def EOF(self):
            return self.getToken(D96Parser.EOF, 0)

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
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 84
            self.list_exp()
            self.state = 85
            self.match(D96Parser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Class_programContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def CLASS(self):
            return self.getToken(D96Parser.CLASS, 0)

        def LCB(self):
            return self.getToken(D96Parser.LCB, 0)

        def class_program_member(self):
            return self.getTypedRuleContext(D96Parser.Class_program_memberContext,0)


        def RCB(self):
            return self.getToken(D96Parser.RCB, 0)

        def getRuleIndex(self):
            return D96Parser.RULE_class_program

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitClass_program" ):
                return visitor.visitClass_program(self)
            else:
                return visitor.visitChildren(self)




    def class_program(self):

        localctx = D96Parser.Class_programContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_class_program)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 87
            self.match(D96Parser.CLASS)
            self.state = 88
            self.match(D96Parser.T__0)
            self.state = 89
            self.match(D96Parser.LCB)
            self.state = 90
            self.class_program_member()
            self.state = 91
            self.match(D96Parser.RCB)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Class_program_memberContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LP(self):
            return self.getToken(D96Parser.LP, 0)

        def RP(self):
            return self.getToken(D96Parser.RP, 0)

        def LCB(self):
            return self.getToken(D96Parser.LCB, 0)

        def body_main(self):
            return self.getTypedRuleContext(D96Parser.Body_mainContext,0)


        def RCB(self):
            return self.getToken(D96Parser.RCB, 0)

        def member_list(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(D96Parser.Member_listContext)
            else:
                return self.getTypedRuleContext(D96Parser.Member_listContext,i)


        def getRuleIndex(self):
            return D96Parser.RULE_class_program_member

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitClass_program_member" ):
                return visitor.visitClass_program_member(self)
            else:
                return visitor.visitChildren(self)




    def class_program_member(self):

        localctx = D96Parser.Class_program_memberContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_class_program_member)
        try:
            self.state = 109
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,0,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 93
                self.match(D96Parser.T__1)
                self.state = 94
                self.match(D96Parser.LP)
                self.state = 95
                self.match(D96Parser.RP)
                self.state = 96
                self.match(D96Parser.LCB)
                self.state = 97
                self.body_main()
                self.state = 98
                self.match(D96Parser.RCB)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 100
                self.member_list()
                self.state = 101
                self.match(D96Parser.T__1)
                self.state = 102
                self.match(D96Parser.LP)
                self.state = 103
                self.match(D96Parser.RP)
                self.state = 104
                self.match(D96Parser.LCB)
                self.state = 105
                self.body_main()
                self.state = 106
                self.match(D96Parser.RCB)
                self.state = 107
                self.member_list()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Body_mainContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def var_declare(self):
            return self.getTypedRuleContext(D96Parser.Var_declareContext,0)


        def function_call(self):
            return self.getTypedRuleContext(D96Parser.Function_callContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_body_main

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBody_main" ):
                return visitor.visitBody_main(self)
            else:
                return visitor.visitChildren(self)




    def body_main(self):

        localctx = D96Parser.Body_mainContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_body_main)
        try:
            self.state = 114
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [D96Parser.VAL, D96Parser.VAR]:
                self.enterOuterAlt(localctx, 1)
                self.state = 111
                self.var_declare()
                pass
            elif token in [D96Parser.NORMAL_ID, D96Parser.DOLLAR_ID]:
                self.enterOuterAlt(localctx, 2)
                self.state = 112
                self.function_call()
                pass
            elif token in [D96Parser.RCB]:
                self.enterOuterAlt(localctx, 3)

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


    class Class_declareContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def CLASS(self):
            return self.getToken(D96Parser.CLASS, 0)

        def NORMAL_ID(self):
            return self.getToken(D96Parser.NORMAL_ID, 0)

        def extend(self):
            return self.getTypedRuleContext(D96Parser.ExtendContext,0)


        def LCB(self):
            return self.getToken(D96Parser.LCB, 0)

        def member_list(self):
            return self.getTypedRuleContext(D96Parser.Member_listContext,0)


        def RCB(self):
            return self.getToken(D96Parser.RCB, 0)

        def getRuleIndex(self):
            return D96Parser.RULE_class_declare

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitClass_declare" ):
                return visitor.visitClass_declare(self)
            else:
                return visitor.visitChildren(self)




    def class_declare(self):

        localctx = D96Parser.Class_declareContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_class_declare)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 116
            self.match(D96Parser.CLASS)
            self.state = 117
            self.match(D96Parser.NORMAL_ID)
            self.state = 118
            self.extend()
            self.state = 119
            self.match(D96Parser.LCB)
            self.state = 120
            self.member_list()
            self.state = 121
            self.match(D96Parser.RCB)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExtendContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def COLON(self):
            return self.getToken(D96Parser.COLON, 0)

        def NORMAL_ID(self):
            return self.getToken(D96Parser.NORMAL_ID, 0)

        def getRuleIndex(self):
            return D96Parser.RULE_extend

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExtend" ):
                return visitor.visitExtend(self)
            else:
                return visitor.visitChildren(self)




    def extend(self):

        localctx = D96Parser.ExtendContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_extend)
        try:
            self.state = 126
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [D96Parser.COLON]:
                self.enterOuterAlt(localctx, 1)
                self.state = 123
                self.match(D96Parser.COLON)
                self.state = 124
                self.match(D96Parser.NORMAL_ID)
                pass
            elif token in [D96Parser.LCB]:
                self.enterOuterAlt(localctx, 2)

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


    class Member_listContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def member(self):
            return self.getTypedRuleContext(D96Parser.MemberContext,0)


        def member_list(self):
            return self.getTypedRuleContext(D96Parser.Member_listContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_member_list

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMember_list" ):
                return visitor.visitMember_list(self)
            else:
                return visitor.visitChildren(self)




    def member_list(self):

        localctx = D96Parser.Member_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_member_list)
        try:
            self.state = 133
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,3,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 128
                self.member()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 129
                self.member()
                self.state = 130
                self.member_list()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)

                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class MemberContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def var_declare(self):
            return self.getTypedRuleContext(D96Parser.Var_declareContext,0)


        def method(self):
            return self.getTypedRuleContext(D96Parser.MethodContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_member

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMember" ):
                return visitor.visitMember(self)
            else:
                return visitor.visitChildren(self)




    def member(self):

        localctx = D96Parser.MemberContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_member)
        try:
            self.state = 137
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [D96Parser.VAL, D96Parser.VAR]:
                self.enterOuterAlt(localctx, 1)
                self.state = 135
                self.var_declare()
                pass
            elif token in [D96Parser.NORMAL_ID, D96Parser.DOLLAR_ID]:
                self.enterOuterAlt(localctx, 2)
                self.state = 136
                self.method()
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


    class Constructor_methodContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def CONSTRUCTOR(self):
            return self.getToken(D96Parser.CONSTRUCTOR, 0)

        def LP(self):
            return self.getToken(D96Parser.LP, 0)

        def param_list(self):
            return self.getTypedRuleContext(D96Parser.Param_listContext,0)


        def RP(self):
            return self.getToken(D96Parser.RP, 0)

        def block_statement(self):
            return self.getTypedRuleContext(D96Parser.Block_statementContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_constructor_method

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitConstructor_method" ):
                return visitor.visitConstructor_method(self)
            else:
                return visitor.visitChildren(self)




    def constructor_method(self):

        localctx = D96Parser.Constructor_methodContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_constructor_method)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 139
            self.match(D96Parser.CONSTRUCTOR)
            self.state = 140
            self.match(D96Parser.LP)
            self.state = 141
            self.param_list()
            self.state = 142
            self.match(D96Parser.RP)
            self.state = 143
            self.block_statement()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Destructor_methodContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def DESTRUCTOR(self):
            return self.getToken(D96Parser.DESTRUCTOR, 0)

        def LP(self):
            return self.getToken(D96Parser.LP, 0)

        def RP(self):
            return self.getToken(D96Parser.RP, 0)

        def block_statement(self):
            return self.getTypedRuleContext(D96Parser.Block_statementContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_destructor_method

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDestructor_method" ):
                return visitor.visitDestructor_method(self)
            else:
                return visitor.visitChildren(self)




    def destructor_method(self):

        localctx = D96Parser.Destructor_methodContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_destructor_method)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 145
            self.match(D96Parser.DESTRUCTOR)
            self.state = 146
            self.match(D96Parser.LP)
            self.state = 147
            self.match(D96Parser.RP)
            self.state = 148
            self.block_statement()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class MethodContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LP(self):
            return self.getToken(D96Parser.LP, 0)

        def param_list(self):
            return self.getTypedRuleContext(D96Parser.Param_listContext,0)


        def RP(self):
            return self.getToken(D96Parser.RP, 0)

        def block_statement(self):
            return self.getTypedRuleContext(D96Parser.Block_statementContext,0)


        def NORMAL_ID(self):
            return self.getToken(D96Parser.NORMAL_ID, 0)

        def DOLLAR_ID(self):
            return self.getToken(D96Parser.DOLLAR_ID, 0)

        def getRuleIndex(self):
            return D96Parser.RULE_method

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMethod" ):
                return visitor.visitMethod(self)
            else:
                return visitor.visitChildren(self)




    def method(self):

        localctx = D96Parser.MethodContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_method)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 150
            _la = self._input.LA(1)
            if not(_la==D96Parser.NORMAL_ID or _la==D96Parser.DOLLAR_ID):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 151
            self.match(D96Parser.LP)
            self.state = 152
            self.param_list()
            self.state = 153
            self.match(D96Parser.RP)
            self.state = 154
            self.block_statement()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Param_listContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def parameter(self):
            return self.getTypedRuleContext(D96Parser.ParameterContext,0)


        def SEMI(self):
            return self.getToken(D96Parser.SEMI, 0)

        def param_list(self):
            return self.getTypedRuleContext(D96Parser.Param_listContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_param_list

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitParam_list" ):
                return visitor.visitParam_list(self)
            else:
                return visitor.visitChildren(self)




    def param_list(self):

        localctx = D96Parser.Param_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_param_list)
        try:
            self.state = 162
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,5,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 156
                self.parameter()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 157
                self.parameter()
                self.state = 158
                self.match(D96Parser.SEMI)
                self.state = 159
                self.param_list()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)

                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ParameterContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def COLON(self):
            return self.getToken(D96Parser.COLON, 0)

        def primitive_type(self):
            return self.getTypedRuleContext(D96Parser.Primitive_typeContext,0)


        def normal_id_list(self):
            return self.getTypedRuleContext(D96Parser.Normal_id_listContext,0)


        def dollar_id_list(self):
            return self.getTypedRuleContext(D96Parser.Dollar_id_listContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_parameter

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitParameter" ):
                return visitor.visitParameter(self)
            else:
                return visitor.visitChildren(self)




    def parameter(self):

        localctx = D96Parser.ParameterContext(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_parameter)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 166
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [D96Parser.NORMAL_ID]:
                self.state = 164
                self.normal_id_list()
                pass
            elif token in [D96Parser.DOLLAR_ID]:
                self.state = 165
                self.dollar_id_list()
                pass
            else:
                raise NoViableAltException(self)

            self.state = 168
            self.match(D96Parser.COLON)
            self.state = 169
            self.primitive_type()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Block_statementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LCB(self):
            return self.getToken(D96Parser.LCB, 0)

        def statement(self):
            return self.getTypedRuleContext(D96Parser.StatementContext,0)


        def RCB(self):
            return self.getToken(D96Parser.RCB, 0)

        def getRuleIndex(self):
            return D96Parser.RULE_block_statement

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBlock_statement" ):
                return visitor.visitBlock_statement(self)
            else:
                return visitor.visitChildren(self)




    def block_statement(self):

        localctx = D96Parser.Block_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 26, self.RULE_block_statement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 171
            self.match(D96Parser.LCB)
            self.state = 172
            self.statement()
            self.state = 173
            self.match(D96Parser.RCB)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def var_declare(self):
            return self.getTypedRuleContext(D96Parser.Var_declareContext,0)


        def assign_statement(self):
            return self.getTypedRuleContext(D96Parser.Assign_statementContext,0)


        def function_call(self):
            return self.getTypedRuleContext(D96Parser.Function_callContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_statement

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStatement" ):
                return visitor.visitStatement(self)
            else:
                return visitor.visitChildren(self)




    def statement(self):

        localctx = D96Parser.StatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 28, self.RULE_statement)
        try:
            self.state = 179
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,7,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 175
                self.var_declare()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 176
                self.assign_statement()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 177
                self.function_call()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)

                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Assign_statementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def lhs(self):
            return self.getTypedRuleContext(D96Parser.LhsContext,0)


        def ASSIGN(self):
            return self.getToken(D96Parser.ASSIGN, 0)

        def exp(self):
            return self.getTypedRuleContext(D96Parser.ExpContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_assign_statement

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAssign_statement" ):
                return visitor.visitAssign_statement(self)
            else:
                return visitor.visitChildren(self)




    def assign_statement(self):

        localctx = D96Parser.Assign_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 30, self.RULE_assign_statement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 181
            self.lhs()
            self.state = 182
            self.match(D96Parser.ASSIGN)
            self.state = 183
            self.exp()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class LhsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NORMAL_ID(self):
            return self.getToken(D96Parser.NORMAL_ID, 0)

        def DOLLAR_ID(self):
            return self.getToken(D96Parser.DOLLAR_ID, 0)

        def index(self):
            return self.getTypedRuleContext(D96Parser.IndexContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_lhs

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLhs" ):
                return visitor.visitLhs(self)
            else:
                return visitor.visitChildren(self)




    def lhs(self):

        localctx = D96Parser.LhsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 32, self.RULE_lhs)
        try:
            self.state = 188
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,8,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 185
                self.match(D96Parser.NORMAL_ID)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 186
                self.match(D96Parser.DOLLAR_ID)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 187
                self.index()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class IndexContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def index_operator(self):
            return self.getTypedRuleContext(D96Parser.Index_operatorContext,0)


        def NORMAL_ID(self):
            return self.getToken(D96Parser.NORMAL_ID, 0)

        def DOLLAR_ID(self):
            return self.getToken(D96Parser.DOLLAR_ID, 0)

        def getRuleIndex(self):
            return D96Parser.RULE_index

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIndex" ):
                return visitor.visitIndex(self)
            else:
                return visitor.visitChildren(self)




    def index(self):

        localctx = D96Parser.IndexContext(self, self._ctx, self.state)
        self.enterRule(localctx, 34, self.RULE_index)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 190
            _la = self._input.LA(1)
            if not(_la==D96Parser.NORMAL_ID or _la==D96Parser.DOLLAR_ID):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 191
            self.index_operator()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Function_callContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LP(self):
            return self.getToken(D96Parser.LP, 0)

        def RP(self):
            return self.getToken(D96Parser.RP, 0)

        def NORMAL_ID(self):
            return self.getToken(D96Parser.NORMAL_ID, 0)

        def DOLLAR_ID(self):
            return self.getToken(D96Parser.DOLLAR_ID, 0)

        def exp(self):
            return self.getTypedRuleContext(D96Parser.ExpContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_function_call

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFunction_call" ):
                return visitor.visitFunction_call(self)
            else:
                return visitor.visitChildren(self)




    def function_call(self):

        localctx = D96Parser.Function_callContext(self, self._ctx, self.state)
        self.enterRule(localctx, 36, self.RULE_function_call)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 193
            _la = self._input.LA(1)
            if not(_la==D96Parser.NORMAL_ID or _la==D96Parser.DOLLAR_ID):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 194
            self.match(D96Parser.LP)
            self.state = 196
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << D96Parser.BOOL_TYPE) | (1 << D96Parser.INTEGER_LITERAL) | (1 << D96Parser.STRING_LITERAL) | (1 << D96Parser.REAL_LITERAL) | (1 << D96Parser.LP) | (1 << D96Parser.ARRAY) | (1 << D96Parser.NEW) | (1 << D96Parser.SELF) | (1 << D96Parser.SUB) | (1 << D96Parser.NOT))) != 0) or _la==D96Parser.NORMAL_ID or _la==D96Parser.DOLLAR_ID:
                self.state = 195
                self.exp()


            self.state = 198
            self.match(D96Parser.RP)
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

        def COLON(self):
            return self.getToken(D96Parser.COLON, 0)

        def primitive_type(self):
            return self.getTypedRuleContext(D96Parser.Primitive_typeContext,0)


        def SEMI(self):
            return self.getToken(D96Parser.SEMI, 0)

        def VAR(self):
            return self.getToken(D96Parser.VAR, 0)

        def VAL(self):
            return self.getToken(D96Parser.VAL, 0)

        def normal_id_list(self):
            return self.getTypedRuleContext(D96Parser.Normal_id_listContext,0)


        def dollar_id_list(self):
            return self.getTypedRuleContext(D96Parser.Dollar_id_listContext,0)


        def init_value(self):
            return self.getTypedRuleContext(D96Parser.Init_valueContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_var_declare

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVar_declare" ):
                return visitor.visitVar_declare(self)
            else:
                return visitor.visitChildren(self)




    def var_declare(self):

        localctx = D96Parser.Var_declareContext(self, self._ctx, self.state)
        self.enterRule(localctx, 38, self.RULE_var_declare)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 200
            _la = self._input.LA(1)
            if not(_la==D96Parser.VAL or _la==D96Parser.VAR):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 203
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [D96Parser.NORMAL_ID]:
                self.state = 201
                self.normal_id_list()
                pass
            elif token in [D96Parser.DOLLAR_ID]:
                self.state = 202
                self.dollar_id_list()
                pass
            else:
                raise NoViableAltException(self)

            self.state = 205
            self.match(D96Parser.COLON)
            self.state = 206
            self.primitive_type()
            self.state = 208
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==D96Parser.ASSIGN:
                self.state = 207
                self.init_value()


            self.state = 210
            self.match(D96Parser.SEMI)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Init_valueContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ASSIGN(self):
            return self.getToken(D96Parser.ASSIGN, 0)

        def list_exp(self):
            return self.getTypedRuleContext(D96Parser.List_expContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_init_value

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitInit_value" ):
                return visitor.visitInit_value(self)
            else:
                return visitor.visitChildren(self)




    def init_value(self):

        localctx = D96Parser.Init_valueContext(self, self._ctx, self.state)
        self.enterRule(localctx, 40, self.RULE_init_value)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 212
            self.match(D96Parser.ASSIGN)
            self.state = 213
            self.list_exp()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Array_listContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ARRAY(self):
            return self.getToken(D96Parser.ARRAY, 0)

        def LP(self):
            return self.getToken(D96Parser.LP, 0)

        def literal_list(self):
            return self.getTypedRuleContext(D96Parser.Literal_listContext,0)


        def RP(self):
            return self.getToken(D96Parser.RP, 0)

        def getRuleIndex(self):
            return D96Parser.RULE_array_list

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArray_list" ):
                return visitor.visitArray_list(self)
            else:
                return visitor.visitChildren(self)




    def array_list(self):

        localctx = D96Parser.Array_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 42, self.RULE_array_list)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 215
            self.match(D96Parser.ARRAY)
            self.state = 216
            self.match(D96Parser.LP)
            self.state = 217
            self.literal_list()
            self.state = 218
            self.match(D96Parser.RP)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Literal_listContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def literal(self):
            return self.getTypedRuleContext(D96Parser.LiteralContext,0)


        def COMMA(self):
            return self.getToken(D96Parser.COMMA, 0)

        def literal_list(self):
            return self.getTypedRuleContext(D96Parser.Literal_listContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_literal_list

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLiteral_list" ):
                return visitor.visitLiteral_list(self)
            else:
                return visitor.visitChildren(self)




    def literal_list(self):

        localctx = D96Parser.Literal_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 44, self.RULE_literal_list)
        try:
            self.state = 226
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,12,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 220
                self.literal()
                self.state = 221
                self.match(D96Parser.COMMA)
                self.state = 222
                self.literal_list()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 224
                self.literal()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)

                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Array_typeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ARRAY(self):
            return self.getToken(D96Parser.ARRAY, 0)

        def LSB(self):
            return self.getToken(D96Parser.LSB, 0)

        def primitive_type(self):
            return self.getTypedRuleContext(D96Parser.Primitive_typeContext,0)


        def COMMA(self):
            return self.getToken(D96Parser.COMMA, 0)

        def INTEGER_LITERAL(self):
            return self.getToken(D96Parser.INTEGER_LITERAL, 0)

        def RSB(self):
            return self.getToken(D96Parser.RSB, 0)

        def getRuleIndex(self):
            return D96Parser.RULE_array_type

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArray_type" ):
                return visitor.visitArray_type(self)
            else:
                return visitor.visitChildren(self)




    def array_type(self):

        localctx = D96Parser.Array_typeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 46, self.RULE_array_type)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 228
            self.match(D96Parser.ARRAY)
            self.state = 229
            self.match(D96Parser.LSB)
            self.state = 230
            self.primitive_type()
            self.state = 231
            self.match(D96Parser.COMMA)
            self.state = 232
            self.match(D96Parser.INTEGER_LITERAL)
            self.state = 233
            self.match(D96Parser.RSB)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Primitive_typeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def BOOL_TYPE(self):
            return self.getToken(D96Parser.BOOL_TYPE, 0)

        def INT_TYPE(self):
            return self.getToken(D96Parser.INT_TYPE, 0)

        def FLOAT_TYPE(self):
            return self.getToken(D96Parser.FLOAT_TYPE, 0)

        def array_type(self):
            return self.getTypedRuleContext(D96Parser.Array_typeContext,0)


        def STRING(self):
            return self.getToken(D96Parser.STRING, 0)

        def CLASS(self):
            return self.getToken(D96Parser.CLASS, 0)

        def getRuleIndex(self):
            return D96Parser.RULE_primitive_type

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPrimitive_type" ):
                return visitor.visitPrimitive_type(self)
            else:
                return visitor.visitChildren(self)




    def primitive_type(self):

        localctx = D96Parser.Primitive_typeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 48, self.RULE_primitive_type)
        try:
            self.state = 241
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [D96Parser.BOOL_TYPE]:
                self.enterOuterAlt(localctx, 1)
                self.state = 235
                self.match(D96Parser.BOOL_TYPE)
                pass
            elif token in [D96Parser.INT_TYPE]:
                self.enterOuterAlt(localctx, 2)
                self.state = 236
                self.match(D96Parser.INT_TYPE)
                pass
            elif token in [D96Parser.FLOAT_TYPE]:
                self.enterOuterAlt(localctx, 3)
                self.state = 237
                self.match(D96Parser.FLOAT_TYPE)
                pass
            elif token in [D96Parser.ARRAY]:
                self.enterOuterAlt(localctx, 4)
                self.state = 238
                self.array_type()
                pass
            elif token in [D96Parser.STRING]:
                self.enterOuterAlt(localctx, 5)
                self.state = 239
                self.match(D96Parser.STRING)
                pass
            elif token in [D96Parser.CLASS]:
                self.enterOuterAlt(localctx, 6)
                self.state = 240
                self.match(D96Parser.CLASS)
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


    class LiteralContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def INTEGER_LITERAL(self):
            return self.getToken(D96Parser.INTEGER_LITERAL, 0)

        def BOOL_TYPE(self):
            return self.getToken(D96Parser.BOOL_TYPE, 0)

        def REAL_LITERAL(self):
            return self.getToken(D96Parser.REAL_LITERAL, 0)

        def STRING_LITERAL(self):
            return self.getToken(D96Parser.STRING_LITERAL, 0)

        def array_list(self):
            return self.getTypedRuleContext(D96Parser.Array_listContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_literal

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLiteral" ):
                return visitor.visitLiteral(self)
            else:
                return visitor.visitChildren(self)




    def literal(self):

        localctx = D96Parser.LiteralContext(self, self._ctx, self.state)
        self.enterRule(localctx, 50, self.RULE_literal)
        try:
            self.state = 248
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [D96Parser.INTEGER_LITERAL]:
                self.enterOuterAlt(localctx, 1)
                self.state = 243
                self.match(D96Parser.INTEGER_LITERAL)
                pass
            elif token in [D96Parser.BOOL_TYPE]:
                self.enterOuterAlt(localctx, 2)
                self.state = 244
                self.match(D96Parser.BOOL_TYPE)
                pass
            elif token in [D96Parser.REAL_LITERAL]:
                self.enterOuterAlt(localctx, 3)
                self.state = 245
                self.match(D96Parser.REAL_LITERAL)
                pass
            elif token in [D96Parser.STRING_LITERAL]:
                self.enterOuterAlt(localctx, 4)
                self.state = 246
                self.match(D96Parser.STRING_LITERAL)
                pass
            elif token in [D96Parser.ARRAY]:
                self.enterOuterAlt(localctx, 5)
                self.state = 247
                self.array_list()
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

        def STRING_LITERAL(self, i:int=None):
            if i is None:
                return self.getTokens(D96Parser.STRING_LITERAL)
            else:
                return self.getToken(D96Parser.STRING_LITERAL, i)

        def EQUAL_STR(self):
            return self.getToken(D96Parser.EQUAL_STR, 0)

        def ADD_STR(self):
            return self.getToken(D96Parser.ADD_STR, 0)

        def exp0(self):
            return self.getTypedRuleContext(D96Parser.Exp0Context,0)


        def getRuleIndex(self):
            return D96Parser.RULE_exp

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExp" ):
                return visitor.visitExp(self)
            else:
                return visitor.visitChildren(self)




    def exp(self):

        localctx = D96Parser.ExpContext(self, self._ctx, self.state)
        self.enterRule(localctx, 52, self.RULE_exp)
        try:
            self.state = 257
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,15,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 250
                self.match(D96Parser.STRING_LITERAL)
                self.state = 251
                self.match(D96Parser.EQUAL_STR)
                self.state = 252
                self.match(D96Parser.STRING_LITERAL)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 253
                self.match(D96Parser.STRING_LITERAL)
                self.state = 254
                self.match(D96Parser.ADD_STR)
                self.state = 255
                self.match(D96Parser.STRING_LITERAL)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 256
                self.exp0()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Exp0Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def exp1(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(D96Parser.Exp1Context)
            else:
                return self.getTypedRuleContext(D96Parser.Exp1Context,i)


        def LT(self):
            return self.getToken(D96Parser.LT, 0)

        def LTE(self):
            return self.getToken(D96Parser.LTE, 0)

        def GT(self):
            return self.getToken(D96Parser.GT, 0)

        def GTE(self):
            return self.getToken(D96Parser.GTE, 0)

        def EQUAL(self):
            return self.getToken(D96Parser.EQUAL, 0)

        def NOTEQUAL(self):
            return self.getToken(D96Parser.NOTEQUAL, 0)

        def getRuleIndex(self):
            return D96Parser.RULE_exp0

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExp0" ):
                return visitor.visitExp0(self)
            else:
                return visitor.visitChildren(self)




    def exp0(self):

        localctx = D96Parser.Exp0Context(self, self._ctx, self.state)
        self.enterRule(localctx, 54, self.RULE_exp0)
        try:
            self.state = 284
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,16,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 259
                self.exp1(0)
                self.state = 260
                self.match(D96Parser.LT)
                self.state = 261
                self.exp1(0)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 263
                self.exp1(0)
                self.state = 264
                self.match(D96Parser.LTE)
                self.state = 265
                self.exp1(0)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 267
                self.exp1(0)
                self.state = 268
                self.match(D96Parser.GT)
                self.state = 269
                self.exp1(0)
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 271
                self.exp1(0)
                self.state = 272
                self.match(D96Parser.GTE)
                self.state = 273
                self.exp1(0)
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 275
                self.exp1(0)
                self.state = 276
                self.match(D96Parser.EQUAL)
                self.state = 277
                self.exp1(0)
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 279
                self.exp1(0)
                self.state = 280
                self.match(D96Parser.NOTEQUAL)
                self.state = 281
                self.exp1(0)
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 283
                self.exp1(0)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Exp1Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def exp2(self):
            return self.getTypedRuleContext(D96Parser.Exp2Context,0)


        def exp1(self):
            return self.getTypedRuleContext(D96Parser.Exp1Context,0)


        def AND(self):
            return self.getToken(D96Parser.AND, 0)

        def OR(self):
            return self.getToken(D96Parser.OR, 0)

        def getRuleIndex(self):
            return D96Parser.RULE_exp1

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExp1" ):
                return visitor.visitExp1(self)
            else:
                return visitor.visitChildren(self)



    def exp1(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = D96Parser.Exp1Context(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 56
        self.enterRecursionRule(localctx, 56, self.RULE_exp1, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 287
            self.exp2(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 297
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,18,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 295
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,17,self._ctx)
                    if la_ == 1:
                        localctx = D96Parser.Exp1Context(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_exp1)
                        self.state = 289
                        if not self.precpred(self._ctx, 3):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 3)")
                        self.state = 290
                        self.match(D96Parser.AND)
                        self.state = 291
                        self.exp2(0)
                        pass

                    elif la_ == 2:
                        localctx = D96Parser.Exp1Context(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_exp1)
                        self.state = 292
                        if not self.precpred(self._ctx, 2):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                        self.state = 293
                        self.match(D96Parser.OR)
                        self.state = 294
                        self.exp2(0)
                        pass

             
                self.state = 299
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,18,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Exp2Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def exp3(self):
            return self.getTypedRuleContext(D96Parser.Exp3Context,0)


        def exp2(self):
            return self.getTypedRuleContext(D96Parser.Exp2Context,0)


        def ADD(self):
            return self.getToken(D96Parser.ADD, 0)

        def SUB(self):
            return self.getToken(D96Parser.SUB, 0)

        def getRuleIndex(self):
            return D96Parser.RULE_exp2

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExp2" ):
                return visitor.visitExp2(self)
            else:
                return visitor.visitChildren(self)



    def exp2(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = D96Parser.Exp2Context(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 58
        self.enterRecursionRule(localctx, 58, self.RULE_exp2, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 301
            self.exp3(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 311
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,20,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 309
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,19,self._ctx)
                    if la_ == 1:
                        localctx = D96Parser.Exp2Context(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_exp2)
                        self.state = 303
                        if not self.precpred(self._ctx, 3):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 3)")
                        self.state = 304
                        self.match(D96Parser.ADD)
                        self.state = 305
                        self.exp3(0)
                        pass

                    elif la_ == 2:
                        localctx = D96Parser.Exp2Context(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_exp2)
                        self.state = 306
                        if not self.precpred(self._ctx, 2):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                        self.state = 307
                        self.match(D96Parser.SUB)
                        self.state = 308
                        self.exp3(0)
                        pass

             
                self.state = 313
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,20,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Exp3Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def exp4(self):
            return self.getTypedRuleContext(D96Parser.Exp4Context,0)


        def exp3(self):
            return self.getTypedRuleContext(D96Parser.Exp3Context,0)


        def MUL(self):
            return self.getToken(D96Parser.MUL, 0)

        def DIV(self):
            return self.getToken(D96Parser.DIV, 0)

        def MOD(self):
            return self.getToken(D96Parser.MOD, 0)

        def getRuleIndex(self):
            return D96Parser.RULE_exp3

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExp3" ):
                return visitor.visitExp3(self)
            else:
                return visitor.visitChildren(self)



    def exp3(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = D96Parser.Exp3Context(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 60
        self.enterRecursionRule(localctx, 60, self.RULE_exp3, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 315
            self.exp4()
            self._ctx.stop = self._input.LT(-1)
            self.state = 328
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,22,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 326
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,21,self._ctx)
                    if la_ == 1:
                        localctx = D96Parser.Exp3Context(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_exp3)
                        self.state = 317
                        if not self.precpred(self._ctx, 4):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 4)")
                        self.state = 318
                        self.match(D96Parser.MUL)
                        self.state = 319
                        self.exp4()
                        pass

                    elif la_ == 2:
                        localctx = D96Parser.Exp3Context(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_exp3)
                        self.state = 320
                        if not self.precpred(self._ctx, 3):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 3)")
                        self.state = 321
                        self.match(D96Parser.DIV)
                        self.state = 322
                        self.exp4()
                        pass

                    elif la_ == 3:
                        localctx = D96Parser.Exp3Context(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_exp3)
                        self.state = 323
                        if not self.precpred(self._ctx, 2):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                        self.state = 324
                        self.match(D96Parser.MOD)
                        self.state = 325
                        self.exp4()
                        pass

             
                self.state = 330
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,22,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Exp4Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NOT(self):
            return self.getToken(D96Parser.NOT, 0)

        def exp4(self):
            return self.getTypedRuleContext(D96Parser.Exp4Context,0)


        def exp5(self):
            return self.getTypedRuleContext(D96Parser.Exp5Context,0)


        def getRuleIndex(self):
            return D96Parser.RULE_exp4

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExp4" ):
                return visitor.visitExp4(self)
            else:
                return visitor.visitChildren(self)




    def exp4(self):

        localctx = D96Parser.Exp4Context(self, self._ctx, self.state)
        self.enterRule(localctx, 62, self.RULE_exp4)
        try:
            self.state = 334
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [D96Parser.NOT]:
                self.enterOuterAlt(localctx, 1)
                self.state = 331
                self.match(D96Parser.NOT)
                self.state = 332
                self.exp4()
                pass
            elif token in [D96Parser.BOOL_TYPE, D96Parser.INTEGER_LITERAL, D96Parser.STRING_LITERAL, D96Parser.REAL_LITERAL, D96Parser.LP, D96Parser.ARRAY, D96Parser.NEW, D96Parser.SELF, D96Parser.SUB, D96Parser.NORMAL_ID, D96Parser.DOLLAR_ID]:
                self.enterOuterAlt(localctx, 2)
                self.state = 333
                self.exp5()
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


    class Exp5Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def SUB(self):
            return self.getToken(D96Parser.SUB, 0)

        def exp5(self):
            return self.getTypedRuleContext(D96Parser.Exp5Context,0)


        def exp6(self):
            return self.getTypedRuleContext(D96Parser.Exp6Context,0)


        def getRuleIndex(self):
            return D96Parser.RULE_exp5

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExp5" ):
                return visitor.visitExp5(self)
            else:
                return visitor.visitChildren(self)




    def exp5(self):

        localctx = D96Parser.Exp5Context(self, self._ctx, self.state)
        self.enterRule(localctx, 64, self.RULE_exp5)
        try:
            self.state = 339
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [D96Parser.SUB]:
                self.enterOuterAlt(localctx, 1)
                self.state = 336
                self.match(D96Parser.SUB)
                self.state = 337
                self.exp5()
                pass
            elif token in [D96Parser.BOOL_TYPE, D96Parser.INTEGER_LITERAL, D96Parser.STRING_LITERAL, D96Parser.REAL_LITERAL, D96Parser.LP, D96Parser.ARRAY, D96Parser.NEW, D96Parser.SELF, D96Parser.NORMAL_ID, D96Parser.DOLLAR_ID]:
                self.enterOuterAlt(localctx, 2)
                self.state = 338
                self.exp6()
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


    class Exp6Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def exp7(self):
            return self.getTypedRuleContext(D96Parser.Exp7Context,0)


        def index_operator(self):
            return self.getTypedRuleContext(D96Parser.Index_operatorContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_exp6

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExp6" ):
                return visitor.visitExp6(self)
            else:
                return visitor.visitChildren(self)




    def exp6(self):

        localctx = D96Parser.Exp6Context(self, self._ctx, self.state)
        self.enterRule(localctx, 66, self.RULE_exp6)
        try:
            self.state = 345
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,25,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 341
                self.exp7(0)
                self.state = 342
                self.index_operator()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 344
                self.exp7(0)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Index_operatorContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LSB(self):
            return self.getToken(D96Parser.LSB, 0)

        def exp(self):
            return self.getTypedRuleContext(D96Parser.ExpContext,0)


        def RSB(self):
            return self.getToken(D96Parser.RSB, 0)

        def index_operator(self):
            return self.getTypedRuleContext(D96Parser.Index_operatorContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_index_operator

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIndex_operator" ):
                return visitor.visitIndex_operator(self)
            else:
                return visitor.visitChildren(self)




    def index_operator(self):

        localctx = D96Parser.Index_operatorContext(self, self._ctx, self.state)
        self.enterRule(localctx, 68, self.RULE_index_operator)
        try:
            self.state = 356
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,26,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 347
                self.match(D96Parser.LSB)
                self.state = 348
                self.exp()
                self.state = 349
                self.match(D96Parser.RSB)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 351
                self.match(D96Parser.LSB)
                self.state = 352
                self.exp()
                self.state = 353
                self.match(D96Parser.RSB)
                self.state = 354
                self.index_operator()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Exp7Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def exp8(self):
            return self.getTypedRuleContext(D96Parser.Exp8Context,0)


        def exp7(self):
            return self.getTypedRuleContext(D96Parser.Exp7Context,0)


        def DOT(self):
            return self.getToken(D96Parser.DOT, 0)

        def NORMAL_ID(self):
            return self.getToken(D96Parser.NORMAL_ID, 0)

        def DOLLAR_ID(self):
            return self.getToken(D96Parser.DOLLAR_ID, 0)

        def LP(self):
            return self.getToken(D96Parser.LP, 0)

        def RP(self):
            return self.getToken(D96Parser.RP, 0)

        def list_exp(self):
            return self.getTypedRuleContext(D96Parser.List_expContext,0)


        def SCOPE(self):
            return self.getToken(D96Parser.SCOPE, 0)

        def getRuleIndex(self):
            return D96Parser.RULE_exp7

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExp7" ):
                return visitor.visitExp7(self)
            else:
                return visitor.visitChildren(self)



    def exp7(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = D96Parser.Exp7Context(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 70
        self.enterRecursionRule(localctx, 70, self.RULE_exp7, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 359
            self.exp8()
            self._ctx.stop = self._input.LT(-1)
            self.state = 383
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,32,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 381
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,31,self._ctx)
                    if la_ == 1:
                        localctx = D96Parser.Exp7Context(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_exp7)
                        self.state = 361
                        if not self.precpred(self._ctx, 3):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 3)")
                        self.state = 362
                        self.match(D96Parser.DOT)
                        self.state = 363
                        _la = self._input.LA(1)
                        if not(_la==D96Parser.NORMAL_ID or _la==D96Parser.DOLLAR_ID):
                            self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 369
                        self._errHandler.sync(self)
                        la_ = self._interp.adaptivePredict(self._input,28,self._ctx)
                        if la_ == 1:
                            self.state = 364
                            self.match(D96Parser.LP)
                            self.state = 366
                            self._errHandler.sync(self)
                            _la = self._input.LA(1)
                            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << D96Parser.BOOL_TYPE) | (1 << D96Parser.INTEGER_LITERAL) | (1 << D96Parser.STRING_LITERAL) | (1 << D96Parser.REAL_LITERAL) | (1 << D96Parser.LP) | (1 << D96Parser.ARRAY) | (1 << D96Parser.NEW) | (1 << D96Parser.SELF) | (1 << D96Parser.SUB) | (1 << D96Parser.NOT))) != 0) or _la==D96Parser.NORMAL_ID or _la==D96Parser.DOLLAR_ID:
                                self.state = 365
                                self.list_exp()


                            self.state = 368
                            self.match(D96Parser.RP)


                        pass

                    elif la_ == 2:
                        localctx = D96Parser.Exp7Context(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_exp7)
                        self.state = 371
                        if not self.precpred(self._ctx, 2):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                        self.state = 372
                        self.match(D96Parser.SCOPE)
                        self.state = 373
                        _la = self._input.LA(1)
                        if not(_la==D96Parser.NORMAL_ID or _la==D96Parser.DOLLAR_ID):
                            self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 379
                        self._errHandler.sync(self)
                        la_ = self._interp.adaptivePredict(self._input,30,self._ctx)
                        if la_ == 1:
                            self.state = 374
                            self.match(D96Parser.LP)
                            self.state = 376
                            self._errHandler.sync(self)
                            _la = self._input.LA(1)
                            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << D96Parser.BOOL_TYPE) | (1 << D96Parser.INTEGER_LITERAL) | (1 << D96Parser.STRING_LITERAL) | (1 << D96Parser.REAL_LITERAL) | (1 << D96Parser.LP) | (1 << D96Parser.ARRAY) | (1 << D96Parser.NEW) | (1 << D96Parser.SELF) | (1 << D96Parser.SUB) | (1 << D96Parser.NOT))) != 0) or _la==D96Parser.NORMAL_ID or _la==D96Parser.DOLLAR_ID:
                                self.state = 375
                                self.list_exp()


                            self.state = 378
                            self.match(D96Parser.RP)


                        pass

             
                self.state = 385
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,32,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Exp8Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NEW(self):
            return self.getToken(D96Parser.NEW, 0)

        def NORMAL_ID(self):
            return self.getToken(D96Parser.NORMAL_ID, 0)

        def LP(self):
            return self.getToken(D96Parser.LP, 0)

        def RP(self):
            return self.getToken(D96Parser.RP, 0)

        def list_exp(self):
            return self.getTypedRuleContext(D96Parser.List_expContext,0)


        def exp9(self):
            return self.getTypedRuleContext(D96Parser.Exp9Context,0)


        def getRuleIndex(self):
            return D96Parser.RULE_exp8

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExp8" ):
                return visitor.visitExp8(self)
            else:
                return visitor.visitChildren(self)




    def exp8(self):

        localctx = D96Parser.Exp8Context(self, self._ctx, self.state)
        self.enterRule(localctx, 72, self.RULE_exp8)
        self._la = 0 # Token type
        try:
            self.state = 394
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [D96Parser.NEW]:
                self.enterOuterAlt(localctx, 1)
                self.state = 386
                self.match(D96Parser.NEW)
                self.state = 387
                self.match(D96Parser.NORMAL_ID)
                self.state = 388
                self.match(D96Parser.LP)
                self.state = 390
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << D96Parser.BOOL_TYPE) | (1 << D96Parser.INTEGER_LITERAL) | (1 << D96Parser.STRING_LITERAL) | (1 << D96Parser.REAL_LITERAL) | (1 << D96Parser.LP) | (1 << D96Parser.ARRAY) | (1 << D96Parser.NEW) | (1 << D96Parser.SELF) | (1 << D96Parser.SUB) | (1 << D96Parser.NOT))) != 0) or _la==D96Parser.NORMAL_ID or _la==D96Parser.DOLLAR_ID:
                    self.state = 389
                    self.list_exp()


                self.state = 392
                self.match(D96Parser.RP)
                pass
            elif token in [D96Parser.BOOL_TYPE, D96Parser.INTEGER_LITERAL, D96Parser.STRING_LITERAL, D96Parser.REAL_LITERAL, D96Parser.LP, D96Parser.ARRAY, D96Parser.SELF, D96Parser.NORMAL_ID, D96Parser.DOLLAR_ID]:
                self.enterOuterAlt(localctx, 2)
                self.state = 393
                self.exp9()
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


    class Exp9Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def literal(self):
            return self.getTypedRuleContext(D96Parser.LiteralContext,0)


        def NORMAL_ID(self):
            return self.getToken(D96Parser.NORMAL_ID, 0)

        def DOLLAR_ID(self):
            return self.getToken(D96Parser.DOLLAR_ID, 0)

        def SELF(self):
            return self.getToken(D96Parser.SELF, 0)

        def exp10(self):
            return self.getTypedRuleContext(D96Parser.Exp10Context,0)


        def getRuleIndex(self):
            return D96Parser.RULE_exp9

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExp9" ):
                return visitor.visitExp9(self)
            else:
                return visitor.visitChildren(self)




    def exp9(self):

        localctx = D96Parser.Exp9Context(self, self._ctx, self.state)
        self.enterRule(localctx, 74, self.RULE_exp9)
        try:
            self.state = 401
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [D96Parser.BOOL_TYPE, D96Parser.INTEGER_LITERAL, D96Parser.STRING_LITERAL, D96Parser.REAL_LITERAL, D96Parser.ARRAY]:
                self.enterOuterAlt(localctx, 1)
                self.state = 396
                self.literal()
                pass
            elif token in [D96Parser.NORMAL_ID]:
                self.enterOuterAlt(localctx, 2)
                self.state = 397
                self.match(D96Parser.NORMAL_ID)
                pass
            elif token in [D96Parser.DOLLAR_ID]:
                self.enterOuterAlt(localctx, 3)
                self.state = 398
                self.match(D96Parser.DOLLAR_ID)
                pass
            elif token in [D96Parser.SELF]:
                self.enterOuterAlt(localctx, 4)
                self.state = 399
                self.match(D96Parser.SELF)
                pass
            elif token in [D96Parser.LP]:
                self.enterOuterAlt(localctx, 5)
                self.state = 400
                self.exp10()
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


    class Exp10Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LP(self):
            return self.getToken(D96Parser.LP, 0)

        def exp(self):
            return self.getTypedRuleContext(D96Parser.ExpContext,0)


        def RP(self):
            return self.getToken(D96Parser.RP, 0)

        def getRuleIndex(self):
            return D96Parser.RULE_exp10

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExp10" ):
                return visitor.visitExp10(self)
            else:
                return visitor.visitChildren(self)




    def exp10(self):

        localctx = D96Parser.Exp10Context(self, self._ctx, self.state)
        self.enterRule(localctx, 76, self.RULE_exp10)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 403
            self.match(D96Parser.LP)
            self.state = 404
            self.exp()
            self.state = 405
            self.match(D96Parser.RP)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class List_expContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def exp(self):
            return self.getTypedRuleContext(D96Parser.ExpContext,0)


        def COMMA(self):
            return self.getToken(D96Parser.COMMA, 0)

        def list_exp(self):
            return self.getTypedRuleContext(D96Parser.List_expContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_list_exp

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitList_exp" ):
                return visitor.visitList_exp(self)
            else:
                return visitor.visitChildren(self)




    def list_exp(self):

        localctx = D96Parser.List_expContext(self, self._ctx, self.state)
        self.enterRule(localctx, 78, self.RULE_list_exp)
        try:
            self.state = 412
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,36,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 407
                self.exp()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 408
                self.exp()
                self.state = 409
                self.match(D96Parser.COMMA)
                self.state = 410
                self.list_exp()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Normal_id_listContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NORMAL_ID(self):
            return self.getToken(D96Parser.NORMAL_ID, 0)

        def COMMA(self):
            return self.getToken(D96Parser.COMMA, 0)

        def normal_id_list(self):
            return self.getTypedRuleContext(D96Parser.Normal_id_listContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_normal_id_list

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitNormal_id_list" ):
                return visitor.visitNormal_id_list(self)
            else:
                return visitor.visitChildren(self)




    def normal_id_list(self):

        localctx = D96Parser.Normal_id_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 80, self.RULE_normal_id_list)
        try:
            self.state = 418
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,37,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 414
                self.match(D96Parser.NORMAL_ID)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 415
                self.match(D96Parser.NORMAL_ID)
                self.state = 416
                self.match(D96Parser.COMMA)
                self.state = 417
                self.normal_id_list()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Dollar_id_listContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def DOLLAR_ID(self):
            return self.getToken(D96Parser.DOLLAR_ID, 0)

        def COMMA(self):
            return self.getToken(D96Parser.COMMA, 0)

        def dollar_id_list(self):
            return self.getTypedRuleContext(D96Parser.Dollar_id_listContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_dollar_id_list

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDollar_id_list" ):
                return visitor.visitDollar_id_list(self)
            else:
                return visitor.visitChildren(self)




    def dollar_id_list(self):

        localctx = D96Parser.Dollar_id_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 82, self.RULE_dollar_id_list)
        try:
            self.state = 424
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,38,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 420
                self.match(D96Parser.DOLLAR_ID)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 421
                self.match(D96Parser.DOLLAR_ID)
                self.state = 422
                self.match(D96Parser.COMMA)
                self.state = 423
                self.dollar_id_list()
                pass


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
        self._predicates[28] = self.exp1_sempred
        self._predicates[29] = self.exp2_sempred
        self._predicates[30] = self.exp3_sempred
        self._predicates[35] = self.exp7_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def exp1_sempred(self, localctx:Exp1Context, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 3)
         

            if predIndex == 1:
                return self.precpred(self._ctx, 2)
         

    def exp2_sempred(self, localctx:Exp2Context, predIndex:int):
            if predIndex == 2:
                return self.precpred(self._ctx, 3)
         

            if predIndex == 3:
                return self.precpred(self._ctx, 2)
         

    def exp3_sempred(self, localctx:Exp3Context, predIndex:int):
            if predIndex == 4:
                return self.precpred(self._ctx, 4)
         

            if predIndex == 5:
                return self.precpred(self._ctx, 3)
         

            if predIndex == 6:
                return self.precpred(self._ctx, 2)
         

    def exp7_sempred(self, localctx:Exp7Context, predIndex:int):
            if predIndex == 7:
                return self.precpred(self._ctx, 3)
         

            if predIndex == 8:
                return self.precpred(self._ctx, 2)
         




