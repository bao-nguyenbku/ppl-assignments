# Generated from main/d96/parser/D96.g4 by ANTLR 4.9.2
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
    from typing import TextIO
else:
    from typing.io import TextIO


from lexererr import *



def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2J")
        buf.write("\u0238\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7")
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
        buf.write("\3\3\3\3\3\3\3\3\3\3\4\3\4\3\4\3\5\3\5\3\5\3\5\3\6\3\6")
        buf.write("\3\6\3\6\3\6\3\6\3\7\3\7\3\7\3\7\3\7\3\7\3\7\3\b\3\b\5")
        buf.write("\b\u00c4\n\b\3\t\3\t\3\t\3\t\3\t\3\n\3\n\3\n\3\n\5\n\u00cf")
        buf.write("\n\n\3\13\3\13\3\13\3\13\5\13\u00d5\n\13\3\13\6\13\u00d8")
        buf.write("\n\13\r\13\16\13\u00d9\3\f\3\f\6\f\u00de\n\f\r\f\16\f")
        buf.write("\u00df\3\r\3\r\3\r\3\r\5\r\u00e6\n\r\3\r\6\r\u00e9\n\r")
        buf.write("\r\r\16\r\u00ea\3\16\3\16\3\16\7\16\u00f0\n\16\f\16\16")
        buf.write("\16\u00f3\13\16\5\16\u00f5\n\16\3\17\3\17\7\17\u00f9\n")
        buf.write("\17\f\17\16\17\u00fc\13\17\3\17\3\17\3\17\3\20\3\20\7")
        buf.write("\20\u0103\n\20\f\20\16\20\u0106\13\20\3\20\3\20\3\20\3")
        buf.write("\21\3\21\7\21\u010d\n\21\f\21\16\21\u0110\13\21\3\21\3")
        buf.write("\21\3\21\3\22\3\22\3\22\3\22\3\22\5\22\u011a\n\22\3\23")
        buf.write("\3\23\3\23\3\24\3\24\3\24\3\25\3\25\5\25\u0124\n\25\3")
        buf.write("\25\3\25\7\25\u0128\n\25\f\25\16\25\u012b\13\25\3\26\3")
        buf.write("\26\3\26\3\26\3\27\3\27\3\27\3\27\3\30\3\30\3\31\3\31")
        buf.write("\3\32\3\32\3\33\3\33\3\34\3\34\3\35\3\35\3\36\3\36\3\37")
        buf.write("\3\37\3 \3 \3!\3!\3\"\3\"\3\"\3#\3#\5#\u014e\n#\3#\3#")
        buf.write("\3$\3$\3%\3%\3%\7%\u0157\n%\f%\16%\u015a\13%\5%\u015c")
        buf.write("\n%\3&\3&\3\'\3\'\3\'\3\'\3\'\3\'\3(\3(\3(\3(\3(\3(\3")
        buf.write(")\3)\3)\3)\3)\3)\3)\3)\3)\3*\3*\3*\3+\3+\3+\3+\3+\3+\3")
        buf.write("+\3,\3,\3,\3,\3,\3-\3-\3-\3-\3-\3-\3-\3-\3.\3.\3.\3.\3")
        buf.write(".\3/\3/\3/\3/\3/\3/\3\60\3\60\3\60\3\60\3\60\3\60\3\61")
        buf.write("\3\61\3\61\3\62\3\62\3\62\3\62\3\62\3\62\3\62\3\62\3\63")
        buf.write("\3\63\3\63\3\63\3\63\3\63\3\63\3\64\3\64\3\64\3\64\3\64")
        buf.write("\3\65\3\65\3\65\3\65\3\65\3\65\3\65\3\65\3\65\3\65\3\65")
        buf.write("\3\65\3\66\3\66\3\66\3\66\3\66\3\66\3\66\3\66\3\66\3\66")
        buf.write("\3\66\3\67\3\67\3\67\3\67\38\38\38\39\39\39\39\39\3:\3")
        buf.write(":\3;\3;\3<\3<\3=\3=\3>\3>\3?\3?\3@\3@\3@\3A\3A\3A\3B\3")
        buf.write("B\3B\3C\3C\3D\3D\3D\3E\3E\3F\3F\3F\3G\3G\3H\3H\3H\3I\3")
        buf.write("I\3I\3I\3J\3J\3J\3K\3K\3L\3L\3L\3M\3M\7M\u0209\nM\fM\16")
        buf.write("M\u020c\13M\3M\3M\6M\u0210\nM\rM\16M\u0211\5M\u0214\n")
        buf.write("M\3N\6N\u0217\nN\rN\16N\u0218\3N\3N\3O\3O\3O\3O\7O\u0221")
        buf.write("\nO\fO\16O\u0224\13O\3O\3O\3O\3O\3O\3P\3P\3P\3P\7P\u022f")
        buf.write("\nP\fP\16P\u0232\13P\3P\3P\3Q\3Q\3Q\4\u0222\u0230\2R\3")
        buf.write("\3\5\4\7\5\t\6\13\7\r\b\17\t\21\n\23\13\25\f\27\r\31\16")
        buf.write("\33\17\35\20\37\21!\22#\2%\2\'\2)\23+\24-\25/\2\61\26")
        buf.write("\63\27\65\30\67\319\32;\33=\34?\35A\36C\37E\2G\2I\2K\2")
        buf.write("M O!Q\"S#U$W%Y&[\'](_)a*c+e,g-i.k/m\60o\61q\62s\63u\64")
        buf.write("w\65y\66{\67}8\1779\u0081:\u0083;\u0085<\u0087=\u0089")
        buf.write(">\u008b?\u008d@\u008fA\u0091B\u0093C\u0095D\u0097E\u0099")
        buf.write("F\u009bG\u009dH\u009fI\u00a1J\3\2\17\5\2\62;CHch\3\2\62")
        buf.write(";\3\2\62\63\3\2\63;\4\2\62;aa\t\2$$^^ddhhppttvv\4\2$$")
        buf.write("^^\n\2$$))^^ddhhppttvv\4\2GGgg\4\2--//\5\2C\\aac|\6\2")
        buf.write("\62;C\\aac|\5\2\13\f\17\17\"\"\2\u024b\2\3\3\2\2\2\2\5")
        buf.write("\3\2\2\2\2\7\3\2\2\2\2\t\3\2\2\2\2\13\3\2\2\2\2\r\3\2")
        buf.write("\2\2\2\17\3\2\2\2\2\21\3\2\2\2\2\23\3\2\2\2\2\25\3\2\2")
        buf.write("\2\2\27\3\2\2\2\2\31\3\2\2\2\2\33\3\2\2\2\2\35\3\2\2\2")
        buf.write("\2\37\3\2\2\2\2!\3\2\2\2\2)\3\2\2\2\2+\3\2\2\2\2-\3\2")
        buf.write("\2\2\2\61\3\2\2\2\2\63\3\2\2\2\2\65\3\2\2\2\2\67\3\2\2")
        buf.write("\2\29\3\2\2\2\2;\3\2\2\2\2=\3\2\2\2\2?\3\2\2\2\2A\3\2")
        buf.write("\2\2\2C\3\2\2\2\2M\3\2\2\2\2O\3\2\2\2\2Q\3\2\2\2\2S\3")
        buf.write("\2\2\2\2U\3\2\2\2\2W\3\2\2\2\2Y\3\2\2\2\2[\3\2\2\2\2]")
        buf.write("\3\2\2\2\2_\3\2\2\2\2a\3\2\2\2\2c\3\2\2\2\2e\3\2\2\2\2")
        buf.write("g\3\2\2\2\2i\3\2\2\2\2k\3\2\2\2\2m\3\2\2\2\2o\3\2\2\2")
        buf.write("\2q\3\2\2\2\2s\3\2\2\2\2u\3\2\2\2\2w\3\2\2\2\2y\3\2\2")
        buf.write("\2\2{\3\2\2\2\2}\3\2\2\2\2\177\3\2\2\2\2\u0081\3\2\2\2")
        buf.write("\2\u0083\3\2\2\2\2\u0085\3\2\2\2\2\u0087\3\2\2\2\2\u0089")
        buf.write("\3\2\2\2\2\u008b\3\2\2\2\2\u008d\3\2\2\2\2\u008f\3\2\2")
        buf.write("\2\2\u0091\3\2\2\2\2\u0093\3\2\2\2\2\u0095\3\2\2\2\2\u0097")
        buf.write("\3\2\2\2\2\u0099\3\2\2\2\2\u009b\3\2\2\2\2\u009d\3\2\2")
        buf.write("\2\2\u009f\3\2\2\2\2\u00a1\3\2\2\2\3\u00a3\3\2\2\2\5\u00a8")
        buf.write("\3\2\2\2\7\u00ad\3\2\2\2\t\u00b0\3\2\2\2\13\u00b4\3\2")
        buf.write("\2\2\r\u00ba\3\2\2\2\17\u00c3\3\2\2\2\21\u00c5\3\2\2\2")
        buf.write("\23\u00ce\3\2\2\2\25\u00d4\3\2\2\2\27\u00db\3\2\2\2\31")
        buf.write("\u00e5\3\2\2\2\33\u00f4\3\2\2\2\35\u00f6\3\2\2\2\37\u0100")
        buf.write("\3\2\2\2!\u010a\3\2\2\2#\u0119\3\2\2\2%\u011b\3\2\2\2")
        buf.write("\'\u011e\3\2\2\2)\u0121\3\2\2\2+\u012c\3\2\2\2-\u0130")
        buf.write("\3\2\2\2/\u0134\3\2\2\2\61\u0136\3\2\2\2\63\u0138\3\2")
        buf.write("\2\2\65\u013a\3\2\2\2\67\u013c\3\2\2\29\u013e\3\2\2\2")
        buf.write(";\u0140\3\2\2\2=\u0142\3\2\2\2?\u0144\3\2\2\2A\u0146\3")
        buf.write("\2\2\2C\u0148\3\2\2\2E\u014b\3\2\2\2G\u0151\3\2\2\2I\u015b")
        buf.write("\3\2\2\2K\u015d\3\2\2\2M\u015f\3\2\2\2O\u0165\3\2\2\2")
        buf.write("Q\u016b\3\2\2\2S\u0174\3\2\2\2U\u0177\3\2\2\2W\u017e\3")
        buf.write("\2\2\2Y\u0183\3\2\2\2[\u018b\3\2\2\2]\u0190\3\2\2\2_\u0196")
        buf.write("\3\2\2\2a\u019c\3\2\2\2c\u019f\3\2\2\2e\u01a7\3\2\2\2")
        buf.write("g\u01ae\3\2\2\2i\u01b3\3\2\2\2k\u01bf\3\2\2\2m\u01ca\3")
        buf.write("\2\2\2o\u01ce\3\2\2\2q\u01d1\3\2\2\2s\u01d6\3\2\2\2u\u01d8")
        buf.write("\3\2\2\2w\u01da\3\2\2\2y\u01dc\3\2\2\2{\u01de\3\2\2\2")
        buf.write("}\u01e0\3\2\2\2\177\u01e2\3\2\2\2\u0081\u01e5\3\2\2\2")
        buf.write("\u0083\u01e8\3\2\2\2\u0085\u01eb\3\2\2\2\u0087\u01ed\3")
        buf.write("\2\2\2\u0089\u01f0\3\2\2\2\u008b\u01f2\3\2\2\2\u008d\u01f5")
        buf.write("\3\2\2\2\u008f\u01f7\3\2\2\2\u0091\u01fa\3\2\2\2\u0093")
        buf.write("\u01fe\3\2\2\2\u0095\u0201\3\2\2\2\u0097\u0203\3\2\2\2")
        buf.write("\u0099\u0213\3\2\2\2\u009b\u0216\3\2\2\2\u009d\u021c\3")
        buf.write("\2\2\2\u009f\u022a\3\2\2\2\u00a1\u0235\3\2\2\2\u00a3\u00a4")
        buf.write("\7o\2\2\u00a4\u00a5\7c\2\2\u00a5\u00a6\7k\2\2\u00a6\u00a7")
        buf.write("\7p\2\2\u00a7\4\3\2\2\2\u00a8\u00a9\5\u0099M\2\u00a9\u00aa")
        buf.write("\5\61\31\2\u00aa\u00ab\5\63\32\2\u00ab\u00ac\5\7\4\2\u00ac")
        buf.write("\6\3\2\2\2\u00ad\u00ae\5\65\33\2\u00ae\u00af\5\67\34\2")
        buf.write("\u00af\b\3\2\2\2\u00b0\u00b1\7K\2\2\u00b1\u00b2\7p\2\2")
        buf.write("\u00b2\u00b3\7v\2\2\u00b3\n\3\2\2\2\u00b4\u00b5\7H\2\2")
        buf.write("\u00b5\u00b6\7n\2\2\u00b6\u00b7\7q\2\2\u00b7\u00b8\7c")
        buf.write("\2\2\u00b8\u00b9\7v\2\2\u00b9\f\3\2\2\2\u00ba\u00bb\7")
        buf.write("U\2\2\u00bb\u00bc\7v\2\2\u00bc\u00bd\7t\2\2\u00bd\u00be")
        buf.write("\7k\2\2\u00be\u00bf\7p\2\2\u00bf\u00c0\7i\2\2\u00c0\16")
        buf.write("\3\2\2\2\u00c1\u00c4\5[.\2\u00c2\u00c4\5]/\2\u00c3\u00c1")
        buf.write("\3\2\2\2\u00c3\u00c2\3\2\2\2\u00c4\20\3\2\2\2\u00c5\u00c6")
        buf.write("\7X\2\2\u00c6\u00c7\7q\2\2\u00c7\u00c8\7k\2\2\u00c8\u00c9")
        buf.write("\7f\2\2\u00c9\22\3\2\2\2\u00ca\u00cf\5\25\13\2\u00cb\u00cf")
        buf.write("\5\27\f\2\u00cc\u00cf\5\31\r\2\u00cd\u00cf\5\33\16\2\u00ce")
        buf.write("\u00ca\3\2\2\2\u00ce\u00cb\3\2\2\2\u00ce\u00cc\3\2\2\2")
        buf.write("\u00ce\u00cd\3\2\2\2\u00cf\24\3\2\2\2\u00d0\u00d1\7\62")
        buf.write("\2\2\u00d1\u00d5\7z\2\2\u00d2\u00d3\7\62\2\2\u00d3\u00d5")
        buf.write("\7Z\2\2\u00d4\u00d0\3\2\2\2\u00d4\u00d2\3\2\2\2\u00d5")
        buf.write("\u00d7\3\2\2\2\u00d6\u00d8\t\2\2\2\u00d7\u00d6\3\2\2\2")
        buf.write("\u00d8\u00d9\3\2\2\2\u00d9\u00d7\3\2\2\2\u00d9\u00da\3")
        buf.write("\2\2\2\u00da\26\3\2\2\2\u00db\u00dd\7\62\2\2\u00dc\u00de")
        buf.write("\t\3\2\2\u00dd\u00dc\3\2\2\2\u00de\u00df\3\2\2\2\u00df")
        buf.write("\u00dd\3\2\2\2\u00df\u00e0\3\2\2\2\u00e0\30\3\2\2\2\u00e1")
        buf.write("\u00e2\7\62\2\2\u00e2\u00e6\7d\2\2\u00e3\u00e4\7\62\2")
        buf.write("\2\u00e4\u00e6\7D\2\2\u00e5\u00e1\3\2\2\2\u00e5\u00e3")
        buf.write("\3\2\2\2\u00e6\u00e8\3\2\2\2\u00e7\u00e9\t\4\2\2\u00e8")
        buf.write("\u00e7\3\2\2\2\u00e9\u00ea\3\2\2\2\u00ea\u00e8\3\2\2\2")
        buf.write("\u00ea\u00eb\3\2\2\2\u00eb\32\3\2\2\2\u00ec\u00f5\t\3")
        buf.write("\2\2\u00ed\u00f1\t\5\2\2\u00ee\u00f0\t\6\2\2\u00ef\u00ee")
        buf.write("\3\2\2\2\u00f0\u00f3\3\2\2\2\u00f1\u00ef\3\2\2\2\u00f1")
        buf.write("\u00f2\3\2\2\2\u00f2\u00f5\3\2\2\2\u00f3\u00f1\3\2\2\2")
        buf.write("\u00f4\u00ec\3\2\2\2\u00f4\u00ed\3\2\2\2\u00f5\34\3\2")
        buf.write("\2\2\u00f6\u00fa\7$\2\2\u00f7\u00f9\5#\22\2\u00f8\u00f7")
        buf.write("\3\2\2\2\u00f9\u00fc\3\2\2\2\u00fa\u00f8\3\2\2\2\u00fa")
        buf.write("\u00fb\3\2\2\2\u00fb\u00fd\3\2\2\2\u00fc\u00fa\3\2\2\2")
        buf.write("\u00fd\u00fe\7$\2\2\u00fe\u00ff\b\17\2\2\u00ff\36\3\2")
        buf.write("\2\2\u0100\u0104\7$\2\2\u0101\u0103\5#\22\2\u0102\u0101")
        buf.write("\3\2\2\2\u0103\u0106\3\2\2\2\u0104\u0102\3\2\2\2\u0104")
        buf.write("\u0105\3\2\2\2\u0105\u0107\3\2\2\2\u0106\u0104\3\2\2\2")
        buf.write("\u0107\u0108\5\'\24\2\u0108\u0109\b\20\3\2\u0109 \3\2")
        buf.write("\2\2\u010a\u010e\7$\2\2\u010b\u010d\5#\22\2\u010c\u010b")
        buf.write("\3\2\2\2\u010d\u0110\3\2\2\2\u010e\u010c\3\2\2\2\u010e")
        buf.write("\u010f\3\2\2\2\u010f\u0111\3\2\2\2\u0110\u010e\3\2\2\2")
        buf.write("\u0111\u0112\7\2\2\3\u0112\u0113\b\21\4\2\u0113\"\3\2")
        buf.write("\2\2\u0114\u0115\7^\2\2\u0115\u011a\t\7\2\2\u0116\u011a")
        buf.write("\n\b\2\2\u0117\u0118\7)\2\2\u0118\u011a\7$\2\2\u0119\u0114")
        buf.write("\3\2\2\2\u0119\u0116\3\2\2\2\u0119\u0117\3\2\2\2\u011a")
        buf.write("$\3\2\2\2\u011b\u011c\7^\2\2\u011c\u011d\t\t\2\2\u011d")
        buf.write("&\3\2\2\2\u011e\u011f\7^\2\2\u011f\u0120\n\7\2\2\u0120")
        buf.write("(\3\2\2\2\u0121\u0123\5I%\2\u0122\u0124\5\u0095K\2\u0123")
        buf.write("\u0122\3\2\2\2\u0123\u0124\3\2\2\2\u0124\u0129\3\2\2\2")
        buf.write("\u0125\u0128\5I%\2\u0126\u0128\5E#\2\u0127\u0125\3\2\2")
        buf.write("\2\u0127\u0126\3\2\2\2\u0128\u012b\3\2\2\2\u0129\u0127")
        buf.write("\3\2\2\2\u0129\u012a\3\2\2\2\u012a*\3\2\2\2\u012b\u0129")
        buf.write("\3\2\2\2\u012c\u012d\7X\2\2\u012d\u012e\7c\2\2\u012e\u012f")
        buf.write("\7n\2\2\u012f,\3\2\2\2\u0130\u0131\7X\2\2\u0131\u0132")
        buf.write("\7c\2\2\u0132\u0133\7t\2\2\u0133.\3\2\2\2\u0134\u0135")
        buf.write("\7&\2\2\u0135\60\3\2\2\2\u0136\u0137\7*\2\2\u0137\62\3")
        buf.write("\2\2\2\u0138\u0139\7+\2\2\u0139\64\3\2\2\2\u013a\u013b")
        buf.write("\7}\2\2\u013b\66\3\2\2\2\u013c\u013d\7\177\2\2\u013d8")
        buf.write("\3\2\2\2\u013e\u013f\7]\2\2\u013f:\3\2\2\2\u0140\u0141")
        buf.write("\7_\2\2\u0141<\3\2\2\2\u0142\u0143\7=\2\2\u0143>\3\2\2")
        buf.write("\2\u0144\u0145\7.\2\2\u0145@\3\2\2\2\u0146\u0147\7<\2")
        buf.write("\2\u0147B\3\2\2\2\u0148\u0149\7\60\2\2\u0149\u014a\7\60")
        buf.write("\2\2\u014aD\3\2\2\2\u014b\u014d\t\n\2\2\u014c\u014e\5")
        buf.write("K&\2\u014d\u014c\3\2\2\2\u014d\u014e\3\2\2\2\u014e\u014f")
        buf.write("\3\2\2\2\u014f\u0150\5\33\16\2\u0150F\3\2\2\2\u0151\u0152")
        buf.write("\t\3\2\2\u0152H\3\2\2\2\u0153\u015c\t\3\2\2\u0154\u0158")
        buf.write("\t\5\2\2\u0155\u0157\t\6\2\2\u0156\u0155\3\2\2\2\u0157")
        buf.write("\u015a\3\2\2\2\u0158\u0156\3\2\2\2\u0158\u0159\3\2\2\2")
        buf.write("\u0159\u015c\3\2\2\2\u015a\u0158\3\2\2\2\u015b\u0153\3")
        buf.write("\2\2\2\u015b\u0154\3\2\2\2\u015cJ\3\2\2\2\u015d\u015e")
        buf.write("\t\13\2\2\u015eL\3\2\2\2\u015f\u0160\7E\2\2\u0160\u0161")
        buf.write("\7n\2\2\u0161\u0162\7c\2\2\u0162\u0163\7u\2\2\u0163\u0164")
        buf.write("\7u\2\2\u0164N\3\2\2\2\u0165\u0166\7D\2\2\u0166\u0167")
        buf.write("\7t\2\2\u0167\u0168\7g\2\2\u0168\u0169\7c\2\2\u0169\u016a")
        buf.write("\7m\2\2\u016aP\3\2\2\2\u016b\u016c\7E\2\2\u016c\u016d")
        buf.write("\7q\2\2\u016d\u016e\7p\2\2\u016e\u016f\7v\2\2\u016f\u0170")
        buf.write("\7k\2\2\u0170\u0171\7p\2\2\u0171\u0172\7w\2\2\u0172\u0173")
        buf.write("\7g\2\2\u0173R\3\2\2\2\u0174\u0175\7K\2\2\u0175\u0176")
        buf.write("\7h\2\2\u0176T\3\2\2\2\u0177\u0178\7G\2\2\u0178\u0179")
        buf.write("\7n\2\2\u0179\u017a\7u\2\2\u017a\u017b\7g\2\2\u017b\u017c")
        buf.write("\7k\2\2\u017c\u017d\7h\2\2\u017dV\3\2\2\2\u017e\u017f")
        buf.write("\7G\2\2\u017f\u0180\7n\2\2\u0180\u0181\7u\2\2\u0181\u0182")
        buf.write("\7g\2\2\u0182X\3\2\2\2\u0183\u0184\7H\2\2\u0184\u0185")
        buf.write("\7q\2\2\u0185\u0186\7t\2\2\u0186\u0187\7g\2\2\u0187\u0188")
        buf.write("\7c\2\2\u0188\u0189\7e\2\2\u0189\u018a\7j\2\2\u018aZ\3")
        buf.write("\2\2\2\u018b\u018c\7V\2\2\u018c\u018d\7t\2\2\u018d\u018e")
        buf.write("\7w\2\2\u018e\u018f\7g\2\2\u018f\\\3\2\2\2\u0190\u0191")
        buf.write("\7H\2\2\u0191\u0192\7c\2\2\u0192\u0193\7n\2\2\u0193\u0194")
        buf.write("\7u\2\2\u0194\u0195\7g\2\2\u0195^\3\2\2\2\u0196\u0197")
        buf.write("\7C\2\2\u0197\u0198\7t\2\2\u0198\u0199\7t\2\2\u0199\u019a")
        buf.write("\7c\2\2\u019a\u019b\7{\2\2\u019b`\3\2\2\2\u019c\u019d")
        buf.write("\7K\2\2\u019d\u019e\7p\2\2\u019eb\3\2\2\2\u019f\u01a0")
        buf.write("\7D\2\2\u01a0\u01a1\7q\2\2\u01a1\u01a2\7q\2\2\u01a2\u01a3")
        buf.write("\7n\2\2\u01a3\u01a4\7g\2\2\u01a4\u01a5\7c\2\2\u01a5\u01a6")
        buf.write("\7p\2\2\u01a6d\3\2\2\2\u01a7\u01a8\7T\2\2\u01a8\u01a9")
        buf.write("\7g\2\2\u01a9\u01aa\7v\2\2\u01aa\u01ab\7w\2\2\u01ab\u01ac")
        buf.write("\7t\2\2\u01ac\u01ad\7p\2\2\u01adf\3\2\2\2\u01ae\u01af")
        buf.write("\7P\2\2\u01af\u01b0\7w\2\2\u01b0\u01b1\7n\2\2\u01b1\u01b2")
        buf.write("\7n\2\2\u01b2h\3\2\2\2\u01b3\u01b4\7E\2\2\u01b4\u01b5")
        buf.write("\7q\2\2\u01b5\u01b6\7p\2\2\u01b6\u01b7\7u\2\2\u01b7\u01b8")
        buf.write("\7v\2\2\u01b8\u01b9\7t\2\2\u01b9\u01ba\7w\2\2\u01ba\u01bb")
        buf.write("\7e\2\2\u01bb\u01bc\7v\2\2\u01bc\u01bd\7q\2\2\u01bd\u01be")
        buf.write("\7t\2\2\u01bej\3\2\2\2\u01bf\u01c0\7F\2\2\u01c0\u01c1")
        buf.write("\7g\2\2\u01c1\u01c2\7u\2\2\u01c2\u01c3\7v\2\2\u01c3\u01c4")
        buf.write("\7t\2\2\u01c4\u01c5\7w\2\2\u01c5\u01c6\7e\2\2\u01c6\u01c7")
        buf.write("\7v\2\2\u01c7\u01c8\7q\2\2\u01c8\u01c9\7t\2\2\u01c9l\3")
        buf.write("\2\2\2\u01ca\u01cb\7P\2\2\u01cb\u01cc\7g\2\2\u01cc\u01cd")
        buf.write("\7y\2\2\u01cdn\3\2\2\2\u01ce\u01cf\7D\2\2\u01cf\u01d0")
        buf.write("\7{\2\2\u01d0p\3\2\2\2\u01d1\u01d2\7U\2\2\u01d2\u01d3")
        buf.write("\7g\2\2\u01d3\u01d4\7n\2\2\u01d4\u01d5\7h\2\2\u01d5r\3")
        buf.write("\2\2\2\u01d6\u01d7\7-\2\2\u01d7t\3\2\2\2\u01d8\u01d9\7")
        buf.write("/\2\2\u01d9v\3\2\2\2\u01da\u01db\7,\2\2\u01dbx\3\2\2\2")
        buf.write("\u01dc\u01dd\7\61\2\2\u01ddz\3\2\2\2\u01de\u01df\7\'\2")
        buf.write("\2\u01df|\3\2\2\2\u01e0\u01e1\7#\2\2\u01e1~\3\2\2\2\u01e2")
        buf.write("\u01e3\7(\2\2\u01e3\u01e4\7(\2\2\u01e4\u0080\3\2\2\2\u01e5")
        buf.write("\u01e6\7~\2\2\u01e6\u01e7\7~\2\2\u01e7\u0082\3\2\2\2\u01e8")
        buf.write("\u01e9\7?\2\2\u01e9\u01ea\7?\2\2\u01ea\u0084\3\2\2\2\u01eb")
        buf.write("\u01ec\7?\2\2\u01ec\u0086\3\2\2\2\u01ed\u01ee\7#\2\2\u01ee")
        buf.write("\u01ef\7?\2\2\u01ef\u0088\3\2\2\2\u01f0\u01f1\7@\2\2\u01f1")
        buf.write("\u008a\3\2\2\2\u01f2\u01f3\7@\2\2\u01f3\u01f4\7?\2\2\u01f4")
        buf.write("\u008c\3\2\2\2\u01f5\u01f6\7>\2\2\u01f6\u008e\3\2\2\2")
        buf.write("\u01f7\u01f8\7>\2\2\u01f8\u01f9\7?\2\2\u01f9\u0090\3\2")
        buf.write("\2\2\u01fa\u01fb\7?\2\2\u01fb\u01fc\7?\2\2\u01fc\u01fd")
        buf.write("\7\60\2\2\u01fd\u0092\3\2\2\2\u01fe\u01ff\7-\2\2\u01ff")
        buf.write("\u0200\7\60\2\2\u0200\u0094\3\2\2\2\u0201\u0202\7\60\2")
        buf.write("\2\u0202\u0096\3\2\2\2\u0203\u0204\7<\2\2\u0204\u0205")
        buf.write("\7<\2\2\u0205\u0098\3\2\2\2\u0206\u020a\t\f\2\2\u0207")
        buf.write("\u0209\t\r\2\2\u0208\u0207\3\2\2\2\u0209\u020c\3\2\2\2")
        buf.write("\u020a\u0208\3\2\2\2\u020a\u020b\3\2\2\2\u020b\u0214\3")
        buf.write("\2\2\2\u020c\u020a\3\2\2\2\u020d\u020f\5/\30\2\u020e\u0210")
        buf.write("\t\r\2\2\u020f\u020e\3\2\2\2\u0210\u0211\3\2\2\2\u0211")
        buf.write("\u020f\3\2\2\2\u0211\u0212\3\2\2\2\u0212\u0214\3\2\2\2")
        buf.write("\u0213\u0206\3\2\2\2\u0213\u020d\3\2\2\2\u0214\u009a\3")
        buf.write("\2\2\2\u0215\u0217\t\16\2\2\u0216\u0215\3\2\2\2\u0217")
        buf.write("\u0218\3\2\2\2\u0218\u0216\3\2\2\2\u0218\u0219\3\2\2\2")
        buf.write("\u0219\u021a\3\2\2\2\u021a\u021b\bN\5\2\u021b\u009c\3")
        buf.write("\2\2\2\u021c\u021d\7%\2\2\u021d\u021e\7%\2\2\u021e\u0222")
        buf.write("\3\2\2\2\u021f\u0221\13\2\2\2\u0220\u021f\3\2\2\2\u0221")
        buf.write("\u0224\3\2\2\2\u0222\u0223\3\2\2\2\u0222\u0220\3\2\2\2")
        buf.write("\u0223\u0225\3\2\2\2\u0224\u0222\3\2\2\2\u0225\u0226\7")
        buf.write("%\2\2\u0226\u0227\7%\2\2\u0227\u0228\3\2\2\2\u0228\u0229")
        buf.write("\bO\5\2\u0229\u009e\3\2\2\2\u022a\u022b\7%\2\2\u022b\u022c")
        buf.write("\7%\2\2\u022c\u0230\3\2\2\2\u022d\u022f\13\2\2\2\u022e")
        buf.write("\u022d\3\2\2\2\u022f\u0232\3\2\2\2\u0230\u0231\3\2\2\2")
        buf.write("\u0230\u022e\3\2\2\2\u0231\u0233\3\2\2\2\u0232\u0230\3")
        buf.write("\2\2\2\u0233\u0234\bP\6\2\u0234\u00a0\3\2\2\2\u0235\u0236")
        buf.write("\13\2\2\2\u0236\u0237\bQ\7\2\u0237\u00a2\3\2\2\2\34\2")
        buf.write("\u00c3\u00ce\u00d4\u00d9\u00df\u00e5\u00ea\u00f1\u00f4")
        buf.write("\u00fa\u0104\u010e\u0119\u0123\u0127\u0129\u014d\u0158")
        buf.write("\u015b\u020a\u0211\u0213\u0218\u0222\u0230\b\3\17\2\3")
        buf.write("\20\3\3\21\4\b\2\2\3P\5\3Q\6")
        return buf.getvalue()


