# Generated from main/d96/parser/D96.g4 by ANTLR 4.9.2
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
    from typing import TextIO
else:
    from typing.io import TextIO


from lexererr import *
import inspect



def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2J")
        buf.write("\u0269\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7")
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
        buf.write("L\4M\tM\4N\tN\4O\tO\4P\tP\4Q\tQ\3\2\3\2\3\2\3\2\3\2\3")
        buf.write("\2\3\2\3\2\3\3\3\3\3\3\3\3\3\3\3\4\3\4\3\4\3\4\3\4\3\4")
        buf.write("\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\5\3\5\5")
        buf.write("\5\u00c4\n\5\3\6\3\6\3\6\3\6\3\6\3\6\3\7\3\7\3\7\3\7\3")
        buf.write("\7\3\7\3\7\3\b\3\b\3\b\3\b\3\t\3\t\3\t\3\t\3\t\3\n\3\n")
        buf.write("\3\n\3\n\3\n\3\n\5\n\u00e2\n\n\3\13\3\13\3\13\3\13\5\13")
        buf.write("\u00e8\n\13\3\13\3\13\7\13\u00ec\n\13\f\13\16\13\u00ef")
        buf.write("\13\13\3\13\3\13\3\13\3\13\3\13\5\13\u00f6\n\13\3\13\3")
        buf.write("\13\5\13\u00fa\n\13\3\f\3\f\3\f\7\f\u00ff\n\f\f\f\16\f")
        buf.write("\u0102\13\f\3\f\3\f\3\f\3\f\5\f\u0108\n\f\3\r\3\r\3\r")
        buf.write("\3\r\5\r\u010e\n\r\3\r\3\r\7\r\u0112\n\r\f\r\16\r\u0115")
        buf.write("\13\r\3\r\3\r\3\r\3\r\3\r\5\r\u011c\n\r\3\r\3\r\5\r\u0120")
        buf.write("\n\r\3\16\3\16\3\16\7\16\u0125\n\16\f\16\16\16\u0128\13")
        buf.write("\16\3\16\3\16\5\16\u012c\n\16\3\17\3\17\3\17\3\17\5\17")
        buf.write("\u0132\n\17\3\20\3\20\3\20\3\21\3\21\3\21\3\21\3\21\5")
        buf.write("\21\u013c\n\21\3\22\3\22\7\22\u0140\n\22\f\22\16\22\u0143")
        buf.write("\13\22\3\22\3\22\3\22\3\23\3\23\7\23\u014a\n\23\f\23\16")
        buf.write("\23\u014d\13\23\3\23\3\23\3\23\3\24\3\24\7\24\u0154\n")
        buf.write("\24\f\24\16\24\u0157\13\24\3\24\3\24\3\25\3\25\3\25\3")
        buf.write("\25\3\25\3\25\3\25\3\25\3\25\3\25\3\25\3\25\3\25\5\25")
        buf.write("\u0168\n\25\3\26\3\26\3\26\3\26\3\27\3\27\3\27\3\27\3")
        buf.write("\30\3\30\3\31\3\31\3\32\3\32\3\33\3\33\3\34\3\34\3\35")
        buf.write("\3\35\3\36\3\36\3\37\3\37\3 \3 \3!\3!\3\"\3\"\5\"\u0188")
        buf.write("\n\"\3\"\3\"\3#\3#\3$\3$\3$\7$\u0191\n$\f$\16$\u0194\13")
        buf.write("$\3$\5$\u0197\n$\3%\3%\3&\3&\3&\3&\3&\3&\3\'\3\'\3\'\3")
        buf.write("\'\3\'\3\'\3(\3(\3(\3(\3(\3(\3(\3(\3(\3)\3)\3)\3*\3*\3")
        buf.write("*\3*\3*\3*\3*\3+\3+\3+\3+\3+\3,\3,\3,\3,\3,\3,\3,\3,\3")
        buf.write("-\3-\3-\3-\3-\3.\3.\3.\3.\3.\3.\3/\3/\3/\3/\3/\3/\3\60")
        buf.write("\3\60\3\60\3\61\3\61\3\61\3\61\3\61\3\61\3\61\3\61\3\62")
        buf.write("\3\62\3\62\3\62\3\62\3\62\3\62\3\63\3\63\3\63\3\63\3\63")
        buf.write("\3\64\3\64\3\64\3\64\3\64\3\64\3\64\3\64\3\64\3\64\3\64")
        buf.write("\3\64\3\65\3\65\3\65\3\65\3\65\3\65\3\65\3\65\3\65\3\65")
        buf.write("\3\65\3\66\3\66\3\66\3\66\3\67\3\67\3\67\38\38\38\38\3")
        buf.write("8\39\39\3:\3:\3;\3;\3<\3<\3=\3=\3>\3>\3?\3?\3?\3@\3@\3")
        buf.write("@\3A\3A\3A\3B\3B\3C\3C\3C\3D\3D\3E\3E\3E\3F\3F\3G\3G\3")
        buf.write("G\3H\3H\3H\3H\3I\3I\3I\3J\3J\3K\3K\3K\3L\3L\3L\3M\3M\7")
        buf.write("M\u0247\nM\fM\16M\u024a\13M\3N\3N\6N\u024e\nN\rN\16N\u024f")
        buf.write("\3O\6O\u0253\nO\rO\16O\u0254\3O\3O\3P\3P\3P\3P\7P\u025d")
        buf.write("\nP\fP\16P\u0260\13P\3P\3P\3P\3P\3P\3Q\3Q\3Q\3\u025e\2")
        buf.write("R\3\3\5\4\7\5\t\6\13\7\r\b\17\t\21\n\23\13\25\f\27\r\31")
        buf.write("\16\33\17\35\2\37\2!\2#\20%\21\'\22)\23+\24-\25/\2\61")
        buf.write("\26\63\27\65\30\67\319\32;\33=\34?\35A\36C\2E\2G\2I\2")
        buf.write("K\37M O!Q\"S#U$W%Y&[\'](_)a*c+e,g-i.k/m\60o\61q\62s\63")
        buf.write("u\64w\65y\66{\67}8\1779\u0081:\u0083;\u0085<\u0087=\u0089")
        buf.write(">\u008b?\u008d@\u008fA\u0091B\u0093C\u0095D\u0097E\u0099")
        buf.write("F\u009bG\u009dH\u009fI\u00a1J\3\2\21\5\2\62;CHch\6\2\62")
        buf.write(";CHaach\3\2\62;\4\2\62;aa\3\2\62\63\4\2\62\63aa\3\2\63")
        buf.write(";\4\2$$^^\t\2))^^ddhhppttvv\3\2$$\4\2GGgg\4\2--//\5\2")
        buf.write("C\\aac|\6\2\62;C\\aac|\5\2\13\f\16\17\"\"\2\u0280\2\3")
        buf.write("\3\2\2\2\2\5\3\2\2\2\2\7\3\2\2\2\2\t\3\2\2\2\2\13\3\2")
        buf.write("\2\2\2\r\3\2\2\2\2\17\3\2\2\2\2\21\3\2\2\2\2\23\3\2\2")
        buf.write("\2\2\25\3\2\2\2\2\27\3\2\2\2\2\31\3\2\2\2\2\33\3\2\2\2")
        buf.write("\2#\3\2\2\2\2%\3\2\2\2\2\'\3\2\2\2\2)\3\2\2\2\2+\3\2\2")
        buf.write("\2\2-\3\2\2\2\2\61\3\2\2\2\2\63\3\2\2\2\2\65\3\2\2\2\2")
        buf.write("\67\3\2\2\2\29\3\2\2\2\2;\3\2\2\2\2=\3\2\2\2\2?\3\2\2")
        buf.write("\2\2A\3\2\2\2\2K\3\2\2\2\2M\3\2\2\2\2O\3\2\2\2\2Q\3\2")
        buf.write("\2\2\2S\3\2\2\2\2U\3\2\2\2\2W\3\2\2\2\2Y\3\2\2\2\2[\3")
        buf.write("\2\2\2\2]\3\2\2\2\2_\3\2\2\2\2a\3\2\2\2\2c\3\2\2\2\2e")
        buf.write("\3\2\2\2\2g\3\2\2\2\2i\3\2\2\2\2k\3\2\2\2\2m\3\2\2\2\2")
        buf.write("o\3\2\2\2\2q\3\2\2\2\2s\3\2\2\2\2u\3\2\2\2\2w\3\2\2\2")
        buf.write("\2y\3\2\2\2\2{\3\2\2\2\2}\3\2\2\2\2\177\3\2\2\2\2\u0081")
        buf.write("\3\2\2\2\2\u0083\3\2\2\2\2\u0085\3\2\2\2\2\u0087\3\2\2")
        buf.write("\2\2\u0089\3\2\2\2\2\u008b\3\2\2\2\2\u008d\3\2\2\2\2\u008f")
        buf.write("\3\2\2\2\2\u0091\3\2\2\2\2\u0093\3\2\2\2\2\u0095\3\2\2")
        buf.write("\2\2\u0097\3\2\2\2\2\u0099\3\2\2\2\2\u009b\3\2\2\2\2\u009d")
        buf.write("\3\2\2\2\2\u009f\3\2\2\2\2\u00a1\3\2\2\2\3\u00a3\3\2\2")
        buf.write("\2\5\u00ab\3\2\2\2\7\u00b0\3\2\2\2\t\u00c3\3\2\2\2\13")
        buf.write("\u00c5\3\2\2\2\r\u00cb\3\2\2\2\17\u00d2\3\2\2\2\21\u00d6")
        buf.write("\3\2\2\2\23\u00e1\3\2\2\2\25\u00f9\3\2\2\2\27\u0107\3")
        buf.write("\2\2\2\31\u011f\3\2\2\2\33\u012b\3\2\2\2\35\u0131\3\2")
        buf.write("\2\2\37\u0133\3\2\2\2!\u013b\3\2\2\2#\u013d\3\2\2\2%\u0147")
        buf.write("\3\2\2\2\'\u0151\3\2\2\2)\u0167\3\2\2\2+\u0169\3\2\2\2")
        buf.write("-\u016d\3\2\2\2/\u0171\3\2\2\2\61\u0173\3\2\2\2\63\u0175")
        buf.write("\3\2\2\2\65\u0177\3\2\2\2\67\u0179\3\2\2\29\u017b\3\2")
        buf.write("\2\2;\u017d\3\2\2\2=\u017f\3\2\2\2?\u0181\3\2\2\2A\u0183")
        buf.write("\3\2\2\2C\u0185\3\2\2\2E\u018b\3\2\2\2G\u0196\3\2\2\2")
        buf.write("I\u0198\3\2\2\2K\u019a\3\2\2\2M\u01a0\3\2\2\2O\u01a6\3")
        buf.write("\2\2\2Q\u01af\3\2\2\2S\u01b2\3\2\2\2U\u01b9\3\2\2\2W\u01be")
        buf.write("\3\2\2\2Y\u01c6\3\2\2\2[\u01cb\3\2\2\2]\u01d1\3\2\2\2")
        buf.write("_\u01d7\3\2\2\2a\u01da\3\2\2\2c\u01e2\3\2\2\2e\u01e9\3")
        buf.write("\2\2\2g\u01ee\3\2\2\2i\u01fa\3\2\2\2k\u0205\3\2\2\2m\u0209")
        buf.write("\3\2\2\2o\u020c\3\2\2\2q\u0211\3\2\2\2s\u0213\3\2\2\2")
        buf.write("u\u0215\3\2\2\2w\u0217\3\2\2\2y\u0219\3\2\2\2{\u021b\3")
        buf.write("\2\2\2}\u021d\3\2\2\2\177\u0220\3\2\2\2\u0081\u0223\3")
        buf.write("\2\2\2\u0083\u0226\3\2\2\2\u0085\u0228\3\2\2\2\u0087\u022b")
        buf.write("\3\2\2\2\u0089\u022d\3\2\2\2\u008b\u0230\3\2\2\2\u008d")
        buf.write("\u0232\3\2\2\2\u008f\u0235\3\2\2\2\u0091\u0239\3\2\2\2")
        buf.write("\u0093\u023c\3\2\2\2\u0095\u023e\3\2\2\2\u0097\u0241\3")
        buf.write("\2\2\2\u0099\u0244\3\2\2\2\u009b\u024b\3\2\2\2\u009d\u0252")
        buf.write("\3\2\2\2\u009f\u0258\3\2\2\2\u00a1\u0266\3\2\2\2\u00a3")
        buf.write("\u00a4\7R\2\2\u00a4\u00a5\7t\2\2\u00a5\u00a6\7q\2\2\u00a6")
        buf.write("\u00a7\7i\2\2\u00a7\u00a8\7t\2\2\u00a8\u00a9\7c\2\2\u00a9")
        buf.write("\u00aa\7o\2\2\u00aa\4\3\2\2\2\u00ab\u00ac\7o\2\2\u00ac")
        buf.write("\u00ad\7c\2\2\u00ad\u00ae\7k\2\2\u00ae\u00af\7p\2\2\u00af")
        buf.write("\6\3\2\2\2\u00b0\u00b1\7c\2\2\u00b1\u00b2\7u\2\2\u00b2")
        buf.write("\u00b3\7u\2\2\u00b3\u00b4\7k\2\2\u00b4\u00b5\7i\2\2\u00b5")
        buf.write("\u00b6\7p\2\2\u00b6\u00b7\7a\2\2\u00b7\u00b8\7u\2\2\u00b8")
        buf.write("\u00b9\7v\2\2\u00b9\u00ba\7c\2\2\u00ba\u00bb\7v\2\2\u00bb")
        buf.write("\u00bc\7g\2\2\u00bc\u00bd\7o\2\2\u00bd\u00be\7g\2\2\u00be")
        buf.write("\u00bf\7p\2\2\u00bf\u00c0\7v\2\2\u00c0\b\3\2\2\2\u00c1")
        buf.write("\u00c4\5Y-\2\u00c2\u00c4\5[.\2\u00c3\u00c1\3\2\2\2\u00c3")
        buf.write("\u00c2\3\2\2\2\u00c4\n\3\2\2\2\u00c5\u00c6\7H\2\2\u00c6")
        buf.write("\u00c7\7n\2\2\u00c7\u00c8\7q\2\2\u00c8\u00c9\7c\2\2\u00c9")
        buf.write("\u00ca\7v\2\2\u00ca\f\3\2\2\2\u00cb\u00cc\7U\2\2\u00cc")
        buf.write("\u00cd\7v\2\2\u00cd\u00ce\7t\2\2\u00ce\u00cf\7k\2\2\u00cf")
        buf.write("\u00d0\7p\2\2\u00d0\u00d1\7i\2\2\u00d1\16\3\2\2\2\u00d2")
        buf.write("\u00d3\7K\2\2\u00d3\u00d4\7p\2\2\u00d4\u00d5\7v\2\2\u00d5")
        buf.write("\20\3\2\2\2\u00d6\u00d7\7X\2\2\u00d7\u00d8\7q\2\2\u00d8")
        buf.write("\u00d9\7k\2\2\u00d9\u00da\7f\2\2\u00da\22\3\2\2\2\u00db")
        buf.write("\u00e2\5\25\13\2\u00dc\u00e2\5\27\f\2\u00dd\u00e2\5\31")
        buf.write("\r\2\u00de\u00df\5\33\16\2\u00df\u00e0\b\n\2\2\u00e0\u00e2")
        buf.write("\3\2\2\2\u00e1\u00db\3\2\2\2\u00e1\u00dc\3\2\2\2\u00e1")
        buf.write("\u00dd\3\2\2\2\u00e1\u00de\3\2\2\2\u00e2\24\3\2\2\2\u00e3")
        buf.write("\u00e4\7\62\2\2\u00e4\u00e8\7z\2\2\u00e5\u00e6\7\62\2")
        buf.write("\2\u00e6\u00e8\7Z\2\2\u00e7\u00e3\3\2\2\2\u00e7\u00e5")
        buf.write("\3\2\2\2\u00e8\u00e9\3\2\2\2\u00e9\u00ed\t\2\2\2\u00ea")
        buf.write("\u00ec\t\3\2\2\u00eb\u00ea\3\2\2\2\u00ec\u00ef\3\2\2\2")
        buf.write("\u00ed\u00eb\3\2\2\2\u00ed\u00ee\3\2\2\2\u00ee\u00f0\3")
        buf.write("\2\2\2\u00ef\u00ed\3\2\2\2\u00f0\u00fa\t\3\2\2\u00f1\u00f2")
        buf.write("\7\62\2\2\u00f2\u00f6\7z\2\2\u00f3\u00f4\7\62\2\2\u00f4")
        buf.write("\u00f6\7Z\2\2\u00f5\u00f1\3\2\2\2\u00f5\u00f3\3\2\2\2")
        buf.write("\u00f6\u00f7\3\2\2\2\u00f7\u00f8\t\2\2\2\u00f8\u00fa\b")
        buf.write("\13\3\2\u00f9\u00e7\3\2\2\2\u00f9\u00f5\3\2\2\2\u00fa")
        buf.write("\26\3\2\2\2\u00fb\u00fc\7\62\2\2\u00fc\u0100\t\4\2\2\u00fd")
        buf.write("\u00ff\t\5\2\2\u00fe\u00fd\3\2\2\2\u00ff\u0102\3\2\2\2")
        buf.write("\u0100\u00fe\3\2\2\2\u0100\u0101\3\2\2\2\u0101\u0103\3")
        buf.write("\2\2\2\u0102\u0100\3\2\2\2\u0103\u0108\t\4\2\2\u0104\u0105")
        buf.write("\7\62\2\2\u0105\u0106\t\4\2\2\u0106\u0108\b\f\4\2\u0107")
        buf.write("\u00fb\3\2\2\2\u0107\u0104\3\2\2\2\u0108\30\3\2\2\2\u0109")
        buf.write("\u010a\7\62\2\2\u010a\u010e\7d\2\2\u010b\u010c\7\62\2")
        buf.write("\2\u010c\u010e\7D\2\2\u010d\u0109\3\2\2\2\u010d\u010b")
        buf.write("\3\2\2\2\u010e\u010f\3\2\2\2\u010f\u0113\t\6\2\2\u0110")
        buf.write("\u0112\t\7\2\2\u0111\u0110\3\2\2\2\u0112\u0115\3\2\2\2")
        buf.write("\u0113\u0111\3\2\2\2\u0113\u0114\3\2\2\2\u0114\u0116\3")
        buf.write("\2\2\2\u0115\u0113\3\2\2\2\u0116\u0120\t\6\2\2\u0117\u0118")
        buf.write("\7\62\2\2\u0118\u011c\7d\2\2\u0119\u011a\7\62\2\2\u011a")
        buf.write("\u011c\7D\2\2\u011b\u0117\3\2\2\2\u011b\u0119\3\2\2\2")
        buf.write("\u011c\u011d\3\2\2\2\u011d\u011e\t\6\2\2\u011e\u0120\b")
        buf.write("\r\5\2\u011f\u010d\3\2\2\2\u011f\u011b\3\2\2\2\u0120\32")
        buf.write("\3\2\2\2\u0121\u012c\t\4\2\2\u0122\u0126\t\b\2\2\u0123")
        buf.write("\u0125\t\5\2\2\u0124\u0123\3\2\2\2\u0125\u0128\3\2\2\2")
        buf.write("\u0126\u0124\3\2\2\2\u0126\u0127\3\2\2\2\u0127\u0129\3")
        buf.write("\2\2\2\u0128\u0126\3\2\2\2\u0129\u012a\t\4\2\2\u012a\u012c")
        buf.write("\b\16\6\2\u012b\u0121\3\2\2\2\u012b\u0122\3\2\2\2\u012c")
        buf.write("\34\3\2\2\2\u012d\u012e\7)\2\2\u012e\u0132\7$\2\2\u012f")
        buf.write("\u0132\n\t\2\2\u0130\u0132\5\37\20\2\u0131\u012d\3\2\2")
        buf.write("\2\u0131\u012f\3\2\2\2\u0131\u0130\3\2\2\2\u0132\36\3")
        buf.write("\2\2\2\u0133\u0134\7^\2\2\u0134\u0135\t\n\2\2\u0135 \3")
        buf.write("\2\2\2\u0136\u0137\7^\2\2\u0137\u013c\n\n\2\2\u0138\u0139")
        buf.write("\7)\2\2\u0139\u013c\n\13\2\2\u013a\u013c\7^\2\2\u013b")
        buf.write("\u0136\3\2\2\2\u013b\u0138\3\2\2\2\u013b\u013a\3\2\2\2")
        buf.write("\u013c\"\3\2\2\2\u013d\u0141\7$\2\2\u013e\u0140\5\35\17")
        buf.write("\2\u013f\u013e\3\2\2\2\u0140\u0143\3\2\2\2\u0141\u013f")
        buf.write("\3\2\2\2\u0141\u0142\3\2\2\2\u0142\u0144\3\2\2\2\u0143")
        buf.write("\u0141\3\2\2\2\u0144\u0145\7$\2\2\u0145\u0146\b\22\7\2")
        buf.write("\u0146$\3\2\2\2\u0147\u014b\7$\2\2\u0148\u014a\5\35\17")
        buf.write("\2\u0149\u0148\3\2\2\2\u014a\u014d\3\2\2\2\u014b\u0149")
        buf.write("\3\2\2\2\u014b\u014c\3\2\2\2\u014c\u014e\3\2\2\2\u014d")
        buf.write("\u014b\3\2\2\2\u014e\u014f\5!\21\2\u014f\u0150\b\23\b")
        buf.write("\2\u0150&\3\2\2\2\u0151\u0155\7$\2\2\u0152\u0154\5\35")
        buf.write("\17\2\u0153\u0152\3\2\2\2\u0154\u0157\3\2\2\2\u0155\u0153")
        buf.write("\3\2\2\2\u0155\u0156\3\2\2\2\u0156\u0158\3\2\2\2\u0157")
        buf.write("\u0155\3\2\2\2\u0158\u0159\b\24\t\2\u0159(\3\2\2\2\u015a")
        buf.write("\u015b\5\33\16\2\u015b\u015c\5\u0093J\2\u015c\u015d\5")
        buf.write("\33\16\2\u015d\u0168\3\2\2\2\u015e\u015f\5\33\16\2\u015f")
        buf.write("\u0160\5C\"\2\u0160\u0168\3\2\2\2\u0161\u0162\5\33\16")
        buf.write("\2\u0162\u0163\5\u0093J\2\u0163\u0164\5\33\16\2\u0164")
        buf.write("\u0165\5C\"\2\u0165\u0166\b\25\n\2\u0166\u0168\3\2\2\2")
        buf.write("\u0167\u015a\3\2\2\2\u0167\u015e\3\2\2\2\u0167\u0161\3")
        buf.write("\2\2\2\u0168*\3\2\2\2\u0169\u016a\7X\2\2\u016a\u016b\7")
        buf.write("c\2\2\u016b\u016c\7n\2\2\u016c,\3\2\2\2\u016d\u016e\7")
        buf.write("X\2\2\u016e\u016f\7c\2\2\u016f\u0170\7t\2\2\u0170.\3\2")
        buf.write("\2\2\u0171\u0172\7&\2\2\u0172\60\3\2\2\2\u0173\u0174\7")
        buf.write("*\2\2\u0174\62\3\2\2\2\u0175\u0176\7+\2\2\u0176\64\3\2")
        buf.write("\2\2\u0177\u0178\7}\2\2\u0178\66\3\2\2\2\u0179\u017a\7")
        buf.write("\177\2\2\u017a8\3\2\2\2\u017b\u017c\7]\2\2\u017c:\3\2")
        buf.write("\2\2\u017d\u017e\7_\2\2\u017e<\3\2\2\2\u017f\u0180\7=")
        buf.write("\2\2\u0180>\3\2\2\2\u0181\u0182\7.\2\2\u0182@\3\2\2\2")
        buf.write("\u0183\u0184\7<\2\2\u0184B\3\2\2\2\u0185\u0187\t\f\2\2")
        buf.write("\u0186\u0188\5I%\2\u0187\u0186\3\2\2\2\u0187\u0188\3\2")
        buf.write("\2\2\u0188\u0189\3\2\2\2\u0189\u018a\5\33\16\2\u018aD")
        buf.write("\3\2\2\2\u018b\u018c\t\4\2\2\u018cF\3\2\2\2\u018d\u0197")
        buf.write("\t\4\2\2\u018e\u0192\t\b\2\2\u018f\u0191\t\5\2\2\u0190")
        buf.write("\u018f\3\2\2\2\u0191\u0194\3\2\2\2\u0192\u0190\3\2\2\2")
        buf.write("\u0192\u0193\3\2\2\2\u0193\u0195\3\2\2\2\u0194\u0192\3")
        buf.write("\2\2\2\u0195\u0197\t\4\2\2\u0196\u018d\3\2\2\2\u0196\u018e")
        buf.write("\3\2\2\2\u0197H\3\2\2\2\u0198\u0199\t\r\2\2\u0199J\3\2")
        buf.write("\2\2\u019a\u019b\7E\2\2\u019b\u019c\7n\2\2\u019c\u019d")
        buf.write("\7c\2\2\u019d\u019e\7u\2\2\u019e\u019f\7u\2\2\u019fL\3")
        buf.write("\2\2\2\u01a0\u01a1\7D\2\2\u01a1\u01a2\7t\2\2\u01a2\u01a3")
        buf.write("\7g\2\2\u01a3\u01a4\7c\2\2\u01a4\u01a5\7m\2\2\u01a5N\3")
        buf.write("\2\2\2\u01a6\u01a7\7E\2\2\u01a7\u01a8\7q\2\2\u01a8\u01a9")
        buf.write("\7p\2\2\u01a9\u01aa\7v\2\2\u01aa\u01ab\7k\2\2\u01ab\u01ac")
        buf.write("\7p\2\2\u01ac\u01ad\7w\2\2\u01ad\u01ae\7g\2\2\u01aeP\3")
        buf.write("\2\2\2\u01af\u01b0\7K\2\2\u01b0\u01b1\7h\2\2\u01b1R\3")
        buf.write("\2\2\2\u01b2\u01b3\7G\2\2\u01b3\u01b4\7n\2\2\u01b4\u01b5")
        buf.write("\7u\2\2\u01b5\u01b6\7g\2\2\u01b6\u01b7\7k\2\2\u01b7\u01b8")
        buf.write("\7h\2\2\u01b8T\3\2\2\2\u01b9\u01ba\7G\2\2\u01ba\u01bb")
        buf.write("\7n\2\2\u01bb\u01bc\7u\2\2\u01bc\u01bd\7g\2\2\u01bdV\3")
        buf.write("\2\2\2\u01be\u01bf\7H\2\2\u01bf\u01c0\7q\2\2\u01c0\u01c1")
        buf.write("\7t\2\2\u01c1\u01c2\7g\2\2\u01c2\u01c3\7c\2\2\u01c3\u01c4")
        buf.write("\7e\2\2\u01c4\u01c5\7j\2\2\u01c5X\3\2\2\2\u01c6\u01c7")
        buf.write("\7V\2\2\u01c7\u01c8\7t\2\2\u01c8\u01c9\7w\2\2\u01c9\u01ca")
        buf.write("\7g\2\2\u01caZ\3\2\2\2\u01cb\u01cc\7H\2\2\u01cc\u01cd")
        buf.write("\7c\2\2\u01cd\u01ce\7n\2\2\u01ce\u01cf\7u\2\2\u01cf\u01d0")
        buf.write("\7g\2\2\u01d0\\\3\2\2\2\u01d1\u01d2\7C\2\2\u01d2\u01d3")
        buf.write("\7t\2\2\u01d3\u01d4\7t\2\2\u01d4\u01d5\7c\2\2\u01d5\u01d6")
        buf.write("\7{\2\2\u01d6^\3\2\2\2\u01d7\u01d8\7K\2\2\u01d8\u01d9")
        buf.write("\7p\2\2\u01d9`\3\2\2\2\u01da\u01db\7D\2\2\u01db\u01dc")
        buf.write("\7q\2\2\u01dc\u01dd\7q\2\2\u01dd\u01de\7n\2\2\u01de\u01df")
        buf.write("\7g\2\2\u01df\u01e0\7c\2\2\u01e0\u01e1\7p\2\2\u01e1b\3")
        buf.write("\2\2\2\u01e2\u01e3\7T\2\2\u01e3\u01e4\7g\2\2\u01e4\u01e5")
        buf.write("\7v\2\2\u01e5\u01e6\7w\2\2\u01e6\u01e7\7t\2\2\u01e7\u01e8")
        buf.write("\7p\2\2\u01e8d\3\2\2\2\u01e9\u01ea\7P\2\2\u01ea\u01eb")
        buf.write("\7w\2\2\u01eb\u01ec\7n\2\2\u01ec\u01ed\7n\2\2\u01edf\3")
        buf.write("\2\2\2\u01ee\u01ef\7E\2\2\u01ef\u01f0\7q\2\2\u01f0\u01f1")
        buf.write("\7p\2\2\u01f1\u01f2\7u\2\2\u01f2\u01f3\7v\2\2\u01f3\u01f4")
        buf.write("\7t\2\2\u01f4\u01f5\7w\2\2\u01f5\u01f6\7e\2\2\u01f6\u01f7")
        buf.write("\7v\2\2\u01f7\u01f8\7q\2\2\u01f8\u01f9\7t\2\2\u01f9h\3")
        buf.write("\2\2\2\u01fa\u01fb\7F\2\2\u01fb\u01fc\7g\2\2\u01fc\u01fd")
        buf.write("\7u\2\2\u01fd\u01fe\7v\2\2\u01fe\u01ff\7t\2\2\u01ff\u0200")
        buf.write("\7w\2\2\u0200\u0201\7e\2\2\u0201\u0202\7v\2\2\u0202\u0203")
        buf.write("\7q\2\2\u0203\u0204\7t\2\2\u0204j\3\2\2\2\u0205\u0206")
        buf.write("\7P\2\2\u0206\u0207\7g\2\2\u0207\u0208\7y\2\2\u0208l\3")
        buf.write("\2\2\2\u0209\u020a\7D\2\2\u020a\u020b\7{\2\2\u020bn\3")
        buf.write("\2\2\2\u020c\u020d\7U\2\2\u020d\u020e\7g\2\2\u020e\u020f")
        buf.write("\7n\2\2\u020f\u0210\7h\2\2\u0210p\3\2\2\2\u0211\u0212")
        buf.write("\7-\2\2\u0212r\3\2\2\2\u0213\u0214\7/\2\2\u0214t\3\2\2")
        buf.write("\2\u0215\u0216\7,\2\2\u0216v\3\2\2\2\u0217\u0218\7\61")
        buf.write("\2\2\u0218x\3\2\2\2\u0219\u021a\7\'\2\2\u021az\3\2\2\2")
        buf.write("\u021b\u021c\7#\2\2\u021c|\3\2\2\2\u021d\u021e\7(\2\2")
        buf.write("\u021e\u021f\7(\2\2\u021f~\3\2\2\2\u0220\u0221\7~\2\2")
        buf.write("\u0221\u0222\7~\2\2\u0222\u0080\3\2\2\2\u0223\u0224\7")
        buf.write("?\2\2\u0224\u0225\7?\2\2\u0225\u0082\3\2\2\2\u0226\u0227")
        buf.write("\7?\2\2\u0227\u0084\3\2\2\2\u0228\u0229\7#\2\2\u0229\u022a")
        buf.write("\7?\2\2\u022a\u0086\3\2\2\2\u022b\u022c\7@\2\2\u022c\u0088")
        buf.write("\3\2\2\2\u022d\u022e\7@\2\2\u022e\u022f\7?\2\2\u022f\u008a")
        buf.write("\3\2\2\2\u0230\u0231\7>\2\2\u0231\u008c\3\2\2\2\u0232")
        buf.write("\u0233\7>\2\2\u0233\u0234\7?\2\2\u0234\u008e\3\2\2\2\u0235")
        buf.write("\u0236\7?\2\2\u0236\u0237\7?\2\2\u0237\u0238\7\60\2\2")
        buf.write("\u0238\u0090\3\2\2\2\u0239\u023a\7-\2\2\u023a\u023b\7")
        buf.write("\60\2\2\u023b\u0092\3\2\2\2\u023c\u023d\7\60\2\2\u023d")
        buf.write("\u0094\3\2\2\2\u023e\u023f\7\60\2\2\u023f\u0240\7\60\2")
        buf.write("\2\u0240\u0096\3\2\2\2\u0241\u0242\7<\2\2\u0242\u0243")
        buf.write("\7<\2\2\u0243\u0098\3\2\2\2\u0244\u0248\t\16\2\2\u0245")
        buf.write("\u0247\t\17\2\2\u0246\u0245\3\2\2\2\u0247\u024a\3\2\2")
        buf.write("\2\u0248\u0246\3\2\2\2\u0248\u0249\3\2\2\2\u0249\u009a")
        buf.write("\3\2\2\2\u024a\u0248\3\2\2\2\u024b\u024d\5/\30\2\u024c")
        buf.write("\u024e\t\17\2\2\u024d\u024c\3\2\2\2\u024e\u024f\3\2\2")
        buf.write("\2\u024f\u024d\3\2\2\2\u024f\u0250\3\2\2\2\u0250\u009c")
        buf.write("\3\2\2\2\u0251\u0253\t\20\2\2\u0252\u0251\3\2\2\2\u0253")
        buf.write("\u0254\3\2\2\2\u0254\u0252\3\2\2\2\u0254\u0255\3\2\2\2")
        buf.write("\u0255\u0256\3\2\2\2\u0256\u0257\bO\13\2\u0257\u009e\3")
        buf.write("\2\2\2\u0258\u0259\7%\2\2\u0259\u025a\7%\2\2\u025a\u025e")
        buf.write("\3\2\2\2\u025b\u025d\13\2\2\2\u025c\u025b\3\2\2\2\u025d")
        buf.write("\u0260\3\2\2\2\u025e\u025f\3\2\2\2\u025e\u025c\3\2\2\2")
        buf.write("\u025f\u0261\3\2\2\2\u0260\u025e\3\2\2\2\u0261\u0262\7")
        buf.write("%\2\2\u0262\u0263\7%\2\2\u0263\u0264\3\2\2\2\u0264\u0265")
        buf.write("\bP\13\2\u0265\u00a0\3\2\2\2\u0266\u0267\13\2\2\2\u0267")
        buf.write("\u0268\bQ\f\2\u0268\u00a2\3\2\2\2\36\2\u00c3\u00e1\u00e7")
        buf.write("\u00ed\u00f5\u00f9\u0100\u0107\u010d\u0113\u011b\u011f")
        buf.write("\u0126\u012b\u0131\u013b\u0141\u014b\u0155\u0167\u0187")
        buf.write("\u0192\u0196\u0248\u024f\u0254\u025e\r\3\n\2\3\13\3\3")
        buf.write("\f\4\3\r\5\3\16\6\3\22\7\3\23\b\3\24\t\3\25\n\b\2\2\3")
        buf.write("Q\13")
        return buf.getvalue()


