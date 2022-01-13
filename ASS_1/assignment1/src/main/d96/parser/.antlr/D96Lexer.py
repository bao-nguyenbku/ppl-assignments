# Generated from e:\HCMUT\PRINCIPLES_OF_PROGRAMMING_LANGUAGE\ppl-assignments\ASS_1\assignment1\src\main\d96\parser\D96.g4 by ANTLR 4.8
from antlr4 import *
from io import StringIO
from typing.io import TextIO
import sys


from lexererr import *
import inspect



def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2J")
        buf.write("\u0246\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7")
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
        buf.write("\3\n\3\n\5\n\u00e0\n\n\3\13\3\13\3\13\3\13\5\13\u00e6")
        buf.write("\n\13\3\13\6\13\u00e9\n\13\r\13\16\13\u00ea\3\f\3\f\6")
        buf.write("\f\u00ef\n\f\r\f\16\f\u00f0\3\r\3\r\3\r\3\r\5\r\u00f7")
        buf.write("\n\r\3\r\6\r\u00fa\n\r\r\r\16\r\u00fb\3\16\3\16\7\16\u0100")
        buf.write("\n\16\f\16\16\16\u0103\13\16\3\17\3\17\7\17\u0107\n\17")
        buf.write("\f\17\16\17\u010a\13\17\3\17\3\17\3\17\3\20\3\20\7\20")
        buf.write("\u0111\n\20\f\20\16\20\u0114\13\20\3\20\3\20\3\20\3\21")
        buf.write("\3\21\7\21\u011b\n\21\f\21\16\21\u011e\13\21\3\21\3\21")
        buf.write("\3\21\3\22\3\22\3\22\3\22\3\22\5\22\u0128\n\22\3\23\3")
        buf.write("\23\3\23\3\24\3\24\3\24\3\25\3\25\5\25\u0132\n\25\3\25")
        buf.write("\3\25\7\25\u0136\n\25\f\25\16\25\u0139\13\25\3\26\3\26")
        buf.write("\3\26\3\26\3\27\3\27\3\27\3\27\3\30\3\30\3\31\3\31\3\32")
        buf.write("\3\32\3\33\3\33\3\34\3\34\3\35\3\35\3\36\3\36\3\37\3\37")
        buf.write("\3 \3 \3!\3!\3\"\3\"\5\"\u0159\n\"\3\"\3\"\3#\3#\3$\3")
        buf.write("$\3$\7$\u0162\n$\f$\16$\u0165\13$\5$\u0167\n$\3%\3%\3")
        buf.write("&\3&\3&\3&\3&\3&\3\'\3\'\3\'\3\'\3\'\3\'\3(\3(\3(\3(\3")
        buf.write("(\3(\3(\3(\3(\3)\3)\3)\3*\3*\3*\3*\3*\3*\3*\3+\3+\3+\3")
        buf.write("+\3+\3,\3,\3,\3,\3,\3,\3,\3,\3-\3-\3-\3-\3-\3.\3.\3.\3")
        buf.write(".\3.\3.\3/\3/\3/\3/\3/\3/\3\60\3\60\3\60\3\61\3\61\3\61")
        buf.write("\3\61\3\61\3\61\3\61\3\61\3\62\3\62\3\62\3\62\3\62\3\62")
        buf.write("\3\62\3\63\3\63\3\63\3\63\3\63\3\64\3\64\3\64\3\64\3\64")
        buf.write("\3\64\3\64\3\64\3\64\3\64\3\64\3\64\3\65\3\65\3\65\3\65")
        buf.write("\3\65\3\65\3\65\3\65\3\65\3\65\3\65\3\66\3\66\3\66\3\66")
        buf.write("\3\67\3\67\3\67\38\38\38\38\38\39\39\3:\3:\3;\3;\3<\3")
        buf.write("<\3=\3=\3>\3>\3?\3?\3?\3@\3@\3@\3A\3A\3A\3B\3B\3C\3C\3")
        buf.write("C\3D\3D\3E\3E\3E\3F\3F\3G\3G\3G\3H\3H\3H\3H\3I\3I\3I\3")
        buf.write("J\3J\3J\3K\3K\3L\3L\3L\3M\3M\7M\u0217\nM\fM\16M\u021a")
        buf.write("\13M\3M\3M\6M\u021e\nM\rM\16M\u021f\5M\u0222\nM\3N\3N")
        buf.write("\3N\3N\7N\u0228\nN\fN\16N\u022b\13N\3N\3N\3N\3N\3N\3O")
        buf.write("\3O\3O\3O\7O\u0236\nO\fO\16O\u0239\13O\3O\3O\3P\6P\u023e")
        buf.write("\nP\rP\16P\u023f\3P\3P\3Q\3Q\3Q\4\u0229\u0237\2R\3\3\5")
        buf.write("\4\7\5\t\6\13\7\r\b\17\t\21\n\23\13\25\f\27\r\31\16\33")
        buf.write("\17\35\20\37\21!\22#\2%\2\'\2)\23+\24-\25/\2\61\26\63")
        buf.write("\27\65\30\67\319\32;\33=\34?\35A\36C\2E\2G\2I\2K\37M ")
        buf.write("O!Q\"S#U$W%Y&[\'](_)a*c+e,g-i.k/m\60o\61q\62s\63u\64w")
        buf.write("\65y\66{\67}8\1779\u0081:\u0083;\u0085<\u0087=\u0089>")
        buf.write("\u008b?\u008d@\u008fA\u0091B\u0093C\u0095D\u0097E\u0099")
        buf.write("F\u009bG\u009dH\u009fI\u00a1J\3\2\17\5\2\62;CHch\3\2\62")
        buf.write(";\3\2\62\63\4\2\62;aa\t\2$$^^ddhhppttvv\4\2$$^^\n\2$$")
        buf.write("))^^ddhhppttvv\4\2GGgg\3\2\63;\4\2--//\5\2C\\aac|\6\2")
        buf.write("\62;C\\aac|\5\2\13\f\17\17\"\"\2\u0258\2\3\3\2\2\2\2\5")
        buf.write("\3\2\2\2\2\7\3\2\2\2\2\t\3\2\2\2\2\13\3\2\2\2\2\r\3\2")
        buf.write("\2\2\2\17\3\2\2\2\2\21\3\2\2\2\2\23\3\2\2\2\2\25\3\2\2")
        buf.write("\2\2\27\3\2\2\2\2\31\3\2\2\2\2\33\3\2\2\2\2\35\3\2\2\2")
        buf.write("\2\37\3\2\2\2\2!\3\2\2\2\2)\3\2\2\2\2+\3\2\2\2\2-\3\2")
        buf.write("\2\2\2\61\3\2\2\2\2\63\3\2\2\2\2\65\3\2\2\2\2\67\3\2\2")
        buf.write("\2\29\3\2\2\2\2;\3\2\2\2\2=\3\2\2\2\2?\3\2\2\2\2A\3\2")
        buf.write("\2\2\2K\3\2\2\2\2M\3\2\2\2\2O\3\2\2\2\2Q\3\2\2\2\2S\3")
        buf.write("\2\2\2\2U\3\2\2\2\2W\3\2\2\2\2Y\3\2\2\2\2[\3\2\2\2\2]")
        buf.write("\3\2\2\2\2_\3\2\2\2\2a\3\2\2\2\2c\3\2\2\2\2e\3\2\2\2\2")
        buf.write("g\3\2\2\2\2i\3\2\2\2\2k\3\2\2\2\2m\3\2\2\2\2o\3\2\2\2")
        buf.write("\2q\3\2\2\2\2s\3\2\2\2\2u\3\2\2\2\2w\3\2\2\2\2y\3\2\2")
        buf.write("\2\2{\3\2\2\2\2}\3\2\2\2\2\177\3\2\2\2\2\u0081\3\2\2\2")
        buf.write("\2\u0083\3\2\2\2\2\u0085\3\2\2\2\2\u0087\3\2\2\2\2\u0089")
        buf.write("\3\2\2\2\2\u008b\3\2\2\2\2\u008d\3\2\2\2\2\u008f\3\2\2")
        buf.write("\2\2\u0091\3\2\2\2\2\u0093\3\2\2\2\2\u0095\3\2\2\2\2\u0097")
        buf.write("\3\2\2\2\2\u0099\3\2\2\2\2\u009b\3\2\2\2\2\u009d\3\2\2")
        buf.write("\2\2\u009f\3\2\2\2\2\u00a1\3\2\2\2\3\u00a3\3\2\2\2\5\u00ab")
        buf.write("\3\2\2\2\7\u00b0\3\2\2\2\t\u00c3\3\2\2\2\13\u00c5\3\2")
        buf.write("\2\2\r\u00cb\3\2\2\2\17\u00d2\3\2\2\2\21\u00d6\3\2\2\2")
        buf.write("\23\u00df\3\2\2\2\25\u00e5\3\2\2\2\27\u00ec\3\2\2\2\31")
        buf.write("\u00f6\3\2\2\2\33\u00fd\3\2\2\2\35\u0104\3\2\2\2\37\u010e")
        buf.write("\3\2\2\2!\u0118\3\2\2\2#\u0127\3\2\2\2%\u0129\3\2\2\2")
        buf.write("\'\u012c\3\2\2\2)\u012f\3\2\2\2+\u013a\3\2\2\2-\u013e")
        buf.write("\3\2\2\2/\u0142\3\2\2\2\61\u0144\3\2\2\2\63\u0146\3\2")
        buf.write("\2\2\65\u0148\3\2\2\2\67\u014a\3\2\2\29\u014c\3\2\2\2")
        buf.write(";\u014e\3\2\2\2=\u0150\3\2\2\2?\u0152\3\2\2\2A\u0154\3")
        buf.write("\2\2\2C\u0156\3\2\2\2E\u015c\3\2\2\2G\u0166\3\2\2\2I\u0168")
        buf.write("\3\2\2\2K\u016a\3\2\2\2M\u0170\3\2\2\2O\u0176\3\2\2\2")
        buf.write("Q\u017f\3\2\2\2S\u0182\3\2\2\2U\u0189\3\2\2\2W\u018e\3")
        buf.write("\2\2\2Y\u0196\3\2\2\2[\u019b\3\2\2\2]\u01a1\3\2\2\2_\u01a7")
        buf.write("\3\2\2\2a\u01aa\3\2\2\2c\u01b2\3\2\2\2e\u01b9\3\2\2\2")
        buf.write("g\u01be\3\2\2\2i\u01ca\3\2\2\2k\u01d5\3\2\2\2m\u01d9\3")
        buf.write("\2\2\2o\u01dc\3\2\2\2q\u01e1\3\2\2\2s\u01e3\3\2\2\2u\u01e5")
        buf.write("\3\2\2\2w\u01e7\3\2\2\2y\u01e9\3\2\2\2{\u01eb\3\2\2\2")
        buf.write("}\u01ed\3\2\2\2\177\u01f0\3\2\2\2\u0081\u01f3\3\2\2\2")
        buf.write("\u0083\u01f6\3\2\2\2\u0085\u01f8\3\2\2\2\u0087\u01fb\3")
        buf.write("\2\2\2\u0089\u01fd\3\2\2\2\u008b\u0200\3\2\2\2\u008d\u0202")
        buf.write("\3\2\2\2\u008f\u0205\3\2\2\2\u0091\u0209\3\2\2\2\u0093")
        buf.write("\u020c\3\2\2\2\u0095\u020f\3\2\2\2\u0097\u0211\3\2\2\2")
        buf.write("\u0099\u0221\3\2\2\2\u009b\u0223\3\2\2\2\u009d\u0231\3")
        buf.write("\2\2\2\u009f\u023d\3\2\2\2\u00a1\u0243\3\2\2\2\u00a3\u00a4")
        buf.write("\7R\2\2\u00a4\u00a5\7t\2\2\u00a5\u00a6\7q\2\2\u00a6\u00a7")
        buf.write("\7i\2\2\u00a7\u00a8\7t\2\2\u00a8\u00a9\7c\2\2\u00a9\u00aa")
        buf.write("\7o\2\2\u00aa\4\3\2\2\2\u00ab\u00ac\7o\2\2\u00ac\u00ad")
        buf.write("\7c\2\2\u00ad\u00ae\7k\2\2\u00ae\u00af\7p\2\2\u00af\6")
        buf.write("\3\2\2\2\u00b0\u00b1\7c\2\2\u00b1\u00b2\7u\2\2\u00b2\u00b3")
        buf.write("\7u\2\2\u00b3\u00b4\7k\2\2\u00b4\u00b5\7i\2\2\u00b5\u00b6")
        buf.write("\7p\2\2\u00b6\u00b7\7a\2\2\u00b7\u00b8\7u\2\2\u00b8\u00b9")
        buf.write("\7v\2\2\u00b9\u00ba\7c\2\2\u00ba\u00bb\7v\2\2\u00bb\u00bc")
        buf.write("\7g\2\2\u00bc\u00bd\7o\2\2\u00bd\u00be\7g\2\2\u00be\u00bf")
        buf.write("\7p\2\2\u00bf\u00c0\7v\2\2\u00c0\b\3\2\2\2\u00c1\u00c4")
        buf.write("\5Y-\2\u00c2\u00c4\5[.\2\u00c3\u00c1\3\2\2\2\u00c3\u00c2")
        buf.write("\3\2\2\2\u00c4\n\3\2\2\2\u00c5\u00c6\7H\2\2\u00c6\u00c7")
        buf.write("\7n\2\2\u00c7\u00c8\7q\2\2\u00c8\u00c9\7c\2\2\u00c9\u00ca")
        buf.write("\7v\2\2\u00ca\f\3\2\2\2\u00cb\u00cc\7U\2\2\u00cc\u00cd")
        buf.write("\7v\2\2\u00cd\u00ce\7t\2\2\u00ce\u00cf\7k\2\2\u00cf\u00d0")
        buf.write("\7p\2\2\u00d0\u00d1\7i\2\2\u00d1\16\3\2\2\2\u00d2\u00d3")
        buf.write("\7K\2\2\u00d3\u00d4\7p\2\2\u00d4\u00d5\7v\2\2\u00d5\20")
        buf.write("\3\2\2\2\u00d6\u00d7\7X\2\2\u00d7\u00d8\7q\2\2\u00d8\u00d9")
        buf.write("\7k\2\2\u00d9\u00da\7f\2\2\u00da\22\3\2\2\2\u00db\u00e0")
        buf.write("\5\25\13\2\u00dc\u00e0\5\27\f\2\u00dd\u00e0\5\31\r\2\u00de")
        buf.write("\u00e0\5\33\16\2\u00df\u00db\3\2\2\2\u00df\u00dc\3\2\2")
        buf.write("\2\u00df\u00dd\3\2\2\2\u00df\u00de\3\2\2\2\u00e0\24\3")
        buf.write("\2\2\2\u00e1\u00e2\7\62\2\2\u00e2\u00e6\7z\2\2\u00e3\u00e4")
        buf.write("\7\62\2\2\u00e4\u00e6\7Z\2\2\u00e5\u00e1\3\2\2\2\u00e5")
        buf.write("\u00e3\3\2\2\2\u00e6\u00e8\3\2\2\2\u00e7\u00e9\t\2\2\2")
        buf.write("\u00e8\u00e7\3\2\2\2\u00e9\u00ea\3\2\2\2\u00ea\u00e8\3")
        buf.write("\2\2\2\u00ea\u00eb\3\2\2\2\u00eb\26\3\2\2\2\u00ec\u00ee")
        buf.write("\7\62\2\2\u00ed\u00ef\t\3\2\2\u00ee\u00ed\3\2\2\2\u00ef")
        buf.write("\u00f0\3\2\2\2\u00f0\u00ee\3\2\2\2\u00f0\u00f1\3\2\2\2")
        buf.write("\u00f1\30\3\2\2\2\u00f2\u00f3\7\62\2\2\u00f3\u00f7\7d")
        buf.write("\2\2\u00f4\u00f5\7\62\2\2\u00f5\u00f7\7D\2\2\u00f6\u00f2")
        buf.write("\3\2\2\2\u00f6\u00f4\3\2\2\2\u00f7\u00f9\3\2\2\2\u00f8")
        buf.write("\u00fa\t\4\2\2\u00f9\u00f8\3\2\2\2\u00fa\u00fb\3\2\2\2")
        buf.write("\u00fb\u00f9\3\2\2\2\u00fb\u00fc\3\2\2\2\u00fc\32\3\2")
        buf.write("\2\2\u00fd\u0101\t\3\2\2\u00fe\u0100\t\5\2\2\u00ff\u00fe")
        buf.write("\3\2\2\2\u0100\u0103\3\2\2\2\u0101\u00ff\3\2\2\2\u0101")
        buf.write("\u0102\3\2\2\2\u0102\34\3\2\2\2\u0103\u0101\3\2\2\2\u0104")
        buf.write("\u0108\7$\2\2\u0105\u0107\5#\22\2\u0106\u0105\3\2\2\2")
        buf.write("\u0107\u010a\3\2\2\2\u0108\u0106\3\2\2\2\u0108\u0109\3")
        buf.write("\2\2\2\u0109\u010b\3\2\2\2\u010a\u0108\3\2\2\2\u010b\u010c")
        buf.write("\5\'\24\2\u010c\u010d\b\17\2\2\u010d\36\3\2\2\2\u010e")
        buf.write("\u0112\7$\2\2\u010f\u0111\5#\22\2\u0110\u010f\3\2\2\2")
        buf.write("\u0111\u0114\3\2\2\2\u0112\u0110\3\2\2\2\u0112\u0113\3")
        buf.write("\2\2\2\u0113\u0115\3\2\2\2\u0114\u0112\3\2\2\2\u0115\u0116")
        buf.write("\7\2\2\3\u0116\u0117\b\20\3\2\u0117 \3\2\2\2\u0118\u011c")
        buf.write("\7$\2\2\u0119\u011b\5#\22\2\u011a\u0119\3\2\2\2\u011b")
        buf.write("\u011e\3\2\2\2\u011c\u011a\3\2\2\2\u011c\u011d\3\2\2\2")
        buf.write("\u011d\u011f\3\2\2\2\u011e\u011c\3\2\2\2\u011f\u0120\7")
        buf.write("$\2\2\u0120\u0121\b\21\4\2\u0121\"\3\2\2\2\u0122\u0123")
        buf.write("\7^\2\2\u0123\u0128\t\6\2\2\u0124\u0128\n\7\2\2\u0125")
        buf.write("\u0126\7)\2\2\u0126\u0128\7$\2\2\u0127\u0122\3\2\2\2\u0127")
        buf.write("\u0124\3\2\2\2\u0127\u0125\3\2\2\2\u0128$\3\2\2\2\u0129")
        buf.write("\u012a\7^\2\2\u012a\u012b\t\b\2\2\u012b&\3\2\2\2\u012c")
        buf.write("\u012d\7^\2\2\u012d\u012e\n\6\2\2\u012e(\3\2\2\2\u012f")
        buf.write("\u0131\5G$\2\u0130\u0132\5\u0095K\2\u0131\u0130\3\2\2")
        buf.write("\2\u0131\u0132\3\2\2\2\u0132\u0137\3\2\2\2\u0133\u0136")
        buf.write("\5G$\2\u0134\u0136\5C\"\2\u0135\u0133\3\2\2\2\u0135\u0134")
        buf.write("\3\2\2\2\u0136\u0139\3\2\2\2\u0137\u0135\3\2\2\2\u0137")
        buf.write("\u0138\3\2\2\2\u0138*\3\2\2\2\u0139\u0137\3\2\2\2\u013a")
        buf.write("\u013b\7X\2\2\u013b\u013c\7c\2\2\u013c\u013d\7n\2\2\u013d")
        buf.write(",\3\2\2\2\u013e\u013f\7X\2\2\u013f\u0140\7c\2\2\u0140")
        buf.write("\u0141\7t\2\2\u0141.\3\2\2\2\u0142\u0143\7&\2\2\u0143")
        buf.write("\60\3\2\2\2\u0144\u0145\7*\2\2\u0145\62\3\2\2\2\u0146")
        buf.write("\u0147\7+\2\2\u0147\64\3\2\2\2\u0148\u0149\7}\2\2\u0149")
        buf.write("\66\3\2\2\2\u014a\u014b\7\177\2\2\u014b8\3\2\2\2\u014c")
        buf.write("\u014d\7]\2\2\u014d:\3\2\2\2\u014e\u014f\7_\2\2\u014f")
        buf.write("<\3\2\2\2\u0150\u0151\7=\2\2\u0151>\3\2\2\2\u0152\u0153")
        buf.write("\7.\2\2\u0153@\3\2\2\2\u0154\u0155\7<\2\2\u0155B\3\2\2")
        buf.write("\2\u0156\u0158\t\t\2\2\u0157\u0159\5I%\2\u0158\u0157\3")
        buf.write("\2\2\2\u0158\u0159\3\2\2\2\u0159\u015a\3\2\2\2\u015a\u015b")
        buf.write("\5\33\16\2\u015bD\3\2\2\2\u015c\u015d\t\3\2\2\u015dF\3")
        buf.write("\2\2\2\u015e\u0167\t\3\2\2\u015f\u0163\t\n\2\2\u0160\u0162")
        buf.write("\t\5\2\2\u0161\u0160\3\2\2\2\u0162\u0165\3\2\2\2\u0163")
        buf.write("\u0161\3\2\2\2\u0163\u0164\3\2\2\2\u0164\u0167\3\2\2\2")
        buf.write("\u0165\u0163\3\2\2\2\u0166\u015e\3\2\2\2\u0166\u015f\3")
        buf.write("\2\2\2\u0167H\3\2\2\2\u0168\u0169\t\13\2\2\u0169J\3\2")
        buf.write("\2\2\u016a\u016b\7E\2\2\u016b\u016c\7n\2\2\u016c\u016d")
        buf.write("\7c\2\2\u016d\u016e\7u\2\2\u016e\u016f\7u\2\2\u016fL\3")
        buf.write("\2\2\2\u0170\u0171\7D\2\2\u0171\u0172\7t\2\2\u0172\u0173")
        buf.write("\7g\2\2\u0173\u0174\7c\2\2\u0174\u0175\7m\2\2\u0175N\3")
        buf.write("\2\2\2\u0176\u0177\7E\2\2\u0177\u0178\7q\2\2\u0178\u0179")
        buf.write("\7p\2\2\u0179\u017a\7v\2\2\u017a\u017b\7k\2\2\u017b\u017c")
        buf.write("\7p\2\2\u017c\u017d\7w\2\2\u017d\u017e\7g\2\2\u017eP\3")
        buf.write("\2\2\2\u017f\u0180\7K\2\2\u0180\u0181\7h\2\2\u0181R\3")
        buf.write("\2\2\2\u0182\u0183\7G\2\2\u0183\u0184\7n\2\2\u0184\u0185")
        buf.write("\7u\2\2\u0185\u0186\7g\2\2\u0186\u0187\7k\2\2\u0187\u0188")
        buf.write("\7h\2\2\u0188T\3\2\2\2\u0189\u018a\7G\2\2\u018a\u018b")
        buf.write("\7n\2\2\u018b\u018c\7u\2\2\u018c\u018d\7g\2\2\u018dV\3")
        buf.write("\2\2\2\u018e\u018f\7H\2\2\u018f\u0190\7q\2\2\u0190\u0191")
        buf.write("\7t\2\2\u0191\u0192\7g\2\2\u0192\u0193\7c\2\2\u0193\u0194")
        buf.write("\7e\2\2\u0194\u0195\7j\2\2\u0195X\3\2\2\2\u0196\u0197")
        buf.write("\7V\2\2\u0197\u0198\7t\2\2\u0198\u0199\7w\2\2\u0199\u019a")
        buf.write("\7g\2\2\u019aZ\3\2\2\2\u019b\u019c\7H\2\2\u019c\u019d")
        buf.write("\7c\2\2\u019d\u019e\7n\2\2\u019e\u019f\7u\2\2\u019f\u01a0")
        buf.write("\7g\2\2\u01a0\\\3\2\2\2\u01a1\u01a2\7C\2\2\u01a2\u01a3")
        buf.write("\7t\2\2\u01a3\u01a4\7t\2\2\u01a4\u01a5\7c\2\2\u01a5\u01a6")
        buf.write("\7{\2\2\u01a6^\3\2\2\2\u01a7\u01a8\7K\2\2\u01a8\u01a9")
        buf.write("\7p\2\2\u01a9`\3\2\2\2\u01aa\u01ab\7D\2\2\u01ab\u01ac")
        buf.write("\7q\2\2\u01ac\u01ad\7q\2\2\u01ad\u01ae\7n\2\2\u01ae\u01af")
        buf.write("\7g\2\2\u01af\u01b0\7c\2\2\u01b0\u01b1\7p\2\2\u01b1b\3")
        buf.write("\2\2\2\u01b2\u01b3\7T\2\2\u01b3\u01b4\7g\2\2\u01b4\u01b5")
        buf.write("\7v\2\2\u01b5\u01b6\7w\2\2\u01b6\u01b7\7t\2\2\u01b7\u01b8")
        buf.write("\7p\2\2\u01b8d\3\2\2\2\u01b9\u01ba\7P\2\2\u01ba\u01bb")
        buf.write("\7w\2\2\u01bb\u01bc\7n\2\2\u01bc\u01bd\7n\2\2\u01bdf\3")
        buf.write("\2\2\2\u01be\u01bf\7E\2\2\u01bf\u01c0\7q\2\2\u01c0\u01c1")
        buf.write("\7p\2\2\u01c1\u01c2\7u\2\2\u01c2\u01c3\7v\2\2\u01c3\u01c4")
        buf.write("\7t\2\2\u01c4\u01c5\7w\2\2\u01c5\u01c6\7e\2\2\u01c6\u01c7")
        buf.write("\7v\2\2\u01c7\u01c8\7q\2\2\u01c8\u01c9\7t\2\2\u01c9h\3")
        buf.write("\2\2\2\u01ca\u01cb\7F\2\2\u01cb\u01cc\7g\2\2\u01cc\u01cd")
        buf.write("\7u\2\2\u01cd\u01ce\7v\2\2\u01ce\u01cf\7t\2\2\u01cf\u01d0")
        buf.write("\7w\2\2\u01d0\u01d1\7e\2\2\u01d1\u01d2\7v\2\2\u01d2\u01d3")
        buf.write("\7q\2\2\u01d3\u01d4\7t\2\2\u01d4j\3\2\2\2\u01d5\u01d6")
        buf.write("\7P\2\2\u01d6\u01d7\7g\2\2\u01d7\u01d8\7y\2\2\u01d8l\3")
        buf.write("\2\2\2\u01d9\u01da\7D\2\2\u01da\u01db\7{\2\2\u01dbn\3")
        buf.write("\2\2\2\u01dc\u01dd\7U\2\2\u01dd\u01de\7g\2\2\u01de\u01df")
        buf.write("\7n\2\2\u01df\u01e0\7h\2\2\u01e0p\3\2\2\2\u01e1\u01e2")
        buf.write("\7-\2\2\u01e2r\3\2\2\2\u01e3\u01e4\7/\2\2\u01e4t\3\2\2")
        buf.write("\2\u01e5\u01e6\7,\2\2\u01e6v\3\2\2\2\u01e7\u01e8\7\61")
        buf.write("\2\2\u01e8x\3\2\2\2\u01e9\u01ea\7\'\2\2\u01eaz\3\2\2\2")
        buf.write("\u01eb\u01ec\7#\2\2\u01ec|\3\2\2\2\u01ed\u01ee\7(\2\2")
        buf.write("\u01ee\u01ef\7(\2\2\u01ef~\3\2\2\2\u01f0\u01f1\7~\2\2")
        buf.write("\u01f1\u01f2\7~\2\2\u01f2\u0080\3\2\2\2\u01f3\u01f4\7")
        buf.write("?\2\2\u01f4\u01f5\7?\2\2\u01f5\u0082\3\2\2\2\u01f6\u01f7")
        buf.write("\7?\2\2\u01f7\u0084\3\2\2\2\u01f8\u01f9\7#\2\2\u01f9\u01fa")
        buf.write("\7?\2\2\u01fa\u0086\3\2\2\2\u01fb\u01fc\7@\2\2\u01fc\u0088")
        buf.write("\3\2\2\2\u01fd\u01fe\7@\2\2\u01fe\u01ff\7?\2\2\u01ff\u008a")
        buf.write("\3\2\2\2\u0200\u0201\7>\2\2\u0201\u008c\3\2\2\2\u0202")
        buf.write("\u0203\7>\2\2\u0203\u0204\7?\2\2\u0204\u008e\3\2\2\2\u0205")
        buf.write("\u0206\7?\2\2\u0206\u0207\7?\2\2\u0207\u0208\7\60\2\2")
        buf.write("\u0208\u0090\3\2\2\2\u0209\u020a\7-\2\2\u020a\u020b\7")
        buf.write("\60\2\2\u020b\u0092\3\2\2\2\u020c\u020d\7\60\2\2\u020d")
        buf.write("\u020e\7\60\2\2\u020e\u0094\3\2\2\2\u020f\u0210\7\60\2")
        buf.write("\2\u0210\u0096\3\2\2\2\u0211\u0212\7<\2\2\u0212\u0213")
        buf.write("\7<\2\2\u0213\u0098\3\2\2\2\u0214\u0218\t\f\2\2\u0215")
        buf.write("\u0217\t\r\2\2\u0216\u0215\3\2\2\2\u0217\u021a\3\2\2\2")
        buf.write("\u0218\u0216\3\2\2\2\u0218\u0219\3\2\2\2\u0219\u0222\3")
        buf.write("\2\2\2\u021a\u0218\3\2\2\2\u021b\u021d\5/\30\2\u021c\u021e")
        buf.write("\t\r\2\2\u021d\u021c\3\2\2\2\u021e\u021f\3\2\2\2\u021f")
        buf.write("\u021d\3\2\2\2\u021f\u0220\3\2\2\2\u0220\u0222\3\2\2\2")
        buf.write("\u0221\u0214\3\2\2\2\u0221\u021b\3\2\2\2\u0222\u009a\3")
        buf.write("\2\2\2\u0223\u0224\7%\2\2\u0224\u0225\7%\2\2\u0225\u0229")
        buf.write("\3\2\2\2\u0226\u0228\13\2\2\2\u0227\u0226\3\2\2\2\u0228")
        buf.write("\u022b\3\2\2\2\u0229\u022a\3\2\2\2\u0229\u0227\3\2\2\2")
        buf.write("\u022a\u022c\3\2\2\2\u022b\u0229\3\2\2\2\u022c\u022d\7")
        buf.write("%\2\2\u022d\u022e\7%\2\2\u022e\u022f\3\2\2\2\u022f\u0230")
        buf.write("\bN\5\2\u0230\u009c\3\2\2\2\u0231\u0232\7%\2\2\u0232\u0233")
        buf.write("\7%\2\2\u0233\u0237\3\2\2\2\u0234\u0236\13\2\2\2\u0235")
        buf.write("\u0234\3\2\2\2\u0236\u0239\3\2\2\2\u0237\u0238\3\2\2\2")
        buf.write("\u0237\u0235\3\2\2\2\u0238\u023a\3\2\2\2\u0239\u0237\3")
        buf.write("\2\2\2\u023a\u023b\bO\6\2\u023b\u009e\3\2\2\2\u023c\u023e")
        buf.write("\t\16\2\2\u023d\u023c\3\2\2\2\u023e\u023f\3\2\2\2\u023f")
        buf.write("\u023d\3\2\2\2\u023f\u0240\3\2\2\2\u0240\u0241\3\2\2\2")
        buf.write("\u0241\u0242\bP\5\2\u0242\u00a0\3\2\2\2\u0243\u0244\13")
        buf.write("\2\2\2\u0244\u0245\bQ\7\2\u0245\u00a2\3\2\2\2\33\2\u00c3")
        buf.write("\u00df\u00e5\u00ea\u00f0\u00f6\u00fb\u0101\u0108\u0112")
        buf.write("\u011c\u0127\u0131\u0135\u0137\u0158\u0163\u0166\u0218")
        buf.write("\u021f\u0221\u0229\u0237\u023f\b\3\17\2\3\20\3\3\21\4")
        buf.write("\b\2\2\3O\5\3Q\6")
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
    ILLEGAL_ESCAPE = 14
    UNCLOSE_STRING = 15
    STRING_LITERAL = 16
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
    DOTDOT = 65
    DOT = 66
    SCOPE = 67
    ID = 68
    BLOCK_COMMENT = 69
    UNTERMINATED_COMMENT = 70
    WS = 71
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
            "'>'", "'>='", "'<'", "'<='", "'==.'", "'+.'", "'..'", "'.'", 
            "'::'" ]

    symbolicNames = [ "<INVALID>",
            "BOOL_TYPE", "FLOAT_TYPE", "STRING", "INT_TYPE", "VOID_TYPE", 
            "INTEGER_LITERAL", "HEX_TYPE", "OCT_TYPE", "BIN_TYPE", "DEC_TYPE", 
            "ILLEGAL_ESCAPE", "UNCLOSE_STRING", "STRING_LITERAL", "REAL_LITERAL", 
            "VAL", "VAR", "LP", "RP", "LCB", "RCB", "LSB", "RSB", "SEMI", 
            "COMMA", "COLON", "CLASS", "BREAK", "CONTINUE", "IF", "ELSEIF", 
            "ELSE", "FOREACH", "TRUE", "FALSE", "ARRAY", "IN", "BOOLEAN", 
            "RETURN", "NULL", "CONSTRUCTOR", "DESTRUCTOR", "NEW", "BY", 
            "SELF", "ADD", "SUB", "MUL", "DIV", "MOD", "NOT", "AND", "OR", 
            "EQUAL", "ASSIGN", "NOTEQUAL", "GT", "GTE", "LT", "LTE", "EQUAL_STR", 
            "ADD_STR", "DOTDOT", "DOT", "SCOPE", "ID", "BLOCK_COMMENT", 
            "UNTERMINATED_COMMENT", "WS", "ERROR_CHAR" ]

    ruleNames = [ "T__0", "T__1", "T__2", "BOOL_TYPE", "FLOAT_TYPE", "STRING", 
                  "INT_TYPE", "VOID_TYPE", "INTEGER_LITERAL", "HEX_TYPE", 
                  "OCT_TYPE", "BIN_TYPE", "DEC_TYPE", "ILLEGAL_ESCAPE", 
                  "UNCLOSE_STRING", "STRING_LITERAL", "STR", "ESC_SEQ", 
                  "ESC_ILLEGAL", "REAL_LITERAL", "VAL", "VAR", "DOLLAR", 
                  "LP", "RP", "LCB", "RCB", "LSB", "RSB", "SEMI", "COMMA", 
                  "COLON", "EXPONENT", "DIGIT", "DEC_DIGIT", "SIGN", "CLASS", 
                  "BREAK", "CONTINUE", "IF", "ELSEIF", "ELSE", "FOREACH", 
                  "TRUE", "FALSE", "ARRAY", "IN", "BOOLEAN", "RETURN", "NULL", 
                  "CONSTRUCTOR", "DESTRUCTOR", "NEW", "BY", "SELF", "ADD", 
                  "SUB", "MUL", "DIV", "MOD", "NOT", "AND", "OR", "EQUAL", 
                  "ASSIGN", "NOTEQUAL", "GT", "GTE", "LT", "LTE", "EQUAL_STR", 
                  "ADD_STR", "DOTDOT", "DOT", "SCOPE", "ID", "BLOCK_COMMENT", 
                  "UNTERMINATED_COMMENT", "WS", "ERROR_CHAR" ]

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
        attributes = inspect.getmembers(D96Lexer, lambda a:not(inspect.isroutine(a)))
        user_defined_attr = [a for a in attributes if not(a[0].startswith('__') and a[0].endswith('__'))]
        for i in user_defined_attr:
            if tk == i[1]:
                print ("{:<30} {:<30} {:<50}".format(result.text, '|', i[0]))
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
            actions[13] = self.ILLEGAL_ESCAPE_action 
            actions[14] = self.UNCLOSE_STRING_action 
            actions[15] = self.STRING_LITERAL_action 
            actions[77] = self.UNTERMINATED_COMMENT_action 
            actions[79] = self.ERROR_CHAR_action 
            self._actions = actions
        action = self._actions.get(ruleIndex, None)
        if action is not None:
            action(localctx, actionIndex)
        else:
            raise Exception("No registered action for:" + str(ruleIndex))


    def ILLEGAL_ESCAPE_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 0:

                y = str(self.text)
                raise IllegalEscape(y[1:])

     

    def UNCLOSE_STRING_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 1:

                x = str(self.text)
                raise UncloseString(x[1:])

     

    def STRING_LITERAL_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 2:

                illegal_escape = ['\v']
                for i in self.text:
                    if i in illegal_escape:
                        y = str(self.text)
                        ill_idx = y.index(i)
                        raise IllegalEscape(y[1:ill_idx+1])
                y = str(self.text)
                self.text = y[1:-1]

     

    def UNTERMINATED_COMMENT_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 3:

                raise ErrorToken('UNTERMINATED_COMMENT')

     

    def ERROR_CHAR_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 4:

                raise ErrorToken(self.text)

     


