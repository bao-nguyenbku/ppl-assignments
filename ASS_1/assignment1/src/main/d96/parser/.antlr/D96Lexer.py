# Generated from e:\HCMUT\PRINCIPLES_OF_PROGRAMMING_LANGUAGE\ppl-assignments\ASS_1\assignment1\src\main\d96\parser\D96.g4 by ANTLR 4.8
from antlr4 import *
from io import StringIO
from typing.io import TextIO
import sys


from lexererr import *



def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2R")
        buf.write("\u028f\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7")
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
        buf.write("L\4M\tM\4N\tN\4O\tO\4P\tP\4Q\tQ\4R\tR\4S\tS\4T\tT\4U\t")
        buf.write("U\4V\tV\4W\tW\4X\tX\4Y\tY\3\2\3\2\3\2\3\2\3\2\3\3\3\3")
        buf.write("\3\3\3\3\3\3\5\3\u00be\n\3\3\3\3\3\7\3\u00c2\n\3\f\3\16")
        buf.write("\3\u00c5\13\3\3\3\3\3\3\4\3\4\3\5\3\5\3\5\5\5\u00ce\n")
        buf.write("\5\3\5\3\5\3\5\3\6\3\6\3\6\3\7\3\7\3\7\3\7\7\7\u00da\n")
        buf.write("\7\f\7\16\7\u00dd\13\7\3\b\3\b\3\b\3\b\3\b\3\b\3\b\3\b")
        buf.write("\3\b\3\b\5\b\u00e9\n\b\3\t\3\t\3\t\3\t\3\n\3\n\3\n\3\n")
        buf.write("\3\n\3\n\3\13\3\13\3\13\3\13\3\13\3\13\3\13\3\f\3\f\5")
        buf.write("\f\u00fe\n\f\3\r\3\r\3\r\3\r\3\r\3\16\3\16\3\16\3\16\3")
        buf.write("\16\3\16\3\16\3\17\3\17\3\17\3\17\3\17\3\17\3\20\3\20")
        buf.write("\3\20\3\20\3\20\5\20\u0117\n\20\3\21\3\21\3\21\3\21\5")
        buf.write("\21\u011d\n\21\3\22\3\22\3\22\3\22\5\22\u0123\n\22\3\22")
        buf.write("\6\22\u0126\n\22\r\22\16\22\u0127\3\23\3\23\6\23\u012c")
        buf.write("\n\23\r\23\16\23\u012d\3\24\3\24\3\24\3\24\5\24\u0134")
        buf.write("\n\24\3\24\6\24\u0137\n\24\r\24\16\24\u0138\3\25\3\25")
        buf.write("\3\25\7\25\u013e\n\25\f\25\16\25\u0141\13\25\5\25\u0143")
        buf.write("\n\25\3\26\3\26\7\26\u0147\n\26\f\26\16\26\u014a\13\26")
        buf.write("\3\26\3\26\3\26\3\27\3\27\7\27\u0151\n\27\f\27\16\27\u0154")
        buf.write("\13\27\3\27\3\27\3\27\3\30\3\30\7\30\u015b\n\30\f\30\16")
        buf.write("\30\u015e\13\30\3\30\3\30\3\30\3\31\3\31\3\31\3\31\3\31")
        buf.write("\5\31\u0168\n\31\3\32\3\32\3\32\3\33\3\33\3\33\3\34\3")
        buf.write("\34\5\34\u0172\n\34\3\34\3\34\7\34\u0176\n\34\f\34\16")
        buf.write("\34\u0179\13\34\3\35\3\35\3\35\3\35\5\35\u017f\n\35\3")
        buf.write("\36\3\36\3\36\3\36\3\37\3\37\3\37\3\37\3 \3 \3!\3!\3\"")
        buf.write("\3\"\3#\3#\3$\3$\3%\3%\3&\3&\3\'\3\'\3(\3(\3)\3)\3*\3")
        buf.write("*\3*\3+\3+\5+\u01a2\n+\3+\3+\3,\3,\3-\3-\3-\7-\u01ab\n")
        buf.write("-\f-\16-\u01ae\13-\5-\u01b0\n-\3.\3.\3/\3/\3/\3/\3/\3")
        buf.write("/\3\60\3\60\3\60\3\60\3\60\3\60\3\60\3\60\3\60\3\61\3")
        buf.write("\61\3\61\3\62\3\62\3\62\3\62\3\62\3\62\3\62\3\63\3\63")
        buf.write("\3\63\3\63\3\63\3\64\3\64\3\64\3\64\3\64\3\64\3\64\3\64")
        buf.write("\3\65\3\65\3\65\3\65\3\65\3\66\3\66\3\66\3\66\3\66\3\66")
        buf.write("\3\67\3\67\3\67\3\67\3\67\3\67\38\38\38\39\39\39\39\3")
        buf.write("9\39\39\39\3:\3:\3:\3:\3:\3:\3:\3;\3;\3;\3;\3;\3<\3<\3")
        buf.write("<\3<\3<\3<\3<\3<\3<\3<\3<\3<\3=\3=\3=\3=\3=\3=\3=\3=\3")
        buf.write("=\3=\3=\3>\3>\3>\3>\3?\3?\3?\3@\3@\3@\3@\3@\3A\3A\3B\3")
        buf.write("B\3C\3C\3D\3D\3E\3E\3F\3F\3G\3G\3G\3H\3H\3H\3I\3I\3I\3")
        buf.write("J\3J\3K\3K\3K\3L\3L\3M\3M\3M\3N\3N\3O\3O\3O\3P\3P\3P\3")
        buf.write("P\3Q\3Q\3Q\3R\3R\3S\3S\3S\3T\3T\7T\u0257\nT\fT\16T\u025a")
        buf.write("\13T\3T\3T\6T\u025e\nT\rT\16T\u025f\5T\u0262\nT\3U\3U")
        buf.write("\3U\3U\7U\u0268\nU\fU\16U\u026b\13U\3V\6V\u026e\nV\rV")
        buf.write("\16V\u026f\3V\3V\3W\3W\3W\3W\7W\u0278\nW\fW\16W\u027b")
        buf.write("\13W\3W\3W\3W\3W\3W\3X\3X\3X\3X\7X\u0286\nX\fX\16X\u0289")
        buf.write("\13X\3X\3X\3Y\3Y\3Y\4\u0279\u0287\2Z\3\3\5\4\7\5\t\6\13")
        buf.write("\7\r\b\17\t\21\n\23\13\25\f\27\r\31\16\33\17\35\20\37")
        buf.write("\21!\22#\23%\24\'\25)\26+\27-\30/\31\61\2\63\2\65\2\67")
        buf.write("\329\33;\34=\35?\2A\36C\37E G!I\"K#M$O%Q&S\'U\2W\2Y\2")
        buf.write("[\2](_)a*c+e,g-i.k/m\60o\61q\62s\63u\64w\65y\66{\67}8")
        buf.write("\1779\u0081:\u0083;\u0085<\u0087=\u0089>\u008b?\u008d")
        buf.write("@\u008fA\u0091B\u0093C\u0095D\u0097E\u0099F\u009bG\u009d")
        buf.write("H\u009fI\u00a1J\u00a3K\u00a5L\u00a7M\u00a9N\u00abO\u00ad")
        buf.write("P\u00afQ\u00b1R\3\2\17\5\2\62;CHch\3\2\62;\3\2\62\63\3")
        buf.write("\2\63;\4\2\62;aa\t\2$$^^ddhhppttvv\4\2$$^^\n\2$$))^^d")
        buf.write("dhhppttvv\4\2GGgg\4\2--//\5\2C\\aac|\6\2\62;C\\aac|\5")
        buf.write("\2\13\f\17\17\"\"\2\u02af\2\3\3\2\2\2\2\5\3\2\2\2\2\7")
        buf.write("\3\2\2\2\2\t\3\2\2\2\2\13\3\2\2\2\2\r\3\2\2\2\2\17\3\2")
        buf.write("\2\2\2\21\3\2\2\2\2\23\3\2\2\2\2\25\3\2\2\2\2\27\3\2\2")
        buf.write("\2\2\31\3\2\2\2\2\33\3\2\2\2\2\35\3\2\2\2\2\37\3\2\2\2")
        buf.write("\2!\3\2\2\2\2#\3\2\2\2\2%\3\2\2\2\2\'\3\2\2\2\2)\3\2\2")
        buf.write("\2\2+\3\2\2\2\2-\3\2\2\2\2/\3\2\2\2\2\67\3\2\2\2\29\3")
        buf.write("\2\2\2\2;\3\2\2\2\2=\3\2\2\2\2A\3\2\2\2\2C\3\2\2\2\2E")
        buf.write("\3\2\2\2\2G\3\2\2\2\2I\3\2\2\2\2K\3\2\2\2\2M\3\2\2\2\2")
        buf.write("O\3\2\2\2\2Q\3\2\2\2\2S\3\2\2\2\2]\3\2\2\2\2_\3\2\2\2")
        buf.write("\2a\3\2\2\2\2c\3\2\2\2\2e\3\2\2\2\2g\3\2\2\2\2i\3\2\2")
        buf.write("\2\2k\3\2\2\2\2m\3\2\2\2\2o\3\2\2\2\2q\3\2\2\2\2s\3\2")
        buf.write("\2\2\2u\3\2\2\2\2w\3\2\2\2\2y\3\2\2\2\2{\3\2\2\2\2}\3")
        buf.write("\2\2\2\2\177\3\2\2\2\2\u0081\3\2\2\2\2\u0083\3\2\2\2\2")
        buf.write("\u0085\3\2\2\2\2\u0087\3\2\2\2\2\u0089\3\2\2\2\2\u008b")
        buf.write("\3\2\2\2\2\u008d\3\2\2\2\2\u008f\3\2\2\2\2\u0091\3\2\2")
        buf.write("\2\2\u0093\3\2\2\2\2\u0095\3\2\2\2\2\u0097\3\2\2\2\2\u0099")
        buf.write("\3\2\2\2\2\u009b\3\2\2\2\2\u009d\3\2\2\2\2\u009f\3\2\2")
        buf.write("\2\2\u00a1\3\2\2\2\2\u00a3\3\2\2\2\2\u00a5\3\2\2\2\2\u00a7")
        buf.write("\3\2\2\2\2\u00a9\3\2\2\2\2\u00ab\3\2\2\2\2\u00ad\3\2\2")
        buf.write("\2\2\u00af\3\2\2\2\2\u00b1\3\2\2\2\3\u00b3\3\2\2\2\5\u00b8")
        buf.write("\3\2\2\2\7\u00c8\3\2\2\2\t\u00ca\3\2\2\2\13\u00d2\3\2")
        buf.write("\2\2\r\u00d5\3\2\2\2\17\u00e8\3\2\2\2\21\u00ea\3\2\2\2")
        buf.write("\23\u00ee\3\2\2\2\25\u00f4\3\2\2\2\27\u00fd\3\2\2\2\31")
        buf.write("\u00ff\3\2\2\2\33\u0104\3\2\2\2\35\u010b\3\2\2\2\37\u0116")
        buf.write("\3\2\2\2!\u011c\3\2\2\2#\u0122\3\2\2\2%\u0129\3\2\2\2")
        buf.write("\'\u0133\3\2\2\2)\u0142\3\2\2\2+\u0144\3\2\2\2-\u014e")
        buf.write("\3\2\2\2/\u0158\3\2\2\2\61\u0167\3\2\2\2\63\u0169\3\2")
        buf.write("\2\2\65\u016c\3\2\2\2\67\u016f\3\2\2\29\u017e\3\2\2\2")
        buf.write(";\u0180\3\2\2\2=\u0184\3\2\2\2?\u0188\3\2\2\2A\u018a\3")
        buf.write("\2\2\2C\u018c\3\2\2\2E\u018e\3\2\2\2G\u0190\3\2\2\2I\u0192")
        buf.write("\3\2\2\2K\u0194\3\2\2\2M\u0196\3\2\2\2O\u0198\3\2\2\2")
        buf.write("Q\u019a\3\2\2\2S\u019c\3\2\2\2U\u019f\3\2\2\2W\u01a5\3")
        buf.write("\2\2\2Y\u01af\3\2\2\2[\u01b1\3\2\2\2]\u01b3\3\2\2\2_\u01b9")
        buf.write("\3\2\2\2a\u01c2\3\2\2\2c\u01c5\3\2\2\2e\u01cc\3\2\2\2")
        buf.write("g\u01d1\3\2\2\2i\u01d9\3\2\2\2k\u01de\3\2\2\2m\u01e4\3")
        buf.write("\2\2\2o\u01ea\3\2\2\2q\u01ed\3\2\2\2s\u01f5\3\2\2\2u\u01fc")
        buf.write("\3\2\2\2w\u0201\3\2\2\2y\u020d\3\2\2\2{\u0218\3\2\2\2")
        buf.write("}\u021c\3\2\2\2\177\u021f\3\2\2\2\u0081\u0224\3\2\2\2")
        buf.write("\u0083\u0226\3\2\2\2\u0085\u0228\3\2\2\2\u0087\u022a\3")
        buf.write("\2\2\2\u0089\u022c\3\2\2\2\u008b\u022e\3\2\2\2\u008d\u0230")
        buf.write("\3\2\2\2\u008f\u0233\3\2\2\2\u0091\u0236\3\2\2\2\u0093")
        buf.write("\u0239\3\2\2\2\u0095\u023b\3\2\2\2\u0097\u023e\3\2\2\2")
        buf.write("\u0099\u0240\3\2\2\2\u009b\u0243\3\2\2\2\u009d\u0245\3")
        buf.write("\2\2\2\u009f\u0248\3\2\2\2\u00a1\u024c\3\2\2\2\u00a3\u024f")
        buf.write("\3\2\2\2\u00a5\u0251\3\2\2\2\u00a7\u0261\3\2\2\2\u00a9")
        buf.write("\u0263\3\2\2\2\u00ab\u026d\3\2\2\2\u00ad\u0273\3\2\2\2")
        buf.write("\u00af\u0281\3\2\2\2\u00b1\u028c\3\2\2\2\u00b3\u00b4\7")
        buf.write("o\2\2\u00b4\u00b5\7c\2\2\u00b5\u00b6\7k\2\2\u00b6\u00b7")
        buf.write("\7p\2\2\u00b7\4\3\2\2\2\u00b8\u00b9\5\35\17\2\u00b9\u00bd")
        buf.write("\5\u00a7T\2\u00ba\u00bb\5Q)\2\u00bb\u00bc\5\u00a7T\2\u00bc")
        buf.write("\u00be\3\2\2\2\u00bd\u00ba\3\2\2\2\u00bd\u00be\3\2\2\2")
        buf.write("\u00be\u00bf\3\2\2\2\u00bf\u00c3\5E#\2\u00c0\u00c2\5\7")
        buf.write("\4\2\u00c1\u00c0\3\2\2\2\u00c2\u00c5\3\2\2\2\u00c3\u00c1")
        buf.write("\3\2\2\2\u00c3\u00c4\3\2\2\2\u00c4\u00c6\3\2\2\2\u00c5")
        buf.write("\u00c3\3\2\2\2\u00c6\u00c7\5G$\2\u00c7\6\3\2\2\2\u00c8")
        buf.write("\u00c9\5\t\5\2\u00c9\b\3\2\2\2\u00ca\u00cb\5\u00a7T\2")
        buf.write("\u00cb\u00cd\5A!\2\u00cc\u00ce\5\r\7\2\u00cd\u00cc\3\2")
        buf.write("\2\2\u00cd\u00ce\3\2\2\2\u00ce\u00cf\3\2\2\2\u00cf\u00d0")
        buf.write("\5C\"\2\u00d0\u00d1\5\13\6\2\u00d1\n\3\2\2\2\u00d2\u00d3")
        buf.write("\5E#\2\u00d3\u00d4\5G$\2\u00d4\f\3\2\2\2\u00d5\u00db\5")
        buf.write("\17\b\2\u00d6\u00d7\5M\'\2\u00d7\u00d8\5\17\b\2\u00d8")
        buf.write("\u00da\3\2\2\2\u00d9\u00d6\3\2\2\2\u00da\u00dd\3\2\2\2")
        buf.write("\u00db\u00d9\3\2\2\2\u00db\u00dc\3\2\2\2\u00dc\16\3\2")
        buf.write("\2\2\u00dd\u00db\3\2\2\2\u00de\u00df\5\u00a7T\2\u00df")
        buf.write("\u00e0\5Q)\2\u00e0\u00e1\5\37\20\2\u00e1\u00e9\3\2\2\2")
        buf.write("\u00e2\u00e3\5\u00a7T\2\u00e3\u00e4\5Q)\2\u00e4\u00e5")
        buf.write("\5\37\20\2\u00e5\u00e6\5O(\2\u00e6\u00e7\5\17\b\2\u00e7")
        buf.write("\u00e9\3\2\2\2\u00e8\u00de\3\2\2\2\u00e8\u00e2\3\2\2\2")
        buf.write("\u00e9\20\3\2\2\2\u00ea\u00eb\7K\2\2\u00eb\u00ec\7p\2")
        buf.write("\2\u00ec\u00ed\7v\2\2\u00ed\22\3\2\2\2\u00ee\u00ef\7H")
        buf.write("\2\2\u00ef\u00f0\7n\2\2\u00f0\u00f1\7q\2\2\u00f1\u00f2")
        buf.write("\7c\2\2\u00f2\u00f3\7v\2\2\u00f3\24\3\2\2\2\u00f4\u00f5")
        buf.write("\7U\2\2\u00f5\u00f6\7v\2\2\u00f6\u00f7\7t\2\2\u00f7\u00f8")
        buf.write("\7k\2\2\u00f8\u00f9\7p\2\2\u00f9\u00fa\7i\2\2\u00fa\26")
        buf.write("\3\2\2\2\u00fb\u00fe\5i\65\2\u00fc\u00fe\5k\66\2\u00fd")
        buf.write("\u00fb\3\2\2\2\u00fd\u00fc\3\2\2\2\u00fe\30\3\2\2\2\u00ff")
        buf.write("\u0100\7X\2\2\u0100\u0101\7q\2\2\u0101\u0102\7k\2\2\u0102")
        buf.write("\u0103\7f\2\2\u0103\32\3\2\2\2\u0104\u0105\5m\67\2\u0105")
        buf.write("\u0106\5I%\2\u0106\u0107\5\37\20\2\u0107\u0108\5O(\2\u0108")
        buf.write("\u0109\5!\21\2\u0109\u010a\5K&\2\u010a\34\3\2\2\2\u010b")
        buf.write("\u010c\7E\2\2\u010c\u010d\7n\2\2\u010d\u010e\7c\2\2\u010e")
        buf.write("\u010f\7u\2\2\u010f\u0110\7u\2\2\u0110\36\3\2\2\2\u0111")
        buf.write("\u0117\5\27\f\2\u0112\u0117\5\21\t\2\u0113\u0117\5\23")
        buf.write("\n\2\u0114\u0117\5\25\13\2\u0115\u0117\5\35\17\2\u0116")
        buf.write("\u0111\3\2\2\2\u0116\u0112\3\2\2\2\u0116\u0113\3\2\2\2")
        buf.write("\u0116\u0114\3\2\2\2\u0116\u0115\3\2\2\2\u0117 \3\2\2")
        buf.write("\2\u0118\u011d\5#\22\2\u0119\u011d\5%\23\2\u011a\u011d")
        buf.write("\5\'\24\2\u011b\u011d\5)\25\2\u011c\u0118\3\2\2\2\u011c")
        buf.write("\u0119\3\2\2\2\u011c\u011a\3\2\2\2\u011c\u011b\3\2\2\2")
        buf.write("\u011d\"\3\2\2\2\u011e\u011f\7\62\2\2\u011f\u0123\7z\2")
        buf.write("\2\u0120\u0121\7\62\2\2\u0121\u0123\7Z\2\2\u0122\u011e")
        buf.write("\3\2\2\2\u0122\u0120\3\2\2\2\u0123\u0125\3\2\2\2\u0124")
        buf.write("\u0126\t\2\2\2\u0125\u0124\3\2\2\2\u0126\u0127\3\2\2\2")
        buf.write("\u0127\u0125\3\2\2\2\u0127\u0128\3\2\2\2\u0128$\3\2\2")
        buf.write("\2\u0129\u012b\7\62\2\2\u012a\u012c\t\3\2\2\u012b\u012a")
        buf.write("\3\2\2\2\u012c\u012d\3\2\2\2\u012d\u012b\3\2\2\2\u012d")
        buf.write("\u012e\3\2\2\2\u012e&\3\2\2\2\u012f\u0130\7\62\2\2\u0130")
        buf.write("\u0134\7d\2\2\u0131\u0132\7\62\2\2\u0132\u0134\7D\2\2")
        buf.write("\u0133\u012f\3\2\2\2\u0133\u0131\3\2\2\2\u0134\u0136\3")
        buf.write("\2\2\2\u0135\u0137\t\4\2\2\u0136\u0135\3\2\2\2\u0137\u0138")
        buf.write("\3\2\2\2\u0138\u0136\3\2\2\2\u0138\u0139\3\2\2\2\u0139")
        buf.write("(\3\2\2\2\u013a\u0143\t\3\2\2\u013b\u013f\t\5\2\2\u013c")
        buf.write("\u013e\t\6\2\2\u013d\u013c\3\2\2\2\u013e\u0141\3\2\2\2")
        buf.write("\u013f\u013d\3\2\2\2\u013f\u0140\3\2\2\2\u0140\u0143\3")
        buf.write("\2\2\2\u0141\u013f\3\2\2\2\u0142\u013a\3\2\2\2\u0142\u013b")
        buf.write("\3\2\2\2\u0143*\3\2\2\2\u0144\u0148\7$\2\2\u0145\u0147")
        buf.write("\5\61\31\2\u0146\u0145\3\2\2\2\u0147\u014a\3\2\2\2\u0148")
        buf.write("\u0146\3\2\2\2\u0148\u0149\3\2\2\2\u0149\u014b\3\2\2\2")
        buf.write("\u014a\u0148\3\2\2\2\u014b\u014c\7$\2\2\u014c\u014d\b")
        buf.write("\26\2\2\u014d,\3\2\2\2\u014e\u0152\7$\2\2\u014f\u0151")
        buf.write("\5\61\31\2\u0150\u014f\3\2\2\2\u0151\u0154\3\2\2\2\u0152")
        buf.write("\u0150\3\2\2\2\u0152\u0153\3\2\2\2\u0153\u0155\3\2\2\2")
        buf.write("\u0154\u0152\3\2\2\2\u0155\u0156\5\65\33\2\u0156\u0157")
        buf.write("\b\27\3\2\u0157.\3\2\2\2\u0158\u015c\7$\2\2\u0159\u015b")
        buf.write("\5\61\31\2\u015a\u0159\3\2\2\2\u015b\u015e\3\2\2\2\u015c")
        buf.write("\u015a\3\2\2\2\u015c\u015d\3\2\2\2\u015d\u015f\3\2\2\2")
        buf.write("\u015e\u015c\3\2\2\2\u015f\u0160\7\2\2\3\u0160\u0161\b")
        buf.write("\30\4\2\u0161\60\3\2\2\2\u0162\u0163\7^\2\2\u0163\u0168")
        buf.write("\t\7\2\2\u0164\u0168\n\b\2\2\u0165\u0166\7)\2\2\u0166")
        buf.write("\u0168\7$\2\2\u0167\u0162\3\2\2\2\u0167\u0164\3\2\2\2")
        buf.write("\u0167\u0165\3\2\2\2\u0168\62\3\2\2\2\u0169\u016a\7^\2")
        buf.write("\2\u016a\u016b\t\t\2\2\u016b\64\3\2\2\2\u016c\u016d\7")
        buf.write("^\2\2\u016d\u016e\n\7\2\2\u016e\66\3\2\2\2\u016f\u0171")
        buf.write("\5Y-\2\u0170\u0172\5\u00a3R\2\u0171\u0170\3\2\2\2\u0171")
        buf.write("\u0172\3\2\2\2\u0172\u0177\3\2\2\2\u0173\u0176\5Y-\2\u0174")
        buf.write("\u0176\5U+\2\u0175\u0173\3\2\2\2\u0175\u0174\3\2\2\2\u0176")
        buf.write("\u0179\3\2\2\2\u0177\u0175\3\2\2\2\u0177\u0178\3\2\2\2")
        buf.write("\u01788\3\2\2\2\u0179\u0177\3\2\2\2\u017a\u017f\5!\21")
        buf.write("\2\u017b\u017f\5\27\f\2\u017c\u017f\5\67\34\2\u017d\u017f")
        buf.write("\5+\26\2\u017e\u017a\3\2\2\2\u017e\u017b\3\2\2\2\u017e")
        buf.write("\u017c\3\2\2\2\u017e\u017d\3\2\2\2\u017f:\3\2\2\2\u0180")
        buf.write("\u0181\7X\2\2\u0181\u0182\7c\2\2\u0182\u0183\7n\2\2\u0183")
        buf.write("<\3\2\2\2\u0184\u0185\7X\2\2\u0185\u0186\7c\2\2\u0186")
        buf.write("\u0187\7t\2\2\u0187>\3\2\2\2\u0188\u0189\7&\2\2\u0189")
        buf.write("@\3\2\2\2\u018a\u018b\7*\2\2\u018bB\3\2\2\2\u018c\u018d")
        buf.write("\7+\2\2\u018dD\3\2\2\2\u018e\u018f\7}\2\2\u018fF\3\2\2")
        buf.write("\2\u0190\u0191\7\177\2\2\u0191H\3\2\2\2\u0192\u0193\7")
        buf.write("]\2\2\u0193J\3\2\2\2\u0194\u0195\7_\2\2\u0195L\3\2\2\2")
        buf.write("\u0196\u0197\7=\2\2\u0197N\3\2\2\2\u0198\u0199\7.\2\2")
        buf.write("\u0199P\3\2\2\2\u019a\u019b\7<\2\2\u019bR\3\2\2\2\u019c")
        buf.write("\u019d\7\60\2\2\u019d\u019e\7\60\2\2\u019eT\3\2\2\2\u019f")
        buf.write("\u01a1\t\n\2\2\u01a0\u01a2\5[.\2\u01a1\u01a0\3\2\2\2\u01a1")
        buf.write("\u01a2\3\2\2\2\u01a2\u01a3\3\2\2\2\u01a3\u01a4\5)\25\2")
        buf.write("\u01a4V\3\2\2\2\u01a5\u01a6\t\3\2\2\u01a6X\3\2\2\2\u01a7")
        buf.write("\u01b0\t\3\2\2\u01a8\u01ac\t\5\2\2\u01a9\u01ab\t\6\2\2")
        buf.write("\u01aa\u01a9\3\2\2\2\u01ab\u01ae\3\2\2\2\u01ac\u01aa\3")
        buf.write("\2\2\2\u01ac\u01ad\3\2\2\2\u01ad\u01b0\3\2\2\2\u01ae\u01ac")
        buf.write("\3\2\2\2\u01af\u01a7\3\2\2\2\u01af\u01a8\3\2\2\2\u01b0")
        buf.write("Z\3\2\2\2\u01b1\u01b2\t\13\2\2\u01b2\\\3\2\2\2\u01b3\u01b4")
        buf.write("\7D\2\2\u01b4\u01b5\7t\2\2\u01b5\u01b6\7g\2\2\u01b6\u01b7")
        buf.write("\7c\2\2\u01b7\u01b8\7m\2\2\u01b8^\3\2\2\2\u01b9\u01ba")
        buf.write("\7E\2\2\u01ba\u01bb\7q\2\2\u01bb\u01bc\7p\2\2\u01bc\u01bd")
        buf.write("\7v\2\2\u01bd\u01be\7k\2\2\u01be\u01bf\7p\2\2\u01bf\u01c0")
        buf.write("\7w\2\2\u01c0\u01c1\7g\2\2\u01c1`\3\2\2\2\u01c2\u01c3")
        buf.write("\7K\2\2\u01c3\u01c4\7h\2\2\u01c4b\3\2\2\2\u01c5\u01c6")
        buf.write("\7G\2\2\u01c6\u01c7\7n\2\2\u01c7\u01c8\7u\2\2\u01c8\u01c9")
        buf.write("\7g\2\2\u01c9\u01ca\7k\2\2\u01ca\u01cb\7h\2\2\u01cbd\3")
        buf.write("\2\2\2\u01cc\u01cd\7G\2\2\u01cd\u01ce\7n\2\2\u01ce\u01cf")
        buf.write("\7u\2\2\u01cf\u01d0\7g\2\2\u01d0f\3\2\2\2\u01d1\u01d2")
        buf.write("\7H\2\2\u01d2\u01d3\7q\2\2\u01d3\u01d4\7t\2\2\u01d4\u01d5")
        buf.write("\7g\2\2\u01d5\u01d6\7c\2\2\u01d6\u01d7\7e\2\2\u01d7\u01d8")
        buf.write("\7j\2\2\u01d8h\3\2\2\2\u01d9\u01da\7V\2\2\u01da\u01db")
        buf.write("\7t\2\2\u01db\u01dc\7w\2\2\u01dc\u01dd\7g\2\2\u01ddj\3")
        buf.write("\2\2\2\u01de\u01df\7H\2\2\u01df\u01e0\7c\2\2\u01e0\u01e1")
        buf.write("\7n\2\2\u01e1\u01e2\7u\2\2\u01e2\u01e3\7g\2\2\u01e3l\3")
        buf.write("\2\2\2\u01e4\u01e5\7C\2\2\u01e5\u01e6\7t\2\2\u01e6\u01e7")
        buf.write("\7t\2\2\u01e7\u01e8\7c\2\2\u01e8\u01e9\7{\2\2\u01e9n\3")
        buf.write("\2\2\2\u01ea\u01eb\7K\2\2\u01eb\u01ec\7p\2\2\u01ecp\3")
        buf.write("\2\2\2\u01ed\u01ee\7D\2\2\u01ee\u01ef\7q\2\2\u01ef\u01f0")
        buf.write("\7q\2\2\u01f0\u01f1\7n\2\2\u01f1\u01f2\7g\2\2\u01f2\u01f3")
        buf.write("\7c\2\2\u01f3\u01f4\7p\2\2\u01f4r\3\2\2\2\u01f5\u01f6")
        buf.write("\7T\2\2\u01f6\u01f7\7g\2\2\u01f7\u01f8\7v\2\2\u01f8\u01f9")
        buf.write("\7w\2\2\u01f9\u01fa\7t\2\2\u01fa\u01fb\7p\2\2\u01fbt\3")
        buf.write("\2\2\2\u01fc\u01fd\7P\2\2\u01fd\u01fe\7w\2\2\u01fe\u01ff")
        buf.write("\7n\2\2\u01ff\u0200\7n\2\2\u0200v\3\2\2\2\u0201\u0202")
        buf.write("\7E\2\2\u0202\u0203\7q\2\2\u0203\u0204\7p\2\2\u0204\u0205")
        buf.write("\7u\2\2\u0205\u0206\7v\2\2\u0206\u0207\7t\2\2\u0207\u0208")
        buf.write("\7w\2\2\u0208\u0209\7e\2\2\u0209\u020a\7v\2\2\u020a\u020b")
        buf.write("\7q\2\2\u020b\u020c\7t\2\2\u020cx\3\2\2\2\u020d\u020e")
        buf.write("\7F\2\2\u020e\u020f\7g\2\2\u020f\u0210\7u\2\2\u0210\u0211")
        buf.write("\7v\2\2\u0211\u0212\7t\2\2\u0212\u0213\7w\2\2\u0213\u0214")
        buf.write("\7e\2\2\u0214\u0215\7v\2\2\u0215\u0216\7q\2\2\u0216\u0217")
        buf.write("\7t\2\2\u0217z\3\2\2\2\u0218\u0219\7P\2\2\u0219\u021a")
        buf.write("\7g\2\2\u021a\u021b\7y\2\2\u021b|\3\2\2\2\u021c\u021d")
        buf.write("\7D\2\2\u021d\u021e\7{\2\2\u021e~\3\2\2\2\u021f\u0220")
        buf.write("\7U\2\2\u0220\u0221\7g\2\2\u0221\u0222\7n\2\2\u0222\u0223")
        buf.write("\7h\2\2\u0223\u0080\3\2\2\2\u0224\u0225\7-\2\2\u0225\u0082")
        buf.write("\3\2\2\2\u0226\u0227\7/\2\2\u0227\u0084\3\2\2\2\u0228")
        buf.write("\u0229\7,\2\2\u0229\u0086\3\2\2\2\u022a\u022b\7\61\2\2")
        buf.write("\u022b\u0088\3\2\2\2\u022c\u022d\7\'\2\2\u022d\u008a\3")
        buf.write("\2\2\2\u022e\u022f\7#\2\2\u022f\u008c\3\2\2\2\u0230\u0231")
        buf.write("\7(\2\2\u0231\u0232\7(\2\2\u0232\u008e\3\2\2\2\u0233\u0234")
        buf.write("\7~\2\2\u0234\u0235\7~\2\2\u0235\u0090\3\2\2\2\u0236\u0237")
        buf.write("\7?\2\2\u0237\u0238\7?\2\2\u0238\u0092\3\2\2\2\u0239\u023a")
        buf.write("\7?\2\2\u023a\u0094\3\2\2\2\u023b\u023c\7#\2\2\u023c\u023d")
        buf.write("\7?\2\2\u023d\u0096\3\2\2\2\u023e\u023f\7@\2\2\u023f\u0098")
        buf.write("\3\2\2\2\u0240\u0241\7@\2\2\u0241\u0242\7?\2\2\u0242\u009a")
        buf.write("\3\2\2\2\u0243\u0244\7>\2\2\u0244\u009c\3\2\2\2\u0245")
        buf.write("\u0246\7>\2\2\u0246\u0247\7?\2\2\u0247\u009e\3\2\2\2\u0248")
        buf.write("\u0249\7?\2\2\u0249\u024a\7?\2\2\u024a\u024b\7\60\2\2")
        buf.write("\u024b\u00a0\3\2\2\2\u024c\u024d\7-\2\2\u024d\u024e\7")
        buf.write("\60\2\2\u024e\u00a2\3\2\2\2\u024f\u0250\7\60\2\2\u0250")
        buf.write("\u00a4\3\2\2\2\u0251\u0252\7<\2\2\u0252\u0253\7<\2\2\u0253")
        buf.write("\u00a6\3\2\2\2\u0254\u0258\t\f\2\2\u0255\u0257\t\r\2\2")
        buf.write("\u0256\u0255\3\2\2\2\u0257\u025a\3\2\2\2\u0258\u0256\3")
        buf.write("\2\2\2\u0258\u0259\3\2\2\2\u0259\u0262\3\2\2\2\u025a\u0258")
        buf.write("\3\2\2\2\u025b\u025d\5? \2\u025c\u025e\t\r\2\2\u025d\u025c")
        buf.write("\3\2\2\2\u025e\u025f\3\2\2\2\u025f\u025d\3\2\2\2\u025f")
        buf.write("\u0260\3\2\2\2\u0260\u0262\3\2\2\2\u0261\u0254\3\2\2\2")
        buf.write("\u0261\u025b\3\2\2\2\u0262\u00a8\3\2\2\2\u0263\u0269\5")
        buf.write("\u00a7T\2\u0264\u0265\5O(\2\u0265\u0266\5\u00a7T\2\u0266")
        buf.write("\u0268\3\2\2\2\u0267\u0264\3\2\2\2\u0268\u026b\3\2\2\2")
        buf.write("\u0269\u0267\3\2\2\2\u0269\u026a\3\2\2\2\u026a\u00aa\3")
        buf.write("\2\2\2\u026b\u0269\3\2\2\2\u026c\u026e\t\16\2\2\u026d")
        buf.write("\u026c\3\2\2\2\u026e\u026f\3\2\2\2\u026f\u026d\3\2\2\2")
        buf.write("\u026f\u0270\3\2\2\2\u0270\u0271\3\2\2\2\u0271\u0272\b")
        buf.write("V\5\2\u0272\u00ac\3\2\2\2\u0273\u0274\7%\2\2\u0274\u0275")
        buf.write("\7%\2\2\u0275\u0279\3\2\2\2\u0276\u0278\13\2\2\2\u0277")
        buf.write("\u0276\3\2\2\2\u0278\u027b\3\2\2\2\u0279\u027a\3\2\2\2")
        buf.write("\u0279\u0277\3\2\2\2\u027a\u027c\3\2\2\2\u027b\u0279\3")
        buf.write("\2\2\2\u027c\u027d\7%\2\2\u027d\u027e\7%\2\2\u027e\u027f")
        buf.write("\3\2\2\2\u027f\u0280\bW\5\2\u0280\u00ae\3\2\2\2\u0281")
        buf.write("\u0282\7%\2\2\u0282\u0283\7%\2\2\u0283\u0287\3\2\2\2\u0284")
        buf.write("\u0286\13\2\2\2\u0285\u0284\3\2\2\2\u0286\u0289\3\2\2")
        buf.write("\2\u0287\u0288\3\2\2\2\u0287\u0285\3\2\2\2\u0288\u028a")
        buf.write("\3\2\2\2\u0289\u0287\3\2\2\2\u028a\u028b\bX\6\2\u028b")
        buf.write("\u00b0\3\2\2\2\u028c\u028d\13\2\2\2\u028d\u028e\bY\7\2")
        buf.write("\u028e\u00b2\3\2\2\2$\2\u00bd\u00c3\u00cd\u00db\u00e8")
        buf.write("\u00fd\u0116\u011c\u0122\u0127\u012d\u0133\u0138\u013f")
        buf.write("\u0142\u0148\u0152\u015c\u0167\u0171\u0175\u0177\u017e")
        buf.write("\u01a1\u01ac\u01af\u0258\u025f\u0261\u0269\u026f\u0279")
        buf.write("\u0287\b\3\26\2\3\27\3\3\30\4\b\2\2\3X\5\3Y\6")
        return buf.getvalue()