class D96Lexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    T__0 = 1
    METHOD = 2
    BLOCK_STATEMENT = 3
    INT_TYPE = 4
    FLOAT_TYPE = 5
    STRING = 6
    BOOL_TYPE = 7
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
    DOTDOT = 29
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
    WS = 69
    BLOCK_COMMENT = 70
    UNTERMINATED_COMMENT = 71
    ERROR_CHAR = 72

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'main'", "'Int'", "'Float'", "'String'", "'Void'", "'Val'", 
            "'Var'", "'('", "')'", "'{'", "'}'", "'['", "']'", "';'", "','", 
            "':'", "'..'", "'Class'", "'Break'", "'Continue'", "'If'", "'Elseif'", 
            "'Else'", "'Foreach'", "'True'", "'False'", "'Array'", "'In'", 
            "'Boolean'", "'Return'", "'Null'", "'Constructor'", "'Destructor'", 
            "'New'", "'By'", "'Self'", "'+'", "'-'", "'*'", "'/'", "'%'", 
            "'!'", "'&&'", "'||'", "'=='", "'='", "'!='", "'>'", "'>='", 
            "'<'", "'<='", "'==.'", "'+.'", "'.'", "'::'" ]

    symbolicNames = [ "<INVALID>",
            "METHOD", "BLOCK_STATEMENT", "INT_TYPE", "FLOAT_TYPE", "STRING", 
            "BOOL_TYPE", "VOID_TYPE", "INTEGER_LITERAL", "HEX_TYPE", "OCT_TYPE", 
            "BIN_TYPE", "DEC_TYPE", "STRING_LITERAL", "ILLEGAL_ESCAPE", 
            "UNCLOSE_STRING", "REAL_LITERAL", "VAL", "VAR", "LP", "RP", 
            "LCB", "RCB", "LSB", "RSB", "SEMI", "COMMA", "COLON", "DOTDOT", 
            "CLASS", "BREAK", "CONTINUE", "IF", "ELSEIF", "ELSE", "FOREACH", 
            "TRUE", "FALSE", "ARRAY", "IN", "BOOLEAN", "RETURN", "NULL", 
            "CONSTRUCTOR", "DESTRUCTOR", "NEW", "BY", "SELF", "ADD", "SUB", 
            "MUL", "DIV", "MOD", "NOT", "AND", "OR", "EQUAL", "ASSIGN", 
            "NOTEQUAL", "GT", "GTE", "LT", "LTE", "EQUAL_STR", "ADD_STR", 
            "DOT", "SCOPE", "ID", "WS", "BLOCK_COMMENT", "UNTERMINATED_COMMENT", 
            "ERROR_CHAR" ]

    ruleNames = [ "T__0", "METHOD", "BLOCK_STATEMENT", "INT_TYPE", "FLOAT_TYPE", 
                  "STRING", "BOOL_TYPE", "VOID_TYPE", "INTEGER_LITERAL", 
                  "HEX_TYPE", "OCT_TYPE", "BIN_TYPE", "DEC_TYPE", "STRING_LITERAL", 
                  "ILLEGAL_ESCAPE", "UNCLOSE_STRING", "STR", "ESC_SEQ", 
                  "ESC_ILLEGAL", "REAL_LITERAL", "VAL", "VAR", "DOLLAR", 
                  "LP", "RP", "LCB", "RCB", "LSB", "RSB", "SEMI", "COMMA", 
                  "COLON", "DOTDOT", "EXPONENT", "DIGIT", "DEC_DIGIT", "SIGN", 
                  "CLASS", "BREAK", "CONTINUE", "IF", "ELSEIF", "ELSE", 
                  "FOREACH", "TRUE", "FALSE", "ARRAY", "IN", "BOOLEAN", 
                  "RETURN", "NULL", "CONSTRUCTOR", "DESTRUCTOR", "NEW", 
                  "BY", "SELF", "ADD", "SUB", "MUL", "DIV", "MOD", "NOT", 
                  "AND", "OR", "EQUAL", "ASSIGN", "NOTEQUAL", "GT", "GTE", 
                  "LT", "LTE", "EQUAL_STR", "ADD_STR", "DOT", "SCOPE", "ID", 
                  "WS", "BLOCK_COMMENT", "UNTERMINATED_COMMENT", "ERROR_CHAR" ]

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
            actions[13] = self.STRING_LITERAL_action 
            actions[14] = self.ILLEGAL_ESCAPE_action 
            actions[15] = self.UNCLOSE_STRING_action 
            actions[78] = self.UNTERMINATED_COMMENT_action 
            actions[79] = self.ERROR_CHAR_action 
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

     


