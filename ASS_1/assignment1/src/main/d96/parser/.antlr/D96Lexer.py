# Generated from e:\HCMUT\PRINCIPLES_OF_PROGRAMMING_LANGUAGE\ASSIGNMENT\ASS_1\assignment1\src\main\d96\parser\D96.g4 by ANTLR 4.8
from antlr4 import *
from io import StringIO
from typing.io import TextIO
import sys


from lexererr import *



def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2F")
        buf.write("\u0231\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7")
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
        buf.write("L\3\2\3\2\3\2\3\2\3\2\3\3\3\3\3\3\3\3\3\3\5\3\u00a4\n")
        buf.write("\3\3\3\3\3\7\3\u00a8\n\3\f\3\16\3\u00ab\13\3\3\3\3\3\3")
        buf.write("\4\3\4\5\4\u00b1\n\4\3\4\3\4\3\4\3\4\5\4\u00b7\n\4\3\4")
        buf.write("\3\4\3\5\3\5\3\6\3\6\3\7\3\7\3\7\3\7\7\7\u00c3\n\7\f\7")
        buf.write("\16\7\u00c6\13\7\3\b\3\b\3\b\3\b\3\b\3\t\3\t\3\t\3\t\3")
        buf.write("\n\3\n\5\n\u00d3\n\n\3\13\3\13\3\13\3\13\3\13\3\f\3\f")
        buf.write("\3\f\3\f\3\f\3\f\3\f\3\f\3\f\3\f\3\f\3\f\3\r\3\r\3\r\3")
        buf.write("\r\3\r\3\r\3\16\3\16\3\16\3\16\3\16\3\16\5\16\u00f2\n")
        buf.write("\16\3\17\6\17\u00f5\n\17\r\17\16\17\u00f6\3\20\3\20\7")
        buf.write("\20\u00fb\n\20\f\20\16\20\u00fe\13\20\3\21\3\21\3\21\3")
        buf.write("\21\3\22\3\22\3\22\3\22\3\23\3\23\3\23\3\23\3\23\3\23")
        buf.write("\3\24\3\24\3\25\3\25\3\26\3\26\3\27\3\27\3\30\3\30\3\31")
        buf.write("\3\31\3\32\3\32\3\33\3\33\3\34\3\34\3\35\3\35\3\36\3\36")
        buf.write("\3\36\3\37\3\37\3 \3 \3 \3 \3 \3 \3!\3!\3!\3!\3!\3!\3")
        buf.write("!\3!\3\"\3\"\3\"\3\"\3\"\3\"\3\"\3\"\3#\3#\3#\3#\3#\3")
        buf.write("$\3$\3$\3$\3$\3$\3$\3$\3$\3%\3%\3%\3%\3%\3&\3&\3&\3&\3")
        buf.write("&\3&\3\'\3\'\3\'\3\'\3\'\3\'\3\'\3(\3(\3(\3)\3)\3)\3)")
        buf.write("\3)\3)\3)\3*\3*\3*\3*\3*\3*\3*\3*\3*\3*\3+\3+\3+\3+\3")
        buf.write("+\3,\3,\3,\3,\3,\3,\3-\3-\3-\3-\3-\3-\3-\3.\3.\5.\u0185")
        buf.write("\n.\3.\6.\u0188\n.\r.\16.\u0189\3/\3/\3\60\3\60\3\61\6")
        buf.write("\61\u0191\n\61\r\61\16\61\u0192\3\62\3\62\7\62\u0197\n")
        buf.write("\62\f\62\16\62\u019a\13\62\3\62\3\62\3\62\3\63\6\63\u01a0")
        buf.write("\n\63\r\63\16\63\u01a1\3\63\3\63\3\63\7\63\u01a7\n\63")
        buf.write("\f\63\16\63\u01aa\13\63\3\63\7\63\u01ad\n\63\f\63\16\63")
        buf.write("\u01b0\13\63\3\63\3\63\6\63\u01b4\n\63\r\63\16\63\u01b5")
        buf.write("\3\63\5\63\u01b9\n\63\3\63\6\63\u01bc\n\63\r\63\16\63")
        buf.write("\u01bd\3\63\3\63\5\63\u01c2\n\63\3\64\3\64\3\65\3\65\3")
        buf.write("\65\3\66\3\66\3\67\3\67\38\38\39\39\3:\3:\3;\3;\3;\3<")
        buf.write("\3<\3<\3=\3=\3=\3=\3>\3>\3>\3?\3?\3@\3@\3@\3A\3A\3A\3")
        buf.write("B\3B\3C\3C\3C\3D\6D\u01ee\nD\rD\16D\u01ef\3D\3D\3E\3E")
        buf.write("\3E\3E\7E\u01f8\nE\fE\16E\u01fb\13E\3E\3E\3E\3E\3E\3F")
        buf.write("\3F\5F\u0204\nF\3G\3G\3G\3H\3H\3H\5H\u020c\nH\3I\3I\7")
        buf.write("I\u0210\nI\fI\16I\u0213\13I\3I\5I\u0216\nI\3I\3I\3J\3")
        buf.write("J\7J\u021c\nJ\fJ\16J\u021f\13J\3J\3J\3J\3K\3K\3K\3L\3")
        buf.write("L\3L\3L\7L\u022b\nL\fL\16L\u022e\13L\3L\3L\4\u01f9\u022c")
        buf.write("\2M\3\3\5\4\7\5\t\6\13\7\r\b\17\t\21\n\23\13\25\f\27\r")
        buf.write("\31\16\33\17\35\20\37\21!\22#\23%\24\'\25)\26+\27-\30")
        buf.write("/\31\61\32\63\33\65\34\67\359\36;\37=\2? A!C\"E#G$I%K")
        buf.write("&M\'O(Q)S*U+W,Y-[\2]\2_\2a.c/e\60g\61i\62k\63m\64o\65")
        buf.write("q\66s\67u8w9y:{;}<\177=\u0081>\u0083?\u0085@\u0087A\u0089")
        buf.write("B\u008b\2\u008d\2\u008f\2\u0091C\u0093D\u0095E\u0097F")
        buf.write("\3\2\f\3\2\62;\5\2C\\aac|\6\2\62;C\\aac|\4\2GGgg\4\2-")
        buf.write("-//\5\2\13\f\17\17\"\"\7\2\n\f\16\17$$))^^\n\2$$))^^d")
        buf.write("dhhppttvv\3\2^^\7\3\n\f\16\17$$))^^\2\u024a\2\3\3\2\2")
        buf.write("\2\2\5\3\2\2\2\2\7\3\2\2\2\2\t\3\2\2\2\2\13\3\2\2\2\2")
        buf.write("\r\3\2\2\2\2\17\3\2\2\2\2\21\3\2\2\2\2\23\3\2\2\2\2\25")
        buf.write("\3\2\2\2\2\27\3\2\2\2\2\31\3\2\2\2\2\33\3\2\2\2\2\35\3")
        buf.write("\2\2\2\2\37\3\2\2\2\2!\3\2\2\2\2#\3\2\2\2\2%\3\2\2\2\2")
        buf.write("\'\3\2\2\2\2)\3\2\2\2\2+\3\2\2\2\2-\3\2\2\2\2/\3\2\2\2")
        buf.write("\2\61\3\2\2\2\2\63\3\2\2\2\2\65\3\2\2\2\2\67\3\2\2\2\2")
        buf.write("9\3\2\2\2\2;\3\2\2\2\2?\3\2\2\2\2A\3\2\2\2\2C\3\2\2\2")
        buf.write("\2E\3\2\2\2\2G\3\2\2\2\2I\3\2\2\2\2K\3\2\2\2\2M\3\2\2")
        buf.write("\2\2O\3\2\2\2\2Q\3\2\2\2\2S\3\2\2\2\2U\3\2\2\2\2W\3\2")
        buf.write("\2\2\2Y\3\2\2\2\2a\3\2\2\2\2c\3\2\2\2\2e\3\2\2\2\2g\3")
        buf.write("\2\2\2\2i\3\2\2\2\2k\3\2\2\2\2m\3\2\2\2\2o\3\2\2\2\2q")
        buf.write("\3\2\2\2\2s\3\2\2\2\2u\3\2\2\2\2w\3\2\2\2\2y\3\2\2\2\2")
        buf.write("{\3\2\2\2\2}\3\2\2\2\2\177\3\2\2\2\2\u0081\3\2\2\2\2\u0083")
        buf.write("\3\2\2\2\2\u0085\3\2\2\2\2\u0087\3\2\2\2\2\u0089\3\2\2")
        buf.write("\2\2\u0091\3\2\2\2\2\u0093\3\2\2\2\2\u0095\3\2\2\2\2\u0097")
        buf.write("\3\2\2\2\3\u0099\3\2\2\2\5\u009e\3\2\2\2\7\u00b0\3\2\2")
        buf.write("\2\t\u00ba\3\2\2\2\13\u00bc\3\2\2\2\r\u00be\3\2\2\2\17")
        buf.write("\u00c7\3\2\2\2\21\u00cc\3\2\2\2\23\u00d2\3\2\2\2\25\u00d4")
        buf.write("\3\2\2\2\27\u00d9\3\2\2\2\31\u00e5\3\2\2\2\33\u00f1\3")
        buf.write("\2\2\2\35\u00f4\3\2\2\2\37\u00f8\3\2\2\2!\u00ff\3\2\2")
        buf.write("\2#\u0103\3\2\2\2%\u0107\3\2\2\2\'\u010d\3\2\2\2)\u010f")
        buf.write("\3\2\2\2+\u0111\3\2\2\2-\u0113\3\2\2\2/\u0115\3\2\2\2")
        buf.write("\61\u0117\3\2\2\2\63\u0119\3\2\2\2\65\u011b\3\2\2\2\67")
        buf.write("\u011d\3\2\2\29\u011f\3\2\2\2;\u0121\3\2\2\2=\u0124\3")
        buf.write("\2\2\2?\u0126\3\2\2\2A\u012c\3\2\2\2C\u0134\3\2\2\2E\u013c")
        buf.write("\3\2\2\2G\u0141\3\2\2\2I\u014a\3\2\2\2K\u014f\3\2\2\2")
        buf.write("M\u0155\3\2\2\2O\u015c\3\2\2\2Q\u015f\3\2\2\2S\u0166\3")
        buf.write("\2\2\2U\u0170\3\2\2\2W\u0175\3\2\2\2Y\u017b\3\2\2\2[\u0182")
        buf.write("\3\2\2\2]\u018b\3\2\2\2_\u018d\3\2\2\2a\u0190\3\2\2\2")
        buf.write("c\u0194\3\2\2\2e\u01c1\3\2\2\2g\u01c3\3\2\2\2i\u01c5\3")
        buf.write("\2\2\2k\u01c8\3\2\2\2m\u01ca\3\2\2\2o\u01cc\3\2\2\2q\u01ce")
        buf.write("\3\2\2\2s\u01d0\3\2\2\2u\u01d2\3\2\2\2w\u01d5\3\2\2\2")
        buf.write("y\u01d8\3\2\2\2{\u01dc\3\2\2\2}\u01df\3\2\2\2\177\u01e1")
        buf.write("\3\2\2\2\u0081\u01e4\3\2\2\2\u0083\u01e7\3\2\2\2\u0085")
        buf.write("\u01e9\3\2\2\2\u0087\u01ed\3\2\2\2\u0089\u01f3\3\2\2\2")
        buf.write("\u008b\u0203\3\2\2\2\u008d\u0205\3\2\2\2\u008f\u020b\3")
        buf.write("\2\2\2\u0091\u020d\3\2\2\2\u0093\u0219\3\2\2\2\u0095\u0223")
        buf.write("\3\2\2\2\u0097\u0226\3\2\2\2\u0099\u009a\7o\2\2\u009a")
        buf.write("\u009b\7c\2\2\u009b\u009c\7k\2\2\u009c\u009d\7p\2\2\u009d")
        buf.write("\4\3\2\2\2\u009e\u009f\5%\23\2\u009f\u00a3\5\37\20\2\u00a0")
        buf.write("\u00a1\59\35\2\u00a1\u00a2\5\37\20\2\u00a2\u00a4\3\2\2")
        buf.write("\2\u00a3\u00a0\3\2\2\2\u00a3\u00a4\3\2\2\2\u00a4\u00a5")
        buf.write("\3\2\2\2\u00a5\u00a9\5-\27\2\u00a6\u00a8\5\t\5\2\u00a7")
        buf.write("\u00a6\3\2\2\2\u00a8\u00ab\3\2\2\2\u00a9\u00a7\3\2\2\2")
        buf.write("\u00a9\u00aa\3\2\2\2\u00aa\u00ac\3\2\2\2\u00ab\u00a9\3")
        buf.write("\2\2\2\u00ac\u00ad\5/\30\2\u00ad\6\3\2\2\2\u00ae\u00b1")
        buf.write("\5#\22\2\u00af\u00b1\5!\21\2\u00b0\u00ae\3\2\2\2\u00b0")
        buf.write("\u00af\3\2\2\2\u00b1\u00b2\3\2\2\2\u00b2\u00b3\5\r\7\2")
        buf.write("\u00b3\u00b4\59\35\2\u00b4\u00b6\5\33\16\2\u00b5\u00b7")
        buf.write("\3\2\2\2\u00b6\u00b5\3\2\2\2\u00b6\u00b7\3\2\2\2\u00b7")
        buf.write("\u00b8\3\2\2\2\u00b8\u00b9\5\65\33\2\u00b9\b\3\2\2\2\u00ba")
        buf.write("\u00bb\5\17\b\2\u00bb\n\3\2\2\2\u00bc\u00bd\3\2\2\2\u00bd")
        buf.write("\f\3\2\2\2\u00be\u00c4\5\37\20\2\u00bf\u00c0\5\67\34\2")
        buf.write("\u00c0\u00c1\5\37\20\2\u00c1\u00c3\3\2\2\2\u00c2\u00bf")
        buf.write("\3\2\2\2\u00c3\u00c6\3\2\2\2\u00c4\u00c2\3\2\2\2\u00c4")
        buf.write("\u00c5\3\2\2\2\u00c5\16\3\2\2\2\u00c6\u00c4\3\2\2\2\u00c7")
        buf.write("\u00c8\5\37\20\2\u00c8\u00c9\5)\25\2\u00c9\u00ca\3\2\2")
        buf.write("\2\u00ca\u00cb\5+\26\2\u00cb\20\3\2\2\2\u00cc\u00cd\7")
        buf.write("K\2\2\u00cd\u00ce\7p\2\2\u00ce\u00cf\7v\2\2\u00cf\22\3")
        buf.write("\2\2\2\u00d0\u00d3\5I%\2\u00d1\u00d3\5K&\2\u00d2\u00d0")
        buf.write("\3\2\2\2\u00d2\u00d1\3\2\2\2\u00d3\24\3\2\2\2\u00d4\u00d5")
        buf.write("\7X\2\2\u00d5\u00d6\7q\2\2\u00d6\u00d7\7k\2\2\u00d7\u00d8")
        buf.write("\7f\2\2\u00d8\26\3\2\2\2\u00d9\u00da\7C\2\2\u00da\u00db")
        buf.write("\7t\2\2\u00db\u00dc\7t\2\2\u00dc\u00dd\7c\2\2\u00dd\u00de")
        buf.write("\7{\2\2\u00de\u00df\3\2\2\2\u00df\u00e0\5\61\31\2\u00e0")
        buf.write("\u00e1\5\33\16\2\u00e1\u00e2\5\67\34\2\u00e2\u00e3\5\35")
        buf.write("\17\2\u00e3\u00e4\5\63\32\2\u00e4\30\3\2\2\2\u00e5\u00e6")
        buf.write("\7H\2\2\u00e6\u00e7\7n\2\2\u00e7\u00e8\7q\2\2\u00e8\u00e9")
        buf.write("\7c\2\2\u00e9\u00ea\7v\2\2\u00ea\32\3\2\2\2\u00eb\u00f2")
        buf.write("\5\23\n\2\u00ec\u00f2\5\21\t\2\u00ed\u00f2\5\31\r\2\u00ee")
        buf.write("\u00f2\5M\'\2\u00ef\u00f2\5\27\f\2\u00f0\u00f2\5%\23\2")
        buf.write("\u00f1\u00eb\3\2\2\2\u00f1\u00ec\3\2\2\2\u00f1\u00ed\3")
        buf.write("\2\2\2\u00f1\u00ee\3\2\2\2\u00f1\u00ef\3\2\2\2\u00f1\u00f0")
        buf.write("\3\2\2\2\u00f2\34\3\2\2\2\u00f3\u00f5\t\2\2\2\u00f4\u00f3")
        buf.write("\3\2\2\2\u00f5\u00f6\3\2\2\2\u00f6\u00f4\3\2\2\2\u00f6")
        buf.write("\u00f7\3\2\2\2\u00f7\36\3\2\2\2\u00f8\u00fc\t\3\2\2\u00f9")
        buf.write("\u00fb\t\4\2\2\u00fa\u00f9\3\2\2\2\u00fb\u00fe\3\2\2\2")
        buf.write("\u00fc\u00fa\3\2\2\2\u00fc\u00fd\3\2\2\2\u00fd \3\2\2")
        buf.write("\2\u00fe\u00fc\3\2\2\2\u00ff\u0100\7x\2\2\u0100\u0101")
        buf.write("\7c\2\2\u0101\u0102\7n\2\2\u0102\"\3\2\2\2\u0103\u0104")
        buf.write("\7x\2\2\u0104\u0105\7c\2\2\u0105\u0106\7t\2\2\u0106$\3")
        buf.write("\2\2\2\u0107\u0108\7e\2\2\u0108\u0109\7n\2\2\u0109\u010a")
        buf.write("\7c\2\2\u010a\u010b\7u\2\2\u010b\u010c\7u\2\2\u010c&\3")
        buf.write("\2\2\2\u010d\u010e\7&\2\2\u010e(\3\2\2\2\u010f\u0110\7")
        buf.write("*\2\2\u0110*\3\2\2\2\u0111\u0112\7+\2\2\u0112,\3\2\2\2")
        buf.write("\u0113\u0114\7}\2\2\u0114.\3\2\2\2\u0115\u0116\7\177\2")
        buf.write("\2\u0116\60\3\2\2\2\u0117\u0118\7]\2\2\u0118\62\3\2\2")
        buf.write("\2\u0119\u011a\7_\2\2\u011a\64\3\2\2\2\u011b\u011c\7=")
        buf.write("\2\2\u011c\66\3\2\2\2\u011d\u011e\7.\2\2\u011e8\3\2\2")
        buf.write("\2\u011f\u0120\7<\2\2\u0120:\3\2\2\2\u0121\u0122\7\60")
        buf.write("\2\2\u0122\u0123\7\60\2\2\u0123<\3\2\2\2\u0124\u0125\7")
        buf.write("\60\2\2\u0125>\3\2\2\2\u0126\u0127\7D\2\2\u0127\u0128")
        buf.write("\7t\2\2\u0128\u0129\7g\2\2\u0129\u012a\7c\2\2\u012a\u012b")
        buf.write("\7m\2\2\u012b@\3\2\2\2\u012c\u012d\7H\2\2\u012d\u012e")
        buf.write("\7q\2\2\u012e\u012f\7t\2\2\u012f\u0130\7g\2\2\u0130\u0131")
        buf.write("\7c\2\2\u0131\u0132\7e\2\2\u0132\u0133\7j\2\2\u0133B\3")
        buf.write("\2\2\2\u0134\u0135\7D\2\2\u0135\u0136\7q\2\2\u0136\u0137")
        buf.write("\7q\2\2\u0137\u0138\7n\2\2\u0138\u0139\7g\2\2\u0139\u013a")
        buf.write("\7c\2\2\u013a\u013b\7p\2\2\u013bD\3\2\2\2\u013c\u013d")
        buf.write("\7P\2\2\u013d\u013e\7w\2\2\u013e\u013f\7n\2\2\u013f\u0140")
        buf.write("\7n\2\2\u0140F\3\2\2\2\u0141\u0142\7E\2\2\u0142\u0143")
        buf.write("\7q\2\2\u0143\u0144\7p\2\2\u0144\u0145\7v\2\2\u0145\u0146")
        buf.write("\7k\2\2\u0146\u0147\7p\2\2\u0147\u0148\7w\2\2\u0148\u0149")
        buf.write("\7g\2\2\u0149H\3\2\2\2\u014a\u014b\7V\2\2\u014b\u014c")
        buf.write("\7t\2\2\u014c\u014d\7w\2\2\u014d\u014e\7g\2\2\u014eJ\3")
        buf.write("\2\2\2\u014f\u0150\7H\2\2\u0150\u0151\7c\2\2\u0151\u0152")
        buf.write("\7n\2\2\u0152\u0153\7u\2\2\u0153\u0154\7g\2\2\u0154L\3")
        buf.write("\2\2\2\u0155\u0156\7u\2\2\u0156\u0157\7v\2\2\u0157\u0158")
        buf.write("\7t\2\2\u0158\u0159\7k\2\2\u0159\u015a\7p\2\2\u015a\u015b")
        buf.write("\7i\2\2\u015bN\3\2\2\2\u015c\u015d\7k\2\2\u015d\u015e")
        buf.write("\7h\2\2\u015eP\3\2\2\2\u015f\u0160\7g\2\2\u0160\u0161")
        buf.write("\7n\2\2\u0161\u0162\7u\2\2\u0162\u0163\7g\2\2\u0163\u0164")
        buf.write("\7k\2\2\u0164\u0165\7h\2\2\u0165R\3\2\2\2\u0166\u0167")
        buf.write("\7C\2\2\u0167\u0168\7t\2\2\u0168\u0169\7t\2\2\u0169\u016a")
        buf.write("\7c\2\2\u016a\u016b\7{\2\2\u016b\u016c\7\"\2\2\u016c\u016d")
        buf.write("\7K\2\2\u016d\u016e\7p\2\2\u016e\u016f\7v\2\2\u016fT\3")
        buf.write("\2\2\2\u0170\u0171\7G\2\2\u0171\u0172\7n\2\2\u0172\u0173")
        buf.write("\7u\2\2\u0173\u0174\7g\2\2\u0174V\3\2\2\2\u0175\u0176")
        buf.write("\7H\2\2\u0176\u0177\7n\2\2\u0177\u0178\7q\2\2\u0178\u0179")
        buf.write("\7c\2\2\u0179\u017a\7v\2\2\u017aX\3\2\2\2\u017b\u017c")
        buf.write("\7t\2\2\u017c\u017d\7g\2\2\u017d\u017e\7v\2\2\u017e\u017f")
        buf.write("\7w\2\2\u017f\u0180\7t\2\2\u0180\u0181\7p\2\2\u0181Z\3")
        buf.write("\2\2\2\u0182\u0184\t\5\2\2\u0183\u0185\5k\66\2\u0184\u0183")
        buf.write("\3\2\2\2\u0184\u0185\3\2\2\2\u0185\u0187\3\2\2\2\u0186")
        buf.write("\u0188\5]/\2\u0187\u0186\3\2\2\2\u0188\u0189\3\2\2\2\u0189")
        buf.write("\u0187\3\2\2\2\u0189\u018a\3\2\2\2\u018a\\\3\2\2\2\u018b")
        buf.write("\u018c\t\2\2\2\u018c^\3\2\2\2\u018d\u018e\t\6\2\2\u018e")
        buf.write("`\3\2\2\2\u018f\u0191\5]/\2\u0190\u018f\3\2\2\2\u0191")
        buf.write("\u0192\3\2\2\2\u0192\u0190\3\2\2\2\u0192\u0193\3\2\2\2")
        buf.write("\u0193b\3\2\2\2\u0194\u0198\7$\2\2\u0195\u0197\5\u008b")
        buf.write("F\2\u0196\u0195\3\2\2\2\u0197\u019a\3\2\2\2\u0198\u0196")
        buf.write("\3\2\2\2\u0198\u0199\3\2\2\2\u0199\u019b\3\2\2\2\u019a")
        buf.write("\u0198\3\2\2\2\u019b\u019c\7$\2\2\u019c\u019d\b\62\2\2")
        buf.write("\u019dd\3\2\2\2\u019e\u01a0\5]/\2\u019f\u019e\3\2\2\2")
        buf.write("\u01a0\u01a1\3\2\2\2\u01a1\u019f\3\2\2\2\u01a1\u01a2\3")
        buf.write("\2\2\2\u01a2\u01a3\3\2\2\2\u01a3\u01a8\5=\37\2\u01a4\u01a7")
        buf.write("\5]/\2\u01a5\u01a7\5[.\2\u01a6\u01a4\3\2\2\2\u01a6\u01a5")
        buf.write("\3\2\2\2\u01a7\u01aa\3\2\2\2\u01a8\u01a6\3\2\2\2\u01a8")
        buf.write("\u01a9\3\2\2\2\u01a9\u01c2\3\2\2\2\u01aa\u01a8\3\2\2\2")
        buf.write("\u01ab\u01ad\5]/\2\u01ac\u01ab\3\2\2\2\u01ad\u01b0\3\2")
        buf.write("\2\2\u01ae\u01ac\3\2\2\2\u01ae\u01af\3\2\2\2\u01af\u01b1")
        buf.write("\3\2\2\2\u01b0\u01ae\3\2\2\2\u01b1\u01b3\5=\37\2\u01b2")
        buf.write("\u01b4\5]/\2\u01b3\u01b2\3\2\2\2\u01b4\u01b5\3\2\2\2\u01b5")
        buf.write("\u01b3\3\2\2\2\u01b5\u01b6\3\2\2\2\u01b6\u01b8\3\2\2\2")
        buf.write("\u01b7\u01b9\5[.\2\u01b8\u01b7\3\2\2\2\u01b8\u01b9\3\2")
        buf.write("\2\2\u01b9\u01c2\3\2\2\2\u01ba\u01bc\5]/\2\u01bb\u01ba")
        buf.write("\3\2\2\2\u01bc\u01bd\3\2\2\2\u01bd\u01bb\3\2\2\2\u01bd")
        buf.write("\u01be\3\2\2\2\u01be\u01bf\3\2\2\2\u01bf\u01c0\5[.\2\u01c0")
        buf.write("\u01c2\3\2\2\2\u01c1\u019f\3\2\2\2\u01c1\u01ae\3\2\2\2")
        buf.write("\u01c1\u01bb\3\2\2\2\u01c2f\3\2\2\2\u01c3\u01c4\7-\2\2")
        buf.write("\u01c4h\3\2\2\2\u01c5\u01c6\7-\2\2\u01c6\u01c7\7\60\2")
        buf.write("\2\u01c7j\3\2\2\2\u01c8\u01c9\7/\2\2\u01c9l\3\2\2\2\u01ca")
        buf.write("\u01cb\7,\2\2\u01cbn\3\2\2\2\u01cc\u01cd\7\61\2\2\u01cd")
        buf.write("p\3\2\2\2\u01ce\u01cf\7\'\2\2\u01cfr\3\2\2\2\u01d0\u01d1")
        buf.write("\7#\2\2\u01d1t\3\2\2\2\u01d2\u01d3\7#\2\2\u01d3\u01d4")
        buf.write("\7?\2\2\u01d4v\3\2\2\2\u01d5\u01d6\7?\2\2\u01d6\u01d7")
        buf.write("\7?\2\2\u01d7x\3\2\2\2\u01d8\u01d9\7?\2\2\u01d9\u01da")
        buf.write("\7?\2\2\u01da\u01db\7\60\2\2\u01dbz\3\2\2\2\u01dc\u01dd")
        buf.write("\7(\2\2\u01dd\u01de\7(\2\2\u01de|\3\2\2\2\u01df\u01e0")
        buf.write("\7@\2\2\u01e0~\3\2\2\2\u01e1\u01e2\7~\2\2\u01e2\u01e3")
        buf.write("\7~\2\2\u01e3\u0080\3\2\2\2\u01e4\u01e5\7>\2\2\u01e5\u01e6")
        buf.write("\7?\2\2\u01e6\u0082\3\2\2\2\u01e7\u01e8\7?\2\2\u01e8\u0084")
        buf.write("\3\2\2\2\u01e9\u01ea\7@\2\2\u01ea\u01eb\7?\2\2\u01eb\u0086")
        buf.write("\3\2\2\2\u01ec\u01ee\t\7\2\2\u01ed\u01ec\3\2\2\2\u01ee")
        buf.write("\u01ef\3\2\2\2\u01ef\u01ed\3\2\2\2\u01ef\u01f0\3\2\2\2")
        buf.write("\u01f0\u01f1\3\2\2\2\u01f1\u01f2\bD\3\2\u01f2\u0088\3")
        buf.write("\2\2\2\u01f3\u01f4\7%\2\2\u01f4\u01f5\7%\2\2\u01f5\u01f9")
        buf.write("\3\2\2\2\u01f6\u01f8\13\2\2\2\u01f7\u01f6\3\2\2\2\u01f8")
        buf.write("\u01fb\3\2\2\2\u01f9\u01fa\3\2\2\2\u01f9\u01f7\3\2\2\2")
        buf.write("\u01fa\u01fc\3\2\2\2\u01fb\u01f9\3\2\2\2\u01fc\u01fd\7")
        buf.write("%\2\2\u01fd\u01fe\7%\2\2\u01fe\u01ff\3\2\2\2\u01ff\u0200")
        buf.write("\bE\3\2\u0200\u008a\3\2\2\2\u0201\u0204\n\b\2\2\u0202")
        buf.write("\u0204\5\u008dG\2\u0203\u0201\3\2\2\2\u0203\u0202\3\2")
        buf.write("\2\2\u0204\u008c\3\2\2\2\u0205\u0206\7^\2\2\u0206\u0207")
        buf.write("\t\t\2\2\u0207\u008e\3\2\2\2\u0208\u0209\7^\2\2\u0209")
        buf.write("\u020c\n\t\2\2\u020a\u020c\n\n\2\2\u020b\u0208\3\2\2\2")
        buf.write("\u020b\u020a\3\2\2\2\u020c\u0090\3\2\2\2\u020d\u0211\7")
        buf.write("$\2\2\u020e\u0210\5\u008bF\2\u020f\u020e\3\2\2\2\u0210")
        buf.write("\u0213\3\2\2\2\u0211\u020f\3\2\2\2\u0211\u0212\3\2\2\2")
        buf.write("\u0212\u0215\3\2\2\2\u0213\u0211\3\2\2\2\u0214\u0216\t")
        buf.write("\13\2\2\u0215\u0214\3\2\2\2\u0216\u0217\3\2\2\2\u0217")
        buf.write("\u0218\bI\4\2\u0218\u0092\3\2\2\2\u0219\u021d\7$\2\2\u021a")
        buf.write("\u021c\5\u008bF\2\u021b\u021a\3\2\2\2\u021c\u021f\3\2")
        buf.write("\2\2\u021d\u021b\3\2\2\2\u021d\u021e\3\2\2\2\u021e\u0220")
        buf.write("\3\2\2\2\u021f\u021d\3\2\2\2\u0220\u0221\5\u008fH\2\u0221")
        buf.write("\u0222\bJ\5\2\u0222\u0094\3\2\2\2\u0223\u0224\13\2\2\2")
        buf.write("\u0224\u0225\bK\6\2\u0225\u0096\3\2\2\2\u0226\u0227\7")
        buf.write("%\2\2\u0227\u0228\7%\2\2\u0228\u022c\3\2\2\2\u0229\u022b")
        buf.write("\13\2\2\2\u022a\u0229\3\2\2\2\u022b\u022e\3\2\2\2\u022c")
        buf.write("\u022d\3\2\2\2\u022c\u022a\3\2\2\2\u022d\u022f\3\2\2\2")
        buf.write("\u022e\u022c\3\2\2\2\u022f\u0230\bL\7\2\u0230\u0098\3")
        buf.write("\2\2\2 \2\u00a3\u00a9\u00b0\u00b6\u00c4\u00d2\u00f1\u00f6")
        buf.write("\u00fc\u0184\u0189\u0192\u0198\u01a1\u01a6\u01a8\u01ae")
        buf.write("\u01b5\u01b8\u01bd\u01c1\u01ef\u01f9\u0203\u020b\u0211")
        buf.write("\u0215\u021d\u022c\b\3\62\2\b\2\2\3I\3\3J\4\3K\5\3L\6")
        return buf.getvalue()


