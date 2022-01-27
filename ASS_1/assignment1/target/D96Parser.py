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
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3C")
        buf.write("\u0284\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
        buf.write("\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r\4\16")
        buf.write("\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23\t\23")
        buf.write("\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30\4\31")
        buf.write("\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36\t\36")
        buf.write("\4\37\t\37\4 \t \4!\t!\4\"\t\"\4#\t#\4$\t$\4%\t%\4&\t")
        buf.write("&\4\'\t\'\4(\t(\4)\t)\4*\t*\4+\t+\4,\t,\4-\t-\4.\t.\4")
        buf.write("/\t/\4\60\t\60\4\61\t\61\4\62\t\62\4\63\t\63\4\64\t\64")
        buf.write("\4\65\t\65\4\66\t\66\4\67\t\67\48\t8\49\t9\4:\t:\4;\t")
        buf.write(";\4<\t<\4=\t=\4>\t>\4?\t?\4@\t@\4A\tA\4B\tB\4C\tC\3\2")
        buf.write("\3\2\3\2\3\3\3\3\3\3\3\3\5\3\u008e\n\3\3\4\3\4\3\4\3\4")
        buf.write("\3\4\3\5\3\5\3\5\5\5\u0098\n\5\3\6\3\6\3\6\3\6\3\7\3\7")
        buf.write("\5\7\u00a0\n\7\3\b\3\b\3\b\3\b\5\b\u00a6\n\b\3\t\3\t\3")
        buf.write("\t\3\t\5\t\u00ac\n\t\3\n\3\n\3\n\3\n\3\n\3\n\3\13\3\13")
        buf.write("\3\13\3\13\3\13\3\f\3\f\3\f\3\f\3\f\3\f\3\r\3\r\5\r\u00c1")
        buf.write("\n\r\3\16\3\16\3\16\3\16\3\16\5\16\u00c8\n\16\3\17\3\17")
        buf.write("\3\17\3\17\3\17\3\17\3\17\3\17\5\17\u00d2\n\17\3\20\3")
        buf.write("\20\3\20\3\20\3\21\3\21\5\21\u00da\n\21\3\22\3\22\3\22")
        buf.write("\3\22\5\22\u00e0\n\22\3\23\3\23\3\23\3\23\3\23\3\23\3")
        buf.write("\23\3\23\3\23\3\23\3\23\3\23\3\23\3\23\5\23\u00f0\n\23")
        buf.write("\3\24\3\24\3\24\3\25\3\25\3\25\3\26\3\26\3\26\3\26\3\27")
        buf.write("\3\27\5\27\u00fe\n\27\3\30\3\30\3\30\3\30\3\30\3\31\3")
        buf.write("\31\3\31\3\31\3\31\3\31\3\31\3\31\3\32\3\32\5\32\u010f")
        buf.write("\n\32\3\33\3\33\3\33\3\33\5\33\u0115\n\33\3\34\3\34\3")
        buf.write("\34\3\34\3\34\3\34\3\35\3\35\3\35\5\35\u0120\n\35\3\36")
        buf.write("\3\36\3\36\3\36\3\36\3\36\3\36\3\36\3\36\3\36\3\36\3\37")
        buf.write("\3\37\3\37\5\37\u0130\n\37\3 \3 \3 \3 \3 \3 \3 \5 \u0139")
        buf.write("\n \3!\3!\3!\3\"\3\"\3\"\3\"\3#\3#\3#\3#\3#\3#\3#\3$\3")
        buf.write("$\3$\3%\3%\3%\3%\3%\3%\3&\3&\3&\3&\3\'\3\'\3\'\3\'\3\'")
        buf.write("\3\'\5\'\u015c\n\'\3\'\3\'\3\'\3\'\3\'\3\'\3\'\5\'\u0165")
        buf.write("\n\'\5\'\u0167\n\'\3(\3(\3(\3(\3(\3(\3(\3(\3(\3(\3(\3")
        buf.write("(\3(\5(\u0176\n(\3(\5(\u0179\n(\3)\3)\3)\3)\3*\3*\3*\3")
        buf.write("*\3*\3*\3*\3*\3*\3*\3*\3*\5*\u018b\n*\5*\u018d\n*\3+\3")
        buf.write("+\3+\3+\3+\3+\3+\3+\3+\3+\3+\3+\3+\5+\u019c\n+\3+\5+\u019f")
        buf.write("\n+\3,\3,\3,\3,\3,\3,\3,\3,\5,\u01a9\n,\3,\3,\3,\3,\3")
        buf.write("-\3-\3-\3-\3-\3.\3.\5.\u01b6\n.\3/\3/\3/\3/\3/\5/\u01bd")
        buf.write("\n/\3\60\3\60\3\60\3\60\3\60\3\60\3\60\3\60\3\60\5\60")
        buf.write("\u01c8\n\60\3\61\3\61\3\61\3\61\3\61\3\61\3\61\3\61\3")
        buf.write("\61\3\61\3\61\3\61\3\61\3\61\3\61\3\61\3\61\3\61\3\61")
        buf.write("\3\61\3\61\3\61\3\61\3\61\3\61\5\61\u01e3\n\61\3\62\3")
        buf.write("\62\3\62\3\62\3\62\3\62\3\62\3\62\3\62\7\62\u01ee\n\62")
        buf.write("\f\62\16\62\u01f1\13\62\3\63\3\63\3\63\3\63\3\63\3\63")
        buf.write("\3\63\3\63\3\63\7\63\u01fc\n\63\f\63\16\63\u01ff\13\63")
        buf.write("\3\64\3\64\3\64\3\64\3\64\3\64\3\64\3\64\3\64\3\64\3\64")
        buf.write("\3\64\7\64\u020d\n\64\f\64\16\64\u0210\13\64\3\65\3\65")
        buf.write("\3\65\5\65\u0215\n\65\3\66\3\66\3\66\5\66\u021a\n\66\3")
        buf.write("\67\3\67\3\67\3\67\3\67\7\67\u0221\n\67\f\67\16\67\u0224")
        buf.write("\13\67\38\38\58\u0228\n8\39\39\39\39\39\79\u022f\n9\f")
        buf.write("9\169\u0232\139\3:\3:\3:\3:\3;\3;\3;\3;\3;\3;\3;\3;\3")
        buf.write(";\3;\3;\7;\u0243\n;\f;\16;\u0246\13;\3<\3<\3<\3<\3<\3")
        buf.write("<\3<\3<\3<\3<\3<\5<\u0253\n<\3=\3=\3=\3=\3=\3=\3=\5=\u025c")
        buf.write("\n=\3>\3>\3>\3>\3>\3>\3>\3>\3>\5>\u0267\n>\3?\3?\3?\3")
        buf.write("?\3@\3@\5@\u026f\n@\3A\3A\3A\3A\3A\5A\u0276\nA\3B\3B\3")
        buf.write("B\3B\5B\u027c\nB\3C\3C\3C\3C\5C\u0282\nC\3C\2\bbdflpt")
        buf.write("D\2\4\6\b\n\f\16\20\22\24\26\30\32\34\36 \"$&(*,.\60\62")
        buf.write("\64\668:<>@BDFHJLNPRTVXZ\\^`bdfhjlnprtvxz|~\u0080\u0082")
        buf.write("\u0084\2\4\3\2?@\3\2\3\4\2\u02a7\2\u0086\3\2\2\2\4\u008d")
        buf.write("\3\2\2\2\6\u008f\3\2\2\2\b\u0097\3\2\2\2\n\u0099\3\2\2")
        buf.write("\2\f\u009f\3\2\2\2\16\u00a5\3\2\2\2\20\u00ab\3\2\2\2\22")
        buf.write("\u00ad\3\2\2\2\24\u00b3\3\2\2\2\26\u00b8\3\2\2\2\30\u00c0")
        buf.write("\3\2\2\2\32\u00c7\3\2\2\2\34\u00c9\3\2\2\2\36\u00d3\3")
        buf.write("\2\2\2 \u00d9\3\2\2\2\"\u00df\3\2\2\2$\u00ef\3\2\2\2&")
        buf.write("\u00f1\3\2\2\2(\u00f4\3\2\2\2*\u00f7\3\2\2\2,\u00fd\3")
        buf.write("\2\2\2.\u00ff\3\2\2\2\60\u0104\3\2\2\2\62\u010e\3\2\2")
        buf.write("\2\64\u0114\3\2\2\2\66\u0116\3\2\2\28\u011f\3\2\2\2:\u0121")
        buf.write("\3\2\2\2<\u012f\3\2\2\2>\u0138\3\2\2\2@\u013a\3\2\2\2")
        buf.write("B\u013d\3\2\2\2D\u0141\3\2\2\2F\u0148\3\2\2\2H\u014b\3")
        buf.write("\2\2\2J\u0151\3\2\2\2L\u0166\3\2\2\2N\u0178\3\2\2\2P\u017a")
        buf.write("\3\2\2\2R\u018c\3\2\2\2T\u019e\3\2\2\2V\u01a0\3\2\2\2")
        buf.write("X\u01ae\3\2\2\2Z\u01b5\3\2\2\2\\\u01bc\3\2\2\2^\u01c7")
        buf.write("\3\2\2\2`\u01e2\3\2\2\2b\u01e4\3\2\2\2d\u01f2\3\2\2\2")
        buf.write("f\u0200\3\2\2\2h\u0214\3\2\2\2j\u0219\3\2\2\2l\u021b\3")
        buf.write("\2\2\2n\u0227\3\2\2\2p\u0229\3\2\2\2r\u0233\3\2\2\2t\u0237")
        buf.write("\3\2\2\2v\u0252\3\2\2\2x\u025b\3\2\2\2z\u0266\3\2\2\2")
        buf.write("|\u0268\3\2\2\2~\u026e\3\2\2\2\u0080\u0275\3\2\2\2\u0082")
        buf.write("\u027b\3\2\2\2\u0084\u0281\3\2\2\2\u0086\u0087\5\4\3\2")
        buf.write("\u0087\u0088\7\2\2\3\u0088\3\3\2\2\2\u0089\u008e\5\6\4")
        buf.write("\2\u008a\u008b\5\6\4\2\u008b\u008c\5\4\3\2\u008c\u008e")
        buf.write("\3\2\2\2\u008d\u0089\3\2\2\2\u008d\u008a\3\2\2\2\u008e")
        buf.write("\5\3\2\2\2\u008f\u0090\7\64\2\2\u0090\u0091\7?\2\2\u0091")
        buf.write("\u0092\5\b\5\2\u0092\u0093\5\n\6\2\u0093\7\3\2\2\2\u0094")
        buf.write("\u0095\7\r\2\2\u0095\u0098\7?\2\2\u0096\u0098\3\2\2\2")
        buf.write("\u0097\u0094\3\2\2\2\u0097\u0096\3\2\2\2\u0098\t\3\2\2")
        buf.write("\2\u0099\u009a\7\7\2\2\u009a\u009b\5\f\7\2\u009b\u009c")
        buf.write("\7\b\2\2\u009c\13\3\2\2\2\u009d\u00a0\5\16\b\2\u009e\u00a0")
        buf.write("\3\2\2\2\u009f\u009d\3\2\2\2\u009f\u009e\3\2\2\2\u00a0")
        buf.write("\r\3\2\2\2\u00a1\u00a2\5\20\t\2\u00a2\u00a3\5\16\b\2\u00a3")
        buf.write("\u00a6\3\2\2\2\u00a4\u00a6\5\20\t\2\u00a5\u00a1\3\2\2")
        buf.write("\2\u00a5\u00a4\3\2\2\2\u00a6\17\3\2\2\2\u00a7\u00ac\5")
        buf.write("J&\2\u00a8\u00ac\5\22\n\2\u00a9\u00ac\5\24\13\2\u00aa")
        buf.write("\u00ac\5\26\f\2\u00ab\u00a7\3\2\2\2\u00ab\u00a8\3\2\2")
        buf.write("\2\u00ab\u00a9\3\2\2\2\u00ab\u00aa\3\2\2\2\u00ac\21\3")
        buf.write("\2\2\2\u00ad\u00ae\7\33\2\2\u00ae\u00af\7\5\2\2\u00af")
        buf.write("\u00b0\5\30\r\2\u00b0\u00b1\7\6\2\2\u00b1\u00b2\5\36\20")
        buf.write("\2\u00b2\23\3\2\2\2\u00b3\u00b4\7\34\2\2\u00b4\u00b5\7")
        buf.write("\5\2\2\u00b5\u00b6\7\6\2\2\u00b6\u00b7\5\36\20\2\u00b7")
        buf.write("\25\3\2\2\2\u00b8\u00b9\t\2\2\2\u00b9\u00ba\7\5\2\2\u00ba")
        buf.write("\u00bb\5\30\r\2\u00bb\u00bc\7\6\2\2\u00bc\u00bd\5\36\20")
        buf.write("\2\u00bd\27\3\2\2\2\u00be\u00c1\5\32\16\2\u00bf\u00c1")
        buf.write("\3\2\2\2\u00c0\u00be\3\2\2\2\u00c0\u00bf\3\2\2\2\u00c1")
        buf.write("\31\3\2\2\2\u00c2\u00c3\5\34\17\2\u00c3\u00c4\7\13\2\2")
        buf.write("\u00c4\u00c5\5\32\16\2\u00c5\u00c8\3\2\2\2\u00c6\u00c8")
        buf.write("\5\34\17\2\u00c7\u00c2\3\2\2\2\u00c7\u00c6\3\2\2\2\u00c8")
        buf.write("\33\3\2\2\2\u00c9\u00ca\5\u0082B\2\u00ca\u00d1\7\r\2\2")
        buf.write("\u00cb\u00d2\7\30\2\2\u00cc\u00d2\7\67\2\2\u00cd\u00d2")
        buf.write("\7\65\2\2\u00ce\u00d2\5V,\2\u00cf\u00d2\7\66\2\2\u00d0")
        buf.write("\u00d2\7?\2\2\u00d1\u00cb\3\2\2\2\u00d1\u00cc\3\2\2\2")
        buf.write("\u00d1\u00cd\3\2\2\2\u00d1\u00ce\3\2\2\2\u00d1\u00cf\3")
        buf.write("\2\2\2\u00d1\u00d0\3\2\2\2\u00d2\35\3\2\2\2\u00d3\u00d4")
        buf.write("\7\7\2\2\u00d4\u00d5\5 \21\2\u00d5\u00d6\7\b\2\2\u00d6")
        buf.write("\37\3\2\2\2\u00d7\u00da\5\"\22\2\u00d8\u00da\3\2\2\2\u00d9")
        buf.write("\u00d7\3\2\2\2\u00d9\u00d8\3\2\2\2\u00da!\3\2\2\2\u00db")
        buf.write("\u00dc\5$\23\2\u00dc\u00dd\5\"\22\2\u00dd\u00e0\3\2\2")
        buf.write("\2\u00de\u00e0\5$\23\2\u00df\u00db\3\2\2\2\u00df\u00de")
        buf.write("\3\2\2\2\u00e0#\3\2\2\2\u00e1\u00f0\5.\30\2\u00e2\u00f0")
        buf.write("\5P)\2\u00e3\u00f0\5&\24\2\u00e4\u00f0\5(\25\2\u00e5\u00f0")
        buf.write("\5*\26\2\u00e6\u00e7\5D#\2\u00e7\u00e8\7\13\2\2\u00e8")
        buf.write("\u00f0\3\2\2\2\u00e9\u00ea\5^\60\2\u00ea\u00eb\5H%\2\u00eb")
        buf.write("\u00ec\7\13\2\2\u00ec\u00f0\3\2\2\2\u00ed\u00f0\5\60\31")
        buf.write("\2\u00ee\u00f0\5:\36\2\u00ef\u00e1\3\2\2\2\u00ef\u00e2")
        buf.write("\3\2\2\2\u00ef\u00e3\3\2\2\2\u00ef\u00e4\3\2\2\2\u00ef")
        buf.write("\u00e5\3\2\2\2\u00ef\u00e6\3\2\2\2\u00ef\u00e9\3\2\2\2")
        buf.write("\u00ef\u00ed\3\2\2\2\u00ef\u00ee\3\2\2\2\u00f0%\3\2\2")
        buf.write("\2\u00f1\u00f2\7\16\2\2\u00f2\u00f3\7\13\2\2\u00f3\'\3")
        buf.write("\2\2\2\u00f4\u00f5\7\17\2\2\u00f5\u00f6\7\13\2\2\u00f6")
        buf.write(")\3\2\2\2\u00f7\u00f8\7\31\2\2\u00f8\u00f9\5,\27\2\u00f9")
        buf.write("\u00fa\7\13\2\2\u00fa+\3\2\2\2\u00fb\u00fe\5^\60\2\u00fc")
        buf.write("\u00fe\3\2\2\2\u00fd\u00fb\3\2\2\2\u00fd\u00fc\3\2\2\2")
        buf.write("\u00fe-\3\2\2\2\u00ff\u0100\5> \2\u0100\u0101\7)\2\2\u0101")
        buf.write("\u0102\5^\60\2\u0102\u0103\7\13\2\2\u0103/\3\2\2\2\u0104")
        buf.write("\u0105\7\20\2\2\u0105\u0106\7\5\2\2\u0106\u0107\5^\60")
        buf.write("\2\u0107\u0108\7\6\2\2\u0108\u0109\5\36\20\2\u0109\u010a")
        buf.write("\5\62\32\2\u010a\u010b\58\35\2\u010b\61\3\2\2\2\u010c")
        buf.write("\u010f\5\64\33\2\u010d\u010f\3\2\2\2\u010e\u010c\3\2\2")
        buf.write("\2\u010e\u010d\3\2\2\2\u010f\63\3\2\2\2\u0110\u0115\5")
        buf.write("\66\34\2\u0111\u0112\5\66\34\2\u0112\u0113\5\64\33\2\u0113")
        buf.write("\u0115\3\2\2\2\u0114\u0110\3\2\2\2\u0114\u0111\3\2\2\2")
        buf.write("\u0115\65\3\2\2\2\u0116\u0117\7\21\2\2\u0117\u0118\7\5")
        buf.write("\2\2\u0118\u0119\5^\60\2\u0119\u011a\7\6\2\2\u011a\u011b")
        buf.write("\5\36\20\2\u011b\67\3\2\2\2\u011c\u011d\7\22\2\2\u011d")
        buf.write("\u0120\5\36\20\2\u011e\u0120\3\2\2\2\u011f\u011c\3\2\2")
        buf.write("\2\u011f\u011e\3\2\2\2\u01209\3\2\2\2\u0121\u0122\7\23")
        buf.write("\2\2\u0122\u0123\7\5\2\2\u0123\u0124\t\2\2\2\u0124\u0125")
        buf.write("\7\27\2\2\u0125\u0126\5^\60\2\u0126\u0127\7\62\2\2\u0127")
        buf.write("\u0128\5^\60\2\u0128\u0129\5<\37\2\u0129\u012a\7\6\2\2")
        buf.write("\u012a\u012b\5\36\20\2\u012b;\3\2\2\2\u012c\u012d\7\36")
        buf.write("\2\2\u012d\u0130\5^\60\2\u012e\u0130\3\2\2\2\u012f\u012c")
        buf.write("\3\2\2\2\u012f\u012e\3\2\2\2\u0130=\3\2\2\2\u0131\u0139")
        buf.write("\7?\2\2\u0132\u0139\7@\2\2\u0133\u0139\5@!\2\u0134\u0139")
        buf.write("\5B\"\2\u0135\u0136\5^\60\2\u0136\u0137\5F$\2\u0137\u0139")
        buf.write("\3\2\2\2\u0138\u0131\3\2\2\2\u0138\u0132\3\2\2\2\u0138")
        buf.write("\u0133\3\2\2\2\u0138\u0134\3\2\2\2\u0138\u0135\3\2\2\2")
        buf.write("\u0139?\3\2\2\2\u013a\u013b\5^\60\2\u013b\u013c\5n8\2")
        buf.write("\u013cA\3\2\2\2\u013d\u013e\7?\2\2\u013e\u013f\7\63\2")
        buf.write("\2\u013f\u0140\7@\2\2\u0140C\3\2\2\2\u0141\u0142\7?\2")
        buf.write("\2\u0142\u0143\7\63\2\2\u0143\u0144\7@\2\2\u0144\u0145")
        buf.write("\7\5\2\2\u0145\u0146\5~@\2\u0146\u0147\7\6\2\2\u0147E")
        buf.write("\3\2\2\2\u0148\u0149\7\61\2\2\u0149\u014a\7?\2\2\u014a")
        buf.write("G\3\2\2\2\u014b\u014c\7\61\2\2\u014c\u014d\7?\2\2\u014d")
        buf.write("\u014e\7\5\2\2\u014e\u014f\5~@\2\u014f\u0150\7\6\2\2\u0150")
        buf.write("I\3\2\2\2\u0151\u0152\t\3\2\2\u0152\u0153\5L\'\2\u0153")
        buf.write("\u0154\7\13\2\2\u0154K\3\2\2\2\u0155\u0156\t\2\2\2\u0156")
        buf.write("\u0157\5N(\2\u0157\u0158\5^\60\2\u0158\u0167\3\2\2\2\u0159")
        buf.write("\u015c\5\u0084C\2\u015a\u015c\5\u0082B\2\u015b\u0159\3")
        buf.write("\2\2\2\u015b\u015a\3\2\2\2\u015c\u015d\3\2\2\2\u015d\u0164")
        buf.write("\7\r\2\2\u015e\u0165\7\30\2\2\u015f\u0165\7\67\2\2\u0160")
        buf.write("\u0165\7\65\2\2\u0161\u0165\5V,\2\u0162\u0165\7\66\2\2")
        buf.write("\u0163\u0165\7?\2\2\u0164\u015e\3\2\2\2\u0164\u015f\3")
        buf.write("\2\2\2\u0164\u0160\3\2\2\2\u0164\u0161\3\2\2\2\u0164\u0162")
        buf.write("\3\2\2\2\u0164\u0163\3\2\2\2\u0165\u0167\3\2\2\2\u0166")
        buf.write("\u0155\3\2\2\2\u0166\u015b\3\2\2\2\u0167M\3\2\2\2\u0168")
        buf.write("\u0169\7\f\2\2\u0169\u016a\t\2\2\2\u016a\u016b\5N(\2\u016b")
        buf.write("\u016c\5^\60\2\u016c\u016d\7\f\2\2\u016d\u0179\3\2\2\2")
        buf.write("\u016e\u0175\7\r\2\2\u016f\u0176\7\30\2\2\u0170\u0176")
        buf.write("\7\67\2\2\u0171\u0176\7\65\2\2\u0172\u0176\5V,\2\u0173")
        buf.write("\u0176\7\66\2\2\u0174\u0176\7?\2\2\u0175\u016f\3\2\2\2")
        buf.write("\u0175\u0170\3\2\2\2\u0175\u0171\3\2\2\2\u0175\u0172\3")
        buf.write("\2\2\2\u0175\u0173\3\2\2\2\u0175\u0174\3\2\2\2\u0176\u0177")
        buf.write("\3\2\2\2\u0177\u0179\7)\2\2\u0178\u0168\3\2\2\2\u0178")
        buf.write("\u016e\3\2\2\2\u0179O\3\2\2\2\u017a\u017b\t\3\2\2\u017b")
        buf.write("\u017c\5R*\2\u017c\u017d\7\13\2\2\u017dQ\3\2\2\2\u017e")
        buf.write("\u017f\7?\2\2\u017f\u0180\5T+\2\u0180\u0181\5^\60\2\u0181")
        buf.write("\u018d\3\2\2\2\u0182\u0183\5\u0082B\2\u0183\u018a\7\r")
        buf.write("\2\2\u0184\u018b\7\30\2\2\u0185\u018b\7\67\2\2\u0186\u018b")
        buf.write("\7\65\2\2\u0187\u018b\5V,\2\u0188\u018b\7\66\2\2\u0189")
        buf.write("\u018b\7?\2\2\u018a\u0184\3\2\2\2\u018a\u0185\3\2\2\2")
        buf.write("\u018a\u0186\3\2\2\2\u018a\u0187\3\2\2\2\u018a\u0188\3")
        buf.write("\2\2\2\u018a\u0189\3\2\2\2\u018b\u018d\3\2\2\2\u018c\u017e")
        buf.write("\3\2\2\2\u018c\u0182\3\2\2\2\u018dS\3\2\2\2\u018e\u018f")
        buf.write("\7\f\2\2\u018f\u0190\7?\2\2\u0190\u0191\5T+\2\u0191\u0192")
        buf.write("\5^\60\2\u0192\u0193\7\f\2\2\u0193\u019f\3\2\2\2\u0194")
        buf.write("\u019b\7\r\2\2\u0195\u019c\7\30\2\2\u0196\u019c\7\67\2")
        buf.write("\2\u0197\u019c\7\65\2\2\u0198\u019c\5V,\2\u0199\u019c")
        buf.write("\7\66\2\2\u019a\u019c\7?\2\2\u019b\u0195\3\2\2\2\u019b")
        buf.write("\u0196\3\2\2\2\u019b\u0197\3\2\2\2\u019b\u0198\3\2\2\2")
        buf.write("\u019b\u0199\3\2\2\2\u019b\u019a\3\2\2\2\u019c\u019d\3")
        buf.write("\2\2\2\u019d\u019f\7)\2\2\u019e\u018e\3\2\2\2\u019e\u0194")
        buf.write("\3\2\2\2\u019fU\3\2\2\2\u01a0\u01a1\7\26\2\2\u01a1\u01a8")
        buf.write("\7\t\2\2\u01a2\u01a9\7\30\2\2\u01a3\u01a9\7\67\2\2\u01a4")
        buf.write("\u01a9\7\65\2\2\u01a5\u01a9\5V,\2\u01a6\u01a9\7\66\2\2")
        buf.write("\u01a7\u01a9\7?\2\2\u01a8\u01a2\3\2\2\2\u01a8\u01a3\3")
        buf.write("\2\2\2\u01a8\u01a4\3\2\2\2\u01a8\u01a5\3\2\2\2\u01a8\u01a6")
        buf.write("\3\2\2\2\u01a8\u01a7\3\2\2\2\u01a9\u01aa\3\2\2\2\u01aa")
        buf.write("\u01ab\7\f\2\2\u01ab\u01ac\79\2\2\u01ac\u01ad\7\n\2\2")
        buf.write("\u01adW\3\2\2\2\u01ae\u01af\7\26\2\2\u01af\u01b0\7\5\2")
        buf.write("\2\u01b0\u01b1\5Z.\2\u01b1\u01b2\7\6\2\2\u01b2Y\3\2\2")
        buf.write("\2\u01b3\u01b6\5\\/\2\u01b4\u01b6\3\2\2\2\u01b5\u01b3")
        buf.write("\3\2\2\2\u01b5\u01b4\3\2\2\2\u01b6[\3\2\2\2\u01b7\u01b8")
        buf.write("\5^\60\2\u01b8\u01b9\7\f\2\2\u01b9\u01ba\5\\/\2\u01ba")
        buf.write("\u01bd\3\2\2\2\u01bb\u01bd\5^\60\2\u01bc\u01b7\3\2\2\2")
        buf.write("\u01bc\u01bb\3\2\2\2\u01bd]\3\2\2\2\u01be\u01bf\5`\61")
        buf.write("\2\u01bf\u01c0\7/\2\2\u01c0\u01c1\5`\61\2\u01c1\u01c8")
        buf.write("\3\2\2\2\u01c2\u01c3\5`\61\2\u01c3\u01c4\7\60\2\2\u01c4")
        buf.write("\u01c5\5`\61\2\u01c5\u01c8\3\2\2\2\u01c6\u01c8\5`\61\2")
        buf.write("\u01c7\u01be\3\2\2\2\u01c7\u01c2\3\2\2\2\u01c7\u01c6\3")
        buf.write("\2\2\2\u01c8_\3\2\2\2\u01c9\u01ca\5b\62\2\u01ca\u01cb")
        buf.write("\7-\2\2\u01cb\u01cc\5b\62\2\u01cc\u01e3\3\2\2\2\u01cd")
        buf.write("\u01ce\5b\62\2\u01ce\u01cf\7.\2\2\u01cf\u01d0\5b\62\2")
        buf.write("\u01d0\u01e3\3\2\2\2\u01d1\u01d2\5b\62\2\u01d2\u01d3\7")
        buf.write("+\2\2\u01d3\u01d4\5b\62\2\u01d4\u01e3\3\2\2\2\u01d5\u01d6")
        buf.write("\5b\62\2\u01d6\u01d7\7(\2\2\u01d7\u01d8\5b\62\2\u01d8")
        buf.write("\u01e3\3\2\2\2\u01d9\u01da\5b\62\2\u01da\u01db\7*\2\2")
        buf.write("\u01db\u01dc\5b\62\2\u01dc\u01e3\3\2\2\2\u01dd\u01de\5")
        buf.write("b\62\2\u01de\u01df\7,\2\2\u01df\u01e0\5b\62\2\u01e0\u01e3")
        buf.write("\3\2\2\2\u01e1\u01e3\5b\62\2\u01e2\u01c9\3\2\2\2\u01e2")
        buf.write("\u01cd\3\2\2\2\u01e2\u01d1\3\2\2\2\u01e2\u01d5\3\2\2\2")
        buf.write("\u01e2\u01d9\3\2\2\2\u01e2\u01dd\3\2\2\2\u01e2\u01e1\3")
        buf.write("\2\2\2\u01e3a\3\2\2\2\u01e4\u01e5\b\62\1\2\u01e5\u01e6")
        buf.write("\5d\63\2\u01e6\u01ef\3\2\2\2\u01e7\u01e8\f\5\2\2\u01e8")
        buf.write("\u01e9\7&\2\2\u01e9\u01ee\5d\63\2\u01ea\u01eb\f\4\2\2")
        buf.write("\u01eb\u01ec\7\'\2\2\u01ec\u01ee\5d\63\2\u01ed\u01e7\3")
        buf.write("\2\2\2\u01ed\u01ea\3\2\2\2\u01ee\u01f1\3\2\2\2\u01ef\u01ed")
        buf.write("\3\2\2\2\u01ef\u01f0\3\2\2\2\u01f0c\3\2\2\2\u01f1\u01ef")
        buf.write("\3\2\2\2\u01f2\u01f3\b\63\1\2\u01f3\u01f4\5f\64\2\u01f4")
        buf.write("\u01fd\3\2\2\2\u01f5\u01f6\f\5\2\2\u01f6\u01f7\7 \2\2")
        buf.write("\u01f7\u01fc\5f\64\2\u01f8\u01f9\f\4\2\2\u01f9\u01fa\7")
        buf.write("!\2\2\u01fa\u01fc\5f\64\2\u01fb\u01f5\3\2\2\2\u01fb\u01f8")
        buf.write("\3\2\2\2\u01fc\u01ff\3\2\2\2\u01fd\u01fb\3\2\2\2\u01fd")
        buf.write("\u01fe\3\2\2\2\u01fee\3\2\2\2\u01ff\u01fd\3\2\2\2\u0200")
        buf.write("\u0201\b\64\1\2\u0201\u0202\5h\65\2\u0202\u020e\3\2\2")
        buf.write("\2\u0203\u0204\f\6\2\2\u0204\u0205\7\"\2\2\u0205\u020d")
        buf.write("\5h\65\2\u0206\u0207\f\5\2\2\u0207\u0208\7#\2\2\u0208")
        buf.write("\u020d\5h\65\2\u0209\u020a\f\4\2\2\u020a\u020b\7$\2\2")
        buf.write("\u020b\u020d\5h\65\2\u020c\u0203\3\2\2\2\u020c\u0206\3")
        buf.write("\2\2\2\u020c\u0209\3\2\2\2\u020d\u0210\3\2\2\2\u020e\u020c")
        buf.write("\3\2\2\2\u020e\u020f\3\2\2\2\u020fg\3\2\2\2\u0210\u020e")
        buf.write("\3\2\2\2\u0211\u0212\7%\2\2\u0212\u0215\5h\65\2\u0213")
        buf.write("\u0215\5j\66\2\u0214\u0211\3\2\2\2\u0214\u0213\3\2\2\2")
        buf.write("\u0215i\3\2\2\2\u0216\u0217\7!\2\2\u0217\u021a\5j\66\2")
        buf.write("\u0218\u021a\5l\67\2\u0219\u0216\3\2\2\2\u0219\u0218\3")
        buf.write("\2\2\2\u021ak\3\2\2\2\u021b\u021c\b\67\1\2\u021c\u021d")
        buf.write("\5t;\2\u021d\u0222\3\2\2\2\u021e\u021f\f\4\2\2\u021f\u0221")
        buf.write("\5r:\2\u0220\u021e\3\2\2\2\u0221\u0224\3\2\2\2\u0222\u0220")
        buf.write("\3\2\2\2\u0222\u0223\3\2\2\2\u0223m\3\2\2\2\u0224\u0222")
        buf.write("\3\2\2\2\u0225\u0228\5p9\2\u0226\u0228\3\2\2\2\u0227\u0225")
        buf.write("\3\2\2\2\u0227\u0226\3\2\2\2\u0228o\3\2\2\2\u0229\u022a")
        buf.write("\b9\1\2\u022a\u022b\5r:\2\u022b\u0230\3\2\2\2\u022c\u022d")
        buf.write("\f\4\2\2\u022d\u022f\5r:\2\u022e\u022c\3\2\2\2\u022f\u0232")
        buf.write("\3\2\2\2\u0230\u022e\3\2\2\2\u0230\u0231\3\2\2\2\u0231")
        buf.write("q\3\2\2\2\u0232\u0230\3\2\2\2\u0233\u0234\7\t\2\2\u0234")
        buf.write("\u0235\5^\60\2\u0235\u0236\7\n\2\2\u0236s\3\2\2\2\u0237")
        buf.write("\u0238\b;\1\2\u0238\u0239\5v<\2\u0239\u0244\3\2\2\2\u023a")
        buf.write("\u023b\f\5\2\2\u023b\u023c\5n8\2\u023c\u023d\5F$\2\u023d")
        buf.write("\u0243\3\2\2\2\u023e\u023f\f\4\2\2\u023f\u0240\5n8\2\u0240")
        buf.write("\u0241\5H%\2\u0241\u0243\3\2\2\2\u0242\u023a\3\2\2\2\u0242")
        buf.write("\u023e\3\2\2\2\u0243\u0246\3\2\2\2\u0244\u0242\3\2\2\2")
        buf.write("\u0244\u0245\3\2\2\2\u0245u\3\2\2\2\u0246\u0244\3\2\2")
        buf.write("\2\u0247\u0248\7?\2\2\u0248\u0249\7\63\2\2\u0249\u024a")
        buf.write("\7@\2\2\u024a\u024b\7\5\2\2\u024b\u024c\5~@\2\u024c\u024d")
        buf.write("\7\6\2\2\u024d\u0253\3\2\2\2\u024e\u024f\7?\2\2\u024f")
        buf.write("\u0250\7\63\2\2\u0250\u0253\7@\2\2\u0251\u0253\5x=\2\u0252")
        buf.write("\u0247\3\2\2\2\u0252\u024e\3\2\2\2\u0252\u0251\3\2\2\2")
        buf.write("\u0253w\3\2\2\2\u0254\u0255\7\35\2\2\u0255\u0256\5x=\2")
        buf.write("\u0256\u0257\7\5\2\2\u0257\u0258\5~@\2\u0258\u0259\7\6")
        buf.write("\2\2\u0259\u025c\3\2\2\2\u025a\u025c\5z>\2\u025b\u0254")
        buf.write("\3\2\2\2\u025b\u025a\3\2\2\2\u025cy\3\2\2\2\u025d\u0267")
        buf.write("\79\2\2\u025e\u0267\7:\2\2\u025f\u0267\5X-\2\u0260\u0267")
        buf.write("\78\2\2\u0261\u0267\7>\2\2\u0262\u0267\7;\2\2\u0263\u0267")
        buf.write("\7?\2\2\u0264\u0267\7\37\2\2\u0265\u0267\5|?\2\u0266\u025d")
        buf.write("\3\2\2\2\u0266\u025e\3\2\2\2\u0266\u025f\3\2\2\2\u0266")
        buf.write("\u0260\3\2\2\2\u0266\u0261\3\2\2\2\u0266\u0262\3\2\2\2")
        buf.write("\u0266\u0263\3\2\2\2\u0266\u0264\3\2\2\2\u0266\u0265\3")
        buf.write("\2\2\2\u0267{\3\2\2\2\u0268\u0269\7\5\2\2\u0269\u026a")
        buf.write("\5^\60\2\u026a\u026b\7\6\2\2\u026b}\3\2\2\2\u026c\u026f")
        buf.write("\5\u0080A\2\u026d\u026f\3\2\2\2\u026e\u026c\3\2\2\2\u026e")
        buf.write("\u026d\3\2\2\2\u026f\177\3\2\2\2\u0270\u0271\5^\60\2\u0271")
        buf.write("\u0272\7\f\2\2\u0272\u0273\5\u0080A\2\u0273\u0276\3\2")
        buf.write("\2\2\u0274\u0276\5^\60\2\u0275\u0270\3\2\2\2\u0275\u0274")
        buf.write("\3\2\2\2\u0276\u0081\3\2\2\2\u0277\u0278\7?\2\2\u0278")
        buf.write("\u0279\7\f\2\2\u0279\u027c\5\u0082B\2\u027a\u027c\7?\2")
        buf.write("\2\u027b\u0277\3\2\2\2\u027b\u027a\3\2\2\2\u027c\u0083")
        buf.write("\3\2\2\2\u027d\u027e\t\2\2\2\u027e\u027f\7\f\2\2\u027f")
        buf.write("\u0282\5\u0084C\2\u0280\u0282\t\2\2\2\u0281\u027d\3\2")
        buf.write("\2\2\u0281\u0280\3\2\2\2\u0282\u0085\3\2\2\2\65\u008d")
        buf.write("\u0097\u009f\u00a5\u00ab\u00c0\u00c7\u00d1\u00d9\u00df")
        buf.write("\u00ef\u00fd\u010e\u0114\u011f\u012f\u0138\u015b\u0164")
        buf.write("\u0166\u0175\u0178\u018a\u018c\u019b\u019e\u01a8\u01b5")
        buf.write("\u01bc\u01c7\u01e2\u01ed\u01ef\u01fb\u01fd\u020c\u020e")
        buf.write("\u0214\u0219\u0222\u0227\u0230\u0242\u0244\u0252\u025b")
        buf.write("\u0266\u026e\u0275\u027b\u0281")
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
                     "'..'", "'::'", "'Class'", "'Float'", "'String'", "'Int'" ]

    symbolicNames = [ "<INVALID>", "VAL", "VAR", "LP", "RP", "LCB", "RCB", 
                      "LSB", "RSB", "SEMI", "COMMA", "COLON", "BREAK", "CONTINUE", 
                      "IF", "ELSEIF", "ELSE", "FOREACH", "TRUE", "FALSE", 
                      "ARRAY", "IN", "BOOLEAN", "RETURN", "NULL", "CONSTRUCTOR", 
                      "DESTRUCTOR", "NEW", "BY", "SELF", "ADD", "SUB", "MUL", 
                      "DIV", "MOD", "NOT", "AND", "OR", "EQUAL", "ASSIGN", 
                      "NOTEQUAL", "GT", "GTE", "LT", "LTE", "EQUAL_STR", 
                      "ADD_STR", "DOT", "DOTDOT", "SCOPE", "CLASS", "FLOAT_TYPE", 
                      "STRING", "INT_TYPE", "BOOL_LITERAL", "ARRAY_SIZE", 
                      "INTEGER_LITERAL", "STRING_LITERAL", "ILLEGAL_ESCAPE", 
                      "UNCLOSE_STRING", "REAL_LITERAL", "NORMAL_ID", "DOLLAR_ID", 
                      "BLOCK_COMMENT", "WS", "ERROR_CHAR" ]

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
    RULE_element_index = 31
    RULE_static_attr_call = 32
    RULE_static_method_call = 33
    RULE_instance_attr_dot_call = 34
    RULE_instance_method_dot_call = 35
    RULE_attribute_declare = 36
    RULE_dec_and_init_list1 = 37
    RULE_pair1 = 38
    RULE_var_declare = 39
    RULE_dec_and_init_list2 = 40
    RULE_pair2 = 41
    RULE_array_type = 42
    RULE_array_literal = 43
    RULE_literal_list = 44
    RULE_literals = 45
    RULE_exp = 46
    RULE_exp0 = 47
    RULE_exp1 = 48
    RULE_exp2 = 49
    RULE_exp3 = 50
    RULE_exp4 = 51
    RULE_exp5 = 52
    RULE_exp6 = 53
    RULE_index_operator_list = 54
    RULE_index_operators = 55
    RULE_index_operator = 56
    RULE_exp7 = 57
    RULE_exp8 = 58
    RULE_exp9 = 59
    RULE_exp10 = 60
    RULE_exp11 = 61
    RULE_list_exp = 62
    RULE_exps = 63
    RULE_normal_id_list = 64
    RULE_id_list = 65

    ruleNames =  [ "program", "class_declares_list", "class_declare", "extend", 
                   "class_members", "member_list", "members", "member", 
                   "constructor_method", "destructor_method", "method_declare", 
                   "param_list", "parameters", "parameter", "block_statements", 
                   "statements_list", "statements", "statement", "break_statement", 
                   "continue_statement", "return_statement", "exp_value", 
                   "assign_statement", "if_else_statement", "elseif_stmt_list", 
                   "elseif_stmts", "elseif_stmt", "else_stmt", "foreach_statement", 
                   "increment", "lhs", "element_index", "static_attr_call", 
                   "static_method_call", "instance_attr_dot_call", "instance_method_dot_call", 
                   "attribute_declare", "dec_and_init_list1", "pair1", "var_declare", 
                   "dec_and_init_list2", "pair2", "array_type", "array_literal", 
                   "literal_list", "literals", "exp", "exp0", "exp1", "exp2", 
                   "exp3", "exp4", "exp5", "exp6", "index_operator_list", 
                   "index_operators", "index_operator", "exp7", "exp8", 
                   "exp9", "exp10", "exp11", "list_exp", "exps", "normal_id_list", 
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
    CLASS=50
    FLOAT_TYPE=51
    STRING=52
    INT_TYPE=53
    BOOL_LITERAL=54
    ARRAY_SIZE=55
    INTEGER_LITERAL=56
    STRING_LITERAL=57
    ILLEGAL_ESCAPE=58
    UNCLOSE_STRING=59
    REAL_LITERAL=60
    NORMAL_ID=61
    DOLLAR_ID=62
    BLOCK_COMMENT=63
    WS=64
    ERROR_CHAR=65

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

        def class_declares_list(self):
            return self.getTypedRuleContext(D96Parser.Class_declares_listContext,0)


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
            self.state = 132
            self.class_declares_list()
            self.state = 133
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
            self.state = 139
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,0,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 135
                self.class_declare()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 136
                self.class_declare()
                self.state = 137
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
            self.state = 141
            self.match(D96Parser.CLASS)
            self.state = 142
            self.match(D96Parser.NORMAL_ID)
            self.state = 143
            self.extend()
            self.state = 144
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
            self.state = 149
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [D96Parser.COLON]:
                self.enterOuterAlt(localctx, 1)
                self.state = 146
                self.match(D96Parser.COLON)
                self.state = 147
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
            self.state = 151
            self.match(D96Parser.LCB)
            self.state = 152
            self.member_list()
            self.state = 153
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
            self.state = 157
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [D96Parser.VAL, D96Parser.VAR, D96Parser.CONSTRUCTOR, D96Parser.DESTRUCTOR, D96Parser.NORMAL_ID, D96Parser.DOLLAR_ID]:
                self.enterOuterAlt(localctx, 1)
                self.state = 155
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
            self.state = 163
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,3,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 159
                self.member()
                self.state = 160
                self.members()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 162
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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMember" ):
                return visitor.visitMember(self)
            else:
                return visitor.visitChildren(self)




    def member(self):

        localctx = D96Parser.MemberContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_member)
        try:
            self.state = 169
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [D96Parser.VAL, D96Parser.VAR]:
                self.enterOuterAlt(localctx, 1)
                self.state = 165
                self.attribute_declare()
                pass
            elif token in [D96Parser.CONSTRUCTOR]:
                self.enterOuterAlt(localctx, 2)
                self.state = 166
                self.constructor_method()
                pass
            elif token in [D96Parser.DESTRUCTOR]:
                self.enterOuterAlt(localctx, 3)
                self.state = 167
                self.destructor_method()
                pass
            elif token in [D96Parser.NORMAL_ID, D96Parser.DOLLAR_ID]:
                self.enterOuterAlt(localctx, 4)
                self.state = 168
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
        self.enterRule(localctx, 16, self.RULE_constructor_method)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 171
            self.match(D96Parser.CONSTRUCTOR)
            self.state = 172
            self.match(D96Parser.LP)
            self.state = 173
            self.param_list()
            self.state = 174
            self.match(D96Parser.RP)
            self.state = 175
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
        self.enterRule(localctx, 18, self.RULE_destructor_method)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 177
            self.match(D96Parser.DESTRUCTOR)
            self.state = 178
            self.match(D96Parser.LP)
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
        self.enterRule(localctx, 20, self.RULE_method_declare)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 182
            _la = self._input.LA(1)
            if not(_la==D96Parser.NORMAL_ID or _la==D96Parser.DOLLAR_ID):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 183
            self.match(D96Parser.LP)
            self.state = 184
            self.param_list()
            self.state = 185
            self.match(D96Parser.RP)
            self.state = 186
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
        self.enterRule(localctx, 22, self.RULE_param_list)
        try:
            self.state = 190
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [D96Parser.NORMAL_ID]:
                self.enterOuterAlt(localctx, 1)
                self.state = 188
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
        self.enterRule(localctx, 24, self.RULE_parameters)
        try:
            self.state = 197
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,6,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 192
                self.parameter()
                self.state = 193
                self.match(D96Parser.SEMI)
                self.state = 194
                self.parameters()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 196
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
        self.enterRule(localctx, 26, self.RULE_parameter)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 199
            self.normal_id_list()
            self.state = 200
            self.match(D96Parser.COLON)
            self.state = 207
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [D96Parser.BOOLEAN]:
                self.state = 201
                self.match(D96Parser.BOOLEAN)
                pass
            elif token in [D96Parser.INT_TYPE]:
                self.state = 202
                self.match(D96Parser.INT_TYPE)
                pass
            elif token in [D96Parser.FLOAT_TYPE]:
                self.state = 203
                self.match(D96Parser.FLOAT_TYPE)
                pass
            elif token in [D96Parser.ARRAY]:
                self.state = 204
                self.array_type()
                pass
            elif token in [D96Parser.STRING]:
                self.state = 205
                self.match(D96Parser.STRING)
                pass
            elif token in [D96Parser.NORMAL_ID]:
                self.state = 206
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
        self.enterRule(localctx, 28, self.RULE_block_statements)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 209
            self.match(D96Parser.LCB)
            self.state = 210
            self.statements_list()
            self.state = 211
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
        self.enterRule(localctx, 30, self.RULE_statements_list)
        try:
            self.state = 215
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [D96Parser.VAL, D96Parser.VAR, D96Parser.LP, D96Parser.BREAK, D96Parser.CONTINUE, D96Parser.IF, D96Parser.FOREACH, D96Parser.ARRAY, D96Parser.RETURN, D96Parser.NEW, D96Parser.SELF, D96Parser.SUB, D96Parser.NOT, D96Parser.BOOL_LITERAL, D96Parser.ARRAY_SIZE, D96Parser.INTEGER_LITERAL, D96Parser.STRING_LITERAL, D96Parser.REAL_LITERAL, D96Parser.NORMAL_ID, D96Parser.DOLLAR_ID]:
                self.enterOuterAlt(localctx, 1)
                self.state = 213
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
        self.enterRule(localctx, 32, self.RULE_statements)
        try:
            self.state = 221
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,9,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 217
                self.statement()
                self.state = 218
                self.statements()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 220
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


        def static_method_call(self):
            return self.getTypedRuleContext(D96Parser.Static_method_callContext,0)


        def SEMI(self):
            return self.getToken(D96Parser.SEMI, 0)

        def exp(self):
            return self.getTypedRuleContext(D96Parser.ExpContext,0)


        def instance_method_dot_call(self):
            return self.getTypedRuleContext(D96Parser.Instance_method_dot_callContext,0)


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
        self.enterRule(localctx, 34, self.RULE_statement)
        try:
            self.state = 237
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,10,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 223
                self.assign_statement()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 224
                self.var_declare()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 225
                self.break_statement()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 226
                self.continue_statement()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 227
                self.return_statement()
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 228
                self.static_method_call()
                self.state = 229
                self.match(D96Parser.SEMI)
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 231
                self.exp()
                self.state = 232
                self.instance_method_dot_call()
                self.state = 233
                self.match(D96Parser.SEMI)
                pass

            elif la_ == 8:
                self.enterOuterAlt(localctx, 8)
                self.state = 235
                self.if_else_statement()
                pass

            elif la_ == 9:
                self.enterOuterAlt(localctx, 9)
                self.state = 236
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
        self.enterRule(localctx, 36, self.RULE_break_statement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 239
            self.match(D96Parser.BREAK)
            self.state = 240
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
        self.enterRule(localctx, 38, self.RULE_continue_statement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 242
            self.match(D96Parser.CONTINUE)
            self.state = 243
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

        def exp_value(self):
            return self.getTypedRuleContext(D96Parser.Exp_valueContext,0)


        def SEMI(self):
            return self.getToken(D96Parser.SEMI, 0)

        def getRuleIndex(self):
            return D96Parser.RULE_return_statement

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitReturn_statement" ):
                return visitor.visitReturn_statement(self)
            else:
                return visitor.visitChildren(self)




    def return_statement(self):

        localctx = D96Parser.Return_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 40, self.RULE_return_statement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 245
            self.match(D96Parser.RETURN)
            self.state = 246
            self.exp_value()
            self.state = 247
            self.match(D96Parser.SEMI)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Exp_valueContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def exp(self):
            return self.getTypedRuleContext(D96Parser.ExpContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_exp_value

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExp_value" ):
                return visitor.visitExp_value(self)
            else:
                return visitor.visitChildren(self)




    def exp_value(self):

        localctx = D96Parser.Exp_valueContext(self, self._ctx, self.state)
        self.enterRule(localctx, 42, self.RULE_exp_value)
        try:
            self.state = 251
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [D96Parser.LP, D96Parser.ARRAY, D96Parser.NEW, D96Parser.SELF, D96Parser.SUB, D96Parser.NOT, D96Parser.BOOL_LITERAL, D96Parser.ARRAY_SIZE, D96Parser.INTEGER_LITERAL, D96Parser.STRING_LITERAL, D96Parser.REAL_LITERAL, D96Parser.NORMAL_ID]:
                self.enterOuterAlt(localctx, 1)
                self.state = 249
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
            self.state = 253
            self.lhs()
            self.state = 254
            self.match(D96Parser.ASSIGN)
            self.state = 255
            self.exp()
            self.state = 256
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
            self.state = 258
            self.match(D96Parser.IF)
            self.state = 259
            self.match(D96Parser.LP)
            self.state = 260
            self.exp()
            self.state = 261
            self.match(D96Parser.RP)
            self.state = 262
            self.block_statements()
            self.state = 263
            self.elseif_stmt_list()
            self.state = 264
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
            self.state = 268
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [D96Parser.ELSEIF]:
                self.enterOuterAlt(localctx, 1)
                self.state = 266
                self.elseif_stmts()
                pass
            elif token in [D96Parser.VAL, D96Parser.VAR, D96Parser.LP, D96Parser.RCB, D96Parser.BREAK, D96Parser.CONTINUE, D96Parser.IF, D96Parser.ELSE, D96Parser.FOREACH, D96Parser.ARRAY, D96Parser.RETURN, D96Parser.NEW, D96Parser.SELF, D96Parser.SUB, D96Parser.NOT, D96Parser.BOOL_LITERAL, D96Parser.ARRAY_SIZE, D96Parser.INTEGER_LITERAL, D96Parser.STRING_LITERAL, D96Parser.REAL_LITERAL, D96Parser.NORMAL_ID, D96Parser.DOLLAR_ID]:
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
            self.state = 274
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,13,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 270
                self.elseif_stmt()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 271
                self.elseif_stmt()
                self.state = 272
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
            self.state = 276
            self.match(D96Parser.ELSEIF)
            self.state = 277
            self.match(D96Parser.LP)
            self.state = 278
            self.exp()
            self.state = 279
            self.match(D96Parser.RP)
            self.state = 280
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
            self.state = 285
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [D96Parser.ELSE]:
                self.enterOuterAlt(localctx, 1)
                self.state = 282
                self.match(D96Parser.ELSE)
                self.state = 283
                self.block_statements()
                pass
            elif token in [D96Parser.VAL, D96Parser.VAR, D96Parser.LP, D96Parser.RCB, D96Parser.BREAK, D96Parser.CONTINUE, D96Parser.IF, D96Parser.FOREACH, D96Parser.ARRAY, D96Parser.RETURN, D96Parser.NEW, D96Parser.SELF, D96Parser.SUB, D96Parser.NOT, D96Parser.BOOL_LITERAL, D96Parser.ARRAY_SIZE, D96Parser.INTEGER_LITERAL, D96Parser.STRING_LITERAL, D96Parser.REAL_LITERAL, D96Parser.NORMAL_ID, D96Parser.DOLLAR_ID]:
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
            self.state = 287
            self.match(D96Parser.FOREACH)
            self.state = 288
            self.match(D96Parser.LP)
            self.state = 289
            _la = self._input.LA(1)
            if not(_la==D96Parser.NORMAL_ID or _la==D96Parser.DOLLAR_ID):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 290
            self.match(D96Parser.IN)
            self.state = 291
            self.exp()
            self.state = 292
            self.match(D96Parser.DOTDOT)
            self.state = 293
            self.exp()
            self.state = 294
            self.increment()
            self.state = 295
            self.match(D96Parser.RP)
            self.state = 296
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
            self.state = 301
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [D96Parser.BY]:
                self.enterOuterAlt(localctx, 1)
                self.state = 298
                self.match(D96Parser.BY)
                self.state = 299
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


        def static_attr_call(self):
            return self.getTypedRuleContext(D96Parser.Static_attr_callContext,0)


        def exp(self):
            return self.getTypedRuleContext(D96Parser.ExpContext,0)


        def instance_attr_dot_call(self):
            return self.getTypedRuleContext(D96Parser.Instance_attr_dot_callContext,0)


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
            self.state = 310
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,16,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 303
                self.match(D96Parser.NORMAL_ID)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 304
                self.match(D96Parser.DOLLAR_ID)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 305
                self.element_index()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 306
                self.static_attr_call()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 307
                self.exp()
                self.state = 308
                self.instance_attr_dot_call()
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


        def index_operator_list(self):
            return self.getTypedRuleContext(D96Parser.Index_operator_listContext,0)


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
            self.state = 312
            self.exp()
            self.state = 313
            self.index_operator_list()
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
        self.enterRule(localctx, 64, self.RULE_static_attr_call)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 315
            self.match(D96Parser.NORMAL_ID)
            self.state = 316
            self.match(D96Parser.SCOPE)
            self.state = 317
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
        self.enterRule(localctx, 66, self.RULE_static_method_call)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 319
            self.match(D96Parser.NORMAL_ID)
            self.state = 320
            self.match(D96Parser.SCOPE)
            self.state = 321
            self.match(D96Parser.DOLLAR_ID)
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


    class Instance_attr_dot_callContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def DOT(self):
            return self.getToken(D96Parser.DOT, 0)

        def NORMAL_ID(self):
            return self.getToken(D96Parser.NORMAL_ID, 0)

        def getRuleIndex(self):
            return D96Parser.RULE_instance_attr_dot_call

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitInstance_attr_dot_call" ):
                return visitor.visitInstance_attr_dot_call(self)
            else:
                return visitor.visitChildren(self)




    def instance_attr_dot_call(self):

        localctx = D96Parser.Instance_attr_dot_callContext(self, self._ctx, self.state)
        self.enterRule(localctx, 68, self.RULE_instance_attr_dot_call)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 326
            self.match(D96Parser.DOT)
            self.state = 327
            self.match(D96Parser.NORMAL_ID)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Instance_method_dot_callContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

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
            return D96Parser.RULE_instance_method_dot_call

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitInstance_method_dot_call" ):
                return visitor.visitInstance_method_dot_call(self)
            else:
                return visitor.visitChildren(self)




    def instance_method_dot_call(self):

        localctx = D96Parser.Instance_method_dot_callContext(self, self._ctx, self.state)
        self.enterRule(localctx, 70, self.RULE_instance_method_dot_call)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 329
            self.match(D96Parser.DOT)
            self.state = 330
            self.match(D96Parser.NORMAL_ID)
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


    class Attribute_declareContext(ParserRuleContext):
        __slots__ = 'parser'

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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAttribute_declare" ):
                return visitor.visitAttribute_declare(self)
            else:
                return visitor.visitChildren(self)




    def attribute_declare(self):

        localctx = D96Parser.Attribute_declareContext(self, self._ctx, self.state)
        self.enterRule(localctx, 72, self.RULE_attribute_declare)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 335
            _la = self._input.LA(1)
            if not(_la==D96Parser.VAL or _la==D96Parser.VAR):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 336
            self.dec_and_init_list1()
            self.state = 337
            self.match(D96Parser.SEMI)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Dec_and_init_list1Context(ParserRuleContext):
        __slots__ = 'parser'

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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDec_and_init_list1" ):
                return visitor.visitDec_and_init_list1(self)
            else:
                return visitor.visitChildren(self)




    def dec_and_init_list1(self):

        localctx = D96Parser.Dec_and_init_list1Context(self, self._ctx, self.state)
        self.enterRule(localctx, 74, self.RULE_dec_and_init_list1)
        self._la = 0 # Token type
        try:
            self.state = 356
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,19,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 339
                _la = self._input.LA(1)
                if not(_la==D96Parser.NORMAL_ID or _la==D96Parser.DOLLAR_ID):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 340
                self.pair1()
                self.state = 341
                self.exp()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 345
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,17,self._ctx)
                if la_ == 1:
                    self.state = 343
                    self.id_list()
                    pass

                elif la_ == 2:
                    self.state = 344
                    self.normal_id_list()
                    pass


                self.state = 347
                self.match(D96Parser.COLON)
                self.state = 354
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [D96Parser.BOOLEAN]:
                    self.state = 348
                    self.match(D96Parser.BOOLEAN)
                    pass
                elif token in [D96Parser.INT_TYPE]:
                    self.state = 349
                    self.match(D96Parser.INT_TYPE)
                    pass
                elif token in [D96Parser.FLOAT_TYPE]:
                    self.state = 350
                    self.match(D96Parser.FLOAT_TYPE)
                    pass
                elif token in [D96Parser.ARRAY]:
                    self.state = 351
                    self.array_type()
                    pass
                elif token in [D96Parser.STRING]:
                    self.state = 352
                    self.match(D96Parser.STRING)
                    pass
                elif token in [D96Parser.NORMAL_ID]:
                    self.state = 353
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
        __slots__ = 'parser'

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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPair1" ):
                return visitor.visitPair1(self)
            else:
                return visitor.visitChildren(self)




    def pair1(self):

        localctx = D96Parser.Pair1Context(self, self._ctx, self.state)
        self.enterRule(localctx, 76, self.RULE_pair1)
        self._la = 0 # Token type
        try:
            self.state = 374
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [D96Parser.COMMA]:
                self.enterOuterAlt(localctx, 1)
                self.state = 358
                self.match(D96Parser.COMMA)
                self.state = 359
                _la = self._input.LA(1)
                if not(_la==D96Parser.NORMAL_ID or _la==D96Parser.DOLLAR_ID):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 360
                self.pair1()
                self.state = 361
                self.exp()
                self.state = 362
                self.match(D96Parser.COMMA)
                pass
            elif token in [D96Parser.COLON]:
                self.enterOuterAlt(localctx, 2)
                self.state = 364
                self.match(D96Parser.COLON)
                self.state = 371
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [D96Parser.BOOLEAN]:
                    self.state = 365
                    self.match(D96Parser.BOOLEAN)
                    pass
                elif token in [D96Parser.INT_TYPE]:
                    self.state = 366
                    self.match(D96Parser.INT_TYPE)
                    pass
                elif token in [D96Parser.FLOAT_TYPE]:
                    self.state = 367
                    self.match(D96Parser.FLOAT_TYPE)
                    pass
                elif token in [D96Parser.ARRAY]:
                    self.state = 368
                    self.array_type()
                    pass
                elif token in [D96Parser.STRING]:
                    self.state = 369
                    self.match(D96Parser.STRING)
                    pass
                elif token in [D96Parser.NORMAL_ID]:
                    self.state = 370
                    self.match(D96Parser.NORMAL_ID)
                    pass
                else:
                    raise NoViableAltException(self)

                self.state = 373
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
        __slots__ = 'parser'

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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVar_declare" ):
                return visitor.visitVar_declare(self)
            else:
                return visitor.visitChildren(self)




    def var_declare(self):

        localctx = D96Parser.Var_declareContext(self, self._ctx, self.state)
        self.enterRule(localctx, 78, self.RULE_var_declare)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 376
            _la = self._input.LA(1)
            if not(_la==D96Parser.VAL or _la==D96Parser.VAR):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 377
            self.dec_and_init_list2()
            self.state = 378
            self.match(D96Parser.SEMI)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Dec_and_init_list2Context(ParserRuleContext):
        __slots__ = 'parser'

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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDec_and_init_list2" ):
                return visitor.visitDec_and_init_list2(self)
            else:
                return visitor.visitChildren(self)




    def dec_and_init_list2(self):

        localctx = D96Parser.Dec_and_init_list2Context(self, self._ctx, self.state)
        self.enterRule(localctx, 80, self.RULE_dec_and_init_list2)
        try:
            self.state = 394
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,23,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 380
                self.match(D96Parser.NORMAL_ID)
                self.state = 381
                self.pair2()
                self.state = 382
                self.exp()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 384
                self.normal_id_list()
                self.state = 385
                self.match(D96Parser.COLON)
                self.state = 392
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [D96Parser.BOOLEAN]:
                    self.state = 386
                    self.match(D96Parser.BOOLEAN)
                    pass
                elif token in [D96Parser.INT_TYPE]:
                    self.state = 387
                    self.match(D96Parser.INT_TYPE)
                    pass
                elif token in [D96Parser.FLOAT_TYPE]:
                    self.state = 388
                    self.match(D96Parser.FLOAT_TYPE)
                    pass
                elif token in [D96Parser.ARRAY]:
                    self.state = 389
                    self.array_type()
                    pass
                elif token in [D96Parser.STRING]:
                    self.state = 390
                    self.match(D96Parser.STRING)
                    pass
                elif token in [D96Parser.NORMAL_ID]:
                    self.state = 391
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
        __slots__ = 'parser'

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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPair2" ):
                return visitor.visitPair2(self)
            else:
                return visitor.visitChildren(self)




    def pair2(self):

        localctx = D96Parser.Pair2Context(self, self._ctx, self.state)
        self.enterRule(localctx, 82, self.RULE_pair2)
        try:
            self.state = 412
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [D96Parser.COMMA]:
                self.enterOuterAlt(localctx, 1)
                self.state = 396
                self.match(D96Parser.COMMA)
                self.state = 397
                self.match(D96Parser.NORMAL_ID)
                self.state = 398
                self.pair2()
                self.state = 399
                self.exp()
                self.state = 400
                self.match(D96Parser.COMMA)
                pass
            elif token in [D96Parser.COLON]:
                self.enterOuterAlt(localctx, 2)
                self.state = 402
                self.match(D96Parser.COLON)
                self.state = 409
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [D96Parser.BOOLEAN]:
                    self.state = 403
                    self.match(D96Parser.BOOLEAN)
                    pass
                elif token in [D96Parser.INT_TYPE]:
                    self.state = 404
                    self.match(D96Parser.INT_TYPE)
                    pass
                elif token in [D96Parser.FLOAT_TYPE]:
                    self.state = 405
                    self.match(D96Parser.FLOAT_TYPE)
                    pass
                elif token in [D96Parser.ARRAY]:
                    self.state = 406
                    self.array_type()
                    pass
                elif token in [D96Parser.STRING]:
                    self.state = 407
                    self.match(D96Parser.STRING)
                    pass
                elif token in [D96Parser.NORMAL_ID]:
                    self.state = 408
                    self.match(D96Parser.NORMAL_ID)
                    pass
                else:
                    raise NoViableAltException(self)

                self.state = 411
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
        self.enterRule(localctx, 84, self.RULE_array_type)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 414
            self.match(D96Parser.ARRAY)
            self.state = 415
            self.match(D96Parser.LSB)
            self.state = 422
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [D96Parser.BOOLEAN]:
                self.state = 416
                self.match(D96Parser.BOOLEAN)
                pass
            elif token in [D96Parser.INT_TYPE]:
                self.state = 417
                self.match(D96Parser.INT_TYPE)
                pass
            elif token in [D96Parser.FLOAT_TYPE]:
                self.state = 418
                self.match(D96Parser.FLOAT_TYPE)
                pass
            elif token in [D96Parser.ARRAY]:
                self.state = 419
                self.array_type()
                pass
            elif token in [D96Parser.STRING]:
                self.state = 420
                self.match(D96Parser.STRING)
                pass
            elif token in [D96Parser.NORMAL_ID]:
                self.state = 421
                self.match(D96Parser.NORMAL_ID)
                pass
            else:
                raise NoViableAltException(self)

            self.state = 424
            self.match(D96Parser.COMMA)
            self.state = 425
            self.match(D96Parser.ARRAY_SIZE)
            self.state = 426
            self.match(D96Parser.RSB)
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
        self.enterRule(localctx, 86, self.RULE_array_literal)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 428
            self.match(D96Parser.ARRAY)
            self.state = 429
            self.match(D96Parser.LP)
            self.state = 430
            self.literal_list()
            self.state = 431
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
        self.enterRule(localctx, 88, self.RULE_literal_list)
        try:
            self.state = 435
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [D96Parser.LP, D96Parser.ARRAY, D96Parser.NEW, D96Parser.SELF, D96Parser.SUB, D96Parser.NOT, D96Parser.BOOL_LITERAL, D96Parser.ARRAY_SIZE, D96Parser.INTEGER_LITERAL, D96Parser.STRING_LITERAL, D96Parser.REAL_LITERAL, D96Parser.NORMAL_ID]:
                self.enterOuterAlt(localctx, 1)
                self.state = 433
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
        self.enterRule(localctx, 90, self.RULE_literals)
        try:
            self.state = 442
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,28,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 437
                self.exp()
                self.state = 438
                self.match(D96Parser.COMMA)
                self.state = 439
                self.literals()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 441
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
        self.enterRule(localctx, 92, self.RULE_exp)
        try:
            self.state = 453
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,29,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 444
                self.exp0()
                self.state = 445
                self.match(D96Parser.EQUAL_STR)
                self.state = 446
                self.exp0()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 448
                self.exp0()
                self.state = 449
                self.match(D96Parser.ADD_STR)
                self.state = 450
                self.exp0()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 452
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
        self.enterRule(localctx, 94, self.RULE_exp0)
        try:
            self.state = 480
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,30,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 455
                self.exp1(0)
                self.state = 456
                self.match(D96Parser.LT)
                self.state = 457
                self.exp1(0)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 459
                self.exp1(0)
                self.state = 460
                self.match(D96Parser.LTE)
                self.state = 461
                self.exp1(0)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 463
                self.exp1(0)
                self.state = 464
                self.match(D96Parser.GT)
                self.state = 465
                self.exp1(0)
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 467
                self.exp1(0)
                self.state = 468
                self.match(D96Parser.EQUAL)
                self.state = 469
                self.exp1(0)
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 471
                self.exp1(0)
                self.state = 472
                self.match(D96Parser.NOTEQUAL)
                self.state = 473
                self.exp1(0)
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 475
                self.exp1(0)
                self.state = 476
                self.match(D96Parser.GTE)
                self.state = 477
                self.exp1(0)
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 479
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
        _startState = 96
        self.enterRecursionRule(localctx, 96, self.RULE_exp1, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 483
            self.exp2(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 493
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,32,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 491
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,31,self._ctx)
                    if la_ == 1:
                        localctx = D96Parser.Exp1Context(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_exp1)
                        self.state = 485
                        if not self.precpred(self._ctx, 3):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 3)")
                        self.state = 486
                        self.match(D96Parser.AND)
                        self.state = 487
                        self.exp2(0)
                        pass

                    elif la_ == 2:
                        localctx = D96Parser.Exp1Context(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_exp1)
                        self.state = 488
                        if not self.precpred(self._ctx, 2):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                        self.state = 489
                        self.match(D96Parser.OR)
                        self.state = 490
                        self.exp2(0)
                        pass

             
                self.state = 495
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,32,self._ctx)

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
        _startState = 98
        self.enterRecursionRule(localctx, 98, self.RULE_exp2, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 497
            self.exp3(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 507
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,34,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 505
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,33,self._ctx)
                    if la_ == 1:
                        localctx = D96Parser.Exp2Context(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_exp2)
                        self.state = 499
                        if not self.precpred(self._ctx, 3):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 3)")
                        self.state = 500
                        self.match(D96Parser.ADD)
                        self.state = 501
                        self.exp3(0)
                        pass

                    elif la_ == 2:
                        localctx = D96Parser.Exp2Context(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_exp2)
                        self.state = 502
                        if not self.precpred(self._ctx, 2):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                        self.state = 503
                        self.match(D96Parser.SUB)
                        self.state = 504
                        self.exp3(0)
                        pass

             
                self.state = 509
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,34,self._ctx)

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
        _startState = 100
        self.enterRecursionRule(localctx, 100, self.RULE_exp3, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 511
            self.exp4()
            self._ctx.stop = self._input.LT(-1)
            self.state = 524
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,36,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 522
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,35,self._ctx)
                    if la_ == 1:
                        localctx = D96Parser.Exp3Context(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_exp3)
                        self.state = 513
                        if not self.precpred(self._ctx, 4):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 4)")
                        self.state = 514
                        self.match(D96Parser.MUL)
                        self.state = 515
                        self.exp4()
                        pass

                    elif la_ == 2:
                        localctx = D96Parser.Exp3Context(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_exp3)
                        self.state = 516
                        if not self.precpred(self._ctx, 3):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 3)")
                        self.state = 517
                        self.match(D96Parser.DIV)
                        self.state = 518
                        self.exp4()
                        pass

                    elif la_ == 3:
                        localctx = D96Parser.Exp3Context(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_exp3)
                        self.state = 519
                        if not self.precpred(self._ctx, 2):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                        self.state = 520
                        self.match(D96Parser.MOD)
                        self.state = 521
                        self.exp4()
                        pass

             
                self.state = 526
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,36,self._ctx)

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
        self.enterRule(localctx, 102, self.RULE_exp4)
        try:
            self.state = 530
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [D96Parser.NOT]:
                self.enterOuterAlt(localctx, 1)
                self.state = 527
                self.match(D96Parser.NOT)
                self.state = 528
                self.exp4()
                pass
            elif token in [D96Parser.LP, D96Parser.ARRAY, D96Parser.NEW, D96Parser.SELF, D96Parser.SUB, D96Parser.BOOL_LITERAL, D96Parser.ARRAY_SIZE, D96Parser.INTEGER_LITERAL, D96Parser.STRING_LITERAL, D96Parser.REAL_LITERAL, D96Parser.NORMAL_ID]:
                self.enterOuterAlt(localctx, 2)
                self.state = 529
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
        self.enterRule(localctx, 104, self.RULE_exp5)
        try:
            self.state = 535
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [D96Parser.SUB]:
                self.enterOuterAlt(localctx, 1)
                self.state = 532
                self.match(D96Parser.SUB)
                self.state = 533
                self.exp5()
                pass
            elif token in [D96Parser.LP, D96Parser.ARRAY, D96Parser.NEW, D96Parser.SELF, D96Parser.BOOL_LITERAL, D96Parser.ARRAY_SIZE, D96Parser.INTEGER_LITERAL, D96Parser.STRING_LITERAL, D96Parser.REAL_LITERAL, D96Parser.NORMAL_ID]:
                self.enterOuterAlt(localctx, 2)
                self.state = 534
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


        def index_operator(self):
            return self.getTypedRuleContext(D96Parser.Index_operatorContext,0)


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
        _startState = 106
        self.enterRecursionRule(localctx, 106, self.RULE_exp6, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 538
            self.exp7(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 544
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,39,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = D96Parser.Exp6Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_exp6)
                    self.state = 540
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 541
                    self.index_operator() 
                self.state = 546
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,39,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Index_operator_listContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def index_operators(self):
            return self.getTypedRuleContext(D96Parser.Index_operatorsContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_index_operator_list

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIndex_operator_list" ):
                return visitor.visitIndex_operator_list(self)
            else:
                return visitor.visitChildren(self)




    def index_operator_list(self):

        localctx = D96Parser.Index_operator_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 108, self.RULE_index_operator_list)
        try:
            self.state = 549
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [D96Parser.LSB]:
                self.enterOuterAlt(localctx, 1)
                self.state = 547
                self.index_operators(0)
                pass
            elif token in [D96Parser.ASSIGN, D96Parser.DOT]:
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


    class Index_operatorsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def index_operator(self):
            return self.getTypedRuleContext(D96Parser.Index_operatorContext,0)


        def index_operators(self):
            return self.getTypedRuleContext(D96Parser.Index_operatorsContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_index_operators

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIndex_operators" ):
                return visitor.visitIndex_operators(self)
            else:
                return visitor.visitChildren(self)



    def index_operators(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = D96Parser.Index_operatorsContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 110
        self.enterRecursionRule(localctx, 110, self.RULE_index_operators, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 552
            self.index_operator()
            self._ctx.stop = self._input.LT(-1)
            self.state = 558
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,41,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = D96Parser.Index_operatorsContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_index_operators)
                    self.state = 554
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 555
                    self.index_operator() 
                self.state = 560
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

        def getRuleIndex(self):
            return D96Parser.RULE_index_operator

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIndex_operator" ):
                return visitor.visitIndex_operator(self)
            else:
                return visitor.visitChildren(self)




    def index_operator(self):

        localctx = D96Parser.Index_operatorContext(self, self._ctx, self.state)
        self.enterRule(localctx, 112, self.RULE_index_operator)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 561
            self.match(D96Parser.LSB)
            self.state = 562
            self.exp()
            self.state = 563
            self.match(D96Parser.RSB)
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


        def index_operator_list(self):
            return self.getTypedRuleContext(D96Parser.Index_operator_listContext,0)


        def instance_attr_dot_call(self):
            return self.getTypedRuleContext(D96Parser.Instance_attr_dot_callContext,0)


        def instance_method_dot_call(self):
            return self.getTypedRuleContext(D96Parser.Instance_method_dot_callContext,0)


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
        _startState = 114
        self.enterRecursionRule(localctx, 114, self.RULE_exp7, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 566
            self.exp8()
            self._ctx.stop = self._input.LT(-1)
            self.state = 578
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,43,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 576
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,42,self._ctx)
                    if la_ == 1:
                        localctx = D96Parser.Exp7Context(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_exp7)
                        self.state = 568
                        if not self.precpred(self._ctx, 3):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 3)")
                        self.state = 569
                        self.index_operator_list()
                        self.state = 570
                        self.instance_attr_dot_call()
                        pass

                    elif la_ == 2:
                        localctx = D96Parser.Exp7Context(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_exp7)
                        self.state = 572
                        if not self.precpred(self._ctx, 2):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                        self.state = 573
                        self.index_operator_list()
                        self.state = 574
                        self.instance_method_dot_call()
                        pass

             
                self.state = 580
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
        self.enterRule(localctx, 116, self.RULE_exp8)
        try:
            self.state = 592
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,44,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 581
                self.match(D96Parser.NORMAL_ID)
                self.state = 582
                self.match(D96Parser.SCOPE)
                self.state = 583
                self.match(D96Parser.DOLLAR_ID)
                self.state = 584
                self.match(D96Parser.LP)
                self.state = 585
                self.list_exp()
                self.state = 586
                self.match(D96Parser.RP)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 588
                self.match(D96Parser.NORMAL_ID)
                self.state = 589
                self.match(D96Parser.SCOPE)
                self.state = 590
                self.match(D96Parser.DOLLAR_ID)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 591
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
        self.enterRule(localctx, 118, self.RULE_exp9)
        try:
            self.state = 601
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [D96Parser.NEW]:
                self.enterOuterAlt(localctx, 1)
                self.state = 594
                self.match(D96Parser.NEW)
                self.state = 595
                self.exp9()
                self.state = 596
                self.match(D96Parser.LP)
                self.state = 597
                self.list_exp()
                self.state = 598
                self.match(D96Parser.RP)
                pass
            elif token in [D96Parser.LP, D96Parser.ARRAY, D96Parser.SELF, D96Parser.BOOL_LITERAL, D96Parser.ARRAY_SIZE, D96Parser.INTEGER_LITERAL, D96Parser.STRING_LITERAL, D96Parser.REAL_LITERAL, D96Parser.NORMAL_ID]:
                self.enterOuterAlt(localctx, 2)
                self.state = 600
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
        self.enterRule(localctx, 120, self.RULE_exp10)
        try:
            self.state = 612
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [D96Parser.ARRAY_SIZE]:
                self.enterOuterAlt(localctx, 1)
                self.state = 603
                self.match(D96Parser.ARRAY_SIZE)
                pass
            elif token in [D96Parser.INTEGER_LITERAL]:
                self.enterOuterAlt(localctx, 2)
                self.state = 604
                self.match(D96Parser.INTEGER_LITERAL)
                pass
            elif token in [D96Parser.ARRAY]:
                self.enterOuterAlt(localctx, 3)
                self.state = 605
                self.array_literal()
                pass
            elif token in [D96Parser.BOOL_LITERAL]:
                self.enterOuterAlt(localctx, 4)
                self.state = 606
                self.match(D96Parser.BOOL_LITERAL)
                pass
            elif token in [D96Parser.REAL_LITERAL]:
                self.enterOuterAlt(localctx, 5)
                self.state = 607
                self.match(D96Parser.REAL_LITERAL)
                pass
            elif token in [D96Parser.STRING_LITERAL]:
                self.enterOuterAlt(localctx, 6)
                self.state = 608
                self.match(D96Parser.STRING_LITERAL)
                pass
            elif token in [D96Parser.NORMAL_ID]:
                self.enterOuterAlt(localctx, 7)
                self.state = 609
                self.match(D96Parser.NORMAL_ID)
                pass
            elif token in [D96Parser.SELF]:
                self.enterOuterAlt(localctx, 8)
                self.state = 610
                self.match(D96Parser.SELF)
                pass
            elif token in [D96Parser.LP]:
                self.enterOuterAlt(localctx, 9)
                self.state = 611
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
        self.enterRule(localctx, 122, self.RULE_exp11)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 614
            self.match(D96Parser.LP)
            self.state = 615
            self.exp()
            self.state = 616
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
        self.enterRule(localctx, 124, self.RULE_list_exp)
        try:
            self.state = 620
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [D96Parser.LP, D96Parser.ARRAY, D96Parser.NEW, D96Parser.SELF, D96Parser.SUB, D96Parser.NOT, D96Parser.BOOL_LITERAL, D96Parser.ARRAY_SIZE, D96Parser.INTEGER_LITERAL, D96Parser.STRING_LITERAL, D96Parser.REAL_LITERAL, D96Parser.NORMAL_ID]:
                self.enterOuterAlt(localctx, 1)
                self.state = 618
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
        self.enterRule(localctx, 126, self.RULE_exps)
        try:
            self.state = 627
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,48,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 622
                self.exp()
                self.state = 623
                self.match(D96Parser.COMMA)
                self.state = 624
                self.exps()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 626
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
        self.enterRule(localctx, 128, self.RULE_normal_id_list)
        try:
            self.state = 633
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,49,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 629
                self.match(D96Parser.NORMAL_ID)
                self.state = 630
                self.match(D96Parser.COMMA)
                self.state = 631
                self.normal_id_list()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 632
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
        self.enterRule(localctx, 130, self.RULE_id_list)
        self._la = 0 # Token type
        try:
            self.state = 639
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,50,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 635
                _la = self._input.LA(1)
                if not(_la==D96Parser.NORMAL_ID or _la==D96Parser.DOLLAR_ID):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 636
                self.match(D96Parser.COMMA)
                self.state = 637
                self.id_list()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 638
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
        self._predicates[48] = self.exp1_sempred
        self._predicates[49] = self.exp2_sempred
        self._predicates[50] = self.exp3_sempred
        self._predicates[53] = self.exp6_sempred
        self._predicates[55] = self.index_operators_sempred
        self._predicates[57] = self.exp7_sempred
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
         




