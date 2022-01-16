# Generated from e:\HCMUT\PRINCIPLES_OF_PROGRAMMING_LANGUAGE\ppl-assignments\ASS_1\assignment1\src\main\d96\parser\D96.g4 by ANTLR 4.8
from antlr4 import *
from io import StringIO
from typing.io import TextIO
import sys


from lexererr import *
import inspect



def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2H")
        buf.write("\u024f\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7")
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
        buf.write("L\4M\tM\4N\tN\4O\tO\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3")
        buf.write("\3\3\3\3\3\3\3\3\3\3\4\3\4\5\4\u00af\n\4\3\5\3\5\3\5\3")
        buf.write("\5\3\5\3\5\3\6\3\6\3\6\3\6\3\6\3\6\3\6\3\7\3\7\3\7\3\7")
        buf.write("\3\b\3\b\3\b\3\b\3\b\3\b\5\b\u00c8\n\b\3\t\3\t\3\t\3\t")
        buf.write("\5\t\u00ce\n\t\3\t\3\t\7\t\u00d2\n\t\f\t\16\t\u00d5\13")
        buf.write("\t\3\t\3\t\3\t\3\t\3\t\5\t\u00dc\n\t\3\t\3\t\5\t\u00e0")
        buf.write("\n\t\3\n\3\n\3\n\7\n\u00e5\n\n\f\n\16\n\u00e8\13\n\3\n")
        buf.write("\3\n\3\n\3\n\5\n\u00ee\n\n\3\13\3\13\3\13\3\13\5\13\u00f4")
        buf.write("\n\13\3\13\3\13\7\13\u00f8\n\13\f\13\16\13\u00fb\13\13")
        buf.write("\3\13\3\13\3\13\3\13\3\13\5\13\u0102\n\13\3\13\3\13\5")
        buf.write("\13\u0106\n\13\3\f\3\f\3\f\7\f\u010b\n\f\f\f\16\f\u010e")
        buf.write("\13\f\3\f\3\f\5\f\u0112\n\f\3\r\3\r\3\r\3\r\5\r\u0118")
        buf.write("\n\r\3\16\3\16\3\16\3\17\3\17\3\17\3\17\3\17\5\17\u0122")
        buf.write("\n\17\3\20\3\20\7\20\u0126\n\20\f\20\16\20\u0129\13\20")
        buf.write("\3\20\3\20\3\20\3\21\3\21\7\21\u0130\n\21\f\21\16\21\u0133")
        buf.write("\13\21\3\21\3\21\3\21\3\22\3\22\7\22\u013a\n\22\f\22\16")
        buf.write("\22\u013d\13\22\3\22\3\22\3\23\3\23\3\23\3\23\3\23\3\23")
        buf.write("\3\23\3\23\3\23\3\23\3\23\3\23\3\23\5\23\u014e\n\23\3")
        buf.write("\24\3\24\3\24\3\24\3\25\3\25\3\25\3\25\3\26\3\26\3\27")
        buf.write("\3\27\3\30\3\30\3\31\3\31\3\32\3\32\3\33\3\33\3\34\3\34")
        buf.write("\3\35\3\35\3\36\3\36\3\37\3\37\3 \3 \5 \u016e\n \3 \3")
        buf.write(" \3!\3!\3\"\3\"\3\"\7\"\u0177\n\"\f\"\16\"\u017a\13\"")
        buf.write("\3\"\5\"\u017d\n\"\3#\3#\3$\3$\3$\3$\3$\3$\3%\3%\3%\3")
        buf.write("%\3%\3%\3&\3&\3&\3&\3&\3&\3&\3&\3&\3\'\3\'\3\'\3(\3(\3")
        buf.write("(\3(\3(\3(\3(\3)\3)\3)\3)\3)\3*\3*\3*\3*\3*\3*\3*\3*\3")
        buf.write("+\3+\3+\3+\3+\3,\3,\3,\3,\3,\3,\3-\3-\3-\3-\3-\3-\3.\3")
        buf.write(".\3.\3/\3/\3/\3/\3/\3/\3/\3/\3\60\3\60\3\60\3\60\3\60")
        buf.write("\3\60\3\60\3\61\3\61\3\61\3\61\3\61\3\62\3\62\3\62\3\62")
        buf.write("\3\62\3\62\3\62\3\62\3\62\3\62\3\62\3\62\3\63\3\63\3\63")
        buf.write("\3\63\3\63\3\63\3\63\3\63\3\63\3\63\3\63\3\64\3\64\3\64")
        buf.write("\3\64\3\65\3\65\3\65\3\66\3\66\3\66\3\66\3\66\3\67\3\67")
        buf.write("\38\38\39\39\3:\3:\3;\3;\3<\3<\3=\3=\3=\3>\3>\3>\3?\3")
        buf.write("?\3?\3@\3@\3A\3A\3A\3B\3B\3C\3C\3C\3D\3D\3E\3E\3E\3F\3")
        buf.write("F\3F\3F\3G\3G\3G\3H\3H\3I\3I\3I\3J\3J\3J\3K\3K\7K\u022d")
        buf.write("\nK\fK\16K\u0230\13K\3L\3L\6L\u0234\nL\rL\16L\u0235\3")
        buf.write("M\6M\u0239\nM\rM\16M\u023a\3M\3M\3N\3N\3N\3N\7N\u0243")
        buf.write("\nN\fN\16N\u0246\13N\3N\3N\3N\3N\3N\3O\3O\3O\3\u0244\2")
        buf.write("P\3\3\5\4\7\5\t\6\13\7\r\b\17\t\21\n\23\13\25\f\27\r\31")
        buf.write("\2\33\2\35\2\37\16!\17#\20%\21\'\22)\23+\2-\24/\25\61")
        buf.write("\26\63\27\65\30\67\319\32;\33=\34?\2A\2C\2E\2G\35I\36")
        buf.write("K\37M O!Q\"S#U$W%Y&[\'](_)a*c+e,g-i.k/m\60o\61q\62s\63")
        buf.write("u\64w\65y\66{\67}8\1779\u0081:\u0083;\u0085<\u0087=\u0089")
        buf.write(">\u008b?\u008d@\u008fA\u0091B\u0093C\u0095D\u0097E\u0099")
        buf.write("F\u009bG\u009dH\3\2\23\4\2\62;CH\5\2\62;CHaa\3\2\629\4")
        buf.write("\2\629aa\3\2\62\63\4\2\62\63aa\3\2\62;\3\2\63;\4\2\62")
        buf.write(";aa\4\2$$^^\t\2))^^ddhhppttvv\3\2$$\4\2GGgg\4\2--//\5")
        buf.write("\2C\\aac|\6\2\62;C\\aac|\5\2\13\f\16\17\"\"\2\u0266\2")
        buf.write("\3\3\2\2\2\2\5\3\2\2\2\2\7\3\2\2\2\2\t\3\2\2\2\2\13\3")
        buf.write("\2\2\2\2\r\3\2\2\2\2\17\3\2\2\2\2\21\3\2\2\2\2\23\3\2")
        buf.write("\2\2\2\25\3\2\2\2\2\27\3\2\2\2\2\37\3\2\2\2\2!\3\2\2\2")
        buf.write("\2#\3\2\2\2\2%\3\2\2\2\2\'\3\2\2\2\2)\3\2\2\2\2-\3\2\2")
        buf.write("\2\2/\3\2\2\2\2\61\3\2\2\2\2\63\3\2\2\2\2\65\3\2\2\2\2")
        buf.write("\67\3\2\2\2\29\3\2\2\2\2;\3\2\2\2\2=\3\2\2\2\2G\3\2\2")
        buf.write("\2\2I\3\2\2\2\2K\3\2\2\2\2M\3\2\2\2\2O\3\2\2\2\2Q\3\2")
        buf.write("\2\2\2S\3\2\2\2\2U\3\2\2\2\2W\3\2\2\2\2Y\3\2\2\2\2[\3")
        buf.write("\2\2\2\2]\3\2\2\2\2_\3\2\2\2\2a\3\2\2\2\2c\3\2\2\2\2e")
        buf.write("\3\2\2\2\2g\3\2\2\2\2i\3\2\2\2\2k\3\2\2\2\2m\3\2\2\2\2")
        buf.write("o\3\2\2\2\2q\3\2\2\2\2s\3\2\2\2\2u\3\2\2\2\2w\3\2\2\2")
        buf.write("\2y\3\2\2\2\2{\3\2\2\2\2}\3\2\2\2\2\177\3\2\2\2\2\u0081")
        buf.write("\3\2\2\2\2\u0083\3\2\2\2\2\u0085\3\2\2\2\2\u0087\3\2\2")
        buf.write("\2\2\u0089\3\2\2\2\2\u008b\3\2\2\2\2\u008d\3\2\2\2\2\u008f")
        buf.write("\3\2\2\2\2\u0091\3\2\2\2\2\u0093\3\2\2\2\2\u0095\3\2\2")
        buf.write("\2\2\u0097\3\2\2\2\2\u0099\3\2\2\2\2\u009b\3\2\2\2\2\u009d")
        buf.write("\3\2\2\2\3\u009f\3\2\2\2\5\u00a7\3\2\2\2\7\u00ae\3\2\2")
        buf.write("\2\t\u00b0\3\2\2\2\13\u00b6\3\2\2\2\r\u00bd\3\2\2\2\17")
        buf.write("\u00c7\3\2\2\2\21\u00df\3\2\2\2\23\u00ed\3\2\2\2\25\u0105")
        buf.write("\3\2\2\2\27\u0111\3\2\2\2\31\u0117\3\2\2\2\33\u0119\3")
        buf.write("\2\2\2\35\u0121\3\2\2\2\37\u0123\3\2\2\2!\u012d\3\2\2")
        buf.write("\2#\u0137\3\2\2\2%\u014d\3\2\2\2\'\u014f\3\2\2\2)\u0153")
        buf.write("\3\2\2\2+\u0157\3\2\2\2-\u0159\3\2\2\2/\u015b\3\2\2\2")
        buf.write("\61\u015d\3\2\2\2\63\u015f\3\2\2\2\65\u0161\3\2\2\2\67")
        buf.write("\u0163\3\2\2\29\u0165\3\2\2\2;\u0167\3\2\2\2=\u0169\3")
        buf.write("\2\2\2?\u016b\3\2\2\2A\u0171\3\2\2\2C\u017c\3\2\2\2E\u017e")
        buf.write("\3\2\2\2G\u0180\3\2\2\2I\u0186\3\2\2\2K\u018c\3\2\2\2")
        buf.write("M\u0195\3\2\2\2O\u0198\3\2\2\2Q\u019f\3\2\2\2S\u01a4\3")
        buf.write("\2\2\2U\u01ac\3\2\2\2W\u01b1\3\2\2\2Y\u01b7\3\2\2\2[\u01bd")
        buf.write("\3\2\2\2]\u01c0\3\2\2\2_\u01c8\3\2\2\2a\u01cf\3\2\2\2")
        buf.write("c\u01d4\3\2\2\2e\u01e0\3\2\2\2g\u01eb\3\2\2\2i\u01ef\3")
        buf.write("\2\2\2k\u01f2\3\2\2\2m\u01f7\3\2\2\2o\u01f9\3\2\2\2q\u01fb")
        buf.write("\3\2\2\2s\u01fd\3\2\2\2u\u01ff\3\2\2\2w\u0201\3\2\2\2")
        buf.write("y\u0203\3\2\2\2{\u0206\3\2\2\2}\u0209\3\2\2\2\177\u020c")
        buf.write("\3\2\2\2\u0081\u020e\3\2\2\2\u0083\u0211\3\2\2\2\u0085")
        buf.write("\u0213\3\2\2\2\u0087\u0216\3\2\2\2\u0089\u0218\3\2\2\2")
        buf.write("\u008b\u021b\3\2\2\2\u008d\u021f\3\2\2\2\u008f\u0222\3")
        buf.write("\2\2\2\u0091\u0224\3\2\2\2\u0093\u0227\3\2\2\2\u0095\u022a")
        buf.write("\3\2\2\2\u0097\u0231\3\2\2\2\u0099\u0238\3\2\2\2\u009b")
        buf.write("\u023e\3\2\2\2\u009d\u024c\3\2\2\2\u009f\u00a0\7R\2\2")
        buf.write("\u00a0\u00a1\7t\2\2\u00a1\u00a2\7q\2\2\u00a2\u00a3\7i")
        buf.write("\2\2\u00a3\u00a4\7t\2\2\u00a4\u00a5\7c\2\2\u00a5\u00a6")
        buf.write("\7o\2\2\u00a6\4\3\2\2\2\u00a7\u00a8\7o\2\2\u00a8\u00a9")
        buf.write("\7c\2\2\u00a9\u00aa\7k\2\2\u00aa\u00ab\7p\2\2\u00ab\6")
        buf.write("\3\2\2\2\u00ac\u00af\5U+\2\u00ad\u00af\5W,\2\u00ae\u00ac")
        buf.write("\3\2\2\2\u00ae\u00ad\3\2\2\2\u00af\b\3\2\2\2\u00b0\u00b1")
        buf.write("\7H\2\2\u00b1\u00b2\7n\2\2\u00b2\u00b3\7q\2\2\u00b3\u00b4")
        buf.write("\7c\2\2\u00b4\u00b5\7v\2\2\u00b5\n\3\2\2\2\u00b6\u00b7")
        buf.write("\7U\2\2\u00b7\u00b8\7v\2\2\u00b8\u00b9\7t\2\2\u00b9\u00ba")
        buf.write("\7k\2\2\u00ba\u00bb\7p\2\2\u00bb\u00bc\7i\2\2\u00bc\f")
        buf.write("\3\2\2\2\u00bd\u00be\7K\2\2\u00be\u00bf\7p\2\2\u00bf\u00c0")
        buf.write("\7v\2\2\u00c0\16\3\2\2\2\u00c1\u00c8\5\21\t\2\u00c2\u00c8")
        buf.write("\5\23\n\2\u00c3\u00c8\5\25\13\2\u00c4\u00c5\5\27\f\2\u00c5")
        buf.write("\u00c6\b\b\2\2\u00c6\u00c8\3\2\2\2\u00c7\u00c1\3\2\2\2")
        buf.write("\u00c7\u00c2\3\2\2\2\u00c7\u00c3\3\2\2\2\u00c7\u00c4\3")
        buf.write("\2\2\2\u00c8\20\3\2\2\2\u00c9\u00ca\7\62\2\2\u00ca\u00ce")
        buf.write("\7z\2\2\u00cb\u00cc\7\62\2\2\u00cc\u00ce\7Z\2\2\u00cd")
        buf.write("\u00c9\3\2\2\2\u00cd\u00cb\3\2\2\2\u00ce\u00cf\3\2\2\2")
        buf.write("\u00cf\u00d3\t\2\2\2\u00d0\u00d2\t\3\2\2\u00d1\u00d0\3")
        buf.write("\2\2\2\u00d2\u00d5\3\2\2\2\u00d3\u00d1\3\2\2\2\u00d3\u00d4")
        buf.write("\3\2\2\2\u00d4\u00d6\3\2\2\2\u00d5\u00d3\3\2\2\2\u00d6")
        buf.write("\u00e0\t\2\2\2\u00d7\u00d8\7\62\2\2\u00d8\u00dc\7z\2\2")
        buf.write("\u00d9\u00da\7\62\2\2\u00da\u00dc\7Z\2\2\u00db\u00d7\3")
        buf.write("\2\2\2\u00db\u00d9\3\2\2\2\u00dc\u00dd\3\2\2\2\u00dd\u00de")
        buf.write("\t\2\2\2\u00de\u00e0\b\t\3\2\u00df\u00cd\3\2\2\2\u00df")
        buf.write("\u00db\3\2\2\2\u00e0\22\3\2\2\2\u00e1\u00e2\7\62\2\2\u00e2")
        buf.write("\u00e6\t\4\2\2\u00e3\u00e5\t\5\2\2\u00e4\u00e3\3\2\2\2")
        buf.write("\u00e5\u00e8\3\2\2\2\u00e6\u00e4\3\2\2\2\u00e6\u00e7\3")
        buf.write("\2\2\2\u00e7\u00e9\3\2\2\2\u00e8\u00e6\3\2\2\2\u00e9\u00ee")
        buf.write("\t\4\2\2\u00ea\u00eb\7\62\2\2\u00eb\u00ec\t\4\2\2\u00ec")
        buf.write("\u00ee\b\n\4\2\u00ed\u00e1\3\2\2\2\u00ed\u00ea\3\2\2\2")
        buf.write("\u00ee\24\3\2\2\2\u00ef\u00f0\7\62\2\2\u00f0\u00f4\7d")
        buf.write("\2\2\u00f1\u00f2\7\62\2\2\u00f2\u00f4\7D\2\2\u00f3\u00ef")
        buf.write("\3\2\2\2\u00f3\u00f1\3\2\2\2\u00f4\u00f5\3\2\2\2\u00f5")
        buf.write("\u00f9\t\6\2\2\u00f6\u00f8\t\7\2\2\u00f7\u00f6\3\2\2\2")
        buf.write("\u00f8\u00fb\3\2\2\2\u00f9\u00f7\3\2\2\2\u00f9\u00fa\3")
        buf.write("\2\2\2\u00fa\u00fc\3\2\2\2\u00fb\u00f9\3\2\2\2\u00fc\u0106")
        buf.write("\t\6\2\2\u00fd\u00fe\7\62\2\2\u00fe\u0102\7d\2\2\u00ff")
        buf.write("\u0100\7\62\2\2\u0100\u0102\7D\2\2\u0101\u00fd\3\2\2\2")
        buf.write("\u0101\u00ff\3\2\2\2\u0102\u0103\3\2\2\2\u0103\u0104\t")
        buf.write("\6\2\2\u0104\u0106\b\13\5\2\u0105\u00f3\3\2\2\2\u0105")
        buf.write("\u0101\3\2\2\2\u0106\26\3\2\2\2\u0107\u0112\t\b\2\2\u0108")
        buf.write("\u010c\t\t\2\2\u0109\u010b\t\n\2\2\u010a\u0109\3\2\2\2")
        buf.write("\u010b\u010e\3\2\2\2\u010c\u010a\3\2\2\2\u010c\u010d\3")
        buf.write("\2\2\2\u010d\u010f\3\2\2\2\u010e\u010c\3\2\2\2\u010f\u0110")
        buf.write("\t\b\2\2\u0110\u0112\b\f\6\2\u0111\u0107\3\2\2\2\u0111")
        buf.write("\u0108\3\2\2\2\u0112\30\3\2\2\2\u0113\u0114\7)\2\2\u0114")
        buf.write("\u0118\7$\2\2\u0115\u0118\n\13\2\2\u0116\u0118\5\33\16")
        buf.write("\2\u0117\u0113\3\2\2\2\u0117\u0115\3\2\2\2\u0117\u0116")
        buf.write("\3\2\2\2\u0118\32\3\2\2\2\u0119\u011a\7^\2\2\u011a\u011b")
        buf.write("\t\f\2\2\u011b\34\3\2\2\2\u011c\u011d\7^\2\2\u011d\u0122")
        buf.write("\n\f\2\2\u011e\u011f\7)\2\2\u011f\u0122\n\r\2\2\u0120")
        buf.write("\u0122\7^\2\2\u0121\u011c\3\2\2\2\u0121\u011e\3\2\2\2")
        buf.write("\u0121\u0120\3\2\2\2\u0122\36\3\2\2\2\u0123\u0127\7$\2")
        buf.write("\2\u0124\u0126\5\31\r\2\u0125\u0124\3\2\2\2\u0126\u0129")
        buf.write("\3\2\2\2\u0127\u0125\3\2\2\2\u0127\u0128\3\2\2\2\u0128")
        buf.write("\u012a\3\2\2\2\u0129\u0127\3\2\2\2\u012a\u012b\7$\2\2")
        buf.write("\u012b\u012c\b\20\7\2\u012c \3\2\2\2\u012d\u0131\7$\2")
        buf.write("\2\u012e\u0130\5\31\r\2\u012f\u012e\3\2\2\2\u0130\u0133")
        buf.write("\3\2\2\2\u0131\u012f\3\2\2\2\u0131\u0132\3\2\2\2\u0132")
        buf.write("\u0134\3\2\2\2\u0133\u0131\3\2\2\2\u0134\u0135\5\35\17")
        buf.write("\2\u0135\u0136\b\21\b\2\u0136\"\3\2\2\2\u0137\u013b\7")
        buf.write("$\2\2\u0138\u013a\5\31\r\2\u0139\u0138\3\2\2\2\u013a\u013d")
        buf.write("\3\2\2\2\u013b\u0139\3\2\2\2\u013b\u013c\3\2\2\2\u013c")
        buf.write("\u013e\3\2\2\2\u013d\u013b\3\2\2\2\u013e\u013f\b\22\t")
        buf.write("\2\u013f$\3\2\2\2\u0140\u0141\5\27\f\2\u0141\u0142\5\u008f")
        buf.write("H\2\u0142\u0143\5\27\f\2\u0143\u014e\3\2\2\2\u0144\u0145")
        buf.write("\5\27\f\2\u0145\u0146\5? \2\u0146\u014e\3\2\2\2\u0147")
        buf.write("\u0148\5\27\f\2\u0148\u0149\5\u008fH\2\u0149\u014a\5\27")
        buf.write("\f\2\u014a\u014b\5? \2\u014b\u014c\b\23\n\2\u014c\u014e")
        buf.write("\3\2\2\2\u014d\u0140\3\2\2\2\u014d\u0144\3\2\2\2\u014d")
        buf.write("\u0147\3\2\2\2\u014e&\3\2\2\2\u014f\u0150\7X\2\2\u0150")
        buf.write("\u0151\7c\2\2\u0151\u0152\7n\2\2\u0152(\3\2\2\2\u0153")
        buf.write("\u0154\7X\2\2\u0154\u0155\7c\2\2\u0155\u0156\7t\2\2\u0156")
        buf.write("*\3\2\2\2\u0157\u0158\7&\2\2\u0158,\3\2\2\2\u0159\u015a")
        buf.write("\7*\2\2\u015a.\3\2\2\2\u015b\u015c\7+\2\2\u015c\60\3\2")
        buf.write("\2\2\u015d\u015e\7}\2\2\u015e\62\3\2\2\2\u015f\u0160\7")
        buf.write("\177\2\2\u0160\64\3\2\2\2\u0161\u0162\7]\2\2\u0162\66")
        buf.write("\3\2\2\2\u0163\u0164\7_\2\2\u01648\3\2\2\2\u0165\u0166")
        buf.write("\7=\2\2\u0166:\3\2\2\2\u0167\u0168\7.\2\2\u0168<\3\2\2")
        buf.write("\2\u0169\u016a\7<\2\2\u016a>\3\2\2\2\u016b\u016d\t\16")
        buf.write("\2\2\u016c\u016e\5E#\2\u016d\u016c\3\2\2\2\u016d\u016e")
        buf.write("\3\2\2\2\u016e\u016f\3\2\2\2\u016f\u0170\5\27\f\2\u0170")
        buf.write("@\3\2\2\2\u0171\u0172\t\b\2\2\u0172B\3\2\2\2\u0173\u017d")
        buf.write("\t\b\2\2\u0174\u0178\t\t\2\2\u0175\u0177\t\n\2\2\u0176")
        buf.write("\u0175\3\2\2\2\u0177\u017a\3\2\2\2\u0178\u0176\3\2\2\2")
        buf.write("\u0178\u0179\3\2\2\2\u0179\u017b\3\2\2\2\u017a\u0178\3")
        buf.write("\2\2\2\u017b\u017d\t\b\2\2\u017c\u0173\3\2\2\2\u017c\u0174")
        buf.write("\3\2\2\2\u017dD\3\2\2\2\u017e\u017f\t\17\2\2\u017fF\3")
        buf.write("\2\2\2\u0180\u0181\7E\2\2\u0181\u0182\7n\2\2\u0182\u0183")
        buf.write("\7c\2\2\u0183\u0184\7u\2\2\u0184\u0185\7u\2\2\u0185H\3")
        buf.write("\2\2\2\u0186\u0187\7D\2\2\u0187\u0188\7t\2\2\u0188\u0189")
        buf.write("\7g\2\2\u0189\u018a\7c\2\2\u018a\u018b\7m\2\2\u018bJ\3")
        buf.write("\2\2\2\u018c\u018d\7E\2\2\u018d\u018e\7q\2\2\u018e\u018f")
        buf.write("\7p\2\2\u018f\u0190\7v\2\2\u0190\u0191\7k\2\2\u0191\u0192")
        buf.write("\7p\2\2\u0192\u0193\7w\2\2\u0193\u0194\7g\2\2\u0194L\3")
        buf.write("\2\2\2\u0195\u0196\7K\2\2\u0196\u0197\7h\2\2\u0197N\3")
        buf.write("\2\2\2\u0198\u0199\7G\2\2\u0199\u019a\7n\2\2\u019a\u019b")
        buf.write("\7u\2\2\u019b\u019c\7g\2\2\u019c\u019d\7k\2\2\u019d\u019e")
        buf.write("\7h\2\2\u019eP\3\2\2\2\u019f\u01a0\7G\2\2\u01a0\u01a1")
        buf.write("\7n\2\2\u01a1\u01a2\7u\2\2\u01a2\u01a3\7g\2\2\u01a3R\3")
        buf.write("\2\2\2\u01a4\u01a5\7H\2\2\u01a5\u01a6\7q\2\2\u01a6\u01a7")
        buf.write("\7t\2\2\u01a7\u01a8\7g\2\2\u01a8\u01a9\7c\2\2\u01a9\u01aa")
        buf.write("\7e\2\2\u01aa\u01ab\7j\2\2\u01abT\3\2\2\2\u01ac\u01ad")
        buf.write("\7V\2\2\u01ad\u01ae\7t\2\2\u01ae\u01af\7w\2\2\u01af\u01b0")
        buf.write("\7g\2\2\u01b0V\3\2\2\2\u01b1\u01b2\7H\2\2\u01b2\u01b3")
        buf.write("\7c\2\2\u01b3\u01b4\7n\2\2\u01b4\u01b5\7u\2\2\u01b5\u01b6")
        buf.write("\7g\2\2\u01b6X\3\2\2\2\u01b7\u01b8\7C\2\2\u01b8\u01b9")
        buf.write("\7t\2\2\u01b9\u01ba\7t\2\2\u01ba\u01bb\7c\2\2\u01bb\u01bc")
        buf.write("\7{\2\2\u01bcZ\3\2\2\2\u01bd\u01be\7K\2\2\u01be\u01bf")
        buf.write("\7p\2\2\u01bf\\\3\2\2\2\u01c0\u01c1\7D\2\2\u01c1\u01c2")
        buf.write("\7q\2\2\u01c2\u01c3\7q\2\2\u01c3\u01c4\7n\2\2\u01c4\u01c5")
        buf.write("\7g\2\2\u01c5\u01c6\7c\2\2\u01c6\u01c7\7p\2\2\u01c7^\3")
        buf.write("\2\2\2\u01c8\u01c9\7T\2\2\u01c9\u01ca\7g\2\2\u01ca\u01cb")
        buf.write("\7v\2\2\u01cb\u01cc\7w\2\2\u01cc\u01cd\7t\2\2\u01cd\u01ce")
        buf.write("\7p\2\2\u01ce`\3\2\2\2\u01cf\u01d0\7P\2\2\u01d0\u01d1")
        buf.write("\7w\2\2\u01d1\u01d2\7n\2\2\u01d2\u01d3\7n\2\2\u01d3b\3")
        buf.write("\2\2\2\u01d4\u01d5\7E\2\2\u01d5\u01d6\7q\2\2\u01d6\u01d7")
        buf.write("\7p\2\2\u01d7\u01d8\7u\2\2\u01d8\u01d9\7v\2\2\u01d9\u01da")
        buf.write("\7t\2\2\u01da\u01db\7w\2\2\u01db\u01dc\7e\2\2\u01dc\u01dd")
        buf.write("\7v\2\2\u01dd\u01de\7q\2\2\u01de\u01df\7t\2\2\u01dfd\3")
        buf.write("\2\2\2\u01e0\u01e1\7F\2\2\u01e1\u01e2\7g\2\2\u01e2\u01e3")
        buf.write("\7u\2\2\u01e3\u01e4\7v\2\2\u01e4\u01e5\7t\2\2\u01e5\u01e6")
        buf.write("\7w\2\2\u01e6\u01e7\7e\2\2\u01e7\u01e8\7v\2\2\u01e8\u01e9")
        buf.write("\7q\2\2\u01e9\u01ea\7t\2\2\u01eaf\3\2\2\2\u01eb\u01ec")
        buf.write("\7P\2\2\u01ec\u01ed\7g\2\2\u01ed\u01ee\7y\2\2\u01eeh\3")
        buf.write("\2\2\2\u01ef\u01f0\7D\2\2\u01f0\u01f1\7{\2\2\u01f1j\3")
        buf.write("\2\2\2\u01f2\u01f3\7U\2\2\u01f3\u01f4\7g\2\2\u01f4\u01f5")
        buf.write("\7n\2\2\u01f5\u01f6\7h\2\2\u01f6l\3\2\2\2\u01f7\u01f8")
        buf.write("\7-\2\2\u01f8n\3\2\2\2\u01f9\u01fa\7/\2\2\u01fap\3\2\2")
        buf.write("\2\u01fb\u01fc\7,\2\2\u01fcr\3\2\2\2\u01fd\u01fe\7\61")
        buf.write("\2\2\u01fet\3\2\2\2\u01ff\u0200\7\'\2\2\u0200v\3\2\2\2")
        buf.write("\u0201\u0202\7#\2\2\u0202x\3\2\2\2\u0203\u0204\7(\2\2")
        buf.write("\u0204\u0205\7(\2\2\u0205z\3\2\2\2\u0206\u0207\7~\2\2")
        buf.write("\u0207\u0208\7~\2\2\u0208|\3\2\2\2\u0209\u020a\7?\2\2")
        buf.write("\u020a\u020b\7?\2\2\u020b~\3\2\2\2\u020c\u020d\7?\2\2")
        buf.write("\u020d\u0080\3\2\2\2\u020e\u020f\7#\2\2\u020f\u0210\7")
        buf.write("?\2\2\u0210\u0082\3\2\2\2\u0211\u0212\7@\2\2\u0212\u0084")
        buf.write("\3\2\2\2\u0213\u0214\7@\2\2\u0214\u0215\7?\2\2\u0215\u0086")
        buf.write("\3\2\2\2\u0216\u0217\7>\2\2\u0217\u0088\3\2\2\2\u0218")
        buf.write("\u0219\7>\2\2\u0219\u021a\7?\2\2\u021a\u008a\3\2\2\2\u021b")
        buf.write("\u021c\7?\2\2\u021c\u021d\7?\2\2\u021d\u021e\7\60\2\2")
        buf.write("\u021e\u008c\3\2\2\2\u021f\u0220\7-\2\2\u0220\u0221\7")
        buf.write("\60\2\2\u0221\u008e\3\2\2\2\u0222\u0223\7\60\2\2\u0223")
        buf.write("\u0090\3\2\2\2\u0224\u0225\7\60\2\2\u0225\u0226\7\60\2")
        buf.write("\2\u0226\u0092\3\2\2\2\u0227\u0228\7<\2\2\u0228\u0229")
        buf.write("\7<\2\2\u0229\u0094\3\2\2\2\u022a\u022e\t\20\2\2\u022b")
        buf.write("\u022d\t\21\2\2\u022c\u022b\3\2\2\2\u022d\u0230\3\2\2")
        buf.write("\2\u022e\u022c\3\2\2\2\u022e\u022f\3\2\2\2\u022f\u0096")
        buf.write("\3\2\2\2\u0230\u022e\3\2\2\2\u0231\u0233\5+\26\2\u0232")
        buf.write("\u0234\t\21\2\2\u0233\u0232\3\2\2\2\u0234\u0235\3\2\2")
        buf.write("\2\u0235\u0233\3\2\2\2\u0235\u0236\3\2\2\2\u0236\u0098")
        buf.write("\3\2\2\2\u0237\u0239\t\22\2\2\u0238\u0237\3\2\2\2\u0239")
        buf.write("\u023a\3\2\2\2\u023a\u0238\3\2\2\2\u023a\u023b\3\2\2\2")
        buf.write("\u023b\u023c\3\2\2\2\u023c\u023d\bM\13\2\u023d\u009a\3")
        buf.write("\2\2\2\u023e\u023f\7%\2\2\u023f\u0240\7%\2\2\u0240\u0244")
        buf.write("\3\2\2\2\u0241\u0243\13\2\2\2\u0242\u0241\3\2\2\2\u0243")
        buf.write("\u0246\3\2\2\2\u0244\u0245\3\2\2\2\u0244\u0242\3\2\2\2")
        buf.write("\u0245\u0247\3\2\2\2\u0246\u0244\3\2\2\2\u0247\u0248\7")
        buf.write("%\2\2\u0248\u0249\7%\2\2\u0249\u024a\3\2\2\2\u024a\u024b")
        buf.write("\bN\13\2\u024b\u009c\3\2\2\2\u024c\u024d\13\2\2\2\u024d")
        buf.write("\u024e\bO\f\2\u024e\u009e\3\2\2\2\36\2\u00ae\u00c7\u00cd")
        buf.write("\u00d3\u00db\u00df\u00e6\u00ed\u00f3\u00f9\u0101\u0105")
        buf.write("\u010c\u0111\u0117\u0121\u0127\u0131\u013b\u014d\u016d")
        buf.write("\u0178\u017c\u022e\u0235\u023a\u0244\r\3\b\2\3\t\3\3\n")
        buf.write("\4\3\13\5\3\f\6\3\20\7\3\21\b\3\22\t\3\23\n\b\2\2\3O\13")
        return buf.getvalue()


