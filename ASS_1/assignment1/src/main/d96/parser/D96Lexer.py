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
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2K")
        buf.write("\u0242\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7")
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
        buf.write("\4\3\5\3\5\3\5\3\6\3\6\5\6\u00bd\n\6\3\7\3\7\3\7\3\7\3")
        buf.write("\7\3\7\3\b\3\b\3\b\3\b\3\b\3\b\3\b\3\t\3\t\3\t\3\t\3\n")
        buf.write("\3\n\3\n\3\n\3\n\3\13\3\13\3\13\3\13\5\13\u00d9\n\13\3")
        buf.write("\f\3\f\3\f\3\f\5\f\u00df\n\f\3\f\6\f\u00e2\n\f\r\f\16")
        buf.write("\f\u00e3\3\r\3\r\6\r\u00e8\n\r\r\r\16\r\u00e9\3\16\3\16")
        buf.write("\3\16\3\16\5\16\u00f0\n\16\3\16\6\16\u00f3\n\16\r\16\16")
        buf.write("\16\u00f4\3\17\3\17\3\17\7\17\u00fa\n\17\f\17\16\17\u00fd")
        buf.write("\13\17\5\17\u00ff\n\17\3\20\3\20\7\20\u0103\n\20\f\20")
        buf.write("\16\20\u0106\13\20\3\20\3\20\3\20\3\21\3\21\7\21\u010d")
        buf.write("\n\21\f\21\16\21\u0110\13\21\3\21\3\21\3\21\3\22\3\22")
        buf.write("\7\22\u0117\n\22\f\22\16\22\u011a\13\22\3\22\3\22\3\22")
        buf.write("\3\23\3\23\3\23\3\23\3\23\5\23\u0124\n\23\3\24\3\24\3")
        buf.write("\24\3\25\3\25\3\25\3\26\3\26\5\26\u012e\n\26\3\26\3\26")
        buf.write("\7\26\u0132\n\26\f\26\16\26\u0135\13\26\3\27\3\27\3\27")
        buf.write("\3\27\3\30\3\30\3\30\3\30\3\31\3\31\3\32\3\32\3\33\3\33")
        buf.write("\3\34\3\34\3\35\3\35\3\36\3\36\3\37\3\37\3 \3 \3!\3!\3")
        buf.write("\"\3\"\3#\3#\3#\3$\3$\5$\u0158\n$\3$\3$\3%\3%\3&\3&\3")
        buf.write("&\7&\u0161\n&\f&\16&\u0164\13&\5&\u0166\n&\3\'\3\'\3(")
        buf.write("\3(\3(\3(\3(\3(\3)\3)\3)\3)\3)\3)\3*\3*\3*\3*\3*\3*\3")
        buf.write("*\3*\3*\3+\3+\3+\3,\3,\3,\3,\3,\3,\3,\3-\3-\3-\3-\3-\3")
        buf.write(".\3.\3.\3.\3.\3.\3.\3.\3/\3/\3/\3/\3/\3\60\3\60\3\60\3")
        buf.write("\60\3\60\3\60\3\61\3\61\3\61\3\61\3\61\3\61\3\62\3\62")
        buf.write("\3\62\3\63\3\63\3\63\3\63\3\63\3\63\3\63\3\63\3\64\3\64")
        buf.write("\3\64\3\64\3\64\3\64\3\64\3\65\3\65\3\65\3\65\3\65\3\66")
        buf.write("\3\66\3\66\3\66\3\66\3\66\3\66\3\66\3\66\3\66\3\66\3\66")
        buf.write("\3\67\3\67\3\67\3\67\3\67\3\67\3\67\3\67\3\67\3\67\3\67")
        buf.write("\38\38\38\38\39\39\39\3:\3:\3:\3:\3:\3;\3;\3<\3<\3=\3")
        buf.write("=\3>\3>\3?\3?\3@\3@\3A\3A\3A\3B\3B\3B\3C\3C\3C\3D\3D\3")
        buf.write("E\3E\3E\3F\3F\3G\3G\3G\3H\3H\3I\3I\3I\3J\3J\3J\3J\3K\3")
        buf.write("K\3K\3L\3L\3M\3M\3M\3N\3N\7N\u0213\nN\fN\16N\u0216\13")
        buf.write("N\3N\3N\6N\u021a\nN\rN\16N\u021b\5N\u021e\nN\3O\3O\3O")
        buf.write("\3O\7O\u0224\nO\fO\16O\u0227\13O\3O\3O\3O\3O\3O\3P\3P")
        buf.write("\3P\3P\7P\u0232\nP\fP\16P\u0235\13P\3P\3P\3Q\6Q\u023a")
        buf.write("\nQ\rQ\16Q\u023b\3Q\3Q\3R\3R\3R\4\u0225\u0233\2S\3\3\5")
        buf.write("\4\7\5\t\6\13\7\r\b\17\t\21\n\23\13\25\f\27\r\31\16\33")
        buf.write("\17\35\20\37\21!\22#\23%\2\'\2)\2+\24-\25/\26\61\2\63")
        buf.write("\27\65\30\67\319\32;\33=\34?\35A\36C\37E G\2I\2K\2M\2")
        buf.write("O!Q\"S#U$W%Y&[\'](_)a*c+e,g-i.k/m\60o\61q\62s\63u\64w")
        buf.write("\65y\66{\67}8\1779\u0081:\u0083;\u0085<\u0087=\u0089>")
        buf.write("\u008b?\u008d@\u008fA\u0091B\u0093C\u0095D\u0097E\u0099")
        buf.write("F\u009bG\u009dH\u009fI\u00a1J\u00a3K\3\2\17\5\2\62;CH")
        buf.write("ch\3\2\62;\3\2\62\63\3\2\63;\4\2\62;aa\t\2$$^^ddhhppt")
        buf.write("tvv\4\2$$^^\n\2$$))^^ddhhppttvv\4\2GGgg\4\2--//\5\2C\\")
        buf.write("aac|\6\2\62;C\\aac|\5\2\13\f\17\17\"\"\2\u0255\2\3\3\2")
        buf.write("\2\2\2\5\3\2\2\2\2\7\3\2\2\2\2\t\3\2\2\2\2\13\3\2\2\2")
        buf.write("\2\r\3\2\2\2\2\17\3\2\2\2\2\21\3\2\2\2\2\23\3\2\2\2\2")
        buf.write("\25\3\2\2\2\2\27\3\2\2\2\2\31\3\2\2\2\2\33\3\2\2\2\2\35")
        buf.write("\3\2\2\2\2\37\3\2\2\2\2!\3\2\2\2\2#\3\2\2\2\2+\3\2\2\2")
        buf.write("\2-\3\2\2\2\2/\3\2\2\2\2\63\3\2\2\2\2\65\3\2\2\2\2\67")
        buf.write("\3\2\2\2\29\3\2\2\2\2;\3\2\2\2\2=\3\2\2\2\2?\3\2\2\2\2")
        buf.write("A\3\2\2\2\2C\3\2\2\2\2E\3\2\2\2\2O\3\2\2\2\2Q\3\2\2\2")
        buf.write("\2S\3\2\2\2\2U\3\2\2\2\2W\3\2\2\2\2Y\3\2\2\2\2[\3\2\2")
        buf.write("\2\2]\3\2\2\2\2_\3\2\2\2\2a\3\2\2\2\2c\3\2\2\2\2e\3\2")
        buf.write("\2\2\2g\3\2\2\2\2i\3\2\2\2\2k\3\2\2\2\2m\3\2\2\2\2o\3")
        buf.write("\2\2\2\2q\3\2\2\2\2s\3\2\2\2\2u\3\2\2\2\2w\3\2\2\2\2y")
        buf.write("\3\2\2\2\2{\3\2\2\2\2}\3\2\2\2\2\177\3\2\2\2\2\u0081\3")
        buf.write("\2\2\2\2\u0083\3\2\2\2\2\u0085\3\2\2\2\2\u0087\3\2\2\2")
        buf.write("\2\u0089\3\2\2\2\2\u008b\3\2\2\2\2\u008d\3\2\2\2\2\u008f")
        buf.write("\3\2\2\2\2\u0091\3\2\2\2\2\u0093\3\2\2\2\2\u0095\3\2\2")
        buf.write("\2\2\u0097\3\2\2\2\2\u0099\3\2\2\2\2\u009b\3\2\2\2\2\u009d")
        buf.write("\3\2\2\2\2\u009f\3\2\2\2\2\u00a1\3\2\2\2\2\u00a3\3\2\2")
        buf.write("\2\3\u00a5\3\2\2\2\5\u00ad\3\2\2\2\7\u00b2\3\2\2\2\t\u00b7")
        buf.write("\3\2\2\2\13\u00bc\3\2\2\2\r\u00be\3\2\2\2\17\u00c4\3\2")
        buf.write("\2\2\21\u00cb\3\2\2\2\23\u00cf\3\2\2\2\25\u00d8\3\2\2")
        buf.write("\2\27\u00de\3\2\2\2\31\u00e5\3\2\2\2\33\u00ef\3\2\2\2")
        buf.write("\35\u00fe\3\2\2\2\37\u0100\3\2\2\2!\u010a\3\2\2\2#\u0114")
        buf.write("\3\2\2\2%\u0123\3\2\2\2\'\u0125\3\2\2\2)\u0128\3\2\2\2")
        buf.write("+\u012b\3\2\2\2-\u0136\3\2\2\2/\u013a\3\2\2\2\61\u013e")
        buf.write("\3\2\2\2\63\u0140\3\2\2\2\65\u0142\3\2\2\2\67\u0144\3")
        buf.write("\2\2\29\u0146\3\2\2\2;\u0148\3\2\2\2=\u014a\3\2\2\2?\u014c")
        buf.write("\3\2\2\2A\u014e\3\2\2\2C\u0150\3\2\2\2E\u0152\3\2\2\2")
        buf.write("G\u0155\3\2\2\2I\u015b\3\2\2\2K\u0165\3\2\2\2M\u0167\3")
        buf.write("\2\2\2O\u0169\3\2\2\2Q\u016f\3\2\2\2S\u0175\3\2\2\2U\u017e")
        buf.write("\3\2\2\2W\u0181\3\2\2\2Y\u0188\3\2\2\2[\u018d\3\2\2\2")
        buf.write("]\u0195\3\2\2\2_\u019a\3\2\2\2a\u01a0\3\2\2\2c\u01a6\3")
        buf.write("\2\2\2e\u01a9\3\2\2\2g\u01b1\3\2\2\2i\u01b8\3\2\2\2k\u01bd")
        buf.write("\3\2\2\2m\u01c9\3\2\2\2o\u01d4\3\2\2\2q\u01d8\3\2\2\2")
        buf.write("s\u01db\3\2\2\2u\u01e0\3\2\2\2w\u01e2\3\2\2\2y\u01e4\3")
        buf.write("\2\2\2{\u01e6\3\2\2\2}\u01e8\3\2\2\2\177\u01ea\3\2\2\2")
        buf.write("\u0081\u01ec\3\2\2\2\u0083\u01ef\3\2\2\2\u0085\u01f2\3")
        buf.write("\2\2\2\u0087\u01f5\3\2\2\2\u0089\u01f7\3\2\2\2\u008b\u01fa")
        buf.write("\3\2\2\2\u008d\u01fc\3\2\2\2\u008f\u01ff\3\2\2\2\u0091")
        buf.write("\u0201\3\2\2\2\u0093\u0204\3\2\2\2\u0095\u0208\3\2\2\2")
        buf.write("\u0097\u020b\3\2\2\2\u0099\u020d\3\2\2\2\u009b\u021d\3")
        buf.write("\2\2\2\u009d\u021f\3\2\2\2\u009f\u022d\3\2\2\2\u00a1\u0239")
        buf.write("\3\2\2\2\u00a3\u023f\3\2\2\2\u00a5\u00a6\7R\2\2\u00a6")
        buf.write("\u00a7\7t\2\2\u00a7\u00a8\7q\2\2\u00a8\u00a9\7i\2\2\u00a9")
        buf.write("\u00aa\7t\2\2\u00aa\u00ab\7c\2\2\u00ab\u00ac\7o\2\2\u00ac")
        buf.write("\4\3\2\2\2\u00ad\u00ae\7o\2\2\u00ae\u00af\7c\2\2\u00af")
        buf.write("\u00b0\7k\2\2\u00b0\u00b1\7p\2\2\u00b1\6\3\2\2\2\u00b2")
        buf.write("\u00b3\5\u009bN\2\u00b3\u00b4\5\63\32\2\u00b4\u00b5\5")
        buf.write("\65\33\2\u00b5\u00b6\5\t\5\2\u00b6\b\3\2\2\2\u00b7\u00b8")
        buf.write("\5\67\34\2\u00b8\u00b9\59\35\2\u00b9\n\3\2\2\2\u00ba\u00bd")
        buf.write("\5]/\2\u00bb\u00bd\5_\60\2\u00bc\u00ba\3\2\2\2\u00bc\u00bb")
        buf.write("\3\2\2\2\u00bd\f\3\2\2\2\u00be\u00bf\7H\2\2\u00bf\u00c0")
        buf.write("\7n\2\2\u00c0\u00c1\7q\2\2\u00c1\u00c2\7c\2\2\u00c2\u00c3")
        buf.write("\7v\2\2\u00c3\16\3\2\2\2\u00c4\u00c5\7U\2\2\u00c5\u00c6")
        buf.write("\7v\2\2\u00c6\u00c7\7t\2\2\u00c7\u00c8\7k\2\2\u00c8\u00c9")
        buf.write("\7p\2\2\u00c9\u00ca\7i\2\2\u00ca\20\3\2\2\2\u00cb\u00cc")
        buf.write("\7K\2\2\u00cc\u00cd\7p\2\2\u00cd\u00ce\7v\2\2\u00ce\22")
        buf.write("\3\2\2\2\u00cf\u00d0\7X\2\2\u00d0\u00d1\7q\2\2\u00d1\u00d2")
        buf.write("\7k\2\2\u00d2\u00d3\7f\2\2\u00d3\24\3\2\2\2\u00d4\u00d9")
        buf.write("\5\27\f\2\u00d5\u00d9\5\31\r\2\u00d6\u00d9\5\33\16\2\u00d7")
        buf.write("\u00d9\5\35\17\2\u00d8\u00d4\3\2\2\2\u00d8\u00d5\3\2\2")
        buf.write("\2\u00d8\u00d6\3\2\2\2\u00d8\u00d7\3\2\2\2\u00d9\26\3")
        buf.write("\2\2\2\u00da\u00db\7\62\2\2\u00db\u00df\7z\2\2\u00dc\u00dd")
        buf.write("\7\62\2\2\u00dd\u00df\7Z\2\2\u00de\u00da\3\2\2\2\u00de")
        buf.write("\u00dc\3\2\2\2\u00df\u00e1\3\2\2\2\u00e0\u00e2\t\2\2\2")
        buf.write("\u00e1\u00e0\3\2\2\2\u00e2\u00e3\3\2\2\2\u00e3\u00e1\3")
        buf.write("\2\2\2\u00e3\u00e4\3\2\2\2\u00e4\30\3\2\2\2\u00e5\u00e7")
        buf.write("\7\62\2\2\u00e6\u00e8\t\3\2\2\u00e7\u00e6\3\2\2\2\u00e8")
        buf.write("\u00e9\3\2\2\2\u00e9\u00e7\3\2\2\2\u00e9\u00ea\3\2\2\2")
        buf.write("\u00ea\32\3\2\2\2\u00eb\u00ec\7\62\2\2\u00ec\u00f0\7d")
        buf.write("\2\2\u00ed\u00ee\7\62\2\2\u00ee\u00f0\7D\2\2\u00ef\u00eb")
        buf.write("\3\2\2\2\u00ef\u00ed\3\2\2\2\u00f0\u00f2\3\2\2\2\u00f1")
        buf.write("\u00f3\t\4\2\2\u00f2\u00f1\3\2\2\2\u00f3\u00f4\3\2\2\2")
        buf.write("\u00f4\u00f2\3\2\2\2\u00f4\u00f5\3\2\2\2\u00f5\34\3\2")
        buf.write("\2\2\u00f6\u00ff\t\3\2\2\u00f7\u00fb\t\5\2\2\u00f8\u00fa")
        buf.write("\t\6\2\2\u00f9\u00f8\3\2\2\2\u00fa\u00fd\3\2\2\2\u00fb")
        buf.write("\u00f9\3\2\2\2\u00fb\u00fc\3\2\2\2\u00fc\u00ff\3\2\2\2")
        buf.write("\u00fd\u00fb\3\2\2\2\u00fe\u00f6\3\2\2\2\u00fe\u00f7\3")
        buf.write("\2\2\2\u00ff\36\3\2\2\2\u0100\u0104\7$\2\2\u0101\u0103")
        buf.write("\5%\23\2\u0102\u0101\3\2\2\2\u0103\u0106\3\2\2\2\u0104")
        buf.write("\u0102\3\2\2\2\u0104\u0105\3\2\2\2\u0105\u0107\3\2\2\2")
        buf.write("\u0106\u0104\3\2\2\2\u0107\u0108\5)\25\2\u0108\u0109\b")
        buf.write("\20\2\2\u0109 \3\2\2\2\u010a\u010e\7$\2\2\u010b\u010d")
        buf.write("\5%\23\2\u010c\u010b\3\2\2\2\u010d\u0110\3\2\2\2\u010e")
        buf.write("\u010c\3\2\2\2\u010e\u010f\3\2\2\2\u010f\u0111\3\2\2\2")
        buf.write("\u0110\u010e\3\2\2\2\u0111\u0112\7\2\2\3\u0112\u0113\b")
        buf.write("\21\3\2\u0113\"\3\2\2\2\u0114\u0118\7$\2\2\u0115\u0117")
        buf.write("\5%\23\2\u0116\u0115\3\2\2\2\u0117\u011a\3\2\2\2\u0118")
        buf.write("\u0116\3\2\2\2\u0118\u0119\3\2\2\2\u0119\u011b\3\2\2\2")
        buf.write("\u011a\u0118\3\2\2\2\u011b\u011c\7$\2\2\u011c\u011d\b")
        buf.write("\22\4\2\u011d$\3\2\2\2\u011e\u011f\7^\2\2\u011f\u0124")
        buf.write("\t\7\2\2\u0120\u0124\n\b\2\2\u0121\u0122\7)\2\2\u0122")
        buf.write("\u0124\7$\2\2\u0123\u011e\3\2\2\2\u0123\u0120\3\2\2\2")
        buf.write("\u0123\u0121\3\2\2\2\u0124&\3\2\2\2\u0125\u0126\7^\2\2")
        buf.write("\u0126\u0127\t\t\2\2\u0127(\3\2\2\2\u0128\u0129\7^\2\2")
        buf.write("\u0129\u012a\n\7\2\2\u012a*\3\2\2\2\u012b\u012d\5K&\2")
        buf.write("\u012c\u012e\5\u0097L\2\u012d\u012c\3\2\2\2\u012d\u012e")
        buf.write("\3\2\2\2\u012e\u0133\3\2\2\2\u012f\u0132\5K&\2\u0130\u0132")
        buf.write("\5G$\2\u0131\u012f\3\2\2\2\u0131\u0130\3\2\2\2\u0132\u0135")
        buf.write("\3\2\2\2\u0133\u0131\3\2\2\2\u0133\u0134\3\2\2\2\u0134")
        buf.write(",\3\2\2\2\u0135\u0133\3\2\2\2\u0136\u0137\7X\2\2\u0137")
        buf.write("\u0138\7c\2\2\u0138\u0139\7n\2\2\u0139.\3\2\2\2\u013a")
        buf.write("\u013b\7X\2\2\u013b\u013c\7c\2\2\u013c\u013d\7t\2\2\u013d")
        buf.write("\60\3\2\2\2\u013e\u013f\7&\2\2\u013f\62\3\2\2\2\u0140")
        buf.write("\u0141\7*\2\2\u0141\64\3\2\2\2\u0142\u0143\7+\2\2\u0143")
        buf.write("\66\3\2\2\2\u0144\u0145\7}\2\2\u01458\3\2\2\2\u0146\u0147")
        buf.write("\7\177\2\2\u0147:\3\2\2\2\u0148\u0149\7]\2\2\u0149<\3")
        buf.write("\2\2\2\u014a\u014b\7_\2\2\u014b>\3\2\2\2\u014c\u014d\7")
        buf.write("=\2\2\u014d@\3\2\2\2\u014e\u014f\7.\2\2\u014fB\3\2\2\2")
        buf.write("\u0150\u0151\7<\2\2\u0151D\3\2\2\2\u0152\u0153\7\60\2")
        buf.write("\2\u0153\u0154\7\60\2\2\u0154F\3\2\2\2\u0155\u0157\t\n")
        buf.write("\2\2\u0156\u0158\5M\'\2\u0157\u0156\3\2\2\2\u0157\u0158")
        buf.write("\3\2\2\2\u0158\u0159\3\2\2\2\u0159\u015a\5\35\17\2\u015a")
        buf.write("H\3\2\2\2\u015b\u015c\t\3\2\2\u015cJ\3\2\2\2\u015d\u0166")
        buf.write("\t\3\2\2\u015e\u0162\t\5\2\2\u015f\u0161\t\6\2\2\u0160")
        buf.write("\u015f\3\2\2\2\u0161\u0164\3\2\2\2\u0162\u0160\3\2\2\2")
        buf.write("\u0162\u0163\3\2\2\2\u0163\u0166\3\2\2\2\u0164\u0162\3")
        buf.write("\2\2\2\u0165\u015d\3\2\2\2\u0165\u015e\3\2\2\2\u0166L")
        buf.write("\3\2\2\2\u0167\u0168\t\13\2\2\u0168N\3\2\2\2\u0169\u016a")
        buf.write("\7E\2\2\u016a\u016b\7n\2\2\u016b\u016c\7c\2\2\u016c\u016d")
        buf.write("\7u\2\2\u016d\u016e\7u\2\2\u016eP\3\2\2\2\u016f\u0170")
        buf.write("\7D\2\2\u0170\u0171\7t\2\2\u0171\u0172\7g\2\2\u0172\u0173")
        buf.write("\7c\2\2\u0173\u0174\7m\2\2\u0174R\3\2\2\2\u0175\u0176")
        buf.write("\7E\2\2\u0176\u0177\7q\2\2\u0177\u0178\7p\2\2\u0178\u0179")
        buf.write("\7v\2\2\u0179\u017a\7k\2\2\u017a\u017b\7p\2\2\u017b\u017c")
        buf.write("\7w\2\2\u017c\u017d\7g\2\2\u017dT\3\2\2\2\u017e\u017f")
        buf.write("\7K\2\2\u017f\u0180\7h\2\2\u0180V\3\2\2\2\u0181\u0182")
        buf.write("\7G\2\2\u0182\u0183\7n\2\2\u0183\u0184\7u\2\2\u0184\u0185")
        buf.write("\7g\2\2\u0185\u0186\7k\2\2\u0186\u0187\7h\2\2\u0187X\3")
        buf.write("\2\2\2\u0188\u0189\7G\2\2\u0189\u018a\7n\2\2\u018a\u018b")
        buf.write("\7u\2\2\u018b\u018c\7g\2\2\u018cZ\3\2\2\2\u018d\u018e")
        buf.write("\7H\2\2\u018e\u018f\7q\2\2\u018f\u0190\7t\2\2\u0190\u0191")
        buf.write("\7g\2\2\u0191\u0192\7c\2\2\u0192\u0193\7e\2\2\u0193\u0194")
        buf.write("\7j\2\2\u0194\\\3\2\2\2\u0195\u0196\7V\2\2\u0196\u0197")
        buf.write("\7t\2\2\u0197\u0198\7w\2\2\u0198\u0199\7g\2\2\u0199^\3")
        buf.write("\2\2\2\u019a\u019b\7H\2\2\u019b\u019c\7c\2\2\u019c\u019d")
        buf.write("\7n\2\2\u019d\u019e\7u\2\2\u019e\u019f\7g\2\2\u019f`\3")
        buf.write("\2\2\2\u01a0\u01a1\7C\2\2\u01a1\u01a2\7t\2\2\u01a2\u01a3")
        buf.write("\7t\2\2\u01a3\u01a4\7c\2\2\u01a4\u01a5\7{\2\2\u01a5b\3")
        buf.write("\2\2\2\u01a6\u01a7\7K\2\2\u01a7\u01a8\7p\2\2\u01a8d\3")
        buf.write("\2\2\2\u01a9\u01aa\7D\2\2\u01aa\u01ab\7q\2\2\u01ab\u01ac")
        buf.write("\7q\2\2\u01ac\u01ad\7n\2\2\u01ad\u01ae\7g\2\2\u01ae\u01af")
        buf.write("\7c\2\2\u01af\u01b0\7p\2\2\u01b0f\3\2\2\2\u01b1\u01b2")
        buf.write("\7T\2\2\u01b2\u01b3\7g\2\2\u01b3\u01b4\7v\2\2\u01b4\u01b5")
        buf.write("\7w\2\2\u01b5\u01b6\7t\2\2\u01b6\u01b7\7p\2\2\u01b7h\3")
        buf.write("\2\2\2\u01b8\u01b9\7P\2\2\u01b9\u01ba\7w\2\2\u01ba\u01bb")
        buf.write("\7n\2\2\u01bb\u01bc\7n\2\2\u01bcj\3\2\2\2\u01bd\u01be")
        buf.write("\7E\2\2\u01be\u01bf\7q\2\2\u01bf\u01c0\7p\2\2\u01c0\u01c1")
        buf.write("\7u\2\2\u01c1\u01c2\7v\2\2\u01c2\u01c3\7t\2\2\u01c3\u01c4")
        buf.write("\7w\2\2\u01c4\u01c5\7e\2\2\u01c5\u01c6\7v\2\2\u01c6\u01c7")
        buf.write("\7q\2\2\u01c7\u01c8\7t\2\2\u01c8l\3\2\2\2\u01c9\u01ca")
        buf.write("\7F\2\2\u01ca\u01cb\7g\2\2\u01cb\u01cc\7u\2\2\u01cc\u01cd")
        buf.write("\7v\2\2\u01cd\u01ce\7t\2\2\u01ce\u01cf\7w\2\2\u01cf\u01d0")
        buf.write("\7e\2\2\u01d0\u01d1\7v\2\2\u01d1\u01d2\7q\2\2\u01d2\u01d3")
        buf.write("\7t\2\2\u01d3n\3\2\2\2\u01d4\u01d5\7P\2\2\u01d5\u01d6")
        buf.write("\7g\2\2\u01d6\u01d7\7y\2\2\u01d7p\3\2\2\2\u01d8\u01d9")
        buf.write("\7D\2\2\u01d9\u01da\7{\2\2\u01dar\3\2\2\2\u01db\u01dc")
        buf.write("\7U\2\2\u01dc\u01dd\7g\2\2\u01dd\u01de\7n\2\2\u01de\u01df")
        buf.write("\7h\2\2\u01dft\3\2\2\2\u01e0\u01e1\7-\2\2\u01e1v\3\2\2")
        buf.write("\2\u01e2\u01e3\7/\2\2\u01e3x\3\2\2\2\u01e4\u01e5\7,\2")
        buf.write("\2\u01e5z\3\2\2\2\u01e6\u01e7\7\61\2\2\u01e7|\3\2\2\2")
        buf.write("\u01e8\u01e9\7\'\2\2\u01e9~\3\2\2\2\u01ea\u01eb\7#\2\2")
        buf.write("\u01eb\u0080\3\2\2\2\u01ec\u01ed\7(\2\2\u01ed\u01ee\7")
        buf.write("(\2\2\u01ee\u0082\3\2\2\2\u01ef\u01f0\7~\2\2\u01f0\u01f1")
        buf.write("\7~\2\2\u01f1\u0084\3\2\2\2\u01f2\u01f3\7?\2\2\u01f3\u01f4")
        buf.write("\7?\2\2\u01f4\u0086\3\2\2\2\u01f5\u01f6\7?\2\2\u01f6\u0088")
        buf.write("\3\2\2\2\u01f7\u01f8\7#\2\2\u01f8\u01f9\7?\2\2\u01f9\u008a")
        buf.write("\3\2\2\2\u01fa\u01fb\7@\2\2\u01fb\u008c\3\2\2\2\u01fc")
        buf.write("\u01fd\7@\2\2\u01fd\u01fe\7?\2\2\u01fe\u008e\3\2\2\2\u01ff")
        buf.write("\u0200\7>\2\2\u0200\u0090\3\2\2\2\u0201\u0202\7>\2\2\u0202")
        buf.write("\u0203\7?\2\2\u0203\u0092\3\2\2\2\u0204\u0205\7?\2\2\u0205")
        buf.write("\u0206\7?\2\2\u0206\u0207\7\60\2\2\u0207\u0094\3\2\2\2")
        buf.write("\u0208\u0209\7-\2\2\u0209\u020a\7\60\2\2\u020a\u0096\3")
        buf.write("\2\2\2\u020b\u020c\7\60\2\2\u020c\u0098\3\2\2\2\u020d")
        buf.write("\u020e\7<\2\2\u020e\u020f\7<\2\2\u020f\u009a\3\2\2\2\u0210")
        buf.write("\u0214\t\f\2\2\u0211\u0213\t\r\2\2\u0212\u0211\3\2\2\2")
        buf.write("\u0213\u0216\3\2\2\2\u0214\u0212\3\2\2\2\u0214\u0215\3")
        buf.write("\2\2\2\u0215\u021e\3\2\2\2\u0216\u0214\3\2\2\2\u0217\u0219")
        buf.write("\5\61\31\2\u0218\u021a\t\r\2\2\u0219\u0218\3\2\2\2\u021a")
        buf.write("\u021b\3\2\2\2\u021b\u0219\3\2\2\2\u021b\u021c\3\2\2\2")
        buf.write("\u021c\u021e\3\2\2\2\u021d\u0210\3\2\2\2\u021d\u0217\3")
        buf.write("\2\2\2\u021e\u009c\3\2\2\2\u021f\u0220\7%\2\2\u0220\u0221")
        buf.write("\7%\2\2\u0221\u0225\3\2\2\2\u0222\u0224\13\2\2\2\u0223")
        buf.write("\u0222\3\2\2\2\u0224\u0227\3\2\2\2\u0225\u0226\3\2\2\2")
        buf.write("\u0225\u0223\3\2\2\2\u0226\u0228\3\2\2\2\u0227\u0225\3")
        buf.write("\2\2\2\u0228\u0229\7%\2\2\u0229\u022a\7%\2\2\u022a\u022b")
        buf.write("\3\2\2\2\u022b\u022c\bO\5\2\u022c\u009e\3\2\2\2\u022d")
        buf.write("\u022e\7%\2\2\u022e\u022f\7%\2\2\u022f\u0233\3\2\2\2\u0230")
        buf.write("\u0232\13\2\2\2\u0231\u0230\3\2\2\2\u0232\u0235\3\2\2")
        buf.write("\2\u0233\u0234\3\2\2\2\u0233\u0231\3\2\2\2\u0234\u0236")
        buf.write("\3\2\2\2\u0235\u0233\3\2\2\2\u0236\u0237\bP\6\2\u0237")
        buf.write("\u00a0\3\2\2\2\u0238\u023a\t\16\2\2\u0239\u0238\3\2\2")
        buf.write("\2\u023a\u023b\3\2\2\2\u023b\u0239\3\2\2\2\u023b\u023c")
        buf.write("\3\2\2\2\u023c\u023d\3\2\2\2\u023d\u023e\bQ\5\2\u023e")
        buf.write("\u00a2\3\2\2\2\u023f\u0240\13\2\2\2\u0240\u0241\bR\7\2")
        buf.write("\u0241\u00a4\3\2\2\2\34\2\u00bc\u00d8\u00de\u00e3\u00e9")
        buf.write("\u00ef\u00f4\u00fb\u00fe\u0104\u010e\u0118\u0123\u012d")
        buf.write("\u0131\u0133\u0157\u0162\u0165\u0214\u021b\u021d\u0225")
        buf.write("\u0233\u023b\b\3\20\2\3\21\3\3\22\4\b\2\2\3P\5\3R\6")
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
    DOTDOT = 30
    CLASS = 31
    BREAK = 32
    CONTINUE = 33
    IF = 34
    ELSEIF = 35
    ELSE = 36
    FOREACH = 37
    TRUE = 38
    FALSE = 39
    ARRAY = 40
    IN = 41
    BOOLEAN = 42
    RETURN = 43
    NULL = 44
    CONSTRUCTOR = 45
    DESTRUCTOR = 46
    NEW = 47
    BY = 48
    SELF = 49
    ADD = 50
    SUB = 51
    MUL = 52
    DIV = 53
    MOD = 54
    NOT = 55
    AND = 56
    OR = 57
    EQUAL = 58
    ASSIGN = 59
    NOTEQUAL = 60
    GT = 61
    GTE = 62
    LT = 63
    LTE = 64
    EQUAL_STR = 65
    ADD_STR = 66
    DOT = 67
    SCOPE = 68
    ID = 69
    BLOCK_COMMENT = 70
    UNTERMINATED_COMMENT = 71
    WS = 72
    ERROR_CHAR = 73

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'Program'", "'main'", "'Float'", "'String'", "'Int'", "'Void'", 
            "'Val'", "'Var'", "'('", "')'", "'{'", "'}'", "'['", "']'", 
            "';'", "','", "':'", "'..'", "'Class'", "'Break'", "'Continue'", 
            "'If'", "'Elseif'", "'Else'", "'Foreach'", "'True'", "'False'", 
            "'Array'", "'In'", "'Boolean'", "'Return'", "'Null'", "'Constructor'", 
            "'Destructor'", "'New'", "'By'", "'Self'", "'+'", "'-'", "'*'", 
            "'/'", "'%'", "'!'", "'&&'", "'||'", "'=='", "'='", "'!='", 
            "'>'", "'>='", "'<'", "'<='", "'==.'", "'+.'", "'.'", "'::'" ]

    symbolicNames = [ "<INVALID>",
            "METHOD", "BLOCK_STATEMENT", "BOOL_TYPE", "FLOAT_TYPE", "STRING", 
            "INT_TYPE", "VOID_TYPE", "INTEGER_LITERAL", "HEX_TYPE", "OCT_TYPE", 
            "BIN_TYPE", "DEC_TYPE", "ILLEGAL_ESCAPE", "UNCLOSE_STRING", 
            "STRING_LITERAL", "REAL_LITERAL", "VAL", "VAR", "LP", "RP", 
            "LCB", "RCB", "LSB", "RSB", "SEMI", "COMMA", "COLON", "DOTDOT", 
            "CLASS", "BREAK", "CONTINUE", "IF", "ELSEIF", "ELSE", "FOREACH", 
            "TRUE", "FALSE", "ARRAY", "IN", "BOOLEAN", "RETURN", "NULL", 
            "CONSTRUCTOR", "DESTRUCTOR", "NEW", "BY", "SELF", "ADD", "SUB", 
            "MUL", "DIV", "MOD", "NOT", "AND", "OR", "EQUAL", "ASSIGN", 
            "NOTEQUAL", "GT", "GTE", "LT", "LTE", "EQUAL_STR", "ADD_STR", 
            "DOT", "SCOPE", "ID", "BLOCK_COMMENT", "UNTERMINATED_COMMENT", 
            "WS", "ERROR_CHAR" ]

    ruleNames = [ "T__0", "T__1", "METHOD", "BLOCK_STATEMENT", "BOOL_TYPE", 
                  "FLOAT_TYPE", "STRING", "INT_TYPE", "VOID_TYPE", "INTEGER_LITERAL", 
                  "HEX_TYPE", "OCT_TYPE", "BIN_TYPE", "DEC_TYPE", "ILLEGAL_ESCAPE", 
                  "UNCLOSE_STRING", "STRING_LITERAL", "STR", "ESC_SEQ", 
                  "ESC_ILLEGAL", "REAL_LITERAL", "VAL", "VAR", "DOLLAR", 
                  "LP", "RP", "LCB", "RCB", "LSB", "RSB", "SEMI", "COMMA", 
                  "COLON", "DOTDOT", "EXPONENT", "DIGIT", "DEC_DIGIT", "SIGN", 
                  "CLASS", "BREAK", "CONTINUE", "IF", "ELSEIF", "ELSE", 
                  "FOREACH", "TRUE", "FALSE", "ARRAY", "IN", "BOOLEAN", 
                  "RETURN", "NULL", "CONSTRUCTOR", "DESTRUCTOR", "NEW", 
                  "BY", "SELF", "ADD", "SUB", "MUL", "DIV", "MOD", "NOT", 
                  "AND", "OR", "EQUAL", "ASSIGN", "NOTEQUAL", "GT", "GTE", 
                  "LT", "LTE", "EQUAL_STR", "ADD_STR", "DOT", "SCOPE", "ID", 
                  "BLOCK_COMMENT", "UNTERMINATED_COMMENT", "WS", "ERROR_CHAR" ]

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
            actions[78] = self.UNTERMINATED_COMMENT_action 
            actions[80] = self.ERROR_CHAR_action 
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

                illegal_escape = ['\v', '\c']
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

     


