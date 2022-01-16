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
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2K")
        buf.write("\u026f\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7")
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
        buf.write("L\4M\tM\4N\tN\4O\tO\4P\tP\4Q\tQ\4R\tR\3\2\3\2\3\2\3\2")
        buf.write("\3\2\3\2\3\2\3\2\3\3\3\3\3\3\3\3\3\3\3\4\3\4\3\4\3\4\3")
        buf.write("\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\5")
        buf.write("\3\5\5\5\u00c6\n\5\3\6\3\6\3\6\3\6\3\6\3\6\3\7\3\7\3\7")
        buf.write("\3\7\3\7\3\7\3\7\3\b\3\b\3\b\3\b\3\t\3\t\3\t\3\t\3\t\3")
        buf.write("\n\3\n\3\n\3\n\3\n\3\n\5\n\u00e4\n\n\3\13\3\13\3\13\3")
        buf.write("\13\5\13\u00ea\n\13\3\13\3\13\7\13\u00ee\n\13\f\13\16")
        buf.write("\13\u00f1\13\13\3\13\3\13\3\13\3\13\3\13\5\13\u00f8\n")
        buf.write("\13\3\13\3\13\5\13\u00fc\n\13\3\f\3\f\3\f\7\f\u0101\n")
        buf.write("\f\f\f\16\f\u0104\13\f\3\f\3\f\3\f\3\f\5\f\u010a\n\f\3")
        buf.write("\r\3\r\3\r\3\r\5\r\u0110\n\r\3\r\3\r\7\r\u0114\n\r\f\r")
        buf.write("\16\r\u0117\13\r\3\r\3\r\3\r\3\r\3\r\5\r\u011e\n\r\3\r")
        buf.write("\3\r\5\r\u0122\n\r\3\16\3\16\3\16\7\16\u0127\n\16\f\16")
        buf.write("\16\16\u012a\13\16\3\16\3\16\5\16\u012e\n\16\3\17\3\17")
        buf.write("\3\17\3\17\5\17\u0134\n\17\3\20\3\20\3\20\3\21\3\21\3")
        buf.write("\21\3\21\3\21\5\21\u013e\n\21\3\22\3\22\7\22\u0142\n\22")
        buf.write("\f\22\16\22\u0145\13\22\3\22\3\22\3\22\3\23\3\23\7\23")
        buf.write("\u014c\n\23\f\23\16\23\u014f\13\23\3\23\3\23\3\23\3\24")
        buf.write("\3\24\7\24\u0156\n\24\f\24\16\24\u0159\13\24\3\24\3\24")
        buf.write("\3\25\3\25\3\25\3\25\3\25\3\25\3\25\3\25\3\25\3\25\3\25")
        buf.write("\3\25\3\25\5\25\u016a\n\25\3\26\3\26\3\26\3\26\3\27\3")
        buf.write("\27\3\27\3\27\3\30\3\30\3\31\3\31\3\32\3\32\3\33\3\33")
        buf.write("\3\34\3\34\3\35\3\35\3\36\3\36\3\37\3\37\3 \3 \3!\3!\3")
        buf.write("\"\3\"\5\"\u018a\n\"\3\"\3\"\3#\3#\3$\3$\3$\7$\u0193\n")
        buf.write("$\f$\16$\u0196\13$\3$\5$\u0199\n$\3%\3%\3&\3&\3&\3&\3")
        buf.write("&\3&\3\'\3\'\3\'\3\'\3\'\3\'\3(\3(\3(\3(\3(\3(\3(\3(\3")
        buf.write("(\3)\3)\3)\3*\3*\3*\3*\3*\3*\3*\3+\3+\3+\3+\3+\3,\3,\3")
        buf.write(",\3,\3,\3,\3,\3,\3-\3-\3-\3-\3-\3.\3.\3.\3.\3.\3.\3/\3")
        buf.write("/\3/\3/\3/\3/\3\60\3\60\3\60\3\61\3\61\3\61\3\61\3\61")
        buf.write("\3\61\3\61\3\61\3\62\3\62\3\62\3\62\3\62\3\62\3\62\3\63")
        buf.write("\3\63\3\63\3\63\3\63\3\64\3\64\3\64\3\64\3\64\3\64\3\64")
        buf.write("\3\64\3\64\3\64\3\64\3\64\3\65\3\65\3\65\3\65\3\65\3\65")
        buf.write("\3\65\3\65\3\65\3\65\3\65\3\66\3\66\3\66\3\66\3\67\3\67")
        buf.write("\3\67\38\38\38\38\38\39\39\3:\3:\3;\3;\3<\3<\3=\3=\3>")
        buf.write("\3>\3?\3?\3?\3@\3@\3@\3A\3A\3A\3B\3B\3C\3C\3C\3D\3D\3")
        buf.write("E\3E\3E\3F\3F\3G\3G\3G\3H\3H\3H\3H\3I\3I\3I\3J\3J\3K\3")
        buf.write("K\3K\3L\3L\3L\3M\3M\7M\u0249\nM\fM\16M\u024c\13M\3N\3")
        buf.write("N\6N\u0250\nN\rN\16N\u0251\3O\3O\5O\u0256\nO\3P\6P\u0259")
        buf.write("\nP\rP\16P\u025a\3P\3P\3Q\3Q\3Q\3Q\7Q\u0263\nQ\fQ\16Q")
        buf.write("\u0266\13Q\3Q\3Q\3Q\3Q\3Q\3R\3R\3R\3\u0264\2S\3\3\5\4")
        buf.write("\7\5\t\6\13\7\r\b\17\t\21\n\23\13\25\f\27\r\31\16\33\17")
        buf.write("\35\2\37\2!\2#\20%\21\'\22)\23+\24-\25/\2\61\26\63\27")
        buf.write("\65\30\67\319\32;\33=\34?\35A\36C\2E\2G\2I\2K\37M O!Q")
        buf.write("\"S#U$W%Y&[\'](_)a*c+e,g-i.k/m\60o\61q\62s\63u\64w\65")
        buf.write("y\66{\67}8\1779\u0081:\u0083;\u0085<\u0087=\u0089>\u008b")
        buf.write("?\u008d@\u008fA\u0091B\u0093C\u0095D\u0097E\u0099F\u009b")
        buf.write("G\u009dH\u009fI\u00a1J\u00a3K\3\2\21\5\2\62;CHch\6\2\62")
        buf.write(";CHaach\3\2\62;\4\2\62;aa\3\2\62\63\4\2\62\63aa\3\2\63")
        buf.write(";\4\2$$^^\t\2))^^ddhhppttvv\3\2$$\4\2GGgg\4\2--//\5\2")
        buf.write("C\\aac|\6\2\62;C\\aac|\5\2\13\f\16\17\"\"\2\u0287\2\3")
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
        buf.write("\3\2\2\2\2\u009f\3\2\2\2\2\u00a1\3\2\2\2\2\u00a3\3\2\2")
        buf.write("\2\3\u00a5\3\2\2\2\5\u00ad\3\2\2\2\7\u00b2\3\2\2\2\t\u00c5")
        buf.write("\3\2\2\2\13\u00c7\3\2\2\2\r\u00cd\3\2\2\2\17\u00d4\3\2")
        buf.write("\2\2\21\u00d8\3\2\2\2\23\u00e3\3\2\2\2\25\u00fb\3\2\2")
        buf.write("\2\27\u0109\3\2\2\2\31\u0121\3\2\2\2\33\u012d\3\2\2\2")
        buf.write("\35\u0133\3\2\2\2\37\u0135\3\2\2\2!\u013d\3\2\2\2#\u013f")
        buf.write("\3\2\2\2%\u0149\3\2\2\2\'\u0153\3\2\2\2)\u0169\3\2\2\2")
        buf.write("+\u016b\3\2\2\2-\u016f\3\2\2\2/\u0173\3\2\2\2\61\u0175")
        buf.write("\3\2\2\2\63\u0177\3\2\2\2\65\u0179\3\2\2\2\67\u017b\3")
        buf.write("\2\2\29\u017d\3\2\2\2;\u017f\3\2\2\2=\u0181\3\2\2\2?\u0183")
        buf.write("\3\2\2\2A\u0185\3\2\2\2C\u0187\3\2\2\2E\u018d\3\2\2\2")
        buf.write("G\u0198\3\2\2\2I\u019a\3\2\2\2K\u019c\3\2\2\2M\u01a2\3")
        buf.write("\2\2\2O\u01a8\3\2\2\2Q\u01b1\3\2\2\2S\u01b4\3\2\2\2U\u01bb")
        buf.write("\3\2\2\2W\u01c0\3\2\2\2Y\u01c8\3\2\2\2[\u01cd\3\2\2\2")
        buf.write("]\u01d3\3\2\2\2_\u01d9\3\2\2\2a\u01dc\3\2\2\2c\u01e4\3")
        buf.write("\2\2\2e\u01eb\3\2\2\2g\u01f0\3\2\2\2i\u01fc\3\2\2\2k\u0207")
        buf.write("\3\2\2\2m\u020b\3\2\2\2o\u020e\3\2\2\2q\u0213\3\2\2\2")
        buf.write("s\u0215\3\2\2\2u\u0217\3\2\2\2w\u0219\3\2\2\2y\u021b\3")
        buf.write("\2\2\2{\u021d\3\2\2\2}\u021f\3\2\2\2\177\u0222\3\2\2\2")
        buf.write("\u0081\u0225\3\2\2\2\u0083\u0228\3\2\2\2\u0085\u022a\3")
        buf.write("\2\2\2\u0087\u022d\3\2\2\2\u0089\u022f\3\2\2\2\u008b\u0232")
        buf.write("\3\2\2\2\u008d\u0234\3\2\2\2\u008f\u0237\3\2\2\2\u0091")
        buf.write("\u023b\3\2\2\2\u0093\u023e\3\2\2\2\u0095\u0240\3\2\2\2")
        buf.write("\u0097\u0243\3\2\2\2\u0099\u0246\3\2\2\2\u009b\u024d\3")
        buf.write("\2\2\2\u009d\u0255\3\2\2\2\u009f\u0258\3\2\2\2\u00a1\u025e")
        buf.write("\3\2\2\2\u00a3\u026c\3\2\2\2\u00a5\u00a6\7R\2\2\u00a6")
        buf.write("\u00a7\7t\2\2\u00a7\u00a8\7q\2\2\u00a8\u00a9\7i\2\2\u00a9")
        buf.write("\u00aa\7t\2\2\u00aa\u00ab\7c\2\2\u00ab\u00ac\7o\2\2\u00ac")
        buf.write("\4\3\2\2\2\u00ad\u00ae\7o\2\2\u00ae\u00af\7c\2\2\u00af")
        buf.write("\u00b0\7k\2\2\u00b0\u00b1\7p\2\2\u00b1\6\3\2\2\2\u00b2")
        buf.write("\u00b3\7c\2\2\u00b3\u00b4\7u\2\2\u00b4\u00b5\7u\2\2\u00b5")
        buf.write("\u00b6\7k\2\2\u00b6\u00b7\7i\2\2\u00b7\u00b8\7p\2\2\u00b8")
        buf.write("\u00b9\7a\2\2\u00b9\u00ba\7u\2\2\u00ba\u00bb\7v\2\2\u00bb")
        buf.write("\u00bc\7c\2\2\u00bc\u00bd\7v\2\2\u00bd\u00be\7g\2\2\u00be")
        buf.write("\u00bf\7o\2\2\u00bf\u00c0\7g\2\2\u00c0\u00c1\7p\2\2\u00c1")
        buf.write("\u00c2\7v\2\2\u00c2\b\3\2\2\2\u00c3\u00c6\5Y-\2\u00c4")
        buf.write("\u00c6\5[.\2\u00c5\u00c3\3\2\2\2\u00c5\u00c4\3\2\2\2\u00c6")
        buf.write("\n\3\2\2\2\u00c7\u00c8\7H\2\2\u00c8\u00c9\7n\2\2\u00c9")
        buf.write("\u00ca\7q\2\2\u00ca\u00cb\7c\2\2\u00cb\u00cc\7v\2\2\u00cc")
        buf.write("\f\3\2\2\2\u00cd\u00ce\7U\2\2\u00ce\u00cf\7v\2\2\u00cf")
        buf.write("\u00d0\7t\2\2\u00d0\u00d1\7k\2\2\u00d1\u00d2\7p\2\2\u00d2")
        buf.write("\u00d3\7i\2\2\u00d3\16\3\2\2\2\u00d4\u00d5\7K\2\2\u00d5")
        buf.write("\u00d6\7p\2\2\u00d6\u00d7\7v\2\2\u00d7\20\3\2\2\2\u00d8")
        buf.write("\u00d9\7X\2\2\u00d9\u00da\7q\2\2\u00da\u00db\7k\2\2\u00db")
        buf.write("\u00dc\7f\2\2\u00dc\22\3\2\2\2\u00dd\u00e4\5\25\13\2\u00de")
        buf.write("\u00e4\5\27\f\2\u00df\u00e4\5\31\r\2\u00e0\u00e1\5\33")
        buf.write("\16\2\u00e1\u00e2\b\n\2\2\u00e2\u00e4\3\2\2\2\u00e3\u00dd")
        buf.write("\3\2\2\2\u00e3\u00de\3\2\2\2\u00e3\u00df\3\2\2\2\u00e3")
        buf.write("\u00e0\3\2\2\2\u00e4\24\3\2\2\2\u00e5\u00e6\7\62\2\2\u00e6")
        buf.write("\u00ea\7z\2\2\u00e7\u00e8\7\62\2\2\u00e8\u00ea\7Z\2\2")
        buf.write("\u00e9\u00e5\3\2\2\2\u00e9\u00e7\3\2\2\2\u00ea\u00eb\3")
        buf.write("\2\2\2\u00eb\u00ef\t\2\2\2\u00ec\u00ee\t\3\2\2\u00ed\u00ec")
        buf.write("\3\2\2\2\u00ee\u00f1\3\2\2\2\u00ef\u00ed\3\2\2\2\u00ef")
        buf.write("\u00f0\3\2\2\2\u00f0\u00f2\3\2\2\2\u00f1\u00ef\3\2\2\2")
        buf.write("\u00f2\u00fc\t\3\2\2\u00f3\u00f4\7\62\2\2\u00f4\u00f8")
        buf.write("\7z\2\2\u00f5\u00f6\7\62\2\2\u00f6\u00f8\7Z\2\2\u00f7")
        buf.write("\u00f3\3\2\2\2\u00f7\u00f5\3\2\2\2\u00f8\u00f9\3\2\2\2")
        buf.write("\u00f9\u00fa\t\2\2\2\u00fa\u00fc\b\13\3\2\u00fb\u00e9")
        buf.write("\3\2\2\2\u00fb\u00f7\3\2\2\2\u00fc\26\3\2\2\2\u00fd\u00fe")
        buf.write("\7\62\2\2\u00fe\u0102\t\4\2\2\u00ff\u0101\t\5\2\2\u0100")
        buf.write("\u00ff\3\2\2\2\u0101\u0104\3\2\2\2\u0102\u0100\3\2\2\2")
        buf.write("\u0102\u0103\3\2\2\2\u0103\u0105\3\2\2\2\u0104\u0102\3")
        buf.write("\2\2\2\u0105\u010a\t\4\2\2\u0106\u0107\7\62\2\2\u0107")
        buf.write("\u0108\t\4\2\2\u0108\u010a\b\f\4\2\u0109\u00fd\3\2\2\2")
        buf.write("\u0109\u0106\3\2\2\2\u010a\30\3\2\2\2\u010b\u010c\7\62")
        buf.write("\2\2\u010c\u0110\7d\2\2\u010d\u010e\7\62\2\2\u010e\u0110")
        buf.write("\7D\2\2\u010f\u010b\3\2\2\2\u010f\u010d\3\2\2\2\u0110")
        buf.write("\u0111\3\2\2\2\u0111\u0115\t\6\2\2\u0112\u0114\t\7\2\2")
        buf.write("\u0113\u0112\3\2\2\2\u0114\u0117\3\2\2\2\u0115\u0113\3")
        buf.write("\2\2\2\u0115\u0116\3\2\2\2\u0116\u0118\3\2\2\2\u0117\u0115")
        buf.write("\3\2\2\2\u0118\u0122\t\6\2\2\u0119\u011a\7\62\2\2\u011a")
        buf.write("\u011e\7d\2\2\u011b\u011c\7\62\2\2\u011c\u011e\7D\2\2")
        buf.write("\u011d\u0119\3\2\2\2\u011d\u011b\3\2\2\2\u011e\u011f\3")
        buf.write("\2\2\2\u011f\u0120\t\6\2\2\u0120\u0122\b\r\5\2\u0121\u010f")
        buf.write("\3\2\2\2\u0121\u011d\3\2\2\2\u0122\32\3\2\2\2\u0123\u012e")
        buf.write("\t\4\2\2\u0124\u0128\t\b\2\2\u0125\u0127\t\5\2\2\u0126")
        buf.write("\u0125\3\2\2\2\u0127\u012a\3\2\2\2\u0128\u0126\3\2\2\2")
        buf.write("\u0128\u0129\3\2\2\2\u0129\u012b\3\2\2\2\u012a\u0128\3")
        buf.write("\2\2\2\u012b\u012c\t\4\2\2\u012c\u012e\b\16\6\2\u012d")
        buf.write("\u0123\3\2\2\2\u012d\u0124\3\2\2\2\u012e\34\3\2\2\2\u012f")
        buf.write("\u0130\7)\2\2\u0130\u0134\7$\2\2\u0131\u0134\n\t\2\2\u0132")
        buf.write("\u0134\5\37\20\2\u0133\u012f\3\2\2\2\u0133\u0131\3\2\2")
        buf.write("\2\u0133\u0132\3\2\2\2\u0134\36\3\2\2\2\u0135\u0136\7")
        buf.write("^\2\2\u0136\u0137\t\n\2\2\u0137 \3\2\2\2\u0138\u0139\7")
        buf.write("^\2\2\u0139\u013e\n\n\2\2\u013a\u013b\7)\2\2\u013b\u013e")
        buf.write("\n\13\2\2\u013c\u013e\7^\2\2\u013d\u0138\3\2\2\2\u013d")
        buf.write("\u013a\3\2\2\2\u013d\u013c\3\2\2\2\u013e\"\3\2\2\2\u013f")
        buf.write("\u0143\7$\2\2\u0140\u0142\5\35\17\2\u0141\u0140\3\2\2")
        buf.write("\2\u0142\u0145\3\2\2\2\u0143\u0141\3\2\2\2\u0143\u0144")
        buf.write("\3\2\2\2\u0144\u0146\3\2\2\2\u0145\u0143\3\2\2\2\u0146")
        buf.write("\u0147\7$\2\2\u0147\u0148\b\22\7\2\u0148$\3\2\2\2\u0149")
        buf.write("\u014d\7$\2\2\u014a\u014c\5\35\17\2\u014b\u014a\3\2\2")
        buf.write("\2\u014c\u014f\3\2\2\2\u014d\u014b\3\2\2\2\u014d\u014e")
        buf.write("\3\2\2\2\u014e\u0150\3\2\2\2\u014f\u014d\3\2\2\2\u0150")
        buf.write("\u0151\5!\21\2\u0151\u0152\b\23\b\2\u0152&\3\2\2\2\u0153")
        buf.write("\u0157\7$\2\2\u0154\u0156\5\35\17\2\u0155\u0154\3\2\2")
        buf.write("\2\u0156\u0159\3\2\2\2\u0157\u0155\3\2\2\2\u0157\u0158")
        buf.write("\3\2\2\2\u0158\u015a\3\2\2\2\u0159\u0157\3\2\2\2\u015a")
        buf.write("\u015b\b\24\t\2\u015b(\3\2\2\2\u015c\u015d\5\33\16\2\u015d")
        buf.write("\u015e\5\u0093J\2\u015e\u015f\5\33\16\2\u015f\u016a\3")
        buf.write("\2\2\2\u0160\u0161\5\33\16\2\u0161\u0162\5C\"\2\u0162")
        buf.write("\u016a\3\2\2\2\u0163\u0164\5\33\16\2\u0164\u0165\5\u0093")
        buf.write("J\2\u0165\u0166\5\33\16\2\u0166\u0167\5C\"\2\u0167\u0168")
        buf.write("\b\25\n\2\u0168\u016a\3\2\2\2\u0169\u015c\3\2\2\2\u0169")
        buf.write("\u0160\3\2\2\2\u0169\u0163\3\2\2\2\u016a*\3\2\2\2\u016b")
        buf.write("\u016c\7X\2\2\u016c\u016d\7c\2\2\u016d\u016e\7n\2\2\u016e")
        buf.write(",\3\2\2\2\u016f\u0170\7X\2\2\u0170\u0171\7c\2\2\u0171")
        buf.write("\u0172\7t\2\2\u0172.\3\2\2\2\u0173\u0174\7&\2\2\u0174")
        buf.write("\60\3\2\2\2\u0175\u0176\7*\2\2\u0176\62\3\2\2\2\u0177")
        buf.write("\u0178\7+\2\2\u0178\64\3\2\2\2\u0179\u017a\7}\2\2\u017a")
        buf.write("\66\3\2\2\2\u017b\u017c\7\177\2\2\u017c8\3\2\2\2\u017d")
        buf.write("\u017e\7]\2\2\u017e:\3\2\2\2\u017f\u0180\7_\2\2\u0180")
        buf.write("<\3\2\2\2\u0181\u0182\7=\2\2\u0182>\3\2\2\2\u0183\u0184")
        buf.write("\7.\2\2\u0184@\3\2\2\2\u0185\u0186\7<\2\2\u0186B\3\2\2")
        buf.write("\2\u0187\u0189\t\f\2\2\u0188\u018a\5I%\2\u0189\u0188\3")
        buf.write("\2\2\2\u0189\u018a\3\2\2\2\u018a\u018b\3\2\2\2\u018b\u018c")
        buf.write("\5\33\16\2\u018cD\3\2\2\2\u018d\u018e\t\4\2\2\u018eF\3")
        buf.write("\2\2\2\u018f\u0199\t\4\2\2\u0190\u0194\t\b\2\2\u0191\u0193")
        buf.write("\t\5\2\2\u0192\u0191\3\2\2\2\u0193\u0196\3\2\2\2\u0194")
        buf.write("\u0192\3\2\2\2\u0194\u0195\3\2\2\2\u0195\u0197\3\2\2\2")
        buf.write("\u0196\u0194\3\2\2\2\u0197\u0199\t\4\2\2\u0198\u018f\3")
        buf.write("\2\2\2\u0198\u0190\3\2\2\2\u0199H\3\2\2\2\u019a\u019b")
        buf.write("\t\r\2\2\u019bJ\3\2\2\2\u019c\u019d\7E\2\2\u019d\u019e")
        buf.write("\7n\2\2\u019e\u019f\7c\2\2\u019f\u01a0\7u\2\2\u01a0\u01a1")
        buf.write("\7u\2\2\u01a1L\3\2\2\2\u01a2\u01a3\7D\2\2\u01a3\u01a4")
        buf.write("\7t\2\2\u01a4\u01a5\7g\2\2\u01a5\u01a6\7c\2\2\u01a6\u01a7")
        buf.write("\7m\2\2\u01a7N\3\2\2\2\u01a8\u01a9\7E\2\2\u01a9\u01aa")
        buf.write("\7q\2\2\u01aa\u01ab\7p\2\2\u01ab\u01ac\7v\2\2\u01ac\u01ad")
        buf.write("\7k\2\2\u01ad\u01ae\7p\2\2\u01ae\u01af\7w\2\2\u01af\u01b0")
        buf.write("\7g\2\2\u01b0P\3\2\2\2\u01b1\u01b2\7K\2\2\u01b2\u01b3")
        buf.write("\7h\2\2\u01b3R\3\2\2\2\u01b4\u01b5\7G\2\2\u01b5\u01b6")
        buf.write("\7n\2\2\u01b6\u01b7\7u\2\2\u01b7\u01b8\7g\2\2\u01b8\u01b9")
        buf.write("\7k\2\2\u01b9\u01ba\7h\2\2\u01baT\3\2\2\2\u01bb\u01bc")
        buf.write("\7G\2\2\u01bc\u01bd\7n\2\2\u01bd\u01be\7u\2\2\u01be\u01bf")
        buf.write("\7g\2\2\u01bfV\3\2\2\2\u01c0\u01c1\7H\2\2\u01c1\u01c2")
        buf.write("\7q\2\2\u01c2\u01c3\7t\2\2\u01c3\u01c4\7g\2\2\u01c4\u01c5")
        buf.write("\7c\2\2\u01c5\u01c6\7e\2\2\u01c6\u01c7\7j\2\2\u01c7X\3")
        buf.write("\2\2\2\u01c8\u01c9\7V\2\2\u01c9\u01ca\7t\2\2\u01ca\u01cb")
        buf.write("\7w\2\2\u01cb\u01cc\7g\2\2\u01ccZ\3\2\2\2\u01cd\u01ce")
        buf.write("\7H\2\2\u01ce\u01cf\7c\2\2\u01cf\u01d0\7n\2\2\u01d0\u01d1")
        buf.write("\7u\2\2\u01d1\u01d2\7g\2\2\u01d2\\\3\2\2\2\u01d3\u01d4")
        buf.write("\7C\2\2\u01d4\u01d5\7t\2\2\u01d5\u01d6\7t\2\2\u01d6\u01d7")
        buf.write("\7c\2\2\u01d7\u01d8\7{\2\2\u01d8^\3\2\2\2\u01d9\u01da")
        buf.write("\7K\2\2\u01da\u01db\7p\2\2\u01db`\3\2\2\2\u01dc\u01dd")
        buf.write("\7D\2\2\u01dd\u01de\7q\2\2\u01de\u01df\7q\2\2\u01df\u01e0")
        buf.write("\7n\2\2\u01e0\u01e1\7g\2\2\u01e1\u01e2\7c\2\2\u01e2\u01e3")
        buf.write("\7p\2\2\u01e3b\3\2\2\2\u01e4\u01e5\7T\2\2\u01e5\u01e6")
        buf.write("\7g\2\2\u01e6\u01e7\7v\2\2\u01e7\u01e8\7w\2\2\u01e8\u01e9")
        buf.write("\7t\2\2\u01e9\u01ea\7p\2\2\u01ead\3\2\2\2\u01eb\u01ec")
        buf.write("\7P\2\2\u01ec\u01ed\7w\2\2\u01ed\u01ee\7n\2\2\u01ee\u01ef")
        buf.write("\7n\2\2\u01eff\3\2\2\2\u01f0\u01f1\7E\2\2\u01f1\u01f2")
        buf.write("\7q\2\2\u01f2\u01f3\7p\2\2\u01f3\u01f4\7u\2\2\u01f4\u01f5")
        buf.write("\7v\2\2\u01f5\u01f6\7t\2\2\u01f6\u01f7\7w\2\2\u01f7\u01f8")
        buf.write("\7e\2\2\u01f8\u01f9\7v\2\2\u01f9\u01fa\7q\2\2\u01fa\u01fb")
        buf.write("\7t\2\2\u01fbh\3\2\2\2\u01fc\u01fd\7F\2\2\u01fd\u01fe")
        buf.write("\7g\2\2\u01fe\u01ff\7u\2\2\u01ff\u0200\7v\2\2\u0200\u0201")
        buf.write("\7t\2\2\u0201\u0202\7w\2\2\u0202\u0203\7e\2\2\u0203\u0204")
        buf.write("\7v\2\2\u0204\u0205\7q\2\2\u0205\u0206\7t\2\2\u0206j\3")
        buf.write("\2\2\2\u0207\u0208\7P\2\2\u0208\u0209\7g\2\2\u0209\u020a")
        buf.write("\7y\2\2\u020al\3\2\2\2\u020b\u020c\7D\2\2\u020c\u020d")
        buf.write("\7{\2\2\u020dn\3\2\2\2\u020e\u020f\7U\2\2\u020f\u0210")
        buf.write("\7g\2\2\u0210\u0211\7n\2\2\u0211\u0212\7h\2\2\u0212p\3")
        buf.write("\2\2\2\u0213\u0214\7-\2\2\u0214r\3\2\2\2\u0215\u0216\7")
        buf.write("/\2\2\u0216t\3\2\2\2\u0217\u0218\7,\2\2\u0218v\3\2\2\2")
        buf.write("\u0219\u021a\7\61\2\2\u021ax\3\2\2\2\u021b\u021c\7\'\2")
        buf.write("\2\u021cz\3\2\2\2\u021d\u021e\7#\2\2\u021e|\3\2\2\2\u021f")
        buf.write("\u0220\7(\2\2\u0220\u0221\7(\2\2\u0221~\3\2\2\2\u0222")
        buf.write("\u0223\7~\2\2\u0223\u0224\7~\2\2\u0224\u0080\3\2\2\2\u0225")
        buf.write("\u0226\7?\2\2\u0226\u0227\7?\2\2\u0227\u0082\3\2\2\2\u0228")
        buf.write("\u0229\7?\2\2\u0229\u0084\3\2\2\2\u022a\u022b\7#\2\2\u022b")
        buf.write("\u022c\7?\2\2\u022c\u0086\3\2\2\2\u022d\u022e\7@\2\2\u022e")
        buf.write("\u0088\3\2\2\2\u022f\u0230\7@\2\2\u0230\u0231\7?\2\2\u0231")
        buf.write("\u008a\3\2\2\2\u0232\u0233\7>\2\2\u0233\u008c\3\2\2\2")
        buf.write("\u0234\u0235\7>\2\2\u0235\u0236\7?\2\2\u0236\u008e\3\2")
        buf.write("\2\2\u0237\u0238\7?\2\2\u0238\u0239\7?\2\2\u0239\u023a")
        buf.write("\7\60\2\2\u023a\u0090\3\2\2\2\u023b\u023c\7-\2\2\u023c")
        buf.write("\u023d\7\60\2\2\u023d\u0092\3\2\2\2\u023e\u023f\7\60\2")
        buf.write("\2\u023f\u0094\3\2\2\2\u0240\u0241\7\60\2\2\u0241\u0242")
        buf.write("\7\60\2\2\u0242\u0096\3\2\2\2\u0243\u0244\7<\2\2\u0244")
        buf.write("\u0245\7<\2\2\u0245\u0098\3\2\2\2\u0246\u024a\t\16\2\2")
        buf.write("\u0247\u0249\t\17\2\2\u0248\u0247\3\2\2\2\u0249\u024c")
        buf.write("\3\2\2\2\u024a\u0248\3\2\2\2\u024a\u024b\3\2\2\2\u024b")
        buf.write("\u009a\3\2\2\2\u024c\u024a\3\2\2\2\u024d\u024f\5/\30\2")
        buf.write("\u024e\u0250\t\17\2\2\u024f\u024e\3\2\2\2\u0250\u0251")
        buf.write("\3\2\2\2\u0251\u024f\3\2\2\2\u0251\u0252\3\2\2\2\u0252")
        buf.write("\u009c\3\2\2\2\u0253\u0256\5\u0099M\2\u0254\u0256\5\u009b")
        buf.write("N\2\u0255\u0253\3\2\2\2\u0255\u0254\3\2\2\2\u0256\u009e")
        buf.write("\3\2\2\2\u0257\u0259\t\20\2\2\u0258\u0257\3\2\2\2\u0259")
        buf.write("\u025a\3\2\2\2\u025a\u0258\3\2\2\2\u025a\u025b\3\2\2\2")
        buf.write("\u025b\u025c\3\2\2\2\u025c\u025d\bP\13\2\u025d\u00a0\3")
        buf.write("\2\2\2\u025e\u025f\7%\2\2\u025f\u0260\7%\2\2\u0260\u0264")
        buf.write("\3\2\2\2\u0261\u0263\13\2\2\2\u0262\u0261\3\2\2\2\u0263")
        buf.write("\u0266\3\2\2\2\u0264\u0265\3\2\2\2\u0264\u0262\3\2\2\2")
        buf.write("\u0265\u0267\3\2\2\2\u0266\u0264\3\2\2\2\u0267\u0268\7")
        buf.write("%\2\2\u0268\u0269\7%\2\2\u0269\u026a\3\2\2\2\u026a\u026b")
        buf.write("\bQ\13\2\u026b\u00a2\3\2\2\2\u026c\u026d\13\2\2\2\u026d")
        buf.write("\u026e\bR\f\2\u026e\u00a4\3\2\2\2\37\2\u00c5\u00e3\u00e9")
        buf.write("\u00ef\u00f7\u00fb\u0102\u0109\u010f\u0115\u011d\u0121")
        buf.write("\u0128\u012d\u0133\u013d\u0143\u014d\u0157\u0169\u0189")
        buf.write("\u0194\u0198\u024a\u0251\u0255\u025a\u0264\r\3\n\2\3\13")
        buf.write("\3\3\f\4\3\r\5\3\16\6\3\22\7\3\23\b\3\24\t\3\25\n\b\2")
        buf.write("\2\3R\13")
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
    ID = 70
    WS = 71
    BLOCK_COMMENT = 72
    ERROR_CHAR = 73

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
            "ID", "WS", "BLOCK_COMMENT", "ERROR_CHAR" ]

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
                  "SCOPE", "NORMAL_ID", "DOLLAR_ID", "ID", "WS", "BLOCK_COMMENT", 
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
            actions[80] = self.ERROR_CHAR_action 
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
     


