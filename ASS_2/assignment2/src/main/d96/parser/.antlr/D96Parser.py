# Generated from e:\HCMUT\PRINCIPLES_OF_PROGRAMMING_LANGUAGE\ppl-assignments\ASS_2\assignment2\src\main\d96\parser\D96.g4 by ANTLR 4.8
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
        buf.write("\u02b0\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
        buf.write("\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r\4\16")
        buf.write("\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23\t\23")
        buf.write("\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30\4\31")
        buf.write("\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36\t\36")
        buf.write("\4\37\t\37\4 \t \4!\t!\4\"\t\"\4#\t#\4$\t$\4%\t%\4&\t")
        buf.write("&\4\'\t\'\4(\t(\4)\t)\4*\t*\4+\t+\4,\t,\4-\t-\4.\t.\4")
        buf.write("/\t/\4\60\t\60\4\61\t\61\4\62\t\62\4\63\t\63\4\64\t\64")
        buf.write("\4\65\t\65\4\66\t\66\4\67\t\67\48\t8\49\t9\4:\t:\4;\t")
        buf.write(";\4<\t<\4=\t=\4>\t>\4?\t?\4@\t@\4A\tA\4B\tB\4C\tC\4D\t")
        buf.write("D\4E\tE\3\2\3\2\3\2\3\3\3\3\3\3\3\3\5\3\u0092\n\3\3\4")
        buf.write("\3\4\3\4\3\4\3\4\3\5\3\5\3\5\5\5\u009c\n\5\3\6\3\6\3\6")
        buf.write("\3\6\3\7\3\7\5\7\u00a4\n\7\3\b\3\b\3\b\3\b\5\b\u00aa\n")
        buf.write("\b\3\t\3\t\3\t\3\t\3\t\5\t\u00b1\n\t\3\n\3\n\3\n\3\n\3")
        buf.write("\n\3\n\3\13\3\13\3\13\3\13\3\13\3\f\3\f\3\f\3\f\3\f\3")
        buf.write("\f\3\r\3\r\5\r\u00c6\n\r\3\16\3\16\3\16\3\16\3\16\5\16")
        buf.write("\u00cd\n\16\3\17\3\17\3\17\3\17\3\17\3\17\3\17\3\17\5")
        buf.write("\17\u00d7\n\17\3\20\3\20\3\20\3\20\3\21\3\21\5\21\u00df")
        buf.write("\n\21\3\22\3\22\3\22\3\22\5\22\u00e5\n\22\3\23\3\23\3")
        buf.write("\23\3\23\3\23\3\23\3\23\3\23\3\23\3\23\3\23\3\23\3\23")
        buf.write("\3\23\5\23\u00f5\n\23\3\24\3\24\3\24\3\25\3\25\3\25\3")
        buf.write("\26\3\26\3\26\3\26\3\27\3\27\5\27\u0103\n\27\3\30\3\30")
        buf.write("\3\30\3\30\3\30\3\31\3\31\3\31\3\31\3\31\3\31\3\31\3\31")
        buf.write("\3\32\3\32\5\32\u0114\n\32\3\33\3\33\3\33\3\33\5\33\u011a")
        buf.write("\n\33\3\34\3\34\3\34\3\34\3\34\3\34\3\35\3\35\3\35\5\35")
        buf.write("\u0125\n\35\3\36\3\36\3\36\3\36\3\36\5\36\u012c\n\36\3")
        buf.write("\36\3\36\3\36\3\36\3\36\3\36\3\36\3\36\3\37\3\37\3\37")
        buf.write("\5\37\u0139\n\37\3 \3 \3 \3 \5 \u013f\n \3!\3!\3!\3!\3")
        buf.write("\"\3\"\3\"\3\"\3\"\3\"\3\"\3#\3#\3#\3#\3$\3$\3$\3$\3$")
        buf.write("\3$\3$\3%\3%\3%\3%\3&\3&\3&\3&\3&\3&\5&\u0161\n&\3&\3")
        buf.write("&\3&\3&\3&\3&\3&\5&\u016a\n&\5&\u016c\n&\3\'\3\'\3\'\3")
        buf.write("\'\3\'\3\'\3\'\3\'\3\'\3\'\3\'\3\'\3\'\5\'\u017b\n\'\3")
        buf.write("\'\5\'\u017e\n\'\3(\3(\3(\3(\3)\3)\3)\3)\3*\3*\3*\3*\3")
        buf.write("*\3*\3*\3*\3*\3*\3*\3*\3*\5*\u0195\n*\3*\5*\u0198\n*\3")
        buf.write("+\3+\3+\3+\3,\3,\3,\3,\3,\3,\3,\3,\3,\3,\3,\3,\5,\u01aa")
        buf.write("\n,\5,\u01ac\n,\3-\3-\3-\3-\3-\3-\3-\3-\3-\3-\3-\3-\3")
        buf.write("-\5-\u01bb\n-\3-\5-\u01be\n-\3.\3.\3.\3.\3/\3/\3/\3/\3")
        buf.write("\60\3\60\3\60\3\60\3\60\3\60\3\60\3\60\3\60\3\60\3\60")
        buf.write("\3\60\3\60\5\60\u01d5\n\60\3\60\5\60\u01d8\n\60\3\61\3")
        buf.write("\61\3\61\3\61\3\61\3\61\3\61\5\61\u01e1\n\61\3\61\3\61")
        buf.write("\3\61\3\61\3\62\3\62\3\62\3\62\3\62\3\63\3\63\5\63\u01ee")
        buf.write("\n\63\3\64\3\64\3\64\3\64\3\64\5\64\u01f5\n\64\3\65\3")
        buf.write("\65\3\65\3\65\3\65\3\65\3\65\3\65\3\65\5\65\u0200\n\65")
        buf.write("\3\66\3\66\3\66\3\66\3\66\3\66\3\66\3\66\3\66\3\66\3\66")
        buf.write("\3\66\3\66\3\66\3\66\3\66\3\66\3\66\3\66\3\66\3\66\3\66")
        buf.write("\3\66\3\66\3\66\5\66\u021b\n\66\3\67\3\67\3\67\3\67\3")
        buf.write("\67\3\67\3\67\3\67\3\67\7\67\u0226\n\67\f\67\16\67\u0229")
        buf.write("\13\67\38\38\38\38\38\38\38\38\38\78\u0234\n8\f8\168\u0237")
        buf.write("\138\39\39\39\39\39\39\39\39\39\39\39\39\79\u0245\n9\f")
        buf.write("9\169\u0248\139\3:\3:\3:\5:\u024d\n:\3;\3;\3;\5;\u0252")
        buf.write("\n;\3<\3<\3<\3<\3<\3<\3<\3<\7<\u025c\n<\f<\16<\u025f\13")
        buf.write("<\3=\3=\3=\3=\3=\3=\3=\3=\3=\3=\3=\3=\3=\7=\u026e\n=\f")
        buf.write("=\16=\u0271\13=\3>\3>\3>\3>\3>\3>\3>\3>\3>\3>\3>\5>\u027e")
        buf.write("\n>\3?\3?\3?\3?\3?\3?\3?\5?\u0287\n?\3@\3@\3@\3@\3@\3")
        buf.write("@\3@\3@\3@\3@\5@\u0293\n@\3A\3A\3A\3A\3B\3B\5B\u029b\n")
        buf.write("B\3C\3C\3C\3C\3C\5C\u02a2\nC\3D\3D\3D\3D\5D\u02a8\nD\3")
        buf.write("E\3E\3E\3E\5E\u02ae\nE\3E\2\7lnpvxF\2\4\6\b\n\f\16\20")
        buf.write("\22\24\26\30\32\34\36 \"$&(*,.\60\62\64\668:<>@BDFHJL")
        buf.write("NPRTVXZ\\^`bdfhjlnprtvxz|~\u0080\u0082\u0084\u0086\u0088")
        buf.write("\2\3\3\2=>\2\u02de\2\u008a\3\2\2\2\4\u0091\3\2\2\2\6\u0093")
        buf.write("\3\2\2\2\b\u009b\3\2\2\2\n\u009d\3\2\2\2\f\u00a3\3\2\2")
        buf.write("\2\16\u00a9\3\2\2\2\20\u00b0\3\2\2\2\22\u00b2\3\2\2\2")
        buf.write("\24\u00b8\3\2\2\2\26\u00bd\3\2\2\2\30\u00c5\3\2\2\2\32")
        buf.write("\u00cc\3\2\2\2\34\u00ce\3\2\2\2\36\u00d8\3\2\2\2 \u00de")
        buf.write("\3\2\2\2\"\u00e4\3\2\2\2$\u00f4\3\2\2\2&\u00f6\3\2\2\2")
        buf.write("(\u00f9\3\2\2\2*\u00fc\3\2\2\2,\u0102\3\2\2\2.\u0104\3")
        buf.write("\2\2\2\60\u0109\3\2\2\2\62\u0113\3\2\2\2\64\u0119\3\2")
        buf.write("\2\2\66\u011b\3\2\2\28\u0124\3\2\2\2:\u0126\3\2\2\2<\u0138")
        buf.write("\3\2\2\2>\u013e\3\2\2\2@\u0140\3\2\2\2B\u0144\3\2\2\2")
        buf.write("D\u014b\3\2\2\2F\u014f\3\2\2\2H\u0156\3\2\2\2J\u016b\3")
        buf.write("\2\2\2L\u017d\3\2\2\2N\u017f\3\2\2\2P\u0183\3\2\2\2R\u0197")
        buf.write("\3\2\2\2T\u0199\3\2\2\2V\u01ab\3\2\2\2X\u01bd\3\2\2\2")
        buf.write("Z\u01bf\3\2\2\2\\\u01c3\3\2\2\2^\u01d7\3\2\2\2`\u01d9")
        buf.write("\3\2\2\2b\u01e6\3\2\2\2d\u01ed\3\2\2\2f\u01f4\3\2\2\2")
        buf.write("h\u01ff\3\2\2\2j\u021a\3\2\2\2l\u021c\3\2\2\2n\u022a\3")
        buf.write("\2\2\2p\u0238\3\2\2\2r\u024c\3\2\2\2t\u0251\3\2\2\2v\u0253")
        buf.write("\3\2\2\2x\u0260\3\2\2\2z\u027d\3\2\2\2|\u0286\3\2\2\2")
        buf.write("~\u0292\3\2\2\2\u0080\u0294\3\2\2\2\u0082\u029a\3\2\2")
        buf.write("\2\u0084\u02a1\3\2\2\2\u0086\u02a7\3\2\2\2\u0088\u02ad")
        buf.write("\3\2\2\2\u008a\u008b\5\4\3\2\u008b\u008c\7\2\2\3\u008c")
        buf.write("\3\3\2\2\2\u008d\u0092\5\6\4\2\u008e\u008f\5\6\4\2\u008f")
        buf.write("\u0090\5\4\3\2\u0090\u0092\3\2\2\2\u0091\u008d\3\2\2\2")
        buf.write("\u0091\u008e\3\2\2\2\u0092\5\3\2\2\2\u0093\u0094\7\62")
        buf.write("\2\2\u0094\u0095\7=\2\2\u0095\u0096\5\b\5\2\u0096\u0097")
        buf.write("\5\n\6\2\u0097\7\3\2\2\2\u0098\u0099\7\r\2\2\u0099\u009c")
        buf.write("\7=\2\2\u009a\u009c\3\2\2\2\u009b\u0098\3\2\2\2\u009b")
        buf.write("\u009a\3\2\2\2\u009c\t\3\2\2\2\u009d\u009e\7\7\2\2\u009e")
        buf.write("\u009f\5\f\7\2\u009f\u00a0\7\b\2\2\u00a0\13\3\2\2\2\u00a1")
        buf.write("\u00a4\5\16\b\2\u00a2\u00a4\3\2\2\2\u00a3\u00a1\3\2\2")
        buf.write("\2\u00a3\u00a2\3\2\2\2\u00a4\r\3\2\2\2\u00a5\u00a6\5\20")
        buf.write("\t\2\u00a6\u00a7\5\16\b\2\u00a7\u00aa\3\2\2\2\u00a8\u00aa")
        buf.write("\5\20\t\2\u00a9\u00a5\3\2\2\2\u00a9\u00a8\3\2\2\2\u00aa")
        buf.write("\17\3\2\2\2\u00ab\u00b1\5H%\2\u00ac\u00b1\5N(\2\u00ad")
        buf.write("\u00b1\5\22\n\2\u00ae\u00b1\5\24\13\2\u00af\u00b1\5\26")
        buf.write("\f\2\u00b0\u00ab\3\2\2\2\u00b0\u00ac\3\2\2\2\u00b0\u00ad")
        buf.write("\3\2\2\2\u00b0\u00ae\3\2\2\2\u00b0\u00af\3\2\2\2\u00b1")
        buf.write("\21\3\2\2\2\u00b2\u00b3\7\31\2\2\u00b3\u00b4\7\5\2\2\u00b4")
        buf.write("\u00b5\5\30\r\2\u00b5\u00b6\7\6\2\2\u00b6\u00b7\5\36\20")
        buf.write("\2\u00b7\23\3\2\2\2\u00b8\u00b9\7\32\2\2\u00b9\u00ba\7")
        buf.write("\5\2\2\u00ba\u00bb\7\6\2\2\u00bb\u00bc\5\36\20\2\u00bc")
        buf.write("\25\3\2\2\2\u00bd\u00be\t\2\2\2\u00be\u00bf\7\5\2\2\u00bf")
        buf.write("\u00c0\5\30\r\2\u00c0\u00c1\7\6\2\2\u00c1\u00c2\5\36\20")
        buf.write("\2\u00c2\27\3\2\2\2\u00c3\u00c6\5\32\16\2\u00c4\u00c6")
        buf.write("\3\2\2\2\u00c5\u00c3\3\2\2\2\u00c5\u00c4\3\2\2\2\u00c6")
        buf.write("\31\3\2\2\2\u00c7\u00c8\5\34\17\2\u00c8\u00c9\7\13\2\2")
        buf.write("\u00c9\u00ca\5\32\16\2\u00ca\u00cd\3\2\2\2\u00cb\u00cd")
        buf.write("\5\34\17\2\u00cc\u00c7\3\2\2\2\u00cc\u00cb\3\2\2\2\u00cd")
        buf.write("\33\3\2\2\2\u00ce\u00cf\5\u0086D\2\u00cf\u00d6\7\r\2\2")
        buf.write("\u00d0\u00d7\7\26\2\2\u00d1\u00d7\7\65\2\2\u00d2\u00d7")
        buf.write("\7\63\2\2\u00d3\u00d7\5`\61\2\u00d4\u00d7\7\64\2\2\u00d5")
        buf.write("\u00d7\7=\2\2\u00d6\u00d0\3\2\2\2\u00d6\u00d1\3\2\2\2")
        buf.write("\u00d6\u00d2\3\2\2\2\u00d6\u00d3\3\2\2\2\u00d6\u00d4\3")
        buf.write("\2\2\2\u00d6\u00d5\3\2\2\2\u00d7\35\3\2\2\2\u00d8\u00d9")
        buf.write("\7\7\2\2\u00d9\u00da\5 \21\2\u00da\u00db\7\b\2\2\u00db")
        buf.write("\37\3\2\2\2\u00dc\u00df\5\"\22\2\u00dd\u00df\3\2\2\2\u00de")
        buf.write("\u00dc\3\2\2\2\u00de\u00dd\3\2\2\2\u00df!\3\2\2\2\u00e0")
        buf.write("\u00e1\5$\23\2\u00e1\u00e2\5\"\22\2\u00e2\u00e5\3\2\2")
        buf.write("\2\u00e3\u00e5\5$\23\2\u00e4\u00e0\3\2\2\2\u00e4\u00e3")
        buf.write("\3\2\2\2\u00e5#\3\2\2\2\u00e6\u00f5\5.\30\2\u00e7\u00f5")
        buf.write("\5T+\2\u00e8\u00f5\5Z.\2\u00e9\u00f5\5&\24\2\u00ea\u00f5")
        buf.write("\5(\25\2\u00eb\u00f5\5*\26\2\u00ec\u00ed\5B\"\2\u00ed")
        buf.write("\u00ee\7\13\2\2\u00ee\u00f5\3\2\2\2\u00ef\u00f0\5F$\2")
        buf.write("\u00f0\u00f1\7\13\2\2\u00f1\u00f5\3\2\2\2\u00f2\u00f5")
        buf.write("\5\60\31\2\u00f3\u00f5\5:\36\2\u00f4\u00e6\3\2\2\2\u00f4")
        buf.write("\u00e7\3\2\2\2\u00f4\u00e8\3\2\2\2\u00f4\u00e9\3\2\2\2")
        buf.write("\u00f4\u00ea\3\2\2\2\u00f4\u00eb\3\2\2\2\u00f4\u00ec\3")
        buf.write("\2\2\2\u00f4\u00ef\3\2\2\2\u00f4\u00f2\3\2\2\2\u00f4\u00f3")
        buf.write("\3\2\2\2\u00f5%\3\2\2\2\u00f6\u00f7\7\16\2\2\u00f7\u00f8")
        buf.write("\7\13\2\2\u00f8\'\3\2\2\2\u00f9\u00fa\7\17\2\2\u00fa\u00fb")
        buf.write("\7\13\2\2\u00fb)\3\2\2\2\u00fc\u00fd\7\27\2\2\u00fd\u00fe")
        buf.write("\5,\27\2\u00fe\u00ff\7\13\2\2\u00ff+\3\2\2\2\u0100\u0103")
        buf.write("\5h\65\2\u0101\u0103\3\2\2\2\u0102\u0100\3\2\2\2\u0102")
        buf.write("\u0101\3\2\2\2\u0103-\3\2\2\2\u0104\u0105\5> \2\u0105")
        buf.write("\u0106\7\'\2\2\u0106\u0107\5h\65\2\u0107\u0108\7\13\2")
        buf.write("\2\u0108/\3\2\2\2\u0109\u010a\7\20\2\2\u010a\u010b\7\5")
        buf.write("\2\2\u010b\u010c\5h\65\2\u010c\u010d\7\6\2\2\u010d\u010e")
        buf.write("\5\36\20\2\u010e\u010f\5\62\32\2\u010f\u0110\58\35\2\u0110")
        buf.write("\61\3\2\2\2\u0111\u0114\5\64\33\2\u0112\u0114\3\2\2\2")
        buf.write("\u0113\u0111\3\2\2\2\u0113\u0112\3\2\2\2\u0114\63\3\2")
        buf.write("\2\2\u0115\u011a\5\66\34\2\u0116\u0117\5\66\34\2\u0117")
        buf.write("\u0118\5\64\33\2\u0118\u011a\3\2\2\2\u0119\u0115\3\2\2")
        buf.write("\2\u0119\u0116\3\2\2\2\u011a\65\3\2\2\2\u011b\u011c\7")
        buf.write("\21\2\2\u011c\u011d\7\5\2\2\u011d\u011e\5h\65\2\u011e")
        buf.write("\u011f\7\6\2\2\u011f\u0120\5\36\20\2\u0120\67\3\2\2\2")
        buf.write("\u0121\u0122\7\22\2\2\u0122\u0125\5\36\20\2\u0123\u0125")
        buf.write("\3\2\2\2\u0124\u0121\3\2\2\2\u0124\u0123\3\2\2\2\u0125")
        buf.write("9\3\2\2\2\u0126\u0127\7\23\2\2\u0127\u012b\7\5\2\2\u0128")
        buf.write("\u012c\7=\2\2\u0129\u012c\5@!\2\u012a\u012c\5D#\2\u012b")
        buf.write("\u0128\3\2\2\2\u012b\u0129\3\2\2\2\u012b\u012a\3\2\2\2")
        buf.write("\u012c\u012d\3\2\2\2\u012d\u012e\7\25\2\2\u012e\u012f")
        buf.write("\5h\65\2\u012f\u0130\7\60\2\2\u0130\u0131\5h\65\2\u0131")
        buf.write("\u0132\5<\37\2\u0132\u0133\7\6\2\2\u0133\u0134\5\36\20")
        buf.write("\2\u0134;\3\2\2\2\u0135\u0136\7\34\2\2\u0136\u0139\5h")
        buf.write("\65\2\u0137\u0139\3\2\2\2\u0138\u0135\3\2\2\2\u0138\u0137")
        buf.write("\3\2\2\2\u0139=\3\2\2\2\u013a\u013f\7=\2\2\u013b\u013f")
        buf.write("\5v<\2\u013c\u013f\5@!\2\u013d\u013f\5D#\2\u013e\u013a")
        buf.write("\3\2\2\2\u013e\u013b\3\2\2\2\u013e\u013c\3\2\2\2\u013e")
        buf.write("\u013d\3\2\2\2\u013f?\3\2\2\2\u0140\u0141\7=\2\2\u0141")
        buf.write("\u0142\7\61\2\2\u0142\u0143\7>\2\2\u0143A\3\2\2\2\u0144")
        buf.write("\u0145\7=\2\2\u0145\u0146\7\61\2\2\u0146\u0147\7>\2\2")
        buf.write("\u0147\u0148\7\5\2\2\u0148\u0149\5\u0082B\2\u0149\u014a")
        buf.write("\7\6\2\2\u014aC\3\2\2\2\u014b\u014c\5x=\2\u014c\u014d")
        buf.write("\7/\2\2\u014d\u014e\7=\2\2\u014eE\3\2\2\2\u014f\u0150")
        buf.write("\5x=\2\u0150\u0151\7/\2\2\u0151\u0152\7=\2\2\u0152\u0153")
        buf.write("\7\5\2\2\u0153\u0154\5\u0082B\2\u0154\u0155\7\6\2\2\u0155")
        buf.write("G\3\2\2\2\u0156\u0157\7\4\2\2\u0157\u0158\5J&\2\u0158")
        buf.write("\u0159\7\13\2\2\u0159I\3\2\2\2\u015a\u015b\t\2\2\2\u015b")
        buf.write("\u015c\5L\'\2\u015c\u015d\5h\65\2\u015d\u016c\3\2\2\2")
        buf.write("\u015e\u0161\5\u0088E\2\u015f\u0161\5\u0086D\2\u0160\u015e")
        buf.write("\3\2\2\2\u0160\u015f\3\2\2\2\u0161\u0162\3\2\2\2\u0162")
        buf.write("\u0169\7\r\2\2\u0163\u016a\7\26\2\2\u0164\u016a\7\65\2")
        buf.write("\2\u0165\u016a\7\63\2\2\u0166\u016a\5`\61\2\u0167\u016a")
        buf.write("\7\64\2\2\u0168\u016a\7=\2\2\u0169\u0163\3\2\2\2\u0169")
        buf.write("\u0164\3\2\2\2\u0169\u0165\3\2\2\2\u0169\u0166\3\2\2\2")
        buf.write("\u0169\u0167\3\2\2\2\u0169\u0168\3\2\2\2\u016a\u016c\3")
        buf.write("\2\2\2\u016b\u015a\3\2\2\2\u016b\u0160\3\2\2\2\u016cK")
        buf.write("\3\2\2\2\u016d\u016e\7\f\2\2\u016e\u016f\t\2\2\2\u016f")
        buf.write("\u0170\5L\'\2\u0170\u0171\5h\65\2\u0171\u0172\7\f\2\2")
        buf.write("\u0172\u017e\3\2\2\2\u0173\u017a\7\r\2\2\u0174\u017b\7")
        buf.write("\26\2\2\u0175\u017b\7\65\2\2\u0176\u017b\7\63\2\2\u0177")
        buf.write("\u017b\5`\61\2\u0178\u017b\7\64\2\2\u0179\u017b\7=\2\2")
        buf.write("\u017a\u0174\3\2\2\2\u017a\u0175\3\2\2\2\u017a\u0176\3")
        buf.write("\2\2\2\u017a\u0177\3\2\2\2\u017a\u0178\3\2\2\2\u017a\u0179")
        buf.write("\3\2\2\2\u017b\u017c\3\2\2\2\u017c\u017e\7\'\2\2\u017d")
        buf.write("\u016d\3\2\2\2\u017d\u0173\3\2\2\2\u017eM\3\2\2\2\u017f")
        buf.write("\u0180\7\3\2\2\u0180\u0181\5P)\2\u0181\u0182\7\13\2\2")
        buf.write("\u0182O\3\2\2\2\u0183\u0184\t\2\2\2\u0184\u0185\5R*\2")
        buf.write("\u0185\u0186\5h\65\2\u0186Q\3\2\2\2\u0187\u0188\7\f\2")
        buf.write("\2\u0188\u0189\t\2\2\2\u0189\u018a\5R*\2\u018a\u018b\5")
        buf.write("h\65\2\u018b\u018c\7\f\2\2\u018c\u0198\3\2\2\2\u018d\u0194")
        buf.write("\7\r\2\2\u018e\u0195\7\26\2\2\u018f\u0195\7\65\2\2\u0190")
        buf.write("\u0195\7\63\2\2\u0191\u0195\5`\61\2\u0192\u0195\7\64\2")
        buf.write("\2\u0193\u0195\7=\2\2\u0194\u018e\3\2\2\2\u0194\u018f")
        buf.write("\3\2\2\2\u0194\u0190\3\2\2\2\u0194\u0191\3\2\2\2\u0194")
        buf.write("\u0192\3\2\2\2\u0194\u0193\3\2\2\2\u0195\u0196\3\2\2\2")
        buf.write("\u0196\u0198\7\'\2\2\u0197\u0187\3\2\2\2\u0197\u018d\3")
        buf.write("\2\2\2\u0198S\3\2\2\2\u0199\u019a\7\4\2\2\u019a\u019b")
        buf.write("\5V,\2\u019b\u019c\7\13\2\2\u019cU\3\2\2\2\u019d\u019e")
        buf.write("\7=\2\2\u019e\u019f\5X-\2\u019f\u01a0\5h\65\2\u01a0\u01ac")
        buf.write("\3\2\2\2\u01a1\u01a2\5\u0086D\2\u01a2\u01a9\7\r\2\2\u01a3")
        buf.write("\u01aa\7\26\2\2\u01a4\u01aa\7\65\2\2\u01a5\u01aa\7\63")
        buf.write("\2\2\u01a6\u01aa\5`\61\2\u01a7\u01aa\7\64\2\2\u01a8\u01aa")
        buf.write("\7=\2\2\u01a9\u01a3\3\2\2\2\u01a9\u01a4\3\2\2\2\u01a9")
        buf.write("\u01a5\3\2\2\2\u01a9\u01a6\3\2\2\2\u01a9\u01a7\3\2\2\2")
        buf.write("\u01a9\u01a8\3\2\2\2\u01aa\u01ac\3\2\2\2\u01ab\u019d\3")
        buf.write("\2\2\2\u01ab\u01a1\3\2\2\2\u01acW\3\2\2\2\u01ad\u01ae")
        buf.write("\7\f\2\2\u01ae\u01af\7=\2\2\u01af\u01b0\5X-\2\u01b0\u01b1")
        buf.write("\5h\65\2\u01b1\u01b2\7\f\2\2\u01b2\u01be\3\2\2\2\u01b3")
        buf.write("\u01ba\7\r\2\2\u01b4\u01bb\7\26\2\2\u01b5\u01bb\7\65\2")
        buf.write("\2\u01b6\u01bb\7\63\2\2\u01b7\u01bb\5`\61\2\u01b8\u01bb")
        buf.write("\7\64\2\2\u01b9\u01bb\7=\2\2\u01ba\u01b4\3\2\2\2\u01ba")
        buf.write("\u01b5\3\2\2\2\u01ba\u01b6\3\2\2\2\u01ba\u01b7\3\2\2\2")
        buf.write("\u01ba\u01b8\3\2\2\2\u01ba\u01b9\3\2\2\2\u01bb\u01bc\3")
        buf.write("\2\2\2\u01bc\u01be\7\'\2\2\u01bd\u01ad\3\2\2\2\u01bd\u01b3")
        buf.write("\3\2\2\2\u01beY\3\2\2\2\u01bf\u01c0\7\3\2\2\u01c0\u01c1")
        buf.write("\5\\/\2\u01c1\u01c2\7\13\2\2\u01c2[\3\2\2\2\u01c3\u01c4")
        buf.write("\7=\2\2\u01c4\u01c5\5^\60\2\u01c5\u01c6\5h\65\2\u01c6")
        buf.write("]\3\2\2\2\u01c7\u01c8\7\f\2\2\u01c8\u01c9\7=\2\2\u01c9")
        buf.write("\u01ca\5^\60\2\u01ca\u01cb\5h\65\2\u01cb\u01cc\7\f\2\2")
        buf.write("\u01cc\u01d8\3\2\2\2\u01cd\u01d4\7\r\2\2\u01ce\u01d5\7")
        buf.write("\26\2\2\u01cf\u01d5\7\65\2\2\u01d0\u01d5\7\63\2\2\u01d1")
        buf.write("\u01d5\5`\61\2\u01d2\u01d5\7\64\2\2\u01d3\u01d5\7=\2\2")
        buf.write("\u01d4\u01ce\3\2\2\2\u01d4\u01cf\3\2\2\2\u01d4\u01d0\3")
        buf.write("\2\2\2\u01d4\u01d1\3\2\2\2\u01d4\u01d2\3\2\2\2\u01d4\u01d3")
        buf.write("\3\2\2\2\u01d5\u01d6\3\2\2\2\u01d6\u01d8\7\'\2\2\u01d7")
        buf.write("\u01c7\3\2\2\2\u01d7\u01cd\3\2\2\2\u01d8_\3\2\2\2\u01d9")
        buf.write("\u01da\7\24\2\2\u01da\u01e0\7\t\2\2\u01db\u01e1\7\26\2")
        buf.write("\2\u01dc\u01e1\7\65\2\2\u01dd\u01e1\7\63\2\2\u01de\u01e1")
        buf.write("\5`\61\2\u01df\u01e1\7\64\2\2\u01e0\u01db\3\2\2\2\u01e0")
        buf.write("\u01dc\3\2\2\2\u01e0\u01dd\3\2\2\2\u01e0\u01de\3\2\2\2")
        buf.write("\u01e0\u01df\3\2\2\2\u01e1\u01e2\3\2\2\2\u01e2\u01e3\7")
        buf.write("\f\2\2\u01e3\u01e4\7\67\2\2\u01e4\u01e5\7\n\2\2\u01e5")
        buf.write("a\3\2\2\2\u01e6\u01e7\7\24\2\2\u01e7\u01e8\7\5\2\2\u01e8")
        buf.write("\u01e9\5d\63\2\u01e9\u01ea\7\6\2\2\u01eac\3\2\2\2\u01eb")
        buf.write("\u01ee\5f\64\2\u01ec\u01ee\3\2\2\2\u01ed\u01eb\3\2\2\2")
        buf.write("\u01ed\u01ec\3\2\2\2\u01eee\3\2\2\2\u01ef\u01f0\5h\65")
        buf.write("\2\u01f0\u01f1\7\f\2\2\u01f1\u01f2\5f\64\2\u01f2\u01f5")
        buf.write("\3\2\2\2\u01f3\u01f5\5h\65\2\u01f4\u01ef\3\2\2\2\u01f4")
        buf.write("\u01f3\3\2\2\2\u01f5g\3\2\2\2\u01f6\u01f7\5j\66\2\u01f7")
        buf.write("\u01f8\7-\2\2\u01f8\u01f9\5j\66\2\u01f9\u0200\3\2\2\2")
        buf.write("\u01fa\u01fb\5j\66\2\u01fb\u01fc\7.\2\2\u01fc\u01fd\5")
        buf.write("j\66\2\u01fd\u0200\3\2\2\2\u01fe\u0200\5j\66\2\u01ff\u01f6")
        buf.write("\3\2\2\2\u01ff\u01fa\3\2\2\2\u01ff\u01fe\3\2\2\2\u0200")
        buf.write("i\3\2\2\2\u0201\u0202\5l\67\2\u0202\u0203\7+\2\2\u0203")
        buf.write("\u0204\5l\67\2\u0204\u021b\3\2\2\2\u0205\u0206\5l\67\2")
        buf.write("\u0206\u0207\7,\2\2\u0207\u0208\5l\67\2\u0208\u021b\3")
        buf.write("\2\2\2\u0209\u020a\5l\67\2\u020a\u020b\7)\2\2\u020b\u020c")
        buf.write("\5l\67\2\u020c\u021b\3\2\2\2\u020d\u020e\5l\67\2\u020e")
        buf.write("\u020f\7&\2\2\u020f\u0210\5l\67\2\u0210\u021b\3\2\2\2")
        buf.write("\u0211\u0212\5l\67\2\u0212\u0213\7(\2\2\u0213\u0214\5")
        buf.write("l\67\2\u0214\u021b\3\2\2\2\u0215\u0216\5l\67\2\u0216\u0217")
        buf.write("\7*\2\2\u0217\u0218\5l\67\2\u0218\u021b\3\2\2\2\u0219")
        buf.write("\u021b\5l\67\2\u021a\u0201\3\2\2\2\u021a\u0205\3\2\2\2")
        buf.write("\u021a\u0209\3\2\2\2\u021a\u020d\3\2\2\2\u021a\u0211\3")
        buf.write("\2\2\2\u021a\u0215\3\2\2\2\u021a\u0219\3\2\2\2\u021bk")
        buf.write("\3\2\2\2\u021c\u021d\b\67\1\2\u021d\u021e\5n8\2\u021e")
        buf.write("\u0227\3\2\2\2\u021f\u0220\f\5\2\2\u0220\u0221\7$\2\2")
        buf.write("\u0221\u0226\5n8\2\u0222\u0223\f\4\2\2\u0223\u0224\7%")
        buf.write("\2\2\u0224\u0226\5n8\2\u0225\u021f\3\2\2\2\u0225\u0222")
        buf.write("\3\2\2\2\u0226\u0229\3\2\2\2\u0227\u0225\3\2\2\2\u0227")
        buf.write("\u0228\3\2\2\2\u0228m\3\2\2\2\u0229\u0227\3\2\2\2\u022a")
        buf.write("\u022b\b8\1\2\u022b\u022c\5p9\2\u022c\u0235\3\2\2\2\u022d")
        buf.write("\u022e\f\5\2\2\u022e\u022f\7\36\2\2\u022f\u0234\5p9\2")
        buf.write("\u0230\u0231\f\4\2\2\u0231\u0232\7\37\2\2\u0232\u0234")
        buf.write("\5p9\2\u0233\u022d\3\2\2\2\u0233\u0230\3\2\2\2\u0234\u0237")
        buf.write("\3\2\2\2\u0235\u0233\3\2\2\2\u0235\u0236\3\2\2\2\u0236")
        buf.write("o\3\2\2\2\u0237\u0235\3\2\2\2\u0238\u0239\b9\1\2\u0239")
        buf.write("\u023a\5r:\2\u023a\u0246\3\2\2\2\u023b\u023c\f\6\2\2\u023c")
        buf.write("\u023d\7 \2\2\u023d\u0245\5r:\2\u023e\u023f\f\5\2\2\u023f")
        buf.write("\u0240\7!\2\2\u0240\u0245\5r:\2\u0241\u0242\f\4\2\2\u0242")
        buf.write("\u0243\7\"\2\2\u0243\u0245\5r:\2\u0244\u023b\3\2\2\2\u0244")
        buf.write("\u023e\3\2\2\2\u0244\u0241\3\2\2\2\u0245\u0248\3\2\2\2")
        buf.write("\u0246\u0244\3\2\2\2\u0246\u0247\3\2\2\2\u0247q\3\2\2")
        buf.write("\2\u0248\u0246\3\2\2\2\u0249\u024a\7#\2\2\u024a\u024d")
        buf.write("\5r:\2\u024b\u024d\5t;\2\u024c\u0249\3\2\2\2\u024c\u024b")
        buf.write("\3\2\2\2\u024ds\3\2\2\2\u024e\u024f\7\37\2\2\u024f\u0252")
        buf.write("\5t;\2\u0250\u0252\5v<\2\u0251\u024e\3\2\2\2\u0251\u0250")
        buf.write("\3\2\2\2\u0252u\3\2\2\2\u0253\u0254\b<\1\2\u0254\u0255")
        buf.write("\5x=\2\u0255\u025d\3\2\2\2\u0256\u0257\f\4\2\2\u0257\u0258")
        buf.write("\7\t\2\2\u0258\u0259\5h\65\2\u0259\u025a\7\n\2\2\u025a")
        buf.write("\u025c\3\2\2\2\u025b\u0256\3\2\2\2\u025c\u025f\3\2\2\2")
        buf.write("\u025d\u025b\3\2\2\2\u025d\u025e\3\2\2\2\u025ew\3\2\2")
        buf.write("\2\u025f\u025d\3\2\2\2\u0260\u0261\b=\1\2\u0261\u0262")
        buf.write("\5z>\2\u0262\u026f\3\2\2\2\u0263\u0264\f\5\2\2\u0264\u0265")
        buf.write("\7/\2\2\u0265\u026e\7=\2\2\u0266\u0267\f\4\2\2\u0267\u0268")
        buf.write("\7/\2\2\u0268\u0269\7=\2\2\u0269\u026a\7\5\2\2\u026a\u026b")
        buf.write("\5\u0082B\2\u026b\u026c\7\6\2\2\u026c\u026e\3\2\2\2\u026d")
        buf.write("\u0263\3\2\2\2\u026d\u0266\3\2\2\2\u026e\u0271\3\2\2\2")
        buf.write("\u026f\u026d\3\2\2\2\u026f\u0270\3\2\2\2\u0270y\3\2\2")
        buf.write("\2\u0271\u026f\3\2\2\2\u0272\u0273\7=\2\2\u0273\u0274")
        buf.write("\7\61\2\2\u0274\u0275\7>\2\2\u0275\u0276\7\5\2\2\u0276")
        buf.write("\u0277\5\u0082B\2\u0277\u0278\7\6\2\2\u0278\u027e\3\2")
        buf.write("\2\2\u0279\u027a\7=\2\2\u027a\u027b\7\61\2\2\u027b\u027e")
        buf.write("\7>\2\2\u027c\u027e\5|?\2\u027d\u0272\3\2\2\2\u027d\u0279")
        buf.write("\3\2\2\2\u027d\u027c\3\2\2\2\u027e{\3\2\2\2\u027f\u0280")
        buf.write("\7\33\2\2\u0280\u0281\7=\2\2\u0281\u0282\7\5\2\2\u0282")
        buf.write("\u0283\5\u0082B\2\u0283\u0284\7\6\2\2\u0284\u0287\3\2")
        buf.write("\2\2\u0285\u0287\5~@\2\u0286\u027f\3\2\2\2\u0286\u0285")
        buf.write("\3\2\2\2\u0287}\3\2\2\2\u0288\u0293\7\67\2\2\u0289\u0293")
        buf.write("\78\2\2\u028a\u0293\5b\62\2\u028b\u0293\7\66\2\2\u028c")
        buf.write("\u0293\7<\2\2\u028d\u0293\79\2\2\u028e\u0293\7=\2\2\u028f")
        buf.write("\u0293\7\35\2\2\u0290\u0293\7\30\2\2\u0291\u0293\5\u0080")
        buf.write("A\2\u0292\u0288\3\2\2\2\u0292\u0289\3\2\2\2\u0292\u028a")
        buf.write("\3\2\2\2\u0292\u028b\3\2\2\2\u0292\u028c\3\2\2\2\u0292")
        buf.write("\u028d\3\2\2\2\u0292\u028e\3\2\2\2\u0292\u028f\3\2\2\2")
        buf.write("\u0292\u0290\3\2\2\2\u0292\u0291\3\2\2\2\u0293\177\3\2")
        buf.write("\2\2\u0294\u0295\7\5\2\2\u0295\u0296\5h\65\2\u0296\u0297")
        buf.write("\7\6\2\2\u0297\u0081\3\2\2\2\u0298\u029b\5\u0084C\2\u0299")
        buf.write("\u029b\3\2\2\2\u029a\u0298\3\2\2\2\u029a\u0299\3\2\2\2")
        buf.write("\u029b\u0083\3\2\2\2\u029c\u029d\5h\65\2\u029d\u029e\7")
        buf.write("\f\2\2\u029e\u029f\5\u0084C\2\u029f\u02a2\3\2\2\2\u02a0")
        buf.write("\u02a2\5h\65\2\u02a1\u029c\3\2\2\2\u02a1\u02a0\3\2\2\2")
        buf.write("\u02a2\u0085\3\2\2\2\u02a3\u02a4\7=\2\2\u02a4\u02a5\7")
        buf.write("\f\2\2\u02a5\u02a8\5\u0086D\2\u02a6\u02a8\7=\2\2\u02a7")
        buf.write("\u02a3\3\2\2\2\u02a7\u02a6\3\2\2\2\u02a8\u0087\3\2\2\2")
        buf.write("\u02a9\u02aa\t\2\2\2\u02aa\u02ab\7\f\2\2\u02ab\u02ae\5")
        buf.write("\u0088E\2\u02ac\u02ae\t\2\2\2\u02ad\u02a9\3\2\2\2\u02ad")
        buf.write("\u02ac\3\2\2\2\u02ae\u0089\3\2\2\28\u0091\u009b\u00a3")
        buf.write("\u00a9\u00b0\u00c5\u00cc\u00d6\u00de\u00e4\u00f4\u0102")
        buf.write("\u0113\u0119\u0124\u012b\u0138\u013e\u0160\u0169\u016b")
        buf.write("\u017a\u017d\u0194\u0197\u01a9\u01ab\u01ba\u01bd\u01d4")
        buf.write("\u01d7\u01e0\u01ed\u01f4\u01ff\u021a\u0225\u0227\u0233")
        buf.write("\u0235\u0244\u0246\u024c\u0251\u025d\u026d\u026f\u027d")
        buf.write("\u0286\u0292\u029a\u02a1\u02a7\u02ad")
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
    RULE_var_attribute_declare = 35
    RULE_dec_and_init_list1 = 36
    RULE_pair1 = 37
    RULE_const_attribute_declare = 38
    RULE_dec_and_init_list2 = 39
    RULE_pair2 = 40
    RULE_var_declare = 41
    RULE_dec_and_init_list3 = 42
    RULE_pair3 = 43
    RULE_const_declare = 44
    RULE_dec_and_init_list4 = 45
    RULE_pair4 = 46
    RULE_array_type = 47
    RULE_array_literal = 48
    RULE_literal_list = 49
    RULE_literals = 50
    RULE_exp = 51
    RULE_exp0 = 52
    RULE_exp1 = 53
    RULE_exp2 = 54
    RULE_exp3 = 55
    RULE_exp4 = 56
    RULE_exp5 = 57
    RULE_exp6 = 58
    RULE_exp7 = 59
    RULE_exp8 = 60
    RULE_exp9 = 61
    RULE_exp10 = 62
    RULE_exp11 = 63
    RULE_list_exp = 64
    RULE_exps = 65
    RULE_normal_id_list = 66
    RULE_id_list = 67

    ruleNames =  [ "program", "class_declares_list", "class_declare", "extend", 
                   "class_members", "member_list", "members", "member", 
                   "constructor_method", "destructor_method", "method_declare", 
                   "param_list", "parameters", "parameter", "block_statements", 
                   "statements_list", "statements", "statement", "break_statement", 
                   "continue_statement", "return_statement", "exp_value", 
                   "assign_statement", "if_else_statement", "elseif_stmt_list", 
                   "elseif_stmts", "elseif_stmt", "else_stmt", "foreach_statement", 
                   "increment", "lhs", "static_attr_call", "static_method_call", 
                   "instance_attr_call", "instance_method_call", "var_attribute_declare", 
                   "dec_and_init_list1", "pair1", "const_attribute_declare", 
                   "dec_and_init_list2", "pair2", "var_declare", "dec_and_init_list3", 
                   "pair3", "const_declare", "dec_and_init_list4", "pair4", 
                   "array_type", "array_literal", "literal_list", "literals", 
                   "exp", "exp0", "exp1", "exp2", "exp3", "exp4", "exp5", 
                   "exp6", "exp7", "exp8", "exp9", "exp10", "exp11", "list_exp", 
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
            self.state = 136
            self.class_declares_list()
            self.state = 137
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
            self.state = 143
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,0,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 139
                self.class_declare()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 140
                self.class_declare()
                self.state = 141
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
            self.state = 145
            self.match(D96Parser.CLASS)
            self.state = 146
            self.match(D96Parser.NORMAL_ID)
            self.state = 147
            self.extend()
            self.state = 148
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
            self.state = 153
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [D96Parser.COLON]:
                self.enterOuterAlt(localctx, 1)
                self.state = 150
                self.match(D96Parser.COLON)
                self.state = 151
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
            self.state = 155
            self.match(D96Parser.LCB)
            self.state = 156
            self.member_list()
            self.state = 157
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
            self.state = 161
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [D96Parser.VAL, D96Parser.VAR, D96Parser.CONSTRUCTOR, D96Parser.DESTRUCTOR, D96Parser.NORMAL_ID, D96Parser.DOLLAR_ID]:
                self.enterOuterAlt(localctx, 1)
                self.state = 159
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
            self.state = 167
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,3,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 163
                self.member()
                self.state = 164
                self.members()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 166
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

        def var_attribute_declare(self):
            return self.getTypedRuleContext(D96Parser.Var_attribute_declareContext,0)


        def const_attribute_declare(self):
            return self.getTypedRuleContext(D96Parser.Const_attribute_declareContext,0)


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
            self.state = 174
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [D96Parser.VAR]:
                self.enterOuterAlt(localctx, 1)
                self.state = 169
                self.var_attribute_declare()
                pass
            elif token in [D96Parser.VAL]:
                self.enterOuterAlt(localctx, 2)
                self.state = 170
                self.const_attribute_declare()
                pass
            elif token in [D96Parser.CONSTRUCTOR]:
                self.enterOuterAlt(localctx, 3)
                self.state = 171
                self.constructor_method()
                pass
            elif token in [D96Parser.DESTRUCTOR]:
                self.enterOuterAlt(localctx, 4)
                self.state = 172
                self.destructor_method()
                pass
            elif token in [D96Parser.NORMAL_ID, D96Parser.DOLLAR_ID]:
                self.enterOuterAlt(localctx, 5)
                self.state = 173
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
            self.state = 176
            self.match(D96Parser.CONSTRUCTOR)
            self.state = 177
            self.match(D96Parser.LP)
            self.state = 178
            self.param_list()
            self.state = 179
            self.match(D96Parser.RP)
            self.state = 180
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
            self.state = 182
            self.match(D96Parser.DESTRUCTOR)
            self.state = 183
            self.match(D96Parser.LP)
            self.state = 184
            self.match(D96Parser.RP)
            self.state = 185
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
            self.state = 187
            _la = self._input.LA(1)
            if not(_la==D96Parser.NORMAL_ID or _la==D96Parser.DOLLAR_ID):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 188
            self.match(D96Parser.LP)
            self.state = 189
            self.param_list()
            self.state = 190
            self.match(D96Parser.RP)
            self.state = 191
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
            self.state = 195
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [D96Parser.NORMAL_ID]:
                self.enterOuterAlt(localctx, 1)
                self.state = 193
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
            self.state = 202
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,6,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 197
                self.parameter()
                self.state = 198
                self.match(D96Parser.SEMI)
                self.state = 199
                self.parameters()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 201
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
            self.state = 204
            self.normal_id_list()
            self.state = 205
            self.match(D96Parser.COLON)
            self.state = 212
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [D96Parser.BOOLEAN]:
                self.state = 206
                self.match(D96Parser.BOOLEAN)
                pass
            elif token in [D96Parser.INT_TYPE]:
                self.state = 207
                self.match(D96Parser.INT_TYPE)
                pass
            elif token in [D96Parser.FLOAT_TYPE]:
                self.state = 208
                self.match(D96Parser.FLOAT_TYPE)
                pass
            elif token in [D96Parser.ARRAY]:
                self.state = 209
                self.array_type()
                pass
            elif token in [D96Parser.STRING]:
                self.state = 210
                self.match(D96Parser.STRING)
                pass
            elif token in [D96Parser.NORMAL_ID]:
                self.state = 211
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
            self.state = 214
            self.match(D96Parser.LCB)
            self.state = 215
            self.statements_list()
            self.state = 216
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
            self.state = 220
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [D96Parser.VAL, D96Parser.VAR, D96Parser.LP, D96Parser.BREAK, D96Parser.CONTINUE, D96Parser.IF, D96Parser.FOREACH, D96Parser.ARRAY, D96Parser.RETURN, D96Parser.NULL, D96Parser.NEW, D96Parser.SELF, D96Parser.BOOL_LITERAL, D96Parser.ARRAY_SIZE, D96Parser.INTEGER_LITERAL, D96Parser.STRING_LITERAL, D96Parser.REAL_LITERAL, D96Parser.NORMAL_ID]:
                self.enterOuterAlt(localctx, 1)
                self.state = 218
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
            self.state = 226
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,9,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 222
                self.statement()
                self.state = 223
                self.statements()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 225
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


        def const_declare(self):
            return self.getTypedRuleContext(D96Parser.Const_declareContext,0)


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
            self.state = 242
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,10,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 228
                self.assign_statement()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 229
                self.var_declare()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 230
                self.const_declare()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 231
                self.break_statement()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 232
                self.continue_statement()
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 233
                self.return_statement()
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 234
                self.static_method_call()
                self.state = 235
                self.match(D96Parser.SEMI)
                pass

            elif la_ == 8:
                self.enterOuterAlt(localctx, 8)
                self.state = 237
                self.instance_method_call()
                self.state = 238
                self.match(D96Parser.SEMI)
                pass

            elif la_ == 9:
                self.enterOuterAlt(localctx, 9)
                self.state = 240
                self.if_else_statement()
                pass

            elif la_ == 10:
                self.enterOuterAlt(localctx, 10)
                self.state = 241
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
            self.state = 244
            self.match(D96Parser.BREAK)
            self.state = 245
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
            self.state = 247
            self.match(D96Parser.CONTINUE)
            self.state = 248
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
            self.state = 250
            self.match(D96Parser.RETURN)
            self.state = 251
            self.exp_value()
            self.state = 252
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
            self.state = 256
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [D96Parser.LP, D96Parser.ARRAY, D96Parser.NULL, D96Parser.NEW, D96Parser.SELF, D96Parser.SUB, D96Parser.NOT, D96Parser.BOOL_LITERAL, D96Parser.ARRAY_SIZE, D96Parser.INTEGER_LITERAL, D96Parser.STRING_LITERAL, D96Parser.REAL_LITERAL, D96Parser.NORMAL_ID]:
                self.enterOuterAlt(localctx, 1)
                self.state = 254
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
            self.state = 258
            self.lhs()
            self.state = 259
            self.match(D96Parser.ASSIGN)
            self.state = 260
            self.exp()
            self.state = 261
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
            self.state = 263
            self.match(D96Parser.IF)
            self.state = 264
            self.match(D96Parser.LP)
            self.state = 265
            self.exp()
            self.state = 266
            self.match(D96Parser.RP)
            self.state = 267
            self.block_statements()
            self.state = 268
            self.elseif_stmt_list()
            self.state = 269
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
            self.state = 273
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [D96Parser.ELSEIF]:
                self.enterOuterAlt(localctx, 1)
                self.state = 271
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
            self.state = 279
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,13,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 275
                self.elseif_stmt()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 276
                self.elseif_stmt()
                self.state = 277
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
            self.state = 281
            self.match(D96Parser.ELSEIF)
            self.state = 282
            self.match(D96Parser.LP)
            self.state = 283
            self.exp()
            self.state = 284
            self.match(D96Parser.RP)
            self.state = 285
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
            self.state = 290
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [D96Parser.ELSE]:
                self.enterOuterAlt(localctx, 1)
                self.state = 287
                self.match(D96Parser.ELSE)
                self.state = 288
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
            self.state = 292
            self.match(D96Parser.FOREACH)
            self.state = 293
            self.match(D96Parser.LP)
            self.state = 297
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,15,self._ctx)
            if la_ == 1:
                self.state = 294
                self.match(D96Parser.NORMAL_ID)
                pass

            elif la_ == 2:
                self.state = 295
                self.static_attr_call()
                pass

            elif la_ == 3:
                self.state = 296
                self.instance_attr_call()
                pass


            self.state = 299
            self.match(D96Parser.IN)
            self.state = 300
            self.exp()
            self.state = 301
            self.match(D96Parser.DOTDOT)
            self.state = 302
            self.exp()
            self.state = 303
            self.increment()
            self.state = 304
            self.match(D96Parser.RP)
            self.state = 305
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
            self.state = 310
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [D96Parser.BY]:
                self.enterOuterAlt(localctx, 1)
                self.state = 307
                self.match(D96Parser.BY)
                self.state = 308
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
            self.state = 316
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,17,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 312
                self.match(D96Parser.NORMAL_ID)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 313
                self.exp6(0)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 314
                self.static_attr_call()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 315
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
            self.state = 318
            self.match(D96Parser.NORMAL_ID)
            self.state = 319
            self.match(D96Parser.SCOPE)
            self.state = 320
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
            self.state = 322
            self.match(D96Parser.NORMAL_ID)
            self.state = 323
            self.match(D96Parser.SCOPE)
            self.state = 324
            self.match(D96Parser.DOLLAR_ID)
            self.state = 325
            self.match(D96Parser.LP)
            self.state = 326
            self.list_exp()
            self.state = 327
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
            self.state = 329
            self.exp7(0)
            self.state = 330
            self.match(D96Parser.DOT)
            self.state = 331
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
            self.state = 333
            self.exp7(0)
            self.state = 334
            self.match(D96Parser.DOT)
            self.state = 335
            self.match(D96Parser.NORMAL_ID)
            self.state = 336
            self.match(D96Parser.LP)
            self.state = 337
            self.list_exp()
            self.state = 338
            self.match(D96Parser.RP)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Var_attribute_declareContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def VAR(self):
            return self.getToken(D96Parser.VAR, 0)

        def dec_and_init_list1(self):
            return self.getTypedRuleContext(D96Parser.Dec_and_init_list1Context,0)


        def SEMI(self):
            return self.getToken(D96Parser.SEMI, 0)

        def getRuleIndex(self):
            return D96Parser.RULE_var_attribute_declare




    def var_attribute_declare(self):

        localctx = D96Parser.Var_attribute_declareContext(self, self._ctx, self.state)
        self.enterRule(localctx, 70, self.RULE_var_attribute_declare)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 340
            self.match(D96Parser.VAR)
            self.state = 341
            self.dec_and_init_list1()
            self.state = 342
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
            self.state = 361
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,20,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 344
                _la = self._input.LA(1)
                if not(_la==D96Parser.NORMAL_ID or _la==D96Parser.DOLLAR_ID):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 345
                self.pair1()
                self.state = 346
                self.exp()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 350
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,18,self._ctx)
                if la_ == 1:
                    self.state = 348
                    self.id_list()
                    pass

                elif la_ == 2:
                    self.state = 349
                    self.normal_id_list()
                    pass


                self.state = 352
                self.match(D96Parser.COLON)
                self.state = 359
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [D96Parser.BOOLEAN]:
                    self.state = 353
                    self.match(D96Parser.BOOLEAN)
                    pass
                elif token in [D96Parser.INT_TYPE]:
                    self.state = 354
                    self.match(D96Parser.INT_TYPE)
                    pass
                elif token in [D96Parser.FLOAT_TYPE]:
                    self.state = 355
                    self.match(D96Parser.FLOAT_TYPE)
                    pass
                elif token in [D96Parser.ARRAY]:
                    self.state = 356
                    self.array_type()
                    pass
                elif token in [D96Parser.STRING]:
                    self.state = 357
                    self.match(D96Parser.STRING)
                    pass
                elif token in [D96Parser.NORMAL_ID]:
                    self.state = 358
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
            self.state = 379
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [D96Parser.COMMA]:
                self.enterOuterAlt(localctx, 1)
                self.state = 363
                self.match(D96Parser.COMMA)
                self.state = 364
                _la = self._input.LA(1)
                if not(_la==D96Parser.NORMAL_ID or _la==D96Parser.DOLLAR_ID):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 365
                self.pair1()
                self.state = 366
                self.exp()
                self.state = 367
                self.match(D96Parser.COMMA)
                pass
            elif token in [D96Parser.COLON]:
                self.enterOuterAlt(localctx, 2)
                self.state = 369
                self.match(D96Parser.COLON)
                self.state = 376
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [D96Parser.BOOLEAN]:
                    self.state = 370
                    self.match(D96Parser.BOOLEAN)
                    pass
                elif token in [D96Parser.INT_TYPE]:
                    self.state = 371
                    self.match(D96Parser.INT_TYPE)
                    pass
                elif token in [D96Parser.FLOAT_TYPE]:
                    self.state = 372
                    self.match(D96Parser.FLOAT_TYPE)
                    pass
                elif token in [D96Parser.ARRAY]:
                    self.state = 373
                    self.array_type()
                    pass
                elif token in [D96Parser.STRING]:
                    self.state = 374
                    self.match(D96Parser.STRING)
                    pass
                elif token in [D96Parser.NORMAL_ID]:
                    self.state = 375
                    self.match(D96Parser.NORMAL_ID)
                    pass
                else:
                    raise NoViableAltException(self)

                self.state = 378
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


    class Const_attribute_declareContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def VAL(self):
            return self.getToken(D96Parser.VAL, 0)

        def dec_and_init_list2(self):
            return self.getTypedRuleContext(D96Parser.Dec_and_init_list2Context,0)


        def SEMI(self):
            return self.getToken(D96Parser.SEMI, 0)

        def getRuleIndex(self):
            return D96Parser.RULE_const_attribute_declare




    def const_attribute_declare(self):

        localctx = D96Parser.Const_attribute_declareContext(self, self._ctx, self.state)
        self.enterRule(localctx, 76, self.RULE_const_attribute_declare)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 381
            self.match(D96Parser.VAL)
            self.state = 382
            self.dec_and_init_list2()
            self.state = 383
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

        def pair2(self):
            return self.getTypedRuleContext(D96Parser.Pair2Context,0)


        def exp(self):
            return self.getTypedRuleContext(D96Parser.ExpContext,0)


        def NORMAL_ID(self):
            return self.getToken(D96Parser.NORMAL_ID, 0)

        def DOLLAR_ID(self):
            return self.getToken(D96Parser.DOLLAR_ID, 0)

        def getRuleIndex(self):
            return D96Parser.RULE_dec_and_init_list2




    def dec_and_init_list2(self):

        localctx = D96Parser.Dec_and_init_list2Context(self, self._ctx, self.state)
        self.enterRule(localctx, 78, self.RULE_dec_and_init_list2)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 385
            _la = self._input.LA(1)
            if not(_la==D96Parser.NORMAL_ID or _la==D96Parser.DOLLAR_ID):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 386
            self.pair2()
            self.state = 387
            self.exp()
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

        def pair2(self):
            return self.getTypedRuleContext(D96Parser.Pair2Context,0)


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
            return D96Parser.RULE_pair2




    def pair2(self):

        localctx = D96Parser.Pair2Context(self, self._ctx, self.state)
        self.enterRule(localctx, 80, self.RULE_pair2)
        self._la = 0 # Token type
        try:
            self.state = 405
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [D96Parser.COMMA]:
                self.enterOuterAlt(localctx, 1)
                self.state = 389
                self.match(D96Parser.COMMA)
                self.state = 390
                _la = self._input.LA(1)
                if not(_la==D96Parser.NORMAL_ID or _la==D96Parser.DOLLAR_ID):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 391
                self.pair2()
                self.state = 392
                self.exp()
                self.state = 393
                self.match(D96Parser.COMMA)
                pass
            elif token in [D96Parser.COLON]:
                self.enterOuterAlt(localctx, 2)
                self.state = 395
                self.match(D96Parser.COLON)
                self.state = 402
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [D96Parser.BOOLEAN]:
                    self.state = 396
                    self.match(D96Parser.BOOLEAN)
                    pass
                elif token in [D96Parser.INT_TYPE]:
                    self.state = 397
                    self.match(D96Parser.INT_TYPE)
                    pass
                elif token in [D96Parser.FLOAT_TYPE]:
                    self.state = 398
                    self.match(D96Parser.FLOAT_TYPE)
                    pass
                elif token in [D96Parser.ARRAY]:
                    self.state = 399
                    self.array_type()
                    pass
                elif token in [D96Parser.STRING]:
                    self.state = 400
                    self.match(D96Parser.STRING)
                    pass
                elif token in [D96Parser.NORMAL_ID]:
                    self.state = 401
                    self.match(D96Parser.NORMAL_ID)
                    pass
                else:
                    raise NoViableAltException(self)

                self.state = 404
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

        def VAR(self):
            return self.getToken(D96Parser.VAR, 0)

        def dec_and_init_list3(self):
            return self.getTypedRuleContext(D96Parser.Dec_and_init_list3Context,0)


        def SEMI(self):
            return self.getToken(D96Parser.SEMI, 0)

        def getRuleIndex(self):
            return D96Parser.RULE_var_declare




    def var_declare(self):

        localctx = D96Parser.Var_declareContext(self, self._ctx, self.state)
        self.enterRule(localctx, 82, self.RULE_var_declare)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 407
            self.match(D96Parser.VAR)
            self.state = 408
            self.dec_and_init_list3()
            self.state = 409
            self.match(D96Parser.SEMI)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Dec_and_init_list3Context(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NORMAL_ID(self):
            return self.getToken(D96Parser.NORMAL_ID, 0)

        def pair3(self):
            return self.getTypedRuleContext(D96Parser.Pair3Context,0)


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
            return D96Parser.RULE_dec_and_init_list3




    def dec_and_init_list3(self):

        localctx = D96Parser.Dec_and_init_list3Context(self, self._ctx, self.state)
        self.enterRule(localctx, 84, self.RULE_dec_and_init_list3)
        try:
            self.state = 425
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,26,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 411
                self.match(D96Parser.NORMAL_ID)
                self.state = 412
                self.pair3()
                self.state = 413
                self.exp()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 415
                self.normal_id_list()
                self.state = 416
                self.match(D96Parser.COLON)
                self.state = 423
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [D96Parser.BOOLEAN]:
                    self.state = 417
                    self.match(D96Parser.BOOLEAN)
                    pass
                elif token in [D96Parser.INT_TYPE]:
                    self.state = 418
                    self.match(D96Parser.INT_TYPE)
                    pass
                elif token in [D96Parser.FLOAT_TYPE]:
                    self.state = 419
                    self.match(D96Parser.FLOAT_TYPE)
                    pass
                elif token in [D96Parser.ARRAY]:
                    self.state = 420
                    self.array_type()
                    pass
                elif token in [D96Parser.STRING]:
                    self.state = 421
                    self.match(D96Parser.STRING)
                    pass
                elif token in [D96Parser.NORMAL_ID]:
                    self.state = 422
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


    class Pair3Context(ParserRuleContext):

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

        def pair3(self):
            return self.getTypedRuleContext(D96Parser.Pair3Context,0)


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
            return D96Parser.RULE_pair3




    def pair3(self):

        localctx = D96Parser.Pair3Context(self, self._ctx, self.state)
        self.enterRule(localctx, 86, self.RULE_pair3)
        try:
            self.state = 443
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [D96Parser.COMMA]:
                self.enterOuterAlt(localctx, 1)
                self.state = 427
                self.match(D96Parser.COMMA)
                self.state = 428
                self.match(D96Parser.NORMAL_ID)
                self.state = 429
                self.pair3()
                self.state = 430
                self.exp()
                self.state = 431
                self.match(D96Parser.COMMA)
                pass
            elif token in [D96Parser.COLON]:
                self.enterOuterAlt(localctx, 2)
                self.state = 433
                self.match(D96Parser.COLON)
                self.state = 440
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [D96Parser.BOOLEAN]:
                    self.state = 434
                    self.match(D96Parser.BOOLEAN)
                    pass
                elif token in [D96Parser.INT_TYPE]:
                    self.state = 435
                    self.match(D96Parser.INT_TYPE)
                    pass
                elif token in [D96Parser.FLOAT_TYPE]:
                    self.state = 436
                    self.match(D96Parser.FLOAT_TYPE)
                    pass
                elif token in [D96Parser.ARRAY]:
                    self.state = 437
                    self.array_type()
                    pass
                elif token in [D96Parser.STRING]:
                    self.state = 438
                    self.match(D96Parser.STRING)
                    pass
                elif token in [D96Parser.NORMAL_ID]:
                    self.state = 439
                    self.match(D96Parser.NORMAL_ID)
                    pass
                else:
                    raise NoViableAltException(self)

                self.state = 442
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


    class Const_declareContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def VAL(self):
            return self.getToken(D96Parser.VAL, 0)

        def dec_and_init_list4(self):
            return self.getTypedRuleContext(D96Parser.Dec_and_init_list4Context,0)


        def SEMI(self):
            return self.getToken(D96Parser.SEMI, 0)

        def getRuleIndex(self):
            return D96Parser.RULE_const_declare




    def const_declare(self):

        localctx = D96Parser.Const_declareContext(self, self._ctx, self.state)
        self.enterRule(localctx, 88, self.RULE_const_declare)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 445
            self.match(D96Parser.VAL)
            self.state = 446
            self.dec_and_init_list4()
            self.state = 447
            self.match(D96Parser.SEMI)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Dec_and_init_list4Context(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NORMAL_ID(self):
            return self.getToken(D96Parser.NORMAL_ID, 0)

        def pair4(self):
            return self.getTypedRuleContext(D96Parser.Pair4Context,0)


        def exp(self):
            return self.getTypedRuleContext(D96Parser.ExpContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_dec_and_init_list4




    def dec_and_init_list4(self):

        localctx = D96Parser.Dec_and_init_list4Context(self, self._ctx, self.state)
        self.enterRule(localctx, 90, self.RULE_dec_and_init_list4)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 449
            self.match(D96Parser.NORMAL_ID)
            self.state = 450
            self.pair4()
            self.state = 451
            self.exp()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Pair4Context(ParserRuleContext):

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

        def pair4(self):
            return self.getTypedRuleContext(D96Parser.Pair4Context,0)


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
            return D96Parser.RULE_pair4




    def pair4(self):

        localctx = D96Parser.Pair4Context(self, self._ctx, self.state)
        self.enterRule(localctx, 92, self.RULE_pair4)
        try:
            self.state = 469
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [D96Parser.COMMA]:
                self.enterOuterAlt(localctx, 1)
                self.state = 453
                self.match(D96Parser.COMMA)
                self.state = 454
                self.match(D96Parser.NORMAL_ID)
                self.state = 455
                self.pair4()
                self.state = 456
                self.exp()
                self.state = 457
                self.match(D96Parser.COMMA)
                pass
            elif token in [D96Parser.COLON]:
                self.enterOuterAlt(localctx, 2)
                self.state = 459
                self.match(D96Parser.COLON)
                self.state = 466
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [D96Parser.BOOLEAN]:
                    self.state = 460
                    self.match(D96Parser.BOOLEAN)
                    pass
                elif token in [D96Parser.INT_TYPE]:
                    self.state = 461
                    self.match(D96Parser.INT_TYPE)
                    pass
                elif token in [D96Parser.FLOAT_TYPE]:
                    self.state = 462
                    self.match(D96Parser.FLOAT_TYPE)
                    pass
                elif token in [D96Parser.ARRAY]:
                    self.state = 463
                    self.array_type()
                    pass
                elif token in [D96Parser.STRING]:
                    self.state = 464
                    self.match(D96Parser.STRING)
                    pass
                elif token in [D96Parser.NORMAL_ID]:
                    self.state = 465
                    self.match(D96Parser.NORMAL_ID)
                    pass
                else:
                    raise NoViableAltException(self)

                self.state = 468
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
        self.enterRule(localctx, 94, self.RULE_array_type)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 471
            self.match(D96Parser.ARRAY)
            self.state = 472
            self.match(D96Parser.LSB)
            self.state = 478
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [D96Parser.BOOLEAN]:
                self.state = 473
                self.match(D96Parser.BOOLEAN)
                pass
            elif token in [D96Parser.INT_TYPE]:
                self.state = 474
                self.match(D96Parser.INT_TYPE)
                pass
            elif token in [D96Parser.FLOAT_TYPE]:
                self.state = 475
                self.match(D96Parser.FLOAT_TYPE)
                pass
            elif token in [D96Parser.ARRAY]:
                self.state = 476
                self.array_type()
                pass
            elif token in [D96Parser.STRING]:
                self.state = 477
                self.match(D96Parser.STRING)
                pass
            else:
                raise NoViableAltException(self)

            self.state = 480
            self.match(D96Parser.COMMA)
            self.state = 481
            self.match(D96Parser.ARRAY_SIZE)
            self.state = 482
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

        def literal_list(self):
            return self.getTypedRuleContext(D96Parser.Literal_listContext,0)


        def RP(self):
            return self.getToken(D96Parser.RP, 0)

        def getRuleIndex(self):
            return D96Parser.RULE_array_literal




    def array_literal(self):

        localctx = D96Parser.Array_literalContext(self, self._ctx, self.state)
        self.enterRule(localctx, 96, self.RULE_array_literal)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 484
            self.match(D96Parser.ARRAY)
            self.state = 485
            self.match(D96Parser.LP)
            self.state = 486
            self.literal_list()
            self.state = 487
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

        def literals(self):
            return self.getTypedRuleContext(D96Parser.LiteralsContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_literal_list




    def literal_list(self):

        localctx = D96Parser.Literal_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 98, self.RULE_literal_list)
        try:
            self.state = 491
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [D96Parser.LP, D96Parser.ARRAY, D96Parser.NULL, D96Parser.NEW, D96Parser.SELF, D96Parser.SUB, D96Parser.NOT, D96Parser.BOOL_LITERAL, D96Parser.ARRAY_SIZE, D96Parser.INTEGER_LITERAL, D96Parser.STRING_LITERAL, D96Parser.REAL_LITERAL, D96Parser.NORMAL_ID]:
                self.enterOuterAlt(localctx, 1)
                self.state = 489
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




    def literals(self):

        localctx = D96Parser.LiteralsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 100, self.RULE_literals)
        try:
            self.state = 498
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,33,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 493
                self.exp()
                self.state = 494
                self.match(D96Parser.COMMA)
                self.state = 495
                self.literals()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 497
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
        self.enterRule(localctx, 102, self.RULE_exp)
        try:
            self.state = 509
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,34,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 500
                self.exp0()
                self.state = 501
                self.match(D96Parser.EQUAL_STR)
                self.state = 502
                self.exp0()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 504
                self.exp0()
                self.state = 505
                self.match(D96Parser.ADD_STR)
                self.state = 506
                self.exp0()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 508
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
        self.enterRule(localctx, 104, self.RULE_exp0)
        try:
            self.state = 536
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,35,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 511
                self.exp1(0)
                self.state = 512
                self.match(D96Parser.LT)
                self.state = 513
                self.exp1(0)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 515
                self.exp1(0)
                self.state = 516
                self.match(D96Parser.LTE)
                self.state = 517
                self.exp1(0)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 519
                self.exp1(0)
                self.state = 520
                self.match(D96Parser.GT)
                self.state = 521
                self.exp1(0)
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 523
                self.exp1(0)
                self.state = 524
                self.match(D96Parser.EQUAL)
                self.state = 525
                self.exp1(0)
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 527
                self.exp1(0)
                self.state = 528
                self.match(D96Parser.NOTEQUAL)
                self.state = 529
                self.exp1(0)
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 531
                self.exp1(0)
                self.state = 532
                self.match(D96Parser.GTE)
                self.state = 533
                self.exp1(0)
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 535
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
        _startState = 106
        self.enterRecursionRule(localctx, 106, self.RULE_exp1, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 539
            self.exp2(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 549
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,37,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 547
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,36,self._ctx)
                    if la_ == 1:
                        localctx = D96Parser.Exp1Context(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_exp1)
                        self.state = 541
                        if not self.precpred(self._ctx, 3):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 3)")
                        self.state = 542
                        self.match(D96Parser.AND)
                        self.state = 543
                        self.exp2(0)
                        pass

                    elif la_ == 2:
                        localctx = D96Parser.Exp1Context(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_exp1)
                        self.state = 544
                        if not self.precpred(self._ctx, 2):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                        self.state = 545
                        self.match(D96Parser.OR)
                        self.state = 546
                        self.exp2(0)
                        pass

             
                self.state = 551
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,37,self._ctx)

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
        _startState = 108
        self.enterRecursionRule(localctx, 108, self.RULE_exp2, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 553
            self.exp3(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 563
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,39,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 561
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,38,self._ctx)
                    if la_ == 1:
                        localctx = D96Parser.Exp2Context(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_exp2)
                        self.state = 555
                        if not self.precpred(self._ctx, 3):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 3)")
                        self.state = 556
                        self.match(D96Parser.ADD)
                        self.state = 557
                        self.exp3(0)
                        pass

                    elif la_ == 2:
                        localctx = D96Parser.Exp2Context(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_exp2)
                        self.state = 558
                        if not self.precpred(self._ctx, 2):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                        self.state = 559
                        self.match(D96Parser.SUB)
                        self.state = 560
                        self.exp3(0)
                        pass

             
                self.state = 565
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,39,self._ctx)

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
        _startState = 110
        self.enterRecursionRule(localctx, 110, self.RULE_exp3, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 567
            self.exp4()
            self._ctx.stop = self._input.LT(-1)
            self.state = 580
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,41,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 578
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,40,self._ctx)
                    if la_ == 1:
                        localctx = D96Parser.Exp3Context(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_exp3)
                        self.state = 569
                        if not self.precpred(self._ctx, 4):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 4)")
                        self.state = 570
                        self.match(D96Parser.MUL)
                        self.state = 571
                        self.exp4()
                        pass

                    elif la_ == 2:
                        localctx = D96Parser.Exp3Context(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_exp3)
                        self.state = 572
                        if not self.precpred(self._ctx, 3):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 3)")
                        self.state = 573
                        self.match(D96Parser.DIV)
                        self.state = 574
                        self.exp4()
                        pass

                    elif la_ == 3:
                        localctx = D96Parser.Exp3Context(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_exp3)
                        self.state = 575
                        if not self.precpred(self._ctx, 2):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                        self.state = 576
                        self.match(D96Parser.MOD)
                        self.state = 577
                        self.exp4()
                        pass

             
                self.state = 582
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,41,self._ctx)

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
        self.enterRule(localctx, 112, self.RULE_exp4)
        try:
            self.state = 586
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [D96Parser.NOT]:
                self.enterOuterAlt(localctx, 1)
                self.state = 583
                self.match(D96Parser.NOT)
                self.state = 584
                self.exp4()
                pass
            elif token in [D96Parser.LP, D96Parser.ARRAY, D96Parser.NULL, D96Parser.NEW, D96Parser.SELF, D96Parser.SUB, D96Parser.BOOL_LITERAL, D96Parser.ARRAY_SIZE, D96Parser.INTEGER_LITERAL, D96Parser.STRING_LITERAL, D96Parser.REAL_LITERAL, D96Parser.NORMAL_ID]:
                self.enterOuterAlt(localctx, 2)
                self.state = 585
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
        self.enterRule(localctx, 114, self.RULE_exp5)
        try:
            self.state = 591
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [D96Parser.SUB]:
                self.enterOuterAlt(localctx, 1)
                self.state = 588
                self.match(D96Parser.SUB)
                self.state = 589
                self.exp5()
                pass
            elif token in [D96Parser.LP, D96Parser.ARRAY, D96Parser.NULL, D96Parser.NEW, D96Parser.SELF, D96Parser.BOOL_LITERAL, D96Parser.ARRAY_SIZE, D96Parser.INTEGER_LITERAL, D96Parser.STRING_LITERAL, D96Parser.REAL_LITERAL, D96Parser.NORMAL_ID]:
                self.enterOuterAlt(localctx, 2)
                self.state = 590
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


        def LSB(self):
            return self.getToken(D96Parser.LSB, 0)

        def exp(self):
            return self.getTypedRuleContext(D96Parser.ExpContext,0)


        def RSB(self):
            return self.getToken(D96Parser.RSB, 0)

        def getRuleIndex(self):
            return D96Parser.RULE_exp6



    def exp6(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = D96Parser.Exp6Context(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 116
        self.enterRecursionRule(localctx, 116, self.RULE_exp6, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 594
            self.exp7(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 603
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,44,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = D96Parser.Exp6Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_exp6)
                    self.state = 596
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 597
                    self.match(D96Parser.LSB)
                    self.state = 598
                    self.exp()
                    self.state = 599
                    self.match(D96Parser.RSB) 
                self.state = 605
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,44,self._ctx)

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
        _startState = 118
        self.enterRecursionRule(localctx, 118, self.RULE_exp7, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 607
            self.exp8()
            self._ctx.stop = self._input.LT(-1)
            self.state = 621
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,46,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 619
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,45,self._ctx)
                    if la_ == 1:
                        localctx = D96Parser.Exp7Context(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_exp7)
                        self.state = 609
                        if not self.precpred(self._ctx, 3):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 3)")
                        self.state = 610
                        self.match(D96Parser.DOT)
                        self.state = 611
                        self.match(D96Parser.NORMAL_ID)
                        pass

                    elif la_ == 2:
                        localctx = D96Parser.Exp7Context(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_exp7)
                        self.state = 612
                        if not self.precpred(self._ctx, 2):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                        self.state = 613
                        self.match(D96Parser.DOT)
                        self.state = 614
                        self.match(D96Parser.NORMAL_ID)
                        self.state = 615
                        self.match(D96Parser.LP)
                        self.state = 616
                        self.list_exp()
                        self.state = 617
                        self.match(D96Parser.RP)
                        pass

             
                self.state = 623
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,46,self._ctx)

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
        self.enterRule(localctx, 120, self.RULE_exp8)
        try:
            self.state = 635
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,47,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 624
                self.match(D96Parser.NORMAL_ID)
                self.state = 625
                self.match(D96Parser.SCOPE)
                self.state = 626
                self.match(D96Parser.DOLLAR_ID)
                self.state = 627
                self.match(D96Parser.LP)
                self.state = 628
                self.list_exp()
                self.state = 629
                self.match(D96Parser.RP)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 631
                self.match(D96Parser.NORMAL_ID)
                self.state = 632
                self.match(D96Parser.SCOPE)
                self.state = 633
                self.match(D96Parser.DOLLAR_ID)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 634
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
        self.enterRule(localctx, 122, self.RULE_exp9)
        try:
            self.state = 644
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [D96Parser.NEW]:
                self.enterOuterAlt(localctx, 1)
                self.state = 637
                self.match(D96Parser.NEW)
                self.state = 638
                self.match(D96Parser.NORMAL_ID)
                self.state = 639
                self.match(D96Parser.LP)
                self.state = 640
                self.list_exp()
                self.state = 641
                self.match(D96Parser.RP)
                pass
            elif token in [D96Parser.LP, D96Parser.ARRAY, D96Parser.NULL, D96Parser.SELF, D96Parser.BOOL_LITERAL, D96Parser.ARRAY_SIZE, D96Parser.INTEGER_LITERAL, D96Parser.STRING_LITERAL, D96Parser.REAL_LITERAL, D96Parser.NORMAL_ID]:
                self.enterOuterAlt(localctx, 2)
                self.state = 643
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
        self.enterRule(localctx, 124, self.RULE_exp10)
        try:
            self.state = 656
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [D96Parser.ARRAY_SIZE]:
                self.enterOuterAlt(localctx, 1)
                self.state = 646
                self.match(D96Parser.ARRAY_SIZE)
                pass
            elif token in [D96Parser.INTEGER_LITERAL]:
                self.enterOuterAlt(localctx, 2)
                self.state = 647
                self.match(D96Parser.INTEGER_LITERAL)
                pass
            elif token in [D96Parser.ARRAY]:
                self.enterOuterAlt(localctx, 3)
                self.state = 648
                self.array_literal()
                pass
            elif token in [D96Parser.BOOL_LITERAL]:
                self.enterOuterAlt(localctx, 4)
                self.state = 649
                self.match(D96Parser.BOOL_LITERAL)
                pass
            elif token in [D96Parser.REAL_LITERAL]:
                self.enterOuterAlt(localctx, 5)
                self.state = 650
                self.match(D96Parser.REAL_LITERAL)
                pass
            elif token in [D96Parser.STRING_LITERAL]:
                self.enterOuterAlt(localctx, 6)
                self.state = 651
                self.match(D96Parser.STRING_LITERAL)
                pass
            elif token in [D96Parser.NORMAL_ID]:
                self.enterOuterAlt(localctx, 7)
                self.state = 652
                self.match(D96Parser.NORMAL_ID)
                pass
            elif token in [D96Parser.SELF]:
                self.enterOuterAlt(localctx, 8)
                self.state = 653
                self.match(D96Parser.SELF)
                pass
            elif token in [D96Parser.NULL]:
                self.enterOuterAlt(localctx, 9)
                self.state = 654
                self.match(D96Parser.NULL)
                pass
            elif token in [D96Parser.LP]:
                self.enterOuterAlt(localctx, 10)
                self.state = 655
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
        self.enterRule(localctx, 126, self.RULE_exp11)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 658
            self.match(D96Parser.LP)
            self.state = 659
            self.exp()
            self.state = 660
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
        self.enterRule(localctx, 128, self.RULE_list_exp)
        try:
            self.state = 664
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [D96Parser.LP, D96Parser.ARRAY, D96Parser.NULL, D96Parser.NEW, D96Parser.SELF, D96Parser.SUB, D96Parser.NOT, D96Parser.BOOL_LITERAL, D96Parser.ARRAY_SIZE, D96Parser.INTEGER_LITERAL, D96Parser.STRING_LITERAL, D96Parser.REAL_LITERAL, D96Parser.NORMAL_ID]:
                self.enterOuterAlt(localctx, 1)
                self.state = 662
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
        self.enterRule(localctx, 130, self.RULE_exps)
        try:
            self.state = 671
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,51,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 666
                self.exp()
                self.state = 667
                self.match(D96Parser.COMMA)
                self.state = 668
                self.exps()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 670
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
        self.enterRule(localctx, 132, self.RULE_normal_id_list)
        try:
            self.state = 677
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,52,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 673
                self.match(D96Parser.NORMAL_ID)
                self.state = 674
                self.match(D96Parser.COMMA)
                self.state = 675
                self.normal_id_list()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 676
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
        self.enterRule(localctx, 134, self.RULE_id_list)
        self._la = 0 # Token type
        try:
            self.state = 683
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,53,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 679
                _la = self._input.LA(1)
                if not(_la==D96Parser.NORMAL_ID or _la==D96Parser.DOLLAR_ID):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 680
                self.match(D96Parser.COMMA)
                self.state = 681
                self.id_list()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 682
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
        self._predicates[53] = self.exp1_sempred
        self._predicates[54] = self.exp2_sempred
        self._predicates[55] = self.exp3_sempred
        self._predicates[58] = self.exp6_sempred
        self._predicates[59] = self.exp7_sempred
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
                return self.precpred(self._ctx, 3)
         

            if predIndex == 9:
                return self.precpred(self._ctx, 2)
         




