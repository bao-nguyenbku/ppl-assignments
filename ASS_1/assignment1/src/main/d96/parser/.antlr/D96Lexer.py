# Generated from e:\HCMUT\PRINCIPLES_OF_PROGRAMMING_LANGUAGE\ppl-assignments\ASS_1\assignment1\src\main\d96\parser\D96.g4 by ANTLR 4.8
from antlr4 import *
from io import StringIO
from typing.io import TextIO
import sys


from lexererr import *



def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2J")
        buf.write("\u023d\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7")
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
        buf.write("\2\3\2\3\2\3\3\3\3\3\3\3\3\3\3\3\4\3\4\3\4\3\4\3\4\3\5")
        buf.write("\3\5\3\5\3\6\3\6\5\6\u00bb\n\6\3\7\3\7\3\7\3\7\3\7\3\7")
        buf.write("\3\b\3\b\3\b\3\b\3\b\3\b\3\b\3\t\3\t\3\t\3\t\3\n\3\n\3")
        buf.write("\n\3\n\3\n\3\13\3\13\3\13\3\13\5\13\u00d7\n\13\3\f\3\f")
        buf.write("\3\f\3\f\5\f\u00dd\n\f\3\f\6\f\u00e0\n\f\r\f\16\f\u00e1")
        buf.write("\3\r\3\r\6\r\u00e6\n\r\r\r\16\r\u00e7\3\16\3\16\3\16\3")
        buf.write("\16\5\16\u00ee\n\16\3\16\6\16\u00f1\n\16\r\16\16\16\u00f2")
        buf.write("\3\17\3\17\3\17\7\17\u00f8\n\17\f\17\16\17\u00fb\13\17")
        buf.write("\5\17\u00fd\n\17\3\20\3\20\7\20\u0101\n\20\f\20\16\20")
        buf.write("\u0104\13\20\3\20\3\20\3\20\3\21\3\21\7\21\u010b\n\21")
        buf.write("\f\21\16\21\u010e\13\21\3\21\3\21\3\21\3\22\3\22\7\22")
        buf.write("\u0115\n\22\f\22\16\22\u0118\13\22\3\22\3\22\3\22\3\23")
        buf.write("\3\23\3\23\3\23\3\23\5\23\u0122\n\23\3\24\3\24\3\24\3")
        buf.write("\25\3\25\3\25\3\26\3\26\5\26\u012c\n\26\3\26\3\26\7\26")
        buf.write("\u0130\n\26\f\26\16\26\u0133\13\26\3\27\3\27\3\27\3\27")
        buf.write("\3\30\3\30\3\30\3\30\3\31\3\31\3\32\3\32\3\33\3\33\3\34")
        buf.write("\3\34\3\35\3\35\3\36\3\36\3\37\3\37\3 \3 \3!\3!\3\"\3")
        buf.write("\"\3#\3#\5#\u0153\n#\3#\3#\3$\3$\3%\3%\3%\7%\u015c\n%")
        buf.write("\f%\16%\u015f\13%\5%\u0161\n%\3&\3&\3\'\3\'\3\'\3\'\3")
        buf.write("\'\3\'\3(\3(\3(\3(\3(\3(\3)\3)\3)\3)\3)\3)\3)\3)\3)\3")
        buf.write("*\3*\3*\3+\3+\3+\3+\3+\3+\3+\3,\3,\3,\3,\3,\3-\3-\3-\3")
        buf.write("-\3-\3-\3-\3-\3.\3.\3.\3.\3.\3/\3/\3/\3/\3/\3/\3\60\3")
        buf.write("\60\3\60\3\60\3\60\3\60\3\61\3\61\3\61\3\62\3\62\3\62")
        buf.write("\3\62\3\62\3\62\3\62\3\62\3\63\3\63\3\63\3\63\3\63\3\63")
        buf.write("\3\63\3\64\3\64\3\64\3\64\3\64\3\65\3\65\3\65\3\65\3\65")
        buf.write("\3\65\3\65\3\65\3\65\3\65\3\65\3\65\3\66\3\66\3\66\3\66")
        buf.write("\3\66\3\66\3\66\3\66\3\66\3\66\3\66\3\67\3\67\3\67\3\67")
        buf.write("\38\38\38\39\39\39\39\39\3:\3:\3;\3;\3<\3<\3=\3=\3>\3")
        buf.write(">\3?\3?\3@\3@\3@\3A\3A\3A\3B\3B\3B\3C\3C\3D\3D\3D\3E\3")
        buf.write("E\3F\3F\3F\3G\3G\3H\3H\3H\3I\3I\3I\3I\3J\3J\3J\3K\3K\3")
        buf.write("L\3L\3L\3M\3M\7M\u020e\nM\fM\16M\u0211\13M\3M\3M\6M\u0215")
        buf.write("\nM\rM\16M\u0216\5M\u0219\nM\3N\3N\3N\3N\7N\u021f\nN\f")
        buf.write("N\16N\u0222\13N\3N\3N\3N\3N\3N\3O\3O\3O\3O\7O\u022d\n")
        buf.write("O\fO\16O\u0230\13O\3O\3O\3P\6P\u0235\nP\rP\16P\u0236\3")
        buf.write("P\3P\3Q\3Q\3Q\4\u0220\u022e\2R\3\3\5\4\7\5\t\6\13\7\r")
        buf.write("\b\17\t\21\n\23\13\25\f\27\r\31\16\33\17\35\20\37\21!")
        buf.write("\22#\23%\2\'\2)\2+\24-\25/\26\61\2\63\27\65\30\67\319")
        buf.write("\32;\33=\34?\35A\36C\37E\2G\2I\2K\2M O!Q\"S#U$W%Y&[\'")
        buf.write("](_)a*c+e,g-i.k/m\60o\61q\62s\63u\64w\65y\66{\67}8\177")
        buf.write("9\u0081:\u0083;\u0085<\u0087=\u0089>\u008b?\u008d@\u008f")
        buf.write("A\u0091B\u0093C\u0095D\u0097E\u0099F\u009bG\u009dH\u009f")
        buf.write("I\u00a1J\3\2\17\5\2\62;CHch\3\2\62;\3\2\62\63\3\2\63;")
        buf.write("\4\2\62;aa\t\2$$^^ddhhppttvv\4\2$$^^\n\2$$))^^ddhhppt")
        buf.write("tvv\4\2GGgg\4\2--//\5\2C\\aac|\6\2\62;C\\aac|\5\2\13\f")
        buf.write("\17\17\"\"\2\u0250\2\3\3\2\2\2\2\5\3\2\2\2\2\7\3\2\2\2")
        buf.write("\2\t\3\2\2\2\2\13\3\2\2\2\2\r\3\2\2\2\2\17\3\2\2\2\2\21")
        buf.write("\3\2\2\2\2\23\3\2\2\2\2\25\3\2\2\2\2\27\3\2\2\2\2\31\3")
        buf.write("\2\2\2\2\33\3\2\2\2\2\35\3\2\2\2\2\37\3\2\2\2\2!\3\2\2")
        buf.write("\2\2#\3\2\2\2\2+\3\2\2\2\2-\3\2\2\2\2/\3\2\2\2\2\63\3")
        buf.write("\2\2\2\2\65\3\2\2\2\2\67\3\2\2\2\29\3\2\2\2\2;\3\2\2\2")
        buf.write("\2=\3\2\2\2\2?\3\2\2\2\2A\3\2\2\2\2C\3\2\2\2\2M\3\2\2")
        buf.write("\2\2O\3\2\2\2\2Q\3\2\2\2\2S\3\2\2\2\2U\3\2\2\2\2W\3\2")
        buf.write("\2\2\2Y\3\2\2\2\2[\3\2\2\2\2]\3\2\2\2\2_\3\2\2\2\2a\3")
        buf.write("\2\2\2\2c\3\2\2\2\2e\3\2\2\2\2g\3\2\2\2\2i\3\2\2\2\2k")
        buf.write("\3\2\2\2\2m\3\2\2\2\2o\3\2\2\2\2q\3\2\2\2\2s\3\2\2\2\2")
        buf.write("u\3\2\2\2\2w\3\2\2\2\2y\3\2\2\2\2{\3\2\2\2\2}\3\2\2\2")
        buf.write("\2\177\3\2\2\2\2\u0081\3\2\2\2\2\u0083\3\2\2\2\2\u0085")
        buf.write("\3\2\2\2\2\u0087\3\2\2\2\2\u0089\3\2\2\2\2\u008b\3\2\2")
        buf.write("\2\2\u008d\3\2\2\2\2\u008f\3\2\2\2\2\u0091\3\2\2\2\2\u0093")
        buf.write("\3\2\2\2\2\u0095\3\2\2\2\2\u0097\3\2\2\2\2\u0099\3\2\2")
        buf.write("\2\2\u009b\3\2\2\2\2\u009d\3\2\2\2\2\u009f\3\2\2\2\2\u00a1")
        buf.write("\3\2\2\2\3\u00a3\3\2\2\2\5\u00ab\3\2\2\2\7\u00b0\3\2\2")
        buf.write("\2\t\u00b5\3\2\2\2\13\u00ba\3\2\2\2\r\u00bc\3\2\2\2\17")
        buf.write("\u00c2\3\2\2\2\21\u00c9\3\2\2\2\23\u00cd\3\2\2\2\25\u00d6")
        buf.write("\3\2\2\2\27\u00dc\3\2\2\2\31\u00e3\3\2\2\2\33\u00ed\3")
        buf.write("\2\2\2\35\u00fc\3\2\2\2\37\u00fe\3\2\2\2!\u0108\3\2\2")
        buf.write("\2#\u0112\3\2\2\2%\u0121\3\2\2\2\'\u0123\3\2\2\2)\u0126")
        buf.write("\3\2\2\2+\u0129\3\2\2\2-\u0134\3\2\2\2/\u0138\3\2\2\2")
        buf.write("\61\u013c\3\2\2\2\63\u013e\3\2\2\2\65\u0140\3\2\2\2\67")
        buf.write("\u0142\3\2\2\29\u0144\3\2\2\2;\u0146\3\2\2\2=\u0148\3")
        buf.write("\2\2\2?\u014a\3\2\2\2A\u014c\3\2\2\2C\u014e\3\2\2\2E\u0150")
        buf.write("\3\2\2\2G\u0156\3\2\2\2I\u0160\3\2\2\2K\u0162\3\2\2\2")
        buf.write("M\u0164\3\2\2\2O\u016a\3\2\2\2Q\u0170\3\2\2\2S\u0179\3")
        buf.write("\2\2\2U\u017c\3\2\2\2W\u0183\3\2\2\2Y\u0188\3\2\2\2[\u0190")
        buf.write("\3\2\2\2]\u0195\3\2\2\2_\u019b\3\2\2\2a\u01a1\3\2\2\2")
        buf.write("c\u01a4\3\2\2\2e\u01ac\3\2\2\2g\u01b3\3\2\2\2i\u01b8\3")
        buf.write("\2\2\2k\u01c4\3\2\2\2m\u01cf\3\2\2\2o\u01d3\3\2\2\2q\u01d6")
        buf.write("\3\2\2\2s\u01db\3\2\2\2u\u01dd\3\2\2\2w\u01df\3\2\2\2")
        buf.write("y\u01e1\3\2\2\2{\u01e3\3\2\2\2}\u01e5\3\2\2\2\177\u01e7")
        buf.write("\3\2\2\2\u0081\u01ea\3\2\2\2\u0083\u01ed\3\2\2\2\u0085")
        buf.write("\u01f0\3\2\2\2\u0087\u01f2\3\2\2\2\u0089\u01f5\3\2\2\2")
        buf.write("\u008b\u01f7\3\2\2\2\u008d\u01fa\3\2\2\2\u008f\u01fc\3")
        buf.write("\2\2\2\u0091\u01ff\3\2\2\2\u0093\u0203\3\2\2\2\u0095\u0206")
        buf.write("\3\2\2\2\u0097\u0208\3\2\2\2\u0099\u0218\3\2\2\2\u009b")
        buf.write("\u021a\3\2\2\2\u009d\u0228\3\2\2\2\u009f\u0234\3\2\2\2")
        buf.write("\u00a1\u023a\3\2\2\2\u00a3\u00a4\7R\2\2\u00a4\u00a5\7")
        buf.write("t\2\2\u00a5\u00a6\7q\2\2\u00a6\u00a7\7i\2\2\u00a7\u00a8")
        buf.write("\7t\2\2\u00a8\u00a9\7c\2\2\u00a9\u00aa\7o\2\2\u00aa\4")
        buf.write("\3\2\2\2\u00ab\u00ac\7o\2\2\u00ac\u00ad\7c\2\2\u00ad\u00ae")
        buf.write("\7k\2\2\u00ae\u00af\7p\2\2\u00af\6\3\2\2\2\u00b0\u00b1")
        buf.write("\5\u0099M\2\u00b1\u00b2\5\63\32\2\u00b2\u00b3\5\65\33")
        buf.write("\2\u00b3\u00b4\5\t\5\2\u00b4\b\3\2\2\2\u00b5\u00b6\5\67")
        buf.write("\34\2\u00b6\u00b7\59\35\2\u00b7\n\3\2\2\2\u00b8\u00bb")
        buf.write("\5[.\2\u00b9\u00bb\5]/\2\u00ba\u00b8\3\2\2\2\u00ba\u00b9")
        buf.write("\3\2\2\2\u00bb\f\3\2\2\2\u00bc\u00bd\7H\2\2\u00bd\u00be")
        buf.write("\7n\2\2\u00be\u00bf\7q\2\2\u00bf\u00c0\7c\2\2\u00c0\u00c1")
        buf.write("\7v\2\2\u00c1\16\3\2\2\2\u00c2\u00c3\7U\2\2\u00c3\u00c4")
        buf.write("\7v\2\2\u00c4\u00c5\7t\2\2\u00c5\u00c6\7k\2\2\u00c6\u00c7")
        buf.write("\7p\2\2\u00c7\u00c8\7i\2\2\u00c8\20\3\2\2\2\u00c9\u00ca")
        buf.write("\7K\2\2\u00ca\u00cb\7p\2\2\u00cb\u00cc\7v\2\2\u00cc\22")
        buf.write("\3\2\2\2\u00cd\u00ce\7X\2\2\u00ce\u00cf\7q\2\2\u00cf\u00d0")
        buf.write("\7k\2\2\u00d0\u00d1\7f\2\2\u00d1\24\3\2\2\2\u00d2\u00d7")
        buf.write("\5\27\f\2\u00d3\u00d7\5\31\r\2\u00d4\u00d7\5\33\16\2\u00d5")
        buf.write("\u00d7\5\35\17\2\u00d6\u00d2\3\2\2\2\u00d6\u00d3\3\2\2")
        buf.write("\2\u00d6\u00d4\3\2\2\2\u00d6\u00d5\3\2\2\2\u00d7\26\3")
        buf.write("\2\2\2\u00d8\u00d9\7\62\2\2\u00d9\u00dd\7z\2\2\u00da\u00db")
        buf.write("\7\62\2\2\u00db\u00dd\7Z\2\2\u00dc\u00d8\3\2\2\2\u00dc")
        buf.write("\u00da\3\2\2\2\u00dd\u00df\3\2\2\2\u00de\u00e0\t\2\2\2")
        buf.write("\u00df\u00de\3\2\2\2\u00e0\u00e1\3\2\2\2\u00e1\u00df\3")
        buf.write("\2\2\2\u00e1\u00e2\3\2\2\2\u00e2\30\3\2\2\2\u00e3\u00e5")
        buf.write("\7\62\2\2\u00e4\u00e6\t\3\2\2\u00e5\u00e4\3\2\2\2\u00e6")
        buf.write("\u00e7\3\2\2\2\u00e7\u00e5\3\2\2\2\u00e7\u00e8\3\2\2\2")
        buf.write("\u00e8\32\3\2\2\2\u00e9\u00ea\7\62\2\2\u00ea\u00ee\7d")
        buf.write("\2\2\u00eb\u00ec\7\62\2\2\u00ec\u00ee\7D\2\2\u00ed\u00e9")
        buf.write("\3\2\2\2\u00ed\u00eb\3\2\2\2\u00ee\u00f0\3\2\2\2\u00ef")
        buf.write("\u00f1\t\4\2\2\u00f0\u00ef\3\2\2\2\u00f1\u00f2\3\2\2\2")
        buf.write("\u00f2\u00f0\3\2\2\2\u00f2\u00f3\3\2\2\2\u00f3\34\3\2")
        buf.write("\2\2\u00f4\u00fd\t\3\2\2\u00f5\u00f9\t\5\2\2\u00f6\u00f8")
        buf.write("\t\6\2\2\u00f7\u00f6\3\2\2\2\u00f8\u00fb\3\2\2\2\u00f9")
        buf.write("\u00f7\3\2\2\2\u00f9\u00fa\3\2\2\2\u00fa\u00fd\3\2\2\2")
        buf.write("\u00fb\u00f9\3\2\2\2\u00fc\u00f4\3\2\2\2\u00fc\u00f5\3")
        buf.write("\2\2\2\u00fd\36\3\2\2\2\u00fe\u0102\7$\2\2\u00ff\u0101")
        buf.write("\5%\23\2\u0100\u00ff\3\2\2\2\u0101\u0104\3\2\2\2\u0102")
        buf.write("\u0100\3\2\2\2\u0102\u0103\3\2\2\2\u0103\u0105\3\2\2\2")
        buf.write("\u0104\u0102\3\2\2\2\u0105\u0106\5)\25\2\u0106\u0107\b")
        buf.write("\20\2\2\u0107 \3\2\2\2\u0108\u010c\7$\2\2\u0109\u010b")
        buf.write("\5%\23\2\u010a\u0109\3\2\2\2\u010b\u010e\3\2\2\2\u010c")
        buf.write("\u010a\3\2\2\2\u010c\u010d\3\2\2\2\u010d\u010f\3\2\2\2")
        buf.write("\u010e\u010c\3\2\2\2\u010f\u0110\7\2\2\3\u0110\u0111\b")
        buf.write("\21\3\2\u0111\"\3\2\2\2\u0112\u0116\7$\2\2\u0113\u0115")
        buf.write("\5%\23\2\u0114\u0113\3\2\2\2\u0115\u0118\3\2\2\2\u0116")
        buf.write("\u0114\3\2\2\2\u0116\u0117\3\2\2\2\u0117\u0119\3\2\2\2")
        buf.write("\u0118\u0116\3\2\2\2\u0119\u011a\7$\2\2\u011a\u011b\b")
        buf.write("\22\4\2\u011b$\3\2\2\2\u011c\u011d\7^\2\2\u011d\u0122")
        buf.write("\t\7\2\2\u011e\u0122\n\b\2\2\u011f\u0120\7)\2\2\u0120")
        buf.write("\u0122\7$\2\2\u0121\u011c\3\2\2\2\u0121\u011e\3\2\2\2")
        buf.write("\u0121\u011f\3\2\2\2\u0122&\3\2\2\2\u0123\u0124\7^\2\2")
        buf.write("\u0124\u0125\t\t\2\2\u0125(\3\2\2\2\u0126\u0127\7^\2\2")
        buf.write("\u0127\u0128\n\7\2\2\u0128*\3\2\2\2\u0129\u012b\5I%\2")
        buf.write("\u012a\u012c\5\u0095K\2\u012b\u012a\3\2\2\2\u012b\u012c")
        buf.write("\3\2\2\2\u012c\u0131\3\2\2\2\u012d\u0130\5I%\2\u012e\u0130")
        buf.write("\5E#\2\u012f\u012d\3\2\2\2\u012f\u012e\3\2\2\2\u0130\u0133")
        buf.write("\3\2\2\2\u0131\u012f\3\2\2\2\u0131\u0132\3\2\2\2\u0132")
        buf.write(",\3\2\2\2\u0133\u0131\3\2\2\2\u0134\u0135\7X\2\2\u0135")
        buf.write("\u0136\7c\2\2\u0136\u0137\7n\2\2\u0137.\3\2\2\2\u0138")
        buf.write("\u0139\7X\2\2\u0139\u013a\7c\2\2\u013a\u013b\7t\2\2\u013b")
        buf.write("\60\3\2\2\2\u013c\u013d\7&\2\2\u013d\62\3\2\2\2\u013e")
        buf.write("\u013f\7*\2\2\u013f\64\3\2\2\2\u0140\u0141\7+\2\2\u0141")
        buf.write("\66\3\2\2\2\u0142\u0143\7}\2\2\u01438\3\2\2\2\u0144\u0145")
        buf.write("\7\177\2\2\u0145:\3\2\2\2\u0146\u0147\7]\2\2\u0147<\3")
        buf.write("\2\2\2\u0148\u0149\7_\2\2\u0149>\3\2\2\2\u014a\u014b\7")
        buf.write("=\2\2\u014b@\3\2\2\2\u014c\u014d\7.\2\2\u014dB\3\2\2\2")
        buf.write("\u014e\u014f\7<\2\2\u014fD\3\2\2\2\u0150\u0152\t\n\2\2")
        buf.write("\u0151\u0153\5K&\2\u0152\u0151\3\2\2\2\u0152\u0153\3\2")
        buf.write("\2\2\u0153\u0154\3\2\2\2\u0154\u0155\5\35\17\2\u0155F")
        buf.write("\3\2\2\2\u0156\u0157\t\3\2\2\u0157H\3\2\2\2\u0158\u0161")
        buf.write("\t\3\2\2\u0159\u015d\t\5\2\2\u015a\u015c\t\6\2\2\u015b")
        buf.write("\u015a\3\2\2\2\u015c\u015f\3\2\2\2\u015d\u015b\3\2\2\2")
        buf.write("\u015d\u015e\3\2\2\2\u015e\u0161\3\2\2\2\u015f\u015d\3")
        buf.write("\2\2\2\u0160\u0158\3\2\2\2\u0160\u0159\3\2\2\2\u0161J")
        buf.write("\3\2\2\2\u0162\u0163\t\13\2\2\u0163L\3\2\2\2\u0164\u0165")
        buf.write("\7E\2\2\u0165\u0166\7n\2\2\u0166\u0167\7c\2\2\u0167\u0168")
        buf.write("\7u\2\2\u0168\u0169\7u\2\2\u0169N\3\2\2\2\u016a\u016b")
        buf.write("\7D\2\2\u016b\u016c\7t\2\2\u016c\u016d\7g\2\2\u016d\u016e")
        buf.write("\7c\2\2\u016e\u016f\7m\2\2\u016fP\3\2\2\2\u0170\u0171")
        buf.write("\7E\2\2\u0171\u0172\7q\2\2\u0172\u0173\7p\2\2\u0173\u0174")
        buf.write("\7v\2\2\u0174\u0175\7k\2\2\u0175\u0176\7p\2\2\u0176\u0177")
        buf.write("\7w\2\2\u0177\u0178\7g\2\2\u0178R\3\2\2\2\u0179\u017a")
        buf.write("\7K\2\2\u017a\u017b\7h\2\2\u017bT\3\2\2\2\u017c\u017d")
        buf.write("\7G\2\2\u017d\u017e\7n\2\2\u017e\u017f\7u\2\2\u017f\u0180")
        buf.write("\7g\2\2\u0180\u0181\7k\2\2\u0181\u0182\7h\2\2\u0182V\3")
        buf.write("\2\2\2\u0183\u0184\7G\2\2\u0184\u0185\7n\2\2\u0185\u0186")
        buf.write("\7u\2\2\u0186\u0187\7g\2\2\u0187X\3\2\2\2\u0188\u0189")
        buf.write("\7H\2\2\u0189\u018a\7q\2\2\u018a\u018b\7t\2\2\u018b\u018c")
        buf.write("\7g\2\2\u018c\u018d\7c\2\2\u018d\u018e\7e\2\2\u018e\u018f")
        buf.write("\7j\2\2\u018fZ\3\2\2\2\u0190\u0191\7V\2\2\u0191\u0192")
        buf.write("\7t\2\2\u0192\u0193\7w\2\2\u0193\u0194\7g\2\2\u0194\\")
        buf.write("\3\2\2\2\u0195\u0196\7H\2\2\u0196\u0197\7c\2\2\u0197\u0198")
        buf.write("\7n\2\2\u0198\u0199\7u\2\2\u0199\u019a\7g\2\2\u019a^\3")
        buf.write("\2\2\2\u019b\u019c\7C\2\2\u019c\u019d\7t\2\2\u019d\u019e")
        buf.write("\7t\2\2\u019e\u019f\7c\2\2\u019f\u01a0\7{\2\2\u01a0`\3")
        buf.write("\2\2\2\u01a1\u01a2\7K\2\2\u01a2\u01a3\7p\2\2\u01a3b\3")
        buf.write("\2\2\2\u01a4\u01a5\7D\2\2\u01a5\u01a6\7q\2\2\u01a6\u01a7")
        buf.write("\7q\2\2\u01a7\u01a8\7n\2\2\u01a8\u01a9\7g\2\2\u01a9\u01aa")
        buf.write("\7c\2\2\u01aa\u01ab\7p\2\2\u01abd\3\2\2\2\u01ac\u01ad")
        buf.write("\7T\2\2\u01ad\u01ae\7g\2\2\u01ae\u01af\7v\2\2\u01af\u01b0")
        buf.write("\7w\2\2\u01b0\u01b1\7t\2\2\u01b1\u01b2\7p\2\2\u01b2f\3")
        buf.write("\2\2\2\u01b3\u01b4\7P\2\2\u01b4\u01b5\7w\2\2\u01b5\u01b6")
        buf.write("\7n\2\2\u01b6\u01b7\7n\2\2\u01b7h\3\2\2\2\u01b8\u01b9")
        buf.write("\7E\2\2\u01b9\u01ba\7q\2\2\u01ba\u01bb\7p\2\2\u01bb\u01bc")
        buf.write("\7u\2\2\u01bc\u01bd\7v\2\2\u01bd\u01be\7t\2\2\u01be\u01bf")
        buf.write("\7w\2\2\u01bf\u01c0\7e\2\2\u01c0\u01c1\7v\2\2\u01c1\u01c2")
        buf.write("\7q\2\2\u01c2\u01c3\7t\2\2\u01c3j\3\2\2\2\u01c4\u01c5")
        buf.write("\7F\2\2\u01c5\u01c6\7g\2\2\u01c6\u01c7\7u\2\2\u01c7\u01c8")
        buf.write("\7v\2\2\u01c8\u01c9\7t\2\2\u01c9\u01ca\7w\2\2\u01ca\u01cb")
        buf.write("\7e\2\2\u01cb\u01cc\7v\2\2\u01cc\u01cd\7q\2\2\u01cd\u01ce")
        buf.write("\7t\2\2\u01cel\3\2\2\2\u01cf\u01d0\7P\2\2\u01d0\u01d1")
        buf.write("\7g\2\2\u01d1\u01d2\7y\2\2\u01d2n\3\2\2\2\u01d3\u01d4")
        buf.write("\7D\2\2\u01d4\u01d5\7{\2\2\u01d5p\3\2\2\2\u01d6\u01d7")
        buf.write("\7U\2\2\u01d7\u01d8\7g\2\2\u01d8\u01d9\7n\2\2\u01d9\u01da")
        buf.write("\7h\2\2\u01dar\3\2\2\2\u01db\u01dc\7-\2\2\u01dct\3\2\2")
        buf.write("\2\u01dd\u01de\7/\2\2\u01dev\3\2\2\2\u01df\u01e0\7,\2")
        buf.write("\2\u01e0x\3\2\2\2\u01e1\u01e2\7\61\2\2\u01e2z\3\2\2\2")
        buf.write("\u01e3\u01e4\7\'\2\2\u01e4|\3\2\2\2\u01e5\u01e6\7#\2\2")
        buf.write("\u01e6~\3\2\2\2\u01e7\u01e8\7(\2\2\u01e8\u01e9\7(\2\2")
        buf.write("\u01e9\u0080\3\2\2\2\u01ea\u01eb\7~\2\2\u01eb\u01ec\7")
        buf.write("~\2\2\u01ec\u0082\3\2\2\2\u01ed\u01ee\7?\2\2\u01ee\u01ef")
        buf.write("\7?\2\2\u01ef\u0084\3\2\2\2\u01f0\u01f1\7?\2\2\u01f1\u0086")
        buf.write("\3\2\2\2\u01f2\u01f3\7#\2\2\u01f3\u01f4\7?\2\2\u01f4\u0088")
        buf.write("\3\2\2\2\u01f5\u01f6\7@\2\2\u01f6\u008a\3\2\2\2\u01f7")
        buf.write("\u01f8\7@\2\2\u01f8\u01f9\7?\2\2\u01f9\u008c\3\2\2\2\u01fa")
        buf.write("\u01fb\7>\2\2\u01fb\u008e\3\2\2\2\u01fc\u01fd\7>\2\2\u01fd")
        buf.write("\u01fe\7?\2\2\u01fe\u0090\3\2\2\2\u01ff\u0200\7?\2\2\u0200")
        buf.write("\u0201\7?\2\2\u0201\u0202\7\60\2\2\u0202\u0092\3\2\2\2")
        buf.write("\u0203\u0204\7-\2\2\u0204\u0205\7\60\2\2\u0205\u0094\3")
        buf.write("\2\2\2\u0206\u0207\7\60\2\2\u0207\u0096\3\2\2\2\u0208")
        buf.write("\u0209\7<\2\2\u0209\u020a\7<\2\2\u020a\u0098\3\2\2\2\u020b")
        buf.write("\u020f\t\f\2\2\u020c\u020e\t\r\2\2\u020d\u020c\3\2\2\2")
        buf.write("\u020e\u0211\3\2\2\2\u020f\u020d\3\2\2\2\u020f\u0210\3")
        buf.write("\2\2\2\u0210\u0219\3\2\2\2\u0211\u020f\3\2\2\2\u0212\u0214")
        buf.write("\5\61\31\2\u0213\u0215\t\r\2\2\u0214\u0213\3\2\2\2\u0215")
        buf.write("\u0216\3\2\2\2\u0216\u0214\3\2\2\2\u0216\u0217\3\2\2\2")
        buf.write("\u0217\u0219\3\2\2\2\u0218\u020b\3\2\2\2\u0218\u0212\3")
        buf.write("\2\2\2\u0219\u009a\3\2\2\2\u021a\u021b\7%\2\2\u021b\u021c")
        buf.write("\7%\2\2\u021c\u0220\3\2\2\2\u021d\u021f\13\2\2\2\u021e")
        buf.write("\u021d\3\2\2\2\u021f\u0222\3\2\2\2\u0220\u0221\3\2\2\2")
        buf.write("\u0220\u021e\3\2\2\2\u0221\u0223\3\2\2\2\u0222\u0220\3")
        buf.write("\2\2\2\u0223\u0224\7%\2\2\u0224\u0225\7%\2\2\u0225\u0226")
        buf.write("\3\2\2\2\u0226\u0227\bN\5\2\u0227\u009c\3\2\2\2\u0228")
        buf.write("\u0229\7%\2\2\u0229\u022a\7%\2\2\u022a\u022e\3\2\2\2\u022b")
        buf.write("\u022d\13\2\2\2\u022c\u022b\3\2\2\2\u022d\u0230\3\2\2")
        buf.write("\2\u022e\u022f\3\2\2\2\u022e\u022c\3\2\2\2\u022f\u0231")
        buf.write("\3\2\2\2\u0230\u022e\3\2\2\2\u0231\u0232\bO\6\2\u0232")
        buf.write("\u009e\3\2\2\2\u0233\u0235\t\16\2\2\u0234\u0233\3\2\2")
        buf.write("\2\u0235\u0236\3\2\2\2\u0236\u0234\3\2\2\2\u0236\u0237")
        buf.write("\3\2\2\2\u0237\u0238\3\2\2\2\u0238\u0239\bP\5\2\u0239")
        buf.write("\u00a0\3\2\2\2\u023a\u023b\13\2\2\2\u023b\u023c\bQ\7\2")
        buf.write("\u023c\u00a2\3\2\2\2\34\2\u00ba\u00d6\u00dc\u00e1\u00e7")
        buf.write("\u00ed\u00f2\u00f9\u00fc\u0102\u010c\u0116\u0121\u012b")
        buf.write("\u012f\u0131\u0152\u015d\u0160\u020f\u0216\u0218\u0220")
        buf.write("\u022e\u0236\b\3\20\2\3\21\3\3\22\4\b\2\2\3O\5\3Q\6")
        return buf.getvalue()


