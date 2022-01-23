# Generated from e:\HCMUT\PRINCIPLES_OF_PROGRAMMING_LANGUAGE\ppl-assignments\ASS_1\assignment1\src\main\d96\parser\D96.g4 by ANTLR 4.8
from antlr4 import *
from io import StringIO
from typing.io import TextIO
import sys


from lexererr import *
import inspect



def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2D")
        buf.write("\u0253\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7")
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
        buf.write("L\3\2\3\2\3\2\3\2\3\3\3\3\3\3\3\3\3\4\3\4\3\5\3\5\3\6")
        buf.write("\3\6\3\7\3\7\3\b\3\b\3\t\3\t\3\n\3\n\3\13\3\13\3\f\3\f")
        buf.write("\3\r\3\r\5\r\u00b6\n\r\3\r\3\r\3\16\6\16\u00bb\n\16\r")
        buf.write("\16\16\16\u00bc\3\17\3\17\3\17\3\17\3\17\3\17\3\20\3\20")
        buf.write("\3\20\3\20\3\20\3\20\3\20\3\20\3\20\3\21\3\21\3\21\3\22")
        buf.write("\3\22\3\22\3\22\3\22\3\22\3\22\3\23\3\23\3\23\3\23\3\23")
        buf.write("\3\24\3\24\3\24\3\24\3\24\3\24\3\24\3\24\3\25\3\25\3\25")
        buf.write("\3\25\3\25\3\26\3\26\3\26\3\26\3\26\3\26\3\27\3\27\3\27")
        buf.write("\3\27\3\27\3\27\3\30\3\30\3\30\3\31\3\31\3\31\3\31\3\31")
        buf.write("\3\31\3\31\3\31\3\32\3\32\3\32\3\32\3\32\3\32\3\32\3\33")
        buf.write("\3\33\3\33\3\33\3\33\3\34\3\34\3\34\3\34\3\34\3\34\3\34")
        buf.write("\3\34\3\34\3\34\3\34\3\34\3\35\3\35\3\35\3\35\3\35\3\35")
        buf.write("\3\35\3\35\3\35\3\35\3\35\3\36\3\36\3\36\3\36\3\37\3\37")
        buf.write("\3\37\3 \3 \3 \3 \3 \3!\3!\3\"\3\"\3#\3#\3$\3$\3%\3%\3")
        buf.write("&\3&\3\'\3\'\3\'\3(\3(\3(\3)\3)\3)\3*\3*\3+\3+\3+\3,\3")
        buf.write(",\3-\3-\3-\3.\3.\3/\3/\3/\3\60\3\60\3\60\3\60\3\61\3\61")
        buf.write("\3\61\3\62\3\62\3\63\3\63\3\63\3\64\3\64\3\64\3\65\3\65")
        buf.write("\3\65\3\65\3\65\3\65\3\65\3\65\3\66\3\66\3\66\3\66\3\66")
        buf.write("\3\67\3\67\3\67\3\67\3\67\3\67\38\38\38\38\38\38\39\3")
        buf.write("9\39\39\39\39\39\3:\3:\3:\3:\3;\3;\5;\u0189\n;\3<\3<\3")
        buf.write("<\3<\5<\u018f\n<\3=\3=\3=\3=\5=\u0195\n=\3=\3=\3=\3=\3")
        buf.write("=\5=\u019c\n=\3=\3=\5=\u01a0\n=\3=\6=\u01a3\n=\r=\16=")
        buf.write("\u01a4\7=\u01a7\n=\f=\16=\u01aa\13=\5=\u01ac\n=\3>\3>")
        buf.write("\3>\3>\3>\5>\u01b3\n>\3>\6>\u01b6\n>\r>\16>\u01b7\7>\u01ba")
        buf.write("\n>\f>\16>\u01bd\13>\5>\u01bf\n>\3?\3?\3?\3?\5?\u01c5")
        buf.write("\n?\3?\3?\3?\3?\3?\5?\u01cc\n?\3?\3?\5?\u01d0\n?\3?\6")
        buf.write("?\u01d3\n?\r?\16?\u01d4\7?\u01d7\n?\f?\16?\u01da\13?\5")
        buf.write("?\u01dc\n?\3@\3@\3@\5@\u01e1\n@\3@\6@\u01e4\n@\r@\16@")
        buf.write("\u01e5\7@\u01e8\n@\f@\16@\u01eb\13@\5@\u01ed\n@\3A\3A")
        buf.write("\3A\3A\5A\u01f3\nA\3B\3B\3B\3C\3C\3C\5C\u01fb\nC\3D\3")
        buf.write("D\7D\u01ff\nD\fD\16D\u0202\13D\3D\3D\3D\3E\3E\7E\u0209")
        buf.write("\nE\fE\16E\u020c\13E\3E\3E\3E\3F\3F\7F\u0213\nF\fF\16")
        buf.write("F\u0216\13F\3F\3F\3G\3G\3G\3G\5G\u021e\nG\3G\3G\3G\3G")
        buf.write("\5G\u0224\nG\3G\3G\3G\3G\3G\3G\3G\5G\u022d\nG\3H\3H\7")
        buf.write("H\u0231\nH\fH\16H\u0234\13H\3I\3I\6I\u0238\nI\rI\16I\u0239")
        buf.write("\3J\3J\3J\3J\7J\u0240\nJ\fJ\16J\u0243\13J\3J\3J\3J\3J")
        buf.write("\3J\3K\6K\u024b\nK\rK\16K\u024c\3K\3K\3L\3L\3L\3\u0241")
        buf.write("\2M\3\3\5\4\7\5\t\6\13\7\r\b\17\t\21\n\23\13\25\f\27\r")
        buf.write("\31\2\33\2\35\16\37\17!\20#\21%\22\'\23)\24+\25-\26/\27")
        buf.write("\61\30\63\31\65\32\67\339\34;\35=\36?\37A C!E\"G#I$K%")
        buf.write("M&O\'Q(S)U*W+Y,[-]._/a\60c\61e\62g\63i\64k\65m\66o\67")
        buf.write("q8s9u:w;y\2{\2}\2\177\2\u0081\2\u0083\2\u0085\2\u0087")
        buf.write("<\u0089=\u008b>\u008d?\u008f@\u0091A\u0093B\u0095C\u0097")
        buf.write("D\3\2\21\4\2GGgg\4\2--//\3\2\62;\4\2\62;CH\4\2\63;CH\3")
        buf.write("\2\629\3\2\639\3\2\62\63\3\2\63\63\3\2\63;\4\2$$^^\t\2")
        buf.write("))^^ddhhppttvv\5\2C\\aac|\6\2\62;C\\aac|\5\2\13\f\17\17")
        buf.write("\"\"\2\u0273\2\3\3\2\2\2\2\5\3\2\2\2\2\7\3\2\2\2\2\t\3")
        buf.write("\2\2\2\2\13\3\2\2\2\2\r\3\2\2\2\2\17\3\2\2\2\2\21\3\2")
        buf.write("\2\2\2\23\3\2\2\2\2\25\3\2\2\2\2\27\3\2\2\2\2\35\3\2\2")
        buf.write("\2\2\37\3\2\2\2\2!\3\2\2\2\2#\3\2\2\2\2%\3\2\2\2\2\'\3")
        buf.write("\2\2\2\2)\3\2\2\2\2+\3\2\2\2\2-\3\2\2\2\2/\3\2\2\2\2\61")
        buf.write("\3\2\2\2\2\63\3\2\2\2\2\65\3\2\2\2\2\67\3\2\2\2\29\3\2")
        buf.write("\2\2\2;\3\2\2\2\2=\3\2\2\2\2?\3\2\2\2\2A\3\2\2\2\2C\3")
        buf.write("\2\2\2\2E\3\2\2\2\2G\3\2\2\2\2I\3\2\2\2\2K\3\2\2\2\2M")
        buf.write("\3\2\2\2\2O\3\2\2\2\2Q\3\2\2\2\2S\3\2\2\2\2U\3\2\2\2\2")
        buf.write("W\3\2\2\2\2Y\3\2\2\2\2[\3\2\2\2\2]\3\2\2\2\2_\3\2\2\2")
        buf.write("\2a\3\2\2\2\2c\3\2\2\2\2e\3\2\2\2\2g\3\2\2\2\2i\3\2\2")
        buf.write("\2\2k\3\2\2\2\2m\3\2\2\2\2o\3\2\2\2\2q\3\2\2\2\2s\3\2")
        buf.write("\2\2\2u\3\2\2\2\2w\3\2\2\2\2\u0087\3\2\2\2\2\u0089\3\2")
        buf.write("\2\2\2\u008b\3\2\2\2\2\u008d\3\2\2\2\2\u008f\3\2\2\2\2")
        buf.write("\u0091\3\2\2\2\2\u0093\3\2\2\2\2\u0095\3\2\2\2\2\u0097")
        buf.write("\3\2\2\2\3\u0099\3\2\2\2\5\u009d\3\2\2\2\7\u00a1\3\2\2")
        buf.write("\2\t\u00a3\3\2\2\2\13\u00a5\3\2\2\2\r\u00a7\3\2\2\2\17")
        buf.write("\u00a9\3\2\2\2\21\u00ab\3\2\2\2\23\u00ad\3\2\2\2\25\u00af")
        buf.write("\3\2\2\2\27\u00b1\3\2\2\2\31\u00b3\3\2\2\2\33\u00ba\3")
        buf.write("\2\2\2\35\u00be\3\2\2\2\37\u00c4\3\2\2\2!\u00cd\3\2\2")
        buf.write("\2#\u00d0\3\2\2\2%\u00d7\3\2\2\2\'\u00dc\3\2\2\2)\u00e4")
        buf.write("\3\2\2\2+\u00e9\3\2\2\2-\u00ef\3\2\2\2/\u00f5\3\2\2\2")
        buf.write("\61\u00f8\3\2\2\2\63\u0100\3\2\2\2\65\u0107\3\2\2\2\67")
        buf.write("\u010c\3\2\2\29\u0118\3\2\2\2;\u0123\3\2\2\2=\u0127\3")
        buf.write("\2\2\2?\u012a\3\2\2\2A\u012f\3\2\2\2C\u0131\3\2\2\2E\u0133")
        buf.write("\3\2\2\2G\u0135\3\2\2\2I\u0137\3\2\2\2K\u0139\3\2\2\2")
        buf.write("M\u013b\3\2\2\2O\u013e\3\2\2\2Q\u0141\3\2\2\2S\u0144\3")
        buf.write("\2\2\2U\u0146\3\2\2\2W\u0149\3\2\2\2Y\u014b\3\2\2\2[\u014e")
        buf.write("\3\2\2\2]\u0150\3\2\2\2_\u0153\3\2\2\2a\u0157\3\2\2\2")
        buf.write("c\u015a\3\2\2\2e\u015c\3\2\2\2g\u015f\3\2\2\2i\u0162\3")
        buf.write("\2\2\2k\u016a\3\2\2\2m\u016f\3\2\2\2o\u0175\3\2\2\2q\u017b")
        buf.write("\3\2\2\2s\u0182\3\2\2\2u\u0188\3\2\2\2w\u018e\3\2\2\2")
        buf.write("y\u01ab\3\2\2\2{\u01be\3\2\2\2}\u01db\3\2\2\2\177\u01ec")
        buf.write("\3\2\2\2\u0081\u01f2\3\2\2\2\u0083\u01f4\3\2\2\2\u0085")
        buf.write("\u01fa\3\2\2\2\u0087\u01fc\3\2\2\2\u0089\u0206\3\2\2\2")
        buf.write("\u008b\u0210\3\2\2\2\u008d\u022c\3\2\2\2\u008f\u022e\3")
        buf.write("\2\2\2\u0091\u0235\3\2\2\2\u0093\u023b\3\2\2\2\u0095\u024a")
        buf.write("\3\2\2\2\u0097\u0250\3\2\2\2\u0099\u009a\7X\2\2\u009a")
        buf.write("\u009b\7c\2\2\u009b\u009c\7n\2\2\u009c\4\3\2\2\2\u009d")
        buf.write("\u009e\7X\2\2\u009e\u009f\7c\2\2\u009f\u00a0\7t\2\2\u00a0")
        buf.write("\6\3\2\2\2\u00a1\u00a2\7*\2\2\u00a2\b\3\2\2\2\u00a3\u00a4")
        buf.write("\7+\2\2\u00a4\n\3\2\2\2\u00a5\u00a6\7}\2\2\u00a6\f\3\2")
        buf.write("\2\2\u00a7\u00a8\7\177\2\2\u00a8\16\3\2\2\2\u00a9\u00aa")
        buf.write("\7]\2\2\u00aa\20\3\2\2\2\u00ab\u00ac\7_\2\2\u00ac\22\3")
        buf.write("\2\2\2\u00ad\u00ae\7=\2\2\u00ae\24\3\2\2\2\u00af\u00b0")
        buf.write("\7.\2\2\u00b0\26\3\2\2\2\u00b1\u00b2\7<\2\2\u00b2\30\3")
        buf.write("\2\2\2\u00b3\u00b5\t\2\2\2\u00b4\u00b6\t\3\2\2\u00b5\u00b4")
        buf.write("\3\2\2\2\u00b5\u00b6\3\2\2\2\u00b6\u00b7\3\2\2\2\u00b7")
        buf.write("\u00b8\5\33\16\2\u00b8\32\3\2\2\2\u00b9\u00bb\t\4\2\2")
        buf.write("\u00ba\u00b9\3\2\2\2\u00bb\u00bc\3\2\2\2\u00bc\u00ba\3")
        buf.write("\2\2\2\u00bc\u00bd\3\2\2\2\u00bd\34\3\2\2\2\u00be\u00bf")
        buf.write("\7D\2\2\u00bf\u00c0\7t\2\2\u00c0\u00c1\7g\2\2\u00c1\u00c2")
        buf.write("\7c\2\2\u00c2\u00c3\7m\2\2\u00c3\36\3\2\2\2\u00c4\u00c5")
        buf.write("\7E\2\2\u00c5\u00c6\7q\2\2\u00c6\u00c7\7p\2\2\u00c7\u00c8")
        buf.write("\7v\2\2\u00c8\u00c9\7k\2\2\u00c9\u00ca\7p\2\2\u00ca\u00cb")
        buf.write("\7w\2\2\u00cb\u00cc\7g\2\2\u00cc \3\2\2\2\u00cd\u00ce")
        buf.write("\7K\2\2\u00ce\u00cf\7h\2\2\u00cf\"\3\2\2\2\u00d0\u00d1")
        buf.write("\7G\2\2\u00d1\u00d2\7n\2\2\u00d2\u00d3\7u\2\2\u00d3\u00d4")
        buf.write("\7g\2\2\u00d4\u00d5\7k\2\2\u00d5\u00d6\7h\2\2\u00d6$\3")
        buf.write("\2\2\2\u00d7\u00d8\7G\2\2\u00d8\u00d9\7n\2\2\u00d9\u00da")
        buf.write("\7u\2\2\u00da\u00db\7g\2\2\u00db&\3\2\2\2\u00dc\u00dd")
        buf.write("\7H\2\2\u00dd\u00de\7q\2\2\u00de\u00df\7t\2\2\u00df\u00e0")
        buf.write("\7g\2\2\u00e0\u00e1\7c\2\2\u00e1\u00e2\7e\2\2\u00e2\u00e3")
        buf.write("\7j\2\2\u00e3(\3\2\2\2\u00e4\u00e5\7V\2\2\u00e5\u00e6")
        buf.write("\7t\2\2\u00e6\u00e7\7w\2\2\u00e7\u00e8\7g\2\2\u00e8*\3")
        buf.write("\2\2\2\u00e9\u00ea\7H\2\2\u00ea\u00eb\7c\2\2\u00eb\u00ec")
        buf.write("\7n\2\2\u00ec\u00ed\7u\2\2\u00ed\u00ee\7g\2\2\u00ee,\3")
        buf.write("\2\2\2\u00ef\u00f0\7C\2\2\u00f0\u00f1\7t\2\2\u00f1\u00f2")
        buf.write("\7t\2\2\u00f2\u00f3\7c\2\2\u00f3\u00f4\7{\2\2\u00f4.\3")
        buf.write("\2\2\2\u00f5\u00f6\7K\2\2\u00f6\u00f7\7p\2\2\u00f7\60")
        buf.write("\3\2\2\2\u00f8\u00f9\7D\2\2\u00f9\u00fa\7q\2\2\u00fa\u00fb")
        buf.write("\7q\2\2\u00fb\u00fc\7n\2\2\u00fc\u00fd\7g\2\2\u00fd\u00fe")
        buf.write("\7c\2\2\u00fe\u00ff\7p\2\2\u00ff\62\3\2\2\2\u0100\u0101")
        buf.write("\7T\2\2\u0101\u0102\7g\2\2\u0102\u0103\7v\2\2\u0103\u0104")
        buf.write("\7w\2\2\u0104\u0105\7t\2\2\u0105\u0106\7p\2\2\u0106\64")
        buf.write("\3\2\2\2\u0107\u0108\7P\2\2\u0108\u0109\7w\2\2\u0109\u010a")
        buf.write("\7n\2\2\u010a\u010b\7n\2\2\u010b\66\3\2\2\2\u010c\u010d")
        buf.write("\7E\2\2\u010d\u010e\7q\2\2\u010e\u010f\7p\2\2\u010f\u0110")
        buf.write("\7u\2\2\u0110\u0111\7v\2\2\u0111\u0112\7t\2\2\u0112\u0113")
        buf.write("\7w\2\2\u0113\u0114\7e\2\2\u0114\u0115\7v\2\2\u0115\u0116")
        buf.write("\7q\2\2\u0116\u0117\7t\2\2\u01178\3\2\2\2\u0118\u0119")
        buf.write("\7F\2\2\u0119\u011a\7g\2\2\u011a\u011b\7u\2\2\u011b\u011c")
        buf.write("\7v\2\2\u011c\u011d\7t\2\2\u011d\u011e\7w\2\2\u011e\u011f")
        buf.write("\7e\2\2\u011f\u0120\7v\2\2\u0120\u0121\7q\2\2\u0121\u0122")
        buf.write("\7t\2\2\u0122:\3\2\2\2\u0123\u0124\7P\2\2\u0124\u0125")
        buf.write("\7g\2\2\u0125\u0126\7y\2\2\u0126<\3\2\2\2\u0127\u0128")
        buf.write("\7D\2\2\u0128\u0129\7{\2\2\u0129>\3\2\2\2\u012a\u012b")
        buf.write("\7U\2\2\u012b\u012c\7g\2\2\u012c\u012d\7n\2\2\u012d\u012e")
        buf.write("\7h\2\2\u012e@\3\2\2\2\u012f\u0130\7-\2\2\u0130B\3\2\2")
        buf.write("\2\u0131\u0132\7/\2\2\u0132D\3\2\2\2\u0133\u0134\7,\2")
        buf.write("\2\u0134F\3\2\2\2\u0135\u0136\7\61\2\2\u0136H\3\2\2\2")
        buf.write("\u0137\u0138\7\'\2\2\u0138J\3\2\2\2\u0139\u013a\7#\2\2")
        buf.write("\u013aL\3\2\2\2\u013b\u013c\7(\2\2\u013c\u013d\7(\2\2")
        buf.write("\u013dN\3\2\2\2\u013e\u013f\7~\2\2\u013f\u0140\7~\2\2")
        buf.write("\u0140P\3\2\2\2\u0141\u0142\7?\2\2\u0142\u0143\7?\2\2")
        buf.write("\u0143R\3\2\2\2\u0144\u0145\7?\2\2\u0145T\3\2\2\2\u0146")
        buf.write("\u0147\7#\2\2\u0147\u0148\7?\2\2\u0148V\3\2\2\2\u0149")
        buf.write("\u014a\7@\2\2\u014aX\3\2\2\2\u014b\u014c\7@\2\2\u014c")
        buf.write("\u014d\7?\2\2\u014dZ\3\2\2\2\u014e\u014f\7>\2\2\u014f")
        buf.write("\\\3\2\2\2\u0150\u0151\7>\2\2\u0151\u0152\7?\2\2\u0152")
        buf.write("^\3\2\2\2\u0153\u0154\7?\2\2\u0154\u0155\7?\2\2\u0155")
        buf.write("\u0156\7\60\2\2\u0156`\3\2\2\2\u0157\u0158\7-\2\2\u0158")
        buf.write("\u0159\7\60\2\2\u0159b\3\2\2\2\u015a\u015b\7\60\2\2\u015b")
        buf.write("d\3\2\2\2\u015c\u015d\7\60\2\2\u015d\u015e\7\60\2\2\u015e")
        buf.write("f\3\2\2\2\u015f\u0160\7<\2\2\u0160\u0161\7<\2\2\u0161")
        buf.write("h\3\2\2\2\u0162\u0163\7R\2\2\u0163\u0164\7t\2\2\u0164")
        buf.write("\u0165\7q\2\2\u0165\u0166\7i\2\2\u0166\u0167\7t\2\2\u0167")
        buf.write("\u0168\7c\2\2\u0168\u0169\7o\2\2\u0169j\3\2\2\2\u016a")
        buf.write("\u016b\7o\2\2\u016b\u016c\7c\2\2\u016c\u016d\7k\2\2\u016d")
        buf.write("\u016e\7p\2\2\u016el\3\2\2\2\u016f\u0170\7E\2\2\u0170")
        buf.write("\u0171\7n\2\2\u0171\u0172\7c\2\2\u0172\u0173\7u\2\2\u0173")
        buf.write("\u0174\7u\2\2\u0174n\3\2\2\2\u0175\u0176\7H\2\2\u0176")
        buf.write("\u0177\7n\2\2\u0177\u0178\7q\2\2\u0178\u0179\7c\2\2\u0179")
        buf.write("\u017a\7v\2\2\u017ap\3\2\2\2\u017b\u017c\7U\2\2\u017c")
        buf.write("\u017d\7v\2\2\u017d\u017e\7t\2\2\u017e\u017f\7k\2\2\u017f")
        buf.write("\u0180\7p\2\2\u0180\u0181\7i\2\2\u0181r\3\2\2\2\u0182")
        buf.write("\u0183\7K\2\2\u0183\u0184\7p\2\2\u0184\u0185\7v\2\2\u0185")
        buf.write("t\3\2\2\2\u0186\u0189\5)\25\2\u0187\u0189\5+\26\2\u0188")
        buf.write("\u0186\3\2\2\2\u0188\u0187\3\2\2\2\u0189v\3\2\2\2\u018a")
        buf.write("\u018f\5{>\2\u018b\u018f\5}?\2\u018c\u018f\5\177@\2\u018d")
        buf.write("\u018f\5y=\2\u018e\u018a\3\2\2\2\u018e\u018b\3\2\2\2\u018e")
        buf.write("\u018c\3\2\2\2\u018e\u018d\3\2\2\2\u018fx\3\2\2\2\u0190")
        buf.write("\u0191\7\62\2\2\u0191\u0195\7z\2\2\u0192\u0193\7\62\2")
        buf.write("\2\u0193\u0195\7Z\2\2\u0194\u0190\3\2\2\2\u0194\u0192")
        buf.write("\3\2\2\2\u0195\u0196\3\2\2\2\u0196\u01ac\t\5\2\2\u0197")
        buf.write("\u0198\7\62\2\2\u0198\u019c\7z\2\2\u0199\u019a\7\62\2")
        buf.write("\2\u019a\u019c\7Z\2\2\u019b\u0197\3\2\2\2\u019b\u0199")
        buf.write("\3\2\2\2\u019c\u019d\3\2\2\2\u019d\u01a8\t\6\2\2\u019e")
        buf.write("\u01a0\7a\2\2\u019f\u019e\3\2\2\2\u019f\u01a0\3\2\2\2")
        buf.write("\u01a0\u01a2\3\2\2\2\u01a1\u01a3\t\5\2\2\u01a2\u01a1\3")
        buf.write("\2\2\2\u01a3\u01a4\3\2\2\2\u01a4\u01a2\3\2\2\2\u01a4\u01a5")
        buf.write("\3\2\2\2\u01a5\u01a7\3\2\2\2\u01a6\u019f\3\2\2\2\u01a7")
        buf.write("\u01aa\3\2\2\2\u01a8\u01a6\3\2\2\2\u01a8\u01a9\3\2\2\2")
        buf.write("\u01a9\u01ac\3\2\2\2\u01aa\u01a8\3\2\2\2\u01ab\u0194\3")
        buf.write("\2\2\2\u01ab\u019b\3\2\2\2\u01acz\3\2\2\2\u01ad\u01ae")
        buf.write("\7\62\2\2\u01ae\u01bf\t\7\2\2\u01af\u01b0\7\62\2\2\u01b0")
        buf.write("\u01bb\t\b\2\2\u01b1\u01b3\7a\2\2\u01b2\u01b1\3\2\2\2")
        buf.write("\u01b2\u01b3\3\2\2\2\u01b3\u01b5\3\2\2\2\u01b4\u01b6\t")
        buf.write("\7\2\2\u01b5\u01b4\3\2\2\2\u01b6\u01b7\3\2\2\2\u01b7\u01b5")
        buf.write("\3\2\2\2\u01b7\u01b8\3\2\2\2\u01b8\u01ba\3\2\2\2\u01b9")
        buf.write("\u01b2\3\2\2\2\u01ba\u01bd\3\2\2\2\u01bb\u01b9\3\2\2\2")
        buf.write("\u01bb\u01bc\3\2\2\2\u01bc\u01bf\3\2\2\2\u01bd\u01bb\3")
        buf.write("\2\2\2\u01be\u01ad\3\2\2\2\u01be\u01af\3\2\2\2\u01bf|")
        buf.write("\3\2\2\2\u01c0\u01c1\7\62\2\2\u01c1\u01c5\7d\2\2\u01c2")
        buf.write("\u01c3\7\62\2\2\u01c3\u01c5\7D\2\2\u01c4\u01c0\3\2\2\2")
        buf.write("\u01c4\u01c2\3\2\2\2\u01c5\u01c6\3\2\2\2\u01c6\u01dc\t")
        buf.write("\t\2\2\u01c7\u01c8\7\62\2\2\u01c8\u01cc\7d\2\2\u01c9\u01ca")
        buf.write("\7\62\2\2\u01ca\u01cc\7D\2\2\u01cb\u01c7\3\2\2\2\u01cb")
        buf.write("\u01c9\3\2\2\2\u01cc\u01cd\3\2\2\2\u01cd\u01d8\t\n\2\2")
        buf.write("\u01ce\u01d0\7a\2\2\u01cf\u01ce\3\2\2\2\u01cf\u01d0\3")
        buf.write("\2\2\2\u01d0\u01d2\3\2\2\2\u01d1\u01d3\t\t\2\2\u01d2\u01d1")
        buf.write("\3\2\2\2\u01d3\u01d4\3\2\2\2\u01d4\u01d2\3\2\2\2\u01d4")
        buf.write("\u01d5\3\2\2\2\u01d5\u01d7\3\2\2\2\u01d6\u01cf\3\2\2\2")
        buf.write("\u01d7\u01da\3\2\2\2\u01d8\u01d6\3\2\2\2\u01d8\u01d9\3")
        buf.write("\2\2\2\u01d9\u01dc\3\2\2\2\u01da\u01d8\3\2\2\2\u01db\u01c4")
        buf.write("\3\2\2\2\u01db\u01cb\3\2\2\2\u01dc~\3\2\2\2\u01dd\u01ed")
        buf.write("\t\4\2\2\u01de\u01e9\t\13\2\2\u01df\u01e1\7a\2\2\u01e0")
        buf.write("\u01df\3\2\2\2\u01e0\u01e1\3\2\2\2\u01e1\u01e3\3\2\2\2")
        buf.write("\u01e2\u01e4\t\4\2\2\u01e3\u01e2\3\2\2\2\u01e4\u01e5\3")
        buf.write("\2\2\2\u01e5\u01e3\3\2\2\2\u01e5\u01e6\3\2\2\2\u01e6\u01e8")
        buf.write("\3\2\2\2\u01e7\u01e0\3\2\2\2\u01e8\u01eb\3\2\2\2\u01e9")
        buf.write("\u01e7\3\2\2\2\u01e9\u01ea\3\2\2\2\u01ea\u01ed\3\2\2\2")
        buf.write("\u01eb\u01e9\3\2\2\2\u01ec\u01dd\3\2\2\2\u01ec\u01de\3")
        buf.write("\2\2\2\u01ed\u0080\3\2\2\2\u01ee\u01ef\7)\2\2\u01ef\u01f3")
        buf.write("\7$\2\2\u01f0\u01f3\n\f\2\2\u01f1\u01f3\5\u0083B\2\u01f2")
        buf.write("\u01ee\3\2\2\2\u01f2\u01f0\3\2\2\2\u01f2\u01f1\3\2\2\2")
        buf.write("\u01f3\u0082\3\2\2\2\u01f4\u01f5\7^\2\2\u01f5\u01f6\t")
        buf.write("\r\2\2\u01f6\u0084\3\2\2\2\u01f7\u01f8\7^\2\2\u01f8\u01fb")
        buf.write("\n\r\2\2\u01f9\u01fb\7^\2\2\u01fa\u01f7\3\2\2\2\u01fa")
        buf.write("\u01f9\3\2\2\2\u01fb\u0086\3\2\2\2\u01fc\u0200\7$\2\2")
        buf.write("\u01fd\u01ff\5\u0081A\2\u01fe\u01fd\3\2\2\2\u01ff\u0202")
        buf.write("\3\2\2\2\u0200\u01fe\3\2\2\2\u0200\u0201\3\2\2\2\u0201")
        buf.write("\u0203\3\2\2\2\u0202\u0200\3\2\2\2\u0203\u0204\7$\2\2")
        buf.write("\u0204\u0205\bD\2\2\u0205\u0088\3\2\2\2\u0206\u020a\7")
        buf.write("$\2\2\u0207\u0209\5\u0081A\2\u0208\u0207\3\2\2\2\u0209")
        buf.write("\u020c\3\2\2\2\u020a\u0208\3\2\2\2\u020a\u020b\3\2\2\2")
        buf.write("\u020b\u020d\3\2\2\2\u020c\u020a\3\2\2\2\u020d\u020e\5")
        buf.write("\u0085C\2\u020e\u020f\bE\3\2\u020f\u008a\3\2\2\2\u0210")
        buf.write("\u0214\7$\2\2\u0211\u0213\5\u0081A\2\u0212\u0211\3\2\2")
        buf.write("\2\u0213\u0216\3\2\2\2\u0214\u0212\3\2\2\2\u0214\u0215")
        buf.write("\3\2\2\2\u0215\u0217\3\2\2\2\u0216\u0214\3\2\2\2\u0217")
        buf.write("\u0218\bF\4\2\u0218\u008c\3\2\2\2\u0219\u021a\5\177@\2")
        buf.write("\u021a\u021d\5c\62\2\u021b\u021e\5\33\16\2\u021c\u021e")
        buf.write("\5\31\r\2\u021d\u021b\3\2\2\2\u021d\u021c\3\2\2\2\u021d")
        buf.write("\u021e\3\2\2\2\u021e\u022d\3\2\2\2\u021f\u0220\5\177@")
        buf.write("\2\u0220\u0221\5\31\r\2\u0221\u022d\3\2\2\2\u0222\u0224")
        buf.write("\5\177@\2\u0223\u0222\3\2\2\2\u0223\u0224\3\2\2\2\u0224")
        buf.write("\u0225\3\2\2\2\u0225\u0226\5c\62\2\u0226\u0227\5\33\16")
        buf.write("\2\u0227\u0228\5\31\r\2\u0228\u022d\3\2\2\2\u0229\u022a")
        buf.write("\5c\62\2\u022a\u022b\5\31\r\2\u022b\u022d\3\2\2\2\u022c")
        buf.write("\u0219\3\2\2\2\u022c\u021f\3\2\2\2\u022c\u0223\3\2\2\2")
        buf.write("\u022c\u0229\3\2\2\2\u022d\u008e\3\2\2\2\u022e\u0232\t")
        buf.write("\16\2\2\u022f\u0231\t\17\2\2\u0230\u022f\3\2\2\2\u0231")
        buf.write("\u0234\3\2\2\2\u0232\u0230\3\2\2\2\u0232\u0233\3\2\2\2")
        buf.write("\u0233\u0090\3\2\2\2\u0234\u0232\3\2\2\2\u0235\u0237\7")
        buf.write("&\2\2\u0236\u0238\t\17\2\2\u0237\u0236\3\2\2\2\u0238\u0239")
        buf.write("\3\2\2\2\u0239\u0237\3\2\2\2\u0239\u023a\3\2\2\2\u023a")
        buf.write("\u0092\3\2\2\2\u023b\u023c\7%\2\2\u023c\u023d\7%\2\2\u023d")
        buf.write("\u0241\3\2\2\2\u023e\u0240\13\2\2\2\u023f\u023e\3\2\2")
        buf.write("\2\u0240\u0243\3\2\2\2\u0241\u0242\3\2\2\2\u0241\u023f")
        buf.write("\3\2\2\2\u0242\u0244\3\2\2\2\u0243\u0241\3\2\2\2\u0244")
        buf.write("\u0245\7%\2\2\u0245\u0246\7%\2\2\u0246\u0247\3\2\2\2\u0247")
        buf.write("\u0248\bJ\5\2\u0248\u0094\3\2\2\2\u0249\u024b\t\20\2\2")
        buf.write("\u024a\u0249\3\2\2\2\u024b\u024c\3\2\2\2\u024c\u024a\3")
        buf.write("\2\2\2\u024c\u024d\3\2\2\2\u024d\u024e\3\2\2\2\u024e\u024f")
        buf.write("\bK\5\2\u024f\u0096\3\2\2\2\u0250\u0251\13\2\2\2\u0251")
        buf.write("\u0252\bL\6\2\u0252\u0098\3\2\2\2\'\2\u00b5\u00bc\u0188")
        buf.write("\u018e\u0194\u019b\u019f\u01a4\u01a8\u01ab\u01b2\u01b7")
        buf.write("\u01bb\u01be\u01c4\u01cb\u01cf\u01d4\u01d8\u01db\u01e0")
        buf.write("\u01e5\u01e9\u01ec\u01f2\u01fa\u0200\u020a\u0214\u021d")
        buf.write("\u0223\u022c\u0232\u0239\u0241\u024c\7\3D\2\3E\3\3F\4")
        buf.write("\b\2\2\3L\5")
        return buf.getvalue()


