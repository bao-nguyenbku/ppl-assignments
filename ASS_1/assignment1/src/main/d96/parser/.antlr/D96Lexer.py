# Generated from e:\HCMUT\PRINCIPLES_OF_PROGRAMMING_LANGUAGE\ppl-assignments\ASS_1\assignment1\src\main\d96\parser\D96.g4 by ANTLR 4.8
from antlr4 import *
from io import StringIO
from typing.io import TextIO
import sys


from lexererr import *



def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2C")
        buf.write("\u02b1\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7")
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
        buf.write("L\4M\tM\4N\tN\4O\tO\3\2\3\2\3\2\3\2\3\3\3\3\3\3\3\3\3")
        buf.write("\4\3\4\3\5\3\5\3\6\3\6\3\7\3\7\3\b\3\b\3\t\3\t\3\n\3\n")
        buf.write("\3\13\3\13\3\f\3\f\3\r\3\r\5\r\u00bc\n\r\3\r\3\r\3\16")
        buf.write("\6\16\u00c1\n\16\r\16\16\16\u00c2\3\17\3\17\3\17\3\17")
        buf.write("\3\17\3\17\3\20\3\20\3\20\3\20\3\20\3\20\3\20\3\20\3\20")
        buf.write("\3\21\3\21\3\21\3\22\3\22\3\22\3\22\3\22\3\22\3\22\3\23")
        buf.write("\3\23\3\23\3\23\3\23\3\24\3\24\3\24\3\24\3\24\3\24\3\24")
        buf.write("\3\24\3\25\3\25\3\25\3\25\3\25\3\26\3\26\3\26\3\26\3\26")
        buf.write("\3\26\3\27\3\27\3\27\3\27\3\27\3\27\3\30\3\30\3\30\3\31")
        buf.write("\3\31\3\31\3\31\3\31\3\31\3\31\3\31\3\32\3\32\3\32\3\32")
        buf.write("\3\32\3\32\3\32\3\33\3\33\3\33\3\33\3\33\3\34\3\34\3\34")
        buf.write("\3\34\3\34\3\34\3\34\3\34\3\34\3\34\3\34\3\34\3\35\3\35")
        buf.write("\3\35\3\35\3\35\3\35\3\35\3\35\3\35\3\35\3\35\3\36\3\36")
        buf.write("\3\36\3\36\3\37\3\37\3\37\3 \3 \3 \3 \3 \3!\3!\3\"\3\"")
        buf.write("\3#\3#\3$\3$\3%\3%\3&\3&\3\'\3\'\3\'\3(\3(\3(\3)\3)\3")
        buf.write(")\3*\3*\3+\3+\3+\3,\3,\3-\3-\3-\3.\3.\3/\3/\3/\3\60\3")
        buf.write("\60\3\60\3\60\3\61\3\61\3\61\3\62\3\62\3\63\3\63\3\63")
        buf.write("\3\64\3\64\3\64\3\65\3\65\3\65\3\65\3\65\3\65\3\66\3\66")
        buf.write("\3\66\3\66\3\66\3\66\3\67\3\67\3\67\3\67\3\67\3\67\3\67")
        buf.write("\38\38\38\38\39\39\59\u0182\n9\3:\3:\3:\3:\5:\u0188\n")
        buf.write(":\3;\3;\3;\3;\5;\u018e\n;\3;\3;\3;\3;\3;\5;\u0195\n;\3")
        buf.write(";\3;\5;\u0199\n;\3;\6;\u019c\n;\r;\16;\u019d\7;\u01a0")
        buf.write("\n;\f;\16;\u01a3\13;\5;\u01a5\n;\3<\3<\3<\3<\3<\5<\u01ac")
        buf.write("\n<\3<\6<\u01af\n<\r<\16<\u01b0\7<\u01b3\n<\f<\16<\u01b6")
        buf.write("\13<\5<\u01b8\n<\3=\3=\3=\3=\3=\3=\5=\u01c0\n=\3=\3=\3")
        buf.write("=\3=\5=\u01c6\n=\3=\3=\5=\u01ca\n=\3=\6=\u01cd\n=\r=\16")
        buf.write("=\u01ce\7=\u01d1\n=\f=\16=\u01d4\13=\5=\u01d6\n=\3>\3")
        buf.write(">\3>\5>\u01db\n>\3>\6>\u01de\n>\r>\16>\u01df\7>\u01e2")
        buf.write("\n>\f>\16>\u01e5\13>\5>\u01e7\n>\3?\3?\3?\3?\5?\u01ed")
        buf.write("\n?\3?\3?\3?\3?\3?\5?\u01f4\n?\3?\3?\5?\u01f8\n?\3?\6")
        buf.write("?\u01fb\n?\r?\16?\u01fc\7?\u01ff\n?\f?\16?\u0202\13?\5")
        buf.write("?\u0204\n?\3@\3@\3@\3@\3@\5@\u020b\n@\3@\6@\u020e\n@\r")
        buf.write("@\16@\u020f\7@\u0212\n@\f@\16@\u0215\13@\5@\u0217\n@\3")
        buf.write("A\3A\3A\3A\5A\u021d\nA\3A\3A\3A\3A\3A\5A\u0224\nA\3A\3")
        buf.write("A\5A\u0228\nA\3A\6A\u022b\nA\rA\16A\u022c\7A\u022f\nA")
        buf.write("\fA\16A\u0232\13A\5A\u0234\nA\3B\3B\3B\5B\u0239\nB\3B")
        buf.write("\6B\u023c\nB\rB\16B\u023d\7B\u0240\nB\fB\16B\u0243\13")
        buf.write("B\5B\u0245\nB\3C\3C\3C\3C\5C\u024b\nC\3D\3D\3D\3D\5D\u0251")
        buf.write("\nD\3E\3E\3E\3F\3F\3F\5F\u0259\nF\3G\3G\7G\u025d\nG\f")
        buf.write("G\16G\u0260\13G\3G\3G\3G\3H\3H\7H\u0267\nH\fH\16H\u026a")
        buf.write("\13H\3H\3H\3H\3I\3I\7I\u0271\nI\fI\16I\u0274\13I\3I\3")
        buf.write("I\3J\3J\3J\3J\5J\u027c\nJ\3J\3J\3J\3J\5J\u0282\nJ\3J\3")
        buf.write("J\3J\3J\3J\3J\3J\5J\u028b\nJ\3K\3K\7K\u028f\nK\fK\16K")
        buf.write("\u0292\13K\3L\3L\6L\u0296\nL\rL\16L\u0297\3M\3M\3M\3M")
        buf.write("\7M\u029e\nM\fM\16M\u02a1\13M\3M\3M\3M\3M\3M\3N\6N\u02a9")
        buf.write("\nN\rN\16N\u02aa\3N\3N\3O\3O\3O\3\u029f\2P\3\3\5\4\7\5")
        buf.write("\t\6\13\7\r\b\17\t\21\n\23\13\25\f\27\r\31\2\33\2\35\16")
        buf.write("\37\17!\20#\21%\22\'\23)\24+\25-\26/\27\61\30\63\31\65")
        buf.write("\32\67\339\34;\35=\36?\37A C!E\"G#I$K%M&O\'Q(S)U*W+Y,")
        buf.write("[-]._/a\60c\61e\62g\63i\64k\65m\66o\67q8s9u\2w\2y\2{\2")
        buf.write("}\2\177\2\u0081\2\u0083\2\u0085:\u0087\2\u0089\2\u008b")
        buf.write("\2\u008d;\u008f<\u0091=\u0093>\u0095?\u0097@\u0099A\u009b")
        buf.write("B\u009dC\3\2\21\4\2GGgg\4\2--//\3\2\62;\4\2\63;CH\4\2")
        buf.write("\62;CH\3\2\639\3\2\629\3\2\63\63\3\2\62\63\3\2\63;\4\2")
        buf.write("$$^^\t\2))^^ddhhppttvv\5\2C\\aac|\6\2\62;C\\aac|\5\2\13")
        buf.write("\f\17\17\"\"\2\u02e4\2\3\3\2\2\2\2\5\3\2\2\2\2\7\3\2\2")
        buf.write("\2\2\t\3\2\2\2\2\13\3\2\2\2\2\r\3\2\2\2\2\17\3\2\2\2\2")
        buf.write("\21\3\2\2\2\2\23\3\2\2\2\2\25\3\2\2\2\2\27\3\2\2\2\2\35")
        buf.write("\3\2\2\2\2\37\3\2\2\2\2!\3\2\2\2\2#\3\2\2\2\2%\3\2\2\2")
        buf.write("\2\'\3\2\2\2\2)\3\2\2\2\2+\3\2\2\2\2-\3\2\2\2\2/\3\2\2")
        buf.write("\2\2\61\3\2\2\2\2\63\3\2\2\2\2\65\3\2\2\2\2\67\3\2\2\2")
        buf.write("\29\3\2\2\2\2;\3\2\2\2\2=\3\2\2\2\2?\3\2\2\2\2A\3\2\2")
        buf.write("\2\2C\3\2\2\2\2E\3\2\2\2\2G\3\2\2\2\2I\3\2\2\2\2K\3\2")
        buf.write("\2\2\2M\3\2\2\2\2O\3\2\2\2\2Q\3\2\2\2\2S\3\2\2\2\2U\3")
        buf.write("\2\2\2\2W\3\2\2\2\2Y\3\2\2\2\2[\3\2\2\2\2]\3\2\2\2\2_")
        buf.write("\3\2\2\2\2a\3\2\2\2\2c\3\2\2\2\2e\3\2\2\2\2g\3\2\2\2\2")
        buf.write("i\3\2\2\2\2k\3\2\2\2\2m\3\2\2\2\2o\3\2\2\2\2q\3\2\2\2")
        buf.write("\2s\3\2\2\2\2\u0085\3\2\2\2\2\u008d\3\2\2\2\2\u008f\3")
        buf.write("\2\2\2\2\u0091\3\2\2\2\2\u0093\3\2\2\2\2\u0095\3\2\2\2")
        buf.write("\2\u0097\3\2\2\2\2\u0099\3\2\2\2\2\u009b\3\2\2\2\2\u009d")
        buf.write("\3\2\2\2\3\u009f\3\2\2\2\5\u00a3\3\2\2\2\7\u00a7\3\2\2")
        buf.write("\2\t\u00a9\3\2\2\2\13\u00ab\3\2\2\2\r\u00ad\3\2\2\2\17")
        buf.write("\u00af\3\2\2\2\21\u00b1\3\2\2\2\23\u00b3\3\2\2\2\25\u00b5")
        buf.write("\3\2\2\2\27\u00b7\3\2\2\2\31\u00b9\3\2\2\2\33\u00c0\3")
        buf.write("\2\2\2\35\u00c4\3\2\2\2\37\u00ca\3\2\2\2!\u00d3\3\2\2")
        buf.write("\2#\u00d6\3\2\2\2%\u00dd\3\2\2\2\'\u00e2\3\2\2\2)\u00ea")
        buf.write("\3\2\2\2+\u00ef\3\2\2\2-\u00f5\3\2\2\2/\u00fb\3\2\2\2")
        buf.write("\61\u00fe\3\2\2\2\63\u0106\3\2\2\2\65\u010d\3\2\2\2\67")
        buf.write("\u0112\3\2\2\29\u011e\3\2\2\2;\u0129\3\2\2\2=\u012d\3")
        buf.write("\2\2\2?\u0130\3\2\2\2A\u0135\3\2\2\2C\u0137\3\2\2\2E\u0139")
        buf.write("\3\2\2\2G\u013b\3\2\2\2I\u013d\3\2\2\2K\u013f\3\2\2\2")
        buf.write("M\u0141\3\2\2\2O\u0144\3\2\2\2Q\u0147\3\2\2\2S\u014a\3")
        buf.write("\2\2\2U\u014c\3\2\2\2W\u014f\3\2\2\2Y\u0151\3\2\2\2[\u0154")
        buf.write("\3\2\2\2]\u0156\3\2\2\2_\u0159\3\2\2\2a\u015d\3\2\2\2")
        buf.write("c\u0160\3\2\2\2e\u0162\3\2\2\2g\u0165\3\2\2\2i\u0168\3")
        buf.write("\2\2\2k\u016e\3\2\2\2m\u0174\3\2\2\2o\u017b\3\2\2\2q\u0181")
        buf.write("\3\2\2\2s\u0187\3\2\2\2u\u01a4\3\2\2\2w\u01b7\3\2\2\2")
        buf.write("y\u01d5\3\2\2\2{\u01e6\3\2\2\2}\u0203\3\2\2\2\177\u0216")
        buf.write("\3\2\2\2\u0081\u0233\3\2\2\2\u0083\u0244\3\2\2\2\u0085")
        buf.write("\u024a\3\2\2\2\u0087\u0250\3\2\2\2\u0089\u0252\3\2\2\2")
        buf.write("\u008b\u0258\3\2\2\2\u008d\u025a\3\2\2\2\u008f\u0264\3")
        buf.write("\2\2\2\u0091\u026e\3\2\2\2\u0093\u028a\3\2\2\2\u0095\u028c")
        buf.write("\3\2\2\2\u0097\u0293\3\2\2\2\u0099\u0299\3\2\2\2\u009b")
        buf.write("\u02a8\3\2\2\2\u009d\u02ae\3\2\2\2\u009f\u00a0\7X\2\2")
        buf.write("\u00a0\u00a1\7c\2\2\u00a1\u00a2\7n\2\2\u00a2\4\3\2\2\2")
        buf.write("\u00a3\u00a4\7X\2\2\u00a4\u00a5\7c\2\2\u00a5\u00a6\7t")
        buf.write("\2\2\u00a6\6\3\2\2\2\u00a7\u00a8\7*\2\2\u00a8\b\3\2\2")
        buf.write("\2\u00a9\u00aa\7+\2\2\u00aa\n\3\2\2\2\u00ab\u00ac\7}\2")
        buf.write("\2\u00ac\f\3\2\2\2\u00ad\u00ae\7\177\2\2\u00ae\16\3\2")
        buf.write("\2\2\u00af\u00b0\7]\2\2\u00b0\20\3\2\2\2\u00b1\u00b2\7")
        buf.write("_\2\2\u00b2\22\3\2\2\2\u00b3\u00b4\7=\2\2\u00b4\24\3\2")
        buf.write("\2\2\u00b5\u00b6\7.\2\2\u00b6\26\3\2\2\2\u00b7\u00b8\7")
        buf.write("<\2\2\u00b8\30\3\2\2\2\u00b9\u00bb\t\2\2\2\u00ba\u00bc")
        buf.write("\t\3\2\2\u00bb\u00ba\3\2\2\2\u00bb\u00bc\3\2\2\2\u00bc")
        buf.write("\u00bd\3\2\2\2\u00bd\u00be\5\33\16\2\u00be\32\3\2\2\2")
        buf.write("\u00bf\u00c1\t\4\2\2\u00c0\u00bf\3\2\2\2\u00c1\u00c2\3")
        buf.write("\2\2\2\u00c2\u00c0\3\2\2\2\u00c2\u00c3\3\2\2\2\u00c3\34")
        buf.write("\3\2\2\2\u00c4\u00c5\7D\2\2\u00c5\u00c6\7t\2\2\u00c6\u00c7")
        buf.write("\7g\2\2\u00c7\u00c8\7c\2\2\u00c8\u00c9\7m\2\2\u00c9\36")
        buf.write("\3\2\2\2\u00ca\u00cb\7E\2\2\u00cb\u00cc\7q\2\2\u00cc\u00cd")
        buf.write("\7p\2\2\u00cd\u00ce\7v\2\2\u00ce\u00cf\7k\2\2\u00cf\u00d0")
        buf.write("\7p\2\2\u00d0\u00d1\7w\2\2\u00d1\u00d2\7g\2\2\u00d2 \3")
        buf.write("\2\2\2\u00d3\u00d4\7K\2\2\u00d4\u00d5\7h\2\2\u00d5\"\3")
        buf.write("\2\2\2\u00d6\u00d7\7G\2\2\u00d7\u00d8\7n\2\2\u00d8\u00d9")
        buf.write("\7u\2\2\u00d9\u00da\7g\2\2\u00da\u00db\7k\2\2\u00db\u00dc")
        buf.write("\7h\2\2\u00dc$\3\2\2\2\u00dd\u00de\7G\2\2\u00de\u00df")
        buf.write("\7n\2\2\u00df\u00e0\7u\2\2\u00e0\u00e1\7g\2\2\u00e1&\3")
        buf.write("\2\2\2\u00e2\u00e3\7H\2\2\u00e3\u00e4\7q\2\2\u00e4\u00e5")
        buf.write("\7t\2\2\u00e5\u00e6\7g\2\2\u00e6\u00e7\7c\2\2\u00e7\u00e8")
        buf.write("\7e\2\2\u00e8\u00e9\7j\2\2\u00e9(\3\2\2\2\u00ea\u00eb")
        buf.write("\7V\2\2\u00eb\u00ec\7t\2\2\u00ec\u00ed\7w\2\2\u00ed\u00ee")
        buf.write("\7g\2\2\u00ee*\3\2\2\2\u00ef\u00f0\7H\2\2\u00f0\u00f1")
        buf.write("\7c\2\2\u00f1\u00f2\7n\2\2\u00f2\u00f3\7u\2\2\u00f3\u00f4")
        buf.write("\7g\2\2\u00f4,\3\2\2\2\u00f5\u00f6\7C\2\2\u00f6\u00f7")
        buf.write("\7t\2\2\u00f7\u00f8\7t\2\2\u00f8\u00f9\7c\2\2\u00f9\u00fa")
        buf.write("\7{\2\2\u00fa.\3\2\2\2\u00fb\u00fc\7K\2\2\u00fc\u00fd")
        buf.write("\7p\2\2\u00fd\60\3\2\2\2\u00fe\u00ff\7D\2\2\u00ff\u0100")
        buf.write("\7q\2\2\u0100\u0101\7q\2\2\u0101\u0102\7n\2\2\u0102\u0103")
        buf.write("\7g\2\2\u0103\u0104\7c\2\2\u0104\u0105\7p\2\2\u0105\62")
        buf.write("\3\2\2\2\u0106\u0107\7T\2\2\u0107\u0108\7g\2\2\u0108\u0109")
        buf.write("\7v\2\2\u0109\u010a\7w\2\2\u010a\u010b\7t\2\2\u010b\u010c")
        buf.write("\7p\2\2\u010c\64\3\2\2\2\u010d\u010e\7P\2\2\u010e\u010f")
        buf.write("\7w\2\2\u010f\u0110\7n\2\2\u0110\u0111\7n\2\2\u0111\66")
        buf.write("\3\2\2\2\u0112\u0113\7E\2\2\u0113\u0114\7q\2\2\u0114\u0115")
        buf.write("\7p\2\2\u0115\u0116\7u\2\2\u0116\u0117\7v\2\2\u0117\u0118")
        buf.write("\7t\2\2\u0118\u0119\7w\2\2\u0119\u011a\7e\2\2\u011a\u011b")
        buf.write("\7v\2\2\u011b\u011c\7q\2\2\u011c\u011d\7t\2\2\u011d8\3")
        buf.write("\2\2\2\u011e\u011f\7F\2\2\u011f\u0120\7g\2\2\u0120\u0121")
        buf.write("\7u\2\2\u0121\u0122\7v\2\2\u0122\u0123\7t\2\2\u0123\u0124")
        buf.write("\7w\2\2\u0124\u0125\7e\2\2\u0125\u0126\7v\2\2\u0126\u0127")
        buf.write("\7q\2\2\u0127\u0128\7t\2\2\u0128:\3\2\2\2\u0129\u012a")
        buf.write("\7P\2\2\u012a\u012b\7g\2\2\u012b\u012c\7y\2\2\u012c<\3")
        buf.write("\2\2\2\u012d\u012e\7D\2\2\u012e\u012f\7{\2\2\u012f>\3")
        buf.write("\2\2\2\u0130\u0131\7U\2\2\u0131\u0132\7g\2\2\u0132\u0133")
        buf.write("\7n\2\2\u0133\u0134\7h\2\2\u0134@\3\2\2\2\u0135\u0136")
        buf.write("\7-\2\2\u0136B\3\2\2\2\u0137\u0138\7/\2\2\u0138D\3\2\2")
        buf.write("\2\u0139\u013a\7,\2\2\u013aF\3\2\2\2\u013b\u013c\7\61")
        buf.write("\2\2\u013cH\3\2\2\2\u013d\u013e\7\'\2\2\u013eJ\3\2\2\2")
        buf.write("\u013f\u0140\7#\2\2\u0140L\3\2\2\2\u0141\u0142\7(\2\2")
        buf.write("\u0142\u0143\7(\2\2\u0143N\3\2\2\2\u0144\u0145\7~\2\2")
        buf.write("\u0145\u0146\7~\2\2\u0146P\3\2\2\2\u0147\u0148\7?\2\2")
        buf.write("\u0148\u0149\7?\2\2\u0149R\3\2\2\2\u014a\u014b\7?\2\2")
        buf.write("\u014bT\3\2\2\2\u014c\u014d\7#\2\2\u014d\u014e\7?\2\2")
        buf.write("\u014eV\3\2\2\2\u014f\u0150\7@\2\2\u0150X\3\2\2\2\u0151")
        buf.write("\u0152\7@\2\2\u0152\u0153\7?\2\2\u0153Z\3\2\2\2\u0154")
        buf.write("\u0155\7>\2\2\u0155\\\3\2\2\2\u0156\u0157\7>\2\2\u0157")
        buf.write("\u0158\7?\2\2\u0158^\3\2\2\2\u0159\u015a\7?\2\2\u015a")
        buf.write("\u015b\7?\2\2\u015b\u015c\7\60\2\2\u015c`\3\2\2\2\u015d")
        buf.write("\u015e\7-\2\2\u015e\u015f\7\60\2\2\u015fb\3\2\2\2\u0160")
        buf.write("\u0161\7\60\2\2\u0161d\3\2\2\2\u0162\u0163\7\60\2\2\u0163")
        buf.write("\u0164\7\60\2\2\u0164f\3\2\2\2\u0165\u0166\7<\2\2\u0166")
        buf.write("\u0167\7<\2\2\u0167h\3\2\2\2\u0168\u0169\7E\2\2\u0169")
        buf.write("\u016a\7n\2\2\u016a\u016b\7c\2\2\u016b\u016c\7u\2\2\u016c")
        buf.write("\u016d\7u\2\2\u016dj\3\2\2\2\u016e\u016f\7H\2\2\u016f")
        buf.write("\u0170\7n\2\2\u0170\u0171\7q\2\2\u0171\u0172\7c\2\2\u0172")
        buf.write("\u0173\7v\2\2\u0173l\3\2\2\2\u0174\u0175\7U\2\2\u0175")
        buf.write("\u0176\7v\2\2\u0176\u0177\7t\2\2\u0177\u0178\7k\2\2\u0178")
        buf.write("\u0179\7p\2\2\u0179\u017a\7i\2\2\u017an\3\2\2\2\u017b")
        buf.write("\u017c\7K\2\2\u017c\u017d\7p\2\2\u017d\u017e\7v\2\2\u017e")
        buf.write("p\3\2\2\2\u017f\u0182\5)\25\2\u0180\u0182\5+\26\2\u0181")
        buf.write("\u017f\3\2\2\2\u0181\u0180\3\2\2\2\u0182r\3\2\2\2\u0183")
        buf.write("\u0188\5w<\2\u0184\u0188\5y=\2\u0185\u0188\5{>\2\u0186")
        buf.write("\u0188\5u;\2\u0187\u0183\3\2\2\2\u0187\u0184\3\2\2\2\u0187")
        buf.write("\u0185\3\2\2\2\u0187\u0186\3\2\2\2\u0188t\3\2\2\2\u0189")
        buf.write("\u018a\7\62\2\2\u018a\u018e\7z\2\2\u018b\u018c\7\62\2")
        buf.write("\2\u018c\u018e\7Z\2\2\u018d\u0189\3\2\2\2\u018d\u018b")
        buf.write("\3\2\2\2\u018e\u018f\3\2\2\2\u018f\u01a5\t\5\2\2\u0190")
        buf.write("\u0191\7\62\2\2\u0191\u0195\7z\2\2\u0192\u0193\7\62\2")
        buf.write("\2\u0193\u0195\7Z\2\2\u0194\u0190\3\2\2\2\u0194\u0192")
        buf.write("\3\2\2\2\u0195\u0196\3\2\2\2\u0196\u01a1\t\5\2\2\u0197")
        buf.write("\u0199\7a\2\2\u0198\u0197\3\2\2\2\u0198\u0199\3\2\2\2")
        buf.write("\u0199\u019b\3\2\2\2\u019a\u019c\t\6\2\2\u019b\u019a\3")
        buf.write("\2\2\2\u019c\u019d\3\2\2\2\u019d\u019b\3\2\2\2\u019d\u019e")
        buf.write("\3\2\2\2\u019e\u01a0\3\2\2\2\u019f\u0198\3\2\2\2\u01a0")
        buf.write("\u01a3\3\2\2\2\u01a1\u019f\3\2\2\2\u01a1\u01a2\3\2\2\2")
        buf.write("\u01a2\u01a5\3\2\2\2\u01a3\u01a1\3\2\2\2\u01a4\u018d\3")
        buf.write("\2\2\2\u01a4\u0194\3\2\2\2\u01a5v\3\2\2\2\u01a6\u01a7")
        buf.write("\7\62\2\2\u01a7\u01b8\t\7\2\2\u01a8\u01a9\7\62\2\2\u01a9")
        buf.write("\u01b4\t\7\2\2\u01aa\u01ac\7a\2\2\u01ab\u01aa\3\2\2\2")
        buf.write("\u01ab\u01ac\3\2\2\2\u01ac\u01ae\3\2\2\2\u01ad\u01af\t")
        buf.write("\b\2\2\u01ae\u01ad\3\2\2\2\u01af\u01b0\3\2\2\2\u01b0\u01ae")
        buf.write("\3\2\2\2\u01b0\u01b1\3\2\2\2\u01b1\u01b3\3\2\2\2\u01b2")
        buf.write("\u01ab\3\2\2\2\u01b3\u01b6\3\2\2\2\u01b4\u01b2\3\2\2\2")
        buf.write("\u01b4\u01b5\3\2\2\2\u01b5\u01b8\3\2\2\2\u01b6\u01b4\3")
        buf.write("\2\2\2\u01b7\u01a6\3\2\2\2\u01b7\u01a8\3\2\2\2\u01b8x")
        buf.write("\3\2\2\2\u01b9\u01ba\7\62\2\2\u01ba\u01bb\7d\2\2\u01bb")
        buf.write("\u01c0\7\63\2\2\u01bc\u01bd\7\62\2\2\u01bd\u01be\7D\2")
        buf.write("\2\u01be\u01c0\7\63\2\2\u01bf\u01b9\3\2\2\2\u01bf\u01bc")
        buf.write("\3\2\2\2\u01c0\u01d6\3\2\2\2\u01c1\u01c2\7\62\2\2\u01c2")
        buf.write("\u01c6\7d\2\2\u01c3\u01c4\7\62\2\2\u01c4\u01c6\7D\2\2")
        buf.write("\u01c5\u01c1\3\2\2\2\u01c5\u01c3\3\2\2\2\u01c6\u01c7\3")
        buf.write("\2\2\2\u01c7\u01d2\t\t\2\2\u01c8\u01ca\7a\2\2\u01c9\u01c8")
        buf.write("\3\2\2\2\u01c9\u01ca\3\2\2\2\u01ca\u01cc\3\2\2\2\u01cb")
        buf.write("\u01cd\t\n\2\2\u01cc\u01cb\3\2\2\2\u01cd\u01ce\3\2\2\2")
        buf.write("\u01ce\u01cc\3\2\2\2\u01ce\u01cf\3\2\2\2\u01cf\u01d1\3")
        buf.write("\2\2\2\u01d0\u01c9\3\2\2\2\u01d1\u01d4\3\2\2\2\u01d2\u01d0")
        buf.write("\3\2\2\2\u01d2\u01d3\3\2\2\2\u01d3\u01d6\3\2\2\2\u01d4")
        buf.write("\u01d2\3\2\2\2\u01d5\u01bf\3\2\2\2\u01d5\u01c5\3\2\2\2")
        buf.write("\u01d6z\3\2\2\2\u01d7\u01e7\t\13\2\2\u01d8\u01e3\t\13")
        buf.write("\2\2\u01d9\u01db\7a\2\2\u01da\u01d9\3\2\2\2\u01da\u01db")
        buf.write("\3\2\2\2\u01db\u01dd\3\2\2\2\u01dc\u01de\t\4\2\2\u01dd")
        buf.write("\u01dc\3\2\2\2\u01de\u01df\3\2\2\2\u01df\u01dd\3\2\2\2")
        buf.write("\u01df\u01e0\3\2\2\2\u01e0\u01e2\3\2\2\2\u01e1\u01da\3")
        buf.write("\2\2\2\u01e2\u01e5\3\2\2\2\u01e3\u01e1\3\2\2\2\u01e3\u01e4")
        buf.write("\3\2\2\2\u01e4\u01e7\3\2\2\2\u01e5\u01e3\3\2\2\2\u01e6")
        buf.write("\u01d7\3\2\2\2\u01e6\u01d8\3\2\2\2\u01e7|\3\2\2\2\u01e8")
        buf.write("\u01e9\7\62\2\2\u01e9\u01ed\7z\2\2\u01ea\u01eb\7\62\2")
        buf.write("\2\u01eb\u01ed\7Z\2\2\u01ec\u01e8\3\2\2\2\u01ec\u01ea")
        buf.write("\3\2\2\2\u01ed\u01ee\3\2\2\2\u01ee\u0204\t\6\2\2\u01ef")
        buf.write("\u01f0\7\62\2\2\u01f0\u01f4\7z\2\2\u01f1\u01f2\7\62\2")
        buf.write("\2\u01f2\u01f4\7Z\2\2\u01f3\u01ef\3\2\2\2\u01f3\u01f1")
        buf.write("\3\2\2\2\u01f4\u01f5\3\2\2\2\u01f5\u0200\t\5\2\2\u01f6")
        buf.write("\u01f8\7a\2\2\u01f7\u01f6\3\2\2\2\u01f7\u01f8\3\2\2\2")
        buf.write("\u01f8\u01fa\3\2\2\2\u01f9\u01fb\t\6\2\2\u01fa\u01f9\3")
        buf.write("\2\2\2\u01fb\u01fc\3\2\2\2\u01fc\u01fa\3\2\2\2\u01fc\u01fd")
        buf.write("\3\2\2\2\u01fd\u01ff\3\2\2\2\u01fe\u01f7\3\2\2\2\u01ff")
        buf.write("\u0202\3\2\2\2\u0200\u01fe\3\2\2\2\u0200\u0201\3\2\2\2")
        buf.write("\u0201\u0204\3\2\2\2\u0202\u0200\3\2\2\2\u0203\u01ec\3")
        buf.write("\2\2\2\u0203\u01f3\3\2\2\2\u0204~\3\2\2\2\u0205\u0206")
        buf.write("\7\62\2\2\u0206\u0217\t\b\2\2\u0207\u0208\7\62\2\2\u0208")
        buf.write("\u0213\t\7\2\2\u0209\u020b\7a\2\2\u020a\u0209\3\2\2\2")
        buf.write("\u020a\u020b\3\2\2\2\u020b\u020d\3\2\2\2\u020c\u020e\t")
        buf.write("\b\2\2\u020d\u020c\3\2\2\2\u020e\u020f\3\2\2\2\u020f\u020d")
        buf.write("\3\2\2\2\u020f\u0210\3\2\2\2\u0210\u0212\3\2\2\2\u0211")
        buf.write("\u020a\3\2\2\2\u0212\u0215\3\2\2\2\u0213\u0211\3\2\2\2")
        buf.write("\u0213\u0214\3\2\2\2\u0214\u0217\3\2\2\2\u0215\u0213\3")
        buf.write("\2\2\2\u0216\u0205\3\2\2\2\u0216\u0207\3\2\2\2\u0217\u0080")
        buf.write("\3\2\2\2\u0218\u0219\7\62\2\2\u0219\u021d\7d\2\2\u021a")
        buf.write("\u021b\7\62\2\2\u021b\u021d\7D\2\2\u021c\u0218\3\2\2\2")
        buf.write("\u021c\u021a\3\2\2\2\u021d\u021e\3\2\2\2\u021e\u0234\t")
        buf.write("\n\2\2\u021f\u0220\7\62\2\2\u0220\u0224\7d\2\2\u0221\u0222")
        buf.write("\7\62\2\2\u0222\u0224\7D\2\2\u0223\u021f\3\2\2\2\u0223")
        buf.write("\u0221\3\2\2\2\u0224\u0225\3\2\2\2\u0225\u0230\t\t\2\2")
        buf.write("\u0226\u0228\7a\2\2\u0227\u0226\3\2\2\2\u0227\u0228\3")
        buf.write("\2\2\2\u0228\u022a\3\2\2\2\u0229\u022b\t\n\2\2\u022a\u0229")
        buf.write("\3\2\2\2\u022b\u022c\3\2\2\2\u022c\u022a\3\2\2\2\u022c")
        buf.write("\u022d\3\2\2\2\u022d\u022f\3\2\2\2\u022e\u0227\3\2\2\2")
        buf.write("\u022f\u0232\3\2\2\2\u0230\u022e\3\2\2\2\u0230\u0231\3")
        buf.write("\2\2\2\u0231\u0234\3\2\2\2\u0232\u0230\3\2\2\2\u0233\u021c")
        buf.write("\3\2\2\2\u0233\u0223\3\2\2\2\u0234\u0082\3\2\2\2\u0235")
        buf.write("\u0245\t\4\2\2\u0236\u0241\t\13\2\2\u0237\u0239\7a\2\2")
        buf.write("\u0238\u0237\3\2\2\2\u0238\u0239\3\2\2\2\u0239\u023b\3")
        buf.write("\2\2\2\u023a\u023c\t\4\2\2\u023b\u023a\3\2\2\2\u023c\u023d")
        buf.write("\3\2\2\2\u023d\u023b\3\2\2\2\u023d\u023e\3\2\2\2\u023e")
        buf.write("\u0240\3\2\2\2\u023f\u0238\3\2\2\2\u0240\u0243\3\2\2\2")
        buf.write("\u0241\u023f\3\2\2\2\u0241\u0242\3\2\2\2\u0242\u0245\3")
        buf.write("\2\2\2\u0243\u0241\3\2\2\2\u0244\u0235\3\2\2\2\u0244\u0236")
        buf.write("\3\2\2\2\u0245\u0084\3\2\2\2\u0246\u024b\5\177@\2\u0247")
        buf.write("\u024b\5\u0081A\2\u0248\u024b\5\u0083B\2\u0249\u024b\5")
        buf.write("}?\2\u024a\u0246\3\2\2\2\u024a\u0247\3\2\2\2\u024a\u0248")
        buf.write("\3\2\2\2\u024a\u0249\3\2\2\2\u024b\u0086\3\2\2\2\u024c")
        buf.write("\u024d\7)\2\2\u024d\u0251\7$\2\2\u024e\u0251\n\f\2\2\u024f")
        buf.write("\u0251\5\u0089E\2\u0250\u024c\3\2\2\2\u0250\u024e\3\2")
        buf.write("\2\2\u0250\u024f\3\2\2\2\u0251\u0088\3\2\2\2\u0252\u0253")
        buf.write("\7^\2\2\u0253\u0254\t\r\2\2\u0254\u008a\3\2\2\2\u0255")
        buf.write("\u0256\7^\2\2\u0256\u0259\n\r\2\2\u0257\u0259\7^\2\2\u0258")
        buf.write("\u0255\3\2\2\2\u0258\u0257\3\2\2\2\u0259\u008c\3\2\2\2")
        buf.write("\u025a\u025e\7$\2\2\u025b\u025d\5\u0087D\2\u025c\u025b")
        buf.write("\3\2\2\2\u025d\u0260\3\2\2\2\u025e\u025c\3\2\2\2\u025e")
        buf.write("\u025f\3\2\2\2\u025f\u0261\3\2\2\2\u0260\u025e\3\2\2\2")
        buf.write("\u0261\u0262\7$\2\2\u0262\u0263\bG\2\2\u0263\u008e\3\2")
        buf.write("\2\2\u0264\u0268\7$\2\2\u0265\u0267\5\u0087D\2\u0266\u0265")
        buf.write("\3\2\2\2\u0267\u026a\3\2\2\2\u0268\u0266\3\2\2\2\u0268")
        buf.write("\u0269\3\2\2\2\u0269\u026b\3\2\2\2\u026a\u0268\3\2\2\2")
        buf.write("\u026b\u026c\5\u008bF\2\u026c\u026d\bH\3\2\u026d\u0090")
        buf.write("\3\2\2\2\u026e\u0272\7$\2\2\u026f\u0271\5\u0087D\2\u0270")
        buf.write("\u026f\3\2\2\2\u0271\u0274\3\2\2\2\u0272\u0270\3\2\2\2")
        buf.write("\u0272\u0273\3\2\2\2\u0273\u0275\3\2\2\2\u0274\u0272\3")
        buf.write("\2\2\2\u0275\u0276\bI\4\2\u0276\u0092\3\2\2\2\u0277\u0278")
        buf.write("\5\u0083B\2\u0278\u027b\5c\62\2\u0279\u027c\5\33\16\2")
        buf.write("\u027a\u027c\5\31\r\2\u027b\u0279\3\2\2\2\u027b\u027a")
        buf.write("\3\2\2\2\u027b\u027c\3\2\2\2\u027c\u028b\3\2\2\2\u027d")
        buf.write("\u027e\5\u0083B\2\u027e\u027f\5\31\r\2\u027f\u028b\3\2")
        buf.write("\2\2\u0280\u0282\5\u0083B\2\u0281\u0280\3\2\2\2\u0281")
        buf.write("\u0282\3\2\2\2\u0282\u0283\3\2\2\2\u0283\u0284\5c\62\2")
        buf.write("\u0284\u0285\5\33\16\2\u0285\u0286\5\31\r\2\u0286\u028b")
        buf.write("\3\2\2\2\u0287\u0288\5c\62\2\u0288\u0289\5\31\r\2\u0289")
        buf.write("\u028b\3\2\2\2\u028a\u0277\3\2\2\2\u028a\u027d\3\2\2\2")
        buf.write("\u028a\u0281\3\2\2\2\u028a\u0287\3\2\2\2\u028b\u0094\3")
        buf.write("\2\2\2\u028c\u0290\t\16\2\2\u028d\u028f\t\17\2\2\u028e")
        buf.write("\u028d\3\2\2\2\u028f\u0292\3\2\2\2\u0290\u028e\3\2\2\2")
        buf.write("\u0290\u0291\3\2\2\2\u0291\u0096\3\2\2\2\u0292\u0290\3")
        buf.write("\2\2\2\u0293\u0295\7&\2\2\u0294\u0296\t\17\2\2\u0295\u0294")
        buf.write("\3\2\2\2\u0296\u0297\3\2\2\2\u0297\u0295\3\2\2\2\u0297")
        buf.write("\u0298\3\2\2\2\u0298\u0098\3\2\2\2\u0299\u029a\7%\2\2")
        buf.write("\u029a\u029b\7%\2\2\u029b\u029f\3\2\2\2\u029c\u029e\13")
        buf.write("\2\2\2\u029d\u029c\3\2\2\2\u029e\u02a1\3\2\2\2\u029f\u02a0")
        buf.write("\3\2\2\2\u029f\u029d\3\2\2\2\u02a0\u02a2\3\2\2\2\u02a1")
        buf.write("\u029f\3\2\2\2\u02a2\u02a3\7%\2\2\u02a3\u02a4\7%\2\2\u02a4")
        buf.write("\u02a5\3\2\2\2\u02a5\u02a6\bM\5\2\u02a6\u009a\3\2\2\2")
        buf.write("\u02a7\u02a9\t\20\2\2\u02a8\u02a7\3\2\2\2\u02a9\u02aa")
        buf.write("\3\2\2\2\u02aa\u02a8\3\2\2\2\u02aa\u02ab\3\2\2\2\u02ab")
        buf.write("\u02ac\3\2\2\2\u02ac\u02ad\bN\5\2\u02ad\u009c\3\2\2\2")
        buf.write("\u02ae\u02af\13\2\2\2\u02af\u02b0\bO\6\2\u02b0\u009e\3")
        buf.write("\2\2\2<\2\u00bb\u00c2\u0181\u0187\u018d\u0194\u0198\u019d")
        buf.write("\u01a1\u01a4\u01ab\u01b0\u01b4\u01b7\u01bf\u01c5\u01c9")
        buf.write("\u01ce\u01d2\u01d5\u01da\u01df\u01e3\u01e6\u01ec\u01f3")
        buf.write("\u01f7\u01fc\u0200\u0203\u020a\u020f\u0213\u0216\u021c")
        buf.write("\u0223\u0227\u022c\u0230\u0233\u0238\u023d\u0241\u0244")
        buf.write("\u024a\u0250\u0258\u025e\u0268\u0272\u027b\u0281\u028a")
        buf.write("\u0290\u0297\u029f\u02aa\7\3G\2\3H\3\3I\4\b\2\2\3O\5")
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
    TRUE = 18
    FALSE = 19
    ARRAY = 20
    IN = 21
    BOOLEAN = 22
    RETURN = 23
    NULL = 24
    CONSTRUCTOR = 25
    DESTRUCTOR = 26
    NEW = 27
    BY = 28
    SELF = 29
    ADD = 30
    SUB = 31
    MUL = 32
    DIV = 33
    MOD = 34
    NOT = 35
    AND = 36
    OR = 37
    EQUAL = 38
    ASSIGN = 39
    NOTEQUAL = 40
    GT = 41
    GTE = 42
    LT = 43
    LTE = 44
    EQUAL_STR = 45
    ADD_STR = 46
    DOT = 47
    DOTDOT = 48
    SCOPE = 49
    CLASS = 50
    FLOAT_TYPE = 51
    STRING = 52
    INT_TYPE = 53
    BOOL_LITERAL = 54
    ARRAY_SIZE = 55
    INTEGER_LITERAL = 56
    STRING_LITERAL = 57
    ILLEGAL_ESCAPE = 58
    UNCLOSE_STRING = 59
    REAL_LITERAL = 60
    NORMAL_ID = 61
    DOLLAR_ID = 62
    BLOCK_COMMENT = 63
    WS = 64
    ERROR_CHAR = 65

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'Val'", "'Var'", "'('", "')'", "'{'", "'}'", "'['", "']'", 
            "';'", "','", "':'", "'Break'", "'Continue'", "'If'", "'Elseif'", 
            "'Else'", "'Foreach'", "'True'", "'False'", "'Array'", "'In'", 
            "'Boolean'", "'Return'", "'Null'", "'Constructor'", "'Destructor'", 
            "'New'", "'By'", "'Self'", "'+'", "'-'", "'*'", "'/'", "'%'", 
            "'!'", "'&&'", "'||'", "'=='", "'='", "'!='", "'>'", "'>='", 
            "'<'", "'<='", "'==.'", "'+.'", "'.'", "'..'", "'::'", "'Class'", 
            "'Float'", "'String'", "'Int'" ]

    symbolicNames = [ "<INVALID>",
            "VAL", "VAR", "LP", "RP", "LCB", "RCB", "LSB", "RSB", "SEMI", 
            "COMMA", "COLON", "BREAK", "CONTINUE", "IF", "ELSEIF", "ELSE", 
            "FOREACH", "TRUE", "FALSE", "ARRAY", "IN", "BOOLEAN", "RETURN", 
            "NULL", "CONSTRUCTOR", "DESTRUCTOR", "NEW", "BY", "SELF", "ADD", 
            "SUB", "MUL", "DIV", "MOD", "NOT", "AND", "OR", "EQUAL", "ASSIGN", 
            "NOTEQUAL", "GT", "GTE", "LT", "LTE", "EQUAL_STR", "ADD_STR", 
            "DOT", "DOTDOT", "SCOPE", "CLASS", "FLOAT_TYPE", "STRING", "INT_TYPE", 
            "BOOL_LITERAL", "ARRAY_SIZE", "INTEGER_LITERAL", "STRING_LITERAL", 
            "ILLEGAL_ESCAPE", "UNCLOSE_STRING", "REAL_LITERAL", "NORMAL_ID", 
            "DOLLAR_ID", "BLOCK_COMMENT", "WS", "ERROR_CHAR" ]

    ruleNames = [ "VAL", "VAR", "LP", "RP", "LCB", "RCB", "LSB", "RSB", 
                  "SEMI", "COMMA", "COLON", "EXPONENT", "DEC_DIGIT", "BREAK", 
                  "CONTINUE", "IF", "ELSEIF", "ELSE", "FOREACH", "TRUE", 
                  "FALSE", "ARRAY", "IN", "BOOLEAN", "RETURN", "NULL", "CONSTRUCTOR", 
                  "DESTRUCTOR", "NEW", "BY", "SELF", "ADD", "SUB", "MUL", 
                  "DIV", "MOD", "NOT", "AND", "OR", "EQUAL", "ASSIGN", "NOTEQUAL", 
                  "GT", "GTE", "LT", "LTE", "EQUAL_STR", "ADD_STR", "DOT", 
                  "DOTDOT", "SCOPE", "CLASS", "FLOAT_TYPE", "STRING", "INT_TYPE", 
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


    def emit(self):
        tk = self.type
        result = super().emit() 
        
        if tk == self.INTEGER_LITERAL or tk == self.REAL_LITERAL or tk == self.ARRAY_SIZE:
            result.text = result.text.replace('_', '')
        return result


    def action(self, localctx:RuleContext, ruleIndex:int, actionIndex:int):
        if self._actions is None:
            actions = dict()
            actions[69] = self.STRING_LITERAL_action 
            actions[70] = self.ILLEGAL_ESCAPE_action 
            actions[71] = self.UNCLOSE_STRING_action 
            actions[77] = self.ERROR_CHAR_action 
            self._actions = actions
        action = self._actions.get(ruleIndex, None)
        if action is not None:
            action(localctx, actionIndex)
        else:
            raise Exception("No registered action for:" + str(ruleIndex))


    def STRING_LITERAL_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 0:
             
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
        if actionIndex == 1:

                raise IllegalEscape(str(self.text)[1:])

     

    def UNCLOSE_STRING_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 2:

                raise UncloseString(str(self.text)[1:])

     

    def ERROR_CHAR_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 3:
            raise ErrorToken(self.text)
     


