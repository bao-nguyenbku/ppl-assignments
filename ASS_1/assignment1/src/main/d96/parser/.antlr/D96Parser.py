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
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3H")
        buf.write("\u01b4\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
        buf.write("\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r\4\16")
        buf.write("\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23\t\23")
        buf.write("\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30\4\31")
        buf.write("\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36\t\36")
        buf.write("\4\37\t\37\4 \t \4!\t!\4\"\t\"\4#\t#\4$\t$\4%\t%\4&\t")
        buf.write("&\4\'\t\'\4(\t(\4)\t)\4*\t*\4+\t+\4,\t,\3\2\3\2\6\2[\n")
        buf.write("\2\r\2\16\2\\\3\2\3\2\3\3\3\3\3\3\3\3\3\3\3\3\3\4\3\4")
        buf.write("\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3")
        buf.write("\4\5\4w\n\4\3\5\3\5\3\5\5\5|\n\5\3\6\3\6\3\6\3\6\3\6\3")
        buf.write("\6\3\6\3\7\3\7\3\7\5\7\u0088\n\7\3\b\3\b\3\b\3\b\3\b\5")
        buf.write("\b\u008f\n\b\3\t\3\t\5\t\u0093\n\t\3\n\3\n\3\n\3\n\3\n")
        buf.write("\3\n\3\13\3\13\3\13\3\13\3\13\3\f\3\f\3\f\3\f\3\f\3\f")
        buf.write("\3\r\3\r\3\r\3\r\3\r\3\r\5\r\u00ac\n\r\3\16\3\16\5\16")
        buf.write("\u00b0\n\16\3\16\3\16\3\16\3\17\3\17\3\17\3\17\3\20\3")
        buf.write("\20\3\20\3\20\5\20\u00bd\n\20\3\21\3\21\3\21\3\21\3\21")
        buf.write("\3\22\3\22\3\23\3\23\3\23\5\23\u00c9\n\23\3\24\3\24\3")
        buf.write("\24\3\25\3\25\3\25\5\25\u00d1\n\25\3\25\3\25\3\26\3\26")
        buf.write("\3\26\5\26\u00d8\n\26\3\26\3\26\3\26\5\26\u00dd\n\26\3")
        buf.write("\26\3\26\3\27\3\27\3\27\3\30\3\30\3\30\3\30\3\30\3\31")
        buf.write("\3\31\3\31\3\31\3\31\3\31\5\31\u00ef\n\31\3\32\3\32\3")
        buf.write("\32\3\32\3\32\3\32\3\32\3\33\3\33\3\33\3\33\3\33\3\33")
        buf.write("\5\33\u00fe\n\33\3\34\3\34\3\34\3\34\3\34\5\34\u0105\n")
        buf.write("\34\3\35\3\35\3\35\3\35\3\35\3\35\3\35\5\35\u010e\n\35")
        buf.write("\3\36\3\36\3\36\3\36\3\36\3\36\3\36\3\36\3\36\3\36\3\36")
        buf.write("\3\36\3\36\3\36\3\36\3\36\3\36\3\36\3\36\3\36\3\36\3\36")
        buf.write("\3\36\3\36\3\36\5\36\u0129\n\36\3\37\3\37\3\37\3\37\3")
        buf.write("\37\3\37\3\37\3\37\3\37\7\37\u0134\n\37\f\37\16\37\u0137")
        buf.write("\13\37\3 \3 \3 \3 \3 \3 \3 \3 \3 \7 \u0142\n \f \16 \u0145")
        buf.write("\13 \3!\3!\3!\3!\3!\3!\3!\3!\3!\3!\3!\3!\7!\u0153\n!\f")
        buf.write("!\16!\u0156\13!\3\"\3\"\3\"\5\"\u015b\n\"\3#\3#\3#\5#")
        buf.write("\u0160\n#\3$\3$\3$\3$\5$\u0166\n$\3%\3%\3%\3%\3%\3%\3")
        buf.write("%\3%\3%\5%\u0171\n%\3&\3&\3&\3&\3&\3&\3&\3&\3&\3&\5&\u017d")
        buf.write("\n&\3&\3&\3&\3&\3&\3&\3&\5&\u0186\n&\7&\u0188\n&\f&\16")
        buf.write("&\u018b\13&\3\'\3\'\3\'\3\'\3\'\3\'\3\'\5\'\u0194\n\'")
        buf.write("\3(\3(\3(\3(\3(\5(\u019b\n(\3)\3)\3)\3)\3*\3*\3*\3*\3")
        buf.write("*\5*\u01a6\n*\3+\3+\3+\3+\5+\u01ac\n+\3,\3,\3,\3,\5,\u01b2")
        buf.write("\n,\3,\2\6<>@J-\2\4\6\b\n\f\16\20\22\24\26\30\32\34\36")
        buf.write(" \"$&(*,.\60\62\64\668:<>@BDFHJLNPRTV\2\4\3\2DE\3\2\22")
        buf.write("\23\2\u01c6\2Z\3\2\2\2\4`\3\2\2\2\6v\3\2\2\2\b{\3\2\2")
        buf.write("\2\n}\3\2\2\2\f\u0087\3\2\2\2\16\u008e\3\2\2\2\20\u0092")
        buf.write("\3\2\2\2\22\u0094\3\2\2\2\24\u009a\3\2\2\2\26\u009f\3")
        buf.write("\2\2\2\30\u00ab\3\2\2\2\32\u00af\3\2\2\2\34\u00b4\3\2")
        buf.write("\2\2\36\u00bc\3\2\2\2 \u00be\3\2\2\2\"\u00c3\3\2\2\2$")
        buf.write("\u00c8\3\2\2\2&\u00ca\3\2\2\2(\u00cd\3\2\2\2*\u00d4\3")
        buf.write("\2\2\2,\u00e0\3\2\2\2.\u00e3\3\2\2\2\60\u00ee\3\2\2\2")
        buf.write("\62\u00f0\3\2\2\2\64\u00fd\3\2\2\2\66\u0104\3\2\2\28\u010d")
        buf.write("\3\2\2\2:\u0128\3\2\2\2<\u012a\3\2\2\2>\u0138\3\2\2\2")
        buf.write("@\u0146\3\2\2\2B\u015a\3\2\2\2D\u015f\3\2\2\2F\u0165\3")
        buf.write("\2\2\2H\u0170\3\2\2\2J\u0172\3\2\2\2L\u0193\3\2\2\2N\u019a")
        buf.write("\3\2\2\2P\u019c\3\2\2\2R\u01a5\3\2\2\2T\u01ab\3\2\2\2")
        buf.write("V\u01b1\3\2\2\2X[\5R*\2Y[\5*\26\2ZX\3\2\2\2ZY\3\2\2\2")
        buf.write("[\\\3\2\2\2\\Z\3\2\2\2\\]\3\2\2\2]^\3\2\2\2^_\7\2\2\3")
        buf.write("_\3\3\2\2\2`a\7\35\2\2ab\7\3\2\2bc\7\26\2\2cd\5\6\4\2")
        buf.write("de\7\27\2\2e\5\3\2\2\2fg\7\4\2\2gh\7\24\2\2hi\7\25\2\2")
        buf.write("ij\7\26\2\2jk\5\b\5\2kl\7\27\2\2lw\3\2\2\2mn\5\16\b\2")
        buf.write("no\7\4\2\2op\7\24\2\2pq\7\25\2\2qr\7\26\2\2rs\5\b\5\2")
        buf.write("st\7\27\2\2tu\5\16\b\2uw\3\2\2\2vf\3\2\2\2vm\3\2\2\2w")
        buf.write("\7\3\2\2\2x|\5*\26\2y|\5(\25\2z|\3\2\2\2{x\3\2\2\2{y\3")
        buf.write("\2\2\2{z\3\2\2\2|\t\3\2\2\2}~\7\35\2\2~\177\7D\2\2\177")
        buf.write("\u0080\5\f\7\2\u0080\u0081\7\26\2\2\u0081\u0082\5\16\b")
        buf.write("\2\u0082\u0083\7\27\2\2\u0083\13\3\2\2\2\u0084\u0085\7")
        buf.write("\34\2\2\u0085\u0088\7D\2\2\u0086\u0088\3\2\2\2\u0087\u0084")
        buf.write("\3\2\2\2\u0087\u0086\3\2\2\2\u0088\r\3\2\2\2\u0089\u008f")
        buf.write("\5\20\t\2\u008a\u008b\5\20\t\2\u008b\u008c\5\16\b\2\u008c")
        buf.write("\u008f\3\2\2\2\u008d\u008f\3\2\2\2\u008e\u0089\3\2\2\2")
        buf.write("\u008e\u008a\3\2\2\2\u008e\u008d\3\2\2\2\u008f\17\3\2")
        buf.write("\2\2\u0090\u0093\5*\26\2\u0091\u0093\5\26\f\2\u0092\u0090")
        buf.write("\3\2\2\2\u0092\u0091\3\2\2\2\u0093\21\3\2\2\2\u0094\u0095")
        buf.write("\7+\2\2\u0095\u0096\7\24\2\2\u0096\u0097\5\30\r\2\u0097")
        buf.write("\u0098\7\25\2\2\u0098\u0099\5\34\17\2\u0099\23\3\2\2\2")
        buf.write("\u009a\u009b\7,\2\2\u009b\u009c\7\24\2\2\u009c\u009d\7")
        buf.write("\25\2\2\u009d\u009e\5\34\17\2\u009e\25\3\2\2\2\u009f\u00a0")
        buf.write("\t\2\2\2\u00a0\u00a1\7\24\2\2\u00a1\u00a2\5\30\r\2\u00a2")
        buf.write("\u00a3\7\25\2\2\u00a3\u00a4\5\34\17\2\u00a4\27\3\2\2\2")
        buf.write("\u00a5\u00ac\5\32\16\2\u00a6\u00a7\5\32\16\2\u00a7\u00a8")
        buf.write("\7\32\2\2\u00a8\u00a9\5\30\r\2\u00a9\u00ac\3\2\2\2\u00aa")
        buf.write("\u00ac\3\2\2\2\u00ab\u00a5\3\2\2\2\u00ab\u00a6\3\2\2\2")
        buf.write("\u00ab\u00aa\3\2\2\2\u00ac\31\3\2\2\2\u00ad\u00b0\5T+")
        buf.write("\2\u00ae\u00b0\5V,\2\u00af\u00ad\3\2\2\2\u00af\u00ae\3")
        buf.write("\2\2\2\u00b0\u00b1\3\2\2\2\u00b1\u00b2\7\34\2\2\u00b2")
        buf.write("\u00b3\5\64\33\2\u00b3\33\3\2\2\2\u00b4\u00b5\7\26\2\2")
        buf.write("\u00b5\u00b6\5\36\20\2\u00b6\u00b7\7\27\2\2\u00b7\35\3")
        buf.write("\2\2\2\u00b8\u00bd\5*\26\2\u00b9\u00bd\5 \21\2\u00ba\u00bd")
        buf.write("\5(\25\2\u00bb\u00bd\3\2\2\2\u00bc\u00b8\3\2\2\2\u00bc")
        buf.write("\u00b9\3\2\2\2\u00bc\u00ba\3\2\2\2\u00bc\u00bb\3\2\2\2")
        buf.write("\u00bd\37\3\2\2\2\u00be\u00bf\5$\23\2\u00bf\u00c0\79\2")
        buf.write("\2\u00c0\u00c1\58\35\2\u00c1\u00c2\7\32\2\2\u00c2!\3\2")
        buf.write("\2\2\u00c3\u00c4\3\2\2\2\u00c4#\3\2\2\2\u00c5\u00c9\7")
        buf.write("D\2\2\u00c6\u00c9\7E\2\2\u00c7\u00c9\5&\24\2\u00c8\u00c5")
        buf.write("\3\2\2\2\u00c8\u00c6\3\2\2\2\u00c8\u00c7\3\2\2\2\u00c9")
        buf.write("%\3\2\2\2\u00ca\u00cb\t\2\2\2\u00cb\u00cc\5H%\2\u00cc")
        buf.write("\'\3\2\2\2\u00cd\u00ce\t\2\2\2\u00ce\u00d0\7\24\2\2\u00cf")
        buf.write("\u00d1\58\35\2\u00d0\u00cf\3\2\2\2\u00d0\u00d1\3\2\2\2")
        buf.write("\u00d1\u00d2\3\2\2\2\u00d2\u00d3\7\25\2\2\u00d3)\3\2\2")
        buf.write("\2\u00d4\u00d7\t\3\2\2\u00d5\u00d8\5T+\2\u00d6\u00d8\5")
        buf.write("V,\2\u00d7\u00d5\3\2\2\2\u00d7\u00d6\3\2\2\2\u00d8\u00d9")
        buf.write("\3\2\2\2\u00d9\u00da\7\34\2\2\u00da\u00dc\5\64\33\2\u00db")
        buf.write("\u00dd\5,\27\2\u00dc\u00db\3\2\2\2\u00dc\u00dd\3\2\2\2")
        buf.write("\u00dd\u00de\3\2\2\2\u00de\u00df\7\32\2\2\u00df+\3\2\2")
        buf.write("\2\u00e0\u00e1\79\2\2\u00e1\u00e2\5R*\2\u00e2-\3\2\2\2")
        buf.write("\u00e3\u00e4\7&\2\2\u00e4\u00e5\7\24\2\2\u00e5\u00e6\5")
        buf.write("\60\31\2\u00e6\u00e7\7\25\2\2\u00e7/\3\2\2\2\u00e8\u00e9")
        buf.write("\5\66\34\2\u00e9\u00ea\7\33\2\2\u00ea\u00eb\5\60\31\2")
        buf.write("\u00eb\u00ef\3\2\2\2\u00ec\u00ef\5\66\34\2\u00ed\u00ef")
        buf.write("\3\2\2\2\u00ee\u00e8\3\2\2\2\u00ee\u00ec\3\2\2\2\u00ee")
        buf.write("\u00ed\3\2\2\2\u00ef\61\3\2\2\2\u00f0\u00f1\7&\2\2\u00f1")
        buf.write("\u00f2\7\30\2\2\u00f2\u00f3\5\64\33\2\u00f3\u00f4\7\33")
        buf.write("\2\2\u00f4\u00f5\7\t\2\2\u00f5\u00f6\7\31\2\2\u00f6\63")
        buf.write("\3\2\2\2\u00f7\u00fe\7\5\2\2\u00f8\u00fe\7\b\2\2\u00f9")
        buf.write("\u00fe\7\6\2\2\u00fa\u00fe\5\62\32\2\u00fb\u00fe\7\7\2")
        buf.write("\2\u00fc\u00fe\7\35\2\2\u00fd\u00f7\3\2\2\2\u00fd\u00f8")
        buf.write("\3\2\2\2\u00fd\u00f9\3\2\2\2\u00fd\u00fa\3\2\2\2\u00fd")
        buf.write("\u00fb\3\2\2\2\u00fd\u00fc\3\2\2\2\u00fe\65\3\2\2\2\u00ff")
        buf.write("\u0105\7\t\2\2\u0100\u0105\7\5\2\2\u0101\u0105\7\21\2")
        buf.write("\2\u0102\u0105\7\16\2\2\u0103\u0105\5.\30\2\u0104\u00ff")
        buf.write("\3\2\2\2\u0104\u0100\3\2\2\2\u0104\u0101\3\2\2\2\u0104")
        buf.write("\u0102\3\2\2\2\u0104\u0103\3\2\2\2\u0105\67\3\2\2\2\u0106")
        buf.write("\u0107\7\16\2\2\u0107\u0108\7?\2\2\u0108\u010e\7\16\2")
        buf.write("\2\u0109\u010a\7\16\2\2\u010a\u010b\7@\2\2\u010b\u010e")
        buf.write("\7\16\2\2\u010c\u010e\5:\36\2\u010d\u0106\3\2\2\2\u010d")
        buf.write("\u0109\3\2\2\2\u010d\u010c\3\2\2\2\u010e9\3\2\2\2\u010f")
        buf.write("\u0110\5<\37\2\u0110\u0111\7=\2\2\u0111\u0112\5<\37\2")
        buf.write("\u0112\u0129\3\2\2\2\u0113\u0114\5<\37\2\u0114\u0115\7")
        buf.write(">\2\2\u0115\u0116\5<\37\2\u0116\u0129\3\2\2\2\u0117\u0118")
        buf.write("\5<\37\2\u0118\u0119\7;\2\2\u0119\u011a\5<\37\2\u011a")
        buf.write("\u0129\3\2\2\2\u011b\u011c\5<\37\2\u011c\u011d\7<\2\2")
        buf.write("\u011d\u011e\5<\37\2\u011e\u0129\3\2\2\2\u011f\u0120\5")
        buf.write("<\37\2\u0120\u0121\78\2\2\u0121\u0122\5<\37\2\u0122\u0129")
        buf.write("\3\2\2\2\u0123\u0124\5<\37\2\u0124\u0125\7:\2\2\u0125")
        buf.write("\u0126\5<\37\2\u0126\u0129\3\2\2\2\u0127\u0129\5<\37\2")
        buf.write("\u0128\u010f\3\2\2\2\u0128\u0113\3\2\2\2\u0128\u0117\3")
        buf.write("\2\2\2\u0128\u011b\3\2\2\2\u0128\u011f\3\2\2\2\u0128\u0123")
        buf.write("\3\2\2\2\u0128\u0127\3\2\2\2\u0129;\3\2\2\2\u012a\u012b")
        buf.write("\b\37\1\2\u012b\u012c\5> \2\u012c\u0135\3\2\2\2\u012d")
        buf.write("\u012e\f\5\2\2\u012e\u012f\7\66\2\2\u012f\u0134\5> \2")
        buf.write("\u0130\u0131\f\4\2\2\u0131\u0132\7\67\2\2\u0132\u0134")
        buf.write("\5> \2\u0133\u012d\3\2\2\2\u0133\u0130\3\2\2\2\u0134\u0137")
        buf.write("\3\2\2\2\u0135\u0133\3\2\2\2\u0135\u0136\3\2\2\2\u0136")
        buf.write("=\3\2\2\2\u0137\u0135\3\2\2\2\u0138\u0139\b \1\2\u0139")
        buf.write("\u013a\5@!\2\u013a\u0143\3\2\2\2\u013b\u013c\f\5\2\2\u013c")
        buf.write("\u013d\7\60\2\2\u013d\u0142\5@!\2\u013e\u013f\f\4\2\2")
        buf.write("\u013f\u0140\7\61\2\2\u0140\u0142\5@!\2\u0141\u013b\3")
        buf.write("\2\2\2\u0141\u013e\3\2\2\2\u0142\u0145\3\2\2\2\u0143\u0141")
        buf.write("\3\2\2\2\u0143\u0144\3\2\2\2\u0144?\3\2\2\2\u0145\u0143")
        buf.write("\3\2\2\2\u0146\u0147\b!\1\2\u0147\u0148\5B\"\2\u0148\u0154")
        buf.write("\3\2\2\2\u0149\u014a\f\6\2\2\u014a\u014b\7\62\2\2\u014b")
        buf.write("\u0153\5B\"\2\u014c\u014d\f\5\2\2\u014d\u014e\7\63\2\2")
        buf.write("\u014e\u0153\5B\"\2\u014f\u0150\f\4\2\2\u0150\u0151\7")
        buf.write("\64\2\2\u0151\u0153\5B\"\2\u0152\u0149\3\2\2\2\u0152\u014c")
        buf.write("\3\2\2\2\u0152\u014f\3\2\2\2\u0153\u0156\3\2\2\2\u0154")
        buf.write("\u0152\3\2\2\2\u0154\u0155\3\2\2\2\u0155A\3\2\2\2\u0156")
        buf.write("\u0154\3\2\2\2\u0157\u0158\7\65\2\2\u0158\u015b\5B\"\2")
        buf.write("\u0159\u015b\5D#\2\u015a\u0157\3\2\2\2\u015a\u0159\3\2")
        buf.write("\2\2\u015bC\3\2\2\2\u015c\u015d\7\61\2\2\u015d\u0160\5")
        buf.write("D#\2\u015e\u0160\5F$\2\u015f\u015c\3\2\2\2\u015f\u015e")
        buf.write("\3\2\2\2\u0160E\3\2\2\2\u0161\u0162\5J&\2\u0162\u0163")
        buf.write("\5H%\2\u0163\u0166\3\2\2\2\u0164\u0166\5J&\2\u0165\u0161")
        buf.write("\3\2\2\2\u0165\u0164\3\2\2\2\u0166G\3\2\2\2\u0167\u0168")
        buf.write("\7\30\2\2\u0168\u0169\58\35\2\u0169\u016a\7\31\2\2\u016a")
        buf.write("\u0171\3\2\2\2\u016b\u016c\7\30\2\2\u016c\u016d\58\35")
        buf.write("\2\u016d\u016e\7\31\2\2\u016e\u016f\5H%\2\u016f\u0171")
        buf.write("\3\2\2\2\u0170\u0167\3\2\2\2\u0170\u016b\3\2\2\2\u0171")
        buf.write("I\3\2\2\2\u0172\u0173\b&\1\2\u0173\u0174\5L\'\2\u0174")
        buf.write("\u0189\3\2\2\2\u0175\u0176\f\5\2\2\u0176\u0177\7A\2\2")
        buf.write("\u0177\u017c\t\2\2\2\u0178\u0179\7\24\2\2\u0179\u017a")
        buf.write("\5R*\2\u017a\u017b\7\25\2\2\u017b\u017d\3\2\2\2\u017c")
        buf.write("\u0178\3\2\2\2\u017c\u017d\3\2\2\2\u017d\u0188\3\2\2\2")
        buf.write("\u017e\u017f\f\4\2\2\u017f\u0180\7C\2\2\u0180\u0185\t")
        buf.write("\2\2\2\u0181\u0182\7\24\2\2\u0182\u0183\5R*\2\u0183\u0184")
        buf.write("\7\25\2\2\u0184\u0186\3\2\2\2\u0185\u0181\3\2\2\2\u0185")
        buf.write("\u0186\3\2\2\2\u0186\u0188\3\2\2\2\u0187\u0175\3\2\2\2")
        buf.write("\u0187\u017e\3\2\2\2\u0188\u018b\3\2\2\2\u0189\u0187\3")
        buf.write("\2\2\2\u0189\u018a\3\2\2\2\u018aK\3\2\2\2\u018b\u0189")
        buf.write("\3\2\2\2\u018c\u018d\7-\2\2\u018d\u018e\7D\2\2\u018e\u018f")
        buf.write("\7\24\2\2\u018f\u0190\5R*\2\u0190\u0191\7\25\2\2\u0191")
        buf.write("\u0194\3\2\2\2\u0192\u0194\5N(\2\u0193\u018c\3\2\2\2\u0193")
        buf.write("\u0192\3\2\2\2\u0194M\3\2\2\2\u0195\u019b\5\66\34\2\u0196")
        buf.write("\u019b\7D\2\2\u0197\u019b\7E\2\2\u0198\u019b\7/\2\2\u0199")
        buf.write("\u019b\5P)\2\u019a\u0195\3\2\2\2\u019a\u0196\3\2\2\2\u019a")
        buf.write("\u0197\3\2\2\2\u019a\u0198\3\2\2\2\u019a\u0199\3\2\2\2")
        buf.write("\u019bO\3\2\2\2\u019c\u019d\7\24\2\2\u019d\u019e\58\35")
        buf.write("\2\u019e\u019f\7\25\2\2\u019fQ\3\2\2\2\u01a0\u01a6\58")
        buf.write("\35\2\u01a1\u01a2\58\35\2\u01a2\u01a3\7\33\2\2\u01a3\u01a4")
        buf.write("\5R*\2\u01a4\u01a6\3\2\2\2\u01a5\u01a0\3\2\2\2\u01a5\u01a1")
        buf.write("\3\2\2\2\u01a6S\3\2\2\2\u01a7\u01ac\7D\2\2\u01a8\u01a9")
        buf.write("\7D\2\2\u01a9\u01aa\7\33\2\2\u01aa\u01ac\5T+\2\u01ab\u01a7")
        buf.write("\3\2\2\2\u01ab\u01a8\3\2\2\2\u01acU\3\2\2\2\u01ad\u01b2")
        buf.write("\7E\2\2\u01ae\u01af\7E\2\2\u01af\u01b0\7\33\2\2\u01b0")
        buf.write("\u01b2\5V,\2\u01b1\u01ad\3\2\2\2\u01b1\u01ae\3\2\2\2\u01b2")
        buf.write("W\3\2\2\2(Z\\v{\u0087\u008e\u0092\u00ab\u00af\u00bc\u00c8")
        buf.write("\u00d0\u00d7\u00dc\u00ee\u00fd\u0104\u010d\u0128\u0133")
        buf.write("\u0135\u0141\u0143\u0152\u0154\u015a\u015f\u0165\u0170")
        buf.write("\u017c\u0185\u0187\u0189\u0193\u019a\u01a5\u01ab\u01b1")
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
    RULE_if_else_statement = 16
    RULE_lhs = 17
    RULE_index = 18
    RULE_function_call = 19
    RULE_var_declare = 20
    RULE_init_value = 21
    RULE_array_list = 22
    RULE_literal_list = 23
    RULE_array_type = 24
    RULE_primitive_type = 25
    RULE_literal = 26
    RULE_exp = 27
    RULE_exp0 = 28
    RULE_exp1 = 29
    RULE_exp2 = 30
    RULE_exp3 = 31
    RULE_exp4 = 32
    RULE_exp5 = 33
    RULE_exp6 = 34
    RULE_index_operator = 35
    RULE_exp7 = 36
    RULE_exp8 = 37
    RULE_exp9 = 38
    RULE_exp10 = 39
    RULE_list_exp = 40
    RULE_normal_id_list = 41
    RULE_dollar_id_list = 42

    ruleNames =  [ "program", "class_program", "class_program_member", "body_main", 
                   "class_declare", "extend", "member_list", "member", "constructor_method", 
                   "destructor_method", "method", "param_list", "parameter", 
                   "block_statement", "statement", "assign_statement", "if_else_statement", 
                   "lhs", "index", "function_call", "var_declare", "init_value", 
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
        self.checkVersion("4.8")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ProgramContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def EOF(self):
            return self.getToken(D96Parser.EOF, 0)

        def list_exp(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(D96Parser.List_expContext)
            else:
                return self.getTypedRuleContext(D96Parser.List_expContext,i)


        def var_declare(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(D96Parser.Var_declareContext)
            else:
                return self.getTypedRuleContext(D96Parser.Var_declareContext,i)


        def getRuleIndex(self):
            return D96Parser.RULE_program




    def program(self):

        localctx = D96Parser.ProgramContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_program)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 88 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 88
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [D96Parser.BOOL_TYPE, D96Parser.INTEGER_LITERAL, D96Parser.STRING_LITERAL, D96Parser.REAL_LITERAL, D96Parser.LP, D96Parser.ARRAY, D96Parser.NEW, D96Parser.SELF, D96Parser.SUB, D96Parser.NOT, D96Parser.NORMAL_ID, D96Parser.DOLLAR_ID]:
                    self.state = 86
                    self.list_exp()
                    pass
                elif token in [D96Parser.VAL, D96Parser.VAR]:
                    self.state = 87
                    self.var_declare()
                    pass
                else:
                    raise NoViableAltException(self)

                self.state = 90 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << D96Parser.BOOL_TYPE) | (1 << D96Parser.INTEGER_LITERAL) | (1 << D96Parser.STRING_LITERAL) | (1 << D96Parser.REAL_LITERAL) | (1 << D96Parser.VAL) | (1 << D96Parser.VAR) | (1 << D96Parser.LP) | (1 << D96Parser.ARRAY) | (1 << D96Parser.NEW) | (1 << D96Parser.SELF) | (1 << D96Parser.SUB) | (1 << D96Parser.NOT))) != 0) or _la==D96Parser.NORMAL_ID or _la==D96Parser.DOLLAR_ID):
                    break

            self.state = 92
            self.match(D96Parser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Class_programContext(ParserRuleContext):

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




    def class_program(self):

        localctx = D96Parser.Class_programContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_class_program)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 94
            self.match(D96Parser.CLASS)
            self.state = 95
            self.match(D96Parser.T__0)
            self.state = 96
            self.match(D96Parser.LCB)
            self.state = 97
            self.class_program_member()
            self.state = 98
            self.match(D96Parser.RCB)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Class_program_memberContext(ParserRuleContext):

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




    def class_program_member(self):

        localctx = D96Parser.Class_program_memberContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_class_program_member)
        try:
            self.state = 116
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,2,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 100
                self.match(D96Parser.T__1)
                self.state = 101
                self.match(D96Parser.LP)
                self.state = 102
                self.match(D96Parser.RP)
                self.state = 103
                self.match(D96Parser.LCB)
                self.state = 104
                self.body_main()
                self.state = 105
                self.match(D96Parser.RCB)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 107
                self.member_list()
                self.state = 108
                self.match(D96Parser.T__1)
                self.state = 109
                self.match(D96Parser.LP)
                self.state = 110
                self.match(D96Parser.RP)
                self.state = 111
                self.match(D96Parser.LCB)
                self.state = 112
                self.body_main()
                self.state = 113
                self.match(D96Parser.RCB)
                self.state = 114
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

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def var_declare(self):
            return self.getTypedRuleContext(D96Parser.Var_declareContext,0)


        def function_call(self):
            return self.getTypedRuleContext(D96Parser.Function_callContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_body_main




    def body_main(self):

        localctx = D96Parser.Body_mainContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_body_main)
        try:
            self.state = 121
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [D96Parser.VAL, D96Parser.VAR]:
                self.enterOuterAlt(localctx, 1)
                self.state = 118
                self.var_declare()
                pass
            elif token in [D96Parser.NORMAL_ID, D96Parser.DOLLAR_ID]:
                self.enterOuterAlt(localctx, 2)
                self.state = 119
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




    def class_declare(self):

        localctx = D96Parser.Class_declareContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_class_declare)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 123
            self.match(D96Parser.CLASS)
            self.state = 124
            self.match(D96Parser.NORMAL_ID)
            self.state = 125
            self.extend()
            self.state = 126
            self.match(D96Parser.LCB)
            self.state = 127
            self.member_list()
            self.state = 128
            self.match(D96Parser.RCB)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExtendContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def COLON(self):
            return self.getToken(D96Parser.COLON, 0)

        def NORMAL_ID(self):
            return self.getToken(D96Parser.NORMAL_ID, 0)

        def getRuleIndex(self):
            return D96Parser.RULE_extend




    def extend(self):

        localctx = D96Parser.ExtendContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_extend)
        try:
            self.state = 133
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [D96Parser.COLON]:
                self.enterOuterAlt(localctx, 1)
                self.state = 130
                self.match(D96Parser.COLON)
                self.state = 131
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

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def member(self):
            return self.getTypedRuleContext(D96Parser.MemberContext,0)


        def member_list(self):
            return self.getTypedRuleContext(D96Parser.Member_listContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_member_list




    def member_list(self):

        localctx = D96Parser.Member_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_member_list)
        try:
            self.state = 140
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,5,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 135
                self.member()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 136
                self.member()
                self.state = 137
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

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def var_declare(self):
            return self.getTypedRuleContext(D96Parser.Var_declareContext,0)


        def method(self):
            return self.getTypedRuleContext(D96Parser.MethodContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_member




    def member(self):

        localctx = D96Parser.MemberContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_member)
        try:
            self.state = 144
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [D96Parser.VAL, D96Parser.VAR]:
                self.enterOuterAlt(localctx, 1)
                self.state = 142
                self.var_declare()
                pass
            elif token in [D96Parser.NORMAL_ID, D96Parser.DOLLAR_ID]:
                self.enterOuterAlt(localctx, 2)
                self.state = 143
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




    def constructor_method(self):

        localctx = D96Parser.Constructor_methodContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_constructor_method)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 146
            self.match(D96Parser.CONSTRUCTOR)
            self.state = 147
            self.match(D96Parser.LP)
            self.state = 148
            self.param_list()
            self.state = 149
            self.match(D96Parser.RP)
            self.state = 150
            self.block_statement()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Destructor_methodContext(ParserRuleContext):

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




    def destructor_method(self):

        localctx = D96Parser.Destructor_methodContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_destructor_method)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 152
            self.match(D96Parser.DESTRUCTOR)
            self.state = 153
            self.match(D96Parser.LP)
            self.state = 154
            self.match(D96Parser.RP)
            self.state = 155
            self.block_statement()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class MethodContext(ParserRuleContext):

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




    def method(self):

        localctx = D96Parser.MethodContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_method)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 157
            _la = self._input.LA(1)
            if not(_la==D96Parser.NORMAL_ID or _la==D96Parser.DOLLAR_ID):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 158
            self.match(D96Parser.LP)
            self.state = 159
            self.param_list()
            self.state = 160
            self.match(D96Parser.RP)
            self.state = 161
            self.block_statement()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Param_listContext(ParserRuleContext):

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




    def param_list(self):

        localctx = D96Parser.Param_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_param_list)
        try:
            self.state = 169
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,7,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 163
                self.parameter()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 164
                self.parameter()
                self.state = 165
                self.match(D96Parser.SEMI)
                self.state = 166
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




    def parameter(self):

        localctx = D96Parser.ParameterContext(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_parameter)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 173
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [D96Parser.NORMAL_ID]:
                self.state = 171
                self.normal_id_list()
                pass
            elif token in [D96Parser.DOLLAR_ID]:
                self.state = 172
                self.dollar_id_list()
                pass
            else:
                raise NoViableAltException(self)

            self.state = 175
            self.match(D96Parser.COLON)
            self.state = 176
            self.primitive_type()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Block_statementContext(ParserRuleContext):

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




    def block_statement(self):

        localctx = D96Parser.Block_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 26, self.RULE_block_statement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 178
            self.match(D96Parser.LCB)
            self.state = 179
            self.statement()
            self.state = 180
            self.match(D96Parser.RCB)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StatementContext(ParserRuleContext):

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




    def statement(self):

        localctx = D96Parser.StatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 28, self.RULE_statement)
        try:
            self.state = 186
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,9,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 182
                self.var_declare()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 183
                self.assign_statement()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 184
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

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def lhs(self):
            return self.getTypedRuleContext(D96Parser.LhsContext,0)


        def ASSIGN(self):
            return self.getToken(D96Parser.ASSIGN, 0)

        def exp(self):
            return self.getTypedRuleContext(D96Parser.ExpContext,0)


        def SEMI(self):
            return self.getToken(D96Parser.SEMI, 0)

        def getRuleIndex(self):
            return D96Parser.RULE_assign_statement




    def assign_statement(self):

        localctx = D96Parser.Assign_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 30, self.RULE_assign_statement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 188
            self.lhs()
            self.state = 189
            self.match(D96Parser.ASSIGN)
            self.state = 190
            self.exp()
            self.state = 191
            self.match(D96Parser.SEMI)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class If_else_statementContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return D96Parser.RULE_if_else_statement




    def if_else_statement(self):

        localctx = D96Parser.If_else_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 32, self.RULE_if_else_statement)
        try:
            self.enterOuterAlt(localctx, 1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class LhsContext(ParserRuleContext):

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




    def lhs(self):

        localctx = D96Parser.LhsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 34, self.RULE_lhs)
        try:
            self.state = 198
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,10,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 195
                self.match(D96Parser.NORMAL_ID)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 196
                self.match(D96Parser.DOLLAR_ID)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 197
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




    def index(self):

        localctx = D96Parser.IndexContext(self, self._ctx, self.state)
        self.enterRule(localctx, 36, self.RULE_index)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 200
            _la = self._input.LA(1)
            if not(_la==D96Parser.NORMAL_ID or _la==D96Parser.DOLLAR_ID):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 201
            self.index_operator()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Function_callContext(ParserRuleContext):

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




    def function_call(self):

        localctx = D96Parser.Function_callContext(self, self._ctx, self.state)
        self.enterRule(localctx, 38, self.RULE_function_call)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 203
            _la = self._input.LA(1)
            if not(_la==D96Parser.NORMAL_ID or _la==D96Parser.DOLLAR_ID):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 204
            self.match(D96Parser.LP)
            self.state = 206
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << D96Parser.BOOL_TYPE) | (1 << D96Parser.INTEGER_LITERAL) | (1 << D96Parser.STRING_LITERAL) | (1 << D96Parser.REAL_LITERAL) | (1 << D96Parser.LP) | (1 << D96Parser.ARRAY) | (1 << D96Parser.NEW) | (1 << D96Parser.SELF) | (1 << D96Parser.SUB) | (1 << D96Parser.NOT))) != 0) or _la==D96Parser.NORMAL_ID or _la==D96Parser.DOLLAR_ID:
                self.state = 205
                self.exp()


            self.state = 208
            self.match(D96Parser.RP)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Var_declareContext(ParserRuleContext):

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




    def var_declare(self):

        localctx = D96Parser.Var_declareContext(self, self._ctx, self.state)
        self.enterRule(localctx, 40, self.RULE_var_declare)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 210
            _la = self._input.LA(1)
            if not(_la==D96Parser.VAL or _la==D96Parser.VAR):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 213
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [D96Parser.NORMAL_ID]:
                self.state = 211
                self.normal_id_list()
                pass
            elif token in [D96Parser.DOLLAR_ID]:
                self.state = 212
                self.dollar_id_list()
                pass
            else:
                raise NoViableAltException(self)

            self.state = 215
            self.match(D96Parser.COLON)
            self.state = 216
            self.primitive_type()
            self.state = 218
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==D96Parser.ASSIGN:
                self.state = 217
                self.init_value()


            self.state = 220
            self.match(D96Parser.SEMI)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Init_valueContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ASSIGN(self):
            return self.getToken(D96Parser.ASSIGN, 0)

        def list_exp(self):
            return self.getTypedRuleContext(D96Parser.List_expContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_init_value




    def init_value(self):

        localctx = D96Parser.Init_valueContext(self, self._ctx, self.state)
        self.enterRule(localctx, 42, self.RULE_init_value)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 222
            self.match(D96Parser.ASSIGN)
            self.state = 223
            self.list_exp()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Array_listContext(ParserRuleContext):

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




    def array_list(self):

        localctx = D96Parser.Array_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 44, self.RULE_array_list)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 225
            self.match(D96Parser.ARRAY)
            self.state = 226
            self.match(D96Parser.LP)
            self.state = 227
            self.literal_list()
            self.state = 228
            self.match(D96Parser.RP)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Literal_listContext(ParserRuleContext):

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




    def literal_list(self):

        localctx = D96Parser.Literal_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 46, self.RULE_literal_list)
        try:
            self.state = 236
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,14,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 230
                self.literal()
                self.state = 231
                self.match(D96Parser.COMMA)
                self.state = 232
                self.literal_list()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 234
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




    def array_type(self):

        localctx = D96Parser.Array_typeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 48, self.RULE_array_type)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 238
            self.match(D96Parser.ARRAY)
            self.state = 239
            self.match(D96Parser.LSB)
            self.state = 240
            self.primitive_type()
            self.state = 241
            self.match(D96Parser.COMMA)
            self.state = 242
            self.match(D96Parser.INTEGER_LITERAL)
            self.state = 243
            self.match(D96Parser.RSB)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Primitive_typeContext(ParserRuleContext):

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




    def primitive_type(self):

        localctx = D96Parser.Primitive_typeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 50, self.RULE_primitive_type)
        try:
            self.state = 251
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [D96Parser.BOOL_TYPE]:
                self.enterOuterAlt(localctx, 1)
                self.state = 245
                self.match(D96Parser.BOOL_TYPE)
                pass
            elif token in [D96Parser.INT_TYPE]:
                self.enterOuterAlt(localctx, 2)
                self.state = 246
                self.match(D96Parser.INT_TYPE)
                pass
            elif token in [D96Parser.FLOAT_TYPE]:
                self.enterOuterAlt(localctx, 3)
                self.state = 247
                self.match(D96Parser.FLOAT_TYPE)
                pass
            elif token in [D96Parser.ARRAY]:
                self.enterOuterAlt(localctx, 4)
                self.state = 248
                self.array_type()
                pass
            elif token in [D96Parser.STRING]:
                self.enterOuterAlt(localctx, 5)
                self.state = 249
                self.match(D96Parser.STRING)
                pass
            elif token in [D96Parser.CLASS]:
                self.enterOuterAlt(localctx, 6)
                self.state = 250
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




    def literal(self):

        localctx = D96Parser.LiteralContext(self, self._ctx, self.state)
        self.enterRule(localctx, 52, self.RULE_literal)
        try:
            self.state = 258
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [D96Parser.INTEGER_LITERAL]:
                self.enterOuterAlt(localctx, 1)
                self.state = 253
                self.match(D96Parser.INTEGER_LITERAL)
                pass
            elif token in [D96Parser.BOOL_TYPE]:
                self.enterOuterAlt(localctx, 2)
                self.state = 254
                self.match(D96Parser.BOOL_TYPE)
                pass
            elif token in [D96Parser.REAL_LITERAL]:
                self.enterOuterAlt(localctx, 3)
                self.state = 255
                self.match(D96Parser.REAL_LITERAL)
                pass
            elif token in [D96Parser.STRING_LITERAL]:
                self.enterOuterAlt(localctx, 4)
                self.state = 256
                self.match(D96Parser.STRING_LITERAL)
                pass
            elif token in [D96Parser.ARRAY]:
                self.enterOuterAlt(localctx, 5)
                self.state = 257
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




    def exp(self):

        localctx = D96Parser.ExpContext(self, self._ctx, self.state)
        self.enterRule(localctx, 54, self.RULE_exp)
        try:
            self.state = 267
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,17,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 260
                self.match(D96Parser.STRING_LITERAL)
                self.state = 261
                self.match(D96Parser.EQUAL_STR)
                self.state = 262
                self.match(D96Parser.STRING_LITERAL)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 263
                self.match(D96Parser.STRING_LITERAL)
                self.state = 264
                self.match(D96Parser.ADD_STR)
                self.state = 265
                self.match(D96Parser.STRING_LITERAL)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 266
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




    def exp0(self):

        localctx = D96Parser.Exp0Context(self, self._ctx, self.state)
        self.enterRule(localctx, 56, self.RULE_exp0)
        try:
            self.state = 294
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,18,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 269
                self.exp1(0)
                self.state = 270
                self.match(D96Parser.LT)
                self.state = 271
                self.exp1(0)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 273
                self.exp1(0)
                self.state = 274
                self.match(D96Parser.LTE)
                self.state = 275
                self.exp1(0)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 277
                self.exp1(0)
                self.state = 278
                self.match(D96Parser.GT)
                self.state = 279
                self.exp1(0)
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 281
                self.exp1(0)
                self.state = 282
                self.match(D96Parser.GTE)
                self.state = 283
                self.exp1(0)
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 285
                self.exp1(0)
                self.state = 286
                self.match(D96Parser.EQUAL)
                self.state = 287
                self.exp1(0)
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 289
                self.exp1(0)
                self.state = 290
                self.match(D96Parser.NOTEQUAL)
                self.state = 291
                self.exp1(0)
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 293
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



    def exp1(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = D96Parser.Exp1Context(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 58
        self.enterRecursionRule(localctx, 58, self.RULE_exp1, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 297
            self.exp2(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 307
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,20,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 305
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,19,self._ctx)
                    if la_ == 1:
                        localctx = D96Parser.Exp1Context(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_exp1)
                        self.state = 299
                        if not self.precpred(self._ctx, 3):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 3)")
                        self.state = 300
                        self.match(D96Parser.AND)
                        self.state = 301
                        self.exp2(0)
                        pass

                    elif la_ == 2:
                        localctx = D96Parser.Exp1Context(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_exp1)
                        self.state = 302
                        if not self.precpred(self._ctx, 2):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                        self.state = 303
                        self.match(D96Parser.OR)
                        self.state = 304
                        self.exp2(0)
                        pass

             
                self.state = 309
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,20,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Exp2Context(ParserRuleContext):

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



    def exp2(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = D96Parser.Exp2Context(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 60
        self.enterRecursionRule(localctx, 60, self.RULE_exp2, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 311
            self.exp3(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 321
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,22,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 319
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,21,self._ctx)
                    if la_ == 1:
                        localctx = D96Parser.Exp2Context(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_exp2)
                        self.state = 313
                        if not self.precpred(self._ctx, 3):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 3)")
                        self.state = 314
                        self.match(D96Parser.ADD)
                        self.state = 315
                        self.exp3(0)
                        pass

                    elif la_ == 2:
                        localctx = D96Parser.Exp2Context(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_exp2)
                        self.state = 316
                        if not self.precpred(self._ctx, 2):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                        self.state = 317
                        self.match(D96Parser.SUB)
                        self.state = 318
                        self.exp3(0)
                        pass

             
                self.state = 323
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,22,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Exp3Context(ParserRuleContext):

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



    def exp3(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = D96Parser.Exp3Context(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 62
        self.enterRecursionRule(localctx, 62, self.RULE_exp3, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 325
            self.exp4()
            self._ctx.stop = self._input.LT(-1)
            self.state = 338
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,24,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 336
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,23,self._ctx)
                    if la_ == 1:
                        localctx = D96Parser.Exp3Context(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_exp3)
                        self.state = 327
                        if not self.precpred(self._ctx, 4):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 4)")
                        self.state = 328
                        self.match(D96Parser.MUL)
                        self.state = 329
                        self.exp4()
                        pass

                    elif la_ == 2:
                        localctx = D96Parser.Exp3Context(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_exp3)
                        self.state = 330
                        if not self.precpred(self._ctx, 3):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 3)")
                        self.state = 331
                        self.match(D96Parser.DIV)
                        self.state = 332
                        self.exp4()
                        pass

                    elif la_ == 3:
                        localctx = D96Parser.Exp3Context(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_exp3)
                        self.state = 333
                        if not self.precpred(self._ctx, 2):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                        self.state = 334
                        self.match(D96Parser.MOD)
                        self.state = 335
                        self.exp4()
                        pass

             
                self.state = 340
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,24,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Exp4Context(ParserRuleContext):

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




    def exp4(self):

        localctx = D96Parser.Exp4Context(self, self._ctx, self.state)
        self.enterRule(localctx, 64, self.RULE_exp4)
        try:
            self.state = 344
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [D96Parser.NOT]:
                self.enterOuterAlt(localctx, 1)
                self.state = 341
                self.match(D96Parser.NOT)
                self.state = 342
                self.exp4()
                pass
            elif token in [D96Parser.BOOL_TYPE, D96Parser.INTEGER_LITERAL, D96Parser.STRING_LITERAL, D96Parser.REAL_LITERAL, D96Parser.LP, D96Parser.ARRAY, D96Parser.NEW, D96Parser.SELF, D96Parser.SUB, D96Parser.NORMAL_ID, D96Parser.DOLLAR_ID]:
                self.enterOuterAlt(localctx, 2)
                self.state = 343
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




    def exp5(self):

        localctx = D96Parser.Exp5Context(self, self._ctx, self.state)
        self.enterRule(localctx, 66, self.RULE_exp5)
        try:
            self.state = 349
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [D96Parser.SUB]:
                self.enterOuterAlt(localctx, 1)
                self.state = 346
                self.match(D96Parser.SUB)
                self.state = 347
                self.exp5()
                pass
            elif token in [D96Parser.BOOL_TYPE, D96Parser.INTEGER_LITERAL, D96Parser.STRING_LITERAL, D96Parser.REAL_LITERAL, D96Parser.LP, D96Parser.ARRAY, D96Parser.NEW, D96Parser.SELF, D96Parser.NORMAL_ID, D96Parser.DOLLAR_ID]:
                self.enterOuterAlt(localctx, 2)
                self.state = 348
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

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def exp7(self):
            return self.getTypedRuleContext(D96Parser.Exp7Context,0)


        def index_operator(self):
            return self.getTypedRuleContext(D96Parser.Index_operatorContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_exp6




    def exp6(self):

        localctx = D96Parser.Exp6Context(self, self._ctx, self.state)
        self.enterRule(localctx, 68, self.RULE_exp6)
        try:
            self.state = 355
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,27,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 351
                self.exp7(0)
                self.state = 352
                self.index_operator()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 354
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




    def index_operator(self):

        localctx = D96Parser.Index_operatorContext(self, self._ctx, self.state)
        self.enterRule(localctx, 70, self.RULE_index_operator)
        try:
            self.state = 366
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,28,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 357
                self.match(D96Parser.LSB)
                self.state = 358
                self.exp()
                self.state = 359
                self.match(D96Parser.RSB)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 361
                self.match(D96Parser.LSB)
                self.state = 362
                self.exp()
                self.state = 363
                self.match(D96Parser.RSB)
                self.state = 364
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

        def list_exp(self):
            return self.getTypedRuleContext(D96Parser.List_expContext,0)


        def RP(self):
            return self.getToken(D96Parser.RP, 0)

        def SCOPE(self):
            return self.getToken(D96Parser.SCOPE, 0)

        def getRuleIndex(self):
            return D96Parser.RULE_exp7



    def exp7(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = D96Parser.Exp7Context(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 72
        self.enterRecursionRule(localctx, 72, self.RULE_exp7, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 369
            self.exp8()
            self._ctx.stop = self._input.LT(-1)
            self.state = 391
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,32,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 389
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,31,self._ctx)
                    if la_ == 1:
                        localctx = D96Parser.Exp7Context(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_exp7)
                        self.state = 371
                        if not self.precpred(self._ctx, 3):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 3)")
                        self.state = 372
                        self.match(D96Parser.DOT)
                        self.state = 373
                        _la = self._input.LA(1)
                        if not(_la==D96Parser.NORMAL_ID or _la==D96Parser.DOLLAR_ID):
                            self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 378
                        self._errHandler.sync(self)
                        la_ = self._interp.adaptivePredict(self._input,29,self._ctx)
                        if la_ == 1:
                            self.state = 374
                            self.match(D96Parser.LP)
                            self.state = 375
                            self.list_exp()
                            self.state = 376
                            self.match(D96Parser.RP)


                        pass

                    elif la_ == 2:
                        localctx = D96Parser.Exp7Context(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_exp7)
                        self.state = 380
                        if not self.precpred(self._ctx, 2):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                        self.state = 381
                        self.match(D96Parser.SCOPE)
                        self.state = 382
                        _la = self._input.LA(1)
                        if not(_la==D96Parser.NORMAL_ID or _la==D96Parser.DOLLAR_ID):
                            self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 387
                        self._errHandler.sync(self)
                        la_ = self._interp.adaptivePredict(self._input,30,self._ctx)
                        if la_ == 1:
                            self.state = 383
                            self.match(D96Parser.LP)
                            self.state = 384
                            self.list_exp()
                            self.state = 385
                            self.match(D96Parser.RP)


                        pass

             
                self.state = 393
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

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NEW(self):
            return self.getToken(D96Parser.NEW, 0)

        def NORMAL_ID(self):
            return self.getToken(D96Parser.NORMAL_ID, 0)

        def LP(self):
            return self.getToken(D96Parser.LP, 0)

        def list_exp(self):
            return self.getTypedRuleContext(D96Parser.List_expContext,0)


        def RP(self):
            return self.getToken(D96Parser.RP, 0)

        def exp9(self):
            return self.getTypedRuleContext(D96Parser.Exp9Context,0)


        def getRuleIndex(self):
            return D96Parser.RULE_exp8




    def exp8(self):

        localctx = D96Parser.Exp8Context(self, self._ctx, self.state)
        self.enterRule(localctx, 74, self.RULE_exp8)
        try:
            self.state = 401
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [D96Parser.NEW]:
                self.enterOuterAlt(localctx, 1)
                self.state = 394
                self.match(D96Parser.NEW)
                self.state = 395
                self.match(D96Parser.NORMAL_ID)
                self.state = 396
                self.match(D96Parser.LP)
                self.state = 397
                self.list_exp()
                self.state = 398
                self.match(D96Parser.RP)
                pass
            elif token in [D96Parser.BOOL_TYPE, D96Parser.INTEGER_LITERAL, D96Parser.STRING_LITERAL, D96Parser.REAL_LITERAL, D96Parser.LP, D96Parser.ARRAY, D96Parser.SELF, D96Parser.NORMAL_ID, D96Parser.DOLLAR_ID]:
                self.enterOuterAlt(localctx, 2)
                self.state = 400
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




    def exp9(self):

        localctx = D96Parser.Exp9Context(self, self._ctx, self.state)
        self.enterRule(localctx, 76, self.RULE_exp9)
        try:
            self.state = 408
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [D96Parser.BOOL_TYPE, D96Parser.INTEGER_LITERAL, D96Parser.STRING_LITERAL, D96Parser.REAL_LITERAL, D96Parser.ARRAY]:
                self.enterOuterAlt(localctx, 1)
                self.state = 403
                self.literal()
                pass
            elif token in [D96Parser.NORMAL_ID]:
                self.enterOuterAlt(localctx, 2)
                self.state = 404
                self.match(D96Parser.NORMAL_ID)
                pass
            elif token in [D96Parser.DOLLAR_ID]:
                self.enterOuterAlt(localctx, 3)
                self.state = 405
                self.match(D96Parser.DOLLAR_ID)
                pass
            elif token in [D96Parser.SELF]:
                self.enterOuterAlt(localctx, 4)
                self.state = 406
                self.match(D96Parser.SELF)
                pass
            elif token in [D96Parser.LP]:
                self.enterOuterAlt(localctx, 5)
                self.state = 407
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




    def exp10(self):

        localctx = D96Parser.Exp10Context(self, self._ctx, self.state)
        self.enterRule(localctx, 78, self.RULE_exp10)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 410
            self.match(D96Parser.LP)
            self.state = 411
            self.exp()
            self.state = 412
            self.match(D96Parser.RP)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class List_expContext(ParserRuleContext):

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




    def list_exp(self):

        localctx = D96Parser.List_expContext(self, self._ctx, self.state)
        self.enterRule(localctx, 80, self.RULE_list_exp)
        try:
            self.state = 419
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,35,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 414
                self.exp()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 415
                self.exp()
                self.state = 416
                self.match(D96Parser.COMMA)
                self.state = 417
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




    def normal_id_list(self):

        localctx = D96Parser.Normal_id_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 82, self.RULE_normal_id_list)
        try:
            self.state = 425
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,36,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 421
                self.match(D96Parser.NORMAL_ID)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 422
                self.match(D96Parser.NORMAL_ID)
                self.state = 423
                self.match(D96Parser.COMMA)
                self.state = 424
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




    def dollar_id_list(self):

        localctx = D96Parser.Dollar_id_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 84, self.RULE_dollar_id_list)
        try:
            self.state = 431
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,37,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 427
                self.match(D96Parser.DOLLAR_ID)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 428
                self.match(D96Parser.DOLLAR_ID)
                self.state = 429
                self.match(D96Parser.COMMA)
                self.state = 430
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
        self._predicates[29] = self.exp1_sempred
        self._predicates[30] = self.exp2_sempred
        self._predicates[31] = self.exp3_sempred
        self._predicates[36] = self.exp7_sempred
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
         




