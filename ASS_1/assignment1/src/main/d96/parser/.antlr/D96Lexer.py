# Generated from e:\HCMUT\PRINCIPLES_OF_PROGRAMMING_LANGUAGE\ppl-assignments\ASS_1\assignment1\src\main\d96\parser\D96.g4 by ANTLR 4.8
from antlr4 import *
from io import StringIO
from typing.io import TextIO
import sys


from lexererr import *



def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2\\")
        buf.write("\u0342\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7")
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
        buf.write("U\4V\tV\4W\tW\4X\tX\4Y\tY\4Z\tZ\4[\t[\4\\\t\\\4]\t]\4")
        buf.write("^\t^\4_\t_\4`\t`\4a\ta\4b\tb\3\2\3\2\3\2\3\2\3\2\3\3\3")
        buf.write("\3\3\3\3\3\3\3\5\3\u00d0\n\3\3\3\3\3\7\3\u00d4\n\3\f\3")
        buf.write("\16\3\u00d7\13\3\3\3\3\3\3\4\3\4\5\4\u00dd\n\4\3\5\3\5")
        buf.write("\3\5\3\5\3\5\3\6\3\6\3\6\3\6\7\6\u00e8\n\6\f\6\16\6\u00eb")
        buf.write("\13\6\3\7\3\7\3\7\3\7\3\7\3\7\3\7\3\7\3\7\3\7\5\7\u00f7")
        buf.write("\n\7\3\b\3\b\5\b\u00fb\n\b\3\b\3\b\3\b\3\b\3\b\3\b\3\b")
        buf.write("\3\b\3\b\5\b\u0106\n\b\3\b\3\b\3\b\3\b\5\b\u010c\n\b\5")
        buf.write("\b\u010e\n\b\3\b\3\b\3\t\3\t\3\t\3\t\5\t\u0116\n\t\3\n")
        buf.write("\3\n\3\n\3\n\3\13\3\13\3\13\3\13\3\13\3\13\3\f\3\f\3\f")
        buf.write("\3\f\3\f\3\f\3\f\3\r\3\r\5\r\u012b\n\r\3\16\3\16\3\16")
        buf.write("\3\16\7\16\u0131\n\16\f\16\16\16\u0134\13\16\3\17\3\17")
        buf.write("\3\17\3\17\3\17\3\20\3\20\3\20\3\20\3\20\3\20\3\20\3\20")
        buf.write("\3\20\3\20\3\20\3\20\3\21\3\21\3\21\3\21\3\21\3\21\3\21")
        buf.write("\3\21\3\21\3\21\3\21\5\21\u0152\n\21\3\21\3\21\3\22\3")
        buf.write("\22\3\22\3\22\3\22\3\22\5\22\u015c\n\22\3\23\3\23\3\23")
        buf.write("\3\23\5\23\u0162\n\23\3\24\3\24\3\24\3\24\5\24\u0168\n")
        buf.write("\24\3\25\3\25\7\25\u016c\n\25\f\25\16\25\u016f\13\25\3")
        buf.write("\25\3\25\3\25\3\26\6\26\u0175\n\26\r\26\16\26\u0176\3")
        buf.write("\26\3\26\3\26\7\26\u017c\n\26\f\26\16\26\u017f\13\26\3")
        buf.write("\26\7\26\u0182\n\26\f\26\16\26\u0185\13\26\3\26\3\26\6")
        buf.write("\26\u0189\n\26\r\26\16\26\u018a\3\26\5\26\u018e\n\26\3")
        buf.write("\26\6\26\u0191\n\26\r\26\16\26\u0192\3\26\3\26\5\26\u0197")
        buf.write("\n\26\3\27\3\27\3\27\3\27\5\27\u019d\n\27\3\27\6\27\u01a0")
        buf.write("\n\27\r\27\16\27\u01a1\3\30\3\30\6\30\u01a6\n\30\r\30")
        buf.write("\16\30\u01a7\3\31\3\31\3\31\3\31\5\31\u01ae\n\31\3\31")
        buf.write("\6\31\u01b1\n\31\r\31\16\31\u01b2\3\32\3\32\3\32\7\32")
        buf.write("\u01b8\n\32\f\32\16\32\u01bb\13\32\5\32\u01bd\n\32\3\33")
        buf.write("\3\33\3\33\3\33\3\33\3\33\3\33\3\33\3\33\3\33\3\33\3\33")
        buf.write("\3\33\3\33\3\33\3\33\3\33\5\33\u01d0\n\33\3\34\3\34\3")
        buf.write("\34\3\34\3\34\3\34\3\34\3\34\3\34\5\34\u01db\n\34\3\35")
        buf.write("\3\35\3\35\3\35\3\35\3\35\3\35\5\35\u01e4\n\35\3\36\3")
        buf.write("\36\3\36\3\36\3\36\3\36\3\36\5\36\u01ed\n\36\3\37\3\37")
        buf.write("\3\37\3\37\3\37\3\37\3\37\3\37\3\37\3\37\5\37\u01f9\n")
        buf.write("\37\3 \3 \3 \3 \5 \u01ff\n \3!\3!\3!\3!\3!\3!\3!\5!\u0208")
        buf.write("\n!\3\"\3\"\3\"\3\"\3\"\3\"\5\"\u0210\n\"\3#\3#\3#\3#")
        buf.write("\5#\u0216\n#\3#\3#\5#\u021a\n#\3#\5#\u021d\n#\3$\3$\3")
        buf.write("$\3$\5$\u0223\n$\3$\3$\3$\5$\u0228\n$\3%\3%\3%\3%\5%\u022e")
        buf.write("\n%\3&\3&\3&\3&\3\'\3\'\3\'\3\'\3\'\5\'\u0239\n\'\3(\3")
        buf.write("(\7(\u023d\n(\f(\16(\u0240\13(\3(\3(\3(\5(\u0245\n(\3")
        buf.write(")\3)\3)\3)\3*\3*\3*\3*\3+\3+\3+\3+\3+\3+\3,\3,\3-\3-\3")
        buf.write(".\3.\3/\3/\3\60\3\60\3\61\3\61\3\62\3\62\3\63\3\63\3\64")
        buf.write("\3\64\3\65\3\65\3\66\3\66\3\66\3\67\3\67\38\38\58\u0270")
        buf.write("\n8\38\68\u0273\n8\r8\168\u0274\39\39\3:\3:\3;\3;\3;\3")
        buf.write(";\3;\3;\3<\3<\3<\3<\3<\3<\3<\3<\3=\3=\3=\3=\3=\3=\3=\3")
        buf.write("=\3>\3>\3>\3>\3>\3?\3?\3?\3?\3?\3?\3?\3?\3?\3@\3@\3@\3")
        buf.write("@\3@\3A\3A\3A\3A\3A\3A\3B\3B\3B\3C\3C\3C\3C\3C\3C\3C\3")
        buf.write("D\3D\3D\3D\3D\3D\3D\3D\3D\3D\3E\3E\3E\3E\3E\3F\3F\3F\3")
        buf.write("F\3F\3G\3G\3G\3G\3G\3G\3G\3H\3H\3H\3H\3I\3I\3J\3J\3J\3")
        buf.write("K\3K\3L\3L\3M\3M\3N\3N\3O\3O\3P\3P\3P\3Q\3Q\3Q\3R\3R\3")
        buf.write("R\3R\3S\3S\3S\3T\3T\3T\3U\3U\3V\3V\3V\3W\3W\3X\3X\3X\3")
        buf.write("Y\3Y\3Z\6Z\u02ff\nZ\rZ\16Z\u0300\3Z\3Z\3[\3[\3[\3[\7[")
        buf.write("\u0309\n[\f[\16[\u030c\13[\3[\3[\3[\3[\3[\3\\\3\\\5\\")
        buf.write("\u0315\n\\\3]\3]\3]\3^\3^\3^\5^\u031d\n^\3_\3_\7_\u0321")
        buf.write("\n_\f_\16_\u0324\13_\3_\5_\u0327\n_\3_\3_\3`\3`\7`\u032d")
        buf.write("\n`\f`\16`\u0330\13`\3`\3`\3`\3a\3a\3a\3b\3b\3b\3b\7b")
        buf.write("\u033c\nb\fb\16b\u033f\13b\3b\3b\4\u030a\u033d\2c\3\3")
        buf.write("\5\4\7\5\t\6\13\7\r\b\17\t\21\n\23\13\25\f\27\r\31\16")
        buf.write("\33\17\35\20\37\21!\22#\23%\24\'\25)\26+\27-\30/\31\61")
        buf.write("\32\63\33\65\34\67\359\36;\37= ?!A\"C#E$G%I&K\'M(O)Q*")
        buf.write("S+U,W-Y.[/]\60_\61a\62c\63e\64g\65i\66k\67m\2o\2q\2s\2")
        buf.write("u8w9y:{;}<\177=\u0081>\u0083?\u0085@\u0087A\u0089B\u008b")
        buf.write("C\u008dD\u008fE\u0091F\u0093G\u0095H\u0097I\u0099J\u009b")
        buf.write("K\u009dL\u009fM\u00a1N\u00a3O\u00a5P\u00a7Q\u00a9R\u00ab")
        buf.write("S\u00adT\u00afU\u00b1V\u00b3W\u00b5X\u00b7\2\u00b9\2\u00bb")
        buf.write("\2\u00bdY\u00bfZ\u00c1[\u00c3\\\3\2\20\5\2\62;CHch\3\2")
        buf.write("\62;\3\2\62\63\3\2\63;\4\2\62;aa\5\2C\\aac|\6\2\62;C\\")
        buf.write("aac|\4\2GGgg\4\2--//\5\2\13\f\17\17\"\"\7\2\n\f\16\17")
        buf.write("$$))^^\n\2$$))^^ddhhppttvv\3\2^^\7\3\n\f\16\17$$))^^\2")
        buf.write("\u0389\2\3\3\2\2\2\2\5\3\2\2\2\2\7\3\2\2\2\2\t\3\2\2\2")
        buf.write("\2\13\3\2\2\2\2\r\3\2\2\2\2\17\3\2\2\2\2\21\3\2\2\2\2")
        buf.write("\23\3\2\2\2\2\25\3\2\2\2\2\27\3\2\2\2\2\31\3\2\2\2\2\33")
        buf.write("\3\2\2\2\2\35\3\2\2\2\2\37\3\2\2\2\2!\3\2\2\2\2#\3\2\2")
        buf.write("\2\2%\3\2\2\2\2\'\3\2\2\2\2)\3\2\2\2\2+\3\2\2\2\2-\3\2")
        buf.write("\2\2\2/\3\2\2\2\2\61\3\2\2\2\2\63\3\2\2\2\2\65\3\2\2\2")
        buf.write("\2\67\3\2\2\2\29\3\2\2\2\2;\3\2\2\2\2=\3\2\2\2\2?\3\2")
        buf.write("\2\2\2A\3\2\2\2\2C\3\2\2\2\2E\3\2\2\2\2G\3\2\2\2\2I\3")
        buf.write("\2\2\2\2K\3\2\2\2\2M\3\2\2\2\2O\3\2\2\2\2Q\3\2\2\2\2S")
        buf.write("\3\2\2\2\2U\3\2\2\2\2W\3\2\2\2\2Y\3\2\2\2\2[\3\2\2\2\2")
        buf.write("]\3\2\2\2\2_\3\2\2\2\2a\3\2\2\2\2c\3\2\2\2\2e\3\2\2\2")
        buf.write("\2g\3\2\2\2\2i\3\2\2\2\2k\3\2\2\2\2u\3\2\2\2\2w\3\2\2")
        buf.write("\2\2y\3\2\2\2\2{\3\2\2\2\2}\3\2\2\2\2\177\3\2\2\2\2\u0081")
        buf.write("\3\2\2\2\2\u0083\3\2\2\2\2\u0085\3\2\2\2\2\u0087\3\2\2")
        buf.write("\2\2\u0089\3\2\2\2\2\u008b\3\2\2\2\2\u008d\3\2\2\2\2\u008f")
        buf.write("\3\2\2\2\2\u0091\3\2\2\2\2\u0093\3\2\2\2\2\u0095\3\2\2")
        buf.write("\2\2\u0097\3\2\2\2\2\u0099\3\2\2\2\2\u009b\3\2\2\2\2\u009d")
        buf.write("\3\2\2\2\2\u009f\3\2\2\2\2\u00a1\3\2\2\2\2\u00a3\3\2\2")
        buf.write("\2\2\u00a5\3\2\2\2\2\u00a7\3\2\2\2\2\u00a9\3\2\2\2\2\u00ab")
        buf.write("\3\2\2\2\2\u00ad\3\2\2\2\2\u00af\3\2\2\2\2\u00b1\3\2\2")
        buf.write("\2\2\u00b3\3\2\2\2\2\u00b5\3\2\2\2\2\u00bd\3\2\2\2\2\u00bf")
        buf.write("\3\2\2\2\2\u00c1\3\2\2\2\2\u00c3\3\2\2\2\3\u00c5\3\2\2")
        buf.write("\2\5\u00ca\3\2\2\2\7\u00dc\3\2\2\2\t\u00de\3\2\2\2\13")
        buf.write("\u00e3\3\2\2\2\r\u00f6\3\2\2\2\17\u00fa\3\2\2\2\21\u0115")
        buf.write("\3\2\2\2\23\u0117\3\2\2\2\25\u011b\3\2\2\2\27\u0121\3")
        buf.write("\2\2\2\31\u012a\3\2\2\2\33\u012c\3\2\2\2\35\u0135\3\2")
        buf.write("\2\2\37\u013a\3\2\2\2!\u0146\3\2\2\2#\u015b\3\2\2\2%\u0161")
        buf.write("\3\2\2\2\'\u0167\3\2\2\2)\u0169\3\2\2\2+\u0196\3\2\2\2")
        buf.write("-\u019c\3\2\2\2/\u01a3\3\2\2\2\61\u01ad\3\2\2\2\63\u01bc")
        buf.write("\3\2\2\2\65\u01cf\3\2\2\2\67\u01da\3\2\2\29\u01e3\3\2")
        buf.write("\2\2;\u01ec\3\2\2\2=\u01f8\3\2\2\2?\u01fe\3\2\2\2A\u0207")
        buf.write("\3\2\2\2C\u020f\3\2\2\2E\u021c\3\2\2\2G\u0227\3\2\2\2")
        buf.write("I\u022d\3\2\2\2K\u022f\3\2\2\2M\u0238\3\2\2\2O\u0244\3")
        buf.write("\2\2\2Q\u0246\3\2\2\2S\u024a\3\2\2\2U\u024e\3\2\2\2W\u0254")
        buf.write("\3\2\2\2Y\u0256\3\2\2\2[\u0258\3\2\2\2]\u025a\3\2\2\2")
        buf.write("_\u025c\3\2\2\2a\u025e\3\2\2\2c\u0260\3\2\2\2e\u0262\3")
        buf.write("\2\2\2g\u0264\3\2\2\2i\u0266\3\2\2\2k\u0268\3\2\2\2m\u026b")
        buf.write("\3\2\2\2o\u026d\3\2\2\2q\u0276\3\2\2\2s\u0278\3\2\2\2")
        buf.write("u\u027a\3\2\2\2w\u0280\3\2\2\2y\u0288\3\2\2\2{\u0290\3")
        buf.write("\2\2\2}\u0295\3\2\2\2\177\u029e\3\2\2\2\u0081\u02a3\3")
        buf.write("\2\2\2\u0083\u02a9\3\2\2\2\u0085\u02ac\3\2\2\2\u0087\u02b3")
        buf.write("\3\2\2\2\u0089\u02bd\3\2\2\2\u008b\u02c2\3\2\2\2\u008d")
        buf.write("\u02c7\3\2\2\2\u008f\u02ce\3\2\2\2\u0091\u02d2\3\2\2\2")
        buf.write("\u0093\u02d4\3\2\2\2\u0095\u02d7\3\2\2\2\u0097\u02d9\3")
        buf.write("\2\2\2\u0099\u02db\3\2\2\2\u009b\u02dd\3\2\2\2\u009d\u02df")
        buf.write("\3\2\2\2\u009f\u02e1\3\2\2\2\u00a1\u02e4\3\2\2\2\u00a3")
        buf.write("\u02e7\3\2\2\2\u00a5\u02eb\3\2\2\2\u00a7\u02ee\3\2\2\2")
        buf.write("\u00a9\u02f1\3\2\2\2\u00ab\u02f3\3\2\2\2\u00ad\u02f6\3")
        buf.write("\2\2\2\u00af\u02f8\3\2\2\2\u00b1\u02fb\3\2\2\2\u00b3\u02fe")
        buf.write("\3\2\2\2\u00b5\u0304\3\2\2\2\u00b7\u0314\3\2\2\2\u00b9")
        buf.write("\u0316\3\2\2\2\u00bb\u031c\3\2\2\2\u00bd\u031e\3\2\2\2")
        buf.write("\u00bf\u032a\3\2\2\2\u00c1\u0334\3\2\2\2\u00c3\u0337\3")
        buf.write("\2\2\2\u00c5\u00c6\7o\2\2\u00c6\u00c7\7c\2\2\u00c7\u00c8")
        buf.write("\7k\2\2\u00c8\u00c9\7p\2\2\u00c9\4\3\2\2\2\u00ca\u00cb")
        buf.write("\5U+\2\u00cb\u00cf\5O(\2\u00cc\u00cd\5i\65\2\u00cd\u00ce")
        buf.write("\5O(\2\u00ce\u00d0\3\2\2\2\u00cf\u00cc\3\2\2\2\u00cf\u00d0")
        buf.write("\3\2\2\2\u00d0\u00d1\3\2\2\2\u00d1\u00d5\5]/\2\u00d2\u00d4")
        buf.write("\5\7\4\2\u00d3\u00d2\3\2\2\2\u00d4\u00d7\3\2\2\2\u00d5")
        buf.write("\u00d3\3\2\2\2\u00d5\u00d6\3\2\2\2\u00d6\u00d8\3\2\2\2")
        buf.write("\u00d7\u00d5\3\2\2\2\u00d8\u00d9\5_\60\2\u00d9\6\3\2\2")
        buf.write("\2\u00da\u00dd\5\17\b\2\u00db\u00dd\5\t\5\2\u00dc\u00da")
        buf.write("\3\2\2\2\u00dc\u00db\3\2\2\2\u00dd\b\3\2\2\2\u00de\u00df")
        buf.write("\5O(\2\u00df\u00e0\5Y-\2\u00e0\u00e1\5\13\6\2\u00e1\u00e2")
        buf.write("\5[.\2\u00e2\n\3\2\2\2\u00e3\u00e9\5\r\7\2\u00e4\u00e5")
        buf.write("\5e\63\2\u00e5\u00e6\5\r\7\2\u00e6\u00e8\3\2\2\2\u00e7")
        buf.write("\u00e4\3\2\2\2\u00e8\u00eb\3\2\2\2\u00e9\u00e7\3\2\2\2")
        buf.write("\u00e9\u00ea\3\2\2\2\u00ea\f\3\2\2\2\u00eb\u00e9\3\2\2")
        buf.write("\2\u00ec\u00ed\5O(\2\u00ed\u00ee\5i\65\2\u00ee\u00ef\5")
        buf.write("#\22\2\u00ef\u00f7\3\2\2\2\u00f0\u00f1\5O(\2\u00f1\u00f2")
        buf.write("\5i\65\2\u00f2\u00f3\5#\22\2\u00f3\u00f4\5g\64\2\u00f4")
        buf.write("\u00f5\5\r\7\2\u00f5\u00f7\3\2\2\2\u00f6\u00ec\3\2\2\2")
        buf.write("\u00f6\u00f0\3\2\2\2\u00f7\16\3\2\2\2\u00f8\u00fb\5S*")
        buf.write("\2\u00f9\u00fb\5Q)\2\u00fa\u00f8\3\2\2\2\u00fa\u00f9\3")
        buf.write("\2\2\2\u00fb\u00fc\3\2\2\2\u00fc\u00fd\5\33\16\2\u00fd")
        buf.write("\u00fe\5i\65\2\u00fe\u010d\5#\22\2\u00ff\u0100\5\u00b1")
        buf.write("Y\2\u0100\u0101\5#\22\2\u0101\u0106\3\2\2\2\u0102\u0103")
        buf.write("\5g\64\2\u0103\u0104\5#\22\2\u0104\u0106\3\2\2\2\u0105")
        buf.write("\u00ff\3\2\2\2\u0105\u0102\3\2\2\2\u0106\u010e\3\2\2\2")
        buf.write("\u0107\u010c\5\21\t\2\u0108\u0109\5g\64\2\u0109\u010a")
        buf.write("\5\21\t\2\u010a\u010c\3\2\2\2\u010b\u0107\3\2\2\2\u010b")
        buf.write("\u0108\3\2\2\2\u010c\u010e\3\2\2\2\u010d\u0105\3\2\2\2")
        buf.write("\u010d\u010b\3\2\2\2\u010d\u010e\3\2\2\2\u010e\u010f\3")
        buf.write("\2\2\2\u010f\u0110\5e\63\2\u0110\20\3\2\2\2\u0111\u0112")
        buf.write("\5\u00b1Y\2\u0112\u0113\5\65\33\2\u0113\u0116\3\2\2\2")
        buf.write("\u0114\u0116\5!\21\2\u0115\u0111\3\2\2\2\u0115\u0114\3")
        buf.write("\2\2\2\u0116\22\3\2\2\2\u0117\u0118\7K\2\2\u0118\u0119")
        buf.write("\7p\2\2\u0119\u011a\7v\2\2\u011a\24\3\2\2\2\u011b\u011c")
        buf.write("\7H\2\2\u011c\u011d\7n\2\2\u011d\u011e\7q\2\2\u011e\u011f")
        buf.write("\7c\2\2\u011f\u0120\7v\2\2\u0120\26\3\2\2\2\u0121\u0122")
        buf.write("\7u\2\2\u0122\u0123\7v\2\2\u0123\u0124\7t\2\2\u0124\u0125")
        buf.write("\7k\2\2\u0125\u0126\7p\2\2\u0126\u0127\7i\2\2\u0127\30")
        buf.write("\3\2\2\2\u0128\u012b\5\177@\2\u0129\u012b\5\u0081A\2\u012a")
        buf.write("\u0128\3\2\2\2\u012a\u0129\3\2\2\2\u012b\32\3\2\2\2\u012c")
        buf.write("\u0132\5O(\2\u012d\u012e\5g\64\2\u012e\u012f\5O(\2\u012f")
        buf.write("\u0131\3\2\2\2\u0130\u012d\3\2\2\2\u0131\u0134\3\2\2\2")
        buf.write("\u0132\u0130\3\2\2\2\u0132\u0133\3\2\2\2\u0133\34\3\2")
        buf.write("\2\2\u0134\u0132\3\2\2\2\u0135\u0136\7X\2\2\u0136\u0137")
        buf.write("\7q\2\2\u0137\u0138\7k\2\2\u0138\u0139\7f\2\2\u0139\36")
        buf.write("\3\2\2\2\u013a\u013b\7C\2\2\u013b\u013c\7t\2\2\u013c\u013d")
        buf.write("\7t\2\2\u013d\u013e\7c\2\2\u013e\u013f\7{\2\2\u013f\u0140")
        buf.write("\3\2\2\2\u0140\u0141\5a\61\2\u0141\u0142\5#\22\2\u0142")
        buf.write("\u0143\5g\64\2\u0143\u0144\5\'\24\2\u0144\u0145\5c\62")
        buf.write("\2\u0145 \3\2\2\2\u0146\u0147\7C\2\2\u0147\u0148\7t\2")
        buf.write("\2\u0148\u0149\7t\2\2\u0149\u014a\7c\2\2\u014a\u014b\7")
        buf.write("{\2\2\u014b\u014c\3\2\2\2\u014c\u014d\5Y-\2\u014d\u0151")
        buf.write("\5%\23\2\u014e\u014f\5g\64\2\u014f\u0150\5%\23\2\u0150")
        buf.write("\u0152\3\2\2\2\u0151\u014e\3\2\2\2\u0151\u0152\3\2\2\2")
        buf.write("\u0152\u0153\3\2\2\2\u0153\u0154\5[.\2\u0154\"\3\2\2\2")
        buf.write("\u0155\u015c\5\31\r\2\u0156\u015c\5\23\n\2\u0157\u015c")
        buf.write("\5\25\13\2\u0158\u015c\5\27\f\2\u0159\u015c\5\37\20\2")
        buf.write("\u015a\u015c\5U+\2\u015b\u0155\3\2\2\2\u015b\u0156\3\2")
        buf.write("\2\2\u015b\u0157\3\2\2\2\u015b\u0158\3\2\2\2\u015b\u0159")
        buf.write("\3\2\2\2\u015b\u015a\3\2\2\2\u015c$\3\2\2\2\u015d\u0162")
        buf.write("\5\'\24\2\u015e\u0162\5\31\r\2\u015f\u0162\5+\26\2\u0160")
        buf.write("\u0162\5)\25\2\u0161\u015d\3\2\2\2\u0161\u015e\3\2\2\2")
        buf.write("\u0161\u015f\3\2\2\2\u0161\u0160\3\2\2\2\u0162&\3\2\2")
        buf.write("\2\u0163\u0168\5-\27\2\u0164\u0168\5/\30\2\u0165\u0168")
        buf.write("\5\61\31\2\u0166\u0168\5\63\32\2\u0167\u0163\3\2\2\2\u0167")
        buf.write("\u0164\3\2\2\2\u0167\u0165\3\2\2\2\u0167\u0166\3\2\2\2")
        buf.write("\u0168(\3\2\2\2\u0169\u016d\7$\2\2\u016a\u016c\5\u00b7")
        buf.write("\\\2\u016b\u016a\3\2\2\2\u016c\u016f\3\2\2\2\u016d\u016b")
        buf.write("\3\2\2\2\u016d\u016e\3\2\2\2\u016e\u0170\3\2\2\2\u016f")
        buf.write("\u016d\3\2\2\2\u0170\u0171\7$\2\2\u0171\u0172\b\25\2\2")
        buf.write("\u0172*\3\2\2\2\u0173\u0175\5q9\2\u0174\u0173\3\2\2\2")
        buf.write("\u0175\u0176\3\2\2\2\u0176\u0174\3\2\2\2\u0176\u0177\3")
        buf.write("\2\2\2\u0177\u0178\3\2\2\2\u0178\u017d\5m\67\2\u0179\u017c")
        buf.write("\5q9\2\u017a\u017c\5o8\2\u017b\u0179\3\2\2\2\u017b\u017a")
        buf.write("\3\2\2\2\u017c\u017f\3\2\2\2\u017d\u017b\3\2\2\2\u017d")
        buf.write("\u017e\3\2\2\2\u017e\u0197\3\2\2\2\u017f\u017d\3\2\2\2")
        buf.write("\u0180\u0182\5q9\2\u0181\u0180\3\2\2\2\u0182\u0185\3\2")
        buf.write("\2\2\u0183\u0181\3\2\2\2\u0183\u0184\3\2\2\2\u0184\u0186")
        buf.write("\3\2\2\2\u0185\u0183\3\2\2\2\u0186\u0188\5m\67\2\u0187")
        buf.write("\u0189\5q9\2\u0188\u0187\3\2\2\2\u0189\u018a\3\2\2\2\u018a")
        buf.write("\u0188\3\2\2\2\u018a\u018b\3\2\2\2\u018b\u018d\3\2\2\2")
        buf.write("\u018c\u018e\5o8\2\u018d\u018c\3\2\2\2\u018d\u018e\3\2")
        buf.write("\2\2\u018e\u0197\3\2\2\2\u018f\u0191\5q9\2\u0190\u018f")
        buf.write("\3\2\2\2\u0191\u0192\3\2\2\2\u0192\u0190\3\2\2\2\u0192")
        buf.write("\u0193\3\2\2\2\u0193\u0194\3\2\2\2\u0194\u0195\5o8\2\u0195")
        buf.write("\u0197\3\2\2\2\u0196\u0174\3\2\2\2\u0196\u0183\3\2\2\2")
        buf.write("\u0196\u0190\3\2\2\2\u0197,\3\2\2\2\u0198\u0199\7\62\2")
        buf.write("\2\u0199\u019d\7z\2\2\u019a\u019b\7\62\2\2\u019b\u019d")
        buf.write("\7Z\2\2\u019c\u0198\3\2\2\2\u019c\u019a\3\2\2\2\u019d")
        buf.write("\u019f\3\2\2\2\u019e\u01a0\t\2\2\2\u019f\u019e\3\2\2\2")
        buf.write("\u01a0\u01a1\3\2\2\2\u01a1\u019f\3\2\2\2\u01a1\u01a2\3")
        buf.write("\2\2\2\u01a2.\3\2\2\2\u01a3\u01a5\7\62\2\2\u01a4\u01a6")
        buf.write("\t\3\2\2\u01a5\u01a4\3\2\2\2\u01a6\u01a7\3\2\2\2\u01a7")
        buf.write("\u01a5\3\2\2\2\u01a7\u01a8\3\2\2\2\u01a8\60\3\2\2\2\u01a9")
        buf.write("\u01aa\7\62\2\2\u01aa\u01ae\7d\2\2\u01ab\u01ac\7\62\2")
        buf.write("\2\u01ac\u01ae\7D\2\2\u01ad\u01a9\3\2\2\2\u01ad\u01ab")
        buf.write("\3\2\2\2\u01ae\u01b0\3\2\2\2\u01af\u01b1\t\4\2\2\u01b0")
        buf.write("\u01af\3\2\2\2\u01b1\u01b2\3\2\2\2\u01b2\u01b0\3\2\2\2")
        buf.write("\u01b2\u01b3\3\2\2\2\u01b3\62\3\2\2\2\u01b4\u01bd\t\3")
        buf.write("\2\2\u01b5\u01b9\t\5\2\2\u01b6\u01b8\t\6\2\2\u01b7\u01b6")
        buf.write("\3\2\2\2\u01b8\u01bb\3\2\2\2\u01b9\u01b7\3\2\2\2\u01b9")
        buf.write("\u01ba\3\2\2\2\u01ba\u01bd\3\2\2\2\u01bb\u01b9\3\2\2\2")
        buf.write("\u01bc\u01b4\3\2\2\2\u01bc\u01b5\3\2\2\2\u01bd\64\3\2")
        buf.write("\2\2\u01be\u01bf\5\67\34\2\u01bf\u01c0\5\u00adW\2\u01c0")
        buf.write("\u01c1\5\67\34\2\u01c1\u01d0\3\2\2\2\u01c2\u01c3\5\67")
        buf.write("\34\2\u01c3\u01c4\5\u00abV\2\u01c4\u01c5\5\67\34\2\u01c5")
        buf.write("\u01d0\3\2\2\2\u01c6\u01c7\5\67\34\2\u01c7\u01c8\5\u00a9")
        buf.write("U\2\u01c8\u01c9\5\67\34\2\u01c9\u01d0\3\2\2\2\u01ca\u01cb")
        buf.write("\5\67\34\2\u01cb\u01cc\5\u00afX\2\u01cc\u01cd\5\67\34")
        buf.write("\2\u01cd\u01d0\3\2\2\2\u01ce\u01d0\5\67\34\2\u01cf\u01be")
        buf.write("\3\2\2\2\u01cf\u01c2\3\2\2\2\u01cf\u01c6\3\2\2\2\u01cf")
        buf.write("\u01ca\3\2\2\2\u01cf\u01ce\3\2\2\2\u01d0\66\3\2\2\2\u01d1")
        buf.write("\u01d2\59\35\2\u01d2\u01d3\5\u00a1Q\2\u01d3\u01d4\59\35")
        buf.write("\2\u01d4\u01db\3\2\2\2\u01d5\u01d6\59\35\2\u01d6\u01d7")
        buf.write("\5\u009fP\2\u01d7\u01d8\59\35\2\u01d8\u01db\3\2\2\2\u01d9")
        buf.write("\u01db\59\35\2\u01da\u01d1\3\2\2\2\u01da\u01d5\3\2\2\2")
        buf.write("\u01da\u01d9\3\2\2\2\u01db8\3\2\2\2\u01dc\u01e4\5;\36")
        buf.write("\2\u01dd\u01de\5\u00a5S\2\u01de\u01df\5;\36\2\u01df\u01e4")
        buf.write("\3\2\2\2\u01e0\u01e1\5\u00a7T\2\u01e1\u01e2\5;\36\2\u01e2")
        buf.write("\u01e4\3\2\2\2\u01e3\u01dc\3\2\2\2\u01e3\u01dd\3\2\2\2")
        buf.write("\u01e3\u01e0\3\2\2\2\u01e4:\3\2\2\2\u01e5\u01e6\5\u0091")
        buf.write("I\2\u01e6\u01e7\5=\37\2\u01e7\u01ed\3\2\2\2\u01e8\u01e9")
        buf.write("\5\u0095K\2\u01e9\u01ea\5=\37\2\u01ea\u01ed\3\2\2\2\u01eb")
        buf.write("\u01ed\5=\37\2\u01ec\u01e5\3\2\2\2\u01ec\u01e8\3\2\2\2")
        buf.write("\u01ec\u01eb\3\2\2\2\u01ed<\3\2\2\2\u01ee\u01ef\5\u0097")
        buf.write("L\2\u01ef\u01f0\5? \2\u01f0\u01f9\3\2\2\2\u01f1\u01f2")
        buf.write("\5\u0099M\2\u01f2\u01f3\5? \2\u01f3\u01f9\3\2\2\2\u01f4")
        buf.write("\u01f5\5\u009bN\2\u01f5\u01f6\5? \2\u01f6\u01f9\3\2\2")
        buf.write("\2\u01f7\u01f9\5? \2\u01f8\u01ee\3\2\2\2\u01f8\u01f1\3")
        buf.write("\2\2\2\u01f8\u01f4\3\2\2\2\u01f8\u01f7\3\2\2\2\u01f9>")
        buf.write("\3\2\2\2\u01fa\u01fb\5\u009dO\2\u01fb\u01fc\5? \2\u01fc")
        buf.write("\u01ff\3\2\2\2\u01fd\u01ff\5A!\2\u01fe\u01fa\3\2\2\2\u01fe")
        buf.write("\u01fd\3\2\2\2\u01ff@\3\2\2\2\u0200\u0201\5\u0091I\2\u0201")
        buf.write("\u0202\5A!\2\u0202\u0208\3\2\2\2\u0203\u0204\5\u0095K")
        buf.write("\2\u0204\u0205\5A!\2\u0205\u0208\3\2\2\2\u0206\u0208\5")
        buf.write("C\"\2\u0207\u0200\3\2\2\2\u0207\u0203\3\2\2\2\u0207\u0206")
        buf.write("\3\2\2\2\u0208B\3\2\2\2\u0209\u020a\5E#\2\u020a\u020b")
        buf.write("\5a\61\2\u020b\u020c\5\65\33\2\u020c\u020d\5c\62\2\u020d")
        buf.write("\u0210\3\2\2\2\u020e\u0210\5E#\2\u020f\u0209\3\2\2\2\u020f")
        buf.write("\u020e\3\2\2\2\u0210D\3\2\2\2\u0211\u0212\5m\67\2\u0212")
        buf.write("\u0219\5O(\2\u0213\u0215\5Y-\2\u0214\u0216\5M\'\2\u0215")
        buf.write("\u0214\3\2\2\2\u0215\u0216\3\2\2\2\u0216\u0217\3\2\2\2")
        buf.write("\u0217\u0218\5[.\2\u0218\u021a\3\2\2\2\u0219\u0213\3\2")
        buf.write("\2\2\u0219\u021a\3\2\2\2\u021a\u021d\3\2\2\2\u021b\u021d")
        buf.write("\5G$\2\u021c\u0211\3\2\2\2\u021c\u021b\3\2\2\2\u021dF")
        buf.write("\3\2\2\2\u021e\u021f\5\u008fH\2\u021f\u0220\5G$\2\u0220")
        buf.write("\u0222\5Y-\2\u0221\u0223\5M\'\2\u0222\u0221\3\2\2\2\u0222")
        buf.write("\u0223\3\2\2\2\u0223\u0224\3\2\2\2\u0224\u0225\5[.\2\u0225")
        buf.write("\u0228\3\2\2\2\u0226\u0228\5I%\2\u0227\u021e\3\2\2\2\u0227")
        buf.write("\u0226\3\2\2\2\u0228H\3\2\2\2\u0229\u022e\5%\23\2\u022a")
        buf.write("\u022e\5O(\2\u022b\u022e\5\u008bF\2\u022c\u022e\5K&\2")
        buf.write("\u022d\u0229\3\2\2\2\u022d\u022a\3\2\2\2\u022d\u022b\3")
        buf.write("\2\2\2\u022d\u022c\3\2\2\2\u022eJ\3\2\2\2\u022f\u0230")
        buf.write("\5Y-\2\u0230\u0231\5\65\33\2\u0231\u0232\5[.\2\u0232L")
        buf.write("\3\2\2\2\u0233\u0239\5\65\33\2\u0234\u0235\5\65\33\2\u0235")
        buf.write("\u0236\5g\64\2\u0236\u0237\5M\'\2\u0237\u0239\3\2\2\2")
        buf.write("\u0238\u0233\3\2\2\2\u0238\u0234\3\2\2\2\u0239N\3\2\2")
        buf.write("\2\u023a\u023e\t\7\2\2\u023b\u023d\t\b\2\2\u023c\u023b")
        buf.write("\3\2\2\2\u023d\u0240\3\2\2\2\u023e\u023c\3\2\2\2\u023e")
        buf.write("\u023f\3\2\2\2\u023f\u0245\3\2\2\2\u0240\u023e\3\2\2\2")
        buf.write("\u0241\u0242\5W,\2\u0242\u0243\5O(\2\u0243\u0245\3\2\2")
        buf.write("\2\u0244\u023a\3\2\2\2\u0244\u0241\3\2\2\2\u0245P\3\2")
        buf.write("\2\2\u0246\u0247\7x\2\2\u0247\u0248\7c\2\2\u0248\u0249")
        buf.write("\7n\2\2\u0249R\3\2\2\2\u024a\u024b\7x\2\2\u024b\u024c")
        buf.write("\7c\2\2\u024c\u024d\7t\2\2\u024dT\3\2\2\2\u024e\u024f")
        buf.write("\7e\2\2\u024f\u0250\7n\2\2\u0250\u0251\7c\2\2\u0251\u0252")
        buf.write("\7u\2\2\u0252\u0253\7u\2\2\u0253V\3\2\2\2\u0254\u0255")
        buf.write("\7&\2\2\u0255X\3\2\2\2\u0256\u0257\7*\2\2\u0257Z\3\2\2")
        buf.write("\2\u0258\u0259\7+\2\2\u0259\\\3\2\2\2\u025a\u025b\7}\2")
        buf.write("\2\u025b^\3\2\2\2\u025c\u025d\7\177\2\2\u025d`\3\2\2\2")
        buf.write("\u025e\u025f\7]\2\2\u025fb\3\2\2\2\u0260\u0261\7_\2\2")
        buf.write("\u0261d\3\2\2\2\u0262\u0263\7=\2\2\u0263f\3\2\2\2\u0264")
        buf.write("\u0265\7.\2\2\u0265h\3\2\2\2\u0266\u0267\7<\2\2\u0267")
        buf.write("j\3\2\2\2\u0268\u0269\7\60\2\2\u0269\u026a\7\60\2\2\u026a")
        buf.write("l\3\2\2\2\u026b\u026c\7\60\2\2\u026cn\3\2\2\2\u026d\u026f")
        buf.write("\t\t\2\2\u026e\u0270\5\u0095K\2\u026f\u026e\3\2\2\2\u026f")
        buf.write("\u0270\3\2\2\2\u0270\u0272\3\2\2\2\u0271\u0273\5q9\2\u0272")
        buf.write("\u0271\3\2\2\2\u0273\u0274\3\2\2\2\u0274\u0272\3\2\2\2")
        buf.write("\u0274\u0275\3\2\2\2\u0275p\3\2\2\2\u0276\u0277\t\3\2")
        buf.write("\2\u0277r\3\2\2\2\u0278\u0279\t\n\2\2\u0279t\3\2\2\2\u027a")
        buf.write("\u027b\7D\2\2\u027b\u027c\7t\2\2\u027c\u027d\7g\2\2\u027d")
        buf.write("\u027e\7c\2\2\u027e\u027f\7m\2\2\u027fv\3\2\2\2\u0280")
        buf.write("\u0281\7H\2\2\u0281\u0282\7q\2\2\u0282\u0283\7t\2\2\u0283")
        buf.write("\u0284\7g\2\2\u0284\u0285\7c\2\2\u0285\u0286\7e\2\2\u0286")
        buf.write("\u0287\7j\2\2\u0287x\3\2\2\2\u0288\u0289\7D\2\2\u0289")
        buf.write("\u028a\7q\2\2\u028a\u028b\7q\2\2\u028b\u028c\7n\2\2\u028c")
        buf.write("\u028d\7g\2\2\u028d\u028e\7c\2\2\u028e\u028f\7p\2\2\u028f")
        buf.write("z\3\2\2\2\u0290\u0291\7P\2\2\u0291\u0292\7w\2\2\u0292")
        buf.write("\u0293\7n\2\2\u0293\u0294\7n\2\2\u0294|\3\2\2\2\u0295")
        buf.write("\u0296\7E\2\2\u0296\u0297\7q\2\2\u0297\u0298\7p\2\2\u0298")
        buf.write("\u0299\7v\2\2\u0299\u029a\7k\2\2\u029a\u029b\7p\2\2\u029b")
        buf.write("\u029c\7w\2\2\u029c\u029d\7g\2\2\u029d~\3\2\2\2\u029e")
        buf.write("\u029f\7V\2\2\u029f\u02a0\7t\2\2\u02a0\u02a1\7w\2\2\u02a1")
        buf.write("\u02a2\7g\2\2\u02a2\u0080\3\2\2\2\u02a3\u02a4\7H\2\2\u02a4")
        buf.write("\u02a5\7c\2\2\u02a5\u02a6\7n\2\2\u02a6\u02a7\7u\2\2\u02a7")
        buf.write("\u02a8\7g\2\2\u02a8\u0082\3\2\2\2\u02a9\u02aa\7k\2\2\u02aa")
        buf.write("\u02ab\7h\2\2\u02ab\u0084\3\2\2\2\u02ac\u02ad\7g\2\2\u02ad")
        buf.write("\u02ae\7n\2\2\u02ae\u02af\7u\2\2\u02af\u02b0\7g\2\2\u02b0")
        buf.write("\u02b1\7k\2\2\u02b1\u02b2\7h\2\2\u02b2\u0086\3\2\2\2\u02b3")
        buf.write("\u02b4\7C\2\2\u02b4\u02b5\7t\2\2\u02b5\u02b6\7t\2\2\u02b6")
        buf.write("\u02b7\7c\2\2\u02b7\u02b8\7{\2\2\u02b8\u02b9\7\"\2\2\u02b9")
        buf.write("\u02ba\7K\2\2\u02ba\u02bb\7p\2\2\u02bb\u02bc\7v\2\2\u02bc")
        buf.write("\u0088\3\2\2\2\u02bd\u02be\7G\2\2\u02be\u02bf\7n\2\2\u02bf")
        buf.write("\u02c0\7u\2\2\u02c0\u02c1\7g\2\2\u02c1\u008a\3\2\2\2\u02c2")
        buf.write("\u02c3\7u\2\2\u02c3\u02c4\7g\2\2\u02c4\u02c5\7n\2\2\u02c5")
        buf.write("\u02c6\7h\2\2\u02c6\u008c\3\2\2\2\u02c7\u02c8\7t\2\2\u02c8")
        buf.write("\u02c9\7g\2\2\u02c9\u02ca\7v\2\2\u02ca\u02cb\7w\2\2\u02cb")
        buf.write("\u02cc\7t\2\2\u02cc\u02cd\7p\2\2\u02cd\u008e\3\2\2\2\u02ce")
        buf.write("\u02cf\7p\2\2\u02cf\u02d0\7g\2\2\u02d0\u02d1\7y\2\2\u02d1")
        buf.write("\u0090\3\2\2\2\u02d2\u02d3\7-\2\2\u02d3\u0092\3\2\2\2")
        buf.write("\u02d4\u02d5\7-\2\2\u02d5\u02d6\7\60\2\2\u02d6\u0094\3")
        buf.write("\2\2\2\u02d7\u02d8\7/\2\2\u02d8\u0096\3\2\2\2\u02d9\u02da")
        buf.write("\7,\2\2\u02da\u0098\3\2\2\2\u02db\u02dc\7\61\2\2\u02dc")
        buf.write("\u009a\3\2\2\2\u02dd\u02de\7\'\2\2\u02de\u009c\3\2\2\2")
        buf.write("\u02df\u02e0\7#\2\2\u02e0\u009e\3\2\2\2\u02e1\u02e2\7")
        buf.write("#\2\2\u02e2\u02e3\7?\2\2\u02e3\u00a0\3\2\2\2\u02e4\u02e5")
        buf.write("\7?\2\2\u02e5\u02e6\7?\2\2\u02e6\u00a2\3\2\2\2\u02e7\u02e8")
        buf.write("\7?\2\2\u02e8\u02e9\7?\2\2\u02e9\u02ea\7\60\2\2\u02ea")
        buf.write("\u00a4\3\2\2\2\u02eb\u02ec\7(\2\2\u02ec\u02ed\7(\2\2\u02ed")
        buf.write("\u00a6\3\2\2\2\u02ee\u02ef\7~\2\2\u02ef\u02f0\7~\2\2\u02f0")
        buf.write("\u00a8\3\2\2\2\u02f1\u02f2\7@\2\2\u02f2\u00aa\3\2\2\2")
        buf.write("\u02f3\u02f4\7>\2\2\u02f4\u02f5\7?\2\2\u02f5\u00ac\3\2")
        buf.write("\2\2\u02f6\u02f7\7>\2\2\u02f7\u00ae\3\2\2\2\u02f8\u02f9")
        buf.write("\7@\2\2\u02f9\u02fa\7?\2\2\u02fa\u00b0\3\2\2\2\u02fb\u02fc")
        buf.write("\7?\2\2\u02fc\u00b2\3\2\2\2\u02fd\u02ff\t\13\2\2\u02fe")
        buf.write("\u02fd\3\2\2\2\u02ff\u0300\3\2\2\2\u0300\u02fe\3\2\2\2")
        buf.write("\u0300\u0301\3\2\2\2\u0301\u0302\3\2\2\2\u0302\u0303\b")
        buf.write("Z\3\2\u0303\u00b4\3\2\2\2\u0304\u0305\7%\2\2\u0305\u0306")
        buf.write("\7%\2\2\u0306\u030a\3\2\2\2\u0307\u0309\13\2\2\2\u0308")
        buf.write("\u0307\3\2\2\2\u0309\u030c\3\2\2\2\u030a\u030b\3\2\2\2")
        buf.write("\u030a\u0308\3\2\2\2\u030b\u030d\3\2\2\2\u030c\u030a\3")
        buf.write("\2\2\2\u030d\u030e\7%\2\2\u030e\u030f\7%\2\2\u030f\u0310")
        buf.write("\3\2\2\2\u0310\u0311\b[\3\2\u0311\u00b6\3\2\2\2\u0312")
        buf.write("\u0315\n\f\2\2\u0313\u0315\5\u00b9]\2\u0314\u0312\3\2")
        buf.write("\2\2\u0314\u0313\3\2\2\2\u0315\u00b8\3\2\2\2\u0316\u0317")
        buf.write("\7^\2\2\u0317\u0318\t\r\2\2\u0318\u00ba\3\2\2\2\u0319")
        buf.write("\u031a\7^\2\2\u031a\u031d\n\r\2\2\u031b\u031d\n\16\2\2")
        buf.write("\u031c\u0319\3\2\2\2\u031c\u031b\3\2\2\2\u031d\u00bc\3")
        buf.write("\2\2\2\u031e\u0322\7$\2\2\u031f\u0321\5\u00b7\\\2\u0320")
        buf.write("\u031f\3\2\2\2\u0321\u0324\3\2\2\2\u0322\u0320\3\2\2\2")
        buf.write("\u0322\u0323\3\2\2\2\u0323\u0326\3\2\2\2\u0324\u0322\3")
        buf.write("\2\2\2\u0325\u0327\t\17\2\2\u0326\u0325\3\2\2\2\u0327")
        buf.write("\u0328\3\2\2\2\u0328\u0329\b_\4\2\u0329\u00be\3\2\2\2")
        buf.write("\u032a\u032e\7$\2\2\u032b\u032d\5\u00b7\\\2\u032c\u032b")
        buf.write("\3\2\2\2\u032d\u0330\3\2\2\2\u032e\u032c\3\2\2\2\u032e")
        buf.write("\u032f\3\2\2\2\u032f\u0331\3\2\2\2\u0330\u032e\3\2\2\2")
        buf.write("\u0331\u0332\5\u00bb^\2\u0332\u0333\b`\5\2\u0333\u00c0")
        buf.write("\3\2\2\2\u0334\u0335\13\2\2\2\u0335\u0336\ba\6\2\u0336")
        buf.write("\u00c2\3\2\2\2\u0337\u0338\7%\2\2\u0338\u0339\7%\2\2\u0339")
        buf.write("\u033d\3\2\2\2\u033a\u033c\13\2\2\2\u033b\u033a\3\2\2")
        buf.write("\2\u033c\u033f\3\2\2\2\u033d\u033e\3\2\2\2\u033d\u033b")
        buf.write("\3\2\2\2\u033e\u0340\3\2\2\2\u033f\u033d\3\2\2\2\u0340")
        buf.write("\u0341\bb\7\2\u0341\u00c4\3\2\2\2>\2\u00cf\u00d5\u00dc")
        buf.write("\u00e9\u00f6\u00fa\u0105\u010b\u010d\u0115\u012a\u0132")
        buf.write("\u0151\u015b\u0161\u0167\u016d\u0176\u017b\u017d\u0183")
        buf.write("\u018a\u018d\u0192\u0196\u019c\u01a1\u01a7\u01ad\u01b2")
        buf.write("\u01b9\u01bc\u01cf\u01da\u01e3\u01ec\u01f8\u01fe\u0207")
        buf.write("\u020f\u0215\u0219\u021c\u0222\u0227\u022d\u0238\u023e")
        buf.write("\u0244\u026f\u0274\u0300\u030a\u0314\u031c\u0322\u0326")
        buf.write("\u032e\u033d\b\3\25\2\b\2\2\3_\3\3`\4\3a\5\3b\6")
        return buf.getvalue()


