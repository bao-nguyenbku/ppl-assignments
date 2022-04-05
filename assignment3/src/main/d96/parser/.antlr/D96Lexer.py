# Generated from e:\HCMUT\PRINCIPLES_OF_PROGRAMMING_LANGUAGE\ppl-assignments\assignment3\src\main\d96\parser\D96.g4 by ANTLR 4.8
from antlr4 import *
from io import StringIO
from typing.io import TextIO
import sys


from lexererr import *



def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2A")
        buf.write("\u02be\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7")
        buf.write("\t\7\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r")
        buf.write("\4\16\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23")
        buf.write("\t\23\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30")
        buf.write("\4\31\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36")
        buf.write("\t\36\4\37\t\37\4 \t \4!\t!\4\"\t\"\4#\t#\4$\t$\4%\t%")
        buf.write("\4&\t&\4\'\t\'\4(\t(\4)\t)\4*\t*\4+\t+\4,\t,\4-\t-\4.")
        buf.write("\t.\4/\t/\4\60\t\60\4\61\t\61\4\62\t\62\4\63\t\63\4\64")
        buf.write("\t\64\4\65\t\65\4\66\t\66\4\67\t\67\48\t8\49\t9\4:\t:")
        buf.write("\4;\t;\4<\t<\4=\t=\4>\t>\4?\t?\4@\t@\4A\tA\4B\tB\4C\t")
        buf.write("C\4D\tD\4E\tE\4F\tF\4G\tG\4H\tH\4I\tI\4J\tJ\4K\tK\4L\t")
        buf.write("L\4M\tM\3\2\3\2\3\2\3\2\3\3\3\3\3\3\3\3\3\4\3\4\3\5\3")
        buf.write("\5\3\6\3\6\3\7\3\7\3\b\3\b\3\t\3\t\3\n\3\n\3\13\3\13\3")
        buf.write("\f\3\f\3\r\3\r\5\r\u00b8\n\r\3\r\3\r\3\16\6\16\u00bd\n")
        buf.write("\16\r\16\16\16\u00be\3\17\3\17\3\17\3\17\3\17\3\17\3\20")
        buf.write("\3\20\3\20\3\20\3\20\3\20\3\20\3\20\3\20\3\21\3\21\3\21")
        buf.write("\3\22\3\22\3\22\3\22\3\22\3\22\3\22\3\23\3\23\3\23\3\23")
        buf.write("\3\23\3\24\3\24\3\24\3\24\3\24\3\24\3\24\3\24\3\25\3\25")
        buf.write("\3\25\3\25\3\25\3\25\3\26\3\26\3\26\3\27\3\27\3\27\3\27")
        buf.write("\3\27\3\27\3\27\3\27\3\30\3\30\3\30\3\30\3\30\3\30\3\30")
        buf.write("\3\31\3\31\3\31\3\31\3\31\3\32\3\32\3\32\3\32\3\32\3\32")
        buf.write("\3\32\3\32\3\32\3\32\3\32\3\32\3\33\3\33\3\33\3\33\3\33")
        buf.write("\3\33\3\33\3\33\3\33\3\33\3\33\3\34\3\34\3\34\3\34\3\35")
        buf.write("\3\35\3\35\3\36\3\36\3\36\3\36\3\36\3\37\3\37\3 \3 \3")
        buf.write("!\3!\3\"\3\"\3#\3#\3$\3$\3%\3%\3%\3&\3&\3&\3\'\3\'\3\'")
        buf.write("\3(\3(\3)\3)\3)\3*\3*\3+\3+\3+\3,\3,\3-\3-\3-\3.\3.\3")
        buf.write(".\3.\3/\3/\3/\3\60\3\60\3\61\3\61\3\61\3\62\3\62\3\62")
        buf.write("\3\63\3\63\3\63\3\63\3\63\3\63\3\64\3\64\3\64\3\64\3\64")
        buf.write("\3\64\3\65\3\65\3\65\3\65\3\65\3\65\3\65\3\66\3\66\3\66")
        buf.write("\3\66\3\67\3\67\3\67\3\67\3\67\3\67\3\67\3\67\3\67\5\67")
        buf.write("\u017a\n\67\38\38\38\38\38\38\38\38\38\38\38\38\58\u0188")
        buf.write("\n8\39\39\39\39\59\u018e\n9\39\39\39\39\39\59\u0195\n")
        buf.write("9\39\39\59\u0199\n9\39\69\u019c\n9\r9\169\u019d\79\u01a0")
        buf.write("\n9\f9\169\u01a3\139\59\u01a5\n9\3:\3:\3:\3:\3:\5:\u01ac")
        buf.write("\n:\3:\6:\u01af\n:\r:\16:\u01b0\7:\u01b3\n:\f:\16:\u01b6")
        buf.write("\13:\5:\u01b8\n:\3;\3;\3;\3;\3;\3;\5;\u01c0\n;\3;\3;\3")
        buf.write(";\3;\5;\u01c6\n;\3;\3;\5;\u01ca\n;\3;\6;\u01cd\n;\r;\16")
        buf.write(";\u01ce\7;\u01d1\n;\f;\16;\u01d4\13;\5;\u01d6\n;\3<\3")
        buf.write("<\3<\5<\u01db\n<\3<\6<\u01de\n<\r<\16<\u01df\7<\u01e2")
        buf.write("\n<\f<\16<\u01e5\13<\5<\u01e7\n<\3=\3=\3=\3=\5=\u01ed")
        buf.write("\n=\3=\3=\3=\3=\3=\5=\u01f4\n=\3=\3=\5=\u01f8\n=\3=\6")
        buf.write("=\u01fb\n=\r=\16=\u01fc\7=\u01ff\n=\f=\16=\u0202\13=\5")
        buf.write("=\u0204\n=\3>\3>\3>\3>\3>\5>\u020b\n>\3>\6>\u020e\n>\r")
        buf.write(">\16>\u020f\7>\u0212\n>\f>\16>\u0215\13>\5>\u0217\n>\3")
        buf.write("?\3?\3?\3?\5?\u021d\n?\3?\3?\3?\3?\3?\5?\u0224\n?\3?\3")
        buf.write("?\5?\u0228\n?\3?\6?\u022b\n?\r?\16?\u022c\7?\u022f\n?")
        buf.write("\f?\16?\u0232\13?\5?\u0234\n?\3@\3@\3@\5@\u0239\n@\3@")
        buf.write("\6@\u023c\n@\r@\16@\u023d\7@\u0240\n@\f@\16@\u0243\13")
        buf.write("@\5@\u0245\n@\3A\3A\3A\3A\3A\3A\3A\3A\3A\3A\3A\3A\5A\u0253")
        buf.write("\nA\3B\3B\3B\3B\5B\u0259\nB\3C\3C\3C\3D\3D\3D\5D\u0261")
        buf.write("\nD\3E\3E\7E\u0265\nE\fE\16E\u0268\13E\3E\3E\3E\3F\3F")
        buf.write("\7F\u026f\nF\fF\16F\u0272\13F\3F\3F\3F\3G\3G\7G\u0279")
        buf.write("\nG\fG\16G\u027c\13G\3G\3G\3H\3H\3H\3H\5H\u0284\nH\3H")
        buf.write("\3H\3H\3H\3H\3H\3H\5H\u028d\nH\3H\3H\3H\3H\3H\3H\3H\3")
        buf.write("H\3H\5H\u0298\nH\3I\3I\7I\u029c\nI\fI\16I\u029f\13I\3")
        buf.write("J\3J\6J\u02a3\nJ\rJ\16J\u02a4\3K\3K\3K\3K\7K\u02ab\nK")
        buf.write("\fK\16K\u02ae\13K\3K\3K\3K\3K\3K\3L\6L\u02b6\nL\rL\16")
        buf.write("L\u02b7\3L\3L\3M\3M\3M\3\u02ac\2N\3\3\5\4\7\5\t\6\13\7")
        buf.write("\r\b\17\t\21\n\23\13\25\f\27\r\31\2\33\2\35\16\37\17!")
        buf.write("\20#\21%\22\'\23)\24+\25-\26/\27\61\30\63\31\65\32\67")
        buf.write("\339\34;\35=\36?\37A C!E\"G#I$K%M&O\'Q(S)U*W+Y,[-]._/")
        buf.write("a\60c\61e\62g\63i\64k\65m\66o\67q\2s\2u\2w\2y\2{\2}\2")
        buf.write("\177\2\u00818\u0083\2\u0085\2\u0087\2\u00899\u008b:\u008d")
        buf.write(";\u008f<\u0091=\u0093>\u0095?\u0097@\u0099A\3\2\21\4\2")
        buf.write("GGgg\4\2--//\3\2\62;\4\2\63;CH\4\2\62;CH\3\2\639\3\2\62")
        buf.write("9\3\2\63\63\3\2\62\63\3\2\63;\4\2$$^^\t\2))^^ddhhpptt")
        buf.write("vv\5\2C\\aac|\6\2\62;C\\aac|\5\2\13\f\17\17\"\"\2\u02f1")
        buf.write("\2\3\3\2\2\2\2\5\3\2\2\2\2\7\3\2\2\2\2\t\3\2\2\2\2\13")
        buf.write("\3\2\2\2\2\r\3\2\2\2\2\17\3\2\2\2\2\21\3\2\2\2\2\23\3")
        buf.write("\2\2\2\2\25\3\2\2\2\2\27\3\2\2\2\2\35\3\2\2\2\2\37\3\2")
        buf.write("\2\2\2!\3\2\2\2\2#\3\2\2\2\2%\3\2\2\2\2\'\3\2\2\2\2)\3")
        buf.write("\2\2\2\2+\3\2\2\2\2-\3\2\2\2\2/\3\2\2\2\2\61\3\2\2\2\2")
        buf.write("\63\3\2\2\2\2\65\3\2\2\2\2\67\3\2\2\2\29\3\2\2\2\2;\3")
        buf.write("\2\2\2\2=\3\2\2\2\2?\3\2\2\2\2A\3\2\2\2\2C\3\2\2\2\2E")
        buf.write("\3\2\2\2\2G\3\2\2\2\2I\3\2\2\2\2K\3\2\2\2\2M\3\2\2\2\2")
        buf.write("O\3\2\2\2\2Q\3\2\2\2\2S\3\2\2\2\2U\3\2\2\2\2W\3\2\2\2")
        buf.write("\2Y\3\2\2\2\2[\3\2\2\2\2]\3\2\2\2\2_\3\2\2\2\2a\3\2\2")
        buf.write("\2\2c\3\2\2\2\2e\3\2\2\2\2g\3\2\2\2\2i\3\2\2\2\2k\3\2")
        buf.write("\2\2\2m\3\2\2\2\2o\3\2\2\2\2\u0081\3\2\2\2\2\u0089\3\2")
        buf.write("\2\2\2\u008b\3\2\2\2\2\u008d\3\2\2\2\2\u008f\3\2\2\2\2")
        buf.write("\u0091\3\2\2\2\2\u0093\3\2\2\2\2\u0095\3\2\2\2\2\u0097")
        buf.write("\3\2\2\2\2\u0099\3\2\2\2\3\u009b\3\2\2\2\5\u009f\3\2\2")
        buf.write("\2\7\u00a3\3\2\2\2\t\u00a5\3\2\2\2\13\u00a7\3\2\2\2\r")
        buf.write("\u00a9\3\2\2\2\17\u00ab\3\2\2\2\21\u00ad\3\2\2\2\23\u00af")
        buf.write("\3\2\2\2\25\u00b1\3\2\2\2\27\u00b3\3\2\2\2\31\u00b5\3")
        buf.write("\2\2\2\33\u00bc\3\2\2\2\35\u00c0\3\2\2\2\37\u00c6\3\2")
        buf.write("\2\2!\u00cf\3\2\2\2#\u00d2\3\2\2\2%\u00d9\3\2\2\2\'\u00de")
        buf.write("\3\2\2\2)\u00e6\3\2\2\2+\u00ec\3\2\2\2-\u00ef\3\2\2\2")
        buf.write("/\u00f7\3\2\2\2\61\u00fe\3\2\2\2\63\u0103\3\2\2\2\65\u010f")
        buf.write("\3\2\2\2\67\u011a\3\2\2\29\u011e\3\2\2\2;\u0121\3\2\2")
        buf.write("\2=\u0126\3\2\2\2?\u0128\3\2\2\2A\u012a\3\2\2\2C\u012c")
        buf.write("\3\2\2\2E\u012e\3\2\2\2G\u0130\3\2\2\2I\u0132\3\2\2\2")
        buf.write("K\u0135\3\2\2\2M\u0138\3\2\2\2O\u013b\3\2\2\2Q\u013d\3")
        buf.write("\2\2\2S\u0140\3\2\2\2U\u0142\3\2\2\2W\u0145\3\2\2\2Y\u0147")
        buf.write("\3\2\2\2[\u014a\3\2\2\2]\u014e\3\2\2\2_\u0151\3\2\2\2")
        buf.write("a\u0153\3\2\2\2c\u0156\3\2\2\2e\u0159\3\2\2\2g\u015f\3")
        buf.write("\2\2\2i\u0165\3\2\2\2k\u016c\3\2\2\2m\u0179\3\2\2\2o\u0187")
        buf.write("\3\2\2\2q\u01a4\3\2\2\2s\u01b7\3\2\2\2u\u01d5\3\2\2\2")
        buf.write("w\u01e6\3\2\2\2y\u0203\3\2\2\2{\u0216\3\2\2\2}\u0233\3")
        buf.write("\2\2\2\177\u0244\3\2\2\2\u0081\u0252\3\2\2\2\u0083\u0258")
        buf.write("\3\2\2\2\u0085\u025a\3\2\2\2\u0087\u0260\3\2\2\2\u0089")
        buf.write("\u0262\3\2\2\2\u008b\u026c\3\2\2\2\u008d\u0276\3\2\2\2")
        buf.write("\u008f\u0297\3\2\2\2\u0091\u0299\3\2\2\2\u0093\u02a0\3")
        buf.write("\2\2\2\u0095\u02a6\3\2\2\2\u0097\u02b5\3\2\2\2\u0099\u02bb")
        buf.write("\3\2\2\2\u009b\u009c\7X\2\2\u009c\u009d\7c\2\2\u009d\u009e")
        buf.write("\7n\2\2\u009e\4\3\2\2\2\u009f\u00a0\7X\2\2\u00a0\u00a1")
        buf.write("\7c\2\2\u00a1\u00a2\7t\2\2\u00a2\6\3\2\2\2\u00a3\u00a4")
        buf.write("\7*\2\2\u00a4\b\3\2\2\2\u00a5\u00a6\7+\2\2\u00a6\n\3\2")
        buf.write("\2\2\u00a7\u00a8\7}\2\2\u00a8\f\3\2\2\2\u00a9\u00aa\7")
        buf.write("\177\2\2\u00aa\16\3\2\2\2\u00ab\u00ac\7]\2\2\u00ac\20")
        buf.write("\3\2\2\2\u00ad\u00ae\7_\2\2\u00ae\22\3\2\2\2\u00af\u00b0")
        buf.write("\7=\2\2\u00b0\24\3\2\2\2\u00b1\u00b2\7.\2\2\u00b2\26\3")
        buf.write("\2\2\2\u00b3\u00b4\7<\2\2\u00b4\30\3\2\2\2\u00b5\u00b7")
        buf.write("\t\2\2\2\u00b6\u00b8\t\3\2\2\u00b7\u00b6\3\2\2\2\u00b7")
        buf.write("\u00b8\3\2\2\2\u00b8\u00b9\3\2\2\2\u00b9\u00ba\5\33\16")
        buf.write("\2\u00ba\32\3\2\2\2\u00bb\u00bd\t\4\2\2\u00bc\u00bb\3")
        buf.write("\2\2\2\u00bd\u00be\3\2\2\2\u00be\u00bc\3\2\2\2\u00be\u00bf")
        buf.write("\3\2\2\2\u00bf\34\3\2\2\2\u00c0\u00c1\7D\2\2\u00c1\u00c2")
        buf.write("\7t\2\2\u00c2\u00c3\7g\2\2\u00c3\u00c4\7c\2\2\u00c4\u00c5")
        buf.write("\7m\2\2\u00c5\36\3\2\2\2\u00c6\u00c7\7E\2\2\u00c7\u00c8")
        buf.write("\7q\2\2\u00c8\u00c9\7p\2\2\u00c9\u00ca\7v\2\2\u00ca\u00cb")
        buf.write("\7k\2\2\u00cb\u00cc\7p\2\2\u00cc\u00cd\7w\2\2\u00cd\u00ce")
        buf.write("\7g\2\2\u00ce \3\2\2\2\u00cf\u00d0\7K\2\2\u00d0\u00d1")
        buf.write("\7h\2\2\u00d1\"\3\2\2\2\u00d2\u00d3\7G\2\2\u00d3\u00d4")
        buf.write("\7n\2\2\u00d4\u00d5\7u\2\2\u00d5\u00d6\7g\2\2\u00d6\u00d7")
        buf.write("\7k\2\2\u00d7\u00d8\7h\2\2\u00d8$\3\2\2\2\u00d9\u00da")
        buf.write("\7G\2\2\u00da\u00db\7n\2\2\u00db\u00dc\7u\2\2\u00dc\u00dd")
        buf.write("\7g\2\2\u00dd&\3\2\2\2\u00de\u00df\7H\2\2\u00df\u00e0")
        buf.write("\7q\2\2\u00e0\u00e1\7t\2\2\u00e1\u00e2\7g\2\2\u00e2\u00e3")
        buf.write("\7c\2\2\u00e3\u00e4\7e\2\2\u00e4\u00e5\7j\2\2\u00e5(\3")
        buf.write("\2\2\2\u00e6\u00e7\7C\2\2\u00e7\u00e8\7t\2\2\u00e8\u00e9")
        buf.write("\7t\2\2\u00e9\u00ea\7c\2\2\u00ea\u00eb\7{\2\2\u00eb*\3")
        buf.write("\2\2\2\u00ec\u00ed\7K\2\2\u00ed\u00ee\7p\2\2\u00ee,\3")
        buf.write("\2\2\2\u00ef\u00f0\7D\2\2\u00f0\u00f1\7q\2\2\u00f1\u00f2")
        buf.write("\7q\2\2\u00f2\u00f3\7n\2\2\u00f3\u00f4\7g\2\2\u00f4\u00f5")
        buf.write("\7c\2\2\u00f5\u00f6\7p\2\2\u00f6.\3\2\2\2\u00f7\u00f8")
        buf.write("\7T\2\2\u00f8\u00f9\7g\2\2\u00f9\u00fa\7v\2\2\u00fa\u00fb")
        buf.write("\7w\2\2\u00fb\u00fc\7t\2\2\u00fc\u00fd\7p\2\2\u00fd\60")
        buf.write("\3\2\2\2\u00fe\u00ff\7P\2\2\u00ff\u0100\7w\2\2\u0100\u0101")
        buf.write("\7n\2\2\u0101\u0102\7n\2\2\u0102\62\3\2\2\2\u0103\u0104")
        buf.write("\7E\2\2\u0104\u0105\7q\2\2\u0105\u0106\7p\2\2\u0106\u0107")
        buf.write("\7u\2\2\u0107\u0108\7v\2\2\u0108\u0109\7t\2\2\u0109\u010a")
        buf.write("\7w\2\2\u010a\u010b\7e\2\2\u010b\u010c\7v\2\2\u010c\u010d")
        buf.write("\7q\2\2\u010d\u010e\7t\2\2\u010e\64\3\2\2\2\u010f\u0110")
        buf.write("\7F\2\2\u0110\u0111\7g\2\2\u0111\u0112\7u\2\2\u0112\u0113")
        buf.write("\7v\2\2\u0113\u0114\7t\2\2\u0114\u0115\7w\2\2\u0115\u0116")
        buf.write("\7e\2\2\u0116\u0117\7v\2\2\u0117\u0118\7q\2\2\u0118\u0119")
        buf.write("\7t\2\2\u0119\66\3\2\2\2\u011a\u011b\7P\2\2\u011b\u011c")
        buf.write("\7g\2\2\u011c\u011d\7y\2\2\u011d8\3\2\2\2\u011e\u011f")
        buf.write("\7D\2\2\u011f\u0120\7{\2\2\u0120:\3\2\2\2\u0121\u0122")
        buf.write("\7U\2\2\u0122\u0123\7g\2\2\u0123\u0124\7n\2\2\u0124\u0125")
        buf.write("\7h\2\2\u0125<\3\2\2\2\u0126\u0127\7-\2\2\u0127>\3\2\2")
        buf.write("\2\u0128\u0129\7/\2\2\u0129@\3\2\2\2\u012a\u012b\7,\2")
        buf.write("\2\u012bB\3\2\2\2\u012c\u012d\7\61\2\2\u012dD\3\2\2\2")
        buf.write("\u012e\u012f\7\'\2\2\u012fF\3\2\2\2\u0130\u0131\7#\2\2")
        buf.write("\u0131H\3\2\2\2\u0132\u0133\7(\2\2\u0133\u0134\7(\2\2")
        buf.write("\u0134J\3\2\2\2\u0135\u0136\7~\2\2\u0136\u0137\7~\2\2")
        buf.write("\u0137L\3\2\2\2\u0138\u0139\7?\2\2\u0139\u013a\7?\2\2")
        buf.write("\u013aN\3\2\2\2\u013b\u013c\7?\2\2\u013cP\3\2\2\2\u013d")
        buf.write("\u013e\7#\2\2\u013e\u013f\7?\2\2\u013fR\3\2\2\2\u0140")
        buf.write("\u0141\7@\2\2\u0141T\3\2\2\2\u0142\u0143\7@\2\2\u0143")
        buf.write("\u0144\7?\2\2\u0144V\3\2\2\2\u0145\u0146\7>\2\2\u0146")
        buf.write("X\3\2\2\2\u0147\u0148\7>\2\2\u0148\u0149\7?\2\2\u0149")
        buf.write("Z\3\2\2\2\u014a\u014b\7?\2\2\u014b\u014c\7?\2\2\u014c")
        buf.write("\u014d\7\60\2\2\u014d\\\3\2\2\2\u014e\u014f\7-\2\2\u014f")
        buf.write("\u0150\7\60\2\2\u0150^\3\2\2\2\u0151\u0152\7\60\2\2\u0152")
        buf.write("`\3\2\2\2\u0153\u0154\7\60\2\2\u0154\u0155\7\60\2\2\u0155")
        buf.write("b\3\2\2\2\u0156\u0157\7<\2\2\u0157\u0158\7<\2\2\u0158")
        buf.write("d\3\2\2\2\u0159\u015a\7E\2\2\u015a\u015b\7n\2\2\u015b")
        buf.write("\u015c\7c\2\2\u015c\u015d\7u\2\2\u015d\u015e\7u\2\2\u015e")
        buf.write("f\3\2\2\2\u015f\u0160\7H\2\2\u0160\u0161\7n\2\2\u0161")
        buf.write("\u0162\7q\2\2\u0162\u0163\7c\2\2\u0163\u0164\7v\2\2\u0164")
        buf.write("h\3\2\2\2\u0165\u0166\7U\2\2\u0166\u0167\7v\2\2\u0167")
        buf.write("\u0168\7t\2\2\u0168\u0169\7k\2\2\u0169\u016a\7p\2\2\u016a")
        buf.write("\u016b\7i\2\2\u016bj\3\2\2\2\u016c\u016d\7K\2\2\u016d")
        buf.write("\u016e\7p\2\2\u016e\u016f\7v\2\2\u016fl\3\2\2\2\u0170")
        buf.write("\u0171\7V\2\2\u0171\u0172\7t\2\2\u0172\u0173\7w\2\2\u0173")
        buf.write("\u017a\7g\2\2\u0174\u0175\7H\2\2\u0175\u0176\7c\2\2\u0176")
        buf.write("\u0177\7n\2\2\u0177\u0178\7u\2\2\u0178\u017a\7g\2\2\u0179")
        buf.write("\u0170\3\2\2\2\u0179\u0174\3\2\2\2\u017an\3\2\2\2\u017b")
        buf.write("\u017c\5s:\2\u017c\u017d\b8\2\2\u017d\u0188\3\2\2\2\u017e")
        buf.write("\u017f\5u;\2\u017f\u0180\b8\3\2\u0180\u0188\3\2\2\2\u0181")
        buf.write("\u0182\5w<\2\u0182\u0183\b8\4\2\u0183\u0188\3\2\2\2\u0184")
        buf.write("\u0185\5q9\2\u0185\u0186\b8\5\2\u0186\u0188\3\2\2\2\u0187")
        buf.write("\u017b\3\2\2\2\u0187\u017e\3\2\2\2\u0187\u0181\3\2\2\2")
        buf.write("\u0187\u0184\3\2\2\2\u0188p\3\2\2\2\u0189\u018a\7\62\2")
        buf.write("\2\u018a\u018e\7z\2\2\u018b\u018c\7\62\2\2\u018c\u018e")
        buf.write("\7Z\2\2\u018d\u0189\3\2\2\2\u018d\u018b\3\2\2\2\u018e")
        buf.write("\u018f\3\2\2\2\u018f\u01a5\t\5\2\2\u0190\u0191\7\62\2")
        buf.write("\2\u0191\u0195\7z\2\2\u0192\u0193\7\62\2\2\u0193\u0195")
        buf.write("\7Z\2\2\u0194\u0190\3\2\2\2\u0194\u0192\3\2\2\2\u0195")
        buf.write("\u0196\3\2\2\2\u0196\u01a1\t\5\2\2\u0197\u0199\7a\2\2")
        buf.write("\u0198\u0197\3\2\2\2\u0198\u0199\3\2\2\2\u0199\u019b\3")
        buf.write("\2\2\2\u019a\u019c\t\6\2\2\u019b\u019a\3\2\2\2\u019c\u019d")
        buf.write("\3\2\2\2\u019d\u019b\3\2\2\2\u019d\u019e\3\2\2\2\u019e")
        buf.write("\u01a0\3\2\2\2\u019f\u0198\3\2\2\2\u01a0\u01a3\3\2\2\2")
        buf.write("\u01a1\u019f\3\2\2\2\u01a1\u01a2\3\2\2\2\u01a2\u01a5\3")
        buf.write("\2\2\2\u01a3\u01a1\3\2\2\2\u01a4\u018d\3\2\2\2\u01a4\u0194")
        buf.write("\3\2\2\2\u01a5r\3\2\2\2\u01a6\u01a7\7\62\2\2\u01a7\u01b8")
        buf.write("\t\7\2\2\u01a8\u01a9\7\62\2\2\u01a9\u01b4\t\7\2\2\u01aa")
        buf.write("\u01ac\7a\2\2\u01ab\u01aa\3\2\2\2\u01ab\u01ac\3\2\2\2")
        buf.write("\u01ac\u01ae\3\2\2\2\u01ad\u01af\t\b\2\2\u01ae\u01ad\3")
        buf.write("\2\2\2\u01af\u01b0\3\2\2\2\u01b0\u01ae\3\2\2\2\u01b0\u01b1")
        buf.write("\3\2\2\2\u01b1\u01b3\3\2\2\2\u01b2\u01ab\3\2\2\2\u01b3")
        buf.write("\u01b6\3\2\2\2\u01b4\u01b2\3\2\2\2\u01b4\u01b5\3\2\2\2")
        buf.write("\u01b5\u01b8\3\2\2\2\u01b6\u01b4\3\2\2\2\u01b7\u01a6\3")
        buf.write("\2\2\2\u01b7\u01a8\3\2\2\2\u01b8t\3\2\2\2\u01b9\u01ba")
        buf.write("\7\62\2\2\u01ba\u01bb\7d\2\2\u01bb\u01c0\7\63\2\2\u01bc")
        buf.write("\u01bd\7\62\2\2\u01bd\u01be\7D\2\2\u01be\u01c0\7\63\2")
        buf.write("\2\u01bf\u01b9\3\2\2\2\u01bf\u01bc\3\2\2\2\u01c0\u01d6")
        buf.write("\3\2\2\2\u01c1\u01c2\7\62\2\2\u01c2\u01c6\7d\2\2\u01c3")
        buf.write("\u01c4\7\62\2\2\u01c4\u01c6\7D\2\2\u01c5\u01c1\3\2\2\2")
        buf.write("\u01c5\u01c3\3\2\2\2\u01c6\u01c7\3\2\2\2\u01c7\u01d2\t")
        buf.write("\t\2\2\u01c8\u01ca\7a\2\2\u01c9\u01c8\3\2\2\2\u01c9\u01ca")
        buf.write("\3\2\2\2\u01ca\u01cc\3\2\2\2\u01cb\u01cd\t\n\2\2\u01cc")
        buf.write("\u01cb\3\2\2\2\u01cd\u01ce\3\2\2\2\u01ce\u01cc\3\2\2\2")
        buf.write("\u01ce\u01cf\3\2\2\2\u01cf\u01d1\3\2\2\2\u01d0\u01c9\3")
        buf.write("\2\2\2\u01d1\u01d4\3\2\2\2\u01d2\u01d0\3\2\2\2\u01d2\u01d3")
        buf.write("\3\2\2\2\u01d3\u01d6\3\2\2\2\u01d4\u01d2\3\2\2\2\u01d5")
        buf.write("\u01bf\3\2\2\2\u01d5\u01c5\3\2\2\2\u01d6v\3\2\2\2\u01d7")
        buf.write("\u01e7\t\13\2\2\u01d8\u01e3\t\13\2\2\u01d9\u01db\7a\2")
        buf.write("\2\u01da\u01d9\3\2\2\2\u01da\u01db\3\2\2\2\u01db\u01dd")
        buf.write("\3\2\2\2\u01dc\u01de\t\4\2\2\u01dd\u01dc\3\2\2\2\u01de")
        buf.write("\u01df\3\2\2\2\u01df\u01dd\3\2\2\2\u01df\u01e0\3\2\2\2")
        buf.write("\u01e0\u01e2\3\2\2\2\u01e1\u01da\3\2\2\2\u01e2\u01e5\3")
        buf.write("\2\2\2\u01e3\u01e1\3\2\2\2\u01e3\u01e4\3\2\2\2\u01e4\u01e7")
        buf.write("\3\2\2\2\u01e5\u01e3\3\2\2\2\u01e6\u01d7\3\2\2\2\u01e6")
        buf.write("\u01d8\3\2\2\2\u01e7x\3\2\2\2\u01e8\u01e9\7\62\2\2\u01e9")
        buf.write("\u01ed\7z\2\2\u01ea\u01eb\7\62\2\2\u01eb\u01ed\7Z\2\2")
        buf.write("\u01ec\u01e8\3\2\2\2\u01ec\u01ea\3\2\2\2\u01ed\u01ee\3")
        buf.write("\2\2\2\u01ee\u0204\t\6\2\2\u01ef\u01f0\7\62\2\2\u01f0")
        buf.write("\u01f4\7z\2\2\u01f1\u01f2\7\62\2\2\u01f2\u01f4\7Z\2\2")
        buf.write("\u01f3\u01ef\3\2\2\2\u01f3\u01f1\3\2\2\2\u01f4\u01f5\3")
        buf.write("\2\2\2\u01f5\u0200\t\5\2\2\u01f6\u01f8\7a\2\2\u01f7\u01f6")
        buf.write("\3\2\2\2\u01f7\u01f8\3\2\2\2\u01f8\u01fa\3\2\2\2\u01f9")
        buf.write("\u01fb\t\6\2\2\u01fa\u01f9\3\2\2\2\u01fb\u01fc\3\2\2\2")
        buf.write("\u01fc\u01fa\3\2\2\2\u01fc\u01fd\3\2\2\2\u01fd\u01ff\3")
        buf.write("\2\2\2\u01fe\u01f7\3\2\2\2\u01ff\u0202\3\2\2\2\u0200\u01fe")
        buf.write("\3\2\2\2\u0200\u0201\3\2\2\2\u0201\u0204\3\2\2\2\u0202")
        buf.write("\u0200\3\2\2\2\u0203\u01ec\3\2\2\2\u0203\u01f3\3\2\2\2")
        buf.write("\u0204z\3\2\2\2\u0205\u0206\7\62\2\2\u0206\u0217\t\b\2")
        buf.write("\2\u0207\u0208\7\62\2\2\u0208\u0213\t\7\2\2\u0209\u020b")
        buf.write("\7a\2\2\u020a\u0209\3\2\2\2\u020a\u020b\3\2\2\2\u020b")
        buf.write("\u020d\3\2\2\2\u020c\u020e\t\b\2\2\u020d\u020c\3\2\2\2")
        buf.write("\u020e\u020f\3\2\2\2\u020f\u020d\3\2\2\2\u020f\u0210\3")
        buf.write("\2\2\2\u0210\u0212\3\2\2\2\u0211\u020a\3\2\2\2\u0212\u0215")
        buf.write("\3\2\2\2\u0213\u0211\3\2\2\2\u0213\u0214\3\2\2\2\u0214")
        buf.write("\u0217\3\2\2\2\u0215\u0213\3\2\2\2\u0216\u0205\3\2\2\2")
        buf.write("\u0216\u0207\3\2\2\2\u0217|\3\2\2\2\u0218\u0219\7\62\2")
        buf.write("\2\u0219\u021d\7d\2\2\u021a\u021b\7\62\2\2\u021b\u021d")
        buf.write("\7D\2\2\u021c\u0218\3\2\2\2\u021c\u021a\3\2\2\2\u021d")
        buf.write("\u021e\3\2\2\2\u021e\u0234\t\n\2\2\u021f\u0220\7\62\2")
        buf.write("\2\u0220\u0224\7d\2\2\u0221\u0222\7\62\2\2\u0222\u0224")
        buf.write("\7D\2\2\u0223\u021f\3\2\2\2\u0223\u0221\3\2\2\2\u0224")
        buf.write("\u0225\3\2\2\2\u0225\u0230\t\t\2\2\u0226\u0228\7a\2\2")
        buf.write("\u0227\u0226\3\2\2\2\u0227\u0228\3\2\2\2\u0228\u022a\3")
        buf.write("\2\2\2\u0229\u022b\t\n\2\2\u022a\u0229\3\2\2\2\u022b\u022c")
        buf.write("\3\2\2\2\u022c\u022a\3\2\2\2\u022c\u022d\3\2\2\2\u022d")
        buf.write("\u022f\3\2\2\2\u022e\u0227\3\2\2\2\u022f\u0232\3\2\2\2")
        buf.write("\u0230\u022e\3\2\2\2\u0230\u0231\3\2\2\2\u0231\u0234\3")
        buf.write("\2\2\2\u0232\u0230\3\2\2\2\u0233\u021c\3\2\2\2\u0233\u0223")
        buf.write("\3\2\2\2\u0234~\3\2\2\2\u0235\u0245\t\4\2\2\u0236\u0241")
        buf.write("\t\13\2\2\u0237\u0239\7a\2\2\u0238\u0237\3\2\2\2\u0238")
        buf.write("\u0239\3\2\2\2\u0239\u023b\3\2\2\2\u023a\u023c\t\4\2\2")
        buf.write("\u023b\u023a\3\2\2\2\u023c\u023d\3\2\2\2\u023d\u023b\3")
        buf.write("\2\2\2\u023d\u023e\3\2\2\2\u023e\u0240\3\2\2\2\u023f\u0238")
        buf.write("\3\2\2\2\u0240\u0243\3\2\2\2\u0241\u023f\3\2\2\2\u0241")
        buf.write("\u0242\3\2\2\2\u0242\u0245\3\2\2\2\u0243\u0241\3\2\2\2")
        buf.write("\u0244\u0235\3\2\2\2\u0244\u0236\3\2\2\2\u0245\u0080\3")
        buf.write("\2\2\2\u0246\u0247\5{>\2\u0247\u0248\bA\6\2\u0248\u0253")
        buf.write("\3\2\2\2\u0249\u024a\5}?\2\u024a\u024b\bA\7\2\u024b\u0253")
        buf.write("\3\2\2\2\u024c\u024d\5\177@\2\u024d\u024e\bA\b\2\u024e")
        buf.write("\u0253\3\2\2\2\u024f\u0250\5y=\2\u0250\u0251\bA\t\2\u0251")
        buf.write("\u0253\3\2\2\2\u0252\u0246\3\2\2\2\u0252\u0249\3\2\2\2")
        buf.write("\u0252\u024c\3\2\2\2\u0252\u024f\3\2\2\2\u0253\u0082\3")
        buf.write("\2\2\2\u0254\u0255\7)\2\2\u0255\u0259\7$\2\2\u0256\u0259")
        buf.write("\n\f\2\2\u0257\u0259\5\u0085C\2\u0258\u0254\3\2\2\2\u0258")
        buf.write("\u0256\3\2\2\2\u0258\u0257\3\2\2\2\u0259\u0084\3\2\2\2")
        buf.write("\u025a\u025b\7^\2\2\u025b\u025c\t\r\2\2\u025c\u0086\3")
        buf.write("\2\2\2\u025d\u025e\7^\2\2\u025e\u0261\n\r\2\2\u025f\u0261")
        buf.write("\7^\2\2\u0260\u025d\3\2\2\2\u0260\u025f\3\2\2\2\u0261")
        buf.write("\u0088\3\2\2\2\u0262\u0266\7$\2\2\u0263\u0265\5\u0083")
        buf.write("B\2\u0264\u0263\3\2\2\2\u0265\u0268\3\2\2\2\u0266\u0264")
        buf.write("\3\2\2\2\u0266\u0267\3\2\2\2\u0267\u0269\3\2\2\2\u0268")
        buf.write("\u0266\3\2\2\2\u0269\u026a\7$\2\2\u026a\u026b\bE\n\2\u026b")
        buf.write("\u008a\3\2\2\2\u026c\u0270\7$\2\2\u026d\u026f\5\u0083")
        buf.write("B\2\u026e\u026d\3\2\2\2\u026f\u0272\3\2\2\2\u0270\u026e")
        buf.write("\3\2\2\2\u0270\u0271\3\2\2\2\u0271\u0273\3\2\2\2\u0272")
        buf.write("\u0270\3\2\2\2\u0273\u0274\5\u0087D\2\u0274\u0275\bF\13")
        buf.write("\2\u0275\u008c\3\2\2\2\u0276\u027a\7$\2\2\u0277\u0279")
        buf.write("\5\u0083B\2\u0278\u0277\3\2\2\2\u0279\u027c\3\2\2\2\u027a")
        buf.write("\u0278\3\2\2\2\u027a\u027b\3\2\2\2\u027b\u027d\3\2\2\2")
        buf.write("\u027c\u027a\3\2\2\2\u027d\u027e\bG\f\2\u027e\u008e\3")
        buf.write("\2\2\2\u027f\u0280\5\177@\2\u0280\u0283\5_\60\2\u0281")
        buf.write("\u0284\5\33\16\2\u0282\u0284\5\31\r\2\u0283\u0281\3\2")
        buf.write("\2\2\u0283\u0282\3\2\2\2\u0283\u0284\3\2\2\2\u0284\u0285")
        buf.write("\3\2\2\2\u0285\u0286\bH\r\2\u0286\u0298\3\2\2\2\u0287")
        buf.write("\u0288\5\177@\2\u0288\u0289\5\31\r\2\u0289\u028a\bH\16")
        buf.write("\2\u028a\u0298\3\2\2\2\u028b\u028d\5\177@\2\u028c\u028b")
        buf.write("\3\2\2\2\u028c\u028d\3\2\2\2\u028d\u028e\3\2\2\2\u028e")
        buf.write("\u028f\5_\60\2\u028f\u0290\5\33\16\2\u0290\u0291\5\31")
        buf.write("\r\2\u0291\u0292\bH\17\2\u0292\u0298\3\2\2\2\u0293\u0294")
        buf.write("\5_\60\2\u0294\u0295\5\31\r\2\u0295\u0296\bH\20\2\u0296")
        buf.write("\u0298\3\2\2\2\u0297\u027f\3\2\2\2\u0297\u0287\3\2\2\2")
        buf.write("\u0297\u028c\3\2\2\2\u0297\u0293\3\2\2\2\u0298\u0090\3")
        buf.write("\2\2\2\u0299\u029d\t\16\2\2\u029a\u029c\t\17\2\2\u029b")
        buf.write("\u029a\3\2\2\2\u029c\u029f\3\2\2\2\u029d\u029b\3\2\2\2")
        buf.write("\u029d\u029e\3\2\2\2\u029e\u0092\3\2\2\2\u029f\u029d\3")
        buf.write("\2\2\2\u02a0\u02a2\7&\2\2\u02a1\u02a3\t\17\2\2\u02a2\u02a1")
        buf.write("\3\2\2\2\u02a3\u02a4\3\2\2\2\u02a4\u02a2\3\2\2\2\u02a4")
        buf.write("\u02a5\3\2\2\2\u02a5\u0094\3\2\2\2\u02a6\u02a7\7%\2\2")
        buf.write("\u02a7\u02a8\7%\2\2\u02a8\u02ac\3\2\2\2\u02a9\u02ab\13")
        buf.write("\2\2\2\u02aa\u02a9\3\2\2\2\u02ab\u02ae\3\2\2\2\u02ac\u02ad")
        buf.write("\3\2\2\2\u02ac\u02aa\3\2\2\2\u02ad\u02af\3\2\2\2\u02ae")
        buf.write("\u02ac\3\2\2\2\u02af\u02b0\7%\2\2\u02b0\u02b1\7%\2\2\u02b1")
        buf.write("\u02b2\3\2\2\2\u02b2\u02b3\bK\21\2\u02b3\u0096\3\2\2\2")
        buf.write("\u02b4\u02b6\t\20\2\2\u02b5\u02b4\3\2\2\2\u02b6\u02b7")
        buf.write("\3\2\2\2\u02b7\u02b5\3\2\2\2\u02b7\u02b8\3\2\2\2\u02b8")
        buf.write("\u02b9\3\2\2\2\u02b9\u02ba\bL\21\2\u02ba\u0098\3\2\2\2")
        buf.write("\u02bb\u02bc\13\2\2\2\u02bc\u02bd\bM\22\2\u02bd\u009a")
        buf.write("\3\2\2\2<\2\u00b7\u00be\u0179\u0187\u018d\u0194\u0198")
        buf.write("\u019d\u01a1\u01a4\u01ab\u01b0\u01b4\u01b7\u01bf\u01c5")
        buf.write("\u01c9\u01ce\u01d2\u01d5\u01da\u01df\u01e3\u01e6\u01ec")
        buf.write("\u01f3\u01f7\u01fc\u0200\u0203\u020a\u020f\u0213\u0216")
        buf.write("\u021c\u0223\u0227\u022c\u0230\u0233\u0238\u023d\u0241")
        buf.write("\u0244\u0252\u0258\u0260\u0266\u0270\u027a\u0283\u028c")
        buf.write("\u0297\u029d\u02a4\u02ac\u02b7\23\38\2\38\3\38\4\38\5")
        buf.write("\3A\6\3A\7\3A\b\3A\t\3E\n\3F\13\3G\f\3H\r\3H\16\3H\17")
        buf.write("\3H\20\b\2\2\3M\21")
        return buf.getvalue()


