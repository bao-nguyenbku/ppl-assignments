# Generated from e:\HCMUT\PRINCIPLES_OF_PROGRAMMING_LANGUAGE\ppl-assignments\assignment3\src\main\d96\parser\D96.g4 by ANTLR 4.8
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
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3A")
        buf.write("\u026f\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
        buf.write("\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r\4\16")
        buf.write("\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23\t\23")
        buf.write("\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30\4\31")
        buf.write("\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36\t\36")
        buf.write("\4\37\t\37\4 \t \4!\t!\4\"\t\"\4#\t#\4$\t$\4%\t%\4&\t")
        buf.write("&\4\'\t\'\4(\t(\4)\t)\4*\t*\4+\t+\4,\t,\4-\t-\4.\t.\4")
        buf.write("/\t/\4\60\t\60\4\61\t\61\4\62\t\62\4\63\t\63\4\64\t\64")
        buf.write("\4\65\t\65\4\66\t\66\4\67\t\67\48\t8\49\t9\4:\t:\4;\t")
        buf.write(";\4<\t<\4=\t=\4>\t>\3\2\3\2\3\2\3\3\3\3\3\3\3\3\5\3\u0084")
        buf.write("\n\3\3\4\3\4\3\4\3\4\3\4\3\5\3\5\3\5\5\5\u008e\n\5\3\6")
        buf.write("\3\6\3\6\3\6\3\7\3\7\5\7\u0096\n\7\3\b\3\b\3\b\3\b\5\b")
        buf.write("\u009c\n\b\3\t\3\t\3\t\3\t\5\t\u00a2\n\t\3\n\3\n\3\n\3")
        buf.write("\n\3\n\3\n\3\13\3\13\3\13\3\13\3\13\3\f\3\f\3\f\3\f\3")
        buf.write("\f\3\f\3\r\3\r\5\r\u00b7\n\r\3\16\3\16\3\16\3\16\3\16")
        buf.write("\5\16\u00be\n\16\3\17\3\17\3\17\3\17\3\17\3\17\3\17\3")
        buf.write("\17\5\17\u00c8\n\17\3\20\3\20\3\20\3\20\3\21\3\21\5\21")
        buf.write("\u00d0\n\21\3\22\3\22\3\22\3\22\5\22\u00d6\n\22\3\23\3")
        buf.write("\23\3\23\3\23\3\23\3\23\3\23\3\23\3\23\3\23\3\23\3\23")
        buf.write("\3\23\5\23\u00e5\n\23\3\24\3\24\3\24\3\25\3\25\3\25\3")
        buf.write("\26\3\26\3\26\3\26\3\27\3\27\5\27\u00f3\n\27\3\30\3\30")
        buf.write("\3\30\3\30\3\30\3\31\3\31\3\31\3\31\3\31\3\31\3\31\3\31")
        buf.write("\3\32\3\32\5\32\u0104\n\32\3\33\3\33\3\33\3\33\5\33\u010a")
        buf.write("\n\33\3\34\3\34\3\34\3\34\3\34\3\34\3\35\3\35\3\35\5\35")
        buf.write("\u0115\n\35\3\36\3\36\3\36\3\36\3\36\5\36\u011c\n\36\3")
        buf.write("\36\3\36\3\36\3\36\3\36\3\36\3\36\3\36\3\37\3\37\3\37")
        buf.write("\5\37\u0129\n\37\3 \3 \3 \3 \3 \3 \5 \u0131\n \3!\3!\3")
        buf.write("!\3!\3\"\3\"\3\"\3\"\3\"\3\"\3\"\3#\3#\3#\3#\3$\3$\3$")
        buf.write("\3$\3$\3$\3$\3%\3%\3%\3%\3&\3&\3&\3&\3&\3&\5&\u0153\n")
        buf.write("&\3&\3&\3&\3&\3&\3&\3&\5&\u015c\n&\5&\u015e\n&\3\'\3\'")
        buf.write("\3\'\3\'\3\'\3\'\3\'\3\'\3\'\3\'\3\'\3\'\3\'\5\'\u016d")
        buf.write("\n\'\3\'\5\'\u0170\n\'\3(\3(\3(\3(\3)\3)\3)\3)\3)\3)\3")
        buf.write(")\3)\3)\3)\3)\3)\5)\u0182\n)\5)\u0184\n)\3*\3*\3*\3*\3")
        buf.write("*\3*\3*\3*\3*\3*\3*\3*\3*\5*\u0193\n*\3*\5*\u0196\n*\3")
        buf.write("+\3+\3+\3+\3+\3+\3+\5+\u019f\n+\3+\3+\3+\3+\3,\3,\3,\3")
        buf.write(",\3,\3-\3-\3-\3-\3-\3-\3-\3-\3-\5-\u01b3\n-\3.\3.\3.\3")
        buf.write(".\3.\3.\3.\3.\3.\3.\3.\3.\3.\3.\3.\3.\3.\3.\3.\3.\3.\3")
        buf.write(".\3.\3.\3.\5.\u01ce\n.\3/\3/\3/\3/\3/\3/\3/\3/\3/\7/\u01d9")
        buf.write("\n/\f/\16/\u01dc\13/\3\60\3\60\3\60\3\60\3\60\3\60\3\60")
        buf.write("\3\60\3\60\7\60\u01e7\n\60\f\60\16\60\u01ea\13\60\3\61")
        buf.write("\3\61\3\61\3\61\3\61\3\61\3\61\3\61\3\61\3\61\3\61\3\61")
        buf.write("\7\61\u01f8\n\61\f\61\16\61\u01fb\13\61\3\62\3\62\3\62")
        buf.write("\5\62\u0200\n\62\3\63\3\63\3\63\5\63\u0205\n\63\3\64\3")
        buf.write("\64\3\64\3\64\3\64\7\64\u020c\n\64\f\64\16\64\u020f\13")
        buf.write("\64\3\65\3\65\3\65\3\65\3\65\3\65\3\65\3\65\3\65\3\65")
        buf.write("\7\65\u021b\n\65\f\65\16\65\u021e\13\65\3\66\3\66\3\66")
        buf.write("\3\66\3\66\3\66\3\66\3\66\3\66\3\66\3\66\3\66\3\66\7\66")
        buf.write("\u022d\n\66\f\66\16\66\u0230\13\66\3\67\3\67\3\67\3\67")
        buf.write("\3\67\3\67\3\67\3\67\3\67\3\67\3\67\5\67\u023d\n\67\3")
        buf.write("8\38\38\38\38\38\38\58\u0246\n8\39\39\39\39\39\39\39\3")
        buf.write("9\39\39\59\u0252\n9\3:\3:\3:\3:\3;\3;\5;\u025a\n;\3<\3")
        buf.write("<\3<\3<\3<\5<\u0261\n<\3=\3=\3=\3=\5=\u0267\n=\3>\3>\3")
        buf.write(">\3>\5>\u026d\n>\3>\2\b\\^`fhj?\2\4\6\b\n\f\16\20\22\24")
        buf.write("\26\30\32\34\36 \"$&(*,.\60\62\64\668:<>@BDFHJLNPRTVX")
        buf.write("Z\\^`bdfhjlnprtvxz\2\4\3\2=>\3\2\3\4\2\u0295\2|\3\2\2")
        buf.write("\2\4\u0083\3\2\2\2\6\u0085\3\2\2\2\b\u008d\3\2\2\2\n\u008f")
        buf.write("\3\2\2\2\f\u0095\3\2\2\2\16\u009b\3\2\2\2\20\u00a1\3\2")
        buf.write("\2\2\22\u00a3\3\2\2\2\24\u00a9\3\2\2\2\26\u00ae\3\2\2")
        buf.write("\2\30\u00b6\3\2\2\2\32\u00bd\3\2\2\2\34\u00bf\3\2\2\2")
        buf.write("\36\u00c9\3\2\2\2 \u00cf\3\2\2\2\"\u00d5\3\2\2\2$\u00e4")
        buf.write("\3\2\2\2&\u00e6\3\2\2\2(\u00e9\3\2\2\2*\u00ec\3\2\2\2")
        buf.write(",\u00f2\3\2\2\2.\u00f4\3\2\2\2\60\u00f9\3\2\2\2\62\u0103")
        buf.write("\3\2\2\2\64\u0109\3\2\2\2\66\u010b\3\2\2\28\u0114\3\2")
        buf.write("\2\2:\u0116\3\2\2\2<\u0128\3\2\2\2>\u0130\3\2\2\2@\u0132")
        buf.write("\3\2\2\2B\u0136\3\2\2\2D\u013d\3\2\2\2F\u0141\3\2\2\2")
        buf.write("H\u0148\3\2\2\2J\u015d\3\2\2\2L\u016f\3\2\2\2N\u0171\3")
        buf.write("\2\2\2P\u0183\3\2\2\2R\u0195\3\2\2\2T\u0197\3\2\2\2V\u01a4")
        buf.write("\3\2\2\2X\u01b2\3\2\2\2Z\u01cd\3\2\2\2\\\u01cf\3\2\2\2")
        buf.write("^\u01dd\3\2\2\2`\u01eb\3\2\2\2b\u01ff\3\2\2\2d\u0204\3")
        buf.write("\2\2\2f\u0206\3\2\2\2h\u0210\3\2\2\2j\u021f\3\2\2\2l\u023c")
        buf.write("\3\2\2\2n\u0245\3\2\2\2p\u0251\3\2\2\2r\u0253\3\2\2\2")
        buf.write("t\u0259\3\2\2\2v\u0260\3\2\2\2x\u0266\3\2\2\2z\u026c\3")
        buf.write("\2\2\2|}\5\4\3\2}~\7\2\2\3~\3\3\2\2\2\177\u0084\5\6\4")
        buf.write("\2\u0080\u0081\5\6\4\2\u0081\u0082\5\4\3\2\u0082\u0084")
        buf.write("\3\2\2\2\u0083\177\3\2\2\2\u0083\u0080\3\2\2\2\u0084\5")
        buf.write("\3\2\2\2\u0085\u0086\7\62\2\2\u0086\u0087\7=\2\2\u0087")
        buf.write("\u0088\5\b\5\2\u0088\u0089\5\n\6\2\u0089\7\3\2\2\2\u008a")
        buf.write("\u008b\7\r\2\2\u008b\u008e\7=\2\2\u008c\u008e\3\2\2\2")
        buf.write("\u008d\u008a\3\2\2\2\u008d\u008c\3\2\2\2\u008e\t\3\2\2")
        buf.write("\2\u008f\u0090\7\7\2\2\u0090\u0091\5\f\7\2\u0091\u0092")
        buf.write("\7\b\2\2\u0092\13\3\2\2\2\u0093\u0096\5\16\b\2\u0094\u0096")
        buf.write("\3\2\2\2\u0095\u0093\3\2\2\2\u0095\u0094\3\2\2\2\u0096")
        buf.write("\r\3\2\2\2\u0097\u0098\5\20\t\2\u0098\u0099\5\16\b\2\u0099")
        buf.write("\u009c\3\2\2\2\u009a\u009c\5\20\t\2\u009b\u0097\3\2\2")
        buf.write("\2\u009b\u009a\3\2\2\2\u009c\17\3\2\2\2\u009d\u00a2\5")
        buf.write("H%\2\u009e\u00a2\5\22\n\2\u009f\u00a2\5\24\13\2\u00a0")
        buf.write("\u00a2\5\26\f\2\u00a1\u009d\3\2\2\2\u00a1\u009e\3\2\2")
        buf.write("\2\u00a1\u009f\3\2\2\2\u00a1\u00a0\3\2\2\2\u00a2\21\3")
        buf.write("\2\2\2\u00a3\u00a4\7\31\2\2\u00a4\u00a5\7\5\2\2\u00a5")
        buf.write("\u00a6\5\30\r\2\u00a6\u00a7\7\6\2\2\u00a7\u00a8\5\36\20")
        buf.write("\2\u00a8\23\3\2\2\2\u00a9\u00aa\7\32\2\2\u00aa\u00ab\7")
        buf.write("\5\2\2\u00ab\u00ac\7\6\2\2\u00ac\u00ad\5\36\20\2\u00ad")
        buf.write("\25\3\2\2\2\u00ae\u00af\t\2\2\2\u00af\u00b0\7\5\2\2\u00b0")
        buf.write("\u00b1\5\30\r\2\u00b1\u00b2\7\6\2\2\u00b2\u00b3\5\36\20")
        buf.write("\2\u00b3\27\3\2\2\2\u00b4\u00b7\5\32\16\2\u00b5\u00b7")
        buf.write("\3\2\2\2\u00b6\u00b4\3\2\2\2\u00b6\u00b5\3\2\2\2\u00b7")
        buf.write("\31\3\2\2\2\u00b8\u00b9\5\34\17\2\u00b9\u00ba\7\13\2\2")
        buf.write("\u00ba\u00bb\5\32\16\2\u00bb\u00be\3\2\2\2\u00bc\u00be")
        buf.write("\5\34\17\2\u00bd\u00b8\3\2\2\2\u00bd\u00bc\3\2\2\2\u00be")
        buf.write("\33\3\2\2\2\u00bf\u00c0\5x=\2\u00c0\u00c7\7\r\2\2\u00c1")
        buf.write("\u00c8\7\26\2\2\u00c2\u00c8\7\65\2\2\u00c3\u00c8\7\63")
        buf.write("\2\2\u00c4\u00c8\5T+\2\u00c5\u00c8\7\64\2\2\u00c6\u00c8")
        buf.write("\7=\2\2\u00c7\u00c1\3\2\2\2\u00c7\u00c2\3\2\2\2\u00c7")
        buf.write("\u00c3\3\2\2\2\u00c7\u00c4\3\2\2\2\u00c7\u00c5\3\2\2\2")
        buf.write("\u00c7\u00c6\3\2\2\2\u00c8\35\3\2\2\2\u00c9\u00ca\7\7")
        buf.write("\2\2\u00ca\u00cb\5 \21\2\u00cb\u00cc\7\b\2\2\u00cc\37")
        buf.write("\3\2\2\2\u00cd\u00d0\5\"\22\2\u00ce\u00d0\3\2\2\2\u00cf")
        buf.write("\u00cd\3\2\2\2\u00cf\u00ce\3\2\2\2\u00d0!\3\2\2\2\u00d1")
        buf.write("\u00d2\5$\23\2\u00d2\u00d3\5\"\22\2\u00d3\u00d6\3\2\2")
        buf.write("\2\u00d4\u00d6\5$\23\2\u00d5\u00d1\3\2\2\2\u00d5\u00d4")
        buf.write("\3\2\2\2\u00d6#\3\2\2\2\u00d7\u00e5\5.\30\2\u00d8\u00e5")
        buf.write("\5N(\2\u00d9\u00e5\5&\24\2\u00da\u00e5\5(\25\2\u00db\u00e5")
        buf.write("\5*\26\2\u00dc\u00dd\5B\"\2\u00dd\u00de\7\13\2\2\u00de")
        buf.write("\u00e5\3\2\2\2\u00df\u00e0\5F$\2\u00e0\u00e1\7\13\2\2")
        buf.write("\u00e1\u00e5\3\2\2\2\u00e2\u00e5\5\60\31\2\u00e3\u00e5")
        buf.write("\5:\36\2\u00e4\u00d7\3\2\2\2\u00e4\u00d8\3\2\2\2\u00e4")
        buf.write("\u00d9\3\2\2\2\u00e4\u00da\3\2\2\2\u00e4\u00db\3\2\2\2")
        buf.write("\u00e4\u00dc\3\2\2\2\u00e4\u00df\3\2\2\2\u00e4\u00e2\3")
        buf.write("\2\2\2\u00e4\u00e3\3\2\2\2\u00e5%\3\2\2\2\u00e6\u00e7")
        buf.write("\7\16\2\2\u00e7\u00e8\7\13\2\2\u00e8\'\3\2\2\2\u00e9\u00ea")
        buf.write("\7\17\2\2\u00ea\u00eb\7\13\2\2\u00eb)\3\2\2\2\u00ec\u00ed")
        buf.write("\7\27\2\2\u00ed\u00ee\5,\27\2\u00ee\u00ef\7\13\2\2\u00ef")
        buf.write("+\3\2\2\2\u00f0\u00f3\5X-\2\u00f1\u00f3\3\2\2\2\u00f2")
        buf.write("\u00f0\3\2\2\2\u00f2\u00f1\3\2\2\2\u00f3-\3\2\2\2\u00f4")
        buf.write("\u00f5\5> \2\u00f5\u00f6\7\'\2\2\u00f6\u00f7\5X-\2\u00f7")
        buf.write("\u00f8\7\13\2\2\u00f8/\3\2\2\2\u00f9\u00fa\7\20\2\2\u00fa")
        buf.write("\u00fb\7\5\2\2\u00fb\u00fc\5X-\2\u00fc\u00fd\7\6\2\2\u00fd")
        buf.write("\u00fe\5\36\20\2\u00fe\u00ff\5\62\32\2\u00ff\u0100\58")
        buf.write("\35\2\u0100\61\3\2\2\2\u0101\u0104\5\64\33\2\u0102\u0104")
        buf.write("\3\2\2\2\u0103\u0101\3\2\2\2\u0103\u0102\3\2\2\2\u0104")
        buf.write("\63\3\2\2\2\u0105\u010a\5\66\34\2\u0106\u0107\5\66\34")
        buf.write("\2\u0107\u0108\5\64\33\2\u0108\u010a\3\2\2\2\u0109\u0105")
        buf.write("\3\2\2\2\u0109\u0106\3\2\2\2\u010a\65\3\2\2\2\u010b\u010c")
        buf.write("\7\21\2\2\u010c\u010d\7\5\2\2\u010d\u010e\5X-\2\u010e")
        buf.write("\u010f\7\6\2\2\u010f\u0110\5\36\20\2\u0110\67\3\2\2\2")
        buf.write("\u0111\u0112\7\22\2\2\u0112\u0115\5\36\20\2\u0113\u0115")
        buf.write("\3\2\2\2\u0114\u0111\3\2\2\2\u0114\u0113\3\2\2\2\u0115")
        buf.write("9\3\2\2\2\u0116\u0117\7\23\2\2\u0117\u011b\7\5\2\2\u0118")
        buf.write("\u011c\7=\2\2\u0119\u011c\5@!\2\u011a\u011c\5D#\2\u011b")
        buf.write("\u0118\3\2\2\2\u011b\u0119\3\2\2\2\u011b\u011a\3\2\2\2")
        buf.write("\u011c\u011d\3\2\2\2\u011d\u011e\7\25\2\2\u011e\u011f")
        buf.write("\5X-\2\u011f\u0120\7\60\2\2\u0120\u0121\5X-\2\u0121\u0122")
        buf.write("\5<\37\2\u0122\u0123\7\6\2\2\u0123\u0124\5\36\20\2\u0124")
        buf.write(";\3\2\2\2\u0125\u0126\7\34\2\2\u0126\u0129\5X-\2\u0127")
        buf.write("\u0129\3\2\2\2\u0128\u0125\3\2\2\2\u0128\u0127\3\2\2\2")
        buf.write("\u0129=\3\2\2\2\u012a\u0131\7=\2\2\u012b\u012c\5f\64\2")
        buf.write("\u012c\u012d\5h\65\2\u012d\u0131\3\2\2\2\u012e\u0131\5")
        buf.write("@!\2\u012f\u0131\5D#\2\u0130\u012a\3\2\2\2\u0130\u012b")
        buf.write("\3\2\2\2\u0130\u012e\3\2\2\2\u0130\u012f\3\2\2\2\u0131")
        buf.write("?\3\2\2\2\u0132\u0133\7=\2\2\u0133\u0134\7\61\2\2\u0134")
        buf.write("\u0135\7>\2\2\u0135A\3\2\2\2\u0136\u0137\7=\2\2\u0137")
        buf.write("\u0138\7\61\2\2\u0138\u0139\7>\2\2\u0139\u013a\7\5\2\2")
        buf.write("\u013a\u013b\5t;\2\u013b\u013c\7\6\2\2\u013cC\3\2\2\2")
        buf.write("\u013d\u013e\5j\66\2\u013e\u013f\7/\2\2\u013f\u0140\7")
        buf.write("=\2\2\u0140E\3\2\2\2\u0141\u0142\5j\66\2\u0142\u0143\7")
        buf.write("/\2\2\u0143\u0144\7=\2\2\u0144\u0145\7\5\2\2\u0145\u0146")
        buf.write("\5t;\2\u0146\u0147\7\6\2\2\u0147G\3\2\2\2\u0148\u0149")
        buf.write("\t\3\2\2\u0149\u014a\5J&\2\u014a\u014b\7\13\2\2\u014b")
        buf.write("I\3\2\2\2\u014c\u014d\t\2\2\2\u014d\u014e\5L\'\2\u014e")
        buf.write("\u014f\5X-\2\u014f\u015e\3\2\2\2\u0150\u0153\5z>\2\u0151")
        buf.write("\u0153\5x=\2\u0152\u0150\3\2\2\2\u0152\u0151\3\2\2\2\u0153")
        buf.write("\u0154\3\2\2\2\u0154\u015b\7\r\2\2\u0155\u015c\7\26\2")
        buf.write("\2\u0156\u015c\7\65\2\2\u0157\u015c\7\63\2\2\u0158\u015c")
        buf.write("\5T+\2\u0159\u015c\7\64\2\2\u015a\u015c\7=\2\2\u015b\u0155")
        buf.write("\3\2\2\2\u015b\u0156\3\2\2\2\u015b\u0157\3\2\2\2\u015b")
        buf.write("\u0158\3\2\2\2\u015b\u0159\3\2\2\2\u015b\u015a\3\2\2\2")
        buf.write("\u015c\u015e\3\2\2\2\u015d\u014c\3\2\2\2\u015d\u0152\3")
        buf.write("\2\2\2\u015eK\3\2\2\2\u015f\u0160\7\f\2\2\u0160\u0161")
        buf.write("\t\2\2\2\u0161\u0162\5L\'\2\u0162\u0163\5X-\2\u0163\u0164")
        buf.write("\7\f\2\2\u0164\u0170\3\2\2\2\u0165\u016c\7\r\2\2\u0166")
        buf.write("\u016d\7\26\2\2\u0167\u016d\7\65\2\2\u0168\u016d\7\63")
        buf.write("\2\2\u0169\u016d\5T+\2\u016a\u016d\7\64\2\2\u016b\u016d")
        buf.write("\7=\2\2\u016c\u0166\3\2\2\2\u016c\u0167\3\2\2\2\u016c")
        buf.write("\u0168\3\2\2\2\u016c\u0169\3\2\2\2\u016c\u016a\3\2\2\2")
        buf.write("\u016c\u016b\3\2\2\2\u016d\u016e\3\2\2\2\u016e\u0170\7")
        buf.write("\'\2\2\u016f\u015f\3\2\2\2\u016f\u0165\3\2\2\2\u0170M")
        buf.write("\3\2\2\2\u0171\u0172\t\3\2\2\u0172\u0173\5P)\2\u0173\u0174")
        buf.write("\7\13\2\2\u0174O\3\2\2\2\u0175\u0176\7=\2\2\u0176\u0177")
        buf.write("\5R*\2\u0177\u0178\5X-\2\u0178\u0184\3\2\2\2\u0179\u017a")
        buf.write("\5x=\2\u017a\u0181\7\r\2\2\u017b\u0182\7\26\2\2\u017c")
        buf.write("\u0182\7\65\2\2\u017d\u0182\7\63\2\2\u017e\u0182\5T+\2")
        buf.write("\u017f\u0182\7\64\2\2\u0180\u0182\7=\2\2\u0181\u017b\3")
        buf.write("\2\2\2\u0181\u017c\3\2\2\2\u0181\u017d\3\2\2\2\u0181\u017e")
        buf.write("\3\2\2\2\u0181\u017f\3\2\2\2\u0181\u0180\3\2\2\2\u0182")
        buf.write("\u0184\3\2\2\2\u0183\u0175\3\2\2\2\u0183\u0179\3\2\2\2")
        buf.write("\u0184Q\3\2\2\2\u0185\u0186\7\f\2\2\u0186\u0187\7=\2\2")
        buf.write("\u0187\u0188\5R*\2\u0188\u0189\5X-\2\u0189\u018a\7\f\2")
        buf.write("\2\u018a\u0196\3\2\2\2\u018b\u0192\7\r\2\2\u018c\u0193")
        buf.write("\7\26\2\2\u018d\u0193\7\65\2\2\u018e\u0193\7\63\2\2\u018f")
        buf.write("\u0193\5T+\2\u0190\u0193\7\64\2\2\u0191\u0193\7=\2\2\u0192")
        buf.write("\u018c\3\2\2\2\u0192\u018d\3\2\2\2\u0192\u018e\3\2\2\2")
        buf.write("\u0192\u018f\3\2\2\2\u0192\u0190\3\2\2\2\u0192\u0191\3")
        buf.write("\2\2\2\u0193\u0194\3\2\2\2\u0194\u0196\7\'\2\2\u0195\u0185")
        buf.write("\3\2\2\2\u0195\u018b\3\2\2\2\u0196S\3\2\2\2\u0197\u0198")
        buf.write("\7\24\2\2\u0198\u019e\7\t\2\2\u0199\u019f\7\26\2\2\u019a")
        buf.write("\u019f\7\65\2\2\u019b\u019f\7\63\2\2\u019c\u019f\5T+\2")
        buf.write("\u019d\u019f\7\64\2\2\u019e\u0199\3\2\2\2\u019e\u019a")
        buf.write("\3\2\2\2\u019e\u019b\3\2\2\2\u019e\u019c\3\2\2\2\u019e")
        buf.write("\u019d\3\2\2\2\u019f\u01a0\3\2\2\2\u01a0\u01a1\7\f\2\2")
        buf.write("\u01a1\u01a2\7\67\2\2\u01a2\u01a3\7\n\2\2\u01a3U\3\2\2")
        buf.write("\2\u01a4\u01a5\7\24\2\2\u01a5\u01a6\7\5\2\2\u01a6\u01a7")
        buf.write("\5t;\2\u01a7\u01a8\7\6\2\2\u01a8W\3\2\2\2\u01a9\u01aa")
        buf.write("\5Z.\2\u01aa\u01ab\7-\2\2\u01ab\u01ac\5Z.\2\u01ac\u01b3")
        buf.write("\3\2\2\2\u01ad\u01ae\5Z.\2\u01ae\u01af\7.\2\2\u01af\u01b0")
        buf.write("\5Z.\2\u01b0\u01b3\3\2\2\2\u01b1\u01b3\5Z.\2\u01b2\u01a9")
        buf.write("\3\2\2\2\u01b2\u01ad\3\2\2\2\u01b2\u01b1\3\2\2\2\u01b3")
        buf.write("Y\3\2\2\2\u01b4\u01b5\5\\/\2\u01b5\u01b6\7+\2\2\u01b6")
        buf.write("\u01b7\5\\/\2\u01b7\u01ce\3\2\2\2\u01b8\u01b9\5\\/\2\u01b9")
        buf.write("\u01ba\7,\2\2\u01ba\u01bb\5\\/\2\u01bb\u01ce\3\2\2\2\u01bc")
        buf.write("\u01bd\5\\/\2\u01bd\u01be\7)\2\2\u01be\u01bf\5\\/\2\u01bf")
        buf.write("\u01ce\3\2\2\2\u01c0\u01c1\5\\/\2\u01c1\u01c2\7&\2\2\u01c2")
        buf.write("\u01c3\5\\/\2\u01c3\u01ce\3\2\2\2\u01c4\u01c5\5\\/\2\u01c5")
        buf.write("\u01c6\7(\2\2\u01c6\u01c7\5\\/\2\u01c7\u01ce\3\2\2\2\u01c8")
        buf.write("\u01c9\5\\/\2\u01c9\u01ca\7*\2\2\u01ca\u01cb\5\\/\2\u01cb")
        buf.write("\u01ce\3\2\2\2\u01cc\u01ce\5\\/\2\u01cd\u01b4\3\2\2\2")
        buf.write("\u01cd\u01b8\3\2\2\2\u01cd\u01bc\3\2\2\2\u01cd\u01c0\3")
        buf.write("\2\2\2\u01cd\u01c4\3\2\2\2\u01cd\u01c8\3\2\2\2\u01cd\u01cc")
        buf.write("\3\2\2\2\u01ce[\3\2\2\2\u01cf\u01d0\b/\1\2\u01d0\u01d1")
        buf.write("\5^\60\2\u01d1\u01da\3\2\2\2\u01d2\u01d3\f\5\2\2\u01d3")
        buf.write("\u01d4\7$\2\2\u01d4\u01d9\5^\60\2\u01d5\u01d6\f\4\2\2")
        buf.write("\u01d6\u01d7\7%\2\2\u01d7\u01d9\5^\60\2\u01d8\u01d2\3")
        buf.write("\2\2\2\u01d8\u01d5\3\2\2\2\u01d9\u01dc\3\2\2\2\u01da\u01d8")
        buf.write("\3\2\2\2\u01da\u01db\3\2\2\2\u01db]\3\2\2\2\u01dc\u01da")
        buf.write("\3\2\2\2\u01dd\u01de\b\60\1\2\u01de\u01df\5`\61\2\u01df")
        buf.write("\u01e8\3\2\2\2\u01e0\u01e1\f\5\2\2\u01e1\u01e2\7\36\2")
        buf.write("\2\u01e2\u01e7\5`\61\2\u01e3\u01e4\f\4\2\2\u01e4\u01e5")
        buf.write("\7\37\2\2\u01e5\u01e7\5`\61\2\u01e6\u01e0\3\2\2\2\u01e6")
        buf.write("\u01e3\3\2\2\2\u01e7\u01ea\3\2\2\2\u01e8\u01e6\3\2\2\2")
        buf.write("\u01e8\u01e9\3\2\2\2\u01e9_\3\2\2\2\u01ea\u01e8\3\2\2")
        buf.write("\2\u01eb\u01ec\b\61\1\2\u01ec\u01ed\5b\62\2\u01ed\u01f9")
        buf.write("\3\2\2\2\u01ee\u01ef\f\6\2\2\u01ef\u01f0\7 \2\2\u01f0")
        buf.write("\u01f8\5b\62\2\u01f1\u01f2\f\5\2\2\u01f2\u01f3\7!\2\2")
        buf.write("\u01f3\u01f8\5b\62\2\u01f4\u01f5\f\4\2\2\u01f5\u01f6\7")
        buf.write("\"\2\2\u01f6\u01f8\5b\62\2\u01f7\u01ee\3\2\2\2\u01f7\u01f1")
        buf.write("\3\2\2\2\u01f7\u01f4\3\2\2\2\u01f8\u01fb\3\2\2\2\u01f9")
        buf.write("\u01f7\3\2\2\2\u01f9\u01fa\3\2\2\2\u01faa\3\2\2\2\u01fb")
        buf.write("\u01f9\3\2\2\2\u01fc\u01fd\7#\2\2\u01fd\u0200\5b\62\2")
        buf.write("\u01fe\u0200\5d\63\2\u01ff\u01fc\3\2\2\2\u01ff\u01fe\3")
        buf.write("\2\2\2\u0200c\3\2\2\2\u0201\u0202\7\37\2\2\u0202\u0205")
        buf.write("\5d\63\2\u0203\u0205\5f\64\2\u0204\u0201\3\2\2\2\u0204")
        buf.write("\u0203\3\2\2\2\u0205e\3\2\2\2\u0206\u0207\b\64\1\2\u0207")
        buf.write("\u0208\5j\66\2\u0208\u020d\3\2\2\2\u0209\u020a\f\4\2\2")
        buf.write("\u020a\u020c\5h\65\2\u020b\u0209\3\2\2\2\u020c\u020f\3")
        buf.write("\2\2\2\u020d\u020b\3\2\2\2\u020d\u020e\3\2\2\2\u020eg")
        buf.write("\3\2\2\2\u020f\u020d\3\2\2\2\u0210\u0211\b\65\1\2\u0211")
        buf.write("\u0212\7\t\2\2\u0212\u0213\5X-\2\u0213\u0214\7\n\2\2\u0214")
        buf.write("\u021c\3\2\2\2\u0215\u0216\f\4\2\2\u0216\u0217\7\t\2\2")
        buf.write("\u0217\u0218\5X-\2\u0218\u0219\7\n\2\2\u0219\u021b\3\2")
        buf.write("\2\2\u021a\u0215\3\2\2\2\u021b\u021e\3\2\2\2\u021c\u021a")
        buf.write("\3\2\2\2\u021c\u021d\3\2\2\2\u021di\3\2\2\2\u021e\u021c")
        buf.write("\3\2\2\2\u021f\u0220\b\66\1\2\u0220\u0221\5l\67\2\u0221")
        buf.write("\u022e\3\2\2\2\u0222\u0223\f\5\2\2\u0223\u0224\7/\2\2")
        buf.write("\u0224\u022d\7=\2\2\u0225\u0226\f\4\2\2\u0226\u0227\7")
        buf.write("/\2\2\u0227\u0228\7=\2\2\u0228\u0229\7\5\2\2\u0229\u022a")
        buf.write("\5t;\2\u022a\u022b\7\6\2\2\u022b\u022d\3\2\2\2\u022c\u0222")
        buf.write("\3\2\2\2\u022c\u0225\3\2\2\2\u022d\u0230\3\2\2\2\u022e")
        buf.write("\u022c\3\2\2\2\u022e\u022f\3\2\2\2\u022fk\3\2\2\2\u0230")
        buf.write("\u022e\3\2\2\2\u0231\u0232\7=\2\2\u0232\u0233\7\61\2\2")
        buf.write("\u0233\u0234\7>\2\2\u0234\u0235\7\5\2\2\u0235\u0236\5")
        buf.write("t;\2\u0236\u0237\7\6\2\2\u0237\u023d\3\2\2\2\u0238\u0239")
        buf.write("\7=\2\2\u0239\u023a\7\61\2\2\u023a\u023d\7>\2\2\u023b")
        buf.write("\u023d\5n8\2\u023c\u0231\3\2\2\2\u023c\u0238\3\2\2\2\u023c")
        buf.write("\u023b\3\2\2\2\u023dm\3\2\2\2\u023e\u023f\7\33\2\2\u023f")
        buf.write("\u0240\7=\2\2\u0240\u0241\7\5\2\2\u0241\u0242\5t;\2\u0242")
        buf.write("\u0243\7\6\2\2\u0243\u0246\3\2\2\2\u0244\u0246\5p9\2\u0245")
        buf.write("\u023e\3\2\2\2\u0245\u0244\3\2\2\2\u0246o\3\2\2\2\u0247")
        buf.write("\u0252\7\67\2\2\u0248\u0252\78\2\2\u0249\u0252\5V,\2\u024a")
        buf.write("\u0252\7\66\2\2\u024b\u0252\7<\2\2\u024c\u0252\79\2\2")
        buf.write("\u024d\u0252\7=\2\2\u024e\u0252\7\35\2\2\u024f\u0252\7")
        buf.write("\30\2\2\u0250\u0252\5r:\2\u0251\u0247\3\2\2\2\u0251\u0248")
        buf.write("\3\2\2\2\u0251\u0249\3\2\2\2\u0251\u024a\3\2\2\2\u0251")
        buf.write("\u024b\3\2\2\2\u0251\u024c\3\2\2\2\u0251\u024d\3\2\2\2")
        buf.write("\u0251\u024e\3\2\2\2\u0251\u024f\3\2\2\2\u0251\u0250\3")
        buf.write("\2\2\2\u0252q\3\2\2\2\u0253\u0254\7\5\2\2\u0254\u0255")
        buf.write("\5X-\2\u0255\u0256\7\6\2\2\u0256s\3\2\2\2\u0257\u025a")
        buf.write("\5v<\2\u0258\u025a\3\2\2\2\u0259\u0257\3\2\2\2\u0259\u0258")
        buf.write("\3\2\2\2\u025au\3\2\2\2\u025b\u025c\5X-\2\u025c\u025d")
        buf.write("\7\f\2\2\u025d\u025e\5v<\2\u025e\u0261\3\2\2\2\u025f\u0261")
        buf.write("\5X-\2\u0260\u025b\3\2\2\2\u0260\u025f\3\2\2\2\u0261w")
        buf.write("\3\2\2\2\u0262\u0263\7=\2\2\u0263\u0264\7\f\2\2\u0264")
        buf.write("\u0267\5x=\2\u0265\u0267\7=\2\2\u0266\u0262\3\2\2\2\u0266")
        buf.write("\u0265\3\2\2\2\u0267y\3\2\2\2\u0268\u0269\t\2\2\2\u0269")
        buf.write("\u026a\7\f\2\2\u026a\u026d\5z>\2\u026b\u026d\t\2\2\2\u026c")
        buf.write("\u0268\3\2\2\2\u026c\u026b\3\2\2\2\u026d{\3\2\2\2\63\u0083")
        buf.write("\u008d\u0095\u009b\u00a1\u00b6\u00bd\u00c7\u00cf\u00d5")
        buf.write("\u00e4\u00f2\u0103\u0109\u0114\u011b\u0128\u0130\u0152")
        buf.write("\u015b\u015d\u016c\u016f\u0181\u0183\u0192\u0195\u019e")
        buf.write("\u01b2\u01cd\u01d8\u01da\u01e6\u01e8\u01f7\u01f9\u01ff")
        buf.write("\u0204\u020d\u021c\u022c\u022e\u023c\u0245\u0251\u0259")
        buf.write("\u0260\u0266\u026c")
        return buf.getvalue()


class D96Parser ( Parser ):

    grammarFileName = "D96.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'Val'", "'Var'", "'('", "')'", "'{'", 
                     "'}'", "'['", "']'", "';'", "','", "':'", "'Break'", 
                     "'Continue'", "'If'", "'Elseif'", "'Else'", "'Foreach'", 
                     "'Array'", "'In'", "'Boolean'", "'Return'", "'Null'", 
                     "'Constructor'", "'Destructor'", "'New'", "'By'", "'Self'", 
                     "'+'", "'-'", "'*'", "'/'", "'%'", "'!'", "'&&'", "'||'", 
                     "'=='", "'='", "'!='", "'>'", "'>='", "'<'", "'<='", 
                     "'==.'", "'+.'", "'.'", "'..'", "'::'", "'Class'", 
                     "'Float'", "'String'", "'Int'" ]

    symbolicNames = [ "<INVALID>", "VAL", "VAR", "LP", "RP", "LCB", "RCB", 
                      "LSB", "RSB", "SEMI", "COMMA", "COLON", "BREAK", "CONTINUE", 
                      "IF", "ELSEIF", "ELSE", "FOREACH", "ARRAY", "IN", 
                      "BOOLEAN", "RETURN", "NULL", "CONSTRUCTOR", "DESTRUCTOR", 
                      "NEW", "BY", "SELF", "ADD", "SUB", "MUL", "DIV", "MOD", 
                      "NOT", "AND", "OR", "EQUAL", "ASSIGN", "NOTEQUAL", 
                      "GT", "GTE", "LT", "LTE", "EQUAL_STR", "ADD_STR", 
                      "DOT", "DOTDOT", "SCOPE", "CLASS", "FLOAT_TYPE", "STRING", 
                      "INT_TYPE", "BOOL_LITERAL", "ARRAY_SIZE", "INTEGER_LITERAL", 
                      "STRING_LITERAL", "ILLEGAL_ESCAPE", "UNCLOSE_STRING", 
                      "REAL_LITERAL", "NORMAL_ID", "DOLLAR_ID", "BLOCK_COMMENT", 
                      "WS", "ERROR_CHAR" ]

    RULE_program = 0
    RULE_class_declares_list = 1
    RULE_class_declare = 2
    RULE_extend = 3
    RULE_class_members = 4
    RULE_member_list = 5
    RULE_members = 6
    RULE_member = 7
    RULE_constructor_method = 8
    RULE_destructor_method = 9
    RULE_method_declare = 10
    RULE_param_list = 11
    RULE_parameters = 12
    RULE_parameter = 13
    RULE_block_statements = 14
    RULE_statements_list = 15
    RULE_statements = 16
    RULE_statement = 17
    RULE_break_statement = 18
    RULE_continue_statement = 19
    RULE_return_statement = 20
    RULE_exp_value = 21
    RULE_assign_statement = 22
    RULE_if_else_statement = 23
    RULE_elseif_stmt_list = 24
    RULE_elseif_stmts = 25
    RULE_elseif_stmt = 26
    RULE_else_stmt = 27
    RULE_foreach_statement = 28
    RULE_increment = 29
    RULE_lhs = 30
    RULE_static_attr_call = 31
    RULE_static_method_call = 32
    RULE_instance_attr_call = 33
    RULE_instance_method_call = 34
    RULE_attribute_declare = 35
    RULE_dec_and_init_list1 = 36
    RULE_pair1 = 37
    RULE_var_declare = 38
    RULE_dec_and_init_list2 = 39
    RULE_pair2 = 40
    RULE_array_type = 41
    RULE_array_literal = 42
    RULE_exp = 43
    RULE_exp0 = 44
    RULE_exp1 = 45
    RULE_exp2 = 46
    RULE_exp3 = 47
    RULE_exp4 = 48
    RULE_exp5 = 49
    RULE_exp6 = 50
    RULE_index_operators = 51
    RULE_exp7 = 52
    RULE_exp8 = 53
    RULE_exp9 = 54
    RULE_exp10 = 55
    RULE_exp11 = 56
    RULE_list_exp = 57
    RULE_exps = 58
    RULE_normal_id_list = 59
    RULE_id_list = 60

    ruleNames =  [ "program", "class_declares_list", "class_declare", "extend", 
                   "class_members", "member_list", "members", "member", 
                   "constructor_method", "destructor_method", "method_declare", 
                   "param_list", "parameters", "parameter", "block_statements", 
                   "statements_list", "statements", "statement", "break_statement", 
                   "continue_statement", "return_statement", "exp_value", 
                   "assign_statement", "if_else_statement", "elseif_stmt_list", 
                   "elseif_stmts", "elseif_stmt", "else_stmt", "foreach_statement", 
                   "increment", "lhs", "static_attr_call", "static_method_call", 
                   "instance_attr_call", "instance_method_call", "attribute_declare", 
                   "dec_and_init_list1", "pair1", "var_declare", "dec_and_init_list2", 
                   "pair2", "array_type", "array_literal", "exp", "exp0", 
                   "exp1", "exp2", "exp3", "exp4", "exp5", "exp6", "index_operators", 
                   "exp7", "exp8", "exp9", "exp10", "exp11", "list_exp", 
                   "exps", "normal_id_list", "id_list" ]

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
    ARRAY=18
    IN=19
    BOOLEAN=20
    RETURN=21
    NULL=22
    CONSTRUCTOR=23
    DESTRUCTOR=24
    NEW=25
    BY=26
    SELF=27
    ADD=28
    SUB=29
    MUL=30
    DIV=31
    MOD=32
    NOT=33
    AND=34
    OR=35
    EQUAL=36
    ASSIGN=37
    NOTEQUAL=38
    GT=39
    GTE=40
    LT=41
    LTE=42
    EQUAL_STR=43
    ADD_STR=44
    DOT=45
    DOTDOT=46
    SCOPE=47
    CLASS=48
    FLOAT_TYPE=49
    STRING=50
    INT_TYPE=51
    BOOL_LITERAL=52
    ARRAY_SIZE=53
    INTEGER_LITERAL=54
    STRING_LITERAL=55
    ILLEGAL_ESCAPE=56
    UNCLOSE_STRING=57
    REAL_LITERAL=58
    NORMAL_ID=59
    DOLLAR_ID=60
    BLOCK_COMMENT=61
    WS=62
    ERROR_CHAR=63

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.8")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ProgramContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def class_declares_list(self):
            return self.getTypedRuleContext(D96Parser.Class_declares_listContext,0)


        def EOF(self):
            return self.getToken(D96Parser.EOF, 0)

        def getRuleIndex(self):
            return D96Parser.RULE_program




    def program(self):

        localctx = D96Parser.ProgramContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_program)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 122
            self.class_declares_list()
            self.state = 123
            self.match(D96Parser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Class_declares_listContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def class_declare(self):
            return self.getTypedRuleContext(D96Parser.Class_declareContext,0)


        def class_declares_list(self):
            return self.getTypedRuleContext(D96Parser.Class_declares_listContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_class_declares_list




    def class_declares_list(self):

        localctx = D96Parser.Class_declares_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_class_declares_list)
        try:
            self.state = 129
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,0,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 125
                self.class_declare()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 126
                self.class_declare()
                self.state = 127
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




    def class_declare(self):

        localctx = D96Parser.Class_declareContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_class_declare)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 131
            self.match(D96Parser.CLASS)
            self.state = 132
            self.match(D96Parser.NORMAL_ID)
            self.state = 133
            self.extend()
            self.state = 134
            self.class_members()
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
        self.enterRule(localctx, 6, self.RULE_extend)
        try:
            self.state = 139
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [D96Parser.COLON]:
                self.enterOuterAlt(localctx, 1)
                self.state = 136
                self.match(D96Parser.COLON)
                self.state = 137
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




    def class_members(self):

        localctx = D96Parser.Class_membersContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_class_members)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 141
            self.match(D96Parser.LCB)
            self.state = 142
            self.member_list()
            self.state = 143
            self.match(D96Parser.RCB)
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

        def members(self):
            return self.getTypedRuleContext(D96Parser.MembersContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_member_list




    def member_list(self):

        localctx = D96Parser.Member_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_member_list)
        try:
            self.state = 147
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [D96Parser.VAL, D96Parser.VAR, D96Parser.CONSTRUCTOR, D96Parser.DESTRUCTOR, D96Parser.NORMAL_ID, D96Parser.DOLLAR_ID]:
                self.enterOuterAlt(localctx, 1)
                self.state = 145
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

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def member(self):
            return self.getTypedRuleContext(D96Parser.MemberContext,0)


        def members(self):
            return self.getTypedRuleContext(D96Parser.MembersContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_members




    def members(self):

        localctx = D96Parser.MembersContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_members)
        try:
            self.state = 153
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,3,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 149
                self.member()
                self.state = 150
                self.members()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 152
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

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def attribute_declare(self):
            return self.getTypedRuleContext(D96Parser.Attribute_declareContext,0)


        def constructor_method(self):
            return self.getTypedRuleContext(D96Parser.Constructor_methodContext,0)


        def destructor_method(self):
            return self.getTypedRuleContext(D96Parser.Destructor_methodContext,0)


        def method_declare(self):
            return self.getTypedRuleContext(D96Parser.Method_declareContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_member




    def member(self):

        localctx = D96Parser.MemberContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_member)
        try:
            self.state = 159
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [D96Parser.VAL, D96Parser.VAR]:
                self.enterOuterAlt(localctx, 1)
                self.state = 155
                self.attribute_declare()
                pass
            elif token in [D96Parser.CONSTRUCTOR]:
                self.enterOuterAlt(localctx, 2)
                self.state = 156
                self.constructor_method()
                pass
            elif token in [D96Parser.DESTRUCTOR]:
                self.enterOuterAlt(localctx, 3)
                self.state = 157
                self.destructor_method()
                pass
            elif token in [D96Parser.NORMAL_ID, D96Parser.DOLLAR_ID]:
                self.enterOuterAlt(localctx, 4)
                self.state = 158
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

        def block_statements(self):
            return self.getTypedRuleContext(D96Parser.Block_statementsContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_constructor_method




    def constructor_method(self):

        localctx = D96Parser.Constructor_methodContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_constructor_method)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 161
            self.match(D96Parser.CONSTRUCTOR)
            self.state = 162
            self.match(D96Parser.LP)
            self.state = 163
            self.param_list()
            self.state = 164
            self.match(D96Parser.RP)
            self.state = 165
            self.block_statements()
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

        def block_statements(self):
            return self.getTypedRuleContext(D96Parser.Block_statementsContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_destructor_method




    def destructor_method(self):

        localctx = D96Parser.Destructor_methodContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_destructor_method)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 167
            self.match(D96Parser.DESTRUCTOR)
            self.state = 168
            self.match(D96Parser.LP)
            self.state = 169
            self.match(D96Parser.RP)
            self.state = 170
            self.block_statements()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Method_declareContext(ParserRuleContext):

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




    def method_declare(self):

        localctx = D96Parser.Method_declareContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_method_declare)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 172
            _la = self._input.LA(1)
            if not(_la==D96Parser.NORMAL_ID or _la==D96Parser.DOLLAR_ID):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 173
            self.match(D96Parser.LP)
            self.state = 174
            self.param_list()
            self.state = 175
            self.match(D96Parser.RP)
            self.state = 176
            self.block_statements()
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

        def parameters(self):
            return self.getTypedRuleContext(D96Parser.ParametersContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_param_list




    def param_list(self):

        localctx = D96Parser.Param_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_param_list)
        try:
            self.state = 180
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [D96Parser.NORMAL_ID]:
                self.enterOuterAlt(localctx, 1)
                self.state = 178
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




    def parameters(self):

        localctx = D96Parser.ParametersContext(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_parameters)
        try:
            self.state = 187
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,6,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 182
                self.parameter()
                self.state = 183
                self.match(D96Parser.SEMI)
                self.state = 184
                self.parameters()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 186
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




    def parameter(self):

        localctx = D96Parser.ParameterContext(self, self._ctx, self.state)
        self.enterRule(localctx, 26, self.RULE_parameter)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 189
            self.normal_id_list()
            self.state = 190
            self.match(D96Parser.COLON)
            self.state = 197
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [D96Parser.BOOLEAN]:
                self.state = 191
                self.match(D96Parser.BOOLEAN)
                pass
            elif token in [D96Parser.INT_TYPE]:
                self.state = 192
                self.match(D96Parser.INT_TYPE)
                pass
            elif token in [D96Parser.FLOAT_TYPE]:
                self.state = 193
                self.match(D96Parser.FLOAT_TYPE)
                pass
            elif token in [D96Parser.ARRAY]:
                self.state = 194
                self.array_type()
                pass
            elif token in [D96Parser.STRING]:
                self.state = 195
                self.match(D96Parser.STRING)
                pass
            elif token in [D96Parser.NORMAL_ID]:
                self.state = 196
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




    def block_statements(self):

        localctx = D96Parser.Block_statementsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 28, self.RULE_block_statements)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 199
            self.match(D96Parser.LCB)
            self.state = 200
            self.statements_list()
            self.state = 201
            self.match(D96Parser.RCB)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Statements_listContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def statements(self):
            return self.getTypedRuleContext(D96Parser.StatementsContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_statements_list




    def statements_list(self):

        localctx = D96Parser.Statements_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 30, self.RULE_statements_list)
        try:
            self.state = 205
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [D96Parser.VAL, D96Parser.VAR, D96Parser.LP, D96Parser.BREAK, D96Parser.CONTINUE, D96Parser.IF, D96Parser.FOREACH, D96Parser.ARRAY, D96Parser.RETURN, D96Parser.NULL, D96Parser.NEW, D96Parser.SELF, D96Parser.BOOL_LITERAL, D96Parser.ARRAY_SIZE, D96Parser.INTEGER_LITERAL, D96Parser.STRING_LITERAL, D96Parser.REAL_LITERAL, D96Parser.NORMAL_ID]:
                self.enterOuterAlt(localctx, 1)
                self.state = 203
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

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def statement(self):
            return self.getTypedRuleContext(D96Parser.StatementContext,0)


        def statements(self):
            return self.getTypedRuleContext(D96Parser.StatementsContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_statements




    def statements(self):

        localctx = D96Parser.StatementsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 32, self.RULE_statements)
        try:
            self.state = 211
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,9,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 207
                self.statement()
                self.state = 208
                self.statements()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 210
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


        def static_method_call(self):
            return self.getTypedRuleContext(D96Parser.Static_method_callContext,0)


        def SEMI(self):
            return self.getToken(D96Parser.SEMI, 0)

        def instance_method_call(self):
            return self.getTypedRuleContext(D96Parser.Instance_method_callContext,0)


        def if_else_statement(self):
            return self.getTypedRuleContext(D96Parser.If_else_statementContext,0)


        def foreach_statement(self):
            return self.getTypedRuleContext(D96Parser.Foreach_statementContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_statement




    def statement(self):

        localctx = D96Parser.StatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 34, self.RULE_statement)
        try:
            self.state = 226
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,10,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 213
                self.assign_statement()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 214
                self.var_declare()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 215
                self.break_statement()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 216
                self.continue_statement()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 217
                self.return_statement()
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 218
                self.static_method_call()
                self.state = 219
                self.match(D96Parser.SEMI)
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 221
                self.instance_method_call()
                self.state = 222
                self.match(D96Parser.SEMI)
                pass

            elif la_ == 8:
                self.enterOuterAlt(localctx, 8)
                self.state = 224
                self.if_else_statement()
                pass

            elif la_ == 9:
                self.enterOuterAlt(localctx, 9)
                self.state = 225
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

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def BREAK(self):
            return self.getToken(D96Parser.BREAK, 0)

        def SEMI(self):
            return self.getToken(D96Parser.SEMI, 0)

        def getRuleIndex(self):
            return D96Parser.RULE_break_statement




    def break_statement(self):

        localctx = D96Parser.Break_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 36, self.RULE_break_statement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 228
            self.match(D96Parser.BREAK)
            self.state = 229
            self.match(D96Parser.SEMI)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Continue_statementContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def CONTINUE(self):
            return self.getToken(D96Parser.CONTINUE, 0)

        def SEMI(self):
            return self.getToken(D96Parser.SEMI, 0)

        def getRuleIndex(self):
            return D96Parser.RULE_continue_statement




    def continue_statement(self):

        localctx = D96Parser.Continue_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 38, self.RULE_continue_statement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 231
            self.match(D96Parser.CONTINUE)
            self.state = 232
            self.match(D96Parser.SEMI)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Return_statementContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def RETURN(self):
            return self.getToken(D96Parser.RETURN, 0)

        def exp_value(self):
            return self.getTypedRuleContext(D96Parser.Exp_valueContext,0)


        def SEMI(self):
            return self.getToken(D96Parser.SEMI, 0)

        def getRuleIndex(self):
            return D96Parser.RULE_return_statement




    def return_statement(self):

        localctx = D96Parser.Return_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 40, self.RULE_return_statement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 234
            self.match(D96Parser.RETURN)
            self.state = 235
            self.exp_value()
            self.state = 236
            self.match(D96Parser.SEMI)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Exp_valueContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def exp(self):
            return self.getTypedRuleContext(D96Parser.ExpContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_exp_value




    def exp_value(self):

        localctx = D96Parser.Exp_valueContext(self, self._ctx, self.state)
        self.enterRule(localctx, 42, self.RULE_exp_value)
        try:
            self.state = 240
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [D96Parser.LP, D96Parser.ARRAY, D96Parser.NULL, D96Parser.NEW, D96Parser.SELF, D96Parser.SUB, D96Parser.NOT, D96Parser.BOOL_LITERAL, D96Parser.ARRAY_SIZE, D96Parser.INTEGER_LITERAL, D96Parser.STRING_LITERAL, D96Parser.REAL_LITERAL, D96Parser.NORMAL_ID]:
                self.enterOuterAlt(localctx, 1)
                self.state = 238
                self.exp()
                pass
            elif token in [D96Parser.SEMI]:
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
        self.enterRule(localctx, 44, self.RULE_assign_statement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 242
            self.lhs()
            self.state = 243
            self.match(D96Parser.ASSIGN)
            self.state = 244
            self.exp()
            self.state = 245
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




    def if_else_statement(self):

        localctx = D96Parser.If_else_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 46, self.RULE_if_else_statement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 247
            self.match(D96Parser.IF)
            self.state = 248
            self.match(D96Parser.LP)
            self.state = 249
            self.exp()
            self.state = 250
            self.match(D96Parser.RP)
            self.state = 251
            self.block_statements()
            self.state = 252
            self.elseif_stmt_list()
            self.state = 253
            self.else_stmt()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Elseif_stmt_listContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def elseif_stmts(self):
            return self.getTypedRuleContext(D96Parser.Elseif_stmtsContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_elseif_stmt_list




    def elseif_stmt_list(self):

        localctx = D96Parser.Elseif_stmt_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 48, self.RULE_elseif_stmt_list)
        try:
            self.state = 257
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [D96Parser.ELSEIF]:
                self.enterOuterAlt(localctx, 1)
                self.state = 255
                self.elseif_stmts()
                pass
            elif token in [D96Parser.VAL, D96Parser.VAR, D96Parser.LP, D96Parser.RCB, D96Parser.BREAK, D96Parser.CONTINUE, D96Parser.IF, D96Parser.ELSE, D96Parser.FOREACH, D96Parser.ARRAY, D96Parser.RETURN, D96Parser.NULL, D96Parser.NEW, D96Parser.SELF, D96Parser.BOOL_LITERAL, D96Parser.ARRAY_SIZE, D96Parser.INTEGER_LITERAL, D96Parser.STRING_LITERAL, D96Parser.REAL_LITERAL, D96Parser.NORMAL_ID]:
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

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def elseif_stmt(self):
            return self.getTypedRuleContext(D96Parser.Elseif_stmtContext,0)


        def elseif_stmts(self):
            return self.getTypedRuleContext(D96Parser.Elseif_stmtsContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_elseif_stmts




    def elseif_stmts(self):

        localctx = D96Parser.Elseif_stmtsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 50, self.RULE_elseif_stmts)
        try:
            self.state = 263
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,13,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 259
                self.elseif_stmt()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 260
                self.elseif_stmt()
                self.state = 261
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




    def elseif_stmt(self):

        localctx = D96Parser.Elseif_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 52, self.RULE_elseif_stmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 265
            self.match(D96Parser.ELSEIF)
            self.state = 266
            self.match(D96Parser.LP)
            self.state = 267
            self.exp()
            self.state = 268
            self.match(D96Parser.RP)
            self.state = 269
            self.block_statements()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Else_stmtContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ELSE(self):
            return self.getToken(D96Parser.ELSE, 0)

        def block_statements(self):
            return self.getTypedRuleContext(D96Parser.Block_statementsContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_else_stmt




    def else_stmt(self):

        localctx = D96Parser.Else_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 54, self.RULE_else_stmt)
        try:
            self.state = 274
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [D96Parser.ELSE]:
                self.enterOuterAlt(localctx, 1)
                self.state = 271
                self.match(D96Parser.ELSE)
                self.state = 272
                self.block_statements()
                pass
            elif token in [D96Parser.VAL, D96Parser.VAR, D96Parser.LP, D96Parser.RCB, D96Parser.BREAK, D96Parser.CONTINUE, D96Parser.IF, D96Parser.FOREACH, D96Parser.ARRAY, D96Parser.RETURN, D96Parser.NULL, D96Parser.NEW, D96Parser.SELF, D96Parser.BOOL_LITERAL, D96Parser.ARRAY_SIZE, D96Parser.INTEGER_LITERAL, D96Parser.STRING_LITERAL, D96Parser.REAL_LITERAL, D96Parser.NORMAL_ID]:
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

        def static_attr_call(self):
            return self.getTypedRuleContext(D96Parser.Static_attr_callContext,0)


        def instance_attr_call(self):
            return self.getTypedRuleContext(D96Parser.Instance_attr_callContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_foreach_statement




    def foreach_statement(self):

        localctx = D96Parser.Foreach_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 56, self.RULE_foreach_statement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 276
            self.match(D96Parser.FOREACH)
            self.state = 277
            self.match(D96Parser.LP)
            self.state = 281
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,15,self._ctx)
            if la_ == 1:
                self.state = 278
                self.match(D96Parser.NORMAL_ID)
                pass

            elif la_ == 2:
                self.state = 279
                self.static_attr_call()
                pass

            elif la_ == 3:
                self.state = 280
                self.instance_attr_call()
                pass


            self.state = 283
            self.match(D96Parser.IN)
            self.state = 284
            self.exp()
            self.state = 285
            self.match(D96Parser.DOTDOT)
            self.state = 286
            self.exp()
            self.state = 287
            self.increment()
            self.state = 288
            self.match(D96Parser.RP)
            self.state = 289
            self.block_statements()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class IncrementContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def BY(self):
            return self.getToken(D96Parser.BY, 0)

        def exp(self):
            return self.getTypedRuleContext(D96Parser.ExpContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_increment




    def increment(self):

        localctx = D96Parser.IncrementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 58, self.RULE_increment)
        try:
            self.state = 294
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [D96Parser.BY]:
                self.enterOuterAlt(localctx, 1)
                self.state = 291
                self.match(D96Parser.BY)
                self.state = 292
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

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NORMAL_ID(self):
            return self.getToken(D96Parser.NORMAL_ID, 0)

        def exp6(self):
            return self.getTypedRuleContext(D96Parser.Exp6Context,0)


        def index_operators(self):
            return self.getTypedRuleContext(D96Parser.Index_operatorsContext,0)


        def static_attr_call(self):
            return self.getTypedRuleContext(D96Parser.Static_attr_callContext,0)


        def instance_attr_call(self):
            return self.getTypedRuleContext(D96Parser.Instance_attr_callContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_lhs




    def lhs(self):

        localctx = D96Parser.LhsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 60, self.RULE_lhs)
        try:
            self.state = 302
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,17,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 296
                self.match(D96Parser.NORMAL_ID)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 297
                self.exp6(0)
                self.state = 298
                self.index_operators(0)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 300
                self.static_attr_call()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 301
                self.instance_attr_call()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Static_attr_callContext(ParserRuleContext):

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




    def static_attr_call(self):

        localctx = D96Parser.Static_attr_callContext(self, self._ctx, self.state)
        self.enterRule(localctx, 62, self.RULE_static_attr_call)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 304
            self.match(D96Parser.NORMAL_ID)
            self.state = 305
            self.match(D96Parser.SCOPE)
            self.state = 306
            self.match(D96Parser.DOLLAR_ID)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Static_method_callContext(ParserRuleContext):

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




    def static_method_call(self):

        localctx = D96Parser.Static_method_callContext(self, self._ctx, self.state)
        self.enterRule(localctx, 64, self.RULE_static_method_call)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 308
            self.match(D96Parser.NORMAL_ID)
            self.state = 309
            self.match(D96Parser.SCOPE)
            self.state = 310
            self.match(D96Parser.DOLLAR_ID)
            self.state = 311
            self.match(D96Parser.LP)
            self.state = 312
            self.list_exp()
            self.state = 313
            self.match(D96Parser.RP)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Instance_attr_callContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def exp7(self):
            return self.getTypedRuleContext(D96Parser.Exp7Context,0)


        def DOT(self):
            return self.getToken(D96Parser.DOT, 0)

        def NORMAL_ID(self):
            return self.getToken(D96Parser.NORMAL_ID, 0)

        def getRuleIndex(self):
            return D96Parser.RULE_instance_attr_call




    def instance_attr_call(self):

        localctx = D96Parser.Instance_attr_callContext(self, self._ctx, self.state)
        self.enterRule(localctx, 66, self.RULE_instance_attr_call)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 315
            self.exp7(0)
            self.state = 316
            self.match(D96Parser.DOT)
            self.state = 317
            self.match(D96Parser.NORMAL_ID)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Instance_method_callContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

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
            return D96Parser.RULE_instance_method_call




    def instance_method_call(self):

        localctx = D96Parser.Instance_method_callContext(self, self._ctx, self.state)
        self.enterRule(localctx, 68, self.RULE_instance_method_call)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 319
            self.exp7(0)
            self.state = 320
            self.match(D96Parser.DOT)
            self.state = 321
            self.match(D96Parser.NORMAL_ID)
            self.state = 322
            self.match(D96Parser.LP)
            self.state = 323
            self.list_exp()
            self.state = 324
            self.match(D96Parser.RP)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Attribute_declareContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def dec_and_init_list1(self):
            return self.getTypedRuleContext(D96Parser.Dec_and_init_list1Context,0)


        def SEMI(self):
            return self.getToken(D96Parser.SEMI, 0)

        def VAR(self):
            return self.getToken(D96Parser.VAR, 0)

        def VAL(self):
            return self.getToken(D96Parser.VAL, 0)

        def getRuleIndex(self):
            return D96Parser.RULE_attribute_declare




    def attribute_declare(self):

        localctx = D96Parser.Attribute_declareContext(self, self._ctx, self.state)
        self.enterRule(localctx, 70, self.RULE_attribute_declare)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 326
            _la = self._input.LA(1)
            if not(_la==D96Parser.VAL or _la==D96Parser.VAR):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 327
            self.dec_and_init_list1()
            self.state = 328
            self.match(D96Parser.SEMI)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Dec_and_init_list1Context(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def pair1(self):
            return self.getTypedRuleContext(D96Parser.Pair1Context,0)


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
            return D96Parser.RULE_dec_and_init_list1




    def dec_and_init_list1(self):

        localctx = D96Parser.Dec_and_init_list1Context(self, self._ctx, self.state)
        self.enterRule(localctx, 72, self.RULE_dec_and_init_list1)
        self._la = 0 # Token type
        try:
            self.state = 347
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,20,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 330
                _la = self._input.LA(1)
                if not(_la==D96Parser.NORMAL_ID or _la==D96Parser.DOLLAR_ID):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 331
                self.pair1()
                self.state = 332
                self.exp()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 336
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,18,self._ctx)
                if la_ == 1:
                    self.state = 334
                    self.id_list()
                    pass

                elif la_ == 2:
                    self.state = 335
                    self.normal_id_list()
                    pass


                self.state = 338
                self.match(D96Parser.COLON)
                self.state = 345
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [D96Parser.BOOLEAN]:
                    self.state = 339
                    self.match(D96Parser.BOOLEAN)
                    pass
                elif token in [D96Parser.INT_TYPE]:
                    self.state = 340
                    self.match(D96Parser.INT_TYPE)
                    pass
                elif token in [D96Parser.FLOAT_TYPE]:
                    self.state = 341
                    self.match(D96Parser.FLOAT_TYPE)
                    pass
                elif token in [D96Parser.ARRAY]:
                    self.state = 342
                    self.array_type()
                    pass
                elif token in [D96Parser.STRING]:
                    self.state = 343
                    self.match(D96Parser.STRING)
                    pass
                elif token in [D96Parser.NORMAL_ID]:
                    self.state = 344
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


    class Pair1Context(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(D96Parser.COMMA)
            else:
                return self.getToken(D96Parser.COMMA, i)

        def pair1(self):
            return self.getTypedRuleContext(D96Parser.Pair1Context,0)


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
            return D96Parser.RULE_pair1




    def pair1(self):

        localctx = D96Parser.Pair1Context(self, self._ctx, self.state)
        self.enterRule(localctx, 74, self.RULE_pair1)
        self._la = 0 # Token type
        try:
            self.state = 365
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [D96Parser.COMMA]:
                self.enterOuterAlt(localctx, 1)
                self.state = 349
                self.match(D96Parser.COMMA)
                self.state = 350
                _la = self._input.LA(1)
                if not(_la==D96Parser.NORMAL_ID or _la==D96Parser.DOLLAR_ID):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 351
                self.pair1()
                self.state = 352
                self.exp()
                self.state = 353
                self.match(D96Parser.COMMA)
                pass
            elif token in [D96Parser.COLON]:
                self.enterOuterAlt(localctx, 2)
                self.state = 355
                self.match(D96Parser.COLON)
                self.state = 362
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [D96Parser.BOOLEAN]:
                    self.state = 356
                    self.match(D96Parser.BOOLEAN)
                    pass
                elif token in [D96Parser.INT_TYPE]:
                    self.state = 357
                    self.match(D96Parser.INT_TYPE)
                    pass
                elif token in [D96Parser.FLOAT_TYPE]:
                    self.state = 358
                    self.match(D96Parser.FLOAT_TYPE)
                    pass
                elif token in [D96Parser.ARRAY]:
                    self.state = 359
                    self.array_type()
                    pass
                elif token in [D96Parser.STRING]:
                    self.state = 360
                    self.match(D96Parser.STRING)
                    pass
                elif token in [D96Parser.NORMAL_ID]:
                    self.state = 361
                    self.match(D96Parser.NORMAL_ID)
                    pass
                else:
                    raise NoViableAltException(self)

                self.state = 364
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


    class Var_declareContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def dec_and_init_list2(self):
            return self.getTypedRuleContext(D96Parser.Dec_and_init_list2Context,0)


        def SEMI(self):
            return self.getToken(D96Parser.SEMI, 0)

        def VAR(self):
            return self.getToken(D96Parser.VAR, 0)

        def VAL(self):
            return self.getToken(D96Parser.VAL, 0)

        def getRuleIndex(self):
            return D96Parser.RULE_var_declare




    def var_declare(self):

        localctx = D96Parser.Var_declareContext(self, self._ctx, self.state)
        self.enterRule(localctx, 76, self.RULE_var_declare)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 367
            _la = self._input.LA(1)
            if not(_la==D96Parser.VAL or _la==D96Parser.VAR):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 368
            self.dec_and_init_list2()
            self.state = 369
            self.match(D96Parser.SEMI)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Dec_and_init_list2Context(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NORMAL_ID(self):
            return self.getToken(D96Parser.NORMAL_ID, 0)

        def pair2(self):
            return self.getTypedRuleContext(D96Parser.Pair2Context,0)


        def exp(self):
            return self.getTypedRuleContext(D96Parser.ExpContext,0)


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

        def getRuleIndex(self):
            return D96Parser.RULE_dec_and_init_list2




    def dec_and_init_list2(self):

        localctx = D96Parser.Dec_and_init_list2Context(self, self._ctx, self.state)
        self.enterRule(localctx, 78, self.RULE_dec_and_init_list2)
        try:
            self.state = 385
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,24,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 371
                self.match(D96Parser.NORMAL_ID)
                self.state = 372
                self.pair2()
                self.state = 373
                self.exp()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 375
                self.normal_id_list()
                self.state = 376
                self.match(D96Parser.COLON)
                self.state = 383
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [D96Parser.BOOLEAN]:
                    self.state = 377
                    self.match(D96Parser.BOOLEAN)
                    pass
                elif token in [D96Parser.INT_TYPE]:
                    self.state = 378
                    self.match(D96Parser.INT_TYPE)
                    pass
                elif token in [D96Parser.FLOAT_TYPE]:
                    self.state = 379
                    self.match(D96Parser.FLOAT_TYPE)
                    pass
                elif token in [D96Parser.ARRAY]:
                    self.state = 380
                    self.array_type()
                    pass
                elif token in [D96Parser.STRING]:
                    self.state = 381
                    self.match(D96Parser.STRING)
                    pass
                elif token in [D96Parser.NORMAL_ID]:
                    self.state = 382
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


    class Pair2Context(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(D96Parser.COMMA)
            else:
                return self.getToken(D96Parser.COMMA, i)

        def NORMAL_ID(self):
            return self.getToken(D96Parser.NORMAL_ID, 0)

        def pair2(self):
            return self.getTypedRuleContext(D96Parser.Pair2Context,0)


        def exp(self):
            return self.getTypedRuleContext(D96Parser.ExpContext,0)


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
            return D96Parser.RULE_pair2




    def pair2(self):

        localctx = D96Parser.Pair2Context(self, self._ctx, self.state)
        self.enterRule(localctx, 80, self.RULE_pair2)
        try:
            self.state = 403
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [D96Parser.COMMA]:
                self.enterOuterAlt(localctx, 1)
                self.state = 387
                self.match(D96Parser.COMMA)
                self.state = 388
                self.match(D96Parser.NORMAL_ID)
                self.state = 389
                self.pair2()
                self.state = 390
                self.exp()
                self.state = 391
                self.match(D96Parser.COMMA)
                pass
            elif token in [D96Parser.COLON]:
                self.enterOuterAlt(localctx, 2)
                self.state = 393
                self.match(D96Parser.COLON)
                self.state = 400
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [D96Parser.BOOLEAN]:
                    self.state = 394
                    self.match(D96Parser.BOOLEAN)
                    pass
                elif token in [D96Parser.INT_TYPE]:
                    self.state = 395
                    self.match(D96Parser.INT_TYPE)
                    pass
                elif token in [D96Parser.FLOAT_TYPE]:
                    self.state = 396
                    self.match(D96Parser.FLOAT_TYPE)
                    pass
                elif token in [D96Parser.ARRAY]:
                    self.state = 397
                    self.array_type()
                    pass
                elif token in [D96Parser.STRING]:
                    self.state = 398
                    self.match(D96Parser.STRING)
                    pass
                elif token in [D96Parser.NORMAL_ID]:
                    self.state = 399
                    self.match(D96Parser.NORMAL_ID)
                    pass
                else:
                    raise NoViableAltException(self)

                self.state = 402
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

        def getRuleIndex(self):
            return D96Parser.RULE_array_type




    def array_type(self):

        localctx = D96Parser.Array_typeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 82, self.RULE_array_type)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 405
            self.match(D96Parser.ARRAY)
            self.state = 406
            self.match(D96Parser.LSB)
            self.state = 412
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [D96Parser.BOOLEAN]:
                self.state = 407
                self.match(D96Parser.BOOLEAN)
                pass
            elif token in [D96Parser.INT_TYPE]:
                self.state = 408
                self.match(D96Parser.INT_TYPE)
                pass
            elif token in [D96Parser.FLOAT_TYPE]:
                self.state = 409
                self.match(D96Parser.FLOAT_TYPE)
                pass
            elif token in [D96Parser.ARRAY]:
                self.state = 410
                self.array_type()
                pass
            elif token in [D96Parser.STRING]:
                self.state = 411
                self.match(D96Parser.STRING)
                pass
            else:
                raise NoViableAltException(self)

            self.state = 414
            self.match(D96Parser.COMMA)
            self.state = 415
            self.match(D96Parser.ARRAY_SIZE)
            self.state = 416
            self.match(D96Parser.RSB)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Array_literalContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ARRAY(self):
            return self.getToken(D96Parser.ARRAY, 0)

        def LP(self):
            return self.getToken(D96Parser.LP, 0)

        def list_exp(self):
            return self.getTypedRuleContext(D96Parser.List_expContext,0)


        def RP(self):
            return self.getToken(D96Parser.RP, 0)

        def getRuleIndex(self):
            return D96Parser.RULE_array_literal




    def array_literal(self):

        localctx = D96Parser.Array_literalContext(self, self._ctx, self.state)
        self.enterRule(localctx, 84, self.RULE_array_literal)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 418
            self.match(D96Parser.ARRAY)
            self.state = 419
            self.match(D96Parser.LP)
            self.state = 420
            self.list_exp()
            self.state = 421
            self.match(D96Parser.RP)
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




    def exp(self):

        localctx = D96Parser.ExpContext(self, self._ctx, self.state)
        self.enterRule(localctx, 86, self.RULE_exp)
        try:
            self.state = 432
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,28,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 423
                self.exp0()
                self.state = 424
                self.match(D96Parser.EQUAL_STR)
                self.state = 425
                self.exp0()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 427
                self.exp0()
                self.state = 428
                self.match(D96Parser.ADD_STR)
                self.state = 429
                self.exp0()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 431
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

        def EQUAL(self):
            return self.getToken(D96Parser.EQUAL, 0)

        def NOTEQUAL(self):
            return self.getToken(D96Parser.NOTEQUAL, 0)

        def GTE(self):
            return self.getToken(D96Parser.GTE, 0)

        def getRuleIndex(self):
            return D96Parser.RULE_exp0




    def exp0(self):

        localctx = D96Parser.Exp0Context(self, self._ctx, self.state)
        self.enterRule(localctx, 88, self.RULE_exp0)
        try:
            self.state = 459
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,29,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 434
                self.exp1(0)
                self.state = 435
                self.match(D96Parser.LT)
                self.state = 436
                self.exp1(0)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 438
                self.exp1(0)
                self.state = 439
                self.match(D96Parser.LTE)
                self.state = 440
                self.exp1(0)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 442
                self.exp1(0)
                self.state = 443
                self.match(D96Parser.GT)
                self.state = 444
                self.exp1(0)
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 446
                self.exp1(0)
                self.state = 447
                self.match(D96Parser.EQUAL)
                self.state = 448
                self.exp1(0)
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 450
                self.exp1(0)
                self.state = 451
                self.match(D96Parser.NOTEQUAL)
                self.state = 452
                self.exp1(0)
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 454
                self.exp1(0)
                self.state = 455
                self.match(D96Parser.GTE)
                self.state = 456
                self.exp1(0)
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 458
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
        _startState = 90
        self.enterRecursionRule(localctx, 90, self.RULE_exp1, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 462
            self.exp2(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 472
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,31,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 470
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,30,self._ctx)
                    if la_ == 1:
                        localctx = D96Parser.Exp1Context(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_exp1)
                        self.state = 464
                        if not self.precpred(self._ctx, 3):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 3)")
                        self.state = 465
                        self.match(D96Parser.AND)
                        self.state = 466
                        self.exp2(0)
                        pass

                    elif la_ == 2:
                        localctx = D96Parser.Exp1Context(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_exp1)
                        self.state = 467
                        if not self.precpred(self._ctx, 2):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                        self.state = 468
                        self.match(D96Parser.OR)
                        self.state = 469
                        self.exp2(0)
                        pass

             
                self.state = 474
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,31,self._ctx)

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
        _startState = 92
        self.enterRecursionRule(localctx, 92, self.RULE_exp2, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 476
            self.exp3(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 486
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,33,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 484
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,32,self._ctx)
                    if la_ == 1:
                        localctx = D96Parser.Exp2Context(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_exp2)
                        self.state = 478
                        if not self.precpred(self._ctx, 3):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 3)")
                        self.state = 479
                        self.match(D96Parser.ADD)
                        self.state = 480
                        self.exp3(0)
                        pass

                    elif la_ == 2:
                        localctx = D96Parser.Exp2Context(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_exp2)
                        self.state = 481
                        if not self.precpred(self._ctx, 2):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                        self.state = 482
                        self.match(D96Parser.SUB)
                        self.state = 483
                        self.exp3(0)
                        pass

             
                self.state = 488
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,33,self._ctx)

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
        _startState = 94
        self.enterRecursionRule(localctx, 94, self.RULE_exp3, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 490
            self.exp4()
            self._ctx.stop = self._input.LT(-1)
            self.state = 503
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,35,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 501
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,34,self._ctx)
                    if la_ == 1:
                        localctx = D96Parser.Exp3Context(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_exp3)
                        self.state = 492
                        if not self.precpred(self._ctx, 4):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 4)")
                        self.state = 493
                        self.match(D96Parser.MUL)
                        self.state = 494
                        self.exp4()
                        pass

                    elif la_ == 2:
                        localctx = D96Parser.Exp3Context(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_exp3)
                        self.state = 495
                        if not self.precpred(self._ctx, 3):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 3)")
                        self.state = 496
                        self.match(D96Parser.DIV)
                        self.state = 497
                        self.exp4()
                        pass

                    elif la_ == 3:
                        localctx = D96Parser.Exp3Context(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_exp3)
                        self.state = 498
                        if not self.precpred(self._ctx, 2):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                        self.state = 499
                        self.match(D96Parser.MOD)
                        self.state = 500
                        self.exp4()
                        pass

             
                self.state = 505
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,35,self._ctx)

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
        self.enterRule(localctx, 96, self.RULE_exp4)
        try:
            self.state = 509
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [D96Parser.NOT]:
                self.enterOuterAlt(localctx, 1)
                self.state = 506
                self.match(D96Parser.NOT)
                self.state = 507
                self.exp4()
                pass
            elif token in [D96Parser.LP, D96Parser.ARRAY, D96Parser.NULL, D96Parser.NEW, D96Parser.SELF, D96Parser.SUB, D96Parser.BOOL_LITERAL, D96Parser.ARRAY_SIZE, D96Parser.INTEGER_LITERAL, D96Parser.STRING_LITERAL, D96Parser.REAL_LITERAL, D96Parser.NORMAL_ID]:
                self.enterOuterAlt(localctx, 2)
                self.state = 508
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
        self.enterRule(localctx, 98, self.RULE_exp5)
        try:
            self.state = 514
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [D96Parser.SUB]:
                self.enterOuterAlt(localctx, 1)
                self.state = 511
                self.match(D96Parser.SUB)
                self.state = 512
                self.exp5()
                pass
            elif token in [D96Parser.LP, D96Parser.ARRAY, D96Parser.NULL, D96Parser.NEW, D96Parser.SELF, D96Parser.BOOL_LITERAL, D96Parser.ARRAY_SIZE, D96Parser.INTEGER_LITERAL, D96Parser.STRING_LITERAL, D96Parser.REAL_LITERAL, D96Parser.NORMAL_ID]:
                self.enterOuterAlt(localctx, 2)
                self.state = 513
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

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def exp7(self):
            return self.getTypedRuleContext(D96Parser.Exp7Context,0)


        def exp6(self):
            return self.getTypedRuleContext(D96Parser.Exp6Context,0)


        def index_operators(self):
            return self.getTypedRuleContext(D96Parser.Index_operatorsContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_exp6



    def exp6(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = D96Parser.Exp6Context(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 100
        self.enterRecursionRule(localctx, 100, self.RULE_exp6, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 517
            self.exp7(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 523
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,38,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = D96Parser.Exp6Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_exp6)
                    self.state = 519
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 520
                    self.index_operators(0) 
                self.state = 525
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,38,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Index_operatorsContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LSB(self):
            return self.getToken(D96Parser.LSB, 0)

        def exp(self):
            return self.getTypedRuleContext(D96Parser.ExpContext,0)


        def RSB(self):
            return self.getToken(D96Parser.RSB, 0)

        def index_operators(self):
            return self.getTypedRuleContext(D96Parser.Index_operatorsContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_index_operators



    def index_operators(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = D96Parser.Index_operatorsContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 102
        self.enterRecursionRule(localctx, 102, self.RULE_index_operators, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 527
            self.match(D96Parser.LSB)
            self.state = 528
            self.exp()
            self.state = 529
            self.match(D96Parser.RSB)
            self._ctx.stop = self._input.LT(-1)
            self.state = 538
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,39,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = D96Parser.Index_operatorsContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_index_operators)
                    self.state = 531
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 532
                    self.match(D96Parser.LSB)
                    self.state = 533
                    self.exp()
                    self.state = 534
                    self.match(D96Parser.RSB) 
                self.state = 540
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,39,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
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

        def LP(self):
            return self.getToken(D96Parser.LP, 0)

        def list_exp(self):
            return self.getTypedRuleContext(D96Parser.List_expContext,0)


        def RP(self):
            return self.getToken(D96Parser.RP, 0)

        def getRuleIndex(self):
            return D96Parser.RULE_exp7



    def exp7(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = D96Parser.Exp7Context(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 104
        self.enterRecursionRule(localctx, 104, self.RULE_exp7, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 542
            self.exp8()
            self._ctx.stop = self._input.LT(-1)
            self.state = 556
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,41,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 554
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,40,self._ctx)
                    if la_ == 1:
                        localctx = D96Parser.Exp7Context(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_exp7)
                        self.state = 544
                        if not self.precpred(self._ctx, 3):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 3)")
                        self.state = 545
                        self.match(D96Parser.DOT)
                        self.state = 546
                        self.match(D96Parser.NORMAL_ID)
                        pass

                    elif la_ == 2:
                        localctx = D96Parser.Exp7Context(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_exp7)
                        self.state = 547
                        if not self.precpred(self._ctx, 2):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                        self.state = 548
                        self.match(D96Parser.DOT)
                        self.state = 549
                        self.match(D96Parser.NORMAL_ID)
                        self.state = 550
                        self.match(D96Parser.LP)
                        self.state = 551
                        self.list_exp()
                        self.state = 552
                        self.match(D96Parser.RP)
                        pass

             
                self.state = 558
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,41,self._ctx)

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




    def exp8(self):

        localctx = D96Parser.Exp8Context(self, self._ctx, self.state)
        self.enterRule(localctx, 106, self.RULE_exp8)
        try:
            self.state = 570
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,42,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 559
                self.match(D96Parser.NORMAL_ID)
                self.state = 560
                self.match(D96Parser.SCOPE)
                self.state = 561
                self.match(D96Parser.DOLLAR_ID)
                self.state = 562
                self.match(D96Parser.LP)
                self.state = 563
                self.list_exp()
                self.state = 564
                self.match(D96Parser.RP)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 566
                self.match(D96Parser.NORMAL_ID)
                self.state = 567
                self.match(D96Parser.SCOPE)
                self.state = 568
                self.match(D96Parser.DOLLAR_ID)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 569
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

        def exp10(self):
            return self.getTypedRuleContext(D96Parser.Exp10Context,0)


        def getRuleIndex(self):
            return D96Parser.RULE_exp9




    def exp9(self):

        localctx = D96Parser.Exp9Context(self, self._ctx, self.state)
        self.enterRule(localctx, 108, self.RULE_exp9)
        try:
            self.state = 579
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [D96Parser.NEW]:
                self.enterOuterAlt(localctx, 1)
                self.state = 572
                self.match(D96Parser.NEW)
                self.state = 573
                self.match(D96Parser.NORMAL_ID)
                self.state = 574
                self.match(D96Parser.LP)
                self.state = 575
                self.list_exp()
                self.state = 576
                self.match(D96Parser.RP)
                pass
            elif token in [D96Parser.LP, D96Parser.ARRAY, D96Parser.NULL, D96Parser.SELF, D96Parser.BOOL_LITERAL, D96Parser.ARRAY_SIZE, D96Parser.INTEGER_LITERAL, D96Parser.STRING_LITERAL, D96Parser.REAL_LITERAL, D96Parser.NORMAL_ID]:
                self.enterOuterAlt(localctx, 2)
                self.state = 578
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

        def SELF(self):
            return self.getToken(D96Parser.SELF, 0)

        def NULL(self):
            return self.getToken(D96Parser.NULL, 0)

        def exp11(self):
            return self.getTypedRuleContext(D96Parser.Exp11Context,0)


        def getRuleIndex(self):
            return D96Parser.RULE_exp10




    def exp10(self):

        localctx = D96Parser.Exp10Context(self, self._ctx, self.state)
        self.enterRule(localctx, 110, self.RULE_exp10)
        try:
            self.state = 591
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [D96Parser.ARRAY_SIZE]:
                self.enterOuterAlt(localctx, 1)
                self.state = 581
                self.match(D96Parser.ARRAY_SIZE)
                pass
            elif token in [D96Parser.INTEGER_LITERAL]:
                self.enterOuterAlt(localctx, 2)
                self.state = 582
                self.match(D96Parser.INTEGER_LITERAL)
                pass
            elif token in [D96Parser.ARRAY]:
                self.enterOuterAlt(localctx, 3)
                self.state = 583
                self.array_literal()
                pass
            elif token in [D96Parser.BOOL_LITERAL]:
                self.enterOuterAlt(localctx, 4)
                self.state = 584
                self.match(D96Parser.BOOL_LITERAL)
                pass
            elif token in [D96Parser.REAL_LITERAL]:
                self.enterOuterAlt(localctx, 5)
                self.state = 585
                self.match(D96Parser.REAL_LITERAL)
                pass
            elif token in [D96Parser.STRING_LITERAL]:
                self.enterOuterAlt(localctx, 6)
                self.state = 586
                self.match(D96Parser.STRING_LITERAL)
                pass
            elif token in [D96Parser.NORMAL_ID]:
                self.enterOuterAlt(localctx, 7)
                self.state = 587
                self.match(D96Parser.NORMAL_ID)
                pass
            elif token in [D96Parser.SELF]:
                self.enterOuterAlt(localctx, 8)
                self.state = 588
                self.match(D96Parser.SELF)
                pass
            elif token in [D96Parser.NULL]:
                self.enterOuterAlt(localctx, 9)
                self.state = 589
                self.match(D96Parser.NULL)
                pass
            elif token in [D96Parser.LP]:
                self.enterOuterAlt(localctx, 10)
                self.state = 590
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




    def exp11(self):

        localctx = D96Parser.Exp11Context(self, self._ctx, self.state)
        self.enterRule(localctx, 112, self.RULE_exp11)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 593
            self.match(D96Parser.LP)
            self.state = 594
            self.exp()
            self.state = 595
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

        def exps(self):
            return self.getTypedRuleContext(D96Parser.ExpsContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_list_exp




    def list_exp(self):

        localctx = D96Parser.List_expContext(self, self._ctx, self.state)
        self.enterRule(localctx, 114, self.RULE_list_exp)
        try:
            self.state = 599
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [D96Parser.LP, D96Parser.ARRAY, D96Parser.NULL, D96Parser.NEW, D96Parser.SELF, D96Parser.SUB, D96Parser.NOT, D96Parser.BOOL_LITERAL, D96Parser.ARRAY_SIZE, D96Parser.INTEGER_LITERAL, D96Parser.STRING_LITERAL, D96Parser.REAL_LITERAL, D96Parser.NORMAL_ID]:
                self.enterOuterAlt(localctx, 1)
                self.state = 597
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




    def exps(self):

        localctx = D96Parser.ExpsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 116, self.RULE_exps)
        try:
            self.state = 606
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,46,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 601
                self.exp()
                self.state = 602
                self.match(D96Parser.COMMA)
                self.state = 603
                self.exps()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 605
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
        self.enterRule(localctx, 118, self.RULE_normal_id_list)
        try:
            self.state = 612
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,47,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 608
                self.match(D96Parser.NORMAL_ID)
                self.state = 609
                self.match(D96Parser.COMMA)
                self.state = 610
                self.normal_id_list()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 611
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




    def id_list(self):

        localctx = D96Parser.Id_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 120, self.RULE_id_list)
        self._la = 0 # Token type
        try:
            self.state = 618
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,48,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 614
                _la = self._input.LA(1)
                if not(_la==D96Parser.NORMAL_ID or _la==D96Parser.DOLLAR_ID):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 615
                self.match(D96Parser.COMMA)
                self.state = 616
                self.id_list()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 617
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
        self._predicates[45] = self.exp1_sempred
        self._predicates[46] = self.exp2_sempred
        self._predicates[47] = self.exp3_sempred
        self._predicates[50] = self.exp6_sempred
        self._predicates[51] = self.index_operators_sempred
        self._predicates[52] = self.exp7_sempred
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
         

    def index_operators_sempred(self, localctx:Index_operatorsContext, predIndex:int):
            if predIndex == 8:
                return self.precpred(self._ctx, 2)
         

    def exp7_sempred(self, localctx:Exp7Context, predIndex:int):
            if predIndex == 9:
                return self.precpred(self._ctx, 3)
         

            if predIndex == 10:
                return self.precpred(self._ctx, 2)
         