class D96Lexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    T__0 = 1
    T__1 = 2
    T__2 = 3
    BOOL_TYPE = 4
    FLOAT_TYPE = 5
    STRING = 6
    INT_TYPE = 7
    VOID_TYPE = 8
    INTEGER_LITERAL = 9
    HEX_TYPE = 10
    OCT_TYPE = 11
    BIN_TYPE = 12
    DEC_TYPE = 13
    STRING_LITERAL = 14
    ILLEGAL_ESCAPE = 15
    UNCLOSE_STRING = 16
    REAL_LITERAL = 17
    VAL = 18
    VAR = 19
    LP = 20
    RP = 21
    LCB = 22
    RCB = 23
    LSB = 24
    RSB = 25
    SEMI = 26
    COMMA = 27
    COLON = 28
    CLASS = 29
    BREAK = 30
    CONTINUE = 31
    IF = 32
    ELSEIF = 33
    ELSE = 34
    FOREACH = 35
    TRUE = 36
    FALSE = 37
    ARRAY = 38
    IN = 39
    BOOLEAN = 40
    RETURN = 41
    NULL = 42
    CONSTRUCTOR = 43
    DESTRUCTOR = 44
    NEW = 45
    BY = 46
    SELF = 47
    ADD = 48
    SUB = 49
    MUL = 50
    DIV = 51
    MOD = 52
    NOT = 53
    AND = 54
    OR = 55
    EQUAL = 56
    ASSIGN = 57
    NOTEQUAL = 58
    GT = 59
    GTE = 60
    LT = 61
    LTE = 62
    EQUAL_STR = 63
    ADD_STR = 64
    DOT = 65
    DOTDOT = 66
    SCOPE = 67
    NORMAL_ID = 68
    DOLLAR_ID = 69
    WS = 70
    BLOCK_COMMENT = 71
    ERROR_CHAR = 72

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'Program'", "'main'", "'assign_statement'", "'Float'", "'String'", 
            "'Int'", "'Void'", "'Val'", "'Var'", "'('", "')'", "'{'", "'}'", 
            "'['", "']'", "';'", "','", "':'", "'Class'", "'Break'", "'Continue'", 
            "'If'", "'Elseif'", "'Else'", "'Foreach'", "'True'", "'False'", 
            "'Array'", "'In'", "'Boolean'", "'Return'", "'Null'", "'Constructor'", 
            "'Destructor'", "'New'", "'By'", "'Self'", "'+'", "'-'", "'*'", 
            "'/'", "'%'", "'!'", "'&&'", "'||'", "'=='", "'='", "'!='", 
            "'>'", "'>='", "'<'", "'<='", "'==.'", "'+.'", "'.'", "'..'", 
            "'::'" ]

    symbolicNames = [ "<INVALID>",
            "BOOL_TYPE", "FLOAT_TYPE", "STRING", "INT_TYPE", "VOID_TYPE", 
            "INTEGER_LITERAL", "HEX_TYPE", "OCT_TYPE", "BIN_TYPE", "DEC_TYPE", 
            "STRING_LITERAL", "ILLEGAL_ESCAPE", "UNCLOSE_STRING", "REAL_LITERAL", 
            "VAL", "VAR", "LP", "RP", "LCB", "RCB", "LSB", "RSB", "SEMI", 
            "COMMA", "COLON", "CLASS", "BREAK", "CONTINUE", "IF", "ELSEIF", 
            "ELSE", "FOREACH", "TRUE", "FALSE", "ARRAY", "IN", "BOOLEAN", 
            "RETURN", "NULL", "CONSTRUCTOR", "DESTRUCTOR", "NEW", "BY", 
            "SELF", "ADD", "SUB", "MUL", "DIV", "MOD", "NOT", "AND", "OR", 
            "EQUAL", "ASSIGN", "NOTEQUAL", "GT", "GTE", "LT", "LTE", "EQUAL_STR", 
            "ADD_STR", "DOT", "DOTDOT", "SCOPE", "NORMAL_ID", "DOLLAR_ID", 
            "WS", "BLOCK_COMMENT", "ERROR_CHAR" ]

    ruleNames = [ "T__0", "T__1", "T__2", "BOOL_TYPE", "FLOAT_TYPE", "STRING", 
                  "INT_TYPE", "VOID_TYPE", "INTEGER_LITERAL", "HEX_TYPE", 
                  "OCT_TYPE", "BIN_TYPE", "DEC_TYPE", "STR", "ESC_SEQ", 
                  "ESC_ILLEGAL", "STRING_LITERAL", "ILLEGAL_ESCAPE", "UNCLOSE_STRING", 
                  "REAL_LITERAL", "VAL", "VAR", "DOLLAR", "LP", "RP", "LCB", 
                  "RCB", "LSB", "RSB", "SEMI", "COMMA", "COLON", "EXPONENT", 
                  "DIGIT", "DEC_DIGIT", "SIGN", "CLASS", "BREAK", "CONTINUE", 
                  "IF", "ELSEIF", "ELSE", "FOREACH", "TRUE", "FALSE", "ARRAY", 
                  "IN", "BOOLEAN", "RETURN", "NULL", "CONSTRUCTOR", "DESTRUCTOR", 
                  "NEW", "BY", "SELF", "ADD", "SUB", "MUL", "DIV", "MOD", 
                  "NOT", "AND", "OR", "EQUAL", "ASSIGN", "NOTEQUAL", "GT", 
                  "GTE", "LT", "LTE", "EQUAL_STR", "ADD_STR", "DOT", "DOTDOT", 
                  "SCOPE", "NORMAL_ID", "DOLLAR_ID", "WS", "BLOCK_COMMENT", 
                  "ERROR_CHAR" ]

    grammarFileName = "D96.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.9.2")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


    def emit(self):
        tk = self.type
        result = super().emit() # result mean for input
        # delete later
        print('--------------------------------------------------------------------------------')
        attributes = inspect.getmembers(D96Lexer, lambda a:not(inspect.isroutine(a)))
        user_defined_attr = [a for a in attributes if not(a[0].startswith('__') and a[0].endswith('__'))]
        for i in user_defined_attr:
            if tk == i[1]:
                print ("{:<30} {:<30} {:<50}".format(result.text, '|', i[0]))
        print('--------------------------------------------------------------------------------')

        if tk == self.INTEGER_LITERAL or tk == self.REAL_LITERAL:
            result.text = result.text.replace('_', '')

        return result


    def action(self, localctx:RuleContext, ruleIndex:int, actionIndex:int):
        if self._actions is None:
            actions = dict()
            actions[8] = self.INTEGER_LITERAL_action 
            actions[9] = self.HEX_TYPE_action 
            actions[10] = self.OCT_TYPE_action 
            actions[11] = self.BIN_TYPE_action 
            actions[12] = self.DEC_TYPE_action 
            actions[16] = self.STRING_LITERAL_action 
            actions[17] = self.ILLEGAL_ESCAPE_action 
            actions[18] = self.UNCLOSE_STRING_action 
            actions[19] = self.REAL_LITERAL_action 
            actions[79] = self.ERROR_CHAR_action 
            self._actions = actions
        action = self._actions.get(ruleIndex, None)
        if action is not None:
            action(localctx, actionIndex)
        else:
            raise Exception("No registered action for:" + str(ruleIndex))


    def INTEGER_LITERAL_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 0:

                self.text = self.text.replace('_', '')

     

    def HEX_TYPE_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 1:

                self.text = self.text.replace('_', '')

     

    def OCT_TYPE_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 2:

                self.text = self.text.replace('_', '')

     

    def BIN_TYPE_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 3:

                self.text = self.text.replace('_', '')

     

    def DEC_TYPE_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 4:

                self.text = self.text.replace('_', '')

     

    def STRING_LITERAL_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 5:

                illegal_escape = ['\v']
                for i in self.text:
                    if i in illegal_escape:
                        y = str(self.text)
                        ill_idx = y.index(i)
                        raise IllegalEscape(y[1:ill_idx+1])
                
                y = str(self.text)
                if y.find('\'"') >= 0:
                    y = y.replace('\'"', '"')
                self.text = y[1:-1]

     

    def ILLEGAL_ESCAPE_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 6:

                y = str(self.text)
                raise IllegalEscape(y[1:])

     

    def UNCLOSE_STRING_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 7:

                x = str(self.text)
                raise UncloseString(x[1:])

     

    def REAL_LITERAL_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 8:

                self.text = self.text.replace('_', '')

     

    def ERROR_CHAR_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 9:
            raise ErrorToken(self.text)
     