class D96Lexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    VAL = 1
    VAR = 2
    LP = 3
    RP = 4
    LCB = 5
    RCB = 6
    LSB = 7
    RSB = 8
    SEMI = 9
    COMMA = 10
    COLON = 11
    BREAK = 12
    CONTINUE = 13
    IF = 14
    ELSEIF = 15
    ELSE = 16
    FOREACH = 17
    TRUE = 18
    FALSE = 19
    ARRAY = 20
    IN = 21
    BOOLEAN = 22
    RETURN = 23
    NULL = 24
    CONSTRUCTOR = 25
    DESTRUCTOR = 26
    NEW = 27
    BY = 28
    SELF = 29
    ADD = 30
    SUB = 31
    MUL = 32
    DIV = 33
    MOD = 34
    NOT = 35
    AND = 36
    OR = 37
    EQUAL = 38
    ASSIGN = 39
    NOTEQUAL = 40
    GT = 41
    GTE = 42
    LT = 43
    LTE = 44
    EQUAL_STR = 45
    ADD_STR = 46
    DOT = 47
    DOTDOT = 48
    SCOPE = 49
    PROGRAM = 50
    MAIN = 51
    CLASS = 52
    FLOAT_TYPE = 53
    STRING = 54
    INT_TYPE = 55
    BOOL_LITERAL = 56
    INTEGER_LITERAL = 57
    STRING_LITERAL = 58
    ILLEGAL_ESCAPE = 59
    UNCLOSE_STRING = 60
    REAL_LITERAL = 61
    NORMAL_ID = 62
    DOLLAR_ID = 63
    BLOCK_COMMENT = 64
    WS = 65
    ERROR_CHAR = 66

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'Val'", "'Var'", "'('", "')'", "'{'", "'}'", "'['", "']'", 
            "';'", "','", "':'", "'Break'", "'Continue'", "'If'", "'Elseif'", 
            "'Else'", "'Foreach'", "'True'", "'False'", "'Array'", "'In'", 
            "'Boolean'", "'Return'", "'Null'", "'Constructor'", "'Destructor'", 
            "'New'", "'By'", "'Self'", "'+'", "'-'", "'*'", "'/'", "'%'", 
            "'!'", "'&&'", "'||'", "'=='", "'='", "'!='", "'>'", "'>='", 
            "'<'", "'<='", "'==.'", "'+.'", "'.'", "'..'", "'::'", "'Program'", 
            "'main'", "'Class'", "'Float'", "'String'", "'Int'" ]

    symbolicNames = [ "<INVALID>",
            "VAL", "VAR", "LP", "RP", "LCB", "RCB", "LSB", "RSB", "SEMI", 
            "COMMA", "COLON", "BREAK", "CONTINUE", "IF", "ELSEIF", "ELSE", 
            "FOREACH", "TRUE", "FALSE", "ARRAY", "IN", "BOOLEAN", "RETURN", 
            "NULL", "CONSTRUCTOR", "DESTRUCTOR", "NEW", "BY", "SELF", "ADD", 
            "SUB", "MUL", "DIV", "MOD", "NOT", "AND", "OR", "EQUAL", "ASSIGN", 
            "NOTEQUAL", "GT", "GTE", "LT", "LTE", "EQUAL_STR", "ADD_STR", 
            "DOT", "DOTDOT", "SCOPE", "PROGRAM", "MAIN", "CLASS", "FLOAT_TYPE", 
            "STRING", "INT_TYPE", "BOOL_LITERAL", "INTEGER_LITERAL", "STRING_LITERAL", 
            "ILLEGAL_ESCAPE", "UNCLOSE_STRING", "REAL_LITERAL", "NORMAL_ID", 
            "DOLLAR_ID", "BLOCK_COMMENT", "WS", "ERROR_CHAR" ]

    ruleNames = [ "VAL", "VAR", "LP", "RP", "LCB", "RCB", "LSB", "RSB", 
                  "SEMI", "COMMA", "COLON", "EXPONENT", "DEC_DIGIT", "BREAK", 
                  "CONTINUE", "IF", "ELSEIF", "ELSE", "FOREACH", "TRUE", 
                  "FALSE", "ARRAY", "IN", "BOOLEAN", "RETURN", "NULL", "CONSTRUCTOR", 
                  "DESTRUCTOR", "NEW", "BY", "SELF", "ADD", "SUB", "MUL", 
                  "DIV", "MOD", "NOT", "AND", "OR", "EQUAL", "ASSIGN", "NOTEQUAL", 
                  "GT", "GTE", "LT", "LTE", "EQUAL_STR", "ADD_STR", "DOT", 
                  "DOTDOT", "SCOPE", "PROGRAM", "MAIN", "CLASS", "FLOAT_TYPE", 
                  "STRING", "INT_TYPE", "BOOL_LITERAL", "INTEGER_LITERAL", 
                  "HEX_TYPE", "OCT_TYPE", "BIN_TYPE", "DEC_TYPE", "STR", 
                  "ESC_SEQ", "ESC_ILLEGAL", "STRING_LITERAL", "ILLEGAL_ESCAPE", 
                  "UNCLOSE_STRING", "REAL_LITERAL", "NORMAL_ID", "DOLLAR_ID", 
                  "BLOCK_COMMENT", "WS", "ERROR_CHAR" ]

    grammarFileName = "D96.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.8")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


    def emit(self):
        tk = self.type
        result = super().emit()
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
            actions[66] = self.STRING_LITERAL_action 
            actions[67] = self.ILLEGAL_ESCAPE_action 
            actions[68] = self.UNCLOSE_STRING_action 
            actions[74] = self.ERROR_CHAR_action 
            self._actions = actions
        action = self._actions.get(ruleIndex, None)
        if action is not None:
            action(localctx, actionIndex)
        else:
            raise Exception("No registered action for:" + str(ruleIndex))


    def STRING_LITERAL_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 0:
             
                y = str(self.text)
                idx = y.find('\n')
                if idx >= 0:
                    raise UncloseString(y[1:idx-1])
                self.text = y[1:-1]

     

    def ILLEGAL_ESCAPE_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 1:

                raise IllegalEscape(str(self.text)[1:])

     

    def UNCLOSE_STRING_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 2:

                raise UncloseString(str(self.text)[1:])

     

    def ERROR_CHAR_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 3:
            raise ErrorToken(self.text)
     