class D96Lexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    T__0 = 1
    T__1 = 2
    METHOD = 3
    BLOCK_STATEMENT = 4
    BOOL_TYPE = 5
    FLOAT_TYPE = 6
    STRING = 7
    INT_TYPE = 8
    VOID_TYPE = 9
    INTEGER_LITERAL = 10
    HEX_TYPE = 11
    OCT_TYPE = 12
    BIN_TYPE = 13
    DEC_TYPE = 14
    ILLEGAL_ESCAPE = 15
    UNCLOSE_STRING = 16
    STRING_LITERAL = 17
    REAL_LITERAL = 18
    VAL = 19
    VAR = 20
    LP = 21
    RP = 22
    LCB = 23
    RCB = 24
    LSB = 25
    RSB = 26
    SEMI = 27
    COMMA = 28
    COLON = 29
    CLASS = 30
    BREAK = 31
    CONTINUE = 32
    IF = 33
    ELSEIF = 34
    ELSE = 35
    FOREACH = 36
    TRUE = 37
    FALSE = 38
    ARRAY = 39
    IN = 40
    BOOLEAN = 41
    RETURN = 42
    NULL = 43
    CONSTRUCTOR = 44
    DESTRUCTOR = 45
    NEW = 46
    BY = 47
    SELF = 48
    ADD = 49
    SUB = 50
    MUL = 51
    DIV = 52
    MOD = 53
    NOT = 54
    AND = 55
    OR = 56
    EQUAL = 57
    ASSIGN = 58
    NOTEQUAL = 59
    GT = 60
    GTE = 61
    LT = 62
    LTE = 63
    EQUAL_STR = 64
    ADD_STR = 65
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
            "'Program'", "'main'", "'Float'", "'String'", "'Int'", "'Void'", 
            "'Val'", "'Var'", "'('", "')'", "'{'", "'}'", "'['", "']'", 
            "';'", "','", "':'", "'Class'", "'Break'", "'Continue'", "'If'", 
            "'Elseif'", "'Else'", "'Foreach'", "'True'", "'False'", "'Array'", 
            "'In'", "'Boolean'", "'Return'", "'Null'", "'Constructor'", 
            "'Destructor'", "'New'", "'By'", "'Self'", "'+'", "'-'", "'*'", 
            "'/'", "'%'", "'!'", "'&&'", "'||'", "'=='", "'='", "'!='", 
            "'>'", "'>='", "'<'", "'<='", "'==.'", "'+.'", "'.'", "'::'" ]

    symbolicNames = [ "<INVALID>",
            "METHOD", "BLOCK_STATEMENT", "BOOL_TYPE", "FLOAT_TYPE", "STRING", 
            "INT_TYPE", "VOID_TYPE", "INTEGER_LITERAL", "HEX_TYPE", "OCT_TYPE", 
            "BIN_TYPE", "DEC_TYPE", "ILLEGAL_ESCAPE", "UNCLOSE_STRING", 
            "STRING_LITERAL", "REAL_LITERAL", "VAL", "VAR", "LP", "RP", 
            "LCB", "RCB", "LSB", "RSB", "SEMI", "COMMA", "COLON", "CLASS", 
            "BREAK", "CONTINUE", "IF", "ELSEIF", "ELSE", "FOREACH", "TRUE", 
            "FALSE", "ARRAY", "IN", "BOOLEAN", "RETURN", "NULL", "CONSTRUCTOR", 
            "DESTRUCTOR", "NEW", "BY", "SELF", "ADD", "SUB", "MUL", "DIV", 
            "MOD", "NOT", "AND", "OR", "EQUAL", "ASSIGN", "NOTEQUAL", "GT", 
            "GTE", "LT", "LTE", "EQUAL_STR", "ADD_STR", "DOT", "SCOPE", 
            "ID", "BLOCK_COMMENT", "UNTERMINATED_COMMENT", "WS", "ERROR_CHAR" ]

    ruleNames = [ "T__0", "T__1", "METHOD", "BLOCK_STATEMENT", "BOOL_TYPE", 
                  "FLOAT_TYPE", "STRING", "INT_TYPE", "VOID_TYPE", "INTEGER_LITERAL", 
                  "HEX_TYPE", "OCT_TYPE", "BIN_TYPE", "DEC_TYPE", "ILLEGAL_ESCAPE", 
                  "UNCLOSE_STRING", "STRING_LITERAL", "STR", "ESC_SEQ", 
                  "ESC_ILLEGAL", "REAL_LITERAL", "VAL", "VAR", "DOLLAR", 
                  "LP", "RP", "LCB", "RCB", "LSB", "RSB", "SEMI", "COMMA", 
                  "COLON", "EXPONENT", "DIGIT", "DEC_DIGIT", "SIGN", "CLASS", 
                  "BREAK", "CONTINUE", "IF", "ELSEIF", "ELSE", "FOREACH", 
                  "TRUE", "FALSE", "ARRAY", "IN", "BOOLEAN", "RETURN", "NULL", 
                  "CONSTRUCTOR", "DESTRUCTOR", "NEW", "BY", "SELF", "ADD", 
                  "SUB", "MUL", "DIV", "MOD", "NOT", "AND", "OR", "EQUAL", 
                  "ASSIGN", "NOTEQUAL", "GT", "GTE", "LT", "LTE", "EQUAL_STR", 
                  "ADD_STR", "DOT", "SCOPE", "ID", "BLOCK_COMMENT", "UNTERMINATED_COMMENT", 
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
        result = super().emit() # result mean for input
        # delete later
        print('--------------------------------------------------------------------------------')
        print ("{:<30} {:<30} {:<50}".format(result.text, '|', self.symbolicNames[tk-2]))
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
            actions[14] = self.ILLEGAL_ESCAPE_action 
            actions[15] = self.UNCLOSE_STRING_action 
            actions[16] = self.STRING_LITERAL_action 
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

     


