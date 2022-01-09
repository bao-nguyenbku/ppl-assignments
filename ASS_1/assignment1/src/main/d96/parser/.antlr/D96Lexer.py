# Generated from e:\HCMUT\PRINCIPLES_OF_PROGRAMMING_LANGUAGE\ppl-assignments\ASS_1\assignment1\src\main\d96\parser\D96.g4 by ANTLR 4.8
from antlr4 import *
from io import StringIO
from typing.io import TextIO
import sys


from lexererr import *



def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2O")
        buf.write("\u0275\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7")
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
        buf.write("L\4M\tM\4N\tN\4O\tO\4P\tP\4Q\tQ\4R\tR\4S\tS\4T\tT\3\2")
        buf.write("\3\2\3\2\3\2\3\2\3\3\3\3\3\3\3\3\3\3\5\3\u00b4\n\3\3\3")
        buf.write("\3\3\7\3\u00b8\n\3\f\3\16\3\u00bb\13\3\3\3\3\3\3\4\3\4")
        buf.write("\3\5\3\5\3\5\5\5\u00c4\n\5\3\5\3\5\3\5\3\6\3\6\3\6\3\7")
        buf.write("\3\7\3\7\3\7\7\7\u00d0\n\7\f\7\16\7\u00d3\13\7\3\b\3\b")
        buf.write("\3\b\3\b\3\b\3\b\3\b\3\b\3\b\3\b\5\b\u00df\n\b\3\t\3\t")
        buf.write("\3\t\3\t\3\n\3\n\3\n\3\n\3\n\3\n\3\13\3\13\3\13\3\13\3")
        buf.write("\13\3\13\3\13\3\f\3\f\5\f\u00f4\n\f\3\r\3\r\3\r\3\r\3")
        buf.write("\r\3\16\3\16\3\16\3\16\3\16\3\16\3\16\3\17\3\17\3\17\3")
        buf.write("\17\3\17\3\17\7\17\u0108\n\17\f\17\16\17\u010b\13\17\3")
        buf.write("\17\3\17\3\20\3\20\3\20\3\20\3\20\3\20\3\21\3\21\3\21")
        buf.write("\3\21\3\21\3\21\5\21\u011b\n\21\3\22\3\22\3\22\3\22\5")
        buf.write("\22\u0121\n\22\3\23\3\23\3\23\3\23\5\23\u0127\n\23\3\23")
        buf.write("\6\23\u012a\n\23\r\23\16\23\u012b\3\24\3\24\6\24\u0130")
        buf.write("\n\24\r\24\16\24\u0131\3\25\3\25\3\25\3\25\5\25\u0138")
        buf.write("\n\25\3\25\6\25\u013b\n\25\r\25\16\25\u013c\3\26\3\26")
        buf.write("\3\26\7\26\u0142\n\26\f\26\16\26\u0145\13\26\5\26\u0147")
        buf.write("\n\26\3\27\3\27\7\27\u014b\n\27\f\27\16\27\u014e\13\27")
        buf.write("\3\27\3\27\3\27\3\30\3\30\5\30\u0155\n\30\3\30\3\30\7")
        buf.write("\30\u0159\n\30\f\30\16\30\u015c\13\30\3\31\3\31\3\31\3")
        buf.write("\31\5\31\u0162\n\31\3\32\3\32\3\32\3\32\3\32\3\32\3\33")
        buf.write("\3\33\3\33\3\33\3\34\3\34\3\34\3\34\3\35\3\35\3\36\3\36")
        buf.write("\3\37\3\37\3 \3 \3!\3!\3\"\3\"\3#\3#\3$\3$\3%\3%\3&\3")
        buf.write("&\3\'\3\'\3\'\3(\3(\3)\3)\5)\u018d\n)\3)\3)\3*\3*\3+\3")
        buf.write("+\3+\7+\u0196\n+\f+\16+\u0199\13+\5+\u019b\n+\3,\3,\3")
        buf.write("-\3-\3-\3-\3-\3-\3.\3.\3.\3.\3.\3.\3.\3.\3/\3/\3/\3/\3")
        buf.write("/\3/\3/\3/\3\60\3\60\3\60\3\60\3\60\3\61\3\61\3\61\3\61")
        buf.write("\3\61\3\61\3\61\3\61\3\61\3\62\3\62\3\62\3\62\3\62\3\63")
        buf.write("\3\63\3\63\3\63\3\63\3\63\3\64\3\64\3\64\3\65\3\65\3\65")
        buf.write("\3\65\3\65\3\65\3\65\3\66\3\66\3\66\3\66\3\66\3\66\3\66")
        buf.write("\3\66\3\66\3\66\3\67\3\67\3\67\3\67\3\67\38\38\38\38\3")
        buf.write("8\39\39\39\39\39\39\39\3:\3:\3:\3:\3;\3;\3<\3<\3<\3=\3")
        buf.write("=\3>\3>\3?\3?\3@\3@\3A\3A\3B\3B\3B\3C\3C\3C\3D\3D\3D\3")
        buf.write("D\3E\3E\3E\3F\3F\3F\3G\3G\3H\3H\3H\3I\3I\3J\3J\3J\3K\3")
        buf.write("K\3L\3L\3L\3L\7L\u0226\nL\fL\16L\u0229\13L\3M\3M\7M\u022d")
        buf.write("\nM\fM\16M\u0230\13M\3M\3M\3M\5M\u0235\nM\3N\3N\3N\3N")
        buf.write("\3N\5N\u023c\nN\3O\6O\u023f\nO\rO\16O\u0240\3O\3O\3P\3")
        buf.write("P\3P\3P\7P\u0249\nP\fP\16P\u024c\13P\3P\3P\3P\3P\3P\3")
        buf.write("Q\3Q\7Q\u0255\nQ\fQ\16Q\u0258\13Q\3Q\3Q\3Q\3R\3R\7R\u025f")
        buf.write("\nR\fR\16R\u0262\13R\3R\3R\3R\3R\3S\3S\3S\3T\3T\3T\3T")
        buf.write("\7T\u026f\nT\fT\16T\u0272\13T\3T\3T\4\u024a\u0270\2U\3")
        buf.write("\3\5\4\7\5\t\6\13\7\r\b\17\t\21\n\23\13\25\f\27\r\31\16")
        buf.write("\33\17\35\20\37\21!\22#\23%\24\'\25)\26+\27-\30/\31\61")
        buf.write("\32\63\33\65\34\67\359\36;\37= ?!A\"C#E$G%I&K\'M(O\2Q")
        buf.write("\2S\2U\2W\2Y)[*]+_,a-c.e/g\60i\61k\62m\63o\64q\65s\66")
        buf.write("u\67w8y9{:};\177<\u0081=\u0083>\u0085?\u0087@\u0089A\u008b")
        buf.write("B\u008dC\u008fD\u0091E\u0093F\u0095G\u0097H\u0099I\u009b")
        buf.write("\2\u009dJ\u009fK\u00a1L\u00a3M\u00a5N\u00a7O\3\2\16\5")
        buf.write("\2\62;CHch\3\2\62;\3\2\62\63\3\2\63;\4\2\62;aa\4\2GGg")
        buf.write("g\4\2--//\5\2C\\aac|\6\2\62;C\\aac|\t\2$$^^ddhhppttvv")
        buf.write("\6\2\f\f\17\17$$^^\5\2\13\f\17\17\"\"\2\u0298\2\3\3\2")
        buf.write("\2\2\2\5\3\2\2\2\2\7\3\2\2\2\2\t\3\2\2\2\2\13\3\2\2\2")
        buf.write("\2\r\3\2\2\2\2\17\3\2\2\2\2\21\3\2\2\2\2\23\3\2\2\2\2")
        buf.write("\25\3\2\2\2\2\27\3\2\2\2\2\31\3\2\2\2\2\33\3\2\2\2\2\35")
        buf.write("\3\2\2\2\2\37\3\2\2\2\2!\3\2\2\2\2#\3\2\2\2\2%\3\2\2\2")
        buf.write("\2\'\3\2\2\2\2)\3\2\2\2\2+\3\2\2\2\2-\3\2\2\2\2/\3\2\2")
        buf.write("\2\2\61\3\2\2\2\2\63\3\2\2\2\2\65\3\2\2\2\2\67\3\2\2\2")
        buf.write("\29\3\2\2\2\2;\3\2\2\2\2=\3\2\2\2\2?\3\2\2\2\2A\3\2\2")
        buf.write("\2\2C\3\2\2\2\2E\3\2\2\2\2G\3\2\2\2\2I\3\2\2\2\2K\3\2")
        buf.write("\2\2\2M\3\2\2\2\2Y\3\2\2\2\2[\3\2\2\2\2]\3\2\2\2\2_\3")
        buf.write("\2\2\2\2a\3\2\2\2\2c\3\2\2\2\2e\3\2\2\2\2g\3\2\2\2\2i")
        buf.write("\3\2\2\2\2k\3\2\2\2\2m\3\2\2\2\2o\3\2\2\2\2q\3\2\2\2\2")
        buf.write("s\3\2\2\2\2u\3\2\2\2\2w\3\2\2\2\2y\3\2\2\2\2{\3\2\2\2")
        buf.write("\2}\3\2\2\2\2\177\3\2\2\2\2\u0081\3\2\2\2\2\u0083\3\2")
        buf.write("\2\2\2\u0085\3\2\2\2\2\u0087\3\2\2\2\2\u0089\3\2\2\2\2")
        buf.write("\u008b\3\2\2\2\2\u008d\3\2\2\2\2\u008f\3\2\2\2\2\u0091")
        buf.write("\3\2\2\2\2\u0093\3\2\2\2\2\u0095\3\2\2\2\2\u0097\3\2\2")
        buf.write("\2\2\u0099\3\2\2\2\2\u009d\3\2\2\2\2\u009f\3\2\2\2\2\u00a1")
        buf.write("\3\2\2\2\2\u00a3\3\2\2\2\2\u00a5\3\2\2\2\2\u00a7\3\2\2")
        buf.write("\2\3\u00a9\3\2\2\2\5\u00ae\3\2\2\2\7\u00be\3\2\2\2\t\u00c0")
        buf.write("\3\2\2\2\13\u00c8\3\2\2\2\r\u00cb\3\2\2\2\17\u00de\3\2")
        buf.write("\2\2\21\u00e0\3\2\2\2\23\u00e4\3\2\2\2\25\u00ea\3\2\2")
        buf.write("\2\27\u00f3\3\2\2\2\31\u00f5\3\2\2\2\33\u00fa\3\2\2\2")
        buf.write("\35\u0101\3\2\2\2\37\u010e\3\2\2\2!\u011a\3\2\2\2#\u0120")
        buf.write("\3\2\2\2%\u0126\3\2\2\2\'\u012d\3\2\2\2)\u0137\3\2\2\2")
        buf.write("+\u0146\3\2\2\2-\u0148\3\2\2\2/\u0152\3\2\2\2\61\u0161")
        buf.write("\3\2\2\2\63\u0163\3\2\2\2\65\u0169\3\2\2\2\67\u016d\3")
        buf.write("\2\2\29\u0171\3\2\2\2;\u0173\3\2\2\2=\u0175\3\2\2\2?\u0177")
        buf.write("\3\2\2\2A\u0179\3\2\2\2C\u017b\3\2\2\2E\u017d\3\2\2\2")
        buf.write("G\u017f\3\2\2\2I\u0181\3\2\2\2K\u0183\3\2\2\2M\u0185\3")
        buf.write("\2\2\2O\u0188\3\2\2\2Q\u018a\3\2\2\2S\u0190\3\2\2\2U\u019a")
        buf.write("\3\2\2\2W\u019c\3\2\2\2Y\u019e\3\2\2\2[\u01a4\3\2\2\2")
        buf.write("]\u01ac\3\2\2\2_\u01b4\3\2\2\2a\u01b9\3\2\2\2c\u01c2\3")
        buf.write("\2\2\2e\u01c7\3\2\2\2g\u01cd\3\2\2\2i\u01d0\3\2\2\2k\u01d7")
        buf.write("\3\2\2\2m\u01e1\3\2\2\2o\u01e6\3\2\2\2q\u01eb\3\2\2\2")
        buf.write("s\u01f2\3\2\2\2u\u01f6\3\2\2\2w\u01f8\3\2\2\2y\u01fb\3")
        buf.write("\2\2\2{\u01fd\3\2\2\2}\u01ff\3\2\2\2\177\u0201\3\2\2\2")
        buf.write("\u0081\u0203\3\2\2\2\u0083\u0205\3\2\2\2\u0085\u0208\3")
        buf.write("\2\2\2\u0087\u020b\3\2\2\2\u0089\u020f\3\2\2\2\u008b\u0212")
        buf.write("\3\2\2\2\u008d\u0215\3\2\2\2\u008f\u0217\3\2\2\2\u0091")
        buf.write("\u021a\3\2\2\2\u0093\u021c\3\2\2\2\u0095\u021f\3\2\2\2")
        buf.write("\u0097\u0221\3\2\2\2\u0099\u0234\3\2\2\2\u009b\u023b\3")
        buf.write("\2\2\2\u009d\u023e\3\2\2\2\u009f\u0244\3\2\2\2\u00a1\u0252")
        buf.write("\3\2\2\2\u00a3\u025c\3\2\2\2\u00a5\u0267\3\2\2\2\u00a7")
        buf.write("\u026a\3\2\2\2\u00a9\u00aa\7o\2\2\u00aa\u00ab\7c\2\2\u00ab")
        buf.write("\u00ac\7k\2\2\u00ac\u00ad\7p\2\2\u00ad\4\3\2\2\2\u00ae")
        buf.write("\u00af\5\37\20\2\u00af\u00b3\5\u0099M\2\u00b0\u00b1\5")
        buf.write("K&\2\u00b1\u00b2\5\u0099M\2\u00b2\u00b4\3\2\2\2\u00b3")
        buf.write("\u00b0\3\2\2\2\u00b3\u00b4\3\2\2\2\u00b4\u00b5\3\2\2\2")
        buf.write("\u00b5\u00b9\5? \2\u00b6\u00b8\5\7\4\2\u00b7\u00b6\3\2")
        buf.write("\2\2\u00b8\u00bb\3\2\2\2\u00b9\u00b7\3\2\2\2\u00b9\u00ba")
        buf.write("\3\2\2\2\u00ba\u00bc\3\2\2\2\u00bb\u00b9\3\2\2\2\u00bc")
        buf.write("\u00bd\5A!\2\u00bd\6\3\2\2\2\u00be\u00bf\5\t\5\2\u00bf")
        buf.write("\b\3\2\2\2\u00c0\u00c1\5\u0099M\2\u00c1\u00c3\5;\36\2")
        buf.write("\u00c2\u00c4\5\r\7\2\u00c3\u00c2\3\2\2\2\u00c3\u00c4\3")
        buf.write("\2\2\2\u00c4\u00c5\3\2\2\2\u00c5\u00c6\5=\37\2\u00c6\u00c7")
        buf.write("\5\13\6\2\u00c7\n\3\2\2\2\u00c8\u00c9\5? \2\u00c9\u00ca")
        buf.write("\5A!\2\u00ca\f\3\2\2\2\u00cb\u00d1\5\17\b\2\u00cc\u00cd")
        buf.write("\5G$\2\u00cd\u00ce\5\17\b\2\u00ce\u00d0\3\2\2\2\u00cf")
        buf.write("\u00cc\3\2\2\2\u00d0\u00d3\3\2\2\2\u00d1\u00cf\3\2\2\2")
        buf.write("\u00d1\u00d2\3\2\2\2\u00d2\16\3\2\2\2\u00d3\u00d1\3\2")
        buf.write("\2\2\u00d4\u00d5\5\u0099M\2\u00d5\u00d6\5K&\2\u00d6\u00d7")
        buf.write("\5!\21\2\u00d7\u00df\3\2\2\2\u00d8\u00d9\5\u0099M\2\u00d9")
        buf.write("\u00da\5K&\2\u00da\u00db\5!\21\2\u00db\u00dc\5I%\2\u00dc")
        buf.write("\u00dd\5\17\b\2\u00dd\u00df\3\2\2\2\u00de\u00d4\3\2\2")
        buf.write("\2\u00de\u00d8\3\2\2\2\u00df\20\3\2\2\2\u00e0\u00e1\7")
        buf.write("K\2\2\u00e1\u00e2\7p\2\2\u00e2\u00e3\7v\2\2\u00e3\22\3")
        buf.write("\2\2\2\u00e4\u00e5\7H\2\2\u00e5\u00e6\7n\2\2\u00e6\u00e7")
        buf.write("\7q\2\2\u00e7\u00e8\7c\2\2\u00e8\u00e9\7v\2\2\u00e9\24")
        buf.write("\3\2\2\2\u00ea\u00eb\7u\2\2\u00eb\u00ec\7v\2\2\u00ec\u00ed")
        buf.write("\7t\2\2\u00ed\u00ee\7k\2\2\u00ee\u00ef\7p\2\2\u00ef\u00f0")
        buf.write("\7i\2\2\u00f0\26\3\2\2\2\u00f1\u00f4\5c\62\2\u00f2\u00f4")
        buf.write("\5e\63\2\u00f3\u00f1\3\2\2\2\u00f3\u00f2\3\2\2\2\u00f4")
        buf.write("\30\3\2\2\2\u00f5\u00f6\7X\2\2\u00f6\u00f7\7q\2\2\u00f7")
        buf.write("\u00f8\7k\2\2\u00f8\u00f9\7f\2\2\u00f9\32\3\2\2\2\u00fa")
        buf.write("\u00fb\5\63\32\2\u00fb\u00fc\5C\"\2\u00fc\u00fd\5!\21")
        buf.write("\2\u00fd\u00fe\5I%\2\u00fe\u00ff\5#\22\2\u00ff\u0100\5")
        buf.write("E#\2\u0100\34\3\2\2\2\u0101\u0102\5\63\32\2\u0102\u0103")
        buf.write("\5;\36\2\u0103\u0109\5\61\31\2\u0104\u0105\5I%\2\u0105")
        buf.write("\u0106\5\61\31\2\u0106\u0108\3\2\2\2\u0107\u0104\3\2\2")
        buf.write("\2\u0108\u010b\3\2\2\2\u0109\u0107\3\2\2\2\u0109\u010a")
        buf.write("\3\2\2\2\u010a\u010c\3\2\2\2\u010b\u0109\3\2\2\2\u010c")
        buf.write("\u010d\5=\37\2\u010d\36\3\2\2\2\u010e\u010f\7e\2\2\u010f")
        buf.write("\u0110\7n\2\2\u0110\u0111\7c\2\2\u0111\u0112\7u\2\2\u0112")
        buf.write("\u0113\7u\2\2\u0113 \3\2\2\2\u0114\u011b\5\27\f\2\u0115")
        buf.write("\u011b\5\21\t\2\u0116\u011b\5\23\n\2\u0117\u011b\5\25")
        buf.write("\13\2\u0118\u011b\5\33\16\2\u0119\u011b\5\37\20\2\u011a")
        buf.write("\u0114\3\2\2\2\u011a\u0115\3\2\2\2\u011a\u0116\3\2\2\2")
        buf.write("\u011a\u0117\3\2\2\2\u011a\u0118\3\2\2\2\u011a\u0119\3")
        buf.write("\2\2\2\u011b\"\3\2\2\2\u011c\u0121\5%\23\2\u011d\u0121")
        buf.write("\5\'\24\2\u011e\u0121\5)\25\2\u011f\u0121\5+\26\2\u0120")
        buf.write("\u011c\3\2\2\2\u0120\u011d\3\2\2\2\u0120\u011e\3\2\2\2")
        buf.write("\u0120\u011f\3\2\2\2\u0121$\3\2\2\2\u0122\u0123\7\62\2")
        buf.write("\2\u0123\u0127\7z\2\2\u0124\u0125\7\62\2\2\u0125\u0127")
        buf.write("\7Z\2\2\u0126\u0122\3\2\2\2\u0126\u0124\3\2\2\2\u0127")
        buf.write("\u0129\3\2\2\2\u0128\u012a\t\2\2\2\u0129\u0128\3\2\2\2")
        buf.write("\u012a\u012b\3\2\2\2\u012b\u0129\3\2\2\2\u012b\u012c\3")
        buf.write("\2\2\2\u012c&\3\2\2\2\u012d\u012f\7\62\2\2\u012e\u0130")
        buf.write("\t\3\2\2\u012f\u012e\3\2\2\2\u0130\u0131\3\2\2\2\u0131")
        buf.write("\u012f\3\2\2\2\u0131\u0132\3\2\2\2\u0132(\3\2\2\2\u0133")
        buf.write("\u0134\7\62\2\2\u0134\u0138\7d\2\2\u0135\u0136\7\62\2")
        buf.write("\2\u0136\u0138\7D\2\2\u0137\u0133\3\2\2\2\u0137\u0135")
        buf.write("\3\2\2\2\u0138\u013a\3\2\2\2\u0139\u013b\t\4\2\2\u013a")
        buf.write("\u0139\3\2\2\2\u013b\u013c\3\2\2\2\u013c\u013a\3\2\2\2")
        buf.write("\u013c\u013d\3\2\2\2\u013d*\3\2\2\2\u013e\u0147\t\3\2")
        buf.write("\2\u013f\u0143\t\5\2\2\u0140\u0142\t\6\2\2\u0141\u0140")
        buf.write("\3\2\2\2\u0142\u0145\3\2\2\2\u0143\u0141\3\2\2\2\u0143")
        buf.write("\u0144\3\2\2\2\u0144\u0147\3\2\2\2\u0145\u0143\3\2\2\2")
        buf.write("\u0146\u013e\3\2\2\2\u0146\u013f\3\2\2\2\u0147,\3\2\2")
        buf.write("\2\u0148\u014c\7$\2\2\u0149\u014b\5\u009bN\2\u014a\u0149")
        buf.write("\3\2\2\2\u014b\u014e\3\2\2\2\u014c\u014a\3\2\2\2\u014c")
        buf.write("\u014d\3\2\2\2\u014d\u014f\3\2\2\2\u014e\u014c\3\2\2\2")
        buf.write("\u014f\u0150\7$\2\2\u0150\u0151\b\27\2\2\u0151.\3\2\2")
        buf.write("\2\u0152\u0154\5U+\2\u0153\u0155\5O(\2\u0154\u0153\3\2")
        buf.write("\2\2\u0154\u0155\3\2\2\2\u0155\u015a\3\2\2\2\u0156\u0159")
        buf.write("\5U+\2\u0157\u0159\5Q)\2\u0158\u0156\3\2\2\2\u0158\u0157")
        buf.write("\3\2\2\2\u0159\u015c\3\2\2\2\u015a\u0158\3\2\2\2\u015a")
        buf.write("\u015b\3\2\2\2\u015b\60\3\2\2\2\u015c\u015a\3\2\2\2\u015d")
        buf.write("\u0162\5#\22\2\u015e\u0162\5\27\f\2\u015f\u0162\5/\30")
        buf.write("\2\u0160\u0162\5-\27\2\u0161\u015d\3\2\2\2\u0161\u015e")
        buf.write("\3\2\2\2\u0161\u015f\3\2\2\2\u0161\u0160\3\2\2\2\u0162")
        buf.write("\62\3\2\2\2\u0163\u0164\7C\2\2\u0164\u0165\7t\2\2\u0165")
        buf.write("\u0166\7t\2\2\u0166\u0167\7c\2\2\u0167\u0168\7{\2\2\u0168")
        buf.write("\64\3\2\2\2\u0169\u016a\7x\2\2\u016a\u016b\7c\2\2\u016b")
        buf.write("\u016c\7n\2\2\u016c\66\3\2\2\2\u016d\u016e\7x\2\2\u016e")
        buf.write("\u016f\7c\2\2\u016f\u0170\7t\2\2\u01708\3\2\2\2\u0171")
        buf.write("\u0172\7&\2\2\u0172:\3\2\2\2\u0173\u0174\7*\2\2\u0174")
        buf.write("<\3\2\2\2\u0175\u0176\7+\2\2\u0176>\3\2\2\2\u0177\u0178")
        buf.write("\7}\2\2\u0178@\3\2\2\2\u0179\u017a\7\177\2\2\u017aB\3")
        buf.write("\2\2\2\u017b\u017c\7]\2\2\u017cD\3\2\2\2\u017d\u017e\7")
        buf.write("_\2\2\u017eF\3\2\2\2\u017f\u0180\7=\2\2\u0180H\3\2\2\2")
        buf.write("\u0181\u0182\7.\2\2\u0182J\3\2\2\2\u0183\u0184\7<\2\2")
        buf.write("\u0184L\3\2\2\2\u0185\u0186\7\60\2\2\u0186\u0187\7\60")
        buf.write("\2\2\u0187N\3\2\2\2\u0188\u0189\7\60\2\2\u0189P\3\2\2")
        buf.write("\2\u018a\u018c\t\7\2\2\u018b\u018d\5W,\2\u018c\u018b\3")
        buf.write("\2\2\2\u018c\u018d\3\2\2\2\u018d\u018e\3\2\2\2\u018e\u018f")
        buf.write("\5+\26\2\u018fR\3\2\2\2\u0190\u0191\t\3\2\2\u0191T\3\2")
        buf.write("\2\2\u0192\u019b\t\3\2\2\u0193\u0197\t\5\2\2\u0194\u0196")
        buf.write("\t\6\2\2\u0195\u0194\3\2\2\2\u0196\u0199\3\2\2\2\u0197")
        buf.write("\u0195\3\2\2\2\u0197\u0198\3\2\2\2\u0198\u019b\3\2\2\2")
        buf.write("\u0199\u0197\3\2\2\2\u019a\u0192\3\2\2\2\u019a\u0193\3")
        buf.write("\2\2\2\u019bV\3\2\2\2\u019c\u019d\t\b\2\2\u019dX\3\2\2")
        buf.write("\2\u019e\u019f\7D\2\2\u019f\u01a0\7t\2\2\u01a0\u01a1\7")
        buf.write("g\2\2\u01a1\u01a2\7c\2\2\u01a2\u01a3\7m\2\2\u01a3Z\3\2")
        buf.write("\2\2\u01a4\u01a5\7H\2\2\u01a5\u01a6\7q\2\2\u01a6\u01a7")
        buf.write("\7t\2\2\u01a7\u01a8\7g\2\2\u01a8\u01a9\7c\2\2\u01a9\u01aa")
        buf.write("\7e\2\2\u01aa\u01ab\7j\2\2\u01ab\\\3\2\2\2\u01ac\u01ad")
        buf.write("\7D\2\2\u01ad\u01ae\7q\2\2\u01ae\u01af\7q\2\2\u01af\u01b0")
        buf.write("\7n\2\2\u01b0\u01b1\7g\2\2\u01b1\u01b2\7c\2\2\u01b2\u01b3")
        buf.write("\7p\2\2\u01b3^\3\2\2\2\u01b4\u01b5\7P\2\2\u01b5\u01b6")
        buf.write("\7w\2\2\u01b6\u01b7\7n\2\2\u01b7\u01b8\7n\2\2\u01b8`\3")
        buf.write("\2\2\2\u01b9\u01ba\7E\2\2\u01ba\u01bb\7q\2\2\u01bb\u01bc")
        buf.write("\7p\2\2\u01bc\u01bd\7v\2\2\u01bd\u01be\7k\2\2\u01be\u01bf")
        buf.write("\7p\2\2\u01bf\u01c0\7w\2\2\u01c0\u01c1\7g\2\2\u01c1b\3")
        buf.write("\2\2\2\u01c2\u01c3\7V\2\2\u01c3\u01c4\7t\2\2\u01c4\u01c5")
        buf.write("\7w\2\2\u01c5\u01c6\7g\2\2\u01c6d\3\2\2\2\u01c7\u01c8")
        buf.write("\7H\2\2\u01c8\u01c9\7c\2\2\u01c9\u01ca\7n\2\2\u01ca\u01cb")
        buf.write("\7u\2\2\u01cb\u01cc\7g\2\2\u01ccf\3\2\2\2\u01cd\u01ce")
        buf.write("\7k\2\2\u01ce\u01cf\7h\2\2\u01cfh\3\2\2\2\u01d0\u01d1")
        buf.write("\7g\2\2\u01d1\u01d2\7n\2\2\u01d2\u01d3\7u\2\2\u01d3\u01d4")
        buf.write("\7g\2\2\u01d4\u01d5\7k\2\2\u01d5\u01d6\7h\2\2\u01d6j\3")
        buf.write("\2\2\2\u01d7\u01d8\7C\2\2\u01d8\u01d9\7t\2\2\u01d9\u01da")
        buf.write("\7t\2\2\u01da\u01db\7c\2\2\u01db\u01dc\7{\2\2\u01dc\u01dd")
        buf.write("\7\"\2\2\u01dd\u01de\7K\2\2\u01de\u01df\7p\2\2\u01df\u01e0")
        buf.write("\7v\2\2\u01e0l\3\2\2\2\u01e1\u01e2\7G\2\2\u01e2\u01e3")
        buf.write("\7n\2\2\u01e3\u01e4\7u\2\2\u01e4\u01e5\7g\2\2\u01e5n\3")
        buf.write("\2\2\2\u01e6\u01e7\7u\2\2\u01e7\u01e8\7g\2\2\u01e8\u01e9")
        buf.write("\7n\2\2\u01e9\u01ea\7h\2\2\u01eap\3\2\2\2\u01eb\u01ec")
        buf.write("\7t\2\2\u01ec\u01ed\7g\2\2\u01ed\u01ee\7v\2\2\u01ee\u01ef")
        buf.write("\7w\2\2\u01ef\u01f0\7t\2\2\u01f0\u01f1\7p\2\2\u01f1r\3")
        buf.write("\2\2\2\u01f2\u01f3\7p\2\2\u01f3\u01f4\7g\2\2\u01f4\u01f5")
        buf.write("\7y\2\2\u01f5t\3\2\2\2\u01f6\u01f7\7-\2\2\u01f7v\3\2\2")
        buf.write("\2\u01f8\u01f9\7-\2\2\u01f9\u01fa\7\60\2\2\u01fax\3\2")
        buf.write("\2\2\u01fb\u01fc\7/\2\2\u01fcz\3\2\2\2\u01fd\u01fe\7,")
        buf.write("\2\2\u01fe|\3\2\2\2\u01ff\u0200\7\61\2\2\u0200~\3\2\2")
        buf.write("\2\u0201\u0202\7\'\2\2\u0202\u0080\3\2\2\2\u0203\u0204")
        buf.write("\7#\2\2\u0204\u0082\3\2\2\2\u0205\u0206\7#\2\2\u0206\u0207")
        buf.write("\7?\2\2\u0207\u0084\3\2\2\2\u0208\u0209\7?\2\2\u0209\u020a")
        buf.write("\7?\2\2\u020a\u0086\3\2\2\2\u020b\u020c\7?\2\2\u020c\u020d")
        buf.write("\7?\2\2\u020d\u020e\7\60\2\2\u020e\u0088\3\2\2\2\u020f")
        buf.write("\u0210\7(\2\2\u0210\u0211\7(\2\2\u0211\u008a\3\2\2\2\u0212")
        buf.write("\u0213\7~\2\2\u0213\u0214\7~\2\2\u0214\u008c\3\2\2\2\u0215")
        buf.write("\u0216\7@\2\2\u0216\u008e\3\2\2\2\u0217\u0218\7>\2\2\u0218")
        buf.write("\u0219\7?\2\2\u0219\u0090\3\2\2\2\u021a\u021b\7>\2\2\u021b")
        buf.write("\u0092\3\2\2\2\u021c\u021d\7@\2\2\u021d\u021e\7?\2\2\u021e")
        buf.write("\u0094\3\2\2\2\u021f\u0220\7?\2\2\u0220\u0096\3\2\2\2")
        buf.write("\u0221\u0227\5\u0099M\2\u0222\u0223\5I%\2\u0223\u0224")
        buf.write("\5\u0099M\2\u0224\u0226\3\2\2\2\u0225\u0222\3\2\2\2\u0226")
        buf.write("\u0229\3\2\2\2\u0227\u0225\3\2\2\2\u0227\u0228\3\2\2\2")
        buf.write("\u0228\u0098\3\2\2\2\u0229\u0227\3\2\2\2\u022a\u022e\t")
        buf.write("\t\2\2\u022b\u022d\t\n\2\2\u022c\u022b\3\2\2\2\u022d\u0230")
        buf.write("\3\2\2\2\u022e\u022c\3\2\2\2\u022e\u022f\3\2\2\2\u022f")
        buf.write("\u0235\3\2\2\2\u0230\u022e\3\2\2\2\u0231\u0232\59\35\2")
        buf.write("\u0232\u0233\5\u0099M\2\u0233\u0235\3\2\2\2\u0234\u022a")
        buf.write("\3\2\2\2\u0234\u0231\3\2\2\2\u0235\u009a\3\2\2\2\u0236")
        buf.write("\u0237\7^\2\2\u0237\u023c\t\13\2\2\u0238\u023c\n\f\2\2")
        buf.write("\u0239\u023a\7)\2\2\u023a\u023c\7$\2\2\u023b\u0236\3\2")
        buf.write("\2\2\u023b\u0238\3\2\2\2\u023b\u0239\3\2\2\2\u023c\u009c")
        buf.write("\3\2\2\2\u023d\u023f\t\r\2\2\u023e\u023d\3\2\2\2\u023f")
        buf.write("\u0240\3\2\2\2\u0240\u023e\3\2\2\2\u0240\u0241\3\2\2\2")
        buf.write("\u0241\u0242\3\2\2\2\u0242\u0243\bO\3\2\u0243\u009e\3")
        buf.write("\2\2\2\u0244\u0245\7%\2\2\u0245\u0246\7%\2\2\u0246\u024a")
        buf.write("\3\2\2\2\u0247\u0249\13\2\2\2\u0248\u0247\3\2\2\2\u0249")
        buf.write("\u024c\3\2\2\2\u024a\u024b\3\2\2\2\u024a\u0248\3\2\2\2")
        buf.write("\u024b\u024d\3\2\2\2\u024c\u024a\3\2\2\2\u024d\u024e\7")
        buf.write("%\2\2\u024e\u024f\7%\2\2\u024f\u0250\3\2\2\2\u0250\u0251")
        buf.write("\bP\3\2\u0251\u00a0\3\2\2\2\u0252\u0256\7$\2\2\u0253\u0255")
        buf.write("\5\u009bN\2\u0254\u0253\3\2\2\2\u0255\u0258\3\2\2\2\u0256")
        buf.write("\u0254\3\2\2\2\u0256\u0257\3\2\2\2\u0257\u0259\3\2\2\2")
        buf.write("\u0258\u0256\3\2\2\2\u0259\u025a\7\2\2\3\u025a\u025b\b")
        buf.write("Q\4\2\u025b\u00a2\3\2\2\2\u025c\u0260\7$\2\2\u025d\u025f")
        buf.write("\5\u009bN\2\u025e\u025d\3\2\2\2\u025f\u0262\3\2\2\2\u0260")
        buf.write("\u025e\3\2\2\2\u0260\u0261\3\2\2\2\u0261\u0263\3\2\2\2")
        buf.write("\u0262\u0260\3\2\2\2\u0263\u0264\7^\2\2\u0264\u0265\n")
        buf.write("\13\2\2\u0265\u0266\bR\5\2\u0266\u00a4\3\2\2\2\u0267\u0268")
        buf.write("\13\2\2\2\u0268\u0269\bS\6\2\u0269\u00a6\3\2\2\2\u026a")
        buf.write("\u026b\7%\2\2\u026b\u026c\7%\2\2\u026c\u0270\3\2\2\2\u026d")
        buf.write("\u026f\13\2\2\2\u026e\u026d\3\2\2\2\u026f\u0272\3\2\2")
        buf.write("\2\u0270\u0271\3\2\2\2\u0270\u026e\3\2\2\2\u0271\u0273")
        buf.write("\3\2\2\2\u0272\u0270\3\2\2\2\u0273\u0274\bT\7\2\u0274")
        buf.write("\u00a8\3\2\2\2$\2\u00b3\u00b9\u00c3\u00d1\u00de\u00f3")
        buf.write("\u0109\u011a\u0120\u0126\u012b\u0131\u0137\u013c\u0143")
        buf.write("\u0146\u014c\u0154\u0158\u015a\u0161\u018c\u0197\u019a")
        buf.write("\u0227\u022e\u0234\u023b\u0240\u024a\u0256\u0260\u0270")
        buf.write("\b\3\27\2\b\2\2\3Q\3\3R\4\3S\5\3T\6")
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
    ARRAY_TYPE = 13
    ARRAY_LIST = 14
    CLASS = 15
    PRIMITIVE_TYPE = 16
    INTEGER_LITERAL = 17
    HEX_TYPE = 18
    OCT_TYPE = 19
    BIN_TYPE = 20
    DEC_TYPE = 21
    STRING_LITERAL = 22
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
    DOTDOT = 38
    BREAK = 39
    FOREACH = 40
    BOOLEAN = 41
    NULL = 42
    CONTINUE = 43
    TRUE = 44
    FALSE = 45
    IF = 46
    ELSEIF = 47
    ARRAYINT = 48
    ELSE = 49
    SELF = 50
    RETURN = 51
    NEW = 52
    ADD = 53
    ADD_STR = 54
    SUB = 55
    MUL = 56
    DIV = 57
    MOD = 58
    NOT = 59
    NOTEQUAL = 60
    EQUAL = 61
    EQUAL_STR = 62
    AND = 63
    OR = 64
    GT = 65
    LTE = 66
    LT = 67
    GTE = 68
    ASSIGN = 69
    ID_LIST = 70
    ID = 71
    WS = 72
    BLOCK_COMMENT = 73
    UNCLOSE_STRING = 74
    ILLEGAL_ESCAPE = 75
    ERROR_CHAR = 76
    UNTERMINATED_COMMENT = 77

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'main'", "'Int'", "'Float'", "'string'", "'Void'", "'class'", 
            "'Array'", "'val'", "'var'", "'$'", "'('", "')'", "'{'", "'}'", 
            "'['", "']'", "';'", "','", "':'", "'..'", "'Break'", "'Foreach'", 
            "'Boolean'", "'Null'", "'Continue'", "'True'", "'False'", "'if'", 
            "'elseif'", "'Array Int'", "'Else'", "'self'", "'return'", "'new'", 
            "'+'", "'+.'", "'-'", "'*'", "'/'", "'%'", "'!'", "'!='", "'=='", 
            "'==.'", "'&&'", "'||'", "'>'", "'<='", "'<'", "'>='", "'='" ]

    symbolicNames = [ "<INVALID>",
            "CLASS_DECLARE", "MEMBER", "METHODS", "BLOCK_STATEMENT", "LIST_PARAM", 
            "LIST_METHOD", "INT_TYPE", "FLOAT_TYPE", "STRING", "BOOL_TYPE", 
            "VOID_TYPE", "ARRAY_TYPE", "ARRAY_LIST", "CLASS", "PRIMITIVE_TYPE", 
            "INTEGER_LITERAL", "HEX_TYPE", "OCT_TYPE", "BIN_TYPE", "DEC_TYPE", 
            "STRING_LITERAL", "REAL_LITERAL", "LITERAL", "ARRAY", "VAL", 
            "VAR", "DOLLAR", "LP", "RP", "LCB", "RCB", "LSB", "RSB", "SEMI", 
            "COMMA", "COLON", "DOTDOT", "BREAK", "FOREACH", "BOOLEAN", "NULL", 
            "CONTINUE", "TRUE", "FALSE", "IF", "ELSEIF", "ARRAYINT", "ELSE", 
            "SELF", "RETURN", "NEW", "ADD", "ADD_STR", "SUB", "MUL", "DIV", 
            "MOD", "NOT", "NOTEQUAL", "EQUAL", "EQUAL_STR", "AND", "OR", 
            "GT", "LTE", "LT", "GTE", "ASSIGN", "ID_LIST", "ID", "WS", "BLOCK_COMMENT", 
            "UNCLOSE_STRING", "ILLEGAL_ESCAPE", "ERROR_CHAR", "UNTERMINATED_COMMENT" ]

    ruleNames = [ "T__0", "CLASS_DECLARE", "MEMBER", "METHODS", "BLOCK_STATEMENT", 
                  "LIST_PARAM", "LIST_METHOD", "INT_TYPE", "FLOAT_TYPE", 
                  "STRING", "BOOL_TYPE", "VOID_TYPE", "ARRAY_TYPE", "ARRAY_LIST", 
                  "CLASS", "PRIMITIVE_TYPE", "INTEGER_LITERAL", "HEX_TYPE", 
                  "OCT_TYPE", "BIN_TYPE", "DEC_TYPE", "STRING_LITERAL", 
                  "REAL_LITERAL", "LITERAL", "ARRAY", "VAL", "VAR", "DOLLAR", 
                  "LP", "RP", "LCB", "RCB", "LSB", "RSB", "SEMI", "COMMA", 
                  "COLON", "DOTDOT", "DOT", "EXPONENT", "DIGIT", "DEC_DIGIT", 
                  "SIGN", "BREAK", "FOREACH", "BOOLEAN", "NULL", "CONTINUE", 
                  "TRUE", "FALSE", "IF", "ELSEIF", "ARRAYINT", "ELSE", "SELF", 
                  "RETURN", "NEW", "ADD", "ADD_STR", "SUB", "MUL", "DIV", 
                  "MOD", "NOT", "NOTEQUAL", "EQUAL", "EQUAL_STR", "AND", 
                  "OR", "GT", "LTE", "LT", "GTE", "ASSIGN", "ID_LIST", "ID", 
                  "STR1", "WS", "BLOCK_COMMENT", "UNCLOSE_STRING", "ILLEGAL_ESCAPE", 
                  "ERROR_CHAR", "UNTERMINATED_COMMENT" ]

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
        
        print ("{:<30} {:<30} {:<50}".format(result.text, '|', self.symbolicNames[tk-1]))
        print('--------------------------------------------------------------------------------')
        if tk == self.STRING_LITERAL:
            # string type
            if (result.text[0] == result.text[-1] and result.text[-1] == '"'):
                if result.text.find('\'"') >= 0:
                    result.text = result.text.replace('\'"', '"')
                return result
        if tk == self.INTEGER_LITERAL:
            result.text = result.text.replace('_', '')
            return result
        return result


    def action(self, localctx:RuleContext, ruleIndex:int, actionIndex:int):
        if self._actions is None:
            actions = dict()
            actions[21] = self.STRING_LITERAL_action 
            actions[79] = self.UNCLOSE_STRING_action 
            actions[80] = self.ILLEGAL_ESCAPE_action 
            actions[81] = self.ERROR_CHAR_action 
            actions[82] = self.UNTERMINATED_COMMENT_action 
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

                x = str(self.text)
                raise UncloseString(x[1:])

     

    def ILLEGAL_ESCAPE_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 2:

                y = str(self.text)
                raise IllegalEscape(y[1:])

     

    def ERROR_CHAR_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 3:

                raise ErrorToken(self.text)

     

    def UNTERMINATED_COMMENT_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 4:

                raise ErrorToken('UNTERMINATED_COMMENT')

     