class D96Lexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    T__0 = 1
    CLASS_DECLARE = 2
    MEMBER = 3
    METHODS = 4
    LIST_PARAM = 5
    LIST_METHOD = 6
    VAR_DECLARE = 7
    EXPFULL = 8
    INT_TYPE = 9
    FLOAT_TYPE = 10
    STRING = 11
    BOOL_TYPE = 12
    ID_LIST = 13
    VOID_TYPE = 14
    ARRAY_TYPE = 15
    ARRAY_LIST = 16
    PRIMITIVE_TYPE = 17
    LITERAL = 18
    INTEGER_LITERAL = 19
    STRING_LITERAL = 20
    REAL_LITERAL = 21
    HEX_TYPE = 22
    OCT_TYPE = 23
    BIN_TYPE = 24
    DEC_TYPE = 25
    EXP0 = 26
    EXP1 = 27
    EXP2 = 28
    EXP3 = 29
    EXP4 = 30
    EXP5 = 31
    EXP6 = 32
    EXP7 = 33
    EXP8 = 34
    EXP9 = 35
    EXP10 = 36
    EXP11 = 37
    LIST_EXP = 38
    ID = 39
    VAL = 40
    VAR = 41
    CLASS = 42
    DOLLAR = 43
    LP = 44
    RP = 45
    LCB = 46
    RCB = 47
    LSB = 48
    RSB = 49
    SEMI = 50
    COMMA = 51
    COLON = 52
    DOTDOT = 53
    BREAK = 54
    FOREACH = 55
    BOOLEAN = 56
    NULL = 57
    CONTINUE = 58
    TRUE = 59
    FALSE = 60
    IF = 61
    ELSEIF = 62
    ARRAYINT = 63
    ELSE = 64
    SELF = 65
    RETURN = 66
    NEW = 67
    ADD = 68
    ADD_STR = 69
    SUB = 70
    MUL = 71
    DIV = 72
    MOD = 73
    NOT = 74
    NOTEQUAL = 75
    EQUAL = 76
    EQUAL_STR = 77
    AND = 78
    OR = 79
    GT = 80
    LTE = 81
    LT = 82
    GTE = 83
    ASSIGN = 84
    WS = 85
    BLOCK_COMMENT = 86
    UNCLOSE_STRING = 87
    ILLEGAL_ESCAPE = 88
    ERROR_CHAR = 89
    UNTERMINATED_COMMENT = 90

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'main'", "'Int'", "'Float'", "'string'", "'Void'", "'val'", 
            "'var'", "'class'", "'$'", "'('", "')'", "'{'", "'}'", "'['", 
            "']'", "';'", "','", "':'", "'..'", "'Break'", "'Foreach'", 
            "'Boolean'", "'Null'", "'Continue'", "'True'", "'False'", "'if'", 
            "'elseif'", "'Array Int'", "'Else'", "'self'", "'return'", "'new'", 
            "'+'", "'+.'", "'-'", "'*'", "'/'", "'%'", "'!'", "'!='", "'=='", 
            "'==.'", "'&&'", "'||'", "'>'", "'<='", "'<'", "'>='", "'='" ]

    symbolicNames = [ "<INVALID>",
            "CLASS_DECLARE", "MEMBER", "METHODS", "LIST_PARAM", "LIST_METHOD", 
            "VAR_DECLARE", "EXPFULL", "INT_TYPE", "FLOAT_TYPE", "STRING", 
            "BOOL_TYPE", "ID_LIST", "VOID_TYPE", "ARRAY_TYPE", "ARRAY_LIST", 
            "PRIMITIVE_TYPE", "LITERAL", "INTEGER_LITERAL", "STRING_LITERAL", 
            "REAL_LITERAL", "HEX_TYPE", "OCT_TYPE", "BIN_TYPE", "DEC_TYPE", 
            "EXP0", "EXP1", "EXP2", "EXP3", "EXP4", "EXP5", "EXP6", "EXP7", 
            "EXP8", "EXP9", "EXP10", "EXP11", "LIST_EXP", "ID", "VAL", "VAR", 
            "CLASS", "DOLLAR", "LP", "RP", "LCB", "RCB", "LSB", "RSB", "SEMI", 
            "COMMA", "COLON", "DOTDOT", "BREAK", "FOREACH", "BOOLEAN", "NULL", 
            "CONTINUE", "TRUE", "FALSE", "IF", "ELSEIF", "ARRAYINT", "ELSE", 
            "SELF", "RETURN", "NEW", "ADD", "ADD_STR", "SUB", "MUL", "DIV", 
            "MOD", "NOT", "NOTEQUAL", "EQUAL", "EQUAL_STR", "AND", "OR", 
            "GT", "LTE", "LT", "GTE", "ASSIGN", "WS", "BLOCK_COMMENT", "UNCLOSE_STRING", 
            "ILLEGAL_ESCAPE", "ERROR_CHAR", "UNTERMINATED_COMMENT" ]

    ruleNames = [ "T__0", "CLASS_DECLARE", "MEMBER", "METHODS", "LIST_PARAM", 
                  "LIST_METHOD", "VAR_DECLARE", "EXPFULL", "INT_TYPE", "FLOAT_TYPE", 
                  "STRING", "BOOL_TYPE", "ID_LIST", "VOID_TYPE", "ARRAY_TYPE", 
                  "ARRAY_LIST", "PRIMITIVE_TYPE", "LITERAL", "INTEGER_LITERAL", 
                  "STRING_LITERAL", "REAL_LITERAL", "HEX_TYPE", "OCT_TYPE", 
                  "BIN_TYPE", "DEC_TYPE", "EXP0", "EXP1", "EXP2", "EXP3", 
                  "EXP4", "EXP5", "EXP6", "EXP7", "EXP8", "EXP9", "EXP10", 
                  "EXP11", "LIST_EXP", "ID", "VAL", "VAR", "CLASS", "DOLLAR", 
                  "LP", "RP", "LCB", "RCB", "LSB", "RSB", "SEMI", "COMMA", 
                  "COLON", "DOTDOT", "DOT", "EXPONENT", "DIGIT", "SIGN", 
                  "BREAK", "FOREACH", "BOOLEAN", "NULL", "CONTINUE", "TRUE", 
                  "FALSE", "IF", "ELSEIF", "ARRAYINT", "ELSE", "SELF", "RETURN", 
                  "NEW", "ADD", "ADD_STR", "SUB", "MUL", "DIV", "MOD", "NOT", 
                  "NOTEQUAL", "EQUAL", "EQUAL_STR", "AND", "OR", "GT", "LTE", 
                  "LT", "GTE", "ASSIGN", "WS", "BLOCK_COMMENT", "STR_CHAR", 
                  "ESC_SEQ", "ESC_ILLEGAL", "UNCLOSE_STRING", "ILLEGAL_ESCAPE", 
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
        print(result.text + ' is: ' + self.symbolicNames[tk-1])
        if tk == self.LITERAL:
            result.text = result.text.replace('_', '')
        return result;


    def action(self, localctx:RuleContext, ruleIndex:int, actionIndex:int):
        if self._actions is None:
            actions = dict()
            actions[19] = self.STRING_LITERAL_action 
            actions[93] = self.UNCLOSE_STRING_action 
            actions[94] = self.ILLEGAL_ESCAPE_action 
            actions[95] = self.ERROR_CHAR_action 
            actions[96] = self.UNTERMINATED_COMMENT_action 
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

                raise ErrorToken('UNTERMINATED_COMMENT')

     


