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
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3D")
        buf.write("\u028a\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
        buf.write("\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r\4\16")
        buf.write("\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23\t\23")
        buf.write("\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30\4\31")
        buf.write("\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36\t\36")
        buf.write("\4\37\t\37\4 \t \4!\t!\4\"\t\"\4#\t#\4$\t$\4%\t%\4&\t")
        buf.write("&\4\'\t\'\4(\t(\4)\t)\4*\t*\4+\t+\4,\t,\4-\t-\4.\t.\4")
        buf.write("/\t/\4\60\t\60\4\61\t\61\4\62\t\62\4\63\t\63\4\64\t\64")
        buf.write("\4\65\t\65\4\66\t\66\4\67\t\67\48\t8\49\t9\4:\t:\4;\t")
        buf.write(";\4<\t<\4=\t=\4>\t>\4?\t?\4@\t@\4A\tA\4B\tB\4C\tC\3\2")
        buf.write("\3\2\3\2\6\2\u008a\n\2\r\2\16\2\u008b\3\2\3\2\3\3\3\3")
        buf.write("\3\3\3\3\3\4\3\4\5\4\u0096\n\4\3\5\3\5\3\5\3\5\5\5\u009c")
        buf.write("\n\5\3\6\3\6\3\6\3\6\3\6\3\7\3\7\3\7\5\7\u00a6\n\7\3\b")
        buf.write("\3\b\3\b\3\b\3\t\3\t\5\t\u00ae\n\t\3\n\3\n\3\n\3\n\5\n")
        buf.write("\u00b4\n\n\3\13\3\13\3\13\3\13\3\13\5\13\u00bb\n\13\3")
        buf.write("\f\3\f\3\f\3\f\3\f\3\r\3\r\3\r\3\r\3\r\3\r\3\16\3\16\3")
        buf.write("\16\3\16\3\16\3\17\3\17\3\17\3\17\3\20\3\20\5\20\u00d3")
        buf.write("\n\20\3\21\3\21\3\21\3\21\5\21\u00d9\n\21\3\22\3\22\3")
        buf.write("\22\3\22\3\22\3\22\3\22\3\22\3\22\3\22\3\22\3\22\3\22")
        buf.write("\3\22\3\22\3\22\3\22\3\22\5\22\u00ed\n\22\3\23\3\23\3")
        buf.write("\23\3\23\3\23\3\23\3\24\3\24\5\24\u00f7\n\24\3\25\3\25")
        buf.write("\3\25\3\25\3\25\5\25\u00fe\n\25\3\26\3\26\3\26\3\26\3")
        buf.write("\26\3\26\3\26\3\26\5\26\u0108\n\26\3\27\3\27\3\27\3\27")
        buf.write("\3\30\3\30\5\30\u0110\n\30\3\31\3\31\3\31\3\31\5\31\u0116")
        buf.write("\n\31\3\32\3\32\3\32\3\32\3\32\3\32\3\32\3\32\3\32\3\32")
        buf.write("\3\32\3\32\3\32\3\32\3\32\3\32\3\32\3\32\3\32\5\32\u012b")
        buf.write("\n\32\3\33\3\33\3\33\3\34\3\34\3\34\3\35\3\35\5\35\u0135")
        buf.write("\n\35\3\35\3\35\3\36\3\36\3\36\3\36\3\36\3\37\3\37\3\37")
        buf.write("\3\37\3\37\3\37\3\37\3\37\3 \3 \5 \u0148\n \3!\3!\3!\3")
        buf.write("!\5!\u014e\n!\3\"\3\"\3\"\3\"\3\"\3\"\3#\3#\3#\5#\u0159")
        buf.write("\n#\3$\3$\3$\3$\3$\3$\3$\3$\3$\3$\3$\3%\3%\3%\5%\u0169")
        buf.write("\n%\3&\3&\3&\5&\u016e\n&\3\'\3\'\3\'\3(\3(\3(\3(\3)\3")
        buf.write(")\3)\3)\3)\3)\3)\3*\3*\3*\3*\3+\3+\3+\3+\3+\3+\3+\3,\3")
        buf.write(",\3,\3,\3-\3-\3-\3-\3-\3-\3-\3-\3-\3-\3-\3-\5-\u0199\n")
        buf.write("-\5-\u019b\n-\3.\3.\3.\3.\3.\3.\3.\3.\3.\3.\3.\3.\3.\5")
        buf.write(".\u01aa\n.\3.\5.\u01ad\n.\3/\3/\3/\3/\3/\3/\3/\3/\5/\u01b7")
        buf.write("\n/\3/\3/\3/\3/\3\60\3\60\3\60\3\60\3\60\3\61\3\61\5\61")
        buf.write("\u01c4\n\61\3\62\3\62\3\62\3\62\3\62\5\62\u01cb\n\62\3")
        buf.write("\63\3\63\3\63\3\63\3\63\3\63\3\63\3\63\3\63\5\63\u01d6")
        buf.write("\n\63\3\64\3\64\3\64\3\64\3\64\3\64\3\64\3\64\3\64\3\64")
        buf.write("\3\64\3\64\3\64\3\64\3\64\3\64\3\64\3\64\3\64\3\64\3\64")
        buf.write("\3\64\3\64\3\64\3\64\5\64\u01f1\n\64\3\65\3\65\3\65\3")
        buf.write("\65\3\65\3\65\3\65\3\65\3\65\7\65\u01fc\n\65\f\65\16\65")
        buf.write("\u01ff\13\65\3\66\3\66\3\66\3\66\3\66\3\66\3\66\3\66\3")
        buf.write("\66\7\66\u020a\n\66\f\66\16\66\u020d\13\66\3\67\3\67\3")
        buf.write("\67\3\67\3\67\3\67\3\67\3\67\3\67\3\67\3\67\3\67\7\67")
        buf.write("\u021b\n\67\f\67\16\67\u021e\13\67\38\38\38\58\u0223\n")
        buf.write("8\39\39\39\59\u0228\n9\3:\3:\3:\3:\3:\3:\3:\3:\7:\u0232")
        buf.write("\n:\f:\16:\u0235\13:\3;\3;\3;\3;\3;\3;\3;\3;\3;\5;\u0240")
        buf.write("\n;\3<\3<\3<\3<\3<\3<\3<\3<\3<\3<\3<\3<\3<\7<\u024f\n")
        buf.write("<\f<\16<\u0252\13<\3=\3=\3=\3=\3=\3=\3=\3=\3=\3=\3=\5")
        buf.write("=\u025f\n=\3>\3>\3>\3>\3>\3>\3>\5>\u0268\n>\3?\3?\3?\3")
        buf.write("?\3?\3?\3?\3?\3?\5?\u0273\n?\3@\3@\3@\3@\3A\3A\5A\u027b")
        buf.write("\nA\3B\3B\3B\3B\3B\5B\u0282\nB\3C\3C\3C\3C\5C\u0288\n")
        buf.write("C\3C\2\7hjlrvD\2\4\6\b\n\f\16\20\22\24\26\30\32\34\36")
        buf.write(" \"$&(*,.\60\62\64\668:<>@BDFHJLNPRTVXZ\\^`bdfhjlnprt")
        buf.write("vxz|~\u0080\u0082\u0084\2\4\3\2@A\3\2\3\4\2\u02ae\2\u0089")
        buf.write("\3\2\2\2\4\u008f\3\2\2\2\6\u0095\3\2\2\2\b\u009b\3\2\2")
        buf.write("\2\n\u009d\3\2\2\2\f\u00a5\3\2\2\2\16\u00a7\3\2\2\2\20")
        buf.write("\u00ad\3\2\2\2\22\u00b3\3\2\2\2\24\u00ba\3\2\2\2\26\u00bc")
        buf.write("\3\2\2\2\30\u00c1\3\2\2\2\32\u00c7\3\2\2\2\34\u00cc\3")
        buf.write("\2\2\2\36\u00d2\3\2\2\2 \u00d8\3\2\2\2\"\u00ec\3\2\2\2")
        buf.write("$\u00ee\3\2\2\2&\u00f6\3\2\2\2(\u00fd\3\2\2\2*\u00ff\3")
        buf.write("\2\2\2,\u0109\3\2\2\2.\u010f\3\2\2\2\60\u0115\3\2\2\2")
        buf.write("\62\u012a\3\2\2\2\64\u012c\3\2\2\2\66\u012f\3\2\2\28\u0132")
        buf.write("\3\2\2\2:\u0138\3\2\2\2<\u013d\3\2\2\2>\u0147\3\2\2\2")
        buf.write("@\u014d\3\2\2\2B\u014f\3\2\2\2D\u0158\3\2\2\2F\u015a\3")
        buf.write("\2\2\2H\u0168\3\2\2\2J\u016d\3\2\2\2L\u016f\3\2\2\2N\u0172")
        buf.write("\3\2\2\2P\u0176\3\2\2\2R\u017d\3\2\2\2T\u0181\3\2\2\2")
        buf.write("V\u0188\3\2\2\2X\u019a\3\2\2\2Z\u01ac\3\2\2\2\\\u01ae")
        buf.write("\3\2\2\2^\u01bc\3\2\2\2`\u01c3\3\2\2\2b\u01ca\3\2\2\2")
        buf.write("d\u01d5\3\2\2\2f\u01f0\3\2\2\2h\u01f2\3\2\2\2j\u0200\3")
        buf.write("\2\2\2l\u020e\3\2\2\2n\u0222\3\2\2\2p\u0227\3\2\2\2r\u0229")
        buf.write("\3\2\2\2t\u023f\3\2\2\2v\u0241\3\2\2\2x\u025e\3\2\2\2")
        buf.write("z\u0267\3\2\2\2|\u0272\3\2\2\2~\u0274\3\2\2\2\u0080\u027a")
        buf.write("\3\2\2\2\u0082\u0281\3\2\2\2\u0084\u0287\3\2\2\2\u0086")
        buf.write("\u008a\5R*\2\u0087\u008a\5d\63\2\u0088\u008a\5:\36\2\u0089")
        buf.write("\u0086\3\2\2\2\u0089\u0087\3\2\2\2\u0089\u0088\3\2\2\2")
        buf.write("\u008a\u008b\3\2\2\2\u008b\u0089\3\2\2\2\u008b\u008c\3")
        buf.write("\2\2\2\u008c\u008d\3\2\2\2\u008d\u008e\7\2\2\3\u008e\3")
        buf.write("\3\2\2\2\u008f\u0090\7\66\2\2\u0090\u0091\7\64\2\2\u0091")
        buf.write("\u0092\5\16\b\2\u0092\5\3\2\2\2\u0093\u0096\5\b\5\2\u0094")
        buf.write("\u0096\3\2\2\2\u0095\u0093\3\2\2\2\u0095\u0094\3\2\2\2")
        buf.write("\u0096\7\3\2\2\2\u0097\u0098\5\n\6\2\u0098\u0099\5\b\5")
        buf.write("\2\u0099\u009c\3\2\2\2\u009a\u009c\5\n\6\2\u009b\u0097")
        buf.write("\3\2\2\2\u009b\u009a\3\2\2\2\u009c\t\3\2\2\2\u009d\u009e")
        buf.write("\7\66\2\2\u009e\u009f\7@\2\2\u009f\u00a0\5\f\7\2\u00a0")
        buf.write("\u00a1\5\16\b\2\u00a1\13\3\2\2\2\u00a2\u00a3\7\r\2\2\u00a3")
        buf.write("\u00a6\7@\2\2\u00a4\u00a6\3\2\2\2\u00a5\u00a2\3\2\2\2")
        buf.write("\u00a5\u00a4\3\2\2\2\u00a6\r\3\2\2\2\u00a7\u00a8\7\7\2")
        buf.write("\2\u00a8\u00a9\5\20\t\2\u00a9\u00aa\7\b\2\2\u00aa\17\3")
        buf.write("\2\2\2\u00ab\u00ae\5\22\n\2\u00ac\u00ae\3\2\2\2\u00ad")
        buf.write("\u00ab\3\2\2\2\u00ad\u00ac\3\2\2\2\u00ae\21\3\2\2\2\u00af")
        buf.write("\u00b0\5\24\13\2\u00b0\u00b1\5\22\n\2\u00b1\u00b4\3\2")
        buf.write("\2\2\u00b2\u00b4\5\24\13\2\u00b3\u00af\3\2\2\2\u00b3\u00b2")
        buf.write("\3\2\2\2\u00b4\23\3\2\2\2\u00b5\u00bb\5V,\2\u00b6\u00bb")
        buf.write("\5\30\r\2\u00b7\u00bb\5\32\16\2\u00b8\u00bb\5\26\f\2\u00b9")
        buf.write("\u00bb\5$\23\2\u00ba\u00b5\3\2\2\2\u00ba\u00b6\3\2\2\2")
        buf.write("\u00ba\u00b7\3\2\2\2\u00ba\u00b8\3\2\2\2\u00ba\u00b9\3")
        buf.write("\2\2\2\u00bb\25\3\2\2\2\u00bc\u00bd\7\65\2\2\u00bd\u00be")
        buf.write("\7\5\2\2\u00be\u00bf\7\6\2\2\u00bf\u00c0\5,\27\2\u00c0")
        buf.write("\27\3\2\2\2\u00c1\u00c2\7\33\2\2\u00c2\u00c3\7\5\2\2\u00c3")
        buf.write("\u00c4\5&\24\2\u00c4\u00c5\7\6\2\2\u00c5\u00c6\5,\27\2")
        buf.write("\u00c6\31\3\2\2\2\u00c7\u00c8\7\34\2\2\u00c8\u00c9\7\5")
        buf.write("\2\2\u00c9\u00ca\7\6\2\2\u00ca\u00cb\5\34\17\2\u00cb\33")
        buf.write("\3\2\2\2\u00cc\u00cd\7\7\2\2\u00cd\u00ce\5\36\20\2\u00ce")
        buf.write("\u00cf\7\b\2\2\u00cf\35\3\2\2\2\u00d0\u00d3\5 \21\2\u00d1")
        buf.write("\u00d3\3\2\2\2\u00d2\u00d0\3\2\2\2\u00d2\u00d1\3\2\2\2")
        buf.write("\u00d3\37\3\2\2\2\u00d4\u00d9\5\"\22\2\u00d5\u00d6\5\"")
        buf.write("\22\2\u00d6\u00d7\5 \21\2\u00d7\u00d9\3\2\2\2\u00d8\u00d4")
        buf.write("\3\2\2\2\u00d8\u00d5\3\2\2\2\u00d9!\3\2\2\2\u00da\u00ed")
        buf.write("\5V,\2\u00db\u00ed\5:\36\2\u00dc\u00ed\5\64\33\2\u00dd")
        buf.write("\u00ed\5\66\34\2\u00de\u00df\5T+\2\u00df\u00e0\7\13\2")
        buf.write("\2\u00e0\u00ed\3\2\2\2\u00e1\u00e2\5P)\2\u00e2\u00e3\7")
        buf.write("\13\2\2\u00e3\u00ed\3\2\2\2\u00e4\u00e5\5R*\2\u00e5\u00e6")
        buf.write("\7\13\2\2\u00e6\u00ed\3\2\2\2\u00e7\u00e8\5T+\2\u00e8")
        buf.write("\u00e9\7\13\2\2\u00e9\u00ed\3\2\2\2\u00ea\u00ed\5<\37")
        buf.write("\2\u00eb\u00ed\5F$\2\u00ec\u00da\3\2\2\2\u00ec\u00db\3")
        buf.write("\2\2\2\u00ec\u00dc\3\2\2\2\u00ec\u00dd\3\2\2\2\u00ec\u00de")
        buf.write("\3\2\2\2\u00ec\u00e1\3\2\2\2\u00ec\u00e4\3\2\2\2\u00ec")
        buf.write("\u00e7\3\2\2\2\u00ec\u00ea\3\2\2\2\u00ec\u00eb\3\2\2\2")
        buf.write("\u00ed#\3\2\2\2\u00ee\u00ef\t\2\2\2\u00ef\u00f0\7\5\2")
        buf.write("\2\u00f0\u00f1\5&\24\2\u00f1\u00f2\7\6\2\2\u00f2\u00f3")
        buf.write("\5,\27\2\u00f3%\3\2\2\2\u00f4\u00f7\5(\25\2\u00f5\u00f7")
        buf.write("\3\2\2\2\u00f6\u00f4\3\2\2\2\u00f6\u00f5\3\2\2\2\u00f7")
        buf.write("\'\3\2\2\2\u00f8\u00f9\5*\26\2\u00f9\u00fa\7\13\2\2\u00fa")
        buf.write("\u00fb\5(\25\2\u00fb\u00fe\3\2\2\2\u00fc\u00fe\5*\26\2")
        buf.write("\u00fd\u00f8\3\2\2\2\u00fd\u00fc\3\2\2\2\u00fe)\3\2\2")
        buf.write("\2\u00ff\u0100\5\u0084C\2\u0100\u0107\7\r\2\2\u0101\u0108")
        buf.write("\7\30\2\2\u0102\u0108\79\2\2\u0103\u0108\7\67\2\2\u0104")
        buf.write("\u0108\5\\/\2\u0105\u0108\78\2\2\u0106\u0108\7@\2\2\u0107")
        buf.write("\u0101\3\2\2\2\u0107\u0102\3\2\2\2\u0107\u0103\3\2\2\2")
        buf.write("\u0107\u0104\3\2\2\2\u0107\u0105\3\2\2\2\u0107\u0106\3")
        buf.write("\2\2\2\u0108+\3\2\2\2\u0109\u010a\7\7\2\2\u010a\u010b")
        buf.write("\5.\30\2\u010b\u010c\7\b\2\2\u010c-\3\2\2\2\u010d\u0110")
        buf.write("\5\60\31\2\u010e\u0110\3\2\2\2\u010f\u010d\3\2\2\2\u010f")
        buf.write("\u010e\3\2\2\2\u0110/\3\2\2\2\u0111\u0112\5\62\32\2\u0112")
        buf.write("\u0113\5\60\31\2\u0113\u0116\3\2\2\2\u0114\u0116\5\62")
        buf.write("\32\2\u0115\u0111\3\2\2\2\u0115\u0114\3\2\2\2\u0116\61")
        buf.write("\3\2\2\2\u0117\u012b\5:\36\2\u0118\u012b\5V,\2\u0119\u012b")
        buf.write("\5\64\33\2\u011a\u012b\5\66\34\2\u011b\u012b\58\35\2\u011c")
        buf.write("\u011d\5T+\2\u011d\u011e\7\13\2\2\u011e\u012b\3\2\2\2")
        buf.write("\u011f\u0120\5R*\2\u0120\u0121\7\13\2\2\u0121\u012b\3")
        buf.write("\2\2\2\u0122\u0123\5N(\2\u0123\u0124\7\13\2\2\u0124\u012b")
        buf.write("\3\2\2\2\u0125\u0126\5P)\2\u0126\u0127\7\13\2\2\u0127")
        buf.write("\u012b\3\2\2\2\u0128\u012b\5<\37\2\u0129\u012b\5F$\2\u012a")
        buf.write("\u0117\3\2\2\2\u012a\u0118\3\2\2\2\u012a\u0119\3\2\2\2")
        buf.write("\u012a\u011a\3\2\2\2\u012a\u011b\3\2\2\2\u012a\u011c\3")
        buf.write("\2\2\2\u012a\u011f\3\2\2\2\u012a\u0122\3\2\2\2\u012a\u0125")
        buf.write("\3\2\2\2\u012a\u0128\3\2\2\2\u012a\u0129\3\2\2\2\u012b")
        buf.write("\63\3\2\2\2\u012c\u012d\7\16\2\2\u012d\u012e\7\13\2\2")
        buf.write("\u012e\65\3\2\2\2\u012f\u0130\7\17\2\2\u0130\u0131\7\13")
        buf.write("\2\2\u0131\67\3\2\2\2\u0132\u0134\7\31\2\2\u0133\u0135")
        buf.write("\5d\63\2\u0134\u0133\3\2\2\2\u0134\u0135\3\2\2\2\u0135")
        buf.write("\u0136\3\2\2\2\u0136\u0137\7\13\2\2\u01379\3\2\2\2\u0138")
        buf.write("\u0139\5J&\2\u0139\u013a\7)\2\2\u013a\u013b\5d\63\2\u013b")
        buf.write("\u013c\7\13\2\2\u013c;\3\2\2\2\u013d\u013e\7\20\2\2\u013e")
        buf.write("\u013f\7\5\2\2\u013f\u0140\5d\63\2\u0140\u0141\7\6\2\2")
        buf.write("\u0141\u0142\5,\27\2\u0142\u0143\5> \2\u0143\u0144\5D")
        buf.write("#\2\u0144=\3\2\2\2\u0145\u0148\5@!\2\u0146\u0148\3\2\2")
        buf.write("\2\u0147\u0145\3\2\2\2\u0147\u0146\3\2\2\2\u0148?\3\2")
        buf.write("\2\2\u0149\u014e\5B\"\2\u014a\u014b\5B\"\2\u014b\u014c")
        buf.write("\5@!\2\u014c\u014e\3\2\2\2\u014d\u0149\3\2\2\2\u014d\u014a")
        buf.write("\3\2\2\2\u014eA\3\2\2\2\u014f\u0150\7\21\2\2\u0150\u0151")
        buf.write("\7\5\2\2\u0151\u0152\5d\63\2\u0152\u0153\7\6\2\2\u0153")
        buf.write("\u0154\5,\27\2\u0154C\3\2\2\2\u0155\u0156\7\22\2\2\u0156")
        buf.write("\u0159\5,\27\2\u0157\u0159\3\2\2\2\u0158\u0155\3\2\2\2")
        buf.write("\u0158\u0157\3\2\2\2\u0159E\3\2\2\2\u015a\u015b\7\23\2")
        buf.write("\2\u015b\u015c\7\5\2\2\u015c\u015d\t\2\2\2\u015d\u015e")
        buf.write("\7\27\2\2\u015e\u015f\5d\63\2\u015f\u0160\7\62\2\2\u0160")
        buf.write("\u0161\5d\63\2\u0161\u0162\5H%\2\u0162\u0163\7\6\2\2\u0163")
        buf.write("\u0164\5,\27\2\u0164G\3\2\2\2\u0165\u0166\7\36\2\2\u0166")
        buf.write("\u0169\5d\63\2\u0167\u0169\3\2\2\2\u0168\u0165\3\2\2\2")
        buf.write("\u0168\u0167\3\2\2\2\u0169I\3\2\2\2\u016a\u016e\7@\2\2")
        buf.write("\u016b\u016e\7A\2\2\u016c\u016e\5L\'\2\u016d\u016a\3\2")
        buf.write("\2\2\u016d\u016b\3\2\2\2\u016d\u016c\3\2\2\2\u016eK\3")
        buf.write("\2\2\2\u016f\u0170\t\2\2\2\u0170\u0171\5t;\2\u0171M\3")
        buf.write("\2\2\2\u0172\u0173\7@\2\2\u0173\u0174\7\63\2\2\u0174\u0175")
        buf.write("\7A\2\2\u0175O\3\2\2\2\u0176\u0177\7@\2\2\u0177\u0178")
        buf.write("\7\63\2\2\u0178\u0179\7A\2\2\u0179\u017a\7\5\2\2\u017a")
        buf.write("\u017b\5\u0080A\2\u017b\u017c\7\6\2\2\u017cQ\3\2\2\2\u017d")
        buf.write("\u017e\5d\63\2\u017e\u017f\7\61\2\2\u017f\u0180\t\2\2")
        buf.write("\2\u0180S\3\2\2\2\u0181\u0182\5d\63\2\u0182\u0183\7\61")
        buf.write("\2\2\u0183\u0184\7@\2\2\u0184\u0185\7\5\2\2\u0185\u0186")
        buf.write("\5\u0080A\2\u0186\u0187\7\6\2\2\u0187U\3\2\2\2\u0188\u0189")
        buf.write("\t\3\2\2\u0189\u018a\5X-\2\u018a\u018b\7\13\2\2\u018b")
        buf.write("W\3\2\2\2\u018c\u018d\t\2\2\2\u018d\u018e\5Z.\2\u018e")
        buf.write("\u018f\5d\63\2\u018f\u019b\3\2\2\2\u0190\u0191\5\u0084")
        buf.write("C\2\u0191\u0198\7\r\2\2\u0192\u0199\7\30\2\2\u0193\u0199")
        buf.write("\79\2\2\u0194\u0199\7\67\2\2\u0195\u0199\5\\/\2\u0196")
        buf.write("\u0199\78\2\2\u0197\u0199\7@\2\2\u0198\u0192\3\2\2\2\u0198")
        buf.write("\u0193\3\2\2\2\u0198\u0194\3\2\2\2\u0198\u0195\3\2\2\2")
        buf.write("\u0198\u0196\3\2\2\2\u0198\u0197\3\2\2\2\u0199\u019b\3")
        buf.write("\2\2\2\u019a\u018c\3\2\2\2\u019a\u0190\3\2\2\2\u019bY")
        buf.write("\3\2\2\2\u019c\u019d\7\f\2\2\u019d\u019e\t\2\2\2\u019e")
        buf.write("\u019f\5Z.\2\u019f\u01a0\5d\63\2\u01a0\u01a1\7\f\2\2\u01a1")
        buf.write("\u01ad\3\2\2\2\u01a2\u01a9\7\r\2\2\u01a3\u01aa\7\30\2")
        buf.write("\2\u01a4\u01aa\79\2\2\u01a5\u01aa\7\67\2\2\u01a6\u01aa")
        buf.write("\5\\/\2\u01a7\u01aa\78\2\2\u01a8\u01aa\7@\2\2\u01a9\u01a3")
        buf.write("\3\2\2\2\u01a9\u01a4\3\2\2\2\u01a9\u01a5\3\2\2\2\u01a9")
        buf.write("\u01a6\3\2\2\2\u01a9\u01a7\3\2\2\2\u01a9\u01a8\3\2\2\2")
        buf.write("\u01aa\u01ab\3\2\2\2\u01ab\u01ad\7)\2\2\u01ac\u019c\3")
        buf.write("\2\2\2\u01ac\u01a2\3\2\2\2\u01ad[\3\2\2\2\u01ae\u01af")
        buf.write("\7\26\2\2\u01af\u01b6\7\t\2\2\u01b0\u01b7\7\30\2\2\u01b1")
        buf.write("\u01b7\79\2\2\u01b2\u01b7\7\67\2\2\u01b3\u01b7\5\\/\2")
        buf.write("\u01b4\u01b7\78\2\2\u01b5\u01b7\7@\2\2\u01b6\u01b0\3\2")
        buf.write("\2\2\u01b6\u01b1\3\2\2\2\u01b6\u01b2\3\2\2\2\u01b6\u01b3")
        buf.write("\3\2\2\2\u01b6\u01b4\3\2\2\2\u01b6\u01b5\3\2\2\2\u01b7")
        buf.write("\u01b8\3\2\2\2\u01b8\u01b9\7\f\2\2\u01b9\u01ba\7;\2\2")
        buf.write("\u01ba\u01bb\7\n\2\2\u01bb]\3\2\2\2\u01bc\u01bd\7\26\2")
        buf.write("\2\u01bd\u01be\7\5\2\2\u01be\u01bf\5`\61\2\u01bf\u01c0")
        buf.write("\7\6\2\2\u01c0_\3\2\2\2\u01c1\u01c4\5b\62\2\u01c2\u01c4")
        buf.write("\3\2\2\2\u01c3\u01c1\3\2\2\2\u01c3\u01c2\3\2\2\2\u01c4")
        buf.write("a\3\2\2\2\u01c5\u01c6\5d\63\2\u01c6\u01c7\7\f\2\2\u01c7")
        buf.write("\u01c8\5b\62\2\u01c8\u01cb\3\2\2\2\u01c9\u01cb\5d\63\2")
        buf.write("\u01ca\u01c5\3\2\2\2\u01ca\u01c9\3\2\2\2\u01cbc\3\2\2")
        buf.write("\2\u01cc\u01cd\5f\64\2\u01cd\u01ce\7/\2\2\u01ce\u01cf")
        buf.write("\5f\64\2\u01cf\u01d6\3\2\2\2\u01d0\u01d1\5f\64\2\u01d1")
        buf.write("\u01d2\7\60\2\2\u01d2\u01d3\5f\64\2\u01d3\u01d6\3\2\2")
        buf.write("\2\u01d4\u01d6\5f\64\2\u01d5\u01cc\3\2\2\2\u01d5\u01d0")
        buf.write("\3\2\2\2\u01d5\u01d4\3\2\2\2\u01d6e\3\2\2\2\u01d7\u01d8")
        buf.write("\5h\65\2\u01d8\u01d9\7-\2\2\u01d9\u01da\5h\65\2\u01da")
        buf.write("\u01f1\3\2\2\2\u01db\u01dc\5h\65\2\u01dc\u01dd\7.\2\2")
        buf.write("\u01dd\u01de\5h\65\2\u01de\u01f1\3\2\2\2\u01df\u01e0\5")
        buf.write("h\65\2\u01e0\u01e1\7+\2\2\u01e1\u01e2\5h\65\2\u01e2\u01f1")
        buf.write("\3\2\2\2\u01e3\u01e4\5h\65\2\u01e4\u01e5\7(\2\2\u01e5")
        buf.write("\u01e6\5h\65\2\u01e6\u01f1\3\2\2\2\u01e7\u01e8\5h\65\2")
        buf.write("\u01e8\u01e9\7*\2\2\u01e9\u01ea\5h\65\2\u01ea\u01f1\3")
        buf.write("\2\2\2\u01eb\u01ec\5h\65\2\u01ec\u01ed\7,\2\2\u01ed\u01ee")
        buf.write("\5h\65\2\u01ee\u01f1\3\2\2\2\u01ef\u01f1\5h\65\2\u01f0")
        buf.write("\u01d7\3\2\2\2\u01f0\u01db\3\2\2\2\u01f0\u01df\3\2\2\2")
        buf.write("\u01f0\u01e3\3\2\2\2\u01f0\u01e7\3\2\2\2\u01f0\u01eb\3")
        buf.write("\2\2\2\u01f0\u01ef\3\2\2\2\u01f1g\3\2\2\2\u01f2\u01f3")
        buf.write("\b\65\1\2\u01f3\u01f4\5j\66\2\u01f4\u01fd\3\2\2\2\u01f5")
        buf.write("\u01f6\f\5\2\2\u01f6\u01f7\7&\2\2\u01f7\u01fc\5j\66\2")
        buf.write("\u01f8\u01f9\f\4\2\2\u01f9\u01fa\7\'\2\2\u01fa\u01fc\5")
        buf.write("j\66\2\u01fb\u01f5\3\2\2\2\u01fb\u01f8\3\2\2\2\u01fc\u01ff")
        buf.write("\3\2\2\2\u01fd\u01fb\3\2\2\2\u01fd\u01fe\3\2\2\2\u01fe")
        buf.write("i\3\2\2\2\u01ff\u01fd\3\2\2\2\u0200\u0201\b\66\1\2\u0201")
        buf.write("\u0202\5l\67\2\u0202\u020b\3\2\2\2\u0203\u0204\f\5\2\2")
        buf.write("\u0204\u0205\7 \2\2\u0205\u020a\5l\67\2\u0206\u0207\f")
        buf.write("\4\2\2\u0207\u0208\7!\2\2\u0208\u020a\5l\67\2\u0209\u0203")
        buf.write("\3\2\2\2\u0209\u0206\3\2\2\2\u020a\u020d\3\2\2\2\u020b")
        buf.write("\u0209\3\2\2\2\u020b\u020c\3\2\2\2\u020ck\3\2\2\2\u020d")
        buf.write("\u020b\3\2\2\2\u020e\u020f\b\67\1\2\u020f\u0210\5n8\2")
        buf.write("\u0210\u021c\3\2\2\2\u0211\u0212\f\6\2\2\u0212\u0213\7")
        buf.write("\"\2\2\u0213\u021b\5n8\2\u0214\u0215\f\5\2\2\u0215\u0216")
        buf.write("\7#\2\2\u0216\u021b\5n8\2\u0217\u0218\f\4\2\2\u0218\u0219")
        buf.write("\7$\2\2\u0219\u021b\5n8\2\u021a\u0211\3\2\2\2\u021a\u0214")
        buf.write("\3\2\2\2\u021a\u0217\3\2\2\2\u021b\u021e\3\2\2\2\u021c")
        buf.write("\u021a\3\2\2\2\u021c\u021d\3\2\2\2\u021dm\3\2\2\2\u021e")
        buf.write("\u021c\3\2\2\2\u021f\u0220\7%\2\2\u0220\u0223\5n8\2\u0221")
        buf.write("\u0223\5p9\2\u0222\u021f\3\2\2\2\u0222\u0221\3\2\2\2\u0223")
        buf.write("o\3\2\2\2\u0224\u0225\7!\2\2\u0225\u0228\5p9\2\u0226\u0228")
        buf.write("\5r:\2\u0227\u0224\3\2\2\2\u0227\u0226\3\2\2\2\u0228q")
        buf.write("\3\2\2\2\u0229\u022a\b:\1\2\u022a\u022b\5v<\2\u022b\u0233")
        buf.write("\3\2\2\2\u022c\u022d\f\4\2\2\u022d\u022e\7\t\2\2\u022e")
        buf.write("\u022f\5d\63\2\u022f\u0230\7\n\2\2\u0230\u0232\3\2\2\2")
        buf.write("\u0231\u022c\3\2\2\2\u0232\u0235\3\2\2\2\u0233\u0231\3")
        buf.write("\2\2\2\u0233\u0234\3\2\2\2\u0234s\3\2\2\2\u0235\u0233")
        buf.write("\3\2\2\2\u0236\u0237\7\t\2\2\u0237\u0238\5d\63\2\u0238")
        buf.write("\u0239\7\n\2\2\u0239\u0240\3\2\2\2\u023a\u023b\7\t\2\2")
        buf.write("\u023b\u023c\5d\63\2\u023c\u023d\7\n\2\2\u023d\u023e\5")
        buf.write("t;\2\u023e\u0240\3\2\2\2\u023f\u0236\3\2\2\2\u023f\u023a")
        buf.write("\3\2\2\2\u0240u\3\2\2\2\u0241\u0242\b<\1\2\u0242\u0243")
        buf.write("\5x=\2\u0243\u0250\3\2\2\2\u0244\u0245\f\5\2\2\u0245\u0246")
        buf.write("\7\61\2\2\u0246\u0247\t\2\2\2\u0247\u0248\7\5\2\2\u0248")
        buf.write("\u0249\5\u0080A\2\u0249\u024a\7\6\2\2\u024a\u024f\3\2")
        buf.write("\2\2\u024b\u024c\f\4\2\2\u024c\u024d\7\61\2\2\u024d\u024f")
        buf.write("\t\2\2\2\u024e\u0244\3\2\2\2\u024e\u024b\3\2\2\2\u024f")
        buf.write("\u0252\3\2\2\2\u0250\u024e\3\2\2\2\u0250\u0251\3\2\2\2")
        buf.write("\u0251w\3\2\2\2\u0252\u0250\3\2\2\2\u0253\u0254\7@\2\2")
        buf.write("\u0254\u0255\7\63\2\2\u0255\u0256\7A\2\2\u0256\u0257\7")
        buf.write("\5\2\2\u0257\u0258\5\u0080A\2\u0258\u0259\7\6\2\2\u0259")
        buf.write("\u025f\3\2\2\2\u025a\u025b\7@\2\2\u025b\u025c\7\63\2\2")
        buf.write("\u025c\u025f\7A\2\2\u025d\u025f\5z>\2\u025e\u0253\3\2")
        buf.write("\2\2\u025e\u025a\3\2\2\2\u025e\u025d\3\2\2\2\u025fy\3")
        buf.write("\2\2\2\u0260\u0261\7\35\2\2\u0261\u0262\5z>\2\u0262\u0263")
        buf.write("\7\5\2\2\u0263\u0264\5\u0080A\2\u0264\u0265\7\6\2\2\u0265")
        buf.write("\u0268\3\2\2\2\u0266\u0268\5|?\2\u0267\u0260\3\2\2\2\u0267")
        buf.write("\u0266\3\2\2\2\u0268{\3\2\2\2\u0269\u0273\7;\2\2\u026a")
        buf.write("\u0273\5^\60\2\u026b\u0273\7:\2\2\u026c\u0273\7?\2\2\u026d")
        buf.write("\u0273\7<\2\2\u026e\u0273\7@\2\2\u026f\u0273\7A\2\2\u0270")
        buf.write("\u0273\7\37\2\2\u0271\u0273\5~@\2\u0272\u0269\3\2\2\2")
        buf.write("\u0272\u026a\3\2\2\2\u0272\u026b\3\2\2\2\u0272\u026c\3")
        buf.write("\2\2\2\u0272\u026d\3\2\2\2\u0272\u026e\3\2\2\2\u0272\u026f")
        buf.write("\3\2\2\2\u0272\u0270\3\2\2\2\u0272\u0271\3\2\2\2\u0273")
        buf.write("}\3\2\2\2\u0274\u0275\7\5\2\2\u0275\u0276\5d\63\2\u0276")
        buf.write("\u0277\7\6\2\2\u0277\177\3\2\2\2\u0278\u027b\5\u0082B")
        buf.write("\2\u0279\u027b\3\2\2\2\u027a\u0278\3\2\2\2\u027a\u0279")
        buf.write("\3\2\2\2\u027b\u0081\3\2\2\2\u027c\u027d\5d\63\2\u027d")
        buf.write("\u027e\7\f\2\2\u027e\u027f\5\u0082B\2\u027f\u0282\3\2")
        buf.write("\2\2\u0280\u0282\5d\63\2\u0281\u027c\3\2\2\2\u0281\u0280")
        buf.write("\3\2\2\2\u0282\u0083\3\2\2\2\u0283\u0284\t\2\2\2\u0284")
        buf.write("\u0285\7\f\2\2\u0285\u0288\5\u0084C\2\u0286\u0288\t\2")
        buf.write("\2\2\u0287\u0283\3\2\2\2\u0287\u0286\3\2\2\2\u0288\u0085")
        buf.write("\3\2\2\2\64\u0089\u008b\u0095\u009b\u00a5\u00ad\u00b3")
        buf.write("\u00ba\u00d2\u00d8\u00ec\u00f6\u00fd\u0107\u010f\u0115")
        buf.write("\u012a\u0134\u0147\u014d\u0158\u0168\u016d\u0198\u019a")
        buf.write("\u01a9\u01ac\u01b6\u01c3\u01ca\u01d5\u01f0\u01fb\u01fd")
        buf.write("\u0209\u020b\u021a\u021c\u0222\u0227\u0233\u023f\u024e")
        buf.write("\u0250\u025e\u0267\u0272\u027a\u0281\u0287")
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
                      "INTEGER_LITERAL", "STRING_LITERAL", "ILLEGAL_ESCAPE", 
                      "UNCLOSE_STRING", "REAL_LITERAL", "NORMAL_ID", "DOLLAR_ID", 
                      "BLOCK_COMMENT", "WS", "ERROR_CHAR" ]

    RULE_program = 0
    RULE_class_program = 1
    RULE_class_declares_list = 2
    RULE_class_declares = 3
    RULE_class_declare = 4
    RULE_extend = 5
    RULE_class_members = 6
    RULE_member_list = 7
    RULE_members = 8
    RULE_member = 9
    RULE_main_method = 10
    RULE_constructor_method = 11
    RULE_destructor_method = 12
    RULE_block_des_statements = 13
    RULE_des_statements_list = 14
    RULE_des_statements = 15
    RULE_des_statement = 16
    RULE_method_declare = 17
    RULE_param_list = 18
    RULE_parameters = 19
    RULE_parameter = 20
    RULE_block_statements = 21
    RULE_statements_list = 22
    RULE_statements = 23
    RULE_statement = 24
    RULE_break_statement = 25
    RULE_continue_statement = 26
    RULE_return_statement = 27
    RULE_assign_statement = 28
    RULE_if_else_statement = 29
    RULE_elseif_stmt_list = 30
    RULE_elseif_stmts = 31
    RULE_elseif_stmt = 32
    RULE_else_stmt = 33
    RULE_foreach_statement = 34
    RULE_increment = 35
    RULE_lhs = 36
    RULE_index = 37
    RULE_static_attr_call = 38
    RULE_static_method_call = 39
    RULE_instance_attr_call = 40
    RULE_instance_method_call = 41
    RULE_var_declare = 42
    RULE_dec_and_init_list = 43
    RULE_pair = 44
    RULE_array_type = 45
    RULE_array_literal = 46
    RULE_literal_list = 47
    RULE_literals = 48
    RULE_exp = 49
    RULE_exp0 = 50
    RULE_exp1 = 51
    RULE_exp2 = 52
    RULE_exp3 = 53
    RULE_exp4 = 54
    RULE_exp5 = 55
    RULE_exp6 = 56
    RULE_index_operator = 57
    RULE_exp7 = 58
    RULE_exp8 = 59
    RULE_exp9 = 60
    RULE_exp10 = 61
    RULE_exp11 = 62
    RULE_list_exp = 63
    RULE_exps = 64
    RULE_id_list = 65

    ruleNames =  [ "program", "class_program", "class_declares_list", "class_declares", 
                   "class_declare", "extend", "class_members", "member_list", 
                   "members", "member", "main_method", "constructor_method", 
                   "destructor_method", "block_des_statements", "des_statements_list", 
                   "des_statements", "des_statement", "method_declare", 
                   "param_list", "parameters", "parameter", "block_statements", 
                   "statements_list", "statements", "statement", "break_statement", 
                   "continue_statement", "return_statement", "assign_statement", 
                   "if_else_statement", "elseif_stmt_list", "elseif_stmts", 
                   "elseif_stmt", "else_stmt", "foreach_statement", "increment", 
                   "lhs", "index", "static_attr_call", "static_method_call", 
                   "instance_attr_call", "instance_method_call", "var_declare", 
                   "dec_and_init_list", "pair", "array_type", "array_literal", 
                   "literal_list", "literals", "exp", "exp0", "exp1", "exp2", 
                   "exp3", "exp4", "exp5", "exp6", "index_operator", "exp7", 
                   "exp8", "exp9", "exp10", "exp11", "list_exp", "exps", 
                   "id_list" ]

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
    INTEGER_LITERAL=57
    STRING_LITERAL=58
    ILLEGAL_ESCAPE=59
    UNCLOSE_STRING=60
    REAL_LITERAL=61
    NORMAL_ID=62
    DOLLAR_ID=63
    BLOCK_COMMENT=64
    WS=65
    ERROR_CHAR=66

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

        def instance_attr_call(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(D96Parser.Instance_attr_callContext)
            else:
                return self.getTypedRuleContext(D96Parser.Instance_attr_callContext,i)


        def exp(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(D96Parser.ExpContext)
            else:
                return self.getTypedRuleContext(D96Parser.ExpContext,i)


        def assign_statement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(D96Parser.Assign_statementContext)
            else:
                return self.getTypedRuleContext(D96Parser.Assign_statementContext,i)


        def getRuleIndex(self):
            return D96Parser.RULE_program




    def program(self):

        localctx = D96Parser.ProgramContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_program)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 135 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 135
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,0,self._ctx)
                if la_ == 1:
                    self.state = 132
                    self.instance_attr_call()
                    pass

                elif la_ == 2:
                    self.state = 133
                    self.exp()
                    pass

                elif la_ == 3:
                    self.state = 134
                    self.assign_statement()
                    pass


                self.state = 137 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << D96Parser.LP) | (1 << D96Parser.ARRAY) | (1 << D96Parser.NEW) | (1 << D96Parser.SELF) | (1 << D96Parser.SUB) | (1 << D96Parser.NOT) | (1 << D96Parser.BOOL_LITERAL) | (1 << D96Parser.INTEGER_LITERAL) | (1 << D96Parser.STRING_LITERAL) | (1 << D96Parser.REAL_LITERAL) | (1 << D96Parser.NORMAL_ID) | (1 << D96Parser.DOLLAR_ID))) != 0)):
                    break

            self.state = 139
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

        def PROGRAM(self):
            return self.getToken(D96Parser.PROGRAM, 0)

        def class_members(self):
            return self.getTypedRuleContext(D96Parser.Class_membersContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_class_program




    def class_program(self):

        localctx = D96Parser.Class_programContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_class_program)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 141
            self.match(D96Parser.CLASS)
            self.state = 142
            self.match(D96Parser.PROGRAM)
            self.state = 143
            self.class_members()
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

        def class_declares(self):
            return self.getTypedRuleContext(D96Parser.Class_declaresContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_class_declares_list




    def class_declares_list(self):

        localctx = D96Parser.Class_declares_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_class_declares_list)
        try:
            self.state = 147
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [D96Parser.CLASS]:
                self.enterOuterAlt(localctx, 1)
                self.state = 145
                self.class_declares()
                pass
            elif token in [D96Parser.EOF]:
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


    class Class_declaresContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def class_declare(self):
            return self.getTypedRuleContext(D96Parser.Class_declareContext,0)


        def class_declares(self):
            return self.getTypedRuleContext(D96Parser.Class_declaresContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_class_declares




    def class_declares(self):

        localctx = D96Parser.Class_declaresContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_class_declares)
        try:
            self.state = 153
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,3,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 149
                self.class_declare()
                self.state = 150
                self.class_declares()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 152
                self.class_declare()
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
        self.enterRule(localctx, 8, self.RULE_class_declare)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 155
            self.match(D96Parser.CLASS)
            self.state = 156
            self.match(D96Parser.NORMAL_ID)
            self.state = 157
            self.extend()
            self.state = 158
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
        self.enterRule(localctx, 10, self.RULE_extend)
        try:
            self.state = 163
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [D96Parser.COLON]:
                self.enterOuterAlt(localctx, 1)
                self.state = 160
                self.match(D96Parser.COLON)
                self.state = 161
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
        self.enterRule(localctx, 12, self.RULE_class_members)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 165
            self.match(D96Parser.LCB)
            self.state = 166
            self.member_list()
            self.state = 167
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
        self.enterRule(localctx, 14, self.RULE_member_list)
        try:
            self.state = 171
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [D96Parser.VAL, D96Parser.VAR, D96Parser.CONSTRUCTOR, D96Parser.DESTRUCTOR, D96Parser.MAIN, D96Parser.NORMAL_ID, D96Parser.DOLLAR_ID]:
                self.enterOuterAlt(localctx, 1)
                self.state = 169
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
        self.enterRule(localctx, 16, self.RULE_members)
        try:
            self.state = 177
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,6,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 173
                self.member()
                self.state = 174
                self.members()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 176
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




    def member(self):

        localctx = D96Parser.MemberContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_member)
        try:
            self.state = 184
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [D96Parser.VAL, D96Parser.VAR]:
                self.enterOuterAlt(localctx, 1)
                self.state = 179
                self.var_declare()
                pass
            elif token in [D96Parser.CONSTRUCTOR]:
                self.enterOuterAlt(localctx, 2)
                self.state = 180
                self.constructor_method()
                pass
            elif token in [D96Parser.DESTRUCTOR]:
                self.enterOuterAlt(localctx, 3)
                self.state = 181
                self.destructor_method()
                pass
            elif token in [D96Parser.MAIN]:
                self.enterOuterAlt(localctx, 4)
                self.state = 182
                self.main_method()
                pass
            elif token in [D96Parser.NORMAL_ID, D96Parser.DOLLAR_ID]:
                self.enterOuterAlt(localctx, 5)
                self.state = 183
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




    def main_method(self):

        localctx = D96Parser.Main_methodContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_main_method)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 186
            self.match(D96Parser.MAIN)
            self.state = 187
            self.match(D96Parser.LP)
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
        self.enterRule(localctx, 22, self.RULE_constructor_method)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 191
            self.match(D96Parser.CONSTRUCTOR)
            self.state = 192
            self.match(D96Parser.LP)
            self.state = 193
            self.param_list()
            self.state = 194
            self.match(D96Parser.RP)
            self.state = 195
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

        def block_des_statements(self):
            return self.getTypedRuleContext(D96Parser.Block_des_statementsContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_destructor_method




    def destructor_method(self):

        localctx = D96Parser.Destructor_methodContext(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_destructor_method)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 197
            self.match(D96Parser.DESTRUCTOR)
            self.state = 198
            self.match(D96Parser.LP)
            self.state = 199
            self.match(D96Parser.RP)
            self.state = 200
            self.block_des_statements()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Block_des_statementsContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LCB(self):
            return self.getToken(D96Parser.LCB, 0)

        def des_statements_list(self):
            return self.getTypedRuleContext(D96Parser.Des_statements_listContext,0)


        def RCB(self):
            return self.getToken(D96Parser.RCB, 0)

        def getRuleIndex(self):
            return D96Parser.RULE_block_des_statements




    def block_des_statements(self):

        localctx = D96Parser.Block_des_statementsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 26, self.RULE_block_des_statements)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 202
            self.match(D96Parser.LCB)
            self.state = 203
            self.des_statements_list()
            self.state = 204
            self.match(D96Parser.RCB)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Des_statements_listContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def des_statements(self):
            return self.getTypedRuleContext(D96Parser.Des_statementsContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_des_statements_list




    def des_statements_list(self):

        localctx = D96Parser.Des_statements_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 28, self.RULE_des_statements_list)
        try:
            self.state = 208
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [D96Parser.VAL, D96Parser.VAR, D96Parser.LP, D96Parser.BREAK, D96Parser.CONTINUE, D96Parser.IF, D96Parser.FOREACH, D96Parser.ARRAY, D96Parser.NEW, D96Parser.SELF, D96Parser.SUB, D96Parser.NOT, D96Parser.BOOL_LITERAL, D96Parser.INTEGER_LITERAL, D96Parser.STRING_LITERAL, D96Parser.REAL_LITERAL, D96Parser.NORMAL_ID, D96Parser.DOLLAR_ID]:
                self.enterOuterAlt(localctx, 1)
                self.state = 206
                self.des_statements()
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


    class Des_statementsContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def des_statement(self):
            return self.getTypedRuleContext(D96Parser.Des_statementContext,0)


        def des_statements(self):
            return self.getTypedRuleContext(D96Parser.Des_statementsContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_des_statements




    def des_statements(self):

        localctx = D96Parser.Des_statementsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 30, self.RULE_des_statements)
        try:
            self.state = 214
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,9,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 210
                self.des_statement()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 211
                self.des_statement()
                self.state = 212
                self.des_statements()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Des_statementContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def var_declare(self):
            return self.getTypedRuleContext(D96Parser.Var_declareContext,0)


        def assign_statement(self):
            return self.getTypedRuleContext(D96Parser.Assign_statementContext,0)


        def break_statement(self):
            return self.getTypedRuleContext(D96Parser.Break_statementContext,0)


        def continue_statement(self):
            return self.getTypedRuleContext(D96Parser.Continue_statementContext,0)


        def instance_method_call(self):
            return self.getTypedRuleContext(D96Parser.Instance_method_callContext,0)


        def SEMI(self):
            return self.getToken(D96Parser.SEMI, 0)

        def static_method_call(self):
            return self.getTypedRuleContext(D96Parser.Static_method_callContext,0)


        def instance_attr_call(self):
            return self.getTypedRuleContext(D96Parser.Instance_attr_callContext,0)


        def if_else_statement(self):
            return self.getTypedRuleContext(D96Parser.If_else_statementContext,0)


        def foreach_statement(self):
            return self.getTypedRuleContext(D96Parser.Foreach_statementContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_des_statement




    def des_statement(self):

        localctx = D96Parser.Des_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 32, self.RULE_des_statement)
        try:
            self.state = 234
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,10,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 216
                self.var_declare()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 217
                self.assign_statement()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 218
                self.break_statement()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 219
                self.continue_statement()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 220
                self.instance_method_call()
                self.state = 221
                self.match(D96Parser.SEMI)
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 223
                self.static_method_call()
                self.state = 224
                self.match(D96Parser.SEMI)
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 226
                self.instance_attr_call()
                self.state = 227
                self.match(D96Parser.SEMI)
                pass

            elif la_ == 8:
                self.enterOuterAlt(localctx, 8)
                self.state = 229
                self.instance_method_call()
                self.state = 230
                self.match(D96Parser.SEMI)
                pass

            elif la_ == 9:
                self.enterOuterAlt(localctx, 9)
                self.state = 232
                self.if_else_statement()
                pass

            elif la_ == 10:
                self.enterOuterAlt(localctx, 10)
                self.state = 233
                self.foreach_statement()
                pass


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
        self.enterRule(localctx, 34, self.RULE_method_declare)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 236
            _la = self._input.LA(1)
            if not(_la==D96Parser.NORMAL_ID or _la==D96Parser.DOLLAR_ID):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 237
            self.match(D96Parser.LP)
            self.state = 238
            self.param_list()
            self.state = 239
            self.match(D96Parser.RP)
            self.state = 240
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
        self.enterRule(localctx, 36, self.RULE_param_list)
        try:
            self.state = 244
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [D96Parser.NORMAL_ID, D96Parser.DOLLAR_ID]:
                self.enterOuterAlt(localctx, 1)
                self.state = 242
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
        self.enterRule(localctx, 38, self.RULE_parameters)
        try:
            self.state = 251
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,12,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 246
                self.parameter()
                self.state = 247
                self.match(D96Parser.SEMI)
                self.state = 248
                self.parameters()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 250
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

        def id_list(self):
            return self.getTypedRuleContext(D96Parser.Id_listContext,0)


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
        self.enterRule(localctx, 40, self.RULE_parameter)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 253
            self.id_list()
            self.state = 254
            self.match(D96Parser.COLON)
            self.state = 261
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [D96Parser.BOOLEAN]:
                self.state = 255
                self.match(D96Parser.BOOLEAN)
                pass
            elif token in [D96Parser.INT_TYPE]:
                self.state = 256
                self.match(D96Parser.INT_TYPE)
                pass
            elif token in [D96Parser.FLOAT_TYPE]:
                self.state = 257
                self.match(D96Parser.FLOAT_TYPE)
                pass
            elif token in [D96Parser.ARRAY]:
                self.state = 258
                self.array_type()
                pass
            elif token in [D96Parser.STRING]:
                self.state = 259
                self.match(D96Parser.STRING)
                pass
            elif token in [D96Parser.NORMAL_ID]:
                self.state = 260
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
        self.enterRule(localctx, 42, self.RULE_block_statements)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 263
            self.match(D96Parser.LCB)
            self.state = 264
            self.statements_list()
            self.state = 265
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
        self.enterRule(localctx, 44, self.RULE_statements_list)
        try:
            self.state = 269
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [D96Parser.VAL, D96Parser.VAR, D96Parser.LP, D96Parser.BREAK, D96Parser.CONTINUE, D96Parser.IF, D96Parser.FOREACH, D96Parser.ARRAY, D96Parser.RETURN, D96Parser.NEW, D96Parser.SELF, D96Parser.SUB, D96Parser.NOT, D96Parser.BOOL_LITERAL, D96Parser.INTEGER_LITERAL, D96Parser.STRING_LITERAL, D96Parser.REAL_LITERAL, D96Parser.NORMAL_ID, D96Parser.DOLLAR_ID]:
                self.enterOuterAlt(localctx, 1)
                self.state = 267
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
        self.enterRule(localctx, 46, self.RULE_statements)
        try:
            self.state = 275
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,15,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 271
                self.statement()
                self.state = 272
                self.statements()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 274
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




    def statement(self):

        localctx = D96Parser.StatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 48, self.RULE_statement)
        try:
            self.state = 296
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,16,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 277
                self.assign_statement()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 278
                self.var_declare()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 279
                self.break_statement()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 280
                self.continue_statement()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 281
                self.return_statement()
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 282
                self.instance_method_call()
                self.state = 283
                self.match(D96Parser.SEMI)
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 285
                self.instance_attr_call()
                self.state = 286
                self.match(D96Parser.SEMI)
                pass

            elif la_ == 8:
                self.enterOuterAlt(localctx, 8)
                self.state = 288
                self.static_attr_call()
                self.state = 289
                self.match(D96Parser.SEMI)
                pass

            elif la_ == 9:
                self.enterOuterAlt(localctx, 9)
                self.state = 291
                self.static_method_call()
                self.state = 292
                self.match(D96Parser.SEMI)
                pass

            elif la_ == 10:
                self.enterOuterAlt(localctx, 10)
                self.state = 294
                self.if_else_statement()
                pass

            elif la_ == 11:
                self.enterOuterAlt(localctx, 11)
                self.state = 295
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
        self.enterRule(localctx, 50, self.RULE_break_statement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 298
            self.match(D96Parser.BREAK)
            self.state = 299
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
        self.enterRule(localctx, 52, self.RULE_continue_statement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 301
            self.match(D96Parser.CONTINUE)
            self.state = 302
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

        def SEMI(self):
            return self.getToken(D96Parser.SEMI, 0)

        def exp(self):
            return self.getTypedRuleContext(D96Parser.ExpContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_return_statement




    def return_statement(self):

        localctx = D96Parser.Return_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 54, self.RULE_return_statement)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 304
            self.match(D96Parser.RETURN)
            self.state = 306
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << D96Parser.LP) | (1 << D96Parser.ARRAY) | (1 << D96Parser.NEW) | (1 << D96Parser.SELF) | (1 << D96Parser.SUB) | (1 << D96Parser.NOT) | (1 << D96Parser.BOOL_LITERAL) | (1 << D96Parser.INTEGER_LITERAL) | (1 << D96Parser.STRING_LITERAL) | (1 << D96Parser.REAL_LITERAL) | (1 << D96Parser.NORMAL_ID) | (1 << D96Parser.DOLLAR_ID))) != 0):
                self.state = 305
                self.exp()


            self.state = 308
            self.match(D96Parser.SEMI)
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
        self.enterRule(localctx, 56, self.RULE_assign_statement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 310
            self.lhs()
            self.state = 311
            self.match(D96Parser.ASSIGN)
            self.state = 312
            self.exp()
            self.state = 313
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
        self.enterRule(localctx, 58, self.RULE_if_else_statement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 315
            self.match(D96Parser.IF)
            self.state = 316
            self.match(D96Parser.LP)
            self.state = 317
            self.exp()
            self.state = 318
            self.match(D96Parser.RP)
            self.state = 319
            self.block_statements()
            self.state = 320
            self.elseif_stmt_list()
            self.state = 321
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
        self.enterRule(localctx, 60, self.RULE_elseif_stmt_list)
        try:
            self.state = 325
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [D96Parser.ELSEIF]:
                self.enterOuterAlt(localctx, 1)
                self.state = 323
                self.elseif_stmts()
                pass
            elif token in [D96Parser.VAL, D96Parser.VAR, D96Parser.LP, D96Parser.RCB, D96Parser.BREAK, D96Parser.CONTINUE, D96Parser.IF, D96Parser.ELSE, D96Parser.FOREACH, D96Parser.ARRAY, D96Parser.RETURN, D96Parser.NEW, D96Parser.SELF, D96Parser.SUB, D96Parser.NOT, D96Parser.BOOL_LITERAL, D96Parser.INTEGER_LITERAL, D96Parser.STRING_LITERAL, D96Parser.REAL_LITERAL, D96Parser.NORMAL_ID, D96Parser.DOLLAR_ID]:
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
        self.enterRule(localctx, 62, self.RULE_elseif_stmts)
        try:
            self.state = 331
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,19,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 327
                self.elseif_stmt()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 328
                self.elseif_stmt()
                self.state = 329
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
        self.enterRule(localctx, 64, self.RULE_elseif_stmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 333
            self.match(D96Parser.ELSEIF)
            self.state = 334
            self.match(D96Parser.LP)
            self.state = 335
            self.exp()
            self.state = 336
            self.match(D96Parser.RP)
            self.state = 337
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
        self.enterRule(localctx, 66, self.RULE_else_stmt)
        try:
            self.state = 342
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [D96Parser.ELSE]:
                self.enterOuterAlt(localctx, 1)
                self.state = 339
                self.match(D96Parser.ELSE)
                self.state = 340
                self.block_statements()
                pass
            elif token in [D96Parser.VAL, D96Parser.VAR, D96Parser.LP, D96Parser.RCB, D96Parser.BREAK, D96Parser.CONTINUE, D96Parser.IF, D96Parser.FOREACH, D96Parser.ARRAY, D96Parser.RETURN, D96Parser.NEW, D96Parser.SELF, D96Parser.SUB, D96Parser.NOT, D96Parser.BOOL_LITERAL, D96Parser.INTEGER_LITERAL, D96Parser.STRING_LITERAL, D96Parser.REAL_LITERAL, D96Parser.NORMAL_ID, D96Parser.DOLLAR_ID]:
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

        def DOLLAR_ID(self):
            return self.getToken(D96Parser.DOLLAR_ID, 0)

        def getRuleIndex(self):
            return D96Parser.RULE_foreach_statement




    def foreach_statement(self):

        localctx = D96Parser.Foreach_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 68, self.RULE_foreach_statement)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 344
            self.match(D96Parser.FOREACH)
            self.state = 345
            self.match(D96Parser.LP)
            self.state = 346
            _la = self._input.LA(1)
            if not(_la==D96Parser.NORMAL_ID or _la==D96Parser.DOLLAR_ID):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 347
            self.match(D96Parser.IN)
            self.state = 348
            self.exp()
            self.state = 349
            self.match(D96Parser.DOTDOT)
            self.state = 350
            self.exp()
            self.state = 351
            self.increment()
            self.state = 352
            self.match(D96Parser.RP)
            self.state = 353
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
        self.enterRule(localctx, 70, self.RULE_increment)
        try:
            self.state = 358
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [D96Parser.BY]:
                self.enterOuterAlt(localctx, 1)
                self.state = 355
                self.match(D96Parser.BY)
                self.state = 356
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

        def DOLLAR_ID(self):
            return self.getToken(D96Parser.DOLLAR_ID, 0)

        def index(self):
            return self.getTypedRuleContext(D96Parser.IndexContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_lhs




    def lhs(self):

        localctx = D96Parser.LhsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 72, self.RULE_lhs)
        try:
            self.state = 363
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,22,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 360
                self.match(D96Parser.NORMAL_ID)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 361
                self.match(D96Parser.DOLLAR_ID)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 362
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
        self.enterRule(localctx, 74, self.RULE_index)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 365
            _la = self._input.LA(1)
            if not(_la==D96Parser.NORMAL_ID or _la==D96Parser.DOLLAR_ID):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 366
            self.index_operator()
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
        self.enterRule(localctx, 76, self.RULE_static_attr_call)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 368
            self.match(D96Parser.NORMAL_ID)
            self.state = 369
            self.match(D96Parser.SCOPE)
            self.state = 370
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
        self.enterRule(localctx, 78, self.RULE_static_method_call)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 372
            self.match(D96Parser.NORMAL_ID)
            self.state = 373
            self.match(D96Parser.SCOPE)
            self.state = 374
            self.match(D96Parser.DOLLAR_ID)
            self.state = 375
            self.match(D96Parser.LP)
            self.state = 376
            self.list_exp()
            self.state = 377
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

        def exp(self):
            return self.getTypedRuleContext(D96Parser.ExpContext,0)


        def DOT(self):
            return self.getToken(D96Parser.DOT, 0)

        def NORMAL_ID(self):
            return self.getToken(D96Parser.NORMAL_ID, 0)

        def DOLLAR_ID(self):
            return self.getToken(D96Parser.DOLLAR_ID, 0)

        def getRuleIndex(self):
            return D96Parser.RULE_instance_attr_call




    def instance_attr_call(self):

        localctx = D96Parser.Instance_attr_callContext(self, self._ctx, self.state)
        self.enterRule(localctx, 80, self.RULE_instance_attr_call)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 379
            self.exp()
            self.state = 380
            self.match(D96Parser.DOT)
            self.state = 381
            _la = self._input.LA(1)
            if not(_la==D96Parser.NORMAL_ID or _la==D96Parser.DOLLAR_ID):
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


    class Instance_method_callContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def exp(self):
            return self.getTypedRuleContext(D96Parser.ExpContext,0)


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
        self.enterRule(localctx, 82, self.RULE_instance_method_call)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 383
            self.exp()
            self.state = 384
            self.match(D96Parser.DOT)
            self.state = 385
            self.match(D96Parser.NORMAL_ID)
            self.state = 386
            self.match(D96Parser.LP)
            self.state = 387
            self.list_exp()
            self.state = 388
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




    def var_declare(self):

        localctx = D96Parser.Var_declareContext(self, self._ctx, self.state)
        self.enterRule(localctx, 84, self.RULE_var_declare)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 390
            _la = self._input.LA(1)
            if not(_la==D96Parser.VAL or _la==D96Parser.VAR):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 391
            self.dec_and_init_list()
            self.state = 392
            self.match(D96Parser.SEMI)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Dec_and_init_listContext(ParserRuleContext):

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

        def id_list(self):
            return self.getTypedRuleContext(D96Parser.Id_listContext,0)


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
            return D96Parser.RULE_dec_and_init_list




    def dec_and_init_list(self):

        localctx = D96Parser.Dec_and_init_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 86, self.RULE_dec_and_init_list)
        self._la = 0 # Token type
        try:
            self.state = 408
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,24,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 394
                _la = self._input.LA(1)
                if not(_la==D96Parser.NORMAL_ID or _la==D96Parser.DOLLAR_ID):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 395
                self.pair()
                self.state = 396
                self.exp()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 398
                self.id_list()
                self.state = 399
                self.match(D96Parser.COLON)
                self.state = 406
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [D96Parser.BOOLEAN]:
                    self.state = 400
                    self.match(D96Parser.BOOLEAN)
                    pass
                elif token in [D96Parser.INT_TYPE]:
                    self.state = 401
                    self.match(D96Parser.INT_TYPE)
                    pass
                elif token in [D96Parser.FLOAT_TYPE]:
                    self.state = 402
                    self.match(D96Parser.FLOAT_TYPE)
                    pass
                elif token in [D96Parser.ARRAY]:
                    self.state = 403
                    self.array_type()
                    pass
                elif token in [D96Parser.STRING]:
                    self.state = 404
                    self.match(D96Parser.STRING)
                    pass
                elif token in [D96Parser.NORMAL_ID]:
                    self.state = 405
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




    def pair(self):

        localctx = D96Parser.PairContext(self, self._ctx, self.state)
        self.enterRule(localctx, 88, self.RULE_pair)
        self._la = 0 # Token type
        try:
            self.state = 426
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [D96Parser.COMMA]:
                self.enterOuterAlt(localctx, 1)
                self.state = 410
                self.match(D96Parser.COMMA)
                self.state = 411
                _la = self._input.LA(1)
                if not(_la==D96Parser.NORMAL_ID or _la==D96Parser.DOLLAR_ID):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 412
                self.pair()
                self.state = 413
                self.exp()
                self.state = 414
                self.match(D96Parser.COMMA)
                pass
            elif token in [D96Parser.COLON]:
                self.enterOuterAlt(localctx, 2)
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

                self.state = 425
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

        def INTEGER_LITERAL(self):
            return self.getToken(D96Parser.INTEGER_LITERAL, 0)

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




    def array_type(self):

        localctx = D96Parser.Array_typeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 90, self.RULE_array_type)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 428
            self.match(D96Parser.ARRAY)
            self.state = 429
            self.match(D96Parser.LSB)
            self.state = 436
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [D96Parser.BOOLEAN]:
                self.state = 430
                self.match(D96Parser.BOOLEAN)
                pass
            elif token in [D96Parser.INT_TYPE]:
                self.state = 431
                self.match(D96Parser.INT_TYPE)
                pass
            elif token in [D96Parser.FLOAT_TYPE]:
                self.state = 432
                self.match(D96Parser.FLOAT_TYPE)
                pass
            elif token in [D96Parser.ARRAY]:
                self.state = 433
                self.array_type()
                pass
            elif token in [D96Parser.STRING]:
                self.state = 434
                self.match(D96Parser.STRING)
                pass
            elif token in [D96Parser.NORMAL_ID]:
                self.state = 435
                self.match(D96Parser.NORMAL_ID)
                pass
            else:
                raise NoViableAltException(self)

            self.state = 438
            self.match(D96Parser.COMMA)
            self.state = 439
            self.match(D96Parser.INTEGER_LITERAL)
            self.state = 440
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
        self.enterRule(localctx, 92, self.RULE_array_literal)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 442
            self.match(D96Parser.ARRAY)
            self.state = 443
            self.match(D96Parser.LP)
            self.state = 444
            self.literal_list()
            self.state = 445
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
        self.enterRule(localctx, 94, self.RULE_literal_list)
        try:
            self.state = 449
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [D96Parser.LP, D96Parser.ARRAY, D96Parser.NEW, D96Parser.SELF, D96Parser.SUB, D96Parser.NOT, D96Parser.BOOL_LITERAL, D96Parser.INTEGER_LITERAL, D96Parser.STRING_LITERAL, D96Parser.REAL_LITERAL, D96Parser.NORMAL_ID, D96Parser.DOLLAR_ID]:
                self.enterOuterAlt(localctx, 1)
                self.state = 447
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
        self.enterRule(localctx, 96, self.RULE_literals)
        try:
            self.state = 456
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,29,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 451
                self.exp()
                self.state = 452
                self.match(D96Parser.COMMA)
                self.state = 453
                self.literals()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 455
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
        self.enterRule(localctx, 98, self.RULE_exp)
        try:
            self.state = 467
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,30,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 458
                self.exp0()
                self.state = 459
                self.match(D96Parser.EQUAL_STR)
                self.state = 460
                self.exp0()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 462
                self.exp0()
                self.state = 463
                self.match(D96Parser.ADD_STR)
                self.state = 464
                self.exp0()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 466
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
        self.enterRule(localctx, 100, self.RULE_exp0)
        try:
            self.state = 494
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,31,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 469
                self.exp1(0)
                self.state = 470
                self.match(D96Parser.LT)
                self.state = 471
                self.exp1(0)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 473
                self.exp1(0)
                self.state = 474
                self.match(D96Parser.LTE)
                self.state = 475
                self.exp1(0)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 477
                self.exp1(0)
                self.state = 478
                self.match(D96Parser.GT)
                self.state = 479
                self.exp1(0)
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 481
                self.exp1(0)
                self.state = 482
                self.match(D96Parser.EQUAL)
                self.state = 483
                self.exp1(0)
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 485
                self.exp1(0)
                self.state = 486
                self.match(D96Parser.NOTEQUAL)
                self.state = 487
                self.exp1(0)
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 489
                self.exp1(0)
                self.state = 490
                self.match(D96Parser.GTE)
                self.state = 491
                self.exp1(0)
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 493
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
        _startState = 102
        self.enterRecursionRule(localctx, 102, self.RULE_exp1, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 497
            self.exp2(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 507
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,33,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 505
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,32,self._ctx)
                    if la_ == 1:
                        localctx = D96Parser.Exp1Context(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_exp1)
                        self.state = 499
                        if not self.precpred(self._ctx, 3):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 3)")
                        self.state = 500
                        self.match(D96Parser.AND)
                        self.state = 501
                        self.exp2(0)
                        pass

                    elif la_ == 2:
                        localctx = D96Parser.Exp1Context(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_exp1)
                        self.state = 502
                        if not self.precpred(self._ctx, 2):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                        self.state = 503
                        self.match(D96Parser.OR)
                        self.state = 504
                        self.exp2(0)
                        pass

             
                self.state = 509
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,33,self._ctx)

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
        _startState = 104
        self.enterRecursionRule(localctx, 104, self.RULE_exp2, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 511
            self.exp3(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 521
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,35,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 519
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,34,self._ctx)
                    if la_ == 1:
                        localctx = D96Parser.Exp2Context(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_exp2)
                        self.state = 513
                        if not self.precpred(self._ctx, 3):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 3)")
                        self.state = 514
                        self.match(D96Parser.ADD)
                        self.state = 515
                        self.exp3(0)
                        pass

                    elif la_ == 2:
                        localctx = D96Parser.Exp2Context(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_exp2)
                        self.state = 516
                        if not self.precpred(self._ctx, 2):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                        self.state = 517
                        self.match(D96Parser.SUB)
                        self.state = 518
                        self.exp3(0)
                        pass

             
                self.state = 523
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,35,self._ctx)

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
        _startState = 106
        self.enterRecursionRule(localctx, 106, self.RULE_exp3, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 525
            self.exp4()
            self._ctx.stop = self._input.LT(-1)
            self.state = 538
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,37,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 536
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,36,self._ctx)
                    if la_ == 1:
                        localctx = D96Parser.Exp3Context(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_exp3)
                        self.state = 527
                        if not self.precpred(self._ctx, 4):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 4)")
                        self.state = 528
                        self.match(D96Parser.MUL)
                        self.state = 529
                        self.exp4()
                        pass

                    elif la_ == 2:
                        localctx = D96Parser.Exp3Context(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_exp3)
                        self.state = 530
                        if not self.precpred(self._ctx, 3):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 3)")
                        self.state = 531
                        self.match(D96Parser.DIV)
                        self.state = 532
                        self.exp4()
                        pass

                    elif la_ == 3:
                        localctx = D96Parser.Exp3Context(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_exp3)
                        self.state = 533
                        if not self.precpred(self._ctx, 2):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                        self.state = 534
                        self.match(D96Parser.MOD)
                        self.state = 535
                        self.exp4()
                        pass

             
                self.state = 540
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,37,self._ctx)

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
        self.enterRule(localctx, 108, self.RULE_exp4)
        try:
            self.state = 544
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [D96Parser.NOT]:
                self.enterOuterAlt(localctx, 1)
                self.state = 541
                self.match(D96Parser.NOT)
                self.state = 542
                self.exp4()
                pass
            elif token in [D96Parser.LP, D96Parser.ARRAY, D96Parser.NEW, D96Parser.SELF, D96Parser.SUB, D96Parser.BOOL_LITERAL, D96Parser.INTEGER_LITERAL, D96Parser.STRING_LITERAL, D96Parser.REAL_LITERAL, D96Parser.NORMAL_ID, D96Parser.DOLLAR_ID]:
                self.enterOuterAlt(localctx, 2)
                self.state = 543
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
        self.enterRule(localctx, 110, self.RULE_exp5)
        try:
            self.state = 549
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [D96Parser.SUB]:
                self.enterOuterAlt(localctx, 1)
                self.state = 546
                self.match(D96Parser.SUB)
                self.state = 547
                self.exp5()
                pass
            elif token in [D96Parser.LP, D96Parser.ARRAY, D96Parser.NEW, D96Parser.SELF, D96Parser.BOOL_LITERAL, D96Parser.INTEGER_LITERAL, D96Parser.STRING_LITERAL, D96Parser.REAL_LITERAL, D96Parser.NORMAL_ID, D96Parser.DOLLAR_ID]:
                self.enterOuterAlt(localctx, 2)
                self.state = 548
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
        _startState = 112
        self.enterRecursionRule(localctx, 112, self.RULE_exp6, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 552
            self.exp7(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 561
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,40,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = D96Parser.Exp6Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_exp6)
                    self.state = 554
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 555
                    self.match(D96Parser.LSB)
                    self.state = 556
                    self.exp()
                    self.state = 557
                    self.match(D96Parser.RSB) 
                self.state = 563
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,40,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
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
        self.enterRule(localctx, 114, self.RULE_index_operator)
        try:
            self.state = 573
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,41,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 564
                self.match(D96Parser.LSB)
                self.state = 565
                self.exp()
                self.state = 566
                self.match(D96Parser.RSB)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 568
                self.match(D96Parser.LSB)
                self.state = 569
                self.exp()
                self.state = 570
                self.match(D96Parser.RSB)
                self.state = 571
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
            return D96Parser.RULE_exp7



    def exp7(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = D96Parser.Exp7Context(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 116
        self.enterRecursionRule(localctx, 116, self.RULE_exp7, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 576
            self.exp8()
            self._ctx.stop = self._input.LT(-1)
            self.state = 590
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,43,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 588
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,42,self._ctx)
                    if la_ == 1:
                        localctx = D96Parser.Exp7Context(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_exp7)
                        self.state = 578
                        if not self.precpred(self._ctx, 3):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 3)")
                        self.state = 579
                        self.match(D96Parser.DOT)
                        self.state = 580
                        _la = self._input.LA(1)
                        if not(_la==D96Parser.NORMAL_ID or _la==D96Parser.DOLLAR_ID):
                            self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 581
                        self.match(D96Parser.LP)
                        self.state = 582
                        self.list_exp()
                        self.state = 583
                        self.match(D96Parser.RP)
                        pass

                    elif la_ == 2:
                        localctx = D96Parser.Exp7Context(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_exp7)
                        self.state = 585
                        if not self.precpred(self._ctx, 2):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                        self.state = 586
                        self.match(D96Parser.DOT)
                        self.state = 587
                        _la = self._input.LA(1)
                        if not(_la==D96Parser.NORMAL_ID or _la==D96Parser.DOLLAR_ID):
                            self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        pass

             
                self.state = 592
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,43,self._ctx)

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
        self.enterRule(localctx, 118, self.RULE_exp8)
        try:
            self.state = 604
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,44,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 593
                self.match(D96Parser.NORMAL_ID)
                self.state = 594
                self.match(D96Parser.SCOPE)
                self.state = 595
                self.match(D96Parser.DOLLAR_ID)
                self.state = 596
                self.match(D96Parser.LP)
                self.state = 597
                self.list_exp()
                self.state = 598
                self.match(D96Parser.RP)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 600
                self.match(D96Parser.NORMAL_ID)
                self.state = 601
                self.match(D96Parser.SCOPE)
                self.state = 602
                self.match(D96Parser.DOLLAR_ID)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 603
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




    def exp9(self):

        localctx = D96Parser.Exp9Context(self, self._ctx, self.state)
        self.enterRule(localctx, 120, self.RULE_exp9)
        try:
            self.state = 613
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [D96Parser.NEW]:
                self.enterOuterAlt(localctx, 1)
                self.state = 606
                self.match(D96Parser.NEW)
                self.state = 607
                self.exp9()
                self.state = 608
                self.match(D96Parser.LP)
                self.state = 609
                self.list_exp()
                self.state = 610
                self.match(D96Parser.RP)
                pass
            elif token in [D96Parser.LP, D96Parser.ARRAY, D96Parser.SELF, D96Parser.BOOL_LITERAL, D96Parser.INTEGER_LITERAL, D96Parser.STRING_LITERAL, D96Parser.REAL_LITERAL, D96Parser.NORMAL_ID, D96Parser.DOLLAR_ID]:
                self.enterOuterAlt(localctx, 2)
                self.state = 612
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




    def exp10(self):

        localctx = D96Parser.Exp10Context(self, self._ctx, self.state)
        self.enterRule(localctx, 122, self.RULE_exp10)
        try:
            self.state = 624
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [D96Parser.INTEGER_LITERAL]:
                self.enterOuterAlt(localctx, 1)
                self.state = 615
                self.match(D96Parser.INTEGER_LITERAL)
                pass
            elif token in [D96Parser.ARRAY]:
                self.enterOuterAlt(localctx, 2)
                self.state = 616
                self.array_literal()
                pass
            elif token in [D96Parser.BOOL_LITERAL]:
                self.enterOuterAlt(localctx, 3)
                self.state = 617
                self.match(D96Parser.BOOL_LITERAL)
                pass
            elif token in [D96Parser.REAL_LITERAL]:
                self.enterOuterAlt(localctx, 4)
                self.state = 618
                self.match(D96Parser.REAL_LITERAL)
                pass
            elif token in [D96Parser.STRING_LITERAL]:
                self.enterOuterAlt(localctx, 5)
                self.state = 619
                self.match(D96Parser.STRING_LITERAL)
                pass
            elif token in [D96Parser.NORMAL_ID]:
                self.enterOuterAlt(localctx, 6)
                self.state = 620
                self.match(D96Parser.NORMAL_ID)
                pass
            elif token in [D96Parser.DOLLAR_ID]:
                self.enterOuterAlt(localctx, 7)
                self.state = 621
                self.match(D96Parser.DOLLAR_ID)
                pass
            elif token in [D96Parser.SELF]:
                self.enterOuterAlt(localctx, 8)
                self.state = 622
                self.match(D96Parser.SELF)
                pass
            elif token in [D96Parser.LP]:
                self.enterOuterAlt(localctx, 9)
                self.state = 623
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
        self.enterRule(localctx, 124, self.RULE_exp11)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 626
            self.match(D96Parser.LP)
            self.state = 627
            self.exp()
            self.state = 628
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
        self.enterRule(localctx, 126, self.RULE_list_exp)
        try:
            self.state = 632
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [D96Parser.LP, D96Parser.ARRAY, D96Parser.NEW, D96Parser.SELF, D96Parser.SUB, D96Parser.NOT, D96Parser.BOOL_LITERAL, D96Parser.INTEGER_LITERAL, D96Parser.STRING_LITERAL, D96Parser.REAL_LITERAL, D96Parser.NORMAL_ID, D96Parser.DOLLAR_ID]:
                self.enterOuterAlt(localctx, 1)
                self.state = 630
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
        self.enterRule(localctx, 128, self.RULE_exps)
        try:
            self.state = 639
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,48,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 634
                self.exp()
                self.state = 635
                self.match(D96Parser.COMMA)
                self.state = 636
                self.exps()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 638
                self.exp()
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
        self.enterRule(localctx, 130, self.RULE_id_list)
        self._la = 0 # Token type
        try:
            self.state = 645
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,49,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 641
                _la = self._input.LA(1)
                if not(_la==D96Parser.NORMAL_ID or _la==D96Parser.DOLLAR_ID):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 642
                self.match(D96Parser.COMMA)
                self.state = 643
                self.id_list()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 644
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
        self._predicates[51] = self.exp1_sempred
        self._predicates[52] = self.exp2_sempred
        self._predicates[53] = self.exp3_sempred
        self._predicates[56] = self.exp6_sempred
        self._predicates[58] = self.exp7_sempred
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
         




