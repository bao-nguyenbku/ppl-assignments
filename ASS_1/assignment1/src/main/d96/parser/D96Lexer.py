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
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2E")
        buf.write("\u02c2\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7")
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
        buf.write("L\4M\tM\4N\tN\4O\tO\4P\tP\4Q\tQ\3\2\3\2\3\2\3\2\3\3\3")
        buf.write("\3\3\3\3\3\3\4\3\4\3\5\3\5\3\6\3\6\3\7\3\7\3\b\3\b\3\t")
        buf.write("\3\t\3\n\3\n\3\13\3\13\3\f\3\f\3\r\3\r\5\r\u00c0\n\r\3")
        buf.write("\r\3\r\3\16\6\16\u00c5\n\16\r\16\16\16\u00c6\3\17\3\17")
        buf.write("\3\17\3\17\3\17\3\17\3\20\3\20\3\20\3\20\3\20\3\20\3\20")
        buf.write("\3\20\3\20\3\21\3\21\3\21\3\22\3\22\3\22\3\22\3\22\3\22")
        buf.write("\3\22\3\23\3\23\3\23\3\23\3\23\3\24\3\24\3\24\3\24\3\24")
        buf.write("\3\24\3\24\3\24\3\25\3\25\3\25\3\25\3\25\3\26\3\26\3\26")
        buf.write("\3\26\3\26\3\26\3\27\3\27\3\27\3\27\3\27\3\27\3\30\3\30")
        buf.write("\3\30\3\31\3\31\3\31\3\31\3\31\3\31\3\31\3\31\3\32\3\32")
        buf.write("\3\32\3\32\3\32\3\32\3\32\3\33\3\33\3\33\3\33\3\33\3\34")
        buf.write("\3\34\3\34\3\34\3\34\3\34\3\34\3\34\3\34\3\34\3\34\3\34")
        buf.write("\3\35\3\35\3\35\3\35\3\35\3\35\3\35\3\35\3\35\3\35\3\35")
        buf.write("\3\36\3\36\3\36\3\36\3\37\3\37\3\37\3 \3 \3 \3 \3 \3!")
        buf.write("\3!\3\"\3\"\3#\3#\3$\3$\3%\3%\3&\3&\3\'\3\'\3\'\3(\3(")
        buf.write("\3(\3)\3)\3)\3*\3*\3+\3+\3+\3,\3,\3-\3-\3-\3.\3.\3/\3")
        buf.write("/\3/\3\60\3\60\3\60\3\60\3\61\3\61\3\61\3\62\3\62\3\63")
        buf.write("\3\63\3\63\3\64\3\64\3\64\3\65\3\65\3\65\3\65\3\65\3\65")
        buf.write("\3\65\3\65\3\66\3\66\3\66\3\66\3\66\3\67\3\67\3\67\3\67")
        buf.write("\3\67\3\67\38\38\38\38\38\38\39\39\39\39\39\39\39\3:\3")
        buf.write(":\3:\3:\3;\3;\5;\u0193\n;\3<\3<\3<\3<\5<\u0199\n<\3=\3")
        buf.write("=\3=\3=\5=\u019f\n=\3=\3=\3=\3=\3=\5=\u01a6\n=\3=\3=\5")
        buf.write("=\u01aa\n=\3=\6=\u01ad\n=\r=\16=\u01ae\7=\u01b1\n=\f=")
        buf.write("\16=\u01b4\13=\5=\u01b6\n=\3>\3>\3>\3>\3>\5>\u01bd\n>")
        buf.write("\3>\6>\u01c0\n>\r>\16>\u01c1\7>\u01c4\n>\f>\16>\u01c7")
        buf.write("\13>\5>\u01c9\n>\3?\3?\3?\3?\3?\3?\5?\u01d1\n?\3?\3?\3")
        buf.write("?\3?\5?\u01d7\n?\3?\3?\5?\u01db\n?\3?\6?\u01de\n?\r?\16")
        buf.write("?\u01df\7?\u01e2\n?\f?\16?\u01e5\13?\5?\u01e7\n?\3@\3")
        buf.write("@\3@\5@\u01ec\n@\3@\6@\u01ef\n@\r@\16@\u01f0\7@\u01f3")
        buf.write("\n@\f@\16@\u01f6\13@\5@\u01f8\n@\3A\3A\3A\3A\5A\u01fe")
        buf.write("\nA\3B\3B\3B\3B\5B\u0204\nB\3B\3B\3B\3B\3B\5B\u020b\n")
        buf.write("B\3B\3B\5B\u020f\nB\3B\6B\u0212\nB\rB\16B\u0213\7B\u0216")
        buf.write("\nB\fB\16B\u0219\13B\5B\u021b\nB\3C\3C\3C\3C\3C\5C\u0222")
        buf.write("\nC\3C\6C\u0225\nC\rC\16C\u0226\7C\u0229\nC\fC\16C\u022c")
        buf.write("\13C\5C\u022e\nC\3D\3D\3D\3D\5D\u0234\nD\3D\3D\3D\3D\3")
        buf.write("D\5D\u023b\nD\3D\3D\5D\u023f\nD\3D\6D\u0242\nD\rD\16D")
        buf.write("\u0243\7D\u0246\nD\fD\16D\u0249\13D\5D\u024b\nD\3E\3E")
        buf.write("\3E\5E\u0250\nE\3E\6E\u0253\nE\rE\16E\u0254\7E\u0257\n")
        buf.write("E\fE\16E\u025a\13E\5E\u025c\nE\3F\3F\3F\3F\5F\u0262\n")
        buf.write("F\3G\3G\3G\3H\3H\3H\5H\u026a\nH\3I\3I\7I\u026e\nI\fI\16")
        buf.write("I\u0271\13I\3I\3I\3I\3J\3J\7J\u0278\nJ\fJ\16J\u027b\13")
        buf.write("J\3J\3J\3J\3K\3K\7K\u0282\nK\fK\16K\u0285\13K\3K\3K\3")
        buf.write("L\3L\3L\3L\5L\u028d\nL\3L\3L\3L\3L\5L\u0293\nL\3L\3L\3")
        buf.write("L\3L\3L\3L\3L\5L\u029c\nL\3M\3M\7M\u02a0\nM\fM\16M\u02a3")
        buf.write("\13M\3N\3N\6N\u02a7\nN\rN\16N\u02a8\3O\3O\3O\3O\7O\u02af")
        buf.write("\nO\fO\16O\u02b2\13O\3O\3O\3O\3O\3O\3P\6P\u02ba\nP\rP")
        buf.write("\16P\u02bb\3P\3P\3Q\3Q\3Q\3\u02b0\2R\3\3\5\4\7\5\t\6\13")
        buf.write("\7\r\b\17\t\21\n\23\13\25\f\27\r\31\2\33\2\35\16\37\17")
        buf.write("!\20#\21%\22\'\23)\24+\25-\26/\27\61\30\63\31\65\32\67")
        buf.write("\339\34;\35=\36?\37A C!E\"G#I$K%M&O\'Q(S)U*W+Y,[-]._/")
        buf.write("a\60c\61e\62g\63i\64k\65m\66o\67q8s9u:w;y\2{\2}\2\177")
        buf.write("\2\u0081<\u0083\2\u0085\2\u0087\2\u0089\2\u008b\2\u008d")
        buf.write("\2\u008f\2\u0091=\u0093>\u0095?\u0097@\u0099A\u009bB\u009d")
        buf.write("C\u009fD\u00a1E\3\2\21\4\2GGgg\4\2--//\3\2\62;\4\2\63")
        buf.write(";CH\4\2\62;CH\3\2\639\3\2\629\3\2\63\63\3\2\62\63\3\2")
        buf.write("\63;\4\2$$^^\t\2))^^ddhhppttvv\5\2C\\aac|\6\2\62;C\\a")
        buf.write("ac|\5\2\13\f\17\17\"\"\2\u02f5\2\3\3\2\2\2\2\5\3\2\2\2")
        buf.write("\2\7\3\2\2\2\2\t\3\2\2\2\2\13\3\2\2\2\2\r\3\2\2\2\2\17")
        buf.write("\3\2\2\2\2\21\3\2\2\2\2\23\3\2\2\2\2\25\3\2\2\2\2\27\3")
        buf.write("\2\2\2\2\35\3\2\2\2\2\37\3\2\2\2\2!\3\2\2\2\2#\3\2\2\2")
        buf.write("\2%\3\2\2\2\2\'\3\2\2\2\2)\3\2\2\2\2+\3\2\2\2\2-\3\2\2")
        buf.write("\2\2/\3\2\2\2\2\61\3\2\2\2\2\63\3\2\2\2\2\65\3\2\2\2\2")
        buf.write("\67\3\2\2\2\29\3\2\2\2\2;\3\2\2\2\2=\3\2\2\2\2?\3\2\2")
        buf.write("\2\2A\3\2\2\2\2C\3\2\2\2\2E\3\2\2\2\2G\3\2\2\2\2I\3\2")
        buf.write("\2\2\2K\3\2\2\2\2M\3\2\2\2\2O\3\2\2\2\2Q\3\2\2\2\2S\3")
        buf.write("\2\2\2\2U\3\2\2\2\2W\3\2\2\2\2Y\3\2\2\2\2[\3\2\2\2\2]")
        buf.write("\3\2\2\2\2_\3\2\2\2\2a\3\2\2\2\2c\3\2\2\2\2e\3\2\2\2\2")
        buf.write("g\3\2\2\2\2i\3\2\2\2\2k\3\2\2\2\2m\3\2\2\2\2o\3\2\2\2")
        buf.write("\2q\3\2\2\2\2s\3\2\2\2\2u\3\2\2\2\2w\3\2\2\2\2\u0081\3")
        buf.write("\2\2\2\2\u0091\3\2\2\2\2\u0093\3\2\2\2\2\u0095\3\2\2\2")
        buf.write("\2\u0097\3\2\2\2\2\u0099\3\2\2\2\2\u009b\3\2\2\2\2\u009d")
        buf.write("\3\2\2\2\2\u009f\3\2\2\2\2\u00a1\3\2\2\2\3\u00a3\3\2\2")
        buf.write("\2\5\u00a7\3\2\2\2\7\u00ab\3\2\2\2\t\u00ad\3\2\2\2\13")
        buf.write("\u00af\3\2\2\2\r\u00b1\3\2\2\2\17\u00b3\3\2\2\2\21\u00b5")
        buf.write("\3\2\2\2\23\u00b7\3\2\2\2\25\u00b9\3\2\2\2\27\u00bb\3")
        buf.write("\2\2\2\31\u00bd\3\2\2\2\33\u00c4\3\2\2\2\35\u00c8\3\2")
        buf.write("\2\2\37\u00ce\3\2\2\2!\u00d7\3\2\2\2#\u00da\3\2\2\2%\u00e1")
        buf.write("\3\2\2\2\'\u00e6\3\2\2\2)\u00ee\3\2\2\2+\u00f3\3\2\2\2")
        buf.write("-\u00f9\3\2\2\2/\u00ff\3\2\2\2\61\u0102\3\2\2\2\63\u010a")
        buf.write("\3\2\2\2\65\u0111\3\2\2\2\67\u0116\3\2\2\29\u0122\3\2")
        buf.write("\2\2;\u012d\3\2\2\2=\u0131\3\2\2\2?\u0134\3\2\2\2A\u0139")
        buf.write("\3\2\2\2C\u013b\3\2\2\2E\u013d\3\2\2\2G\u013f\3\2\2\2")
        buf.write("I\u0141\3\2\2\2K\u0143\3\2\2\2M\u0145\3\2\2\2O\u0148\3")
        buf.write("\2\2\2Q\u014b\3\2\2\2S\u014e\3\2\2\2U\u0150\3\2\2\2W\u0153")
        buf.write("\3\2\2\2Y\u0155\3\2\2\2[\u0158\3\2\2\2]\u015a\3\2\2\2")
        buf.write("_\u015d\3\2\2\2a\u0161\3\2\2\2c\u0164\3\2\2\2e\u0166\3")
        buf.write("\2\2\2g\u0169\3\2\2\2i\u016c\3\2\2\2k\u0174\3\2\2\2m\u0179")
        buf.write("\3\2\2\2o\u017f\3\2\2\2q\u0185\3\2\2\2s\u018c\3\2\2\2")
        buf.write("u\u0192\3\2\2\2w\u0198\3\2\2\2y\u01b5\3\2\2\2{\u01c8\3")
        buf.write("\2\2\2}\u01e6\3\2\2\2\177\u01f7\3\2\2\2\u0081\u01fd\3")
        buf.write("\2\2\2\u0083\u021a\3\2\2\2\u0085\u022d\3\2\2\2\u0087\u024a")
        buf.write("\3\2\2\2\u0089\u025b\3\2\2\2\u008b\u0261\3\2\2\2\u008d")
        buf.write("\u0263\3\2\2\2\u008f\u0269\3\2\2\2\u0091\u026b\3\2\2\2")
        buf.write("\u0093\u0275\3\2\2\2\u0095\u027f\3\2\2\2\u0097\u029b\3")
        buf.write("\2\2\2\u0099\u029d\3\2\2\2\u009b\u02a4\3\2\2\2\u009d\u02aa")
        buf.write("\3\2\2\2\u009f\u02b9\3\2\2\2\u00a1\u02bf\3\2\2\2\u00a3")
        buf.write("\u00a4\7X\2\2\u00a4\u00a5\7c\2\2\u00a5\u00a6\7n\2\2\u00a6")
        buf.write("\4\3\2\2\2\u00a7\u00a8\7X\2\2\u00a8\u00a9\7c\2\2\u00a9")
        buf.write("\u00aa\7t\2\2\u00aa\6\3\2\2\2\u00ab\u00ac\7*\2\2\u00ac")
        buf.write("\b\3\2\2\2\u00ad\u00ae\7+\2\2\u00ae\n\3\2\2\2\u00af\u00b0")
        buf.write("\7}\2\2\u00b0\f\3\2\2\2\u00b1\u00b2\7\177\2\2\u00b2\16")
        buf.write("\3\2\2\2\u00b3\u00b4\7]\2\2\u00b4\20\3\2\2\2\u00b5\u00b6")
        buf.write("\7_\2\2\u00b6\22\3\2\2\2\u00b7\u00b8\7=\2\2\u00b8\24\3")
        buf.write("\2\2\2\u00b9\u00ba\7.\2\2\u00ba\26\3\2\2\2\u00bb\u00bc")
        buf.write("\7<\2\2\u00bc\30\3\2\2\2\u00bd\u00bf\t\2\2\2\u00be\u00c0")
        buf.write("\t\3\2\2\u00bf\u00be\3\2\2\2\u00bf\u00c0\3\2\2\2\u00c0")
        buf.write("\u00c1\3\2\2\2\u00c1\u00c2\5\33\16\2\u00c2\32\3\2\2\2")
        buf.write("\u00c3\u00c5\t\4\2\2\u00c4\u00c3\3\2\2\2\u00c5\u00c6\3")
        buf.write("\2\2\2\u00c6\u00c4\3\2\2\2\u00c6\u00c7\3\2\2\2\u00c7\34")
        buf.write("\3\2\2\2\u00c8\u00c9\7D\2\2\u00c9\u00ca\7t\2\2\u00ca\u00cb")
        buf.write("\7g\2\2\u00cb\u00cc\7c\2\2\u00cc\u00cd\7m\2\2\u00cd\36")
        buf.write("\3\2\2\2\u00ce\u00cf\7E\2\2\u00cf\u00d0\7q\2\2\u00d0\u00d1")
        buf.write("\7p\2\2\u00d1\u00d2\7v\2\2\u00d2\u00d3\7k\2\2\u00d3\u00d4")
        buf.write("\7p\2\2\u00d4\u00d5\7w\2\2\u00d5\u00d6\7g\2\2\u00d6 \3")
        buf.write("\2\2\2\u00d7\u00d8\7K\2\2\u00d8\u00d9\7h\2\2\u00d9\"\3")
        buf.write("\2\2\2\u00da\u00db\7G\2\2\u00db\u00dc\7n\2\2\u00dc\u00dd")
        buf.write("\7u\2\2\u00dd\u00de\7g\2\2\u00de\u00df\7k\2\2\u00df\u00e0")
        buf.write("\7h\2\2\u00e0$\3\2\2\2\u00e1\u00e2\7G\2\2\u00e2\u00e3")
        buf.write("\7n\2\2\u00e3\u00e4\7u\2\2\u00e4\u00e5\7g\2\2\u00e5&\3")
        buf.write("\2\2\2\u00e6\u00e7\7H\2\2\u00e7\u00e8\7q\2\2\u00e8\u00e9")
        buf.write("\7t\2\2\u00e9\u00ea\7g\2\2\u00ea\u00eb\7c\2\2\u00eb\u00ec")
        buf.write("\7e\2\2\u00ec\u00ed\7j\2\2\u00ed(\3\2\2\2\u00ee\u00ef")
        buf.write("\7V\2\2\u00ef\u00f0\7t\2\2\u00f0\u00f1\7w\2\2\u00f1\u00f2")
        buf.write("\7g\2\2\u00f2*\3\2\2\2\u00f3\u00f4\7H\2\2\u00f4\u00f5")
        buf.write("\7c\2\2\u00f5\u00f6\7n\2\2\u00f6\u00f7\7u\2\2\u00f7\u00f8")
        buf.write("\7g\2\2\u00f8,\3\2\2\2\u00f9\u00fa\7C\2\2\u00fa\u00fb")
        buf.write("\7t\2\2\u00fb\u00fc\7t\2\2\u00fc\u00fd\7c\2\2\u00fd\u00fe")
        buf.write("\7{\2\2\u00fe.\3\2\2\2\u00ff\u0100\7K\2\2\u0100\u0101")
        buf.write("\7p\2\2\u0101\60\3\2\2\2\u0102\u0103\7D\2\2\u0103\u0104")
        buf.write("\7q\2\2\u0104\u0105\7q\2\2\u0105\u0106\7n\2\2\u0106\u0107")
        buf.write("\7g\2\2\u0107\u0108\7c\2\2\u0108\u0109\7p\2\2\u0109\62")
        buf.write("\3\2\2\2\u010a\u010b\7T\2\2\u010b\u010c\7g\2\2\u010c\u010d")
        buf.write("\7v\2\2\u010d\u010e\7w\2\2\u010e\u010f\7t\2\2\u010f\u0110")
        buf.write("\7p\2\2\u0110\64\3\2\2\2\u0111\u0112\7P\2\2\u0112\u0113")
        buf.write("\7w\2\2\u0113\u0114\7n\2\2\u0114\u0115\7n\2\2\u0115\66")
        buf.write("\3\2\2\2\u0116\u0117\7E\2\2\u0117\u0118\7q\2\2\u0118\u0119")
        buf.write("\7p\2\2\u0119\u011a\7u\2\2\u011a\u011b\7v\2\2\u011b\u011c")
        buf.write("\7t\2\2\u011c\u011d\7w\2\2\u011d\u011e\7e\2\2\u011e\u011f")
        buf.write("\7v\2\2\u011f\u0120\7q\2\2\u0120\u0121\7t\2\2\u01218\3")
        buf.write("\2\2\2\u0122\u0123\7F\2\2\u0123\u0124\7g\2\2\u0124\u0125")
        buf.write("\7u\2\2\u0125\u0126\7v\2\2\u0126\u0127\7t\2\2\u0127\u0128")
        buf.write("\7w\2\2\u0128\u0129\7e\2\2\u0129\u012a\7v\2\2\u012a\u012b")
        buf.write("\7q\2\2\u012b\u012c\7t\2\2\u012c:\3\2\2\2\u012d\u012e")
        buf.write("\7P\2\2\u012e\u012f\7g\2\2\u012f\u0130\7y\2\2\u0130<\3")
        buf.write("\2\2\2\u0131\u0132\7D\2\2\u0132\u0133\7{\2\2\u0133>\3")
        buf.write("\2\2\2\u0134\u0135\7U\2\2\u0135\u0136\7g\2\2\u0136\u0137")
        buf.write("\7n\2\2\u0137\u0138\7h\2\2\u0138@\3\2\2\2\u0139\u013a")
        buf.write("\7-\2\2\u013aB\3\2\2\2\u013b\u013c\7/\2\2\u013cD\3\2\2")
        buf.write("\2\u013d\u013e\7,\2\2\u013eF\3\2\2\2\u013f\u0140\7\61")
        buf.write("\2\2\u0140H\3\2\2\2\u0141\u0142\7\'\2\2\u0142J\3\2\2\2")
        buf.write("\u0143\u0144\7#\2\2\u0144L\3\2\2\2\u0145\u0146\7(\2\2")
        buf.write("\u0146\u0147\7(\2\2\u0147N\3\2\2\2\u0148\u0149\7~\2\2")
        buf.write("\u0149\u014a\7~\2\2\u014aP\3\2\2\2\u014b\u014c\7?\2\2")
        buf.write("\u014c\u014d\7?\2\2\u014dR\3\2\2\2\u014e\u014f\7?\2\2")
        buf.write("\u014fT\3\2\2\2\u0150\u0151\7#\2\2\u0151\u0152\7?\2\2")
        buf.write("\u0152V\3\2\2\2\u0153\u0154\7@\2\2\u0154X\3\2\2\2\u0155")
        buf.write("\u0156\7@\2\2\u0156\u0157\7?\2\2\u0157Z\3\2\2\2\u0158")
        buf.write("\u0159\7>\2\2\u0159\\\3\2\2\2\u015a\u015b\7>\2\2\u015b")
        buf.write("\u015c\7?\2\2\u015c^\3\2\2\2\u015d\u015e\7?\2\2\u015e")
        buf.write("\u015f\7?\2\2\u015f\u0160\7\60\2\2\u0160`\3\2\2\2\u0161")
        buf.write("\u0162\7-\2\2\u0162\u0163\7\60\2\2\u0163b\3\2\2\2\u0164")
        buf.write("\u0165\7\60\2\2\u0165d\3\2\2\2\u0166\u0167\7\60\2\2\u0167")
        buf.write("\u0168\7\60\2\2\u0168f\3\2\2\2\u0169\u016a\7<\2\2\u016a")
        buf.write("\u016b\7<\2\2\u016bh\3\2\2\2\u016c\u016d\7R\2\2\u016d")
        buf.write("\u016e\7t\2\2\u016e\u016f\7q\2\2\u016f\u0170\7i\2\2\u0170")
        buf.write("\u0171\7t\2\2\u0171\u0172\7c\2\2\u0172\u0173\7o\2\2\u0173")
        buf.write("j\3\2\2\2\u0174\u0175\7o\2\2\u0175\u0176\7c\2\2\u0176")
        buf.write("\u0177\7k\2\2\u0177\u0178\7p\2\2\u0178l\3\2\2\2\u0179")
        buf.write("\u017a\7E\2\2\u017a\u017b\7n\2\2\u017b\u017c\7c\2\2\u017c")
        buf.write("\u017d\7u\2\2\u017d\u017e\7u\2\2\u017en\3\2\2\2\u017f")
        buf.write("\u0180\7H\2\2\u0180\u0181\7n\2\2\u0181\u0182\7q\2\2\u0182")
        buf.write("\u0183\7c\2\2\u0183\u0184\7v\2\2\u0184p\3\2\2\2\u0185")
        buf.write("\u0186\7U\2\2\u0186\u0187\7v\2\2\u0187\u0188\7t\2\2\u0188")
        buf.write("\u0189\7k\2\2\u0189\u018a\7p\2\2\u018a\u018b\7i\2\2\u018b")
        buf.write("r\3\2\2\2\u018c\u018d\7K\2\2\u018d\u018e\7p\2\2\u018e")
        buf.write("\u018f\7v\2\2\u018ft\3\2\2\2\u0190\u0193\5)\25\2\u0191")
        buf.write("\u0193\5+\26\2\u0192\u0190\3\2\2\2\u0192\u0191\3\2\2\2")
        buf.write("\u0193v\3\2\2\2\u0194\u0199\5{>\2\u0195\u0199\5}?\2\u0196")
        buf.write("\u0199\5\177@\2\u0197\u0199\5y=\2\u0198\u0194\3\2\2\2")
        buf.write("\u0198\u0195\3\2\2\2\u0198\u0196\3\2\2\2\u0198\u0197\3")
        buf.write("\2\2\2\u0199x\3\2\2\2\u019a\u019b\7\62\2\2\u019b\u019f")
        buf.write("\7z\2\2\u019c\u019d\7\62\2\2\u019d\u019f\7Z\2\2\u019e")
        buf.write("\u019a\3\2\2\2\u019e\u019c\3\2\2\2\u019f\u01a0\3\2\2\2")
        buf.write("\u01a0\u01b6\t\5\2\2\u01a1\u01a2\7\62\2\2\u01a2\u01a6")
        buf.write("\7z\2\2\u01a3\u01a4\7\62\2\2\u01a4\u01a6\7Z\2\2\u01a5")
        buf.write("\u01a1\3\2\2\2\u01a5\u01a3\3\2\2\2\u01a6\u01a7\3\2\2\2")
        buf.write("\u01a7\u01b2\t\5\2\2\u01a8\u01aa\7a\2\2\u01a9\u01a8\3")
        buf.write("\2\2\2\u01a9\u01aa\3\2\2\2\u01aa\u01ac\3\2\2\2\u01ab\u01ad")
        buf.write("\t\6\2\2\u01ac\u01ab\3\2\2\2\u01ad\u01ae\3\2\2\2\u01ae")
        buf.write("\u01ac\3\2\2\2\u01ae\u01af\3\2\2\2\u01af\u01b1\3\2\2\2")
        buf.write("\u01b0\u01a9\3\2\2\2\u01b1\u01b4\3\2\2\2\u01b2\u01b0\3")
        buf.write("\2\2\2\u01b2\u01b3\3\2\2\2\u01b3\u01b6\3\2\2\2\u01b4\u01b2")
        buf.write("\3\2\2\2\u01b5\u019e\3\2\2\2\u01b5\u01a5\3\2\2\2\u01b6")
        buf.write("z\3\2\2\2\u01b7\u01b8\7\62\2\2\u01b8\u01c9\t\7\2\2\u01b9")
        buf.write("\u01ba\7\62\2\2\u01ba\u01c5\t\7\2\2\u01bb\u01bd\7a\2\2")
        buf.write("\u01bc\u01bb\3\2\2\2\u01bc\u01bd\3\2\2\2\u01bd\u01bf\3")
        buf.write("\2\2\2\u01be\u01c0\t\b\2\2\u01bf\u01be\3\2\2\2\u01c0\u01c1")
        buf.write("\3\2\2\2\u01c1\u01bf\3\2\2\2\u01c1\u01c2\3\2\2\2\u01c2")
        buf.write("\u01c4\3\2\2\2\u01c3\u01bc\3\2\2\2\u01c4\u01c7\3\2\2\2")
        buf.write("\u01c5\u01c3\3\2\2\2\u01c5\u01c6\3\2\2\2\u01c6\u01c9\3")
        buf.write("\2\2\2\u01c7\u01c5\3\2\2\2\u01c8\u01b7\3\2\2\2\u01c8\u01b9")
        buf.write("\3\2\2\2\u01c9|\3\2\2\2\u01ca\u01cb\7\62\2\2\u01cb\u01cc")
        buf.write("\7d\2\2\u01cc\u01d1\7\63\2\2\u01cd\u01ce\7\62\2\2\u01ce")
        buf.write("\u01cf\7D\2\2\u01cf\u01d1\7\63\2\2\u01d0\u01ca\3\2\2\2")
        buf.write("\u01d0\u01cd\3\2\2\2\u01d1\u01e7\3\2\2\2\u01d2\u01d3\7")
        buf.write("\62\2\2\u01d3\u01d7\7d\2\2\u01d4\u01d5\7\62\2\2\u01d5")
        buf.write("\u01d7\7D\2\2\u01d6\u01d2\3\2\2\2\u01d6\u01d4\3\2\2\2")
        buf.write("\u01d7\u01d8\3\2\2\2\u01d8\u01e3\t\t\2\2\u01d9\u01db\7")
        buf.write("a\2\2\u01da\u01d9\3\2\2\2\u01da\u01db\3\2\2\2\u01db\u01dd")
        buf.write("\3\2\2\2\u01dc\u01de\t\n\2\2\u01dd\u01dc\3\2\2\2\u01de")
        buf.write("\u01df\3\2\2\2\u01df\u01dd\3\2\2\2\u01df\u01e0\3\2\2\2")
        buf.write("\u01e0\u01e2\3\2\2\2\u01e1\u01da\3\2\2\2\u01e2\u01e5\3")
        buf.write("\2\2\2\u01e3\u01e1\3\2\2\2\u01e3\u01e4\3\2\2\2\u01e4\u01e7")
        buf.write("\3\2\2\2\u01e5\u01e3\3\2\2\2\u01e6\u01d0\3\2\2\2\u01e6")
        buf.write("\u01d6\3\2\2\2\u01e7~\3\2\2\2\u01e8\u01f8\t\13\2\2\u01e9")
        buf.write("\u01f4\t\13\2\2\u01ea\u01ec\7a\2\2\u01eb\u01ea\3\2\2\2")
        buf.write("\u01eb\u01ec\3\2\2\2\u01ec\u01ee\3\2\2\2\u01ed\u01ef\t")
        buf.write("\4\2\2\u01ee\u01ed\3\2\2\2\u01ef\u01f0\3\2\2\2\u01f0\u01ee")
        buf.write("\3\2\2\2\u01f0\u01f1\3\2\2\2\u01f1\u01f3\3\2\2\2\u01f2")
        buf.write("\u01eb\3\2\2\2\u01f3\u01f6\3\2\2\2\u01f4\u01f2\3\2\2\2")
        buf.write("\u01f4\u01f5\3\2\2\2\u01f5\u01f8\3\2\2\2\u01f6\u01f4\3")
        buf.write("\2\2\2\u01f7\u01e8\3\2\2\2\u01f7\u01e9\3\2\2\2\u01f8\u0080")
        buf.write("\3\2\2\2\u01f9\u01fe\5\u0085C\2\u01fa\u01fe\5\u0087D\2")
        buf.write("\u01fb\u01fe\5\u0089E\2\u01fc\u01fe\5\u0083B\2\u01fd\u01f9")
        buf.write("\3\2\2\2\u01fd\u01fa\3\2\2\2\u01fd\u01fb\3\2\2\2\u01fd")
        buf.write("\u01fc\3\2\2\2\u01fe\u0082\3\2\2\2\u01ff\u0200\7\62\2")
        buf.write("\2\u0200\u0204\7z\2\2\u0201\u0202\7\62\2\2\u0202\u0204")
        buf.write("\7Z\2\2\u0203\u01ff\3\2\2\2\u0203\u0201\3\2\2\2\u0204")
        buf.write("\u0205\3\2\2\2\u0205\u021b\t\6\2\2\u0206\u0207\7\62\2")
        buf.write("\2\u0207\u020b\7z\2\2\u0208\u0209\7\62\2\2\u0209\u020b")
        buf.write("\7Z\2\2\u020a\u0206\3\2\2\2\u020a\u0208\3\2\2\2\u020b")
        buf.write("\u020c\3\2\2\2\u020c\u0217\t\5\2\2\u020d\u020f\7a\2\2")
        buf.write("\u020e\u020d\3\2\2\2\u020e\u020f\3\2\2\2\u020f\u0211\3")
        buf.write("\2\2\2\u0210\u0212\t\6\2\2\u0211\u0210\3\2\2\2\u0212\u0213")
        buf.write("\3\2\2\2\u0213\u0211\3\2\2\2\u0213\u0214\3\2\2\2\u0214")
        buf.write("\u0216\3\2\2\2\u0215\u020e\3\2\2\2\u0216\u0219\3\2\2\2")
        buf.write("\u0217\u0215\3\2\2\2\u0217\u0218\3\2\2\2\u0218\u021b\3")
        buf.write("\2\2\2\u0219\u0217\3\2\2\2\u021a\u0203\3\2\2\2\u021a\u020a")
        buf.write("\3\2\2\2\u021b\u0084\3\2\2\2\u021c\u021d\7\62\2\2\u021d")
        buf.write("\u022e\t\b\2\2\u021e\u021f\7\62\2\2\u021f\u022a\t\7\2")
        buf.write("\2\u0220\u0222\7a\2\2\u0221\u0220\3\2\2\2\u0221\u0222")
        buf.write("\3\2\2\2\u0222\u0224\3\2\2\2\u0223\u0225\t\b\2\2\u0224")
        buf.write("\u0223\3\2\2\2\u0225\u0226\3\2\2\2\u0226\u0224\3\2\2\2")
        buf.write("\u0226\u0227\3\2\2\2\u0227\u0229\3\2\2\2\u0228\u0221\3")
        buf.write("\2\2\2\u0229\u022c\3\2\2\2\u022a\u0228\3\2\2\2\u022a\u022b")
        buf.write("\3\2\2\2\u022b\u022e\3\2\2\2\u022c\u022a\3\2\2\2\u022d")
        buf.write("\u021c\3\2\2\2\u022d\u021e\3\2\2\2\u022e\u0086\3\2\2\2")
        buf.write("\u022f\u0230\7\62\2\2\u0230\u0234\7d\2\2\u0231\u0232\7")
        buf.write("\62\2\2\u0232\u0234\7D\2\2\u0233\u022f\3\2\2\2\u0233\u0231")
        buf.write("\3\2\2\2\u0234\u0235\3\2\2\2\u0235\u024b\t\n\2\2\u0236")
        buf.write("\u0237\7\62\2\2\u0237\u023b\7d\2\2\u0238\u0239\7\62\2")
        buf.write("\2\u0239\u023b\7D\2\2\u023a\u0236\3\2\2\2\u023a\u0238")
        buf.write("\3\2\2\2\u023b\u023c\3\2\2\2\u023c\u0247\t\t\2\2\u023d")
        buf.write("\u023f\7a\2\2\u023e\u023d\3\2\2\2\u023e\u023f\3\2\2\2")
        buf.write("\u023f\u0241\3\2\2\2\u0240\u0242\t\n\2\2\u0241\u0240\3")
        buf.write("\2\2\2\u0242\u0243\3\2\2\2\u0243\u0241\3\2\2\2\u0243\u0244")
        buf.write("\3\2\2\2\u0244\u0246\3\2\2\2\u0245\u023e\3\2\2\2\u0246")
        buf.write("\u0249\3\2\2\2\u0247\u0245\3\2\2\2\u0247\u0248\3\2\2\2")
        buf.write("\u0248\u024b\3\2\2\2\u0249\u0247\3\2\2\2\u024a\u0233\3")
        buf.write("\2\2\2\u024a\u023a\3\2\2\2\u024b\u0088\3\2\2\2\u024c\u025c")
        buf.write("\t\4\2\2\u024d\u0258\t\13\2\2\u024e\u0250\7a\2\2\u024f")
        buf.write("\u024e\3\2\2\2\u024f\u0250\3\2\2\2\u0250\u0252\3\2\2\2")
        buf.write("\u0251\u0253\t\4\2\2\u0252\u0251\3\2\2\2\u0253\u0254\3")
        buf.write("\2\2\2\u0254\u0252\3\2\2\2\u0254\u0255\3\2\2\2\u0255\u0257")
        buf.write("\3\2\2\2\u0256\u024f\3\2\2\2\u0257\u025a\3\2\2\2\u0258")
        buf.write("\u0256\3\2\2\2\u0258\u0259\3\2\2\2\u0259\u025c\3\2\2\2")
        buf.write("\u025a\u0258\3\2\2\2\u025b\u024c\3\2\2\2\u025b\u024d\3")
        buf.write("\2\2\2\u025c\u008a\3\2\2\2\u025d\u025e\7)\2\2\u025e\u0262")
        buf.write("\7$\2\2\u025f\u0262\n\f\2\2\u0260\u0262\5\u008dG\2\u0261")
        buf.write("\u025d\3\2\2\2\u0261\u025f\3\2\2\2\u0261\u0260\3\2\2\2")
        buf.write("\u0262\u008c\3\2\2\2\u0263\u0264\7^\2\2\u0264\u0265\t")
        buf.write("\r\2\2\u0265\u008e\3\2\2\2\u0266\u0267\7^\2\2\u0267\u026a")
        buf.write("\n\r\2\2\u0268\u026a\7^\2\2\u0269\u0266\3\2\2\2\u0269")
        buf.write("\u0268\3\2\2\2\u026a\u0090\3\2\2\2\u026b\u026f\7$\2\2")
        buf.write("\u026c\u026e\5\u008bF\2\u026d\u026c\3\2\2\2\u026e\u0271")
        buf.write("\3\2\2\2\u026f\u026d\3\2\2\2\u026f\u0270\3\2\2\2\u0270")
        buf.write("\u0272\3\2\2\2\u0271\u026f\3\2\2\2\u0272\u0273\7$\2\2")
        buf.write("\u0273\u0274\bI\2\2\u0274\u0092\3\2\2\2\u0275\u0279\7")
        buf.write("$\2\2\u0276\u0278\5\u008bF\2\u0277\u0276\3\2\2\2\u0278")
        buf.write("\u027b\3\2\2\2\u0279\u0277\3\2\2\2\u0279\u027a\3\2\2\2")
        buf.write("\u027a\u027c\3\2\2\2\u027b\u0279\3\2\2\2\u027c\u027d\5")
        buf.write("\u008fH\2\u027d\u027e\bJ\3\2\u027e\u0094\3\2\2\2\u027f")
        buf.write("\u0283\7$\2\2\u0280\u0282\5\u008bF\2\u0281\u0280\3\2\2")
        buf.write("\2\u0282\u0285\3\2\2\2\u0283\u0281\3\2\2\2\u0283\u0284")
        buf.write("\3\2\2\2\u0284\u0286\3\2\2\2\u0285\u0283\3\2\2\2\u0286")
        buf.write("\u0287\bK\4\2\u0287\u0096\3\2\2\2\u0288\u0289\5\u0089")
        buf.write("E\2\u0289\u028c\5c\62\2\u028a\u028d\5\33\16\2\u028b\u028d")
        buf.write("\5\31\r\2\u028c\u028a\3\2\2\2\u028c\u028b\3\2\2\2\u028c")
        buf.write("\u028d\3\2\2\2\u028d\u029c\3\2\2\2\u028e\u028f\5\u0089")
        buf.write("E\2\u028f\u0290\5\31\r\2\u0290\u029c\3\2\2\2\u0291\u0293")
        buf.write("\5\u0089E\2\u0292\u0291\3\2\2\2\u0292\u0293\3\2\2\2\u0293")
        buf.write("\u0294\3\2\2\2\u0294\u0295\5c\62\2\u0295\u0296\5\33\16")
        buf.write("\2\u0296\u0297\5\31\r\2\u0297\u029c\3\2\2\2\u0298\u0299")
        buf.write("\5c\62\2\u0299\u029a\5\31\r\2\u029a\u029c\3\2\2\2\u029b")
        buf.write("\u0288\3\2\2\2\u029b\u028e\3\2\2\2\u029b\u0292\3\2\2\2")
        buf.write("\u029b\u0298\3\2\2\2\u029c\u0098\3\2\2\2\u029d\u02a1\t")
        buf.write("\16\2\2\u029e\u02a0\t\17\2\2\u029f\u029e\3\2\2\2\u02a0")
        buf.write("\u02a3\3\2\2\2\u02a1\u029f\3\2\2\2\u02a1\u02a2\3\2\2\2")
        buf.write("\u02a2\u009a\3\2\2\2\u02a3\u02a1\3\2\2\2\u02a4\u02a6\7")
        buf.write("&\2\2\u02a5\u02a7\t\17\2\2\u02a6\u02a5\3\2\2\2\u02a7\u02a8")
        buf.write("\3\2\2\2\u02a8\u02a6\3\2\2\2\u02a8\u02a9\3\2\2\2\u02a9")
        buf.write("\u009c\3\2\2\2\u02aa\u02ab\7%\2\2\u02ab\u02ac\7%\2\2\u02ac")
        buf.write("\u02b0\3\2\2\2\u02ad\u02af\13\2\2\2\u02ae\u02ad\3\2\2")
        buf.write("\2\u02af\u02b2\3\2\2\2\u02b0\u02b1\3\2\2\2\u02b0\u02ae")
        buf.write("\3\2\2\2\u02b1\u02b3\3\2\2\2\u02b2\u02b0\3\2\2\2\u02b3")
        buf.write("\u02b4\7%\2\2\u02b4\u02b5\7%\2\2\u02b5\u02b6\3\2\2\2\u02b6")
        buf.write("\u02b7\bO\5\2\u02b7\u009e\3\2\2\2\u02b8\u02ba\t\20\2\2")
        buf.write("\u02b9\u02b8\3\2\2\2\u02ba\u02bb\3\2\2\2\u02bb\u02b9\3")
        buf.write("\2\2\2\u02bb\u02bc\3\2\2\2\u02bc\u02bd\3\2\2\2\u02bd\u02be")
        buf.write("\bP\5\2\u02be\u00a0\3\2\2\2\u02bf\u02c0\13\2\2\2\u02c0")
        buf.write("\u02c1\bQ\6\2\u02c1\u00a2\3\2\2\2<\2\u00bf\u00c6\u0192")
        buf.write("\u0198\u019e\u01a5\u01a9\u01ae\u01b2\u01b5\u01bc\u01c1")
        buf.write("\u01c5\u01c8\u01d0\u01d6\u01da\u01df\u01e3\u01e6\u01eb")
        buf.write("\u01f0\u01f4\u01f7\u01fd\u0203\u020a\u020e\u0213\u0217")
        buf.write("\u021a\u0221\u0226\u022a\u022d\u0233\u023a\u023e\u0243")
        buf.write("\u0247\u024a\u024f\u0254\u0258\u025b\u0261\u0269\u026f")
        buf.write("\u0279\u0283\u028c\u0292\u029b\u02a1\u02a8\u02b0\u02bb")
        buf.write("\7\3I\2\3J\3\3K\4\b\2\2\3Q\5")
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
    ARRAY_SIZE = 57
    INTEGER_LITERAL = 58
    STRING_LITERAL = 59
    ILLEGAL_ESCAPE = 60
    UNCLOSE_STRING = 61
    REAL_LITERAL = 62
    NORMAL_ID = 63
    DOLLAR_ID = 64
    BLOCK_COMMENT = 65
    WS = 66
    ERROR_CHAR = 67

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
            "STRING", "INT_TYPE", "BOOL_LITERAL", "ARRAY_SIZE", "INTEGER_LITERAL", 
            "STRING_LITERAL", "ILLEGAL_ESCAPE", "UNCLOSE_STRING", "REAL_LITERAL", 
            "NORMAL_ID", "DOLLAR_ID", "BLOCK_COMMENT", "WS", "ERROR_CHAR" ]

    ruleNames = [ "VAL", "VAR", "LP", "RP", "LCB", "RCB", "LSB", "RSB", 
                  "SEMI", "COMMA", "COLON", "EXPONENT", "DEC_DIGIT", "BREAK", 
                  "CONTINUE", "IF", "ELSEIF", "ELSE", "FOREACH", "TRUE", 
                  "FALSE", "ARRAY", "IN", "BOOLEAN", "RETURN", "NULL", "CONSTRUCTOR", 
                  "DESTRUCTOR", "NEW", "BY", "SELF", "ADD", "SUB", "MUL", 
                  "DIV", "MOD", "NOT", "AND", "OR", "EQUAL", "ASSIGN", "NOTEQUAL", 
                  "GT", "GTE", "LT", "LTE", "EQUAL_STR", "ADD_STR", "DOT", 
                  "DOTDOT", "SCOPE", "PROGRAM", "MAIN", "CLASS", "FLOAT_TYPE", 
                  "STRING", "INT_TYPE", "BOOL_LITERAL", "ARRAY_SIZE", "ARRAY_SIZE_HEX", 
                  "ARRAY_SIZE_OCT", "ARRAY_SIZE_BIN", "ARRAY_SIZE_DEC", 
                  "INTEGER_LITERAL", "HEX_TYPE", "OCT_TYPE", "BIN_TYPE", 
                  "DEC_TYPE", "STR", "ESC_SEQ", "ESC_ILLEGAL", "STRING_LITERAL", 
                  "ILLEGAL_ESCAPE", "UNCLOSE_STRING", "REAL_LITERAL", "NORMAL_ID", 
                  "DOLLAR_ID", "BLOCK_COMMENT", "WS", "ERROR_CHAR" ]

    grammarFileName = "D96.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.9.2")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


    def emit(self):
        tk = self.type
        result = super().emit()
        # delete later
        print('----------------------------------------------------------------------------')
        attributes = inspect.getmembers(D96Lexer, lambda a:not(inspect.isroutine(a)))
        user_defined_attr = [a for a in attributes if not(a[0].startswith('__') and a[0].endswith('__'))]
        for i in user_defined_attr:
            if tk == i[1]:
                print ("{:<30} {:<30} {:<50}".format(result.text, '|', i[0]))
        print('----------------------------------------------------------------------------')
        if tk == self.INTEGER_LITERAL or tk == self.REAL_LITERAL or tk == self.ARRAY_SIZE:
            result.text = result.text.replace('_', '')
        return result


    def action(self, localctx:RuleContext, ruleIndex:int, actionIndex:int):
        if self._actions is None:
            actions = dict()
            actions[71] = self.STRING_LITERAL_action 
            actions[72] = self.ILLEGAL_ESCAPE_action 
            actions[73] = self.UNCLOSE_STRING_action 
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
                newLineIdx = y.find('\n')
                if newLineIdx >= 0:
                    raise UncloseString(y[1:newLineIdx-1])
                if y[-2:] == '\'"':
                    raise UncloseString(y[1:])
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
     