class D96Lexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    T__0 = 1
    CLASS_DECLARE = 2
    VAR_DECLARE = 3
    MEMBER = 4
    LIST_DATA = 5
    ID_LIST = 6
    METHODS = 7
    INT_TYPE = 8
    BOOL_TYPE = 9
    VOID_TYPE = 10
    ARRAY_TYPE = 11
    FLOAT_TYPE = 12
    PRIMITIVE_TYPE = 13
    INTLIT = 14
    ID = 15
    VAL = 16
    VAR = 17
    CLASS = 18
    DOLLAR = 19
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
    BREAK = 30
    FOREACH = 31
    BOOLEAN = 32
    NULL = 33
    CONTINUE = 34
    TRUE = 35
    FALSE = 36
    STRING = 37
    IF = 38
    ELSEIF = 39
    ARRAYINT = 40
    ELSE = 41
    FLOAT = 42
    RETURN = 43
    INTEGER_LITERAL = 44
    STRING_LITERAL = 45
    REAL_LITERAL = 46
    ADD = 47
    ADD_STR = 48
    SUB = 49
    MUL = 50
    DIV = 51
    MOD = 52
    NOT = 53
    NOTEQUAL = 54
    EQUAL = 55
    EQUAL_STR = 56
    AND = 57
    GT = 58
    OR = 59
    LTE = 60
    ASSIGN = 61
    GTE = 62
    WS = 63
    BLOCK_COMMENT = 64
    UNCLOSE_STRING = 65
    ILLEGAL_ESCAPE = 66
    ERROR_CHAR = 67
    UNTERMINATED_COMMENT = 68

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'main'", "'Int'", "'Void'", "'val'", "'var'", "'class'", "'$'", 
            "'('", "')'", "'{'", "'}'", "'['", "']'", "';'", "','", "':'", 
            "'..'", "'Break'", "'Foreach'", "'Boolean'", "'Null'", "'Continue'", 
            "'True'", "'False'", "'string'", "'if'", "'elseif'", "'Array Int'", 
            "'Else'", "'return'", "'+'", "'+.'", "'-'", "'*'", "'/'", "'%'", 
            "'!'", "'!='", "'=='", "'==.'", "'&&'", "'>'", "'||'", "'<='", 
            "'='", "'>='" ]

    symbolicNames = [ "<INVALID>",
            "CLASS_DECLARE", "VAR_DECLARE", "MEMBER", "LIST_DATA", "ID_LIST", 
            "METHODS", "INT_TYPE", "BOOL_TYPE", "VOID_TYPE", "ARRAY_TYPE", 
            "FLOAT_TYPE", "PRIMITIVE_TYPE", "INTLIT", "ID", "VAL", "VAR", 
            "CLASS", "DOLLAR", "LP", "RP", "LCB", "RCB", "LSB", "RSB", "SEMI", 
            "COMMA", "COLON", "DOTDOT", "BREAK", "FOREACH", "BOOLEAN", "NULL", 
            "CONTINUE", "TRUE", "FALSE", "STRING", "IF", "ELSEIF", "ARRAYINT", 
            "ELSE", "FLOAT", "RETURN", "INTEGER_LITERAL", "STRING_LITERAL", 
            "REAL_LITERAL", "ADD", "ADD_STR", "SUB", "MUL", "DIV", "MOD", 
            "NOT", "NOTEQUAL", "EQUAL", "EQUAL_STR", "AND", "GT", "OR", 
            "LTE", "ASSIGN", "GTE", "WS", "BLOCK_COMMENT", "UNCLOSE_STRING", 
            "ILLEGAL_ESCAPE", "ERROR_CHAR", "UNTERMINATED_COMMENT" ]

    ruleNames = [ "T__0", "CLASS_DECLARE", "VAR_DECLARE", "MEMBER", "LIST_DATA", 
                  "ID_LIST", "METHODS", "INT_TYPE", "BOOL_TYPE", "VOID_TYPE", 
                  "ARRAY_TYPE", "FLOAT_TYPE", "PRIMITIVE_TYPE", "INTLIT", 
                  "ID", "VAL", "VAR", "CLASS", "DOLLAR", "LP", "RP", "LCB", 
                  "RCB", "LSB", "RSB", "SEMI", "COMMA", "COLON", "DOTDOT", 
                  "DOT", "BREAK", "FOREACH", "BOOLEAN", "NULL", "CONTINUE", 
                  "TRUE", "FALSE", "STRING", "IF", "ELSEIF", "ARRAYINT", 
                  "ELSE", "FLOAT", "RETURN", "EXPONENT", "DIGIT", "SIGN", 
                  "INTEGER_LITERAL", "STRING_LITERAL", "REAL_LITERAL", "ADD", 
                  "ADD_STR", "SUB", "MUL", "DIV", "MOD", "NOT", "NOTEQUAL", 
                  "EQUAL", "EQUAL_STR", "AND", "GT", "OR", "LTE", "ASSIGN", 
                  "GTE", "WS", "BLOCK_COMMENT", "STR_CHAR", "ESC_SEQ", "ESC_ILLEGAL", 
                  "UNCLOSE_STRING", "ILLEGAL_ESCAPE", "ERROR_CHAR", "UNTERMINATED_COMMENT" ]

    grammarFileName = "D96.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.8")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


    def action(self, localctx:RuleContext, ruleIndex:int, actionIndex:int):
        if self._actions is None:
            actions = dict()
            actions[48] = self.STRING_LITERAL_action 
            actions[71] = self.UNCLOSE_STRING_action 
            actions[72] = self.ILLEGAL_ESCAPE_action 
            actions[73] = self.ERROR_CHAR_action 
            actions[74] = self.UNTERMINATED_COMMENT_action 
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
            	
     

    def UNCLOSE_STRING_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 1:

            		y = str(self.text)
            		possible = ['\b', '\t', '\n', '\f', '\r', '"', "'", '\\']
            		if y[-1] in possible:
            			raise UncloseString(y[1:-1])
            		else:
            			raise UncloseString(y[1:])
            	
     

    def ILLEGAL_ESCAPE_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 2:

            		y = str(self.text)
            		raise IllegalEscape(y[1:])
            	
     

    def ERROR_CHAR_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 3:

            		raise ErrorToken(self.text)
            	
     

    def UNTERMINATED_COMMENT_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 4:

            	raise ErrorToken('UNTERMINATED_COMMENT');

     