class D96Lexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    T__0 = 1
    T__1 = 2
    BOOL_TYPE = 3
    FLOAT_TYPE = 4
    STRING = 5
    INT_TYPE = 6
    INTEGER_LITERAL = 7
    HEX_TYPE = 8
    OCT_TYPE = 9
    BIN_TYPE = 10
    DEC_TYPE = 11
    STRING_LITERAL = 12
    ILLEGAL_ESCAPE = 13
    UNCLOSE_STRING = 14
    REAL_LITERAL = 15
    VAL = 16
    VAR = 17
    LP = 18
    RP = 19
    LCB = 20
    RCB = 21
    LSB = 22
    RSB = 23
    SEMI = 24
    COMMA = 25
    COLON = 26
    CLASS = 27
    BREAK = 28
    CONTINUE = 29
    IF = 30
    ELSEIF = 31
    ELSE = 32
    FOREACH = 33
    TRUE = 34
    FALSE = 35
    ARRAY = 36
    IN = 37
    BOOLEAN = 38
    RETURN = 39
    NULL = 40
    CONSTRUCTOR = 41
    DESTRUCTOR = 42
    NEW = 43
    BY = 44
    SELF = 45
    ADD = 46
    SUB = 47
    MUL = 48
    DIV = 49
    MOD = 50
    NOT = 51
    AND = 52
    OR = 53
    EQUAL = 54
    ASSIGN = 55
    NOTEQUAL = 56
    GT = 57
    GTE = 58
    LT = 59
    LTE = 60
    EQUAL_STR = 61
    ADD_STR = 62
    DOT = 63
    DOTDOT = 64
    SCOPE = 65
    NORMAL_ID = 66
    DOLLAR_ID = 67
    WS = 68
    BLOCK_COMMENT = 69
    ERROR_CHAR = 70

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'Program'", "'main'", "'Float'", "'String'", "'Int'", "'Val'", 
            "'Var'", "'('", "')'", "'{'", "'}'", "'['", "']'", "';'", "','", 
            "':'", "'Class'", "'Break'", "'Continue'", "'If'", "'Elseif'", 
            "'Else'", "'Foreach'", "'True'", "'False'", "'Array'", "'In'", 
            "'Boolean'", "'Return'", "'Null'", "'Constructor'", "'Destructor'", 
            "'New'", "'By'", "'Self'", "'+'", "'-'", "'*'", "'/'", "'%'", 
            "'!'", "'&&'", "'||'", "'=='", "'='", "'!='", "'>'", "'>='", 
            "'<'", "'<='", "'==.'", "'+.'", "'.'", "'..'", "'::'" ]

    symbolicNames = [ "<INVALID>",
            "BOOL_TYPE", "FLOAT_TYPE", "STRING", "INT_TYPE", "INTEGER_LITERAL", 
            "HEX_TYPE", "OCT_TYPE", "BIN_TYPE", "DEC_TYPE", "STRING_LITERAL", 
            "ILLEGAL_ESCAPE", "UNCLOSE_STRING", "REAL_LITERAL", "VAL", "VAR", 
            "LP", "RP", "LCB", "RCB", "LSB", "RSB", "SEMI", "COMMA", "COLON", 
            "CLASS", "BREAK", "CONTINUE", "IF", "ELSEIF", "ELSE", "FOREACH", 
            "TRUE", "FALSE", "ARRAY", "IN", "BOOLEAN", "RETURN", "NULL", 
            "CONSTRUCTOR", "DESTRUCTOR", "NEW", "BY", "SELF", "ADD", "SUB", 
            "MUL", "DIV", "MOD", "NOT", "AND", "OR", "EQUAL", "ASSIGN", 
            "NOTEQUAL", "GT", "GTE", "LT", "LTE", "EQUAL_STR", "ADD_STR", 
            "DOT", "DOTDOT", "SCOPE", "NORMAL_ID", "DOLLAR_ID", "WS", "BLOCK_COMMENT", 
            "ERROR_CHAR" ]

    ruleNames = [ "T__0", "T__1", "BOOL_TYPE", "FLOAT_TYPE", "STRING", "INT_TYPE", 
                  "INTEGER_LITERAL", "HEX_TYPE", "OCT_TYPE", "BIN_TYPE", 
                  "DEC_TYPE", "STR", "ESC_SEQ", "ESC_ILLEGAL", "STRING_LITERAL", 
                  "ILLEGAL_ESCAPE", "UNCLOSE_STRING", "REAL_LITERAL", "VAL", 
                  "VAR", "DOLLAR", "LP", "RP", "LCB", "RCB", "LSB", "RSB", 
                  "SEMI", "COMMA", "COLON", "EXPONENT", "DIGIT", "DEC_DIGIT", 
                  "SIGN", "CLASS", "BREAK", "CONTINUE", "IF", "ELSEIF", 
                  "ELSE", "FOREACH", "TRUE", "FALSE", "ARRAY", "IN", "BOOLEAN", 
                  "RETURN", "NULL", "CONSTRUCTOR", "DESTRUCTOR", "NEW", 
                  "BY", "SELF", "ADD", "SUB", "MUL", "DIV", "MOD", "NOT", 
                  "AND", "OR", "EQUAL", "ASSIGN", "NOTEQUAL", "GT", "GTE", 
                  "LT", "LTE", "EQUAL_STR", "ADD_STR", "DOT", "DOTDOT", 
                  "SCOPE", "NORMAL_ID", "DOLLAR_ID", "WS", "BLOCK_COMMENT", 
                  "ERROR_CHAR" ]

    grammarFileName = "D96.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.8")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


    def printToken(self):
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
    def emit(self):
        self.printToken()
        tk = self.type
        result = super().emit()
        if tk == self.INTEGER_LITERAL or tk == self.REAL_LITERAL:
            result.text = result.text.replace('_', '')
        return result


    def action(self, localctx:RuleContext, ruleIndex:int, actionIndex:int):
        if self._actions is None:
            actions = dict()
            actions[6] = self.INTEGER_LITERAL_action 
            actions[7] = self.HEX_TYPE_action 
            actions[8] = self.OCT_TYPE_action 
            actions[9] = self.BIN_TYPE_action 
            actions[10] = self.DEC_TYPE_action 
            actions[14] = self.STRING_LITERAL_action 
            actions[15] = self.ILLEGAL_ESCAPE_action 
            actions[16] = self.UNCLOSE_STRING_action 
            actions[17] = self.REAL_LITERAL_action 
            actions[77] = self.ERROR_CHAR_action 
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
     