class D96Lexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    VAL = 1
    VAR = 2
    LP = 3
    RP = 4
    LCB = 5
    RCB = 6
    LSB = 7
    RSB = 8
    SEMI = 9
    COMMA = 10
    COLON = 11
    BREAK = 12
    CONTINUE = 13
    IF = 14
    ELSEIF = 15
    ELSE = 16
    FOREACH = 17
    ARRAY = 18
    IN = 19
    BOOLEAN = 20
    RETURN = 21
    NULL = 22
    CONSTRUCTOR = 23
    DESTRUCTOR = 24
    NEW = 25
    BY = 26
    SELF = 27
    ADD = 28
    SUB = 29
    MUL = 30
    DIV = 31
    MOD = 32
    NOT = 33
    AND = 34
    OR = 35
    EQUAL = 36
    ASSIGN = 37
    NOTEQUAL = 38
    GT = 39
    GTE = 40
    LT = 41
    LTE = 42
    EQUAL_STR = 43
    ADD_STR = 44
    DOT = 45
    DOTDOT = 46
    SCOPE = 47
    CLASS = 48
    FLOAT_TYPE = 49
    STRING = 50
    INT_TYPE = 51
    BOOL_LITERAL = 52
    ARRAY_SIZE = 53
    INTEGER_LITERAL = 54
    STRING_LITERAL = 55
    ILLEGAL_ESCAPE = 56
    UNCLOSE_STRING = 57
    REAL_LITERAL = 58
    NORMAL_ID = 59
    DOLLAR_ID = 60
    BLOCK_COMMENT = 61
    WS = 62
    ERROR_CHAR = 63

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'Val'", "'Var'", "'('", "')'", "'{'", "'}'", "'['", "']'", 
            "';'", "','", "':'", "'Break'", "'Continue'", "'If'", "'Elseif'", 
            "'Else'", "'Foreach'", "'Array'", "'In'", "'Boolean'", "'Return'", 
            "'Null'", "'Constructor'", "'Destructor'", "'New'", "'By'", 
            "'Self'", "'+'", "'-'", "'*'", "'/'", "'%'", "'!'", "'&&'", 
            "'||'", "'=='", "'='", "'!='", "'>'", "'>='", "'<'", "'<='", 
            "'==.'", "'+.'", "'.'", "'..'", "'::'", "'Class'", "'Float'", 
            "'String'", "'Int'" ]

    symbolicNames = [ "<INVALID>",
            "VAL", "VAR", "LP", "RP", "LCB", "RCB", "LSB", "RSB", "SEMI", 
            "COMMA", "COLON", "BREAK", "CONTINUE", "IF", "ELSEIF", "ELSE", 
            "FOREACH", "ARRAY", "IN", "BOOLEAN", "RETURN", "NULL", "CONSTRUCTOR", 
            "DESTRUCTOR", "NEW", "BY", "SELF", "ADD", "SUB", "MUL", "DIV", 
            "MOD", "NOT", "AND", "OR", "EQUAL", "ASSIGN", "NOTEQUAL", "GT", 
            "GTE", "LT", "LTE", "EQUAL_STR", "ADD_STR", "DOT", "DOTDOT", 
            "SCOPE", "CLASS", "FLOAT_TYPE", "STRING", "INT_TYPE", "BOOL_LITERAL", 
            "ARRAY_SIZE", "INTEGER_LITERAL", "STRING_LITERAL", "ILLEGAL_ESCAPE", 
            "UNCLOSE_STRING", "REAL_LITERAL", "NORMAL_ID", "DOLLAR_ID", 
            "BLOCK_COMMENT", "WS", "ERROR_CHAR" ]

    ruleNames = [ "VAL", "VAR", "LP", "RP", "LCB", "RCB", "LSB", "RSB", 
                  "SEMI", "COMMA", "COLON", "EXPONENT", "DEC_DIGIT", "BREAK", 
                  "CONTINUE", "IF", "ELSEIF", "ELSE", "FOREACH", "ARRAY", 
                  "IN", "BOOLEAN", "RETURN", "NULL", "CONSTRUCTOR", "DESTRUCTOR", 
                  "NEW", "BY", "SELF", "ADD", "SUB", "MUL", "DIV", "MOD", 
                  "NOT", "AND", "OR", "EQUAL", "ASSIGN", "NOTEQUAL", "GT", 
                  "GTE", "LT", "LTE", "EQUAL_STR", "ADD_STR", "DOT", "DOTDOT", 
                  "SCOPE", "CLASS", "FLOAT_TYPE", "STRING", "INT_TYPE", 
                  "BOOL_LITERAL", "ARRAY_SIZE", "ARRAY_SIZE_HEX", "ARRAY_SIZE_OCT", 
                  "ARRAY_SIZE_BIN", "ARRAY_SIZE_DEC", "HEX_TYPE", "OCT_TYPE", 
                  "BIN_TYPE", "DEC_TYPE", "INTEGER_LITERAL", "STR", "ESC_SEQ", 
                  "ESC_ILLEGAL", "STRING_LITERAL", "ILLEGAL_ESCAPE", "UNCLOSE_STRING", 
                  "REAL_LITERAL", "NORMAL_ID", "DOLLAR_ID", "BLOCK_COMMENT", 
                  "WS", "ERROR_CHAR" ]

    grammarFileName = "D96.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.8")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


    def action(self, localctx:RuleContext, ruleIndex:int, actionIndex:int):
        if self._actions is None:
            actions = dict()
            actions[54] = self.ARRAY_SIZE_action 
            actions[63] = self.INTEGER_LITERAL_action 
            actions[67] = self.STRING_LITERAL_action 
            actions[68] = self.ILLEGAL_ESCAPE_action 
            actions[69] = self.UNCLOSE_STRING_action 
            actions[70] = self.REAL_LITERAL_action 
            actions[75] = self.ERROR_CHAR_action 
            self._actions = actions
        action = self._actions.get(ruleIndex, None)
        if action is not None:
            action(localctx, actionIndex)
        else:
            raise Exception("No registered action for:" + str(ruleIndex))


    def ARRAY_SIZE_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 0:
            self.text = self.text.replace('_', '')
     

        if actionIndex == 1:
            self.text = self.text.replace('_', '')
     

        if actionIndex == 2:
            self.text = self.text.replace('_', '')
     

        if actionIndex == 3:
            self.text = self.text.replace('_', '')
     

    def INTEGER_LITERAL_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 4:
            self.text = self.text.replace('_', '')
     

        if actionIndex == 5:
            self.text = self.text.replace('_', '')
     

        if actionIndex == 6:
            self.text = self.text.replace('_', '')
     

        if actionIndex == 7:
            self.text = self.text.replace('_', '')
     

    def STRING_LITERAL_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 8:
             
                y = str(self.text)
                illegalEscape = ['\b', '\t', '\n', '\f', '\r', '\a', '\v']
                for i in illegalEscape:
                    ch = y.find(i)
                    if ch >= 0:
                        if i == '\n':
                            raise UncloseString(y[1:ch-1])
                        raise UncloseString(y[1:ch])
                    
                if y[-2:] == '\'"' and y[-3] != '\\':
                    raise UncloseString(y[1:])
                self.text = y[1:-1]

     

    def ILLEGAL_ESCAPE_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 9:

                raise IllegalEscape(str(self.text)[1:])

     

    def UNCLOSE_STRING_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 10:

                raise UncloseString(str(self.text)[1:])

     

    def REAL_LITERAL_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 11:
            self.text = self.text.replace('_', '')
     

        if actionIndex == 12:
            self.text = self.text.replace('_', '')
     

        if actionIndex == 13:
            self.text = self.text.replace('_', '')
     

        if actionIndex == 14:
            self.text = self.text.replace('_', '')
     

    def ERROR_CHAR_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 15:
            raise ErrorToken(self.text)
     