class D96Lexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    T__0 = 1
    CLASS_DECLARE = 2
    MEMBER = 3
    METHODS = 4
    BLOCK_STATEMENT = 5
    LIST_PARAM = 6
    LIST_METHOD = 7
    INT_TYPE = 8
    FLOAT_TYPE = 9
    STRING = 10
    BOOL_TYPE = 11
    VOID_TYPE = 12
    ARRAY_TYPE = 13
    CLASS = 14
    PRIMITIVE_TYPE = 15
    INTEGER_LITERAL = 16
    HEX_TYPE = 17
    OCT_TYPE = 18
    BIN_TYPE = 19
    DEC_TYPE = 20
    STRING_LITERAL = 21
    ILLEGAL_ESCAPE = 22
    UNCLOSE_STRING = 23
    REAL_LITERAL = 24
    LITERAL = 25
    VAL = 26
    VAR = 27
    LP = 28
    RP = 29
    LCB = 30
    RCB = 31
    LSB = 32
    RSB = 33
    SEMI = 34
    COMMA = 35
    COLON = 36
    DOTDOT = 37
    BREAK = 38
    CONTINUE = 39
    IF = 40
    ELSEIF = 41
    ELSE = 42
    FOREACH = 43
    TRUE = 44
    FALSE = 45
    ARRAY = 46
    IN = 47
    BOOLEAN = 48
    RETURN = 49
    NULL = 50
    CONSTRUCTOR = 51
    DESTRUCTOR = 52
    NEW = 53
    BY = 54
    SELF = 55
    ADD = 56
    SUB = 57
    MUL = 58
    DIV = 59
    MOD = 60
    NOT = 61
    AND = 62
    OR = 63
    EQUAL = 64
    ASSIGN = 65
    NOTEQUAL = 66
    GT = 67
    GTE = 68
    LT = 69
    LTE = 70
    EQUAL_STR = 71
    ADD_STR = 72
    DOT = 73
    SCOPE = 74
    ID = 75
    ID_LIST = 76
    WS = 77
    BLOCK_COMMENT = 78
    UNTERMINATED_COMMENT = 79
    ERROR_CHAR = 80

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'main'", "'Int'", "'Float'", "'String'", "'Void'", "'Class'", 
            "'Val'", "'Var'", "'('", "')'", "'{'", "'}'", "'['", "']'", 
            "';'", "','", "':'", "'..'", "'Break'", "'Continue'", "'If'", 
            "'Elseif'", "'Else'", "'Foreach'", "'True'", "'False'", "'Array'", 
            "'In'", "'Boolean'", "'Return'", "'Null'", "'Constructor'", 
            "'Destructor'", "'New'", "'By'", "'Self'", "'+'", "'-'", "'*'", 
            "'/'", "'%'", "'!'", "'&&'", "'||'", "'=='", "'='", "'!='", 
            "'>'", "'>='", "'<'", "'<='", "'==.'", "'+.'", "'.'", "'::'" ]

    symbolicNames = [ "<INVALID>",
            "CLASS_DECLARE", "MEMBER", "METHODS", "BLOCK_STATEMENT", "LIST_PARAM", 
            "LIST_METHOD", "INT_TYPE", "FLOAT_TYPE", "STRING", "BOOL_TYPE", 
            "VOID_TYPE", "ARRAY_TYPE", "CLASS", "PRIMITIVE_TYPE", "INTEGER_LITERAL", 
            "HEX_TYPE", "OCT_TYPE", "BIN_TYPE", "DEC_TYPE", "STRING_LITERAL", 
            "ILLEGAL_ESCAPE", "UNCLOSE_STRING", "REAL_LITERAL", "LITERAL", 
            "VAL", "VAR", "LP", "RP", "LCB", "RCB", "LSB", "RSB", "SEMI", 
            "COMMA", "COLON", "DOTDOT", "BREAK", "CONTINUE", "IF", "ELSEIF", 
            "ELSE", "FOREACH", "TRUE", "FALSE", "ARRAY", "IN", "BOOLEAN", 
            "RETURN", "NULL", "CONSTRUCTOR", "DESTRUCTOR", "NEW", "BY", 
            "SELF", "ADD", "SUB", "MUL", "DIV", "MOD", "NOT", "AND", "OR", 
            "EQUAL", "ASSIGN", "NOTEQUAL", "GT", "GTE", "LT", "LTE", "EQUAL_STR", 
            "ADD_STR", "DOT", "SCOPE", "ID", "ID_LIST", "WS", "BLOCK_COMMENT", 
            "UNTERMINATED_COMMENT", "ERROR_CHAR" ]

    ruleNames = [ "T__0", "CLASS_DECLARE", "MEMBER", "METHODS", "BLOCK_STATEMENT", 
                  "LIST_PARAM", "LIST_METHOD", "INT_TYPE", "FLOAT_TYPE", 
                  "STRING", "BOOL_TYPE", "VOID_TYPE", "ARRAY_TYPE", "CLASS", 
                  "PRIMITIVE_TYPE", "INTEGER_LITERAL", "HEX_TYPE", "OCT_TYPE", 
                  "BIN_TYPE", "DEC_TYPE", "STRING_LITERAL", "ILLEGAL_ESCAPE", 
                  "UNCLOSE_STRING", "STR", "ESC_SEQ", "ESC_ILLEGAL", "REAL_LITERAL", 
                  "LITERAL", "VAL", "VAR", "DOLLAR", "LP", "RP", "LCB", 
                  "RCB", "LSB", "RSB", "SEMI", "COMMA", "COLON", "DOTDOT", 
                  "EXPONENT", "DIGIT", "DEC_DIGIT", "SIGN", "BREAK", "CONTINUE", 
                  "IF", "ELSEIF", "ELSE", "FOREACH", "TRUE", "FALSE", "ARRAY", 
                  "IN", "BOOLEAN", "RETURN", "NULL", "CONSTRUCTOR", "DESTRUCTOR", 
                  "NEW", "BY", "SELF", "ADD", "SUB", "MUL", "DIV", "MOD", 
                  "NOT", "AND", "OR", "EQUAL", "ASSIGN", "NOTEQUAL", "GT", 
                  "GTE", "LT", "LTE", "EQUAL_STR", "ADD_STR", "DOT", "SCOPE", 
                  "ID", "ID_LIST", "WS", "BLOCK_COMMENT", "UNTERMINATED_COMMENT", 
                  "ERROR_CHAR" ]

    grammarFileName = "D96.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.8")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


    def emit(self):
        tk = self.type
        result = super().emit() # result mean for input
        # delete later
        print('--------------------------------------------------------------------------------')
        
        print ("{:<30} {:<30} {:<50}".format(result.text, '|', self.symbolicNames[tk-1]))
        print('--------------------------------------------------------------------------------')
        if tk == self.STRING_LITERAL:
            if result.text.find('\'"') >= 0:
                result.text = result.text.replace('\'"', '"')
                return result
        if tk == self.INTEGER_LITERAL or tk == self.REAL_LITERAL:
            result.text = result.text.replace('_', '')
            return result
        return result


    def action(self, localctx:RuleContext, ruleIndex:int, actionIndex:int):
        if self._actions is None:
            actions = dict()
            actions[20] = self.STRING_LITERAL_action 
            actions[21] = self.ILLEGAL_ESCAPE_action 
            actions[22] = self.UNCLOSE_STRING_action 
            actions[86] = self.UNTERMINATED_COMMENT_action 
            actions[87] = self.ERROR_CHAR_action 
            self._actions = actions
        action = self._actions.get(ruleIndex, None)
        if action is not None:
            action(localctx, actionIndex)
        else:
            raise Exception("No registered action for:" + str(ruleIndex))


    def STRING_LITERAL_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 0:

                y = str(self.text)
                self.text = y[1:-1]

     

    def ILLEGAL_ESCAPE_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 1:

               
                y = str(self.text)
                raise IllegalEscape(y[1:])

     

    def UNCLOSE_STRING_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 2:

                x = str(self.text)
                raise UncloseString(x[1:])

     

    def UNTERMINATED_COMMENT_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 3:

                raise ErrorToken('UNTERMINATED_COMMENT')

     

    def ERROR_CHAR_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 4:

                raise ErrorToken(self.text)

     


