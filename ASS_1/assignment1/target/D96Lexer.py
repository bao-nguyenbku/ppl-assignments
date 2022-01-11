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
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2P")
        buf.write("\u026b\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7")
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
        buf.write("U\4V\tV\3\2\3\2\3\2\3\2\3\2\3\3\3\3\3\3\3\3\3\3\5\3\u00b8")
        buf.write("\n\3\3\3\3\3\7\3\u00bc\n\3\f\3\16\3\u00bf\13\3\3\3\3\3")
        buf.write("\3\4\3\4\3\5\3\5\3\5\5\5\u00c8\n\5\3\5\3\5\3\5\3\6\3\6")
        buf.write("\3\6\3\7\3\7\3\7\3\7\7\7\u00d4\n\7\f\7\16\7\u00d7\13\7")
        buf.write("\3\b\3\b\3\b\3\b\3\b\3\b\3\b\3\b\3\b\3\b\5\b\u00e3\n\b")
        buf.write("\3\t\3\t\3\t\3\t\3\n\3\n\3\n\3\n\3\n\3\n\3\13\3\13\3\13")
        buf.write("\3\13\3\13\3\13\3\13\3\f\3\f\5\f\u00f8\n\f\3\r\3\r\3\r")
        buf.write("\3\r\3\r\3\16\3\16\3\16\3\16\3\16\3\16\3\17\3\17\3\17")
        buf.write("\3\17\3\17\5\17\u010a\n\17\3\20\3\20\3\20\3\20\5\20\u0110")
        buf.write("\n\20\3\21\3\21\3\21\3\21\5\21\u0116\n\21\3\21\6\21\u0119")
        buf.write("\n\21\r\21\16\21\u011a\3\22\3\22\6\22\u011f\n\22\r\22")
        buf.write("\16\22\u0120\3\23\3\23\3\23\3\23\5\23\u0127\n\23\3\23")
        buf.write("\6\23\u012a\n\23\r\23\16\23\u012b\3\24\3\24\3\24\7\24")
        buf.write("\u0131\n\24\f\24\16\24\u0134\13\24\5\24\u0136\n\24\3\25")
        buf.write("\3\25\7\25\u013a\n\25\f\25\16\25\u013d\13\25\3\25\3\25")
        buf.write("\3\25\3\26\3\26\7\26\u0144\n\26\f\26\16\26\u0147\13\26")
        buf.write("\3\26\3\26\3\26\3\27\3\27\7\27\u014e\n\27\f\27\16\27\u0151")
        buf.write("\13\27\3\27\3\27\3\27\3\30\3\30\3\30\3\30\3\30\5\30\u015b")
        buf.write("\n\30\3\31\3\31\3\31\3\32\3\32\3\32\3\33\3\33\5\33\u0165")
        buf.write("\n\33\3\33\3\33\7\33\u0169\n\33\f\33\16\33\u016c\13\33")
        buf.write("\3\34\3\34\3\34\3\34\5\34\u0172\n\34\3\35\3\35\3\35\3")
        buf.write("\35\3\35\3\35\3\36\3\36\3\36\3\36\3\37\3\37\3\37\3\37")
        buf.write("\3 \3 \3!\3!\3\"\3\"\3#\3#\3$\3$\3%\3%\3&\3&\3\'\3\'\3")
        buf.write("(\3(\3)\3)\3*\3*\3*\3+\3+\3+\3,\3,\3-\3-\5-\u01a0\n-\3")
        buf.write("-\3-\3.\3.\3/\3/\3/\7/\u01a9\n/\f/\16/\u01ac\13/\5/\u01ae")
        buf.write("\n/\3\60\3\60\3\61\3\61\3\61\3\61\3\61\3\61\3\62\3\62")
        buf.write("\3\62\3\62\3\62\3\62\3\62\3\62\3\63\3\63\3\63\3\63\3\63")
        buf.write("\3\63\3\63\3\63\3\64\3\64\3\64\3\64\3\64\3\65\3\65\3\65")
        buf.write("\3\65\3\65\3\65\3\65\3\65\3\65\3\66\3\66\3\66\3\66\3\66")
        buf.write("\3\67\3\67\3\67\3\67\3\67\3\67\38\38\38\39\39\39\39\3")
        buf.write("9\39\39\3:\3:\3:\3:\3:\3;\3;\3;\3;\3;\3<\3<\3<\3=\3=\3")
        buf.write("=\3>\3>\3>\3>\3>\3>\3>\3?\3?\3?\3?\3@\3@\3A\3A\3B\3B\3")
        buf.write("C\3C\3D\3D\3E\3E\3F\3F\3F\3G\3G\3G\3H\3H\3H\3I\3I\3J\3")
        buf.write("J\3J\3K\3K\3L\3L\3L\3M\3M\3M\3N\3N\3O\3O\3O\3O\3P\3P\3")
        buf.write("P\3Q\3Q\7Q\u0233\nQ\fQ\16Q\u0236\13Q\3Q\3Q\6Q\u023a\n")
        buf.write("Q\rQ\16Q\u023b\5Q\u023e\nQ\3R\3R\3R\3R\7R\u0244\nR\fR")
        buf.write("\16R\u0247\13R\3S\6S\u024a\nS\rS\16S\u024b\3S\3S\3T\3")
        buf.write("T\3T\3T\7T\u0254\nT\fT\16T\u0257\13T\3T\3T\3T\3T\3T\3")
        buf.write("U\3U\3U\3U\7U\u0262\nU\fU\16U\u0265\13U\3U\3U\3V\3V\3")
        buf.write("V\4\u0255\u0263\2W\3\3\5\4\7\5\t\6\13\7\r\b\17\t\21\n")
        buf.write("\23\13\25\f\27\r\31\16\33\17\35\20\37\21!\22#\23%\24\'")
        buf.write("\25)\26+\27-\30/\2\61\2\63\2\65\31\67\329\33;\34=\35?")
        buf.write("\36A\37C E!G\"I#K$M%O&Q\'S(U)W*Y\2[\2]\2_\2a+c,e-g.i/")
        buf.write("k\60m\61o\62q\63s\64u\65w\66y\67{8}9\177:\u0081;\u0083")
        buf.write("<\u0085=\u0087>\u0089?\u008b@\u008dA\u008fB\u0091C\u0093")
        buf.write("D\u0095E\u0097F\u0099G\u009bH\u009dI\u009fJ\u00a1K\u00a3")
        buf.write("L\u00a5M\u00a7N\u00a9O\u00abP\3\2\17\5\2\62;CHch\3\2\62")
        buf.write(";\3\2\62\63\3\2\63;\4\2\62;aa\t\2$$^^ddhhppttvv\4\2$$")
        buf.write("^^\n\2$$))^^ddhhppttvv\4\2GGgg\4\2--//\5\2C\\aac|\6\2")
        buf.write("\62;C\\aac|\5\2\13\f\17\17\"\"\2\u028c\2\3\3\2\2\2\2\5")
        buf.write("\3\2\2\2\2\7\3\2\2\2\2\t\3\2\2\2\2\13\3\2\2\2\2\r\3\2")
        buf.write("\2\2\2\17\3\2\2\2\2\21\3\2\2\2\2\23\3\2\2\2\2\25\3\2\2")
        buf.write("\2\2\27\3\2\2\2\2\31\3\2\2\2\2\33\3\2\2\2\2\35\3\2\2\2")
        buf.write("\2\37\3\2\2\2\2!\3\2\2\2\2#\3\2\2\2\2%\3\2\2\2\2\'\3\2")
        buf.write("\2\2\2)\3\2\2\2\2+\3\2\2\2\2-\3\2\2\2\2\65\3\2\2\2\2\67")
        buf.write("\3\2\2\2\29\3\2\2\2\2;\3\2\2\2\2=\3\2\2\2\2?\3\2\2\2\2")
        buf.write("A\3\2\2\2\2C\3\2\2\2\2E\3\2\2\2\2G\3\2\2\2\2I\3\2\2\2")
        buf.write("\2K\3\2\2\2\2M\3\2\2\2\2O\3\2\2\2\2Q\3\2\2\2\2S\3\2\2")
        buf.write("\2\2U\3\2\2\2\2W\3\2\2\2\2a\3\2\2\2\2c\3\2\2\2\2e\3\2")
        buf.write("\2\2\2g\3\2\2\2\2i\3\2\2\2\2k\3\2\2\2\2m\3\2\2\2\2o\3")
        buf.write("\2\2\2\2q\3\2\2\2\2s\3\2\2\2\2u\3\2\2\2\2w\3\2\2\2\2y")
        buf.write("\3\2\2\2\2{\3\2\2\2\2}\3\2\2\2\2\177\3\2\2\2\2\u0081\3")
        buf.write("\2\2\2\2\u0083\3\2\2\2\2\u0085\3\2\2\2\2\u0087\3\2\2\2")
        buf.write("\2\u0089\3\2\2\2\2\u008b\3\2\2\2\2\u008d\3\2\2\2\2\u008f")
        buf.write("\3\2\2\2\2\u0091\3\2\2\2\2\u0093\3\2\2\2\2\u0095\3\2\2")
        buf.write("\2\2\u0097\3\2\2\2\2\u0099\3\2\2\2\2\u009b\3\2\2\2\2\u009d")
        buf.write("\3\2\2\2\2\u009f\3\2\2\2\2\u00a1\3\2\2\2\2\u00a3\3\2\2")
        buf.write("\2\2\u00a5\3\2\2\2\2\u00a7\3\2\2\2\2\u00a9\3\2\2\2\2\u00ab")
        buf.write("\3\2\2\2\3\u00ad\3\2\2\2\5\u00b2\3\2\2\2\7\u00c2\3\2\2")
        buf.write("\2\t\u00c4\3\2\2\2\13\u00cc\3\2\2\2\r\u00cf\3\2\2\2\17")
        buf.write("\u00e2\3\2\2\2\21\u00e4\3\2\2\2\23\u00e8\3\2\2\2\25\u00ee")
        buf.write("\3\2\2\2\27\u00f7\3\2\2\2\31\u00f9\3\2\2\2\33\u00fe\3")
        buf.write("\2\2\2\35\u0109\3\2\2\2\37\u010f\3\2\2\2!\u0115\3\2\2")
        buf.write("\2#\u011c\3\2\2\2%\u0126\3\2\2\2\'\u0135\3\2\2\2)\u0137")
        buf.write("\3\2\2\2+\u0141\3\2\2\2-\u014b\3\2\2\2/\u015a\3\2\2\2")
        buf.write("\61\u015c\3\2\2\2\63\u015f\3\2\2\2\65\u0162\3\2\2\2\67")
        buf.write("\u0171\3\2\2\29\u0173\3\2\2\2;\u0179\3\2\2\2=\u017d\3")
        buf.write("\2\2\2?\u0181\3\2\2\2A\u0183\3\2\2\2C\u0185\3\2\2\2E\u0187")
        buf.write("\3\2\2\2G\u0189\3\2\2\2I\u018b\3\2\2\2K\u018d\3\2\2\2")
        buf.write("M\u018f\3\2\2\2O\u0191\3\2\2\2Q\u0193\3\2\2\2S\u0195\3")
        buf.write("\2\2\2U\u0198\3\2\2\2W\u019b\3\2\2\2Y\u019d\3\2\2\2[\u01a3")
        buf.write("\3\2\2\2]\u01ad\3\2\2\2_\u01af\3\2\2\2a\u01b1\3\2\2\2")
        buf.write("c\u01b7\3\2\2\2e\u01bf\3\2\2\2g\u01c7\3\2\2\2i\u01cc\3")
        buf.write("\2\2\2k\u01d5\3\2\2\2m\u01da\3\2\2\2o\u01e0\3\2\2\2q\u01e3")
        buf.write("\3\2\2\2s\u01ea\3\2\2\2u\u01ef\3\2\2\2w\u01f4\3\2\2\2")
        buf.write("y\u01f7\3\2\2\2{\u01fa\3\2\2\2}\u0201\3\2\2\2\177\u0205")
        buf.write("\3\2\2\2\u0081\u0207\3\2\2\2\u0083\u0209\3\2\2\2\u0085")
        buf.write("\u020b\3\2\2\2\u0087\u020d\3\2\2\2\u0089\u020f\3\2\2\2")
        buf.write("\u008b\u0211\3\2\2\2\u008d\u0214\3\2\2\2\u008f\u0217\3")
        buf.write("\2\2\2\u0091\u021a\3\2\2\2\u0093\u021c\3\2\2\2\u0095\u021f")
        buf.write("\3\2\2\2\u0097\u0221\3\2\2\2\u0099\u0224\3\2\2\2\u009b")
        buf.write("\u0227\3\2\2\2\u009d\u0229\3\2\2\2\u009f\u022d\3\2\2\2")
        buf.write("\u00a1\u023d\3\2\2\2\u00a3\u023f\3\2\2\2\u00a5\u0249\3")
        buf.write("\2\2\2\u00a7\u024f\3\2\2\2\u00a9\u025d\3\2\2\2\u00ab\u0268")
        buf.write("\3\2\2\2\u00ad\u00ae\7o\2\2\u00ae\u00af\7c\2\2\u00af\u00b0")
        buf.write("\7k\2\2\u00b0\u00b1\7p\2\2\u00b1\4\3\2\2\2\u00b2\u00b3")
        buf.write("\5\33\16\2\u00b3\u00b7\5\u00a1Q\2\u00b4\u00b5\5Q)\2\u00b5")
        buf.write("\u00b6\5\u00a1Q\2\u00b6\u00b8\3\2\2\2\u00b7\u00b4\3\2")
        buf.write("\2\2\u00b7\u00b8\3\2\2\2\u00b8\u00b9\3\2\2\2\u00b9\u00bd")
        buf.write("\5E#\2\u00ba\u00bc\5\7\4\2\u00bb\u00ba\3\2\2\2\u00bc\u00bf")
        buf.write("\3\2\2\2\u00bd\u00bb\3\2\2\2\u00bd\u00be\3\2\2\2\u00be")
        buf.write("\u00c0\3\2\2\2\u00bf\u00bd\3\2\2\2\u00c0\u00c1\5G$\2\u00c1")
        buf.write("\6\3\2\2\2\u00c2\u00c3\5\t\5\2\u00c3\b\3\2\2\2\u00c4\u00c5")
        buf.write("\5\u00a1Q\2\u00c5\u00c7\5A!\2\u00c6\u00c8\5\r\7\2\u00c7")
        buf.write("\u00c6\3\2\2\2\u00c7\u00c8\3\2\2\2\u00c8\u00c9\3\2\2\2")
        buf.write("\u00c9\u00ca\5C\"\2\u00ca\u00cb\5\13\6\2\u00cb\n\3\2\2")
        buf.write("\2\u00cc\u00cd\5E#\2\u00cd\u00ce\5G$\2\u00ce\f\3\2\2\2")
        buf.write("\u00cf\u00d5\5\17\b\2\u00d0\u00d1\5M\'\2\u00d1\u00d2\5")
        buf.write("\17\b\2\u00d2\u00d4\3\2\2\2\u00d3\u00d0\3\2\2\2\u00d4")
        buf.write("\u00d7\3\2\2\2\u00d5\u00d3\3\2\2\2\u00d5\u00d6\3\2\2\2")
        buf.write("\u00d6\16\3\2\2\2\u00d7\u00d5\3\2\2\2\u00d8\u00d9\5\u00a1")
        buf.write("Q\2\u00d9\u00da\5Q)\2\u00da\u00db\5\35\17\2\u00db\u00e3")
        buf.write("\3\2\2\2\u00dc\u00dd\5\u00a1Q\2\u00dd\u00de\5Q)\2\u00de")
        buf.write("\u00df\5\35\17\2\u00df\u00e0\5O(\2\u00e0\u00e1\5\17\b")
        buf.write("\2\u00e1\u00e3\3\2\2\2\u00e2\u00d8\3\2\2\2\u00e2\u00dc")
        buf.write("\3\2\2\2\u00e3\20\3\2\2\2\u00e4\u00e5\7K\2\2\u00e5\u00e6")
        buf.write("\7p\2\2\u00e6\u00e7\7v\2\2\u00e7\22\3\2\2\2\u00e8\u00e9")
        buf.write("\7H\2\2\u00e9\u00ea\7n\2\2\u00ea\u00eb\7q\2\2\u00eb\u00ec")
        buf.write("\7c\2\2\u00ec\u00ed\7v\2\2\u00ed\24\3\2\2\2\u00ee\u00ef")
        buf.write("\7U\2\2\u00ef\u00f0\7v\2\2\u00f0\u00f1\7t\2\2\u00f1\u00f2")
        buf.write("\7k\2\2\u00f2\u00f3\7p\2\2\u00f3\u00f4\7i\2\2\u00f4\26")
        buf.write("\3\2\2\2\u00f5\u00f8\5k\66\2\u00f6\u00f8\5m\67\2\u00f7")
        buf.write("\u00f5\3\2\2\2\u00f7\u00f6\3\2\2\2\u00f8\30\3\2\2\2\u00f9")
        buf.write("\u00fa\7X\2\2\u00fa\u00fb\7q\2\2\u00fb\u00fc\7k\2\2\u00fc")
        buf.write("\u00fd\7f\2\2\u00fd\32\3\2\2\2\u00fe\u00ff\7e\2\2\u00ff")
        buf.write("\u0100\7n\2\2\u0100\u0101\7c\2\2\u0101\u0102\7u\2\2\u0102")
        buf.write("\u0103\7u\2\2\u0103\34\3\2\2\2\u0104\u010a\5\27\f\2\u0105")
        buf.write("\u010a\5\21\t\2\u0106\u010a\5\23\n\2\u0107\u010a\5\25")
        buf.write("\13\2\u0108\u010a\5\33\16\2\u0109\u0104\3\2\2\2\u0109")
        buf.write("\u0105\3\2\2\2\u0109\u0106\3\2\2\2\u0109\u0107\3\2\2\2")
        buf.write("\u0109\u0108\3\2\2\2\u010a\36\3\2\2\2\u010b\u0110\5!\21")
        buf.write("\2\u010c\u0110\5#\22\2\u010d\u0110\5%\23\2\u010e\u0110")
        buf.write("\5\'\24\2\u010f\u010b\3\2\2\2\u010f\u010c\3\2\2\2\u010f")
        buf.write("\u010d\3\2\2\2\u010f\u010e\3\2\2\2\u0110 \3\2\2\2\u0111")
        buf.write("\u0112\7\62\2\2\u0112\u0116\7z\2\2\u0113\u0114\7\62\2")
        buf.write("\2\u0114\u0116\7Z\2\2\u0115\u0111\3\2\2\2\u0115\u0113")
        buf.write("\3\2\2\2\u0116\u0118\3\2\2\2\u0117\u0119\t\2\2\2\u0118")
        buf.write("\u0117\3\2\2\2\u0119\u011a\3\2\2\2\u011a\u0118\3\2\2\2")
        buf.write("\u011a\u011b\3\2\2\2\u011b\"\3\2\2\2\u011c\u011e\7\62")
        buf.write("\2\2\u011d\u011f\t\3\2\2\u011e\u011d\3\2\2\2\u011f\u0120")
        buf.write("\3\2\2\2\u0120\u011e\3\2\2\2\u0120\u0121\3\2\2\2\u0121")
        buf.write("$\3\2\2\2\u0122\u0123\7\62\2\2\u0123\u0127\7d\2\2\u0124")
        buf.write("\u0125\7\62\2\2\u0125\u0127\7D\2\2\u0126\u0122\3\2\2\2")
        buf.write("\u0126\u0124\3\2\2\2\u0127\u0129\3\2\2\2\u0128\u012a\t")
        buf.write("\4\2\2\u0129\u0128\3\2\2\2\u012a\u012b\3\2\2\2\u012b\u0129")
        buf.write("\3\2\2\2\u012b\u012c\3\2\2\2\u012c&\3\2\2\2\u012d\u0136")
        buf.write("\t\3\2\2\u012e\u0132\t\5\2\2\u012f\u0131\t\6\2\2\u0130")
        buf.write("\u012f\3\2\2\2\u0131\u0134\3\2\2\2\u0132\u0130\3\2\2\2")
        buf.write("\u0132\u0133\3\2\2\2\u0133\u0136\3\2\2\2\u0134\u0132\3")
        buf.write("\2\2\2\u0135\u012d\3\2\2\2\u0135\u012e\3\2\2\2\u0136(")
        buf.write("\3\2\2\2\u0137\u013b\7$\2\2\u0138\u013a\5/\30\2\u0139")
        buf.write("\u0138\3\2\2\2\u013a\u013d\3\2\2\2\u013b\u0139\3\2\2\2")
        buf.write("\u013b\u013c\3\2\2\2\u013c\u013e\3\2\2\2\u013d\u013b\3")
        buf.write("\2\2\2\u013e\u013f\7$\2\2\u013f\u0140\b\25\2\2\u0140*")
        buf.write("\3\2\2\2\u0141\u0145\7$\2\2\u0142\u0144\5/\30\2\u0143")
        buf.write("\u0142\3\2\2\2\u0144\u0147\3\2\2\2\u0145\u0143\3\2\2\2")
        buf.write("\u0145\u0146\3\2\2\2\u0146\u0148\3\2\2\2\u0147\u0145\3")
        buf.write("\2\2\2\u0148\u0149\5\63\32\2\u0149\u014a\b\26\3\2\u014a")
        buf.write(",\3\2\2\2\u014b\u014f\7$\2\2\u014c\u014e\5/\30\2\u014d")
        buf.write("\u014c\3\2\2\2\u014e\u0151\3\2\2\2\u014f\u014d\3\2\2\2")
        buf.write("\u014f\u0150\3\2\2\2\u0150\u0152\3\2\2\2\u0151\u014f\3")
        buf.write("\2\2\2\u0152\u0153\7\2\2\3\u0153\u0154\b\27\4\2\u0154")
        buf.write(".\3\2\2\2\u0155\u0156\7^\2\2\u0156\u015b\t\7\2\2\u0157")
        buf.write("\u015b\n\b\2\2\u0158\u0159\7)\2\2\u0159\u015b\7$\2\2\u015a")
        buf.write("\u0155\3\2\2\2\u015a\u0157\3\2\2\2\u015a\u0158\3\2\2\2")
        buf.write("\u015b\60\3\2\2\2\u015c\u015d\7^\2\2\u015d\u015e\t\t\2")
        buf.write("\2\u015e\62\3\2\2\2\u015f\u0160\7^\2\2\u0160\u0161\n\7")
        buf.write("\2\2\u0161\64\3\2\2\2\u0162\u0164\5]/\2\u0163\u0165\5")
        buf.write("W,\2\u0164\u0163\3\2\2\2\u0164\u0165\3\2\2\2\u0165\u016a")
        buf.write("\3\2\2\2\u0166\u0169\5]/\2\u0167\u0169\5Y-\2\u0168\u0166")
        buf.write("\3\2\2\2\u0168\u0167\3\2\2\2\u0169\u016c\3\2\2\2\u016a")
        buf.write("\u0168\3\2\2\2\u016a\u016b\3\2\2\2\u016b\66\3\2\2\2\u016c")
        buf.write("\u016a\3\2\2\2\u016d\u0172\5\37\20\2\u016e\u0172\5\27")
        buf.write("\f\2\u016f\u0172\5\65\33\2\u0170\u0172\5)\25\2\u0171\u016d")
        buf.write("\3\2\2\2\u0171\u016e\3\2\2\2\u0171\u016f\3\2\2\2\u0171")
        buf.write("\u0170\3\2\2\2\u01728\3\2\2\2\u0173\u0174\7C\2\2\u0174")
        buf.write("\u0175\7t\2\2\u0175\u0176\7t\2\2\u0176\u0177\7c\2\2\u0177")
        buf.write("\u0178\7{\2\2\u0178:\3\2\2\2\u0179\u017a\7x\2\2\u017a")
        buf.write("\u017b\7c\2\2\u017b\u017c\7n\2\2\u017c<\3\2\2\2\u017d")
        buf.write("\u017e\7x\2\2\u017e\u017f\7c\2\2\u017f\u0180\7t\2\2\u0180")
        buf.write(">\3\2\2\2\u0181\u0182\7&\2\2\u0182@\3\2\2\2\u0183\u0184")
        buf.write("\7*\2\2\u0184B\3\2\2\2\u0185\u0186\7+\2\2\u0186D\3\2\2")
        buf.write("\2\u0187\u0188\7}\2\2\u0188F\3\2\2\2\u0189\u018a\7\177")
        buf.write("\2\2\u018aH\3\2\2\2\u018b\u018c\7]\2\2\u018cJ\3\2\2\2")
        buf.write("\u018d\u018e\7_\2\2\u018eL\3\2\2\2\u018f\u0190\7=\2\2")
        buf.write("\u0190N\3\2\2\2\u0191\u0192\7.\2\2\u0192P\3\2\2\2\u0193")
        buf.write("\u0194\7<\2\2\u0194R\3\2\2\2\u0195\u0196\7<\2\2\u0196")
        buf.write("\u0197\7<\2\2\u0197T\3\2\2\2\u0198\u0199\7\60\2\2\u0199")
        buf.write("\u019a\7\60\2\2\u019aV\3\2\2\2\u019b\u019c\7\60\2\2\u019c")
        buf.write("X\3\2\2\2\u019d\u019f\t\n\2\2\u019e\u01a0\5_\60\2\u019f")
        buf.write("\u019e\3\2\2\2\u019f\u01a0\3\2\2\2\u01a0\u01a1\3\2\2\2")
        buf.write("\u01a1\u01a2\5\'\24\2\u01a2Z\3\2\2\2\u01a3\u01a4\t\3\2")
        buf.write("\2\u01a4\\\3\2\2\2\u01a5\u01ae\t\3\2\2\u01a6\u01aa\t\5")
        buf.write("\2\2\u01a7\u01a9\t\6\2\2\u01a8\u01a7\3\2\2\2\u01a9\u01ac")
        buf.write("\3\2\2\2\u01aa\u01a8\3\2\2\2\u01aa\u01ab\3\2\2\2\u01ab")
        buf.write("\u01ae\3\2\2\2\u01ac\u01aa\3\2\2\2\u01ad\u01a5\3\2\2\2")
        buf.write("\u01ad\u01a6\3\2\2\2\u01ae^\3\2\2\2\u01af\u01b0\t\13\2")
        buf.write("\2\u01b0`\3\2\2\2\u01b1\u01b2\7D\2\2\u01b2\u01b3\7t\2")
        buf.write("\2\u01b3\u01b4\7g\2\2\u01b4\u01b5\7c\2\2\u01b5\u01b6\7")
        buf.write("m\2\2\u01b6b\3\2\2\2\u01b7\u01b8\7H\2\2\u01b8\u01b9\7")
        buf.write("q\2\2\u01b9\u01ba\7t\2\2\u01ba\u01bb\7g\2\2\u01bb\u01bc")
        buf.write("\7c\2\2\u01bc\u01bd\7e\2\2\u01bd\u01be\7j\2\2\u01bed\3")
        buf.write("\2\2\2\u01bf\u01c0\7D\2\2\u01c0\u01c1\7q\2\2\u01c1\u01c2")
        buf.write("\7q\2\2\u01c2\u01c3\7n\2\2\u01c3\u01c4\7g\2\2\u01c4\u01c5")
        buf.write("\7c\2\2\u01c5\u01c6\7p\2\2\u01c6f\3\2\2\2\u01c7\u01c8")
        buf.write("\7P\2\2\u01c8\u01c9\7w\2\2\u01c9\u01ca\7n\2\2\u01ca\u01cb")
        buf.write("\7n\2\2\u01cbh\3\2\2\2\u01cc\u01cd\7E\2\2\u01cd\u01ce")
        buf.write("\7q\2\2\u01ce\u01cf\7p\2\2\u01cf\u01d0\7v\2\2\u01d0\u01d1")
        buf.write("\7k\2\2\u01d1\u01d2\7p\2\2\u01d2\u01d3\7w\2\2\u01d3\u01d4")
        buf.write("\7g\2\2\u01d4j\3\2\2\2\u01d5\u01d6\7V\2\2\u01d6\u01d7")
        buf.write("\7t\2\2\u01d7\u01d8\7w\2\2\u01d8\u01d9\7g\2\2\u01d9l\3")
        buf.write("\2\2\2\u01da\u01db\7H\2\2\u01db\u01dc\7c\2\2\u01dc\u01dd")
        buf.write("\7n\2\2\u01dd\u01de\7u\2\2\u01de\u01df\7g\2\2\u01dfn\3")
        buf.write("\2\2\2\u01e0\u01e1\7K\2\2\u01e1\u01e2\7h\2\2\u01e2p\3")
        buf.write("\2\2\2\u01e3\u01e4\7G\2\2\u01e4\u01e5\7n\2\2\u01e5\u01e6")
        buf.write("\7u\2\2\u01e6\u01e7\7g\2\2\u01e7\u01e8\7k\2\2\u01e8\u01e9")
        buf.write("\7h\2\2\u01e9r\3\2\2\2\u01ea\u01eb\7G\2\2\u01eb\u01ec")
        buf.write("\7n\2\2\u01ec\u01ed\7u\2\2\u01ed\u01ee\7g\2\2\u01eet\3")
        buf.write("\2\2\2\u01ef\u01f0\7u\2\2\u01f0\u01f1\7g\2\2\u01f1\u01f2")
        buf.write("\7n\2\2\u01f2\u01f3\7h\2\2\u01f3v\3\2\2\2\u01f4\u01f5")
        buf.write("\7K\2\2\u01f5\u01f6\7p\2\2\u01f6x\3\2\2\2\u01f7\u01f8")
        buf.write("\7D\2\2\u01f8\u01f9\7{\2\2\u01f9z\3\2\2\2\u01fa\u01fb")
        buf.write("\7t\2\2\u01fb\u01fc\7g\2\2\u01fc\u01fd\7v\2\2\u01fd\u01fe")
        buf.write("\7w\2\2\u01fe\u01ff\7t\2\2\u01ff\u0200\7p\2\2\u0200|\3")
        buf.write("\2\2\2\u0201\u0202\7p\2\2\u0202\u0203\7g\2\2\u0203\u0204")
        buf.write("\7y\2\2\u0204~\3\2\2\2\u0205\u0206\7-\2\2\u0206\u0080")
        buf.write("\3\2\2\2\u0207\u0208\7/\2\2\u0208\u0082\3\2\2\2\u0209")
        buf.write("\u020a\7,\2\2\u020a\u0084\3\2\2\2\u020b\u020c\7\61\2\2")
        buf.write("\u020c\u0086\3\2\2\2\u020d\u020e\7\'\2\2\u020e\u0088\3")
        buf.write("\2\2\2\u020f\u0210\7#\2\2\u0210\u008a\3\2\2\2\u0211\u0212")
        buf.write("\7(\2\2\u0212\u0213\7(\2\2\u0213\u008c\3\2\2\2\u0214\u0215")
        buf.write("\7~\2\2\u0215\u0216\7~\2\2\u0216\u008e\3\2\2\2\u0217\u0218")
        buf.write("\7?\2\2\u0218\u0219\7?\2\2\u0219\u0090\3\2\2\2\u021a\u021b")
        buf.write("\7?\2\2\u021b\u0092\3\2\2\2\u021c\u021d\7#\2\2\u021d\u021e")
        buf.write("\7?\2\2\u021e\u0094\3\2\2\2\u021f\u0220\7@\2\2\u0220\u0096")
        buf.write("\3\2\2\2\u0221\u0222\7@\2\2\u0222\u0223\7?\2\2\u0223\u0098")
        buf.write("\3\2\2\2\u0224\u0225\7>\2\2\u0225\u0226\7?\2\2\u0226\u009a")
        buf.write("\3\2\2\2\u0227\u0228\7>\2\2\u0228\u009c\3\2\2\2\u0229")
        buf.write("\u022a\7?\2\2\u022a\u022b\7?\2\2\u022b\u022c\7\60\2\2")
        buf.write("\u022c\u009e\3\2\2\2\u022d\u022e\7-\2\2\u022e\u022f\7")
        buf.write("\60\2\2\u022f\u00a0\3\2\2\2\u0230\u0234\t\f\2\2\u0231")
        buf.write("\u0233\t\r\2\2\u0232\u0231\3\2\2\2\u0233\u0236\3\2\2\2")
        buf.write("\u0234\u0232\3\2\2\2\u0234\u0235\3\2\2\2\u0235\u023e\3")
        buf.write("\2\2\2\u0236\u0234\3\2\2\2\u0237\u0239\5? \2\u0238\u023a")
        buf.write("\t\r\2\2\u0239\u0238\3\2\2\2\u023a\u023b\3\2\2\2\u023b")
        buf.write("\u0239\3\2\2\2\u023b\u023c\3\2\2\2\u023c\u023e\3\2\2\2")
        buf.write("\u023d\u0230\3\2\2\2\u023d\u0237\3\2\2\2\u023e\u00a2\3")
        buf.write("\2\2\2\u023f\u0245\5\u00a1Q\2\u0240\u0241\5O(\2\u0241")
        buf.write("\u0242\5\u00a1Q\2\u0242\u0244\3\2\2\2\u0243\u0240\3\2")
        buf.write("\2\2\u0244\u0247\3\2\2\2\u0245\u0243\3\2\2\2\u0245\u0246")
        buf.write("\3\2\2\2\u0246\u00a4\3\2\2\2\u0247\u0245\3\2\2\2\u0248")
        buf.write("\u024a\t\16\2\2\u0249\u0248\3\2\2\2\u024a\u024b\3\2\2")
        buf.write("\2\u024b\u0249\3\2\2\2\u024b\u024c\3\2\2\2\u024c\u024d")
        buf.write("\3\2\2\2\u024d\u024e\bS\5\2\u024e\u00a6\3\2\2\2\u024f")
        buf.write("\u0250\7%\2\2\u0250\u0251\7%\2\2\u0251\u0255\3\2\2\2\u0252")
        buf.write("\u0254\13\2\2\2\u0253\u0252\3\2\2\2\u0254\u0257\3\2\2")
        buf.write("\2\u0255\u0256\3\2\2\2\u0255\u0253\3\2\2\2\u0256\u0258")
        buf.write("\3\2\2\2\u0257\u0255\3\2\2\2\u0258\u0259\7%\2\2\u0259")
        buf.write("\u025a\7%\2\2\u025a\u025b\3\2\2\2\u025b\u025c\bT\5\2\u025c")
        buf.write("\u00a8\3\2\2\2\u025d\u025e\7%\2\2\u025e\u025f\7%\2\2\u025f")
        buf.write("\u0263\3\2\2\2\u0260\u0262\13\2\2\2\u0261\u0260\3\2\2")
        buf.write("\2\u0262\u0265\3\2\2\2\u0263\u0264\3\2\2\2\u0263\u0261")
        buf.write("\3\2\2\2\u0264\u0266\3\2\2\2\u0265\u0263\3\2\2\2\u0266")
        buf.write("\u0267\bU\6\2\u0267\u00aa\3\2\2\2\u0268\u0269\13\2\2\2")
        buf.write("\u0269\u026a\bV\7\2\u026a\u00ac\3\2\2\2$\2\u00b7\u00bd")
        buf.write("\u00c7\u00d5\u00e2\u00f7\u0109\u010f\u0115\u011a\u0120")
        buf.write("\u0126\u012b\u0132\u0135\u013b\u0145\u014f\u015a\u0164")
        buf.write("\u0168\u016a\u0171\u019f\u01aa\u01ad\u0234\u023b\u023d")
        buf.write("\u0245\u024b\u0255\u0263\b\3\25\2\3\26\3\3\27\4\b\2\2")
        buf.write("\3U\5\3V\6")
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
    CLASS = 13
    PRIMITIVE_TYPE = 14
    INTEGER_LITERAL = 15
    HEX_TYPE = 16
    OCT_TYPE = 17
    BIN_TYPE = 18
    DEC_TYPE = 19
    STRING_LITERAL = 20
    ILLEGAL_ESCAPE = 21
    UNCLOSE_STRING = 22
    REAL_LITERAL = 23
    LITERAL = 24
    ARRAY = 25
    VAL = 26
    VAR = 27
    DOLLAR = 28
    LP = 29
    RP = 30
    LCB = 31
    RCB = 32
    LSB = 33
    RSB = 34
    SEMI = 35
    COMMA = 36
    COLON = 37
    SCOPE = 38
    DOTDOT = 39
    DOT = 40
    BREAK = 41
    FOREACH = 42
    BOOLEAN = 43
    NULL = 44
    CONTINUE = 45
    TRUE = 46
    FALSE = 47
    IF = 48
    ELSEIF = 49
    ELSE = 50
    SELF = 51
    IN = 52
    BY = 53
    RETURN = 54
    NEW = 55
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
    LTE = 69
    LT = 70
    EQUAL_STR = 71
    ADD_STR = 72
    ID = 73
    ID_LIST = 74
    WS = 75
    BLOCK_COMMENT = 76
    UNTERMINATED_COMMENT = 77
    ERROR_CHAR = 78

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'main'", "'Int'", "'Float'", "'String'", "'Void'", "'class'", 
            "'Array'", "'val'", "'var'", "'$'", "'('", "')'", "'{'", "'}'", 
            "'['", "']'", "';'", "','", "':'", "'::'", "'..'", "'.'", "'Break'", 
            "'Foreach'", "'Boolean'", "'Null'", "'Continue'", "'True'", 
            "'False'", "'If'", "'Elseif'", "'Else'", "'self'", "'In'", "'By'", 
            "'return'", "'new'", "'+'", "'-'", "'*'", "'/'", "'%'", "'!'", 
            "'&&'", "'||'", "'=='", "'='", "'!='", "'>'", "'>='", "'<='", 
            "'<'", "'==.'", "'+.'" ]

    symbolicNames = [ "<INVALID>",
            "CLASS_DECLARE", "MEMBER", "METHODS", "BLOCK_STATEMENT", "LIST_PARAM", 
            "LIST_METHOD", "INT_TYPE", "FLOAT_TYPE", "STRING", "BOOL_TYPE", 
            "VOID_TYPE", "CLASS", "PRIMITIVE_TYPE", "INTEGER_LITERAL", "HEX_TYPE", 
            "OCT_TYPE", "BIN_TYPE", "DEC_TYPE", "STRING_LITERAL", "ILLEGAL_ESCAPE", 
            "UNCLOSE_STRING", "REAL_LITERAL", "LITERAL", "ARRAY", "VAL", 
            "VAR", "DOLLAR", "LP", "RP", "LCB", "RCB", "LSB", "RSB", "SEMI", 
            "COMMA", "COLON", "SCOPE", "DOTDOT", "DOT", "BREAK", "FOREACH", 
            "BOOLEAN", "NULL", "CONTINUE", "TRUE", "FALSE", "IF", "ELSEIF", 
            "ELSE", "SELF", "IN", "BY", "RETURN", "NEW", "ADD", "SUB", "MUL", 
            "DIV", "MOD", "NOT", "AND", "OR", "EQUAL", "ASSIGN", "NOTEQUAL", 
            "GT", "GTE", "LTE", "LT", "EQUAL_STR", "ADD_STR", "ID", "ID_LIST", 
            "WS", "BLOCK_COMMENT", "UNTERMINATED_COMMENT", "ERROR_CHAR" ]

    ruleNames = [ "T__0", "CLASS_DECLARE", "MEMBER", "METHODS", "BLOCK_STATEMENT", 
                  "LIST_PARAM", "LIST_METHOD", "INT_TYPE", "FLOAT_TYPE", 
                  "STRING", "BOOL_TYPE", "VOID_TYPE", "CLASS", "PRIMITIVE_TYPE", 
                  "INTEGER_LITERAL", "HEX_TYPE", "OCT_TYPE", "BIN_TYPE", 
                  "DEC_TYPE", "STRING_LITERAL", "ILLEGAL_ESCAPE", "UNCLOSE_STRING", 
                  "STR", "ESC_SEQ", "ESC_ILLEGAL", "REAL_LITERAL", "LITERAL", 
                  "ARRAY", "VAL", "VAR", "DOLLAR", "LP", "RP", "LCB", "RCB", 
                  "LSB", "RSB", "SEMI", "COMMA", "COLON", "SCOPE", "DOTDOT", 
                  "DOT", "EXPONENT", "DIGIT", "DEC_DIGIT", "SIGN", "BREAK", 
                  "FOREACH", "BOOLEAN", "NULL", "CONTINUE", "TRUE", "FALSE", 
                  "IF", "ELSEIF", "ELSE", "SELF", "IN", "BY", "RETURN", 
                  "NEW", "ADD", "SUB", "MUL", "DIV", "MOD", "NOT", "AND", 
                  "OR", "EQUAL", "ASSIGN", "NOTEQUAL", "GT", "GTE", "LTE", 
                  "LT", "EQUAL_STR", "ADD_STR", "ID", "ID_LIST", "WS", "BLOCK_COMMENT", 
                  "UNTERMINATED_COMMENT", "ERROR_CHAR" ]

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
            actions[19] = self.STRING_LITERAL_action 
            actions[20] = self.ILLEGAL_ESCAPE_action 
            actions[21] = self.UNCLOSE_STRING_action 
            actions[83] = self.UNTERMINATED_COMMENT_action 
            actions[84] = self.ERROR_CHAR_action 
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

     


