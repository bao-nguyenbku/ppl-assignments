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
        buf.write("\u026c\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7")
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
        buf.write("\3\n\3\n\3\n\3\n\5\n\u00e2\n\n\3\13\3\13\3\f\3\f\3\f\3")
        buf.write("\f\5\f\u00ea\n\f\3\f\3\f\7\f\u00ee\n\f\f\f\16\f\u00f1")
        buf.write("\13\f\3\f\3\f\3\f\3\f\3\f\5\f\u00f8\n\f\3\f\3\f\5\f\u00fc")
        buf.write("\n\f\3\r\3\r\3\r\7\r\u0101\n\r\f\r\16\r\u0104\13\r\3\r")
        buf.write("\3\r\3\r\3\r\5\r\u010a\n\r\3\16\3\16\3\16\3\16\5\16\u0110")
        buf.write("\n\16\3\16\3\16\7\16\u0114\n\16\f\16\16\16\u0117\13\16")
        buf.write("\3\16\3\16\3\16\3\16\3\16\5\16\u011e\n\16\3\16\3\16\5")
        buf.write("\16\u0122\n\16\3\17\3\17\3\17\7\17\u0127\n\17\f\17\16")
        buf.write("\17\u012a\13\17\3\17\3\17\5\17\u012e\n\17\3\20\3\20\7")
        buf.write("\20\u0132\n\20\f\20\16\20\u0135\13\20\3\20\3\20\3\20\3")
        buf.write("\21\3\21\7\21\u013c\n\21\f\21\16\21\u013f\13\21\3\21\3")
        buf.write("\21\3\21\3\22\3\22\7\22\u0146\n\22\f\22\16\22\u0149\13")
        buf.write("\22\3\22\3\22\3\22\3\23\3\23\3\23\3\23\5\23\u0152\n\23")
        buf.write("\3\24\3\24\3\24\3\25\3\25\3\25\5\25\u015a\n\25\3\26\3")
        buf.write("\26\3\26\3\26\3\26\3\26\3\26\3\26\3\26\3\26\3\26\3\26")
        buf.write("\3\26\5\26\u0169\n\26\3\27\3\27\3\27\3\27\3\30\3\30\3")
        buf.write("\30\3\30\3\31\3\31\3\32\3\32\3\33\3\33\3\34\3\34\3\35")
        buf.write("\3\35\3\36\3\36\3\37\3\37\3 \3 \3!\3!\3\"\3\"\3#\3#\5")
        buf.write("#\u0189\n#\3#\3#\3$\3$\3%\3%\3%\7%\u0192\n%\f%\16%\u0195")
        buf.write("\13%\3%\5%\u0198\n%\3&\3&\3\'\3\'\3\'\3\'\3\'\3\'\3(\3")
        buf.write("(\3(\3(\3(\3(\3)\3)\3)\3)\3)\3)\3)\3)\3)\3*\3*\3*\3+\3")
        buf.write("+\3+\3+\3+\3+\3+\3,\3,\3,\3,\3,\3-\3-\3-\3-\3-\3-\3-\3")
        buf.write("-\3.\3.\3.\3.\3.\3/\3/\3/\3/\3/\3/\3\60\3\60\3\60\3\60")
        buf.write("\3\60\3\60\3\61\3\61\3\61\3\62\3\62\3\62\3\62\3\62\3\62")
        buf.write("\3\62\3\62\3\63\3\63\3\63\3\63\3\63\3\63\3\63\3\64\3\64")
        buf.write("\3\64\3\64\3\64\3\65\3\65\3\65\3\65\3\65\3\65\3\65\3\65")
        buf.write("\3\65\3\65\3\65\3\65\3\66\3\66\3\66\3\66\3\66\3\66\3\66")
        buf.write("\3\66\3\66\3\66\3\66\3\67\3\67\3\67\3\67\38\38\38\39\3")
        buf.write("9\39\39\39\3:\3:\3;\3;\3<\3<\3=\3=\3>\3>\3?\3?\3@\3@\3")
        buf.write("@\3A\3A\3A\3B\3B\3B\3C\3C\3D\3D\3D\3E\3E\3F\3F\3F\3G\3")
        buf.write("G\3H\3H\3H\3I\3I\3I\3I\3J\3J\3J\3K\3K\3L\3L\3L\3M\3M\3")
        buf.write("M\3N\3N\7N\u0248\nN\fN\16N\u024b\13N\3N\3N\6N\u024f\n")
        buf.write("N\rN\16N\u0250\5N\u0253\nN\3O\3O\3O\3O\7O\u0259\nO\fO")
        buf.write("\16O\u025c\13O\3O\3O\3O\3O\3O\3P\6P\u0264\nP\rP\16P\u0265")
        buf.write("\3P\3P\3Q\3Q\3Q\3\u025a\2R\3\3\5\4\7\5\t\6\13\7\r\b\17")
        buf.write("\t\21\n\23\13\25\f\27\r\31\16\33\17\35\20\37\21!\22#\23")
        buf.write("%\2\'\2)\2+\24-\25/\26\61\2\63\27\65\30\67\319\32;\33")
        buf.write("=\34?\35A\36C\37E\2G\2I\2K\2M O!Q\"S#U$W%Y&[\'](_)a*c")
        buf.write("+e,g-i.k/m\60o\61q\62s\63u\64w\65y\66{\67}8\1779\u0081")
        buf.write(":\u0083;\u0085<\u0087=\u0089>\u008b?\u008d@\u008fA\u0091")
        buf.write("B\u0093C\u0095D\u0097E\u0099F\u009bG\u009dH\u009fI\u00a1")
        buf.write("J\3\2\20\5\2\62;CHch\6\2\62;CHaach\3\2\62;\4\2\62;aa\3")
        buf.write("\2\62\63\4\2\62\63aa\6\2\n\f\16\17$$^^\t\2))^^ddhhppt")
        buf.write("tvv\4\2GGgg\3\2\63;\4\2--//\5\2C\\aac|\6\2\62;C\\aac|")
        buf.write("\5\2\13\f\17\17\"\"\2\u0283\2\3\3\2\2\2\2\5\3\2\2\2\2")
        buf.write("\7\3\2\2\2\2\t\3\2\2\2\2\13\3\2\2\2\2\r\3\2\2\2\2\17\3")
        buf.write("\2\2\2\2\21\3\2\2\2\2\23\3\2\2\2\2\25\3\2\2\2\2\27\3\2")
        buf.write("\2\2\2\31\3\2\2\2\2\33\3\2\2\2\2\35\3\2\2\2\2\37\3\2\2")
        buf.write("\2\2!\3\2\2\2\2#\3\2\2\2\2+\3\2\2\2\2-\3\2\2\2\2/\3\2")
        buf.write("\2\2\2\63\3\2\2\2\2\65\3\2\2\2\2\67\3\2\2\2\29\3\2\2\2")
        buf.write("\2;\3\2\2\2\2=\3\2\2\2\2?\3\2\2\2\2A\3\2\2\2\2C\3\2\2")
        buf.write("\2\2M\3\2\2\2\2O\3\2\2\2\2Q\3\2\2\2\2S\3\2\2\2\2U\3\2")
        buf.write("\2\2\2W\3\2\2\2\2Y\3\2\2\2\2[\3\2\2\2\2]\3\2\2\2\2_\3")
        buf.write("\2\2\2\2a\3\2\2\2\2c\3\2\2\2\2e\3\2\2\2\2g\3\2\2\2\2i")
        buf.write("\3\2\2\2\2k\3\2\2\2\2m\3\2\2\2\2o\3\2\2\2\2q\3\2\2\2\2")
        buf.write("s\3\2\2\2\2u\3\2\2\2\2w\3\2\2\2\2y\3\2\2\2\2{\3\2\2\2")
        buf.write("\2}\3\2\2\2\2\177\3\2\2\2\2\u0081\3\2\2\2\2\u0083\3\2")
        buf.write("\2\2\2\u0085\3\2\2\2\2\u0087\3\2\2\2\2\u0089\3\2\2\2\2")
        buf.write("\u008b\3\2\2\2\2\u008d\3\2\2\2\2\u008f\3\2\2\2\2\u0091")
        buf.write("\3\2\2\2\2\u0093\3\2\2\2\2\u0095\3\2\2\2\2\u0097\3\2\2")
        buf.write("\2\2\u0099\3\2\2\2\2\u009b\3\2\2\2\2\u009d\3\2\2\2\2\u009f")
        buf.write("\3\2\2\2\2\u00a1\3\2\2\2\3\u00a3\3\2\2\2\5\u00ab\3\2\2")
        buf.write("\2\7\u00b0\3\2\2\2\t\u00c3\3\2\2\2\13\u00c5\3\2\2\2\r")
        buf.write("\u00cb\3\2\2\2\17\u00d2\3\2\2\2\21\u00d6\3\2\2\2\23\u00e1")
        buf.write("\3\2\2\2\25\u00e3\3\2\2\2\27\u00fb\3\2\2\2\31\u0109\3")
        buf.write("\2\2\2\33\u0121\3\2\2\2\35\u012d\3\2\2\2\37\u012f\3\2")
        buf.write("\2\2!\u0139\3\2\2\2#\u0143\3\2\2\2%\u0151\3\2\2\2\'\u0153")
        buf.write("\3\2\2\2)\u0159\3\2\2\2+\u0168\3\2\2\2-\u016a\3\2\2\2")
        buf.write("/\u016e\3\2\2\2\61\u0172\3\2\2\2\63\u0174\3\2\2\2\65\u0176")
        buf.write("\3\2\2\2\67\u0178\3\2\2\29\u017a\3\2\2\2;\u017c\3\2\2")
        buf.write("\2=\u017e\3\2\2\2?\u0180\3\2\2\2A\u0182\3\2\2\2C\u0184")
        buf.write("\3\2\2\2E\u0186\3\2\2\2G\u018c\3\2\2\2I\u0197\3\2\2\2")
        buf.write("K\u0199\3\2\2\2M\u019b\3\2\2\2O\u01a1\3\2\2\2Q\u01a7\3")
        buf.write("\2\2\2S\u01b0\3\2\2\2U\u01b3\3\2\2\2W\u01ba\3\2\2\2Y\u01bf")
        buf.write("\3\2\2\2[\u01c7\3\2\2\2]\u01cc\3\2\2\2_\u01d2\3\2\2\2")
        buf.write("a\u01d8\3\2\2\2c\u01db\3\2\2\2e\u01e3\3\2\2\2g\u01ea\3")
        buf.write("\2\2\2i\u01ef\3\2\2\2k\u01fb\3\2\2\2m\u0206\3\2\2\2o\u020a")
        buf.write("\3\2\2\2q\u020d\3\2\2\2s\u0212\3\2\2\2u\u0214\3\2\2\2")
        buf.write("w\u0216\3\2\2\2y\u0218\3\2\2\2{\u021a\3\2\2\2}\u021c\3")
        buf.write("\2\2\2\177\u021e\3\2\2\2\u0081\u0221\3\2\2\2\u0083\u0224")
        buf.write("\3\2\2\2\u0085\u0227\3\2\2\2\u0087\u0229\3\2\2\2\u0089")
        buf.write("\u022c\3\2\2\2\u008b\u022e\3\2\2\2\u008d\u0231\3\2\2\2")
        buf.write("\u008f\u0233\3\2\2\2\u0091\u0236\3\2\2\2\u0093\u023a\3")
        buf.write("\2\2\2\u0095\u023d\3\2\2\2\u0097\u023f\3\2\2\2\u0099\u0242")
        buf.write("\3\2\2\2\u009b\u0252\3\2\2\2\u009d\u0254\3\2\2\2\u009f")
        buf.write("\u0263\3\2\2\2\u00a1\u0269\3\2\2\2\u00a3\u00a4\7R\2\2")
        buf.write("\u00a4\u00a5\7t\2\2\u00a5\u00a6\7q\2\2\u00a6\u00a7\7i")
        buf.write("\2\2\u00a7\u00a8\7t\2\2\u00a8\u00a9\7c\2\2\u00a9\u00aa")
        buf.write("\7o\2\2\u00aa\4\3\2\2\2\u00ab\u00ac\7o\2\2\u00ac\u00ad")
        buf.write("\7c\2\2\u00ad\u00ae\7k\2\2\u00ae\u00af\7p\2\2\u00af\6")
        buf.write("\3\2\2\2\u00b0\u00b1\7c\2\2\u00b1\u00b2\7u\2\2\u00b2\u00b3")
        buf.write("\7u\2\2\u00b3\u00b4\7k\2\2\u00b4\u00b5\7i\2\2\u00b5\u00b6")
        buf.write("\7p\2\2\u00b6\u00b7\7a\2\2\u00b7\u00b8\7u\2\2\u00b8\u00b9")
        buf.write("\7v\2\2\u00b9\u00ba\7c\2\2\u00ba\u00bb\7v\2\2\u00bb\u00bc")
        buf.write("\7g\2\2\u00bc\u00bd\7o\2\2\u00bd\u00be\7g\2\2\u00be\u00bf")
        buf.write("\7p\2\2\u00bf\u00c0\7v\2\2\u00c0\b\3\2\2\2\u00c1\u00c4")
        buf.write("\5[.\2\u00c2\u00c4\5]/\2\u00c3\u00c1\3\2\2\2\u00c3\u00c2")
        buf.write("\3\2\2\2\u00c4\n\3\2\2\2\u00c5\u00c6\7H\2\2\u00c6\u00c7")
        buf.write("\7n\2\2\u00c7\u00c8\7q\2\2\u00c8\u00c9\7c\2\2\u00c9\u00ca")
        buf.write("\7v\2\2\u00ca\f\3\2\2\2\u00cb\u00cc\7U\2\2\u00cc\u00cd")
        buf.write("\7v\2\2\u00cd\u00ce\7t\2\2\u00ce\u00cf\7k\2\2\u00cf\u00d0")
        buf.write("\7p\2\2\u00d0\u00d1\7i\2\2\u00d1\16\3\2\2\2\u00d2\u00d3")
        buf.write("\7K\2\2\u00d3\u00d4\7p\2\2\u00d4\u00d5\7v\2\2\u00d5\20")
        buf.write("\3\2\2\2\u00d6\u00d7\7X\2\2\u00d7\u00d8\7q\2\2\u00d8\u00d9")
        buf.write("\7k\2\2\u00d9\u00da\7f\2\2\u00da\22\3\2\2\2\u00db\u00e2")
        buf.write("\5\27\f\2\u00dc\u00e2\5\31\r\2\u00dd\u00e2\5\33\16\2\u00de")
        buf.write("\u00df\5\35\17\2\u00df\u00e0\b\n\2\2\u00e0\u00e2\3\2\2")
        buf.write("\2\u00e1\u00db\3\2\2\2\u00e1\u00dc\3\2\2\2\u00e1\u00dd")
        buf.write("\3\2\2\2\u00e1\u00de\3\2\2\2\u00e2\24\3\2\2\2\u00e3\u00e4")
        buf.write("\5\35\17\2\u00e4\26\3\2\2\2\u00e5\u00e6\7\62\2\2\u00e6")
        buf.write("\u00ea\7z\2\2\u00e7\u00e8\7\62\2\2\u00e8\u00ea\7Z\2\2")
        buf.write("\u00e9\u00e5\3\2\2\2\u00e9\u00e7\3\2\2\2\u00ea\u00eb\3")
        buf.write("\2\2\2\u00eb\u00ef\t\2\2\2\u00ec\u00ee\t\3\2\2\u00ed\u00ec")
        buf.write("\3\2\2\2\u00ee\u00f1\3\2\2\2\u00ef\u00ed\3\2\2\2\u00ef")
        buf.write("\u00f0\3\2\2\2\u00f0\u00f2\3\2\2\2\u00f1\u00ef\3\2\2\2")
        buf.write("\u00f2\u00fc\t\3\2\2\u00f3\u00f4\7\62\2\2\u00f4\u00f8")
        buf.write("\7z\2\2\u00f5\u00f6\7\62\2\2\u00f6\u00f8\7Z\2\2\u00f7")
        buf.write("\u00f3\3\2\2\2\u00f7\u00f5\3\2\2\2\u00f8\u00f9\3\2\2\2")
        buf.write("\u00f9\u00fa\t\2\2\2\u00fa\u00fc\b\f\3\2\u00fb\u00e9\3")
        buf.write("\2\2\2\u00fb\u00f7\3\2\2\2\u00fc\30\3\2\2\2\u00fd\u00fe")
        buf.write("\7\62\2\2\u00fe\u0102\t\4\2\2\u00ff\u0101\t\5\2\2\u0100")
        buf.write("\u00ff\3\2\2\2\u0101\u0104\3\2\2\2\u0102\u0100\3\2\2\2")
        buf.write("\u0102\u0103\3\2\2\2\u0103\u0105\3\2\2\2\u0104\u0102\3")
        buf.write("\2\2\2\u0105\u010a\t\4\2\2\u0106\u0107\7\62\2\2\u0107")
        buf.write("\u0108\t\4\2\2\u0108\u010a\b\r\4\2\u0109\u00fd\3\2\2\2")
        buf.write("\u0109\u0106\3\2\2\2\u010a\32\3\2\2\2\u010b\u010c\7\62")
        buf.write("\2\2\u010c\u0110\7d\2\2\u010d\u010e\7\62\2\2\u010e\u0110")
        buf.write("\7D\2\2\u010f\u010b\3\2\2\2\u010f\u010d\3\2\2\2\u0110")
        buf.write("\u0111\3\2\2\2\u0111\u0115\t\6\2\2\u0112\u0114\t\7\2\2")
        buf.write("\u0113\u0112\3\2\2\2\u0114\u0117\3\2\2\2\u0115\u0113\3")
        buf.write("\2\2\2\u0115\u0116\3\2\2\2\u0116\u0118\3\2\2\2\u0117\u0115")
        buf.write("\3\2\2\2\u0118\u0122\t\6\2\2\u0119\u011a\7\62\2\2\u011a")
        buf.write("\u011e\7d\2\2\u011b\u011c\7\62\2\2\u011c\u011e\7D\2\2")
        buf.write("\u011d\u0119\3\2\2\2\u011d\u011b\3\2\2\2\u011e\u011f\3")
        buf.write("\2\2\2\u011f\u0120\t\6\2\2\u0120\u0122\b\16\5\2\u0121")
        buf.write("\u010f\3\2\2\2\u0121\u011d\3\2\2\2\u0122\34\3\2\2\2\u0123")
        buf.write("\u012e\t\4\2\2\u0124\u0128\t\4\2\2\u0125\u0127\t\5\2\2")
        buf.write("\u0126\u0125\3\2\2\2\u0127\u012a\3\2\2\2\u0128\u0126\3")
        buf.write("\2\2\2\u0128\u0129\3\2\2\2\u0129\u012b\3\2\2\2\u012a\u0128")
        buf.write("\3\2\2\2\u012b\u012c\t\4\2\2\u012c\u012e\b\17\6\2\u012d")
        buf.write("\u0123\3\2\2\2\u012d\u0124\3\2\2\2\u012e\36\3\2\2\2\u012f")
        buf.write("\u0133\7$\2\2\u0130\u0132\5%\23\2\u0131\u0130\3\2\2\2")
        buf.write("\u0132\u0135\3\2\2\2\u0133\u0131\3\2\2\2\u0133\u0134\3")
        buf.write("\2\2\2\u0134\u0136\3\2\2\2\u0135\u0133\3\2\2\2\u0136\u0137")
        buf.write("\7$\2\2\u0137\u0138\b\20\7\2\u0138 \3\2\2\2\u0139\u013d")
        buf.write("\7$\2\2\u013a\u013c\5%\23\2\u013b\u013a\3\2\2\2\u013c")
        buf.write("\u013f\3\2\2\2\u013d\u013b\3\2\2\2\u013d\u013e\3\2\2\2")
        buf.write("\u013e\u0140\3\2\2\2\u013f\u013d\3\2\2\2\u0140\u0141\5")
        buf.write(")\25\2\u0141\u0142\b\21\b\2\u0142\"\3\2\2\2\u0143\u0147")
        buf.write("\7$\2\2\u0144\u0146\5%\23\2\u0145\u0144\3\2\2\2\u0146")
        buf.write("\u0149\3\2\2\2\u0147\u0145\3\2\2\2\u0147\u0148\3\2\2\2")
        buf.write("\u0148\u014a\3\2\2\2\u0149\u0147\3\2\2\2\u014a\u014b\7")
        buf.write("\2\2\3\u014b\u014c\b\22\t\2\u014c$\3\2\2\2\u014d\u014e")
        buf.write("\7)\2\2\u014e\u0152\7$\2\2\u014f\u0152\n\b\2\2\u0150\u0152")
        buf.write("\5\'\24\2\u0151\u014d\3\2\2\2\u0151\u014f\3\2\2\2\u0151")
        buf.write("\u0150\3\2\2\2\u0152&\3\2\2\2\u0153\u0154\7^\2\2\u0154")
        buf.write("\u0155\t\t\2\2\u0155(\3\2\2\2\u0156\u0157\7^\2\2\u0157")
        buf.write("\u015a\n\t\2\2\u0158\u015a\7^\2\2\u0159\u0156\3\2\2\2")
        buf.write("\u0159\u0158\3\2\2\2\u015a*\3\2\2\2\u015b\u015c\5\35\17")
        buf.write("\2\u015c\u015d\5\u0095K\2\u015d\u015e\5\35\17\2\u015e")
        buf.write("\u0169\3\2\2\2\u015f\u0160\5\35\17\2\u0160\u0161\5E#\2")
        buf.write("\u0161\u0169\3\2\2\2\u0162\u0163\5\35\17\2\u0163\u0164")
        buf.write("\5\u0095K\2\u0164\u0165\5\35\17\2\u0165\u0166\5E#\2\u0166")
        buf.write("\u0167\b\26\n\2\u0167\u0169\3\2\2\2\u0168\u015b\3\2\2")
        buf.write("\2\u0168\u015f\3\2\2\2\u0168\u0162\3\2\2\2\u0169,\3\2")
        buf.write("\2\2\u016a\u016b\7X\2\2\u016b\u016c\7c\2\2\u016c\u016d")
        buf.write("\7n\2\2\u016d.\3\2\2\2\u016e\u016f\7X\2\2\u016f\u0170")
        buf.write("\7c\2\2\u0170\u0171\7t\2\2\u0171\60\3\2\2\2\u0172\u0173")
        buf.write("\7&\2\2\u0173\62\3\2\2\2\u0174\u0175\7*\2\2\u0175\64\3")
        buf.write("\2\2\2\u0176\u0177\7+\2\2\u0177\66\3\2\2\2\u0178\u0179")
        buf.write("\7}\2\2\u01798\3\2\2\2\u017a\u017b\7\177\2\2\u017b:\3")
        buf.write("\2\2\2\u017c\u017d\7]\2\2\u017d<\3\2\2\2\u017e\u017f\7")
        buf.write("_\2\2\u017f>\3\2\2\2\u0180\u0181\7=\2\2\u0181@\3\2\2\2")
        buf.write("\u0182\u0183\7.\2\2\u0183B\3\2\2\2\u0184\u0185\7<\2\2")
        buf.write("\u0185D\3\2\2\2\u0186\u0188\t\n\2\2\u0187\u0189\5K&\2")
        buf.write("\u0188\u0187\3\2\2\2\u0188\u0189\3\2\2\2\u0189\u018a\3")
        buf.write("\2\2\2\u018a\u018b\5\35\17\2\u018bF\3\2\2\2\u018c\u018d")
        buf.write("\t\4\2\2\u018dH\3\2\2\2\u018e\u0198\t\4\2\2\u018f\u0193")
        buf.write("\t\13\2\2\u0190\u0192\t\5\2\2\u0191\u0190\3\2\2\2\u0192")
        buf.write("\u0195\3\2\2\2\u0193\u0191\3\2\2\2\u0193\u0194\3\2\2\2")
        buf.write("\u0194\u0196\3\2\2\2\u0195\u0193\3\2\2\2\u0196\u0198\t")
        buf.write("\4\2\2\u0197\u018e\3\2\2\2\u0197\u018f\3\2\2\2\u0198J")
        buf.write("\3\2\2\2\u0199\u019a\t\f\2\2\u019aL\3\2\2\2\u019b\u019c")
        buf.write("\7E\2\2\u019c\u019d\7n\2\2\u019d\u019e\7c\2\2\u019e\u019f")
        buf.write("\7u\2\2\u019f\u01a0\7u\2\2\u01a0N\3\2\2\2\u01a1\u01a2")
        buf.write("\7D\2\2\u01a2\u01a3\7t\2\2\u01a3\u01a4\7g\2\2\u01a4\u01a5")
        buf.write("\7c\2\2\u01a5\u01a6\7m\2\2\u01a6P\3\2\2\2\u01a7\u01a8")
        buf.write("\7E\2\2\u01a8\u01a9\7q\2\2\u01a9\u01aa\7p\2\2\u01aa\u01ab")
        buf.write("\7v\2\2\u01ab\u01ac\7k\2\2\u01ac\u01ad\7p\2\2\u01ad\u01ae")
        buf.write("\7w\2\2\u01ae\u01af\7g\2\2\u01afR\3\2\2\2\u01b0\u01b1")
        buf.write("\7K\2\2\u01b1\u01b2\7h\2\2\u01b2T\3\2\2\2\u01b3\u01b4")
        buf.write("\7G\2\2\u01b4\u01b5\7n\2\2\u01b5\u01b6\7u\2\2\u01b6\u01b7")
        buf.write("\7g\2\2\u01b7\u01b8\7k\2\2\u01b8\u01b9\7h\2\2\u01b9V\3")
        buf.write("\2\2\2\u01ba\u01bb\7G\2\2\u01bb\u01bc\7n\2\2\u01bc\u01bd")
        buf.write("\7u\2\2\u01bd\u01be\7g\2\2\u01beX\3\2\2\2\u01bf\u01c0")
        buf.write("\7H\2\2\u01c0\u01c1\7q\2\2\u01c1\u01c2\7t\2\2\u01c2\u01c3")
        buf.write("\7g\2\2\u01c3\u01c4\7c\2\2\u01c4\u01c5\7e\2\2\u01c5\u01c6")
        buf.write("\7j\2\2\u01c6Z\3\2\2\2\u01c7\u01c8\7V\2\2\u01c8\u01c9")
        buf.write("\7t\2\2\u01c9\u01ca\7w\2\2\u01ca\u01cb\7g\2\2\u01cb\\")
        buf.write("\3\2\2\2\u01cc\u01cd\7H\2\2\u01cd\u01ce\7c\2\2\u01ce\u01cf")
        buf.write("\7n\2\2\u01cf\u01d0\7u\2\2\u01d0\u01d1\7g\2\2\u01d1^\3")
        buf.write("\2\2\2\u01d2\u01d3\7C\2\2\u01d3\u01d4\7t\2\2\u01d4\u01d5")
        buf.write("\7t\2\2\u01d5\u01d6\7c\2\2\u01d6\u01d7\7{\2\2\u01d7`\3")
        buf.write("\2\2\2\u01d8\u01d9\7K\2\2\u01d9\u01da\7p\2\2\u01dab\3")
        buf.write("\2\2\2\u01db\u01dc\7D\2\2\u01dc\u01dd\7q\2\2\u01dd\u01de")
        buf.write("\7q\2\2\u01de\u01df\7n\2\2\u01df\u01e0\7g\2\2\u01e0\u01e1")
        buf.write("\7c\2\2\u01e1\u01e2\7p\2\2\u01e2d\3\2\2\2\u01e3\u01e4")
        buf.write("\7T\2\2\u01e4\u01e5\7g\2\2\u01e5\u01e6\7v\2\2\u01e6\u01e7")
        buf.write("\7w\2\2\u01e7\u01e8\7t\2\2\u01e8\u01e9\7p\2\2\u01e9f\3")
        buf.write("\2\2\2\u01ea\u01eb\7P\2\2\u01eb\u01ec\7w\2\2\u01ec\u01ed")
        buf.write("\7n\2\2\u01ed\u01ee\7n\2\2\u01eeh\3\2\2\2\u01ef\u01f0")
        buf.write("\7E\2\2\u01f0\u01f1\7q\2\2\u01f1\u01f2\7p\2\2\u01f2\u01f3")
        buf.write("\7u\2\2\u01f3\u01f4\7v\2\2\u01f4\u01f5\7t\2\2\u01f5\u01f6")
        buf.write("\7w\2\2\u01f6\u01f7\7e\2\2\u01f7\u01f8\7v\2\2\u01f8\u01f9")
        buf.write("\7q\2\2\u01f9\u01fa\7t\2\2\u01faj\3\2\2\2\u01fb\u01fc")
        buf.write("\7F\2\2\u01fc\u01fd\7g\2\2\u01fd\u01fe\7u\2\2\u01fe\u01ff")
        buf.write("\7v\2\2\u01ff\u0200\7t\2\2\u0200\u0201\7w\2\2\u0201\u0202")
        buf.write("\7e\2\2\u0202\u0203\7v\2\2\u0203\u0204\7q\2\2\u0204\u0205")
        buf.write("\7t\2\2\u0205l\3\2\2\2\u0206\u0207\7P\2\2\u0207\u0208")
        buf.write("\7g\2\2\u0208\u0209\7y\2\2\u0209n\3\2\2\2\u020a\u020b")
        buf.write("\7D\2\2\u020b\u020c\7{\2\2\u020cp\3\2\2\2\u020d\u020e")
        buf.write("\7U\2\2\u020e\u020f\7g\2\2\u020f\u0210\7n\2\2\u0210\u0211")
        buf.write("\7h\2\2\u0211r\3\2\2\2\u0212\u0213\7-\2\2\u0213t\3\2\2")
        buf.write("\2\u0214\u0215\7/\2\2\u0215v\3\2\2\2\u0216\u0217\7,\2")
        buf.write("\2\u0217x\3\2\2\2\u0218\u0219\7\61\2\2\u0219z\3\2\2\2")
        buf.write("\u021a\u021b\7\'\2\2\u021b|\3\2\2\2\u021c\u021d\7#\2\2")
        buf.write("\u021d~\3\2\2\2\u021e\u021f\7(\2\2\u021f\u0220\7(\2\2")
        buf.write("\u0220\u0080\3\2\2\2\u0221\u0222\7~\2\2\u0222\u0223\7")
        buf.write("~\2\2\u0223\u0082\3\2\2\2\u0224\u0225\7?\2\2\u0225\u0226")
        buf.write("\7?\2\2\u0226\u0084\3\2\2\2\u0227\u0228\7?\2\2\u0228\u0086")
        buf.write("\3\2\2\2\u0229\u022a\7#\2\2\u022a\u022b\7?\2\2\u022b\u0088")
        buf.write("\3\2\2\2\u022c\u022d\7@\2\2\u022d\u008a\3\2\2\2\u022e")
        buf.write("\u022f\7@\2\2\u022f\u0230\7?\2\2\u0230\u008c\3\2\2\2\u0231")
        buf.write("\u0232\7>\2\2\u0232\u008e\3\2\2\2\u0233\u0234\7>\2\2\u0234")
        buf.write("\u0235\7?\2\2\u0235\u0090\3\2\2\2\u0236\u0237\7?\2\2\u0237")
        buf.write("\u0238\7?\2\2\u0238\u0239\7\60\2\2\u0239\u0092\3\2\2\2")
        buf.write("\u023a\u023b\7-\2\2\u023b\u023c\7\60\2\2\u023c\u0094\3")
        buf.write("\2\2\2\u023d\u023e\7\60\2\2\u023e\u0096\3\2\2\2\u023f")
        buf.write("\u0240\7\60\2\2\u0240\u0241\7\60\2\2\u0241\u0098\3\2\2")
        buf.write("\2\u0242\u0243\7<\2\2\u0243\u0244\7<\2\2\u0244\u009a\3")
        buf.write("\2\2\2\u0245\u0249\t\r\2\2\u0246\u0248\t\16\2\2\u0247")
        buf.write("\u0246\3\2\2\2\u0248\u024b\3\2\2\2\u0249\u0247\3\2\2\2")
        buf.write("\u0249\u024a\3\2\2\2\u024a\u0253\3\2\2\2\u024b\u0249\3")
        buf.write("\2\2\2\u024c\u024e\5\61\31\2\u024d\u024f\t\16\2\2\u024e")
        buf.write("\u024d\3\2\2\2\u024f\u0250\3\2\2\2\u0250\u024e\3\2\2\2")
        buf.write("\u0250\u0251\3\2\2\2\u0251\u0253\3\2\2\2\u0252\u0245\3")
        buf.write("\2\2\2\u0252\u024c\3\2\2\2\u0253\u009c\3\2\2\2\u0254\u0255")
        buf.write("\7%\2\2\u0255\u0256\7%\2\2\u0256\u025a\3\2\2\2\u0257\u0259")
        buf.write("\13\2\2\2\u0258\u0257\3\2\2\2\u0259\u025c\3\2\2\2\u025a")
        buf.write("\u025b\3\2\2\2\u025a\u0258\3\2\2\2\u025b\u025d\3\2\2\2")
        buf.write("\u025c\u025a\3\2\2\2\u025d\u025e\7%\2\2\u025e\u025f\7")
        buf.write("%\2\2\u025f\u0260\3\2\2\2\u0260\u0261\bO\13\2\u0261\u009e")
        buf.write("\3\2\2\2\u0262\u0264\t\17\2\2\u0263\u0262\3\2\2\2\u0264")
        buf.write("\u0265\3\2\2\2\u0265\u0263\3\2\2\2\u0265\u0266\3\2\2\2")
        buf.write("\u0266\u0267\3\2\2\2\u0267\u0268\bP\13\2\u0268\u00a0\3")
        buf.write("\2\2\2\u0269\u026a\13\2\2\2\u026a\u026b\bQ\f\2\u026b\u00a2")
        buf.write("\3\2\2\2\37\2\u00c3\u00e1\u00e9\u00ef\u00f7\u00fb\u0102")
        buf.write("\u0109\u010f\u0115\u011d\u0121\u0128\u012d\u0133\u013d")
        buf.write("\u0147\u0151\u0159\u0168\u0188\u0193\u0197\u0249\u0250")
        buf.write("\u0252\u025a\u0265\r\3\n\2\3\f\3\3\r\4\3\16\5\3\17\6\3")
        buf.write("\20\7\3\21\b\3\22\t\3\26\n\b\2\2\3Q\13")
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
    ARRAY_SIZE = 10
    HEX_TYPE = 11
    OCT_TYPE = 12
    BIN_TYPE = 13
    DEC_TYPE = 14
    STRING_LITERAL = 15
    ILLEGAL_ESCAPE = 16
    UNCLOSE_STRING = 17
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
    DOTDOT = 67
    SCOPE = 68
    ID = 69
    BLOCK_COMMENT = 70
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
            "'>'", "'>='", "'<'", "'<='", "'==.'", "'+.'", "'.'", "'..'", 
            "'::'" ]

    symbolicNames = [ "<INVALID>",
            "BOOL_TYPE", "FLOAT_TYPE", "STRING", "INT_TYPE", "VOID_TYPE", 
            "INTEGER_LITERAL", "ARRAY_SIZE", "HEX_TYPE", "OCT_TYPE", "BIN_TYPE", 
            "DEC_TYPE", "STRING_LITERAL", "ILLEGAL_ESCAPE", "UNCLOSE_STRING", 
            "REAL_LITERAL", "VAL", "VAR", "LP", "RP", "LCB", "RCB", "LSB", 
            "RSB", "SEMI", "COMMA", "COLON", "CLASS", "BREAK", "CONTINUE", 
            "IF", "ELSEIF", "ELSE", "FOREACH", "TRUE", "FALSE", "ARRAY", 
            "IN", "BOOLEAN", "RETURN", "NULL", "CONSTRUCTOR", "DESTRUCTOR", 
            "NEW", "BY", "SELF", "ADD", "SUB", "MUL", "DIV", "MOD", "NOT", 
            "AND", "OR", "EQUAL", "ASSIGN", "NOTEQUAL", "GT", "GTE", "LT", 
            "LTE", "EQUAL_STR", "ADD_STR", "DOT", "DOTDOT", "SCOPE", "ID", 
            "BLOCK_COMMENT", "WS", "ERROR_CHAR" ]

    ruleNames = [ "T__0", "T__1", "T__2", "BOOL_TYPE", "FLOAT_TYPE", "STRING", 
                  "INT_TYPE", "VOID_TYPE", "INTEGER_LITERAL", "ARRAY_SIZE", 
                  "HEX_TYPE", "OCT_TYPE", "BIN_TYPE", "DEC_TYPE", "STRING_LITERAL", 
                  "ILLEGAL_ESCAPE", "UNCLOSE_STRING", "STR", "ESC_SEQ", 
                  "ESC_ILLEGAL", "REAL_LITERAL", "VAL", "VAR", "DOLLAR", 
                  "LP", "RP", "LCB", "RCB", "LSB", "RSB", "SEMI", "COMMA", 
                  "COLON", "EXPONENT", "DIGIT", "DEC_DIGIT", "SIGN", "CLASS", 
                  "BREAK", "CONTINUE", "IF", "ELSEIF", "ELSE", "FOREACH", 
                  "TRUE", "FALSE", "ARRAY", "IN", "BOOLEAN", "RETURN", "NULL", 
                  "CONSTRUCTOR", "DESTRUCTOR", "NEW", "BY", "SELF", "ADD", 
                  "SUB", "MUL", "DIV", "MOD", "NOT", "AND", "OR", "EQUAL", 
                  "ASSIGN", "NOTEQUAL", "GT", "GTE", "LT", "LTE", "EQUAL_STR", 
                  "ADD_STR", "DOT", "DOTDOT", "SCOPE", "ID", "BLOCK_COMMENT", 
                  "WS", "ERROR_CHAR" ]

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
        return result


    def action(self, localctx:RuleContext, ruleIndex:int, actionIndex:int):
        if self._actions is None:
            actions = dict()
            actions[8] = self.INTEGER_LITERAL_action 
            actions[10] = self.HEX_TYPE_action 
            actions[11] = self.OCT_TYPE_action 
            actions[12] = self.BIN_TYPE_action 
            actions[13] = self.DEC_TYPE_action 
            actions[14] = self.STRING_LITERAL_action 
            actions[15] = self.ILLEGAL_ESCAPE_action 
            actions[16] = self.UNCLOSE_STRING_action 
            actions[20] = self.REAL_LITERAL_action 
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
                print(y)
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

     


