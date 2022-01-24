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
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3E")
        buf.write("\u0273\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
        buf.write("\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r\4\16")
        buf.write("\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23\t\23")
        buf.write("\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30\4\31")
        buf.write("\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36\t\36")
        buf.write("\4\37\t\37\4 \t \4!\t!\4\"\t\"\4#\t#\4$\t$\4%\t%\4&\t")
        buf.write("&\4\'\t\'\4(\t(\4)\t)\4*\t*\4+\t+\4,\t,\4-\t-\4.\t.\4")
        buf.write("/\t/\4\60\t\60\4\61\t\61\4\62\t\62\4\63\t\63\4\64\t\64")
        buf.write("\4\65\t\65\4\66\t\66\4\67\t\67\48\t8\49\t9\4:\t:\4;\t")
        buf.write(";\4<\t<\4=\t=\4>\t>\4?\t?\3\2\3\2\6\2\u0081\n\2\r\2\16")
        buf.write("\2\u0082\3\2\3\2\3\3\3\3\3\3\3\3\5\3\u008b\n\3\3\4\3\4")
        buf.write("\3\4\3\4\3\4\3\5\3\5\3\5\5\5\u0095\n\5\3\6\3\6\3\6\3\6")
        buf.write("\3\7\3\7\5\7\u009d\n\7\3\b\3\b\3\b\3\b\5\b\u00a3\n\b\3")
        buf.write("\t\3\t\3\t\3\t\3\t\5\t\u00aa\n\t\3\n\3\n\3\n\3\n\3\n\3")
        buf.write("\13\3\13\3\13\3\13\3\13\3\13\3\f\3\f\3\f\3\f\3\f\3\r\3")
        buf.write("\r\3\r\3\r\3\r\3\r\3\16\3\16\5\16\u00c4\n\16\3\17\3\17")
        buf.write("\3\17\3\17\3\17\5\17\u00cb\n\17\3\20\3\20\3\20\3\20\3")
        buf.write("\20\3\20\3\20\3\20\5\20\u00d5\n\20\3\21\3\21\3\21\3\21")
        buf.write("\3\22\3\22\5\22\u00dd\n\22\3\23\3\23\3\23\3\23\5\23\u00e3")
        buf.write("\n\23\3\24\3\24\3\24\3\24\3\24\3\24\3\24\3\24\3\24\3\24")
        buf.write("\3\24\3\24\3\24\3\24\3\24\3\24\3\24\3\24\3\24\5\24\u00f8")
        buf.write("\n\24\3\25\3\25\3\25\3\26\3\26\3\26\3\27\3\27\5\27\u0102")
        buf.write("\n\27\3\27\3\27\3\30\3\30\3\30\3\30\3\30\3\31\3\31\3\31")
        buf.write("\3\31\3\31\3\31\3\31\3\31\3\32\3\32\5\32\u0115\n\32\3")
        buf.write("\33\3\33\3\33\3\33\5\33\u011b\n\33\3\34\3\34\3\34\3\34")
        buf.write("\3\34\3\34\3\35\3\35\3\35\5\35\u0126\n\35\3\36\3\36\3")
        buf.write("\36\3\36\3\36\3\36\3\36\3\36\3\36\3\36\3\36\3\37\3\37")
        buf.write("\3\37\5\37\u0136\n\37\3 \3 \3 \3 \3 \5 \u013d\n \3!\3")
        buf.write("!\3!\3\"\3\"\3\"\3\"\3\"\3#\3#\3#\3#\3$\3$\3$\3$\3$\3")
        buf.write("$\3$\3%\5%\u0153\n%\3%\5%\u0156\n%\3%\3%\3&\5&\u015b\n")
        buf.write("&\3&\5&\u015e\n&\3&\3&\3&\3&\3&\3\'\3\'\3\'\3\'\3(\3(")
        buf.write("\3(\3(\3(\3(\5(\u016f\n(\3(\3(\3(\3(\3(\3(\3(\5(\u0178")
        buf.write("\n(\5(\u017a\n(\3)\3)\3)\3)\3)\3)\3)\3)\3)\3)\3)\3)\3")
        buf.write(")\5)\u0189\n)\3)\5)\u018c\n)\3*\3*\3*\3*\3*\3*\3*\3*\5")
        buf.write("*\u0196\n*\3*\3*\3*\3*\3*\3+\3+\3+\3+\3+\3,\3,\5,\u01a4")
        buf.write("\n,\3-\3-\3-\3-\3-\5-\u01ab\n-\3.\3.\3.\3.\3.\3.\3.\3")
        buf.write(".\3.\5.\u01b6\n.\3/\3/\3/\3/\3/\3/\3/\3/\3/\3/\3/\3/\3")
        buf.write("/\3/\3/\3/\3/\3/\3/\3/\3/\3/\3/\3/\3/\5/\u01d1\n/\3\60")
        buf.write("\3\60\3\60\3\60\3\60\3\60\3\60\3\60\3\60\7\60\u01dc\n")
        buf.write("\60\f\60\16\60\u01df\13\60\3\61\3\61\3\61\3\61\3\61\3")
        buf.write("\61\3\61\3\61\3\61\7\61\u01ea\n\61\f\61\16\61\u01ed\13")
        buf.write("\61\3\62\3\62\3\62\3\62\3\62\3\62\3\62\3\62\3\62\3\62")
        buf.write("\3\62\3\62\7\62\u01fb\n\62\f\62\16\62\u01fe\13\62\3\63")
        buf.write("\3\63\3\63\5\63\u0203\n\63\3\64\3\64\3\64\5\64\u0208\n")
        buf.write("\64\3\65\3\65\3\65\3\65\3\65\3\65\3\65\3\65\7\65\u0212")
        buf.write("\n\65\f\65\16\65\u0215\13\65\3\66\3\66\3\66\3\66\3\66")
        buf.write("\3\66\3\66\3\66\3\66\5\66\u0220\n\66\3\67\3\67\3\67\5")
        buf.write("\67\u0225\n\67\3\67\3\67\3\67\3\67\3\67\3\67\3\67\3\67")
        buf.write("\3\67\3\67\7\67\u0231\n\67\f\67\16\67\u0234\13\67\38\3")
        buf.write("8\38\38\38\38\38\38\38\38\38\58\u0241\n8\39\39\39\39\3")
        buf.write("9\39\39\59\u024a\n9\3:\3:\3:\3:\3:\3:\3:\3:\3:\3:\5:\u0256")
        buf.write("\n:\3;\3;\3;\3;\3<\3<\5<\u025e\n<\3=\3=\3=\3=\3=\5=\u0265")
        buf.write("\n=\3>\3>\3>\3>\5>\u026b\n>\3?\3?\3?\3?\5?\u0271\n?\3")
        buf.write("?\2\7^`bhl@\2\4\6\b\n\f\16\20\22\24\26\30\32\34\36 \"")
        buf.write("$&(*,.\60\62\64\668:<>@BDFHJLNPRTVXZ\\^`bdfhjlnprtvxz")
        buf.write("|\2\4\3\2AB\3\2\3\4\2\u0298\2\u0080\3\2\2\2\4\u008a\3")
        buf.write("\2\2\2\6\u008c\3\2\2\2\b\u0094\3\2\2\2\n\u0096\3\2\2\2")
        buf.write("\f\u009c\3\2\2\2\16\u00a2\3\2\2\2\20\u00a9\3\2\2\2\22")
        buf.write("\u00ab\3\2\2\2\24\u00b0\3\2\2\2\26\u00b6\3\2\2\2\30\u00bb")
        buf.write("\3\2\2\2\32\u00c3\3\2\2\2\34\u00ca\3\2\2\2\36\u00cc\3")
        buf.write("\2\2\2 \u00d6\3\2\2\2\"\u00dc\3\2\2\2$\u00e2\3\2\2\2&")
        buf.write("\u00f7\3\2\2\2(\u00f9\3\2\2\2*\u00fc\3\2\2\2,\u00ff\3")
        buf.write("\2\2\2.\u0105\3\2\2\2\60\u010a\3\2\2\2\62\u0114\3\2\2")
        buf.write("\2\64\u011a\3\2\2\2\66\u011c\3\2\2\28\u0125\3\2\2\2:\u0127")
        buf.write("\3\2\2\2<\u0135\3\2\2\2>\u013c\3\2\2\2@\u013e\3\2\2\2")
        buf.write("B\u0141\3\2\2\2D\u0146\3\2\2\2F\u014a\3\2\2\2H\u0152\3")
        buf.write("\2\2\2J\u015a\3\2\2\2L\u0164\3\2\2\2N\u0179\3\2\2\2P\u018b")
        buf.write("\3\2\2\2R\u018d\3\2\2\2T\u019c\3\2\2\2V\u01a3\3\2\2\2")
        buf.write("X\u01aa\3\2\2\2Z\u01b5\3\2\2\2\\\u01d0\3\2\2\2^\u01d2")
        buf.write("\3\2\2\2`\u01e0\3\2\2\2b\u01ee\3\2\2\2d\u0202\3\2\2\2")
        buf.write("f\u0207\3\2\2\2h\u0209\3\2\2\2j\u021f\3\2\2\2l\u0224\3")
        buf.write("\2\2\2n\u0240\3\2\2\2p\u0249\3\2\2\2r\u0255\3\2\2\2t\u0257")
        buf.write("\3\2\2\2v\u025d\3\2\2\2x\u0264\3\2\2\2z\u026a\3\2\2\2")
        buf.write("|\u0270\3\2\2\2~\u0081\5\4\3\2\177\u0081\5.\30\2\u0080")
        buf.write("~\3\2\2\2\u0080\177\3\2\2\2\u0081\u0082\3\2\2\2\u0082")
        buf.write("\u0080\3\2\2\2\u0082\u0083\3\2\2\2\u0083\u0084\3\2\2\2")
        buf.write("\u0084\u0085\7\2\2\3\u0085\3\3\2\2\2\u0086\u008b\5\6\4")
        buf.write("\2\u0087\u0088\5\6\4\2\u0088\u0089\5\4\3\2\u0089\u008b")
        buf.write("\3\2\2\2\u008a\u0086\3\2\2\2\u008a\u0087\3\2\2\2\u008b")
        buf.write("\5\3\2\2\2\u008c\u008d\7\66\2\2\u008d\u008e\7A\2\2\u008e")
        buf.write("\u008f\5\b\5\2\u008f\u0090\5\n\6\2\u0090\7\3\2\2\2\u0091")
        buf.write("\u0092\7\r\2\2\u0092\u0095\7A\2\2\u0093\u0095\3\2\2\2")
        buf.write("\u0094\u0091\3\2\2\2\u0094\u0093\3\2\2\2\u0095\t\3\2\2")
        buf.write("\2\u0096\u0097\7\7\2\2\u0097\u0098\5\f\7\2\u0098\u0099")
        buf.write("\7\b\2\2\u0099\13\3\2\2\2\u009a\u009d\5\16\b\2\u009b\u009d")
        buf.write("\3\2\2\2\u009c\u009a\3\2\2\2\u009c\u009b\3\2\2\2\u009d")
        buf.write("\r\3\2\2\2\u009e\u009f\5\20\t\2\u009f\u00a0\5\16\b\2\u00a0")
        buf.write("\u00a3\3\2\2\2\u00a1\u00a3\5\20\t\2\u00a2\u009e\3\2\2")
        buf.write("\2\u00a2\u00a1\3\2\2\2\u00a3\17\3\2\2\2\u00a4\u00aa\5")
        buf.write("L\'\2\u00a5\u00aa\5\24\13\2\u00a6\u00aa\5\26\f\2\u00a7")
        buf.write("\u00aa\5\22\n\2\u00a8\u00aa\5\30\r\2\u00a9\u00a4\3\2\2")
        buf.write("\2\u00a9\u00a5\3\2\2\2\u00a9\u00a6\3\2\2\2\u00a9\u00a7")
        buf.write("\3\2\2\2\u00a9\u00a8\3\2\2\2\u00aa\21\3\2\2\2\u00ab\u00ac")
        buf.write("\7\65\2\2\u00ac\u00ad\7\5\2\2\u00ad\u00ae\7\6\2\2\u00ae")
        buf.write("\u00af\5 \21\2\u00af\23\3\2\2\2\u00b0\u00b1\7\33\2\2\u00b1")
        buf.write("\u00b2\7\5\2\2\u00b2\u00b3\5\32\16\2\u00b3\u00b4\7\6\2")
        buf.write("\2\u00b4\u00b5\5 \21\2\u00b5\25\3\2\2\2\u00b6\u00b7\7")
        buf.write("\34\2\2\u00b7\u00b8\7\5\2\2\u00b8\u00b9\7\6\2\2\u00b9")
        buf.write("\u00ba\5 \21\2\u00ba\27\3\2\2\2\u00bb\u00bc\t\2\2\2\u00bc")
        buf.write("\u00bd\7\5\2\2\u00bd\u00be\5\32\16\2\u00be\u00bf\7\6\2")
        buf.write("\2\u00bf\u00c0\5 \21\2\u00c0\31\3\2\2\2\u00c1\u00c4\5")
        buf.write("\34\17\2\u00c2\u00c4\3\2\2\2\u00c3\u00c1\3\2\2\2\u00c3")
        buf.write("\u00c2\3\2\2\2\u00c4\33\3\2\2\2\u00c5\u00c6\5\36\20\2")
        buf.write("\u00c6\u00c7\7\13\2\2\u00c7\u00c8\5\34\17\2\u00c8\u00cb")
        buf.write("\3\2\2\2\u00c9\u00cb\5\36\20\2\u00ca\u00c5\3\2\2\2\u00ca")
        buf.write("\u00c9\3\2\2\2\u00cb\35\3\2\2\2\u00cc\u00cd\5z>\2\u00cd")
        buf.write("\u00d4\7\r\2\2\u00ce\u00d5\7\30\2\2\u00cf\u00d5\79\2\2")
        buf.write("\u00d0\u00d5\7\67\2\2\u00d1\u00d5\5R*\2\u00d2\u00d5\7")
        buf.write("8\2\2\u00d3\u00d5\7A\2\2\u00d4\u00ce\3\2\2\2\u00d4\u00cf")
        buf.write("\3\2\2\2\u00d4\u00d0\3\2\2\2\u00d4\u00d1\3\2\2\2\u00d4")
        buf.write("\u00d2\3\2\2\2\u00d4\u00d3\3\2\2\2\u00d5\37\3\2\2\2\u00d6")
        buf.write("\u00d7\7\7\2\2\u00d7\u00d8\5\"\22\2\u00d8\u00d9\7\b\2")
        buf.write("\2\u00d9!\3\2\2\2\u00da\u00dd\5$\23\2\u00db\u00dd\3\2")
        buf.write("\2\2\u00dc\u00da\3\2\2\2\u00dc\u00db\3\2\2\2\u00dd#\3")
        buf.write("\2\2\2\u00de\u00df\5&\24\2\u00df\u00e0\5$\23\2\u00e0\u00e3")
        buf.write("\3\2\2\2\u00e1\u00e3\5&\24\2\u00e2\u00de\3\2\2\2\u00e2")
        buf.write("\u00e1\3\2\2\2\u00e3%\3\2\2\2\u00e4\u00f8\5.\30\2\u00e5")
        buf.write("\u00f8\5L\'\2\u00e6\u00f8\5(\25\2\u00e7\u00f8\5*\26\2")
        buf.write("\u00e8\u00f8\5,\27\2\u00e9\u00ea\5J&\2\u00ea\u00eb\7\13")
        buf.write("\2\2\u00eb\u00f8\3\2\2\2\u00ec\u00ed\5H%\2\u00ed\u00ee")
        buf.write("\7\13\2\2\u00ee\u00f8\3\2\2\2\u00ef\u00f0\5D#\2\u00f0")
        buf.write("\u00f1\7\13\2\2\u00f1\u00f8\3\2\2\2\u00f2\u00f3\5F$\2")
        buf.write("\u00f3\u00f4\7\13\2\2\u00f4\u00f8\3\2\2\2\u00f5\u00f8")
        buf.write("\5\60\31\2\u00f6\u00f8\5:\36\2\u00f7\u00e4\3\2\2\2\u00f7")
        buf.write("\u00e5\3\2\2\2\u00f7\u00e6\3\2\2\2\u00f7\u00e7\3\2\2\2")
        buf.write("\u00f7\u00e8\3\2\2\2\u00f7\u00e9\3\2\2\2\u00f7\u00ec\3")
        buf.write("\2\2\2\u00f7\u00ef\3\2\2\2\u00f7\u00f2\3\2\2\2\u00f7\u00f5")
        buf.write("\3\2\2\2\u00f7\u00f6\3\2\2\2\u00f8\'\3\2\2\2\u00f9\u00fa")
        buf.write("\7\16\2\2\u00fa\u00fb\7\13\2\2\u00fb)\3\2\2\2\u00fc\u00fd")
        buf.write("\7\17\2\2\u00fd\u00fe\7\13\2\2\u00fe+\3\2\2\2\u00ff\u0101")
        buf.write("\7\31\2\2\u0100\u0102\5Z.\2\u0101\u0100\3\2\2\2\u0101")
        buf.write("\u0102\3\2\2\2\u0102\u0103\3\2\2\2\u0103\u0104\7\13\2")
        buf.write("\2\u0104-\3\2\2\2\u0105\u0106\5> \2\u0106\u0107\7)\2\2")
        buf.write("\u0107\u0108\5Z.\2\u0108\u0109\7\13\2\2\u0109/\3\2\2\2")
        buf.write("\u010a\u010b\7\20\2\2\u010b\u010c\7\5\2\2\u010c\u010d")
        buf.write("\5Z.\2\u010d\u010e\7\6\2\2\u010e\u010f\5 \21\2\u010f\u0110")
        buf.write("\5\62\32\2\u0110\u0111\58\35\2\u0111\61\3\2\2\2\u0112")
        buf.write("\u0115\5\64\33\2\u0113\u0115\3\2\2\2\u0114\u0112\3\2\2")
        buf.write("\2\u0114\u0113\3\2\2\2\u0115\63\3\2\2\2\u0116\u011b\5")
        buf.write("\66\34\2\u0117\u0118\5\66\34\2\u0118\u0119\5\64\33\2\u0119")
        buf.write("\u011b\3\2\2\2\u011a\u0116\3\2\2\2\u011a\u0117\3\2\2\2")
        buf.write("\u011b\65\3\2\2\2\u011c\u011d\7\21\2\2\u011d\u011e\7\5")
        buf.write("\2\2\u011e\u011f\5Z.\2\u011f\u0120\7\6\2\2\u0120\u0121")
        buf.write("\5 \21\2\u0121\67\3\2\2\2\u0122\u0123\7\22\2\2\u0123\u0126")
        buf.write("\5 \21\2\u0124\u0126\3\2\2\2\u0125\u0122\3\2\2\2\u0125")
        buf.write("\u0124\3\2\2\2\u01269\3\2\2\2\u0127\u0128\7\23\2\2\u0128")
        buf.write("\u0129\7\5\2\2\u0129\u012a\t\2\2\2\u012a\u012b\7\27\2")
        buf.write("\2\u012b\u012c\5Z.\2\u012c\u012d\7\62\2\2\u012d\u012e")
        buf.write("\5Z.\2\u012e\u012f\5<\37\2\u012f\u0130\7\6\2\2\u0130\u0131")
        buf.write("\5 \21\2\u0131;\3\2\2\2\u0132\u0133\7\36\2\2\u0133\u0136")
        buf.write("\5Z.\2\u0134\u0136\3\2\2\2\u0135\u0132\3\2\2\2\u0135\u0134")
        buf.write("\3\2\2\2\u0136=\3\2\2\2\u0137\u013d\7A\2\2\u0138\u013d")
        buf.write("\7B\2\2\u0139\u013d\5@!\2\u013a\u013d\5H%\2\u013b\u013d")
        buf.write("\5D#\2\u013c\u0137\3\2\2\2\u013c\u0138\3\2\2\2\u013c\u0139")
        buf.write("\3\2\2\2\u013c\u013a\3\2\2\2\u013c\u013b\3\2\2\2\u013d")
        buf.write("?\3\2\2\2\u013e\u013f\5Z.\2\u013f\u0140\5j\66\2\u0140")
        buf.write("A\3\2\2\2\u0141\u0142\t\2\2\2\u0142\u0143\7\5\2\2\u0143")
        buf.write("\u0144\5v<\2\u0144\u0145\7\6\2\2\u0145C\3\2\2\2\u0146")
        buf.write("\u0147\7A\2\2\u0147\u0148\7\63\2\2\u0148\u0149\7B\2\2")
        buf.write("\u0149E\3\2\2\2\u014a\u014b\7A\2\2\u014b\u014c\7\63\2")
        buf.write("\2\u014c\u014d\7B\2\2\u014d\u014e\7\5\2\2\u014e\u014f")
        buf.write("\5v<\2\u014f\u0150\7\6\2\2\u0150G\3\2\2\2\u0151\u0153")
        buf.write("\5Z.\2\u0152\u0151\3\2\2\2\u0152\u0153\3\2\2\2\u0153\u0155")
        buf.write("\3\2\2\2\u0154\u0156\7\61\2\2\u0155\u0154\3\2\2\2\u0155")
        buf.write("\u0156\3\2\2\2\u0156\u0157\3\2\2\2\u0157\u0158\7A\2\2")
        buf.write("\u0158I\3\2\2\2\u0159\u015b\5Z.\2\u015a\u0159\3\2\2\2")
        buf.write("\u015a\u015b\3\2\2\2\u015b\u015d\3\2\2\2\u015c\u015e\7")
        buf.write("\61\2\2\u015d\u015c\3\2\2\2\u015d\u015e\3\2\2\2\u015e")
        buf.write("\u015f\3\2\2\2\u015f\u0160\7A\2\2\u0160\u0161\7\5\2\2")
        buf.write("\u0161\u0162\5v<\2\u0162\u0163\7\6\2\2\u0163K\3\2\2\2")
        buf.write("\u0164\u0165\t\3\2\2\u0165\u0166\5N(\2\u0166\u0167\7\13")
        buf.write("\2\2\u0167M\3\2\2\2\u0168\u0169\t\2\2\2\u0169\u016a\5")
        buf.write("P)\2\u016a\u016b\5Z.\2\u016b\u017a\3\2\2\2\u016c\u016f")
        buf.write("\5|?\2\u016d\u016f\5z>\2\u016e\u016c\3\2\2\2\u016e\u016d")
        buf.write("\3\2\2\2\u016f\u0170\3\2\2\2\u0170\u0177\7\r\2\2\u0171")
        buf.write("\u0178\7\30\2\2\u0172\u0178\79\2\2\u0173\u0178\7\67\2")
        buf.write("\2\u0174\u0178\5R*\2\u0175\u0178\78\2\2\u0176\u0178\7")
        buf.write("A\2\2\u0177\u0171\3\2\2\2\u0177\u0172\3\2\2\2\u0177\u0173")
        buf.write("\3\2\2\2\u0177\u0174\3\2\2\2\u0177\u0175\3\2\2\2\u0177")
        buf.write("\u0176\3\2\2\2\u0178\u017a\3\2\2\2\u0179\u0168\3\2\2\2")
        buf.write("\u0179\u016e\3\2\2\2\u017aO\3\2\2\2\u017b\u017c\7\f\2")
        buf.write("\2\u017c\u017d\t\2\2\2\u017d\u017e\5P)\2\u017e\u017f\5")
        buf.write("Z.\2\u017f\u0180\7\f\2\2\u0180\u018c\3\2\2\2\u0181\u0188")
        buf.write("\7\r\2\2\u0182\u0189\7\30\2\2\u0183\u0189\79\2\2\u0184")
        buf.write("\u0189\7\67\2\2\u0185\u0189\5R*\2\u0186\u0189\78\2\2\u0187")
        buf.write("\u0189\7A\2\2\u0188\u0182\3\2\2\2\u0188\u0183\3\2\2\2")
        buf.write("\u0188\u0184\3\2\2\2\u0188\u0185\3\2\2\2\u0188\u0186\3")
        buf.write("\2\2\2\u0188\u0187\3\2\2\2\u0189\u018a\3\2\2\2\u018a\u018c")
        buf.write("\7)\2\2\u018b\u017b\3\2\2\2\u018b\u0181\3\2\2\2\u018c")
        buf.write("Q\3\2\2\2\u018d\u018e\7\26\2\2\u018e\u0195\7\t\2\2\u018f")
        buf.write("\u0196\7\30\2\2\u0190\u0196\79\2\2\u0191\u0196\7\67\2")
        buf.write("\2\u0192\u0196\5R*\2\u0193\u0196\78\2\2\u0194\u0196\7")
        buf.write("A\2\2\u0195\u018f\3\2\2\2\u0195\u0190\3\2\2\2\u0195\u0191")
        buf.write("\3\2\2\2\u0195\u0192\3\2\2\2\u0195\u0193\3\2\2\2\u0195")
        buf.write("\u0194\3\2\2\2\u0196\u0197\3\2\2\2\u0197\u0198\7\f\2\2")
        buf.write("\u0198\u0199\7;\2\2\u0199\u019a\7\n\2\2\u019a\u019b\b")
        buf.write("*\1\2\u019bS\3\2\2\2\u019c\u019d\7\26\2\2\u019d\u019e")
        buf.write("\7\5\2\2\u019e\u019f\5V,\2\u019f\u01a0\7\6\2\2\u01a0U")
        buf.write("\3\2\2\2\u01a1\u01a4\5X-\2\u01a2\u01a4\3\2\2\2\u01a3\u01a1")
        buf.write("\3\2\2\2\u01a3\u01a2\3\2\2\2\u01a4W\3\2\2\2\u01a5\u01a6")
        buf.write("\5Z.\2\u01a6\u01a7\7\f\2\2\u01a7\u01a8\5X-\2\u01a8\u01ab")
        buf.write("\3\2\2\2\u01a9\u01ab\5Z.\2\u01aa\u01a5\3\2\2\2\u01aa\u01a9")
        buf.write("\3\2\2\2\u01abY\3\2\2\2\u01ac\u01ad\5\\/\2\u01ad\u01ae")
        buf.write("\7/\2\2\u01ae\u01af\5\\/\2\u01af\u01b6\3\2\2\2\u01b0\u01b1")
        buf.write("\5\\/\2\u01b1\u01b2\7\60\2\2\u01b2\u01b3\5\\/\2\u01b3")
        buf.write("\u01b6\3\2\2\2\u01b4\u01b6\5\\/\2\u01b5\u01ac\3\2\2\2")
        buf.write("\u01b5\u01b0\3\2\2\2\u01b5\u01b4\3\2\2\2\u01b6[\3\2\2")
        buf.write("\2\u01b7\u01b8\5^\60\2\u01b8\u01b9\7-\2\2\u01b9\u01ba")
        buf.write("\5^\60\2\u01ba\u01d1\3\2\2\2\u01bb\u01bc\5^\60\2\u01bc")
        buf.write("\u01bd\7.\2\2\u01bd\u01be\5^\60\2\u01be\u01d1\3\2\2\2")
        buf.write("\u01bf\u01c0\5^\60\2\u01c0\u01c1\7+\2\2\u01c1\u01c2\5")
        buf.write("^\60\2\u01c2\u01d1\3\2\2\2\u01c3\u01c4\5^\60\2\u01c4\u01c5")
        buf.write("\7(\2\2\u01c5\u01c6\5^\60\2\u01c6\u01d1\3\2\2\2\u01c7")
        buf.write("\u01c8\5^\60\2\u01c8\u01c9\7*\2\2\u01c9\u01ca\5^\60\2")
        buf.write("\u01ca\u01d1\3\2\2\2\u01cb\u01cc\5^\60\2\u01cc\u01cd\7")
        buf.write(",\2\2\u01cd\u01ce\5^\60\2\u01ce\u01d1\3\2\2\2\u01cf\u01d1")
        buf.write("\5^\60\2\u01d0\u01b7\3\2\2\2\u01d0\u01bb\3\2\2\2\u01d0")
        buf.write("\u01bf\3\2\2\2\u01d0\u01c3\3\2\2\2\u01d0\u01c7\3\2\2\2")
        buf.write("\u01d0\u01cb\3\2\2\2\u01d0\u01cf\3\2\2\2\u01d1]\3\2\2")
        buf.write("\2\u01d2\u01d3\b\60\1\2\u01d3\u01d4\5`\61\2\u01d4\u01dd")
        buf.write("\3\2\2\2\u01d5\u01d6\f\5\2\2\u01d6\u01d7\7&\2\2\u01d7")
        buf.write("\u01dc\5`\61\2\u01d8\u01d9\f\4\2\2\u01d9\u01da\7\'\2\2")
        buf.write("\u01da\u01dc\5`\61\2\u01db\u01d5\3\2\2\2\u01db\u01d8\3")
        buf.write("\2\2\2\u01dc\u01df\3\2\2\2\u01dd\u01db\3\2\2\2\u01dd\u01de")
        buf.write("\3\2\2\2\u01de_\3\2\2\2\u01df\u01dd\3\2\2\2\u01e0\u01e1")
        buf.write("\b\61\1\2\u01e1\u01e2\5b\62\2\u01e2\u01eb\3\2\2\2\u01e3")
        buf.write("\u01e4\f\5\2\2\u01e4\u01e5\7 \2\2\u01e5\u01ea\5b\62\2")
        buf.write("\u01e6\u01e7\f\4\2\2\u01e7\u01e8\7!\2\2\u01e8\u01ea\5")
        buf.write("b\62\2\u01e9\u01e3\3\2\2\2\u01e9\u01e6\3\2\2\2\u01ea\u01ed")
        buf.write("\3\2\2\2\u01eb\u01e9\3\2\2\2\u01eb\u01ec\3\2\2\2\u01ec")
        buf.write("a\3\2\2\2\u01ed\u01eb\3\2\2\2\u01ee\u01ef\b\62\1\2\u01ef")
        buf.write("\u01f0\5d\63\2\u01f0\u01fc\3\2\2\2\u01f1\u01f2\f\6\2\2")
        buf.write("\u01f2\u01f3\7\"\2\2\u01f3\u01fb\5d\63\2\u01f4\u01f5\f")
        buf.write("\5\2\2\u01f5\u01f6\7#\2\2\u01f6\u01fb\5d\63\2\u01f7\u01f8")
        buf.write("\f\4\2\2\u01f8\u01f9\7$\2\2\u01f9\u01fb\5d\63\2\u01fa")
        buf.write("\u01f1\3\2\2\2\u01fa\u01f4\3\2\2\2\u01fa\u01f7\3\2\2\2")
        buf.write("\u01fb\u01fe\3\2\2\2\u01fc\u01fa\3\2\2\2\u01fc\u01fd\3")
        buf.write("\2\2\2\u01fdc\3\2\2\2\u01fe\u01fc\3\2\2\2\u01ff\u0200")
        buf.write("\7%\2\2\u0200\u0203\5d\63\2\u0201\u0203\5f\64\2\u0202")
        buf.write("\u01ff\3\2\2\2\u0202\u0201\3\2\2\2\u0203e\3\2\2\2\u0204")
        buf.write("\u0205\7!\2\2\u0205\u0208\5f\64\2\u0206\u0208\5h\65\2")
        buf.write("\u0207\u0204\3\2\2\2\u0207\u0206\3\2\2\2\u0208g\3\2\2")
        buf.write("\2\u0209\u020a\b\65\1\2\u020a\u020b\5l\67\2\u020b\u0213")
        buf.write("\3\2\2\2\u020c\u020d\f\4\2\2\u020d\u020e\7\t\2\2\u020e")
        buf.write("\u020f\5Z.\2\u020f\u0210\7\n\2\2\u0210\u0212\3\2\2\2\u0211")
        buf.write("\u020c\3\2\2\2\u0212\u0215\3\2\2\2\u0213\u0211\3\2\2\2")
        buf.write("\u0213\u0214\3\2\2\2\u0214i\3\2\2\2\u0215\u0213\3\2\2")
        buf.write("\2\u0216\u0217\7\t\2\2\u0217\u0218\5Z.\2\u0218\u0219\7")
        buf.write("\n\2\2\u0219\u0220\3\2\2\2\u021a\u021b\7\t\2\2\u021b\u021c")
        buf.write("\5Z.\2\u021c\u021d\7\n\2\2\u021d\u021e\5j\66\2\u021e\u0220")
        buf.write("\3\2\2\2\u021f\u0216\3\2\2\2\u021f\u021a\3\2\2\2\u0220")
        buf.write("k\3\2\2\2\u0221\u0222\b\67\1\2\u0222\u0225\5B\"\2\u0223")
        buf.write("\u0225\5n8\2\u0224\u0221\3\2\2\2\u0224\u0223\3\2\2\2\u0225")
        buf.write("\u0232\3\2\2\2\u0226\u0227\f\6\2\2\u0227\u0228\7\61\2")
        buf.write("\2\u0228\u0229\7A\2\2\u0229\u022a\7\5\2\2\u022a\u022b")
        buf.write("\5v<\2\u022b\u022c\7\6\2\2\u022c\u0231\3\2\2\2\u022d\u022e")
        buf.write("\f\5\2\2\u022e\u022f\7\61\2\2\u022f\u0231\7A\2\2\u0230")
        buf.write("\u0226\3\2\2\2\u0230\u022d\3\2\2\2\u0231\u0234\3\2\2\2")
        buf.write("\u0232\u0230\3\2\2\2\u0232\u0233\3\2\2\2\u0233m\3\2\2")
        buf.write("\2\u0234\u0232\3\2\2\2\u0235\u0236\7A\2\2\u0236\u0237")
        buf.write("\7\63\2\2\u0237\u0238\7B\2\2\u0238\u0239\7\5\2\2\u0239")
        buf.write("\u023a\5v<\2\u023a\u023b\7\6\2\2\u023b\u0241\3\2\2\2\u023c")
        buf.write("\u023d\7A\2\2\u023d\u023e\7\63\2\2\u023e\u0241\7B\2\2")
        buf.write("\u023f\u0241\5p9\2\u0240\u0235\3\2\2\2\u0240\u023c\3\2")
        buf.write("\2\2\u0240\u023f\3\2\2\2\u0241o\3\2\2\2\u0242\u0243\7")
        buf.write("\35\2\2\u0243\u0244\5p9\2\u0244\u0245\7\5\2\2\u0245\u0246")
        buf.write("\5v<\2\u0246\u0247\7\6\2\2\u0247\u024a\3\2\2\2\u0248\u024a")
        buf.write("\5r:\2\u0249\u0242\3\2\2\2\u0249\u0248\3\2\2\2\u024aq")
        buf.write("\3\2\2\2\u024b\u0256\7;\2\2\u024c\u0256\7<\2\2\u024d\u0256")
        buf.write("\5T+\2\u024e\u0256\7:\2\2\u024f\u0256\7@\2\2\u0250\u0256")
        buf.write("\7=\2\2\u0251\u0256\7A\2\2\u0252\u0256\7B\2\2\u0253\u0256")
        buf.write("\7\37\2\2\u0254\u0256\5t;\2\u0255\u024b\3\2\2\2\u0255")
        buf.write("\u024c\3\2\2\2\u0255\u024d\3\2\2\2\u0255\u024e\3\2\2\2")
        buf.write("\u0255\u024f\3\2\2\2\u0255\u0250\3\2\2\2\u0255\u0251\3")
        buf.write("\2\2\2\u0255\u0252\3\2\2\2\u0255\u0253\3\2\2\2\u0255\u0254")
        buf.write("\3\2\2\2\u0256s\3\2\2\2\u0257\u0258\7\5\2\2\u0258\u0259")
        buf.write("\5Z.\2\u0259\u025a\7\6\2\2\u025au\3\2\2\2\u025b\u025e")
        buf.write("\5x=\2\u025c\u025e\3\2\2\2\u025d\u025b\3\2\2\2\u025d\u025c")
        buf.write("\3\2\2\2\u025ew\3\2\2\2\u025f\u0260\5Z.\2\u0260\u0261")
        buf.write("\7\f\2\2\u0261\u0262\5x=\2\u0262\u0265\3\2\2\2\u0263\u0265")
        buf.write("\5Z.\2\u0264\u025f\3\2\2\2\u0264\u0263\3\2\2\2\u0265y")
        buf.write("\3\2\2\2\u0266\u0267\7A\2\2\u0267\u0268\7\f\2\2\u0268")
        buf.write("\u026b\5z>\2\u0269\u026b\7A\2\2\u026a\u0266\3\2\2\2\u026a")
        buf.write("\u0269\3\2\2\2\u026b{\3\2\2\2\u026c\u026d\t\2\2\2\u026d")
        buf.write("\u026e\7\f\2\2\u026e\u0271\5|?\2\u026f\u0271\t\2\2\2\u0270")
        buf.write("\u026c\3\2\2\2\u0270\u026f\3\2\2\2\u0271}\3\2\2\2\67\u0080")
        buf.write("\u0082\u008a\u0094\u009c\u00a2\u00a9\u00c3\u00ca\u00d4")
        buf.write("\u00dc\u00e2\u00f7\u0101\u0114\u011a\u0125\u0135\u013c")
        buf.write("\u0152\u0155\u015a\u015d\u016e\u0177\u0179\u0188\u018b")
        buf.write("\u0195\u01a3\u01aa\u01b5\u01d0\u01db\u01dd\u01e9\u01eb")
        buf.write("\u01fa\u01fc\u0202\u0207\u0213\u021f\u0224\u0230\u0232")
        buf.write("\u0240\u0249\u0255\u025d\u0264\u026a\u0270")
        return buf.getvalue()


class D96Parser ( Parser ):

    grammarFileName = "D96.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'Val'", "'Var'", "'('", "')'", "'{'", 
                     "'}'", "'['", "']'", "';'", "','", "':'", "'Break'", 
                     "'Continue'", "'If'", "'Elseif'", "'Else'", "'Foreach'", 
                     "'True'", "'False'", "'Array'", "'In'", "'Boolean'", 
                     "'Return'", "'Null'", "'Constructor'", "'Destructor'", 
                     "'New'", "'By'", "'Self'", "'+'", "'-'", "'*'", "'/'", 
                     "'%'", "'!'", "'&&'", "'||'", "'=='", "'='", "'!='", 
                     "'>'", "'>='", "'<'", "'<='", "'==.'", "'+.'", "'.'", 
                     "'..'", "'::'", "'Program'", "'main'", "'Class'", "'Float'", 
                     "'String'", "'Int'" ]

    symbolicNames = [ "<INVALID>", "VAL", "VAR", "LP", "RP", "LCB", "RCB", 
                      "LSB", "RSB", "SEMI", "COMMA", "COLON", "BREAK", "CONTINUE", 
                      "IF", "ELSEIF", "ELSE", "FOREACH", "TRUE", "FALSE", 
                      "ARRAY", "IN", "BOOLEAN", "RETURN", "NULL", "CONSTRUCTOR", 
                      "DESTRUCTOR", "NEW", "BY", "SELF", "ADD", "SUB", "MUL", 
                      "DIV", "MOD", "NOT", "AND", "OR", "EQUAL", "ASSIGN", 
                      "NOTEQUAL", "GT", "GTE", "LT", "LTE", "EQUAL_STR", 
                      "ADD_STR", "DOT", "DOTDOT", "SCOPE", "PROGRAM", "MAIN", 
                      "CLASS", "FLOAT_TYPE", "STRING", "INT_TYPE", "BOOL_LITERAL", 
                      "ARRAY_SIZE", "INTEGER_LITERAL", "STRING_LITERAL", 
                      "ILLEGAL_ESCAPE", "UNCLOSE_STRING", "REAL_LITERAL", 
                      "NORMAL_ID", "DOLLAR_ID", "BLOCK_COMMENT", "WS", "ERROR_CHAR" ]

    RULE_program = 0
    RULE_class_declares_list = 1
    RULE_class_declare = 2
    RULE_extend = 3
    RULE_class_members = 4
    RULE_member_list = 5
    RULE_members = 6
    RULE_member = 7
    RULE_main_method = 8
    RULE_constructor_method = 9
    RULE_destructor_method = 10
    RULE_method_declare = 11
    RULE_param_list = 12
    RULE_parameters = 13
    RULE_parameter = 14
    RULE_block_statements = 15
    RULE_statements_list = 16
    RULE_statements = 17
    RULE_statement = 18
    RULE_break_statement = 19
    RULE_continue_statement = 20
    RULE_return_statement = 21
    RULE_assign_statement = 22
    RULE_if_else_statement = 23
    RULE_elseif_stmt_list = 24
    RULE_elseif_stmts = 25
    RULE_elseif_stmt = 26
    RULE_else_stmt = 27
    RULE_foreach_statement = 28
    RULE_increment = 29
    RULE_lhs = 30
    RULE_element_index = 31
    RULE_function_call = 32
    RULE_static_attr_call = 33
    RULE_static_method_call = 34
    RULE_instance_attr_call = 35
    RULE_instance_method_call = 36
    RULE_var_declare = 37
    RULE_dec_and_init_list = 38
    RULE_pair = 39
    RULE_array_type = 40
    RULE_array_literal = 41
    RULE_literal_list = 42
    RULE_literals = 43
    RULE_exp = 44
    RULE_exp0 = 45
    RULE_exp1 = 46
    RULE_exp2 = 47
    RULE_exp3 = 48
    RULE_exp4 = 49
    RULE_exp5 = 50
    RULE_exp6 = 51
    RULE_index_operator = 52
    RULE_exp7 = 53
    RULE_exp8 = 54
    RULE_exp9 = 55
    RULE_exp10 = 56
    RULE_exp11 = 57
    RULE_list_exp = 58
    RULE_exps = 59
    RULE_normal_id_list = 60
    RULE_id_list = 61

    ruleNames =  [ "program", "class_declares_list", "class_declare", "extend", 
                   "class_members", "member_list", "members", "member", 
                   "main_method", "constructor_method", "destructor_method", 
                   "method_declare", "param_list", "parameters", "parameter", 
                   "block_statements", "statements_list", "statements", 
                   "statement", "break_statement", "continue_statement", 
                   "return_statement", "assign_statement", "if_else_statement", 
                   "elseif_stmt_list", "elseif_stmts", "elseif_stmt", "else_stmt", 
                   "foreach_statement", "increment", "lhs", "element_index", 
                   "function_call", "static_attr_call", "static_method_call", 
                   "instance_attr_call", "instance_method_call", "var_declare", 
                   "dec_and_init_list", "pair", "array_type", "array_literal", 
                   "literal_list", "literals", "exp", "exp0", "exp1", "exp2", 
                   "exp3", "exp4", "exp5", "exp6", "index_operator", "exp7", 
                   "exp8", "exp9", "exp10", "exp11", "list_exp", "exps", 
                   "normal_id_list", "id_list" ]

    EOF = Token.EOF
    VAL=1
    VAR=2
    LP=3
    RP=4
    LCB=5
    RCB=6
    LSB=7
    RSB=8
    SEMI=9
    COMMA=10
    COLON=11
    BREAK=12
    CONTINUE=13
    IF=14
    ELSEIF=15
    ELSE=16
    FOREACH=17
    TRUE=18
    FALSE=19
    ARRAY=20
    IN=21
    BOOLEAN=22
    RETURN=23
    NULL=24
    CONSTRUCTOR=25
    DESTRUCTOR=26
    NEW=27
    BY=28
    SELF=29
    ADD=30
    SUB=31
    MUL=32
    DIV=33
    MOD=34
    NOT=35
    AND=36
    OR=37
    EQUAL=38
    ASSIGN=39
    NOTEQUAL=40
    GT=41
    GTE=42
    LT=43
    LTE=44
    EQUAL_STR=45
    ADD_STR=46
    DOT=47
    DOTDOT=48
    SCOPE=49
    PROGRAM=50
    MAIN=51
    CLASS=52
    FLOAT_TYPE=53
    STRING=54
    INT_TYPE=55
    BOOL_LITERAL=56
    ARRAY_SIZE=57
    INTEGER_LITERAL=58
    STRING_LITERAL=59
    ILLEGAL_ESCAPE=60
    UNCLOSE_STRING=61
    REAL_LITERAL=62
    NORMAL_ID=63
    DOLLAR_ID=64
    BLOCK_COMMENT=65
    WS=66
    ERROR_CHAR=67

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

        def EOF(self):
            return self.getToken(D96Parser.EOF, 0)

        def class_declares_list(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(D96Parser.Class_declares_listContext)
            else:
                return self.getTypedRuleContext(D96Parser.Class_declares_listContext,i)


        def assign_statement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(D96Parser.Assign_statementContext)
            else:
                return self.getTypedRuleContext(D96Parser.Assign_statementContext,i)


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
            self.state = 126 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 126
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [D96Parser.CLASS]:
                    self.state = 124
                    self.class_declares_list()
                    pass
                elif token in [D96Parser.LP, D96Parser.ARRAY, D96Parser.NEW, D96Parser.SELF, D96Parser.SUB, D96Parser.NOT, D96Parser.DOT, D96Parser.BOOL_LITERAL, D96Parser.ARRAY_SIZE, D96Parser.INTEGER_LITERAL, D96Parser.STRING_LITERAL, D96Parser.REAL_LITERAL, D96Parser.NORMAL_ID, D96Parser.DOLLAR_ID]:
                    self.state = 125
                    self.assign_statement()
                    pass
                else:
                    raise NoViableAltException(self)

                self.state = 128 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (((((_la - 3)) & ~0x3f) == 0 and ((1 << (_la - 3)) & ((1 << (D96Parser.LP - 3)) | (1 << (D96Parser.ARRAY - 3)) | (1 << (D96Parser.NEW - 3)) | (1 << (D96Parser.SELF - 3)) | (1 << (D96Parser.SUB - 3)) | (1 << (D96Parser.NOT - 3)) | (1 << (D96Parser.DOT - 3)) | (1 << (D96Parser.CLASS - 3)) | (1 << (D96Parser.BOOL_LITERAL - 3)) | (1 << (D96Parser.ARRAY_SIZE - 3)) | (1 << (D96Parser.INTEGER_LITERAL - 3)) | (1 << (D96Parser.STRING_LITERAL - 3)) | (1 << (D96Parser.REAL_LITERAL - 3)) | (1 << (D96Parser.NORMAL_ID - 3)) | (1 << (D96Parser.DOLLAR_ID - 3)))) != 0)):
                    break

            self.state = 130
            self.match(D96Parser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Class_declares_listContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def class_declare(self):
            return self.getTypedRuleContext(D96Parser.Class_declareContext,0)


        def class_declares_list(self):
            return self.getTypedRuleContext(D96Parser.Class_declares_listContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_class_declares_list

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitClass_declares_list" ):
                return visitor.visitClass_declares_list(self)
            else:
                return visitor.visitChildren(self)




    def class_declares_list(self):

        localctx = D96Parser.Class_declares_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_class_declares_list)
        try:
            self.state = 136
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,2,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 132
                self.class_declare()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 133
                self.class_declare()
                self.state = 134
                self.class_declares_list()
                pass


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


        def class_members(self):
            return self.getTypedRuleContext(D96Parser.Class_membersContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_class_declare

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitClass_declare" ):
                return visitor.visitClass_declare(self)
            else:
                return visitor.visitChildren(self)




    def class_declare(self):

        localctx = D96Parser.Class_declareContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_class_declare)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 138
            self.match(D96Parser.CLASS)
            self.state = 139
            self.match(D96Parser.NORMAL_ID)
            self.state = 140
            self.extend()
            self.state = 141
            self.class_members()
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
        self.enterRule(localctx, 6, self.RULE_extend)
        try:
            self.state = 146
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [D96Parser.COLON]:
                self.enterOuterAlt(localctx, 1)
                self.state = 143
                self.match(D96Parser.COLON)
                self.state = 144
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


    class Class_membersContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LCB(self):
            return self.getToken(D96Parser.LCB, 0)

        def member_list(self):
            return self.getTypedRuleContext(D96Parser.Member_listContext,0)


        def RCB(self):
            return self.getToken(D96Parser.RCB, 0)

        def getRuleIndex(self):
            return D96Parser.RULE_class_members

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitClass_members" ):
                return visitor.visitClass_members(self)
            else:
                return visitor.visitChildren(self)




    def class_members(self):

        localctx = D96Parser.Class_membersContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_class_members)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 148
            self.match(D96Parser.LCB)
            self.state = 149
            self.member_list()
            self.state = 150
            self.match(D96Parser.RCB)
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

        def members(self):
            return self.getTypedRuleContext(D96Parser.MembersContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_member_list

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMember_list" ):
                return visitor.visitMember_list(self)
            else:
                return visitor.visitChildren(self)




    def member_list(self):

        localctx = D96Parser.Member_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_member_list)
        try:
            self.state = 154
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [D96Parser.VAL, D96Parser.VAR, D96Parser.CONSTRUCTOR, D96Parser.DESTRUCTOR, D96Parser.MAIN, D96Parser.NORMAL_ID, D96Parser.DOLLAR_ID]:
                self.enterOuterAlt(localctx, 1)
                self.state = 152
                self.members()
                pass
            elif token in [D96Parser.RCB]:
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


    class MembersContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def member(self):
            return self.getTypedRuleContext(D96Parser.MemberContext,0)


        def members(self):
            return self.getTypedRuleContext(D96Parser.MembersContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_members

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMembers" ):
                return visitor.visitMembers(self)
            else:
                return visitor.visitChildren(self)




    def members(self):

        localctx = D96Parser.MembersContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_members)
        try:
            self.state = 160
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,5,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 156
                self.member()
                self.state = 157
                self.members()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 159
                self.member()
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


        def constructor_method(self):
            return self.getTypedRuleContext(D96Parser.Constructor_methodContext,0)


        def destructor_method(self):
            return self.getTypedRuleContext(D96Parser.Destructor_methodContext,0)


        def main_method(self):
            return self.getTypedRuleContext(D96Parser.Main_methodContext,0)


        def method_declare(self):
            return self.getTypedRuleContext(D96Parser.Method_declareContext,0)


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
            self.state = 167
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [D96Parser.VAL, D96Parser.VAR]:
                self.enterOuterAlt(localctx, 1)
                self.state = 162
                self.var_declare()
                pass
            elif token in [D96Parser.CONSTRUCTOR]:
                self.enterOuterAlt(localctx, 2)
                self.state = 163
                self.constructor_method()
                pass
            elif token in [D96Parser.DESTRUCTOR]:
                self.enterOuterAlt(localctx, 3)
                self.state = 164
                self.destructor_method()
                pass
            elif token in [D96Parser.MAIN]:
                self.enterOuterAlt(localctx, 4)
                self.state = 165
                self.main_method()
                pass
            elif token in [D96Parser.NORMAL_ID, D96Parser.DOLLAR_ID]:
                self.enterOuterAlt(localctx, 5)
                self.state = 166
                self.method_declare()
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


    class Main_methodContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def MAIN(self):
            return self.getToken(D96Parser.MAIN, 0)

        def LP(self):
            return self.getToken(D96Parser.LP, 0)

        def RP(self):
            return self.getToken(D96Parser.RP, 0)

        def block_statements(self):
            return self.getTypedRuleContext(D96Parser.Block_statementsContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_main_method

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMain_method" ):
                return visitor.visitMain_method(self)
            else:
                return visitor.visitChildren(self)




    def main_method(self):

        localctx = D96Parser.Main_methodContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_main_method)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 169
            self.match(D96Parser.MAIN)
            self.state = 170
            self.match(D96Parser.LP)
            self.state = 171
            self.match(D96Parser.RP)
            self.state = 172
            self.block_statements()
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

        def block_statements(self):
            return self.getTypedRuleContext(D96Parser.Block_statementsContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_constructor_method

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitConstructor_method" ):
                return visitor.visitConstructor_method(self)
            else:
                return visitor.visitChildren(self)




    def constructor_method(self):

        localctx = D96Parser.Constructor_methodContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_constructor_method)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 174
            self.match(D96Parser.CONSTRUCTOR)
            self.state = 175
            self.match(D96Parser.LP)
            self.state = 176
            self.param_list()
            self.state = 177
            self.match(D96Parser.RP)
            self.state = 178
            self.block_statements()
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

        def block_statements(self):
            return self.getTypedRuleContext(D96Parser.Block_statementsContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_destructor_method

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDestructor_method" ):
                return visitor.visitDestructor_method(self)
            else:
                return visitor.visitChildren(self)




    def destructor_method(self):

        localctx = D96Parser.Destructor_methodContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_destructor_method)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 180
            self.match(D96Parser.DESTRUCTOR)
            self.state = 181
            self.match(D96Parser.LP)
            self.state = 182
            self.match(D96Parser.RP)
            self.state = 183
            self.block_statements()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Method_declareContext(ParserRuleContext):
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

        def block_statements(self):
            return self.getTypedRuleContext(D96Parser.Block_statementsContext,0)


        def NORMAL_ID(self):
            return self.getToken(D96Parser.NORMAL_ID, 0)

        def DOLLAR_ID(self):
            return self.getToken(D96Parser.DOLLAR_ID, 0)

        def getRuleIndex(self):
            return D96Parser.RULE_method_declare

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMethod_declare" ):
                return visitor.visitMethod_declare(self)
            else:
                return visitor.visitChildren(self)




    def method_declare(self):

        localctx = D96Parser.Method_declareContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_method_declare)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 185
            _la = self._input.LA(1)
            if not(_la==D96Parser.NORMAL_ID or _la==D96Parser.DOLLAR_ID):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 186
            self.match(D96Parser.LP)
            self.state = 187
            self.param_list()
            self.state = 188
            self.match(D96Parser.RP)
            self.state = 189
            self.block_statements()
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

        def parameters(self):
            return self.getTypedRuleContext(D96Parser.ParametersContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_param_list

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitParam_list" ):
                return visitor.visitParam_list(self)
            else:
                return visitor.visitChildren(self)




    def param_list(self):

        localctx = D96Parser.Param_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_param_list)
        try:
            self.state = 193
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [D96Parser.NORMAL_ID]:
                self.enterOuterAlt(localctx, 1)
                self.state = 191
                self.parameters()
                pass
            elif token in [D96Parser.RP]:
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


    class ParametersContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def parameter(self):
            return self.getTypedRuleContext(D96Parser.ParameterContext,0)


        def SEMI(self):
            return self.getToken(D96Parser.SEMI, 0)

        def parameters(self):
            return self.getTypedRuleContext(D96Parser.ParametersContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_parameters

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitParameters" ):
                return visitor.visitParameters(self)
            else:
                return visitor.visitChildren(self)




    def parameters(self):

        localctx = D96Parser.ParametersContext(self, self._ctx, self.state)
        self.enterRule(localctx, 26, self.RULE_parameters)
        try:
            self.state = 200
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,8,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 195
                self.parameter()
                self.state = 196
                self.match(D96Parser.SEMI)
                self.state = 197
                self.parameters()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 199
                self.parameter()
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

        def normal_id_list(self):
            return self.getTypedRuleContext(D96Parser.Normal_id_listContext,0)


        def COLON(self):
            return self.getToken(D96Parser.COLON, 0)

        def BOOLEAN(self):
            return self.getToken(D96Parser.BOOLEAN, 0)

        def INT_TYPE(self):
            return self.getToken(D96Parser.INT_TYPE, 0)

        def FLOAT_TYPE(self):
            return self.getToken(D96Parser.FLOAT_TYPE, 0)

        def array_type(self):
            return self.getTypedRuleContext(D96Parser.Array_typeContext,0)


        def STRING(self):
            return self.getToken(D96Parser.STRING, 0)

        def NORMAL_ID(self):
            return self.getToken(D96Parser.NORMAL_ID, 0)

        def getRuleIndex(self):
            return D96Parser.RULE_parameter

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitParameter" ):
                return visitor.visitParameter(self)
            else:
                return visitor.visitChildren(self)




    def parameter(self):

        localctx = D96Parser.ParameterContext(self, self._ctx, self.state)
        self.enterRule(localctx, 28, self.RULE_parameter)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 202
            self.normal_id_list()
            self.state = 203
            self.match(D96Parser.COLON)
            self.state = 210
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [D96Parser.BOOLEAN]:
                self.state = 204
                self.match(D96Parser.BOOLEAN)
                pass
            elif token in [D96Parser.INT_TYPE]:
                self.state = 205
                self.match(D96Parser.INT_TYPE)
                pass
            elif token in [D96Parser.FLOAT_TYPE]:
                self.state = 206
                self.match(D96Parser.FLOAT_TYPE)
                pass
            elif token in [D96Parser.ARRAY]:
                self.state = 207
                self.array_type()
                pass
            elif token in [D96Parser.STRING]:
                self.state = 208
                self.match(D96Parser.STRING)
                pass
            elif token in [D96Parser.NORMAL_ID]:
                self.state = 209
                self.match(D96Parser.NORMAL_ID)
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


    class Block_statementsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LCB(self):
            return self.getToken(D96Parser.LCB, 0)

        def statements_list(self):
            return self.getTypedRuleContext(D96Parser.Statements_listContext,0)


        def RCB(self):
            return self.getToken(D96Parser.RCB, 0)

        def getRuleIndex(self):
            return D96Parser.RULE_block_statements

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBlock_statements" ):
                return visitor.visitBlock_statements(self)
            else:
                return visitor.visitChildren(self)




    def block_statements(self):

        localctx = D96Parser.Block_statementsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 30, self.RULE_block_statements)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 212
            self.match(D96Parser.LCB)
            self.state = 213
            self.statements_list()
            self.state = 214
            self.match(D96Parser.RCB)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Statements_listContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def statements(self):
            return self.getTypedRuleContext(D96Parser.StatementsContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_statements_list

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStatements_list" ):
                return visitor.visitStatements_list(self)
            else:
                return visitor.visitChildren(self)




    def statements_list(self):

        localctx = D96Parser.Statements_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 32, self.RULE_statements_list)
        try:
            self.state = 218
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [D96Parser.VAL, D96Parser.VAR, D96Parser.LP, D96Parser.BREAK, D96Parser.CONTINUE, D96Parser.IF, D96Parser.FOREACH, D96Parser.ARRAY, D96Parser.RETURN, D96Parser.NEW, D96Parser.SELF, D96Parser.SUB, D96Parser.NOT, D96Parser.DOT, D96Parser.BOOL_LITERAL, D96Parser.ARRAY_SIZE, D96Parser.INTEGER_LITERAL, D96Parser.STRING_LITERAL, D96Parser.REAL_LITERAL, D96Parser.NORMAL_ID, D96Parser.DOLLAR_ID]:
                self.enterOuterAlt(localctx, 1)
                self.state = 216
                self.statements()
                pass
            elif token in [D96Parser.RCB]:
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


    class StatementsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def statement(self):
            return self.getTypedRuleContext(D96Parser.StatementContext,0)


        def statements(self):
            return self.getTypedRuleContext(D96Parser.StatementsContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_statements

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStatements" ):
                return visitor.visitStatements(self)
            else:
                return visitor.visitChildren(self)




    def statements(self):

        localctx = D96Parser.StatementsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 34, self.RULE_statements)
        try:
            self.state = 224
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,11,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 220
                self.statement()
                self.state = 221
                self.statements()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 223
                self.statement()
                pass


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

        def assign_statement(self):
            return self.getTypedRuleContext(D96Parser.Assign_statementContext,0)


        def var_declare(self):
            return self.getTypedRuleContext(D96Parser.Var_declareContext,0)


        def break_statement(self):
            return self.getTypedRuleContext(D96Parser.Break_statementContext,0)


        def continue_statement(self):
            return self.getTypedRuleContext(D96Parser.Continue_statementContext,0)


        def return_statement(self):
            return self.getTypedRuleContext(D96Parser.Return_statementContext,0)


        def instance_method_call(self):
            return self.getTypedRuleContext(D96Parser.Instance_method_callContext,0)


        def SEMI(self):
            return self.getToken(D96Parser.SEMI, 0)

        def instance_attr_call(self):
            return self.getTypedRuleContext(D96Parser.Instance_attr_callContext,0)


        def static_attr_call(self):
            return self.getTypedRuleContext(D96Parser.Static_attr_callContext,0)


        def static_method_call(self):
            return self.getTypedRuleContext(D96Parser.Static_method_callContext,0)


        def if_else_statement(self):
            return self.getTypedRuleContext(D96Parser.If_else_statementContext,0)


        def foreach_statement(self):
            return self.getTypedRuleContext(D96Parser.Foreach_statementContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_statement

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStatement" ):
                return visitor.visitStatement(self)
            else:
                return visitor.visitChildren(self)




    def statement(self):

        localctx = D96Parser.StatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 36, self.RULE_statement)
        try:
            self.state = 245
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,12,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 226
                self.assign_statement()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 227
                self.var_declare()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 228
                self.break_statement()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 229
                self.continue_statement()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 230
                self.return_statement()
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 231
                self.instance_method_call()
                self.state = 232
                self.match(D96Parser.SEMI)
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 234
                self.instance_attr_call()
                self.state = 235
                self.match(D96Parser.SEMI)
                pass

            elif la_ == 8:
                self.enterOuterAlt(localctx, 8)
                self.state = 237
                self.static_attr_call()
                self.state = 238
                self.match(D96Parser.SEMI)
                pass

            elif la_ == 9:
                self.enterOuterAlt(localctx, 9)
                self.state = 240
                self.static_method_call()
                self.state = 241
                self.match(D96Parser.SEMI)
                pass

            elif la_ == 10:
                self.enterOuterAlt(localctx, 10)
                self.state = 243
                self.if_else_statement()
                pass

            elif la_ == 11:
                self.enterOuterAlt(localctx, 11)
                self.state = 244
                self.foreach_statement()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Break_statementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def BREAK(self):
            return self.getToken(D96Parser.BREAK, 0)

        def SEMI(self):
            return self.getToken(D96Parser.SEMI, 0)

        def getRuleIndex(self):
            return D96Parser.RULE_break_statement

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBreak_statement" ):
                return visitor.visitBreak_statement(self)
            else:
                return visitor.visitChildren(self)




    def break_statement(self):

        localctx = D96Parser.Break_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 38, self.RULE_break_statement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 247
            self.match(D96Parser.BREAK)
            self.state = 248
            self.match(D96Parser.SEMI)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Continue_statementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def CONTINUE(self):
            return self.getToken(D96Parser.CONTINUE, 0)

        def SEMI(self):
            return self.getToken(D96Parser.SEMI, 0)

        def getRuleIndex(self):
            return D96Parser.RULE_continue_statement

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitContinue_statement" ):
                return visitor.visitContinue_statement(self)
            else:
                return visitor.visitChildren(self)




    def continue_statement(self):

        localctx = D96Parser.Continue_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 40, self.RULE_continue_statement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 250
            self.match(D96Parser.CONTINUE)
            self.state = 251
            self.match(D96Parser.SEMI)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Return_statementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def RETURN(self):
            return self.getToken(D96Parser.RETURN, 0)

        def SEMI(self):
            return self.getToken(D96Parser.SEMI, 0)

        def exp(self):
            return self.getTypedRuleContext(D96Parser.ExpContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_return_statement

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitReturn_statement" ):
                return visitor.visitReturn_statement(self)
            else:
                return visitor.visitChildren(self)




    def return_statement(self):

        localctx = D96Parser.Return_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 42, self.RULE_return_statement)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 253
            self.match(D96Parser.RETURN)
            self.state = 255
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if ((((_la - 3)) & ~0x3f) == 0 and ((1 << (_la - 3)) & ((1 << (D96Parser.LP - 3)) | (1 << (D96Parser.ARRAY - 3)) | (1 << (D96Parser.NEW - 3)) | (1 << (D96Parser.SELF - 3)) | (1 << (D96Parser.SUB - 3)) | (1 << (D96Parser.NOT - 3)) | (1 << (D96Parser.BOOL_LITERAL - 3)) | (1 << (D96Parser.ARRAY_SIZE - 3)) | (1 << (D96Parser.INTEGER_LITERAL - 3)) | (1 << (D96Parser.STRING_LITERAL - 3)) | (1 << (D96Parser.REAL_LITERAL - 3)) | (1 << (D96Parser.NORMAL_ID - 3)) | (1 << (D96Parser.DOLLAR_ID - 3)))) != 0):
                self.state = 254
                self.exp()


            self.state = 257
            self.match(D96Parser.SEMI)
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


        def SEMI(self):
            return self.getToken(D96Parser.SEMI, 0)

        def getRuleIndex(self):
            return D96Parser.RULE_assign_statement

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAssign_statement" ):
                return visitor.visitAssign_statement(self)
            else:
                return visitor.visitChildren(self)




    def assign_statement(self):

        localctx = D96Parser.Assign_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 44, self.RULE_assign_statement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 259
            self.lhs()
            self.state = 260
            self.match(D96Parser.ASSIGN)
            self.state = 261
            self.exp()
            self.state = 262
            self.match(D96Parser.SEMI)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class If_else_statementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IF(self):
            return self.getToken(D96Parser.IF, 0)

        def LP(self):
            return self.getToken(D96Parser.LP, 0)

        def exp(self):
            return self.getTypedRuleContext(D96Parser.ExpContext,0)


        def RP(self):
            return self.getToken(D96Parser.RP, 0)

        def block_statements(self):
            return self.getTypedRuleContext(D96Parser.Block_statementsContext,0)


        def elseif_stmt_list(self):
            return self.getTypedRuleContext(D96Parser.Elseif_stmt_listContext,0)


        def else_stmt(self):
            return self.getTypedRuleContext(D96Parser.Else_stmtContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_if_else_statement

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIf_else_statement" ):
                return visitor.visitIf_else_statement(self)
            else:
                return visitor.visitChildren(self)




    def if_else_statement(self):

        localctx = D96Parser.If_else_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 46, self.RULE_if_else_statement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 264
            self.match(D96Parser.IF)
            self.state = 265
            self.match(D96Parser.LP)
            self.state = 266
            self.exp()
            self.state = 267
            self.match(D96Parser.RP)
            self.state = 268
            self.block_statements()
            self.state = 269
            self.elseif_stmt_list()
            self.state = 270
            self.else_stmt()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Elseif_stmt_listContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def elseif_stmts(self):
            return self.getTypedRuleContext(D96Parser.Elseif_stmtsContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_elseif_stmt_list

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitElseif_stmt_list" ):
                return visitor.visitElseif_stmt_list(self)
            else:
                return visitor.visitChildren(self)




    def elseif_stmt_list(self):

        localctx = D96Parser.Elseif_stmt_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 48, self.RULE_elseif_stmt_list)
        try:
            self.state = 274
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [D96Parser.ELSEIF]:
                self.enterOuterAlt(localctx, 1)
                self.state = 272
                self.elseif_stmts()
                pass
            elif token in [D96Parser.VAL, D96Parser.VAR, D96Parser.LP, D96Parser.RCB, D96Parser.BREAK, D96Parser.CONTINUE, D96Parser.IF, D96Parser.ELSE, D96Parser.FOREACH, D96Parser.ARRAY, D96Parser.RETURN, D96Parser.NEW, D96Parser.SELF, D96Parser.SUB, D96Parser.NOT, D96Parser.DOT, D96Parser.BOOL_LITERAL, D96Parser.ARRAY_SIZE, D96Parser.INTEGER_LITERAL, D96Parser.STRING_LITERAL, D96Parser.REAL_LITERAL, D96Parser.NORMAL_ID, D96Parser.DOLLAR_ID]:
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


    class Elseif_stmtsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def elseif_stmt(self):
            return self.getTypedRuleContext(D96Parser.Elseif_stmtContext,0)


        def elseif_stmts(self):
            return self.getTypedRuleContext(D96Parser.Elseif_stmtsContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_elseif_stmts

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitElseif_stmts" ):
                return visitor.visitElseif_stmts(self)
            else:
                return visitor.visitChildren(self)




    def elseif_stmts(self):

        localctx = D96Parser.Elseif_stmtsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 50, self.RULE_elseif_stmts)
        try:
            self.state = 280
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,15,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 276
                self.elseif_stmt()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 277
                self.elseif_stmt()
                self.state = 278
                self.elseif_stmts()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Elseif_stmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ELSEIF(self):
            return self.getToken(D96Parser.ELSEIF, 0)

        def LP(self):
            return self.getToken(D96Parser.LP, 0)

        def exp(self):
            return self.getTypedRuleContext(D96Parser.ExpContext,0)


        def RP(self):
            return self.getToken(D96Parser.RP, 0)

        def block_statements(self):
            return self.getTypedRuleContext(D96Parser.Block_statementsContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_elseif_stmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitElseif_stmt" ):
                return visitor.visitElseif_stmt(self)
            else:
                return visitor.visitChildren(self)




    def elseif_stmt(self):

        localctx = D96Parser.Elseif_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 52, self.RULE_elseif_stmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 282
            self.match(D96Parser.ELSEIF)
            self.state = 283
            self.match(D96Parser.LP)
            self.state = 284
            self.exp()
            self.state = 285
            self.match(D96Parser.RP)
            self.state = 286
            self.block_statements()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Else_stmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ELSE(self):
            return self.getToken(D96Parser.ELSE, 0)

        def block_statements(self):
            return self.getTypedRuleContext(D96Parser.Block_statementsContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_else_stmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitElse_stmt" ):
                return visitor.visitElse_stmt(self)
            else:
                return visitor.visitChildren(self)




    def else_stmt(self):

        localctx = D96Parser.Else_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 54, self.RULE_else_stmt)
        try:
            self.state = 291
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [D96Parser.ELSE]:
                self.enterOuterAlt(localctx, 1)
                self.state = 288
                self.match(D96Parser.ELSE)
                self.state = 289
                self.block_statements()
                pass
            elif token in [D96Parser.VAL, D96Parser.VAR, D96Parser.LP, D96Parser.RCB, D96Parser.BREAK, D96Parser.CONTINUE, D96Parser.IF, D96Parser.FOREACH, D96Parser.ARRAY, D96Parser.RETURN, D96Parser.NEW, D96Parser.SELF, D96Parser.SUB, D96Parser.NOT, D96Parser.DOT, D96Parser.BOOL_LITERAL, D96Parser.ARRAY_SIZE, D96Parser.INTEGER_LITERAL, D96Parser.STRING_LITERAL, D96Parser.REAL_LITERAL, D96Parser.NORMAL_ID, D96Parser.DOLLAR_ID]:
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


    class Foreach_statementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def FOREACH(self):
            return self.getToken(D96Parser.FOREACH, 0)

        def LP(self):
            return self.getToken(D96Parser.LP, 0)

        def IN(self):
            return self.getToken(D96Parser.IN, 0)

        def exp(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(D96Parser.ExpContext)
            else:
                return self.getTypedRuleContext(D96Parser.ExpContext,i)


        def DOTDOT(self):
            return self.getToken(D96Parser.DOTDOT, 0)

        def increment(self):
            return self.getTypedRuleContext(D96Parser.IncrementContext,0)


        def RP(self):
            return self.getToken(D96Parser.RP, 0)

        def block_statements(self):
            return self.getTypedRuleContext(D96Parser.Block_statementsContext,0)


        def NORMAL_ID(self):
            return self.getToken(D96Parser.NORMAL_ID, 0)

        def DOLLAR_ID(self):
            return self.getToken(D96Parser.DOLLAR_ID, 0)

        def getRuleIndex(self):
            return D96Parser.RULE_foreach_statement

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitForeach_statement" ):
                return visitor.visitForeach_statement(self)
            else:
                return visitor.visitChildren(self)




    def foreach_statement(self):

        localctx = D96Parser.Foreach_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 56, self.RULE_foreach_statement)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 293
            self.match(D96Parser.FOREACH)
            self.state = 294
            self.match(D96Parser.LP)
            self.state = 295
            _la = self._input.LA(1)
            if not(_la==D96Parser.NORMAL_ID or _la==D96Parser.DOLLAR_ID):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 296
            self.match(D96Parser.IN)
            self.state = 297
            self.exp()
            self.state = 298
            self.match(D96Parser.DOTDOT)
            self.state = 299
            self.exp()
            self.state = 300
            self.increment()
            self.state = 301
            self.match(D96Parser.RP)
            self.state = 302
            self.block_statements()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class IncrementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def BY(self):
            return self.getToken(D96Parser.BY, 0)

        def exp(self):
            return self.getTypedRuleContext(D96Parser.ExpContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_increment

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIncrement" ):
                return visitor.visitIncrement(self)
            else:
                return visitor.visitChildren(self)




    def increment(self):

        localctx = D96Parser.IncrementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 58, self.RULE_increment)
        try:
            self.state = 307
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [D96Parser.BY]:
                self.enterOuterAlt(localctx, 1)
                self.state = 304
                self.match(D96Parser.BY)
                self.state = 305
                self.exp()
                pass
            elif token in [D96Parser.RP]:
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


    class LhsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NORMAL_ID(self):
            return self.getToken(D96Parser.NORMAL_ID, 0)

        def DOLLAR_ID(self):
            return self.getToken(D96Parser.DOLLAR_ID, 0)

        def element_index(self):
            return self.getTypedRuleContext(D96Parser.Element_indexContext,0)


        def instance_attr_call(self):
            return self.getTypedRuleContext(D96Parser.Instance_attr_callContext,0)


        def static_attr_call(self):
            return self.getTypedRuleContext(D96Parser.Static_attr_callContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_lhs

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLhs" ):
                return visitor.visitLhs(self)
            else:
                return visitor.visitChildren(self)




    def lhs(self):

        localctx = D96Parser.LhsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 60, self.RULE_lhs)
        try:
            self.state = 314
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,18,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 309
                self.match(D96Parser.NORMAL_ID)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 310
                self.match(D96Parser.DOLLAR_ID)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 311
                self.element_index()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 312
                self.instance_attr_call()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 313
                self.static_attr_call()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Element_indexContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def exp(self):
            return self.getTypedRuleContext(D96Parser.ExpContext,0)


        def index_operator(self):
            return self.getTypedRuleContext(D96Parser.Index_operatorContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_element_index

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitElement_index" ):
                return visitor.visitElement_index(self)
            else:
                return visitor.visitChildren(self)




    def element_index(self):

        localctx = D96Parser.Element_indexContext(self, self._ctx, self.state)
        self.enterRule(localctx, 62, self.RULE_element_index)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 316
            self.exp()
            self.state = 317
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

        def list_exp(self):
            return self.getTypedRuleContext(D96Parser.List_expContext,0)


        def RP(self):
            return self.getToken(D96Parser.RP, 0)

        def NORMAL_ID(self):
            return self.getToken(D96Parser.NORMAL_ID, 0)

        def DOLLAR_ID(self):
            return self.getToken(D96Parser.DOLLAR_ID, 0)

        def getRuleIndex(self):
            return D96Parser.RULE_function_call

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFunction_call" ):
                return visitor.visitFunction_call(self)
            else:
                return visitor.visitChildren(self)




    def function_call(self):

        localctx = D96Parser.Function_callContext(self, self._ctx, self.state)
        self.enterRule(localctx, 64, self.RULE_function_call)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 319
            _la = self._input.LA(1)
            if not(_la==D96Parser.NORMAL_ID or _la==D96Parser.DOLLAR_ID):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 320
            self.match(D96Parser.LP)
            self.state = 321
            self.list_exp()
            self.state = 322
            self.match(D96Parser.RP)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Static_attr_callContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NORMAL_ID(self):
            return self.getToken(D96Parser.NORMAL_ID, 0)

        def SCOPE(self):
            return self.getToken(D96Parser.SCOPE, 0)

        def DOLLAR_ID(self):
            return self.getToken(D96Parser.DOLLAR_ID, 0)

        def getRuleIndex(self):
            return D96Parser.RULE_static_attr_call

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStatic_attr_call" ):
                return visitor.visitStatic_attr_call(self)
            else:
                return visitor.visitChildren(self)




    def static_attr_call(self):

        localctx = D96Parser.Static_attr_callContext(self, self._ctx, self.state)
        self.enterRule(localctx, 66, self.RULE_static_attr_call)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 324
            self.match(D96Parser.NORMAL_ID)
            self.state = 325
            self.match(D96Parser.SCOPE)
            self.state = 326
            self.match(D96Parser.DOLLAR_ID)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Static_method_callContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NORMAL_ID(self):
            return self.getToken(D96Parser.NORMAL_ID, 0)

        def SCOPE(self):
            return self.getToken(D96Parser.SCOPE, 0)

        def DOLLAR_ID(self):
            return self.getToken(D96Parser.DOLLAR_ID, 0)

        def LP(self):
            return self.getToken(D96Parser.LP, 0)

        def list_exp(self):
            return self.getTypedRuleContext(D96Parser.List_expContext,0)


        def RP(self):
            return self.getToken(D96Parser.RP, 0)

        def getRuleIndex(self):
            return D96Parser.RULE_static_method_call

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStatic_method_call" ):
                return visitor.visitStatic_method_call(self)
            else:
                return visitor.visitChildren(self)




    def static_method_call(self):

        localctx = D96Parser.Static_method_callContext(self, self._ctx, self.state)
        self.enterRule(localctx, 68, self.RULE_static_method_call)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 328
            self.match(D96Parser.NORMAL_ID)
            self.state = 329
            self.match(D96Parser.SCOPE)
            self.state = 330
            self.match(D96Parser.DOLLAR_ID)
            self.state = 331
            self.match(D96Parser.LP)
            self.state = 332
            self.list_exp()
            self.state = 333
            self.match(D96Parser.RP)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Instance_attr_callContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NORMAL_ID(self):
            return self.getToken(D96Parser.NORMAL_ID, 0)

        def exp(self):
            return self.getTypedRuleContext(D96Parser.ExpContext,0)


        def DOT(self):
            return self.getToken(D96Parser.DOT, 0)

        def getRuleIndex(self):
            return D96Parser.RULE_instance_attr_call

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitInstance_attr_call" ):
                return visitor.visitInstance_attr_call(self)
            else:
                return visitor.visitChildren(self)




    def instance_attr_call(self):

        localctx = D96Parser.Instance_attr_callContext(self, self._ctx, self.state)
        self.enterRule(localctx, 70, self.RULE_instance_attr_call)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 336
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,19,self._ctx)
            if la_ == 1:
                self.state = 335
                self.exp()


            self.state = 339
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==D96Parser.DOT:
                self.state = 338
                self.match(D96Parser.DOT)


            self.state = 341
            self.match(D96Parser.NORMAL_ID)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Instance_method_callContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NORMAL_ID(self):
            return self.getToken(D96Parser.NORMAL_ID, 0)

        def LP(self):
            return self.getToken(D96Parser.LP, 0)

        def list_exp(self):
            return self.getTypedRuleContext(D96Parser.List_expContext,0)


        def RP(self):
            return self.getToken(D96Parser.RP, 0)

        def exp(self):
            return self.getTypedRuleContext(D96Parser.ExpContext,0)


        def DOT(self):
            return self.getToken(D96Parser.DOT, 0)

        def getRuleIndex(self):
            return D96Parser.RULE_instance_method_call

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitInstance_method_call" ):
                return visitor.visitInstance_method_call(self)
            else:
                return visitor.visitChildren(self)




    def instance_method_call(self):

        localctx = D96Parser.Instance_method_callContext(self, self._ctx, self.state)
        self.enterRule(localctx, 72, self.RULE_instance_method_call)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 344
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,21,self._ctx)
            if la_ == 1:
                self.state = 343
                self.exp()


            self.state = 347
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==D96Parser.DOT:
                self.state = 346
                self.match(D96Parser.DOT)


            self.state = 349
            self.match(D96Parser.NORMAL_ID)
            self.state = 350
            self.match(D96Parser.LP)
            self.state = 351
            self.list_exp()
            self.state = 352
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

        def dec_and_init_list(self):
            return self.getTypedRuleContext(D96Parser.Dec_and_init_listContext,0)


        def SEMI(self):
            return self.getToken(D96Parser.SEMI, 0)

        def VAR(self):
            return self.getToken(D96Parser.VAR, 0)

        def VAL(self):
            return self.getToken(D96Parser.VAL, 0)

        def getRuleIndex(self):
            return D96Parser.RULE_var_declare

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVar_declare" ):
                return visitor.visitVar_declare(self)
            else:
                return visitor.visitChildren(self)




    def var_declare(self):

        localctx = D96Parser.Var_declareContext(self, self._ctx, self.state)
        self.enterRule(localctx, 74, self.RULE_var_declare)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 354
            _la = self._input.LA(1)
            if not(_la==D96Parser.VAL or _la==D96Parser.VAR):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 355
            self.dec_and_init_list()
            self.state = 356
            self.match(D96Parser.SEMI)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Dec_and_init_listContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def pair(self):
            return self.getTypedRuleContext(D96Parser.PairContext,0)


        def exp(self):
            return self.getTypedRuleContext(D96Parser.ExpContext,0)


        def NORMAL_ID(self):
            return self.getToken(D96Parser.NORMAL_ID, 0)

        def DOLLAR_ID(self):
            return self.getToken(D96Parser.DOLLAR_ID, 0)

        def COLON(self):
            return self.getToken(D96Parser.COLON, 0)

        def id_list(self):
            return self.getTypedRuleContext(D96Parser.Id_listContext,0)


        def normal_id_list(self):
            return self.getTypedRuleContext(D96Parser.Normal_id_listContext,0)


        def BOOLEAN(self):
            return self.getToken(D96Parser.BOOLEAN, 0)

        def INT_TYPE(self):
            return self.getToken(D96Parser.INT_TYPE, 0)

        def FLOAT_TYPE(self):
            return self.getToken(D96Parser.FLOAT_TYPE, 0)

        def array_type(self):
            return self.getTypedRuleContext(D96Parser.Array_typeContext,0)


        def STRING(self):
            return self.getToken(D96Parser.STRING, 0)

        def getRuleIndex(self):
            return D96Parser.RULE_dec_and_init_list

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDec_and_init_list" ):
                return visitor.visitDec_and_init_list(self)
            else:
                return visitor.visitChildren(self)




    def dec_and_init_list(self):

        localctx = D96Parser.Dec_and_init_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 76, self.RULE_dec_and_init_list)
        self._la = 0 # Token type
        try:
            self.state = 375
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,25,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 358
                _la = self._input.LA(1)
                if not(_la==D96Parser.NORMAL_ID or _la==D96Parser.DOLLAR_ID):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 359
                self.pair()
                self.state = 360
                self.exp()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 364
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,23,self._ctx)
                if la_ == 1:
                    self.state = 362
                    self.id_list()
                    pass

                elif la_ == 2:
                    self.state = 363
                    self.normal_id_list()
                    pass


                self.state = 366
                self.match(D96Parser.COLON)
                self.state = 373
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [D96Parser.BOOLEAN]:
                    self.state = 367
                    self.match(D96Parser.BOOLEAN)
                    pass
                elif token in [D96Parser.INT_TYPE]:
                    self.state = 368
                    self.match(D96Parser.INT_TYPE)
                    pass
                elif token in [D96Parser.FLOAT_TYPE]:
                    self.state = 369
                    self.match(D96Parser.FLOAT_TYPE)
                    pass
                elif token in [D96Parser.ARRAY]:
                    self.state = 370
                    self.array_type()
                    pass
                elif token in [D96Parser.STRING]:
                    self.state = 371
                    self.match(D96Parser.STRING)
                    pass
                elif token in [D96Parser.NORMAL_ID]:
                    self.state = 372
                    self.match(D96Parser.NORMAL_ID)
                    pass
                else:
                    raise NoViableAltException(self)

                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class PairContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(D96Parser.COMMA)
            else:
                return self.getToken(D96Parser.COMMA, i)

        def pair(self):
            return self.getTypedRuleContext(D96Parser.PairContext,0)


        def exp(self):
            return self.getTypedRuleContext(D96Parser.ExpContext,0)


        def NORMAL_ID(self):
            return self.getToken(D96Parser.NORMAL_ID, 0)

        def DOLLAR_ID(self):
            return self.getToken(D96Parser.DOLLAR_ID, 0)

        def COLON(self):
            return self.getToken(D96Parser.COLON, 0)

        def ASSIGN(self):
            return self.getToken(D96Parser.ASSIGN, 0)

        def BOOLEAN(self):
            return self.getToken(D96Parser.BOOLEAN, 0)

        def INT_TYPE(self):
            return self.getToken(D96Parser.INT_TYPE, 0)

        def FLOAT_TYPE(self):
            return self.getToken(D96Parser.FLOAT_TYPE, 0)

        def array_type(self):
            return self.getTypedRuleContext(D96Parser.Array_typeContext,0)


        def STRING(self):
            return self.getToken(D96Parser.STRING, 0)

        def getRuleIndex(self):
            return D96Parser.RULE_pair

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPair" ):
                return visitor.visitPair(self)
            else:
                return visitor.visitChildren(self)




    def pair(self):

        localctx = D96Parser.PairContext(self, self._ctx, self.state)
        self.enterRule(localctx, 78, self.RULE_pair)
        self._la = 0 # Token type
        try:
            self.state = 393
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [D96Parser.COMMA]:
                self.enterOuterAlt(localctx, 1)
                self.state = 377
                self.match(D96Parser.COMMA)
                self.state = 378
                _la = self._input.LA(1)
                if not(_la==D96Parser.NORMAL_ID or _la==D96Parser.DOLLAR_ID):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 379
                self.pair()
                self.state = 380
                self.exp()
                self.state = 381
                self.match(D96Parser.COMMA)
                pass
            elif token in [D96Parser.COLON]:
                self.enterOuterAlt(localctx, 2)
                self.state = 383
                self.match(D96Parser.COLON)
                self.state = 390
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [D96Parser.BOOLEAN]:
                    self.state = 384
                    self.match(D96Parser.BOOLEAN)
                    pass
                elif token in [D96Parser.INT_TYPE]:
                    self.state = 385
                    self.match(D96Parser.INT_TYPE)
                    pass
                elif token in [D96Parser.FLOAT_TYPE]:
                    self.state = 386
                    self.match(D96Parser.FLOAT_TYPE)
                    pass
                elif token in [D96Parser.ARRAY]:
                    self.state = 387
                    self.array_type()
                    pass
                elif token in [D96Parser.STRING]:
                    self.state = 388
                    self.match(D96Parser.STRING)
                    pass
                elif token in [D96Parser.NORMAL_ID]:
                    self.state = 389
                    self.match(D96Parser.NORMAL_ID)
                    pass
                else:
                    raise NoViableAltException(self)

                self.state = 392
                self.match(D96Parser.ASSIGN)
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


    class Array_typeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ARRAY(self):
            return self.getToken(D96Parser.ARRAY, 0)

        def LSB(self):
            return self.getToken(D96Parser.LSB, 0)

        def COMMA(self):
            return self.getToken(D96Parser.COMMA, 0)

        def ARRAY_SIZE(self):
            return self.getToken(D96Parser.ARRAY_SIZE, 0)

        def RSB(self):
            return self.getToken(D96Parser.RSB, 0)

        def BOOLEAN(self):
            return self.getToken(D96Parser.BOOLEAN, 0)

        def INT_TYPE(self):
            return self.getToken(D96Parser.INT_TYPE, 0)

        def FLOAT_TYPE(self):
            return self.getToken(D96Parser.FLOAT_TYPE, 0)

        def array_type(self):
            return self.getTypedRuleContext(D96Parser.Array_typeContext,0)


        def STRING(self):
            return self.getToken(D96Parser.STRING, 0)

        def NORMAL_ID(self):
            return self.getToken(D96Parser.NORMAL_ID, 0)

        def getRuleIndex(self):
            return D96Parser.RULE_array_type

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArray_type" ):
                return visitor.visitArray_type(self)
            else:
                return visitor.visitChildren(self)




    def array_type(self):

        localctx = D96Parser.Array_typeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 80, self.RULE_array_type)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 395
            self.match(D96Parser.ARRAY)
            self.state = 396
            self.match(D96Parser.LSB)
            self.state = 403
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [D96Parser.BOOLEAN]:
                self.state = 397
                self.match(D96Parser.BOOLEAN)
                pass
            elif token in [D96Parser.INT_TYPE]:
                self.state = 398
                self.match(D96Parser.INT_TYPE)
                pass
            elif token in [D96Parser.FLOAT_TYPE]:
                self.state = 399
                self.match(D96Parser.FLOAT_TYPE)
                pass
            elif token in [D96Parser.ARRAY]:
                self.state = 400
                self.array_type()
                pass
            elif token in [D96Parser.STRING]:
                self.state = 401
                self.match(D96Parser.STRING)
                pass
            elif token in [D96Parser.NORMAL_ID]:
                self.state = 402
                self.match(D96Parser.NORMAL_ID)
                pass
            else:
                raise NoViableAltException(self)

            self.state = 405
            self.match(D96Parser.COMMA)
            self.state = 406
            self.match(D96Parser.ARRAY_SIZE)
            self.state = 407
            self.match(D96Parser.RSB)

            #last = len(self._input.tokens)
            #for i in self._input.getTokens(0, last):
                #i.text mean for text of token
                #print(i.text)
                #if i.type == self.INTEGER_LITERAL:
                #    print(bin(int(i.text, 2)))

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Array_literalContext(ParserRuleContext):
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
            return D96Parser.RULE_array_literal

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArray_literal" ):
                return visitor.visitArray_literal(self)
            else:
                return visitor.visitChildren(self)




    def array_literal(self):

        localctx = D96Parser.Array_literalContext(self, self._ctx, self.state)
        self.enterRule(localctx, 82, self.RULE_array_literal)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 410
            self.match(D96Parser.ARRAY)
            self.state = 411
            self.match(D96Parser.LP)
            self.state = 412
            self.literal_list()
            self.state = 413
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

        def literals(self):
            return self.getTypedRuleContext(D96Parser.LiteralsContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_literal_list

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLiteral_list" ):
                return visitor.visitLiteral_list(self)
            else:
                return visitor.visitChildren(self)




    def literal_list(self):

        localctx = D96Parser.Literal_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 84, self.RULE_literal_list)
        try:
            self.state = 417
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [D96Parser.LP, D96Parser.ARRAY, D96Parser.NEW, D96Parser.SELF, D96Parser.SUB, D96Parser.NOT, D96Parser.BOOL_LITERAL, D96Parser.ARRAY_SIZE, D96Parser.INTEGER_LITERAL, D96Parser.STRING_LITERAL, D96Parser.REAL_LITERAL, D96Parser.NORMAL_ID, D96Parser.DOLLAR_ID]:
                self.enterOuterAlt(localctx, 1)
                self.state = 415
                self.literals()
                pass
            elif token in [D96Parser.RP]:
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


    class LiteralsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def exp(self):
            return self.getTypedRuleContext(D96Parser.ExpContext,0)


        def COMMA(self):
            return self.getToken(D96Parser.COMMA, 0)

        def literals(self):
            return self.getTypedRuleContext(D96Parser.LiteralsContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_literals

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLiterals" ):
                return visitor.visitLiterals(self)
            else:
                return visitor.visitChildren(self)




    def literals(self):

        localctx = D96Parser.LiteralsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 86, self.RULE_literals)
        try:
            self.state = 424
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,30,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 419
                self.exp()
                self.state = 420
                self.match(D96Parser.COMMA)
                self.state = 421
                self.literals()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 423
                self.exp()
                pass


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

        def exp0(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(D96Parser.Exp0Context)
            else:
                return self.getTypedRuleContext(D96Parser.Exp0Context,i)


        def EQUAL_STR(self):
            return self.getToken(D96Parser.EQUAL_STR, 0)

        def ADD_STR(self):
            return self.getToken(D96Parser.ADD_STR, 0)

        def getRuleIndex(self):
            return D96Parser.RULE_exp

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExp" ):
                return visitor.visitExp(self)
            else:
                return visitor.visitChildren(self)




    def exp(self):

        localctx = D96Parser.ExpContext(self, self._ctx, self.state)
        self.enterRule(localctx, 88, self.RULE_exp)
        try:
            self.state = 435
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,31,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 426
                self.exp0()
                self.state = 427
                self.match(D96Parser.EQUAL_STR)
                self.state = 428
                self.exp0()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 430
                self.exp0()
                self.state = 431
                self.match(D96Parser.ADD_STR)
                self.state = 432
                self.exp0()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 434
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

        def EQUAL(self):
            return self.getToken(D96Parser.EQUAL, 0)

        def NOTEQUAL(self):
            return self.getToken(D96Parser.NOTEQUAL, 0)

        def GTE(self):
            return self.getToken(D96Parser.GTE, 0)

        def getRuleIndex(self):
            return D96Parser.RULE_exp0

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExp0" ):
                return visitor.visitExp0(self)
            else:
                return visitor.visitChildren(self)




    def exp0(self):

        localctx = D96Parser.Exp0Context(self, self._ctx, self.state)
        self.enterRule(localctx, 90, self.RULE_exp0)
        try:
            self.state = 462
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,32,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 437
                self.exp1(0)
                self.state = 438
                self.match(D96Parser.LT)
                self.state = 439
                self.exp1(0)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 441
                self.exp1(0)
                self.state = 442
                self.match(D96Parser.LTE)
                self.state = 443
                self.exp1(0)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 445
                self.exp1(0)
                self.state = 446
                self.match(D96Parser.GT)
                self.state = 447
                self.exp1(0)
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 449
                self.exp1(0)
                self.state = 450
                self.match(D96Parser.EQUAL)
                self.state = 451
                self.exp1(0)
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 453
                self.exp1(0)
                self.state = 454
                self.match(D96Parser.NOTEQUAL)
                self.state = 455
                self.exp1(0)
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 457
                self.exp1(0)
                self.state = 458
                self.match(D96Parser.GTE)
                self.state = 459
                self.exp1(0)
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 461
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
        _startState = 92
        self.enterRecursionRule(localctx, 92, self.RULE_exp1, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 465
            self.exp2(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 475
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,34,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 473
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,33,self._ctx)
                    if la_ == 1:
                        localctx = D96Parser.Exp1Context(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_exp1)
                        self.state = 467
                        if not self.precpred(self._ctx, 3):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 3)")
                        self.state = 468
                        self.match(D96Parser.AND)
                        self.state = 469
                        self.exp2(0)
                        pass

                    elif la_ == 2:
                        localctx = D96Parser.Exp1Context(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_exp1)
                        self.state = 470
                        if not self.precpred(self._ctx, 2):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                        self.state = 471
                        self.match(D96Parser.OR)
                        self.state = 472
                        self.exp2(0)
                        pass

             
                self.state = 477
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,34,self._ctx)

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
        _startState = 94
        self.enterRecursionRule(localctx, 94, self.RULE_exp2, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 479
            self.exp3(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 489
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,36,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 487
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,35,self._ctx)
                    if la_ == 1:
                        localctx = D96Parser.Exp2Context(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_exp2)
                        self.state = 481
                        if not self.precpred(self._ctx, 3):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 3)")
                        self.state = 482
                        self.match(D96Parser.ADD)
                        self.state = 483
                        self.exp3(0)
                        pass

                    elif la_ == 2:
                        localctx = D96Parser.Exp2Context(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_exp2)
                        self.state = 484
                        if not self.precpred(self._ctx, 2):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                        self.state = 485
                        self.match(D96Parser.SUB)
                        self.state = 486
                        self.exp3(0)
                        pass

             
                self.state = 491
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,36,self._ctx)

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
        _startState = 96
        self.enterRecursionRule(localctx, 96, self.RULE_exp3, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 493
            self.exp4()
            self._ctx.stop = self._input.LT(-1)
            self.state = 506
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,38,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 504
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,37,self._ctx)
                    if la_ == 1:
                        localctx = D96Parser.Exp3Context(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_exp3)
                        self.state = 495
                        if not self.precpred(self._ctx, 4):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 4)")
                        self.state = 496
                        self.match(D96Parser.MUL)
                        self.state = 497
                        self.exp4()
                        pass

                    elif la_ == 2:
                        localctx = D96Parser.Exp3Context(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_exp3)
                        self.state = 498
                        if not self.precpred(self._ctx, 3):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 3)")
                        self.state = 499
                        self.match(D96Parser.DIV)
                        self.state = 500
                        self.exp4()
                        pass

                    elif la_ == 3:
                        localctx = D96Parser.Exp3Context(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_exp3)
                        self.state = 501
                        if not self.precpred(self._ctx, 2):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                        self.state = 502
                        self.match(D96Parser.MOD)
                        self.state = 503
                        self.exp4()
                        pass

             
                self.state = 508
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,38,self._ctx)

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
        self.enterRule(localctx, 98, self.RULE_exp4)
        try:
            self.state = 512
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [D96Parser.NOT]:
                self.enterOuterAlt(localctx, 1)
                self.state = 509
                self.match(D96Parser.NOT)
                self.state = 510
                self.exp4()
                pass
            elif token in [D96Parser.LP, D96Parser.ARRAY, D96Parser.NEW, D96Parser.SELF, D96Parser.SUB, D96Parser.BOOL_LITERAL, D96Parser.ARRAY_SIZE, D96Parser.INTEGER_LITERAL, D96Parser.STRING_LITERAL, D96Parser.REAL_LITERAL, D96Parser.NORMAL_ID, D96Parser.DOLLAR_ID]:
                self.enterOuterAlt(localctx, 2)
                self.state = 511
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
        self.enterRule(localctx, 100, self.RULE_exp5)
        try:
            self.state = 517
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [D96Parser.SUB]:
                self.enterOuterAlt(localctx, 1)
                self.state = 514
                self.match(D96Parser.SUB)
                self.state = 515
                self.exp5()
                pass
            elif token in [D96Parser.LP, D96Parser.ARRAY, D96Parser.NEW, D96Parser.SELF, D96Parser.BOOL_LITERAL, D96Parser.ARRAY_SIZE, D96Parser.INTEGER_LITERAL, D96Parser.STRING_LITERAL, D96Parser.REAL_LITERAL, D96Parser.NORMAL_ID, D96Parser.DOLLAR_ID]:
                self.enterOuterAlt(localctx, 2)
                self.state = 516
                self.exp6(0)
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


        def exp6(self):
            return self.getTypedRuleContext(D96Parser.Exp6Context,0)


        def LSB(self):
            return self.getToken(D96Parser.LSB, 0)

        def exp(self):
            return self.getTypedRuleContext(D96Parser.ExpContext,0)


        def RSB(self):
            return self.getToken(D96Parser.RSB, 0)

        def getRuleIndex(self):
            return D96Parser.RULE_exp6

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExp6" ):
                return visitor.visitExp6(self)
            else:
                return visitor.visitChildren(self)



    def exp6(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = D96Parser.Exp6Context(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 102
        self.enterRecursionRule(localctx, 102, self.RULE_exp6, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 520
            self.exp7(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 529
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,41,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = D96Parser.Exp6Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_exp6)
                    self.state = 522
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 523
                    self.match(D96Parser.LSB)
                    self.state = 524
                    self.exp()
                    self.state = 525
                    self.match(D96Parser.RSB) 
                self.state = 531
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,41,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
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
        self.enterRule(localctx, 104, self.RULE_index_operator)
        try:
            self.state = 541
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,42,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 532
                self.match(D96Parser.LSB)
                self.state = 533
                self.exp()
                self.state = 534
                self.match(D96Parser.RSB)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 536
                self.match(D96Parser.LSB)
                self.state = 537
                self.exp()
                self.state = 538
                self.match(D96Parser.RSB)
                self.state = 539
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

        def function_call(self):
            return self.getTypedRuleContext(D96Parser.Function_callContext,0)


        def exp8(self):
            return self.getTypedRuleContext(D96Parser.Exp8Context,0)


        def exp7(self):
            return self.getTypedRuleContext(D96Parser.Exp7Context,0)


        def DOT(self):
            return self.getToken(D96Parser.DOT, 0)

        def NORMAL_ID(self):
            return self.getToken(D96Parser.NORMAL_ID, 0)

        def LP(self):
            return self.getToken(D96Parser.LP, 0)

        def list_exp(self):
            return self.getTypedRuleContext(D96Parser.List_expContext,0)


        def RP(self):
            return self.getToken(D96Parser.RP, 0)

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
        _startState = 106
        self.enterRecursionRule(localctx, 106, self.RULE_exp7, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 546
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,43,self._ctx)
            if la_ == 1:
                self.state = 544
                self.function_call()
                pass

            elif la_ == 2:
                self.state = 545
                self.exp8()
                pass


            self._ctx.stop = self._input.LT(-1)
            self.state = 560
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,45,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 558
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,44,self._ctx)
                    if la_ == 1:
                        localctx = D96Parser.Exp7Context(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_exp7)
                        self.state = 548
                        if not self.precpred(self._ctx, 4):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 4)")
                        self.state = 549
                        self.match(D96Parser.DOT)
                        self.state = 550
                        self.match(D96Parser.NORMAL_ID)
                        self.state = 551
                        self.match(D96Parser.LP)
                        self.state = 552
                        self.list_exp()
                        self.state = 553
                        self.match(D96Parser.RP)
                        pass

                    elif la_ == 2:
                        localctx = D96Parser.Exp7Context(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_exp7)
                        self.state = 555
                        if not self.precpred(self._ctx, 3):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 3)")
                        self.state = 556
                        self.match(D96Parser.DOT)
                        self.state = 557
                        self.match(D96Parser.NORMAL_ID)
                        pass

             
                self.state = 562
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,45,self._ctx)

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

        def NORMAL_ID(self):
            return self.getToken(D96Parser.NORMAL_ID, 0)

        def SCOPE(self):
            return self.getToken(D96Parser.SCOPE, 0)

        def DOLLAR_ID(self):
            return self.getToken(D96Parser.DOLLAR_ID, 0)

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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExp8" ):
                return visitor.visitExp8(self)
            else:
                return visitor.visitChildren(self)




    def exp8(self):

        localctx = D96Parser.Exp8Context(self, self._ctx, self.state)
        self.enterRule(localctx, 108, self.RULE_exp8)
        try:
            self.state = 574
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,46,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 563
                self.match(D96Parser.NORMAL_ID)
                self.state = 564
                self.match(D96Parser.SCOPE)
                self.state = 565
                self.match(D96Parser.DOLLAR_ID)
                self.state = 566
                self.match(D96Parser.LP)
                self.state = 567
                self.list_exp()
                self.state = 568
                self.match(D96Parser.RP)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 570
                self.match(D96Parser.NORMAL_ID)
                self.state = 571
                self.match(D96Parser.SCOPE)
                self.state = 572
                self.match(D96Parser.DOLLAR_ID)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 573
                self.exp9()
                pass


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

        def NEW(self):
            return self.getToken(D96Parser.NEW, 0)

        def exp9(self):
            return self.getTypedRuleContext(D96Parser.Exp9Context,0)


        def LP(self):
            return self.getToken(D96Parser.LP, 0)

        def list_exp(self):
            return self.getTypedRuleContext(D96Parser.List_expContext,0)


        def RP(self):
            return self.getToken(D96Parser.RP, 0)

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
        self.enterRule(localctx, 110, self.RULE_exp9)
        try:
            self.state = 583
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [D96Parser.NEW]:
                self.enterOuterAlt(localctx, 1)
                self.state = 576
                self.match(D96Parser.NEW)
                self.state = 577
                self.exp9()
                self.state = 578
                self.match(D96Parser.LP)
                self.state = 579
                self.list_exp()
                self.state = 580
                self.match(D96Parser.RP)
                pass
            elif token in [D96Parser.LP, D96Parser.ARRAY, D96Parser.SELF, D96Parser.BOOL_LITERAL, D96Parser.ARRAY_SIZE, D96Parser.INTEGER_LITERAL, D96Parser.STRING_LITERAL, D96Parser.REAL_LITERAL, D96Parser.NORMAL_ID, D96Parser.DOLLAR_ID]:
                self.enterOuterAlt(localctx, 2)
                self.state = 582
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

        def ARRAY_SIZE(self):
            return self.getToken(D96Parser.ARRAY_SIZE, 0)

        def INTEGER_LITERAL(self):
            return self.getToken(D96Parser.INTEGER_LITERAL, 0)

        def array_literal(self):
            return self.getTypedRuleContext(D96Parser.Array_literalContext,0)


        def BOOL_LITERAL(self):
            return self.getToken(D96Parser.BOOL_LITERAL, 0)

        def REAL_LITERAL(self):
            return self.getToken(D96Parser.REAL_LITERAL, 0)

        def STRING_LITERAL(self):
            return self.getToken(D96Parser.STRING_LITERAL, 0)

        def NORMAL_ID(self):
            return self.getToken(D96Parser.NORMAL_ID, 0)

        def DOLLAR_ID(self):
            return self.getToken(D96Parser.DOLLAR_ID, 0)

        def SELF(self):
            return self.getToken(D96Parser.SELF, 0)

        def exp11(self):
            return self.getTypedRuleContext(D96Parser.Exp11Context,0)


        def getRuleIndex(self):
            return D96Parser.RULE_exp10

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExp10" ):
                return visitor.visitExp10(self)
            else:
                return visitor.visitChildren(self)




    def exp10(self):

        localctx = D96Parser.Exp10Context(self, self._ctx, self.state)
        self.enterRule(localctx, 112, self.RULE_exp10)
        try:
            self.state = 595
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [D96Parser.ARRAY_SIZE]:
                self.enterOuterAlt(localctx, 1)
                self.state = 585
                self.match(D96Parser.ARRAY_SIZE)
                pass
            elif token in [D96Parser.INTEGER_LITERAL]:
                self.enterOuterAlt(localctx, 2)
                self.state = 586
                self.match(D96Parser.INTEGER_LITERAL)
                pass
            elif token in [D96Parser.ARRAY]:
                self.enterOuterAlt(localctx, 3)
                self.state = 587
                self.array_literal()
                pass
            elif token in [D96Parser.BOOL_LITERAL]:
                self.enterOuterAlt(localctx, 4)
                self.state = 588
                self.match(D96Parser.BOOL_LITERAL)
                pass
            elif token in [D96Parser.REAL_LITERAL]:
                self.enterOuterAlt(localctx, 5)
                self.state = 589
                self.match(D96Parser.REAL_LITERAL)
                pass
            elif token in [D96Parser.STRING_LITERAL]:
                self.enterOuterAlt(localctx, 6)
                self.state = 590
                self.match(D96Parser.STRING_LITERAL)
                pass
            elif token in [D96Parser.NORMAL_ID]:
                self.enterOuterAlt(localctx, 7)
                self.state = 591
                self.match(D96Parser.NORMAL_ID)
                pass
            elif token in [D96Parser.DOLLAR_ID]:
                self.enterOuterAlt(localctx, 8)
                self.state = 592
                self.match(D96Parser.DOLLAR_ID)
                pass
            elif token in [D96Parser.SELF]:
                self.enterOuterAlt(localctx, 9)
                self.state = 593
                self.match(D96Parser.SELF)
                pass
            elif token in [D96Parser.LP]:
                self.enterOuterAlt(localctx, 10)
                self.state = 594
                self.exp11()
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


    class Exp11Context(ParserRuleContext):
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
            return D96Parser.RULE_exp11

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExp11" ):
                return visitor.visitExp11(self)
            else:
                return visitor.visitChildren(self)




    def exp11(self):

        localctx = D96Parser.Exp11Context(self, self._ctx, self.state)
        self.enterRule(localctx, 114, self.RULE_exp11)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 597
            self.match(D96Parser.LP)
            self.state = 598
            self.exp()
            self.state = 599
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

        def exps(self):
            return self.getTypedRuleContext(D96Parser.ExpsContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_list_exp

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitList_exp" ):
                return visitor.visitList_exp(self)
            else:
                return visitor.visitChildren(self)




    def list_exp(self):

        localctx = D96Parser.List_expContext(self, self._ctx, self.state)
        self.enterRule(localctx, 116, self.RULE_list_exp)
        try:
            self.state = 603
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [D96Parser.LP, D96Parser.ARRAY, D96Parser.NEW, D96Parser.SELF, D96Parser.SUB, D96Parser.NOT, D96Parser.BOOL_LITERAL, D96Parser.ARRAY_SIZE, D96Parser.INTEGER_LITERAL, D96Parser.STRING_LITERAL, D96Parser.REAL_LITERAL, D96Parser.NORMAL_ID, D96Parser.DOLLAR_ID]:
                self.enterOuterAlt(localctx, 1)
                self.state = 601
                self.exps()
                pass
            elif token in [D96Parser.RP]:
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


    class ExpsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def exp(self):
            return self.getTypedRuleContext(D96Parser.ExpContext,0)


        def COMMA(self):
            return self.getToken(D96Parser.COMMA, 0)

        def exps(self):
            return self.getTypedRuleContext(D96Parser.ExpsContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_exps

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExps" ):
                return visitor.visitExps(self)
            else:
                return visitor.visitChildren(self)




    def exps(self):

        localctx = D96Parser.ExpsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 118, self.RULE_exps)
        try:
            self.state = 610
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,50,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 605
                self.exp()
                self.state = 606
                self.match(D96Parser.COMMA)
                self.state = 607
                self.exps()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 609
                self.exp()
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
        self.enterRule(localctx, 120, self.RULE_normal_id_list)
        try:
            self.state = 616
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,51,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 612
                self.match(D96Parser.NORMAL_ID)
                self.state = 613
                self.match(D96Parser.COMMA)
                self.state = 614
                self.normal_id_list()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 615
                self.match(D96Parser.NORMAL_ID)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Id_listContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def COMMA(self):
            return self.getToken(D96Parser.COMMA, 0)

        def id_list(self):
            return self.getTypedRuleContext(D96Parser.Id_listContext,0)


        def NORMAL_ID(self):
            return self.getToken(D96Parser.NORMAL_ID, 0)

        def DOLLAR_ID(self):
            return self.getToken(D96Parser.DOLLAR_ID, 0)

        def getRuleIndex(self):
            return D96Parser.RULE_id_list

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitId_list" ):
                return visitor.visitId_list(self)
            else:
                return visitor.visitChildren(self)




    def id_list(self):

        localctx = D96Parser.Id_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 122, self.RULE_id_list)
        self._la = 0 # Token type
        try:
            self.state = 622
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,52,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 618
                _la = self._input.LA(1)
                if not(_la==D96Parser.NORMAL_ID or _la==D96Parser.DOLLAR_ID):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 619
                self.match(D96Parser.COMMA)
                self.state = 620
                self.id_list()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 621
                _la = self._input.LA(1)
                if not(_la==D96Parser.NORMAL_ID or _la==D96Parser.DOLLAR_ID):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
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
        self._predicates[46] = self.exp1_sempred
        self._predicates[47] = self.exp2_sempred
        self._predicates[48] = self.exp3_sempred
        self._predicates[51] = self.exp6_sempred
        self._predicates[53] = self.exp7_sempred
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
         

    def exp6_sempred(self, localctx:Exp6Context, predIndex:int):
            if predIndex == 7:
                return self.precpred(self._ctx, 2)
         

    def exp7_sempred(self, localctx:Exp7Context, predIndex:int):
            if predIndex == 8:
                return self.precpred(self._ctx, 4)
         

            if predIndex == 9:
                return self.precpred(self._ctx, 3)
         




