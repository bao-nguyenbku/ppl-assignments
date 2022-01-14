import unittest
from TestUtils import TestLexer


class LexerSuite(unittest.TestCase):

    # def test_identifier_1(self):
    #     self.assertTrue(TestLexer.test("_ _123 __abc__", "_,_123,__abc__,<EOF>", 101))

#     def test_identifier_2(self):
#         self.assertTrue(TestLexer.test("aCBbdc", "aCBbdc,<EOF>", 102))

#     def test_identifier_3(self):
#         self.assertTrue(TestLexer.test("$12abc", "$12abc,<EOF>", 103))

#     def test_identifier_4(self):
#         self.assertTrue(TestLexer.test("123a123", "123,a123,<EOF>", 104))

#     def test_identifier_5(self):
#         self.assertTrue(TestLexer.test("_av45", "_av45,<EOF>", 105))

#     def test_identifier_6(self):
#         self.assertTrue(TestLexer.test("$_free", "$_free,<EOF>", 106))

#     def test_identifier_7(self):
#         self.assertTrue(TestLexer.test("$saf afte", "$saf,afte,<EOF>", 107))

#     def test_identifier_8(self):
#         self.assertTrue(TestLexer.test(
#             "_12343_my const", "_12343_my,const,<EOF>", 108))

#     def test_identifier_9(self):
#         self.assertTrue(TestLexer.test("1ABC", "1,ABC,<EOF>", 109))

#     def test_identifier_10(self):
#         self.assertTrue(TestLexer.test("@abcd!ed", "Error Token @", 110))

#     def test_identifier_11(self):
#         self.assertTrue(TestLexer.test("%eHello", "%,eHello,<EOF>", 111))

#     def test_identifier_12(self):
#         self.assertTrue(TestLexer.test("*abcd", "*,abcd,<EOF>", 112))

#     def test_identifier_13(self):
#         self.assertTrue(TestLexer.test("$", "Error Token $", 113))

#     def test_identifier_14(self):
#         self.assertTrue(TestLexer.test("$abc 1adv _123 df3df",
#                         "$abc,1,adv,_123,df3df,<EOF>", 114))

#     def test_var_declare(self):
#         self.assertTrue(TestLexer.test("Var $dec, num: Int = 0b0101110, 0xaff",
#                         "Var,$dec,,,num,:,Int,=,0b0101110,,,0xaff,<EOF>", 115))

#     def test_float_number(self):
#         self.assertTrue(TestLexer.test(
#             "12.45e67 12E-9 1E3 12.2 17.3E+9", "12.45e67,12E-9,1E3,12.2,17.3E+9,<EOF>", 116))

#     def test_integer_number(self):
#         self.assertTrue(TestLexer.test(
#             "1_234 34 12_56_234 0189", "1234,34,1256234,0189,<EOF>", 117))

#     def test_hex_number(self):
#         self.assertTrue(TestLexer.test("0x1T 0XA100 0x123 0x0000",
#                         "0x1,T,0XA100,0x123,0x0000,<EOF>", 118))

#     def test_hex_number_2(self):
#         self.assertTrue(TestLexer.test("0xFG 0FAA X123",
#                         "0xF,G,0,FAA,X123,<EOF>", 119))

#     def test_string_1(self):
#         self.assertTrue(TestLexer.test("\"aj\elhadef\"",
#                         "Illegal Escape In String: aj\e", 120))

#     def test_string_2(self):
#         self.assertTrue(TestLexer.test(
#             "\"ab3j\tlhadef\"", "ab3j	lhadef,<EOF>", 118))

#     def test_string_3(self):
#         self.assertTrue(TestLexer.test("""
#             "Hello from '"Python'""
#         """, """Hello from "Python",<EOF>""", 121))

#     def test_string_4(self):
#         self.assertTrue(TestLexer.test("\"abc \r babc", """Unclosed String: abc
#  babc""", 122))

#     def test_expression_1(self):
#         self.assertTrue(TestLexer.test("(23 >= 5 && a != 9) || 7 + 9",
#                         "(,23,>=,5,&&,a,!=,9,),||,7,+,9,<EOF>", 123))

#     def test_expression_2(self):
#         self.assertTrue(TestLexer.test("34 < 9 + 12e3 - 1.34",
#                         "34,<,9,+,12e3,-,1.34,<EOF>", 124))

#     def test_comment(self):
#         self.assertTrue(TestLexer.test("""
#             ## This is comment ##
#         """, "<EOF>", 125))

#     def test_array(self):
#         self.assertTrue(TestLexer.test("Array(1,2,3,4)",
#                         "Array,(,1,,,2,,,3,,,4,),<EOF>", 126))

#     def test_if_else_stmt(self):
#         self.assertTrue(TestLexer.test("""
#             If (a > b) {Return a;}
#             Elseif (a == b) {a = a + b;}
#             Else {Return b;}
#             """, "If,(,a,>,b,),{,Return,a,;,},Elseif,(,a,==,b,),{,a,=,a,+,b,;,},Else,{,Return,b,;,},<EOF>", 127))

#     def test_for_stmt(self):
#         self.assertTrue(TestLexer.test("""
#             Foreach ($x In 1 .. 100 By 1) {
#                 sum = sum + a[$x];
#             }
#             """, "Foreach,(,$x,In,1,..,100,By,1,),{,sum,=,sum,+,a,[,$x,],;,},<EOF>", 128))

#     def test_for_block_stmt(self):
#         self.assertTrue(TestLexer.test("""
#             {
#                 Var r, s: Int;
#                 r = 2.0;
#                 Var a, b: Array[Int, 5];
#                 s = r * r * Self.myPI;
#                 a[0] = s;
#             }
#             """, "{,Var,r,,,s,:,Int,;,r,=,2.0,;,Var,a,,,b,:,Array,[,Int,,,5,],;,s,=,r,*,r,*,Self,.,myPI,;,a,[,0,],=,s,;,},<EOF>", 129))

#     def test_array_2(self):
#         self.assertTrue(TestLexer.test("""
#             Var $arr : Array[Array[Int, 3], 3] = Array(
#                                                         Array(1,2,5),
#                                                         Array(2,5,6),
#                                                         Array(5,8,7)
#                                                         );
#             )""", "Var,$arr,:,Array,[,Array,[,Int,,,3,],,,3,],=,Array,(,Array,(,1,,,2,,,5,),,,Array,(,2,,,5,,,6,),,,Array,(,5,,,8,,,7,),),;,),<EOF>", 130))

#     def test_string_5(self):
#         self.assertTrue(TestLexer.test("""
#                 Var s : String = \"adsfsdf\vas\"
#                 """, "", 131))

#     def test_literal(self):
#             self.assertTrue(TestLexer.test("""
#                     0b12 0b01 12.34 1560 0X1B
#                     """, "0b1,2,0b01,12.34,1560,0X1B,<EOF>", 132))

#     def test_keyword(self):
#         self.assertTrue(TestLexer.test("""
#                 New Return True False Foreach If Elseif Else Float Int String Var Val Constructor Destructor Null Class By In
#                 """, "New,Return,True,False,Foreach,If,Elseif,Else,Float,Int,String,Var,Val,Constructor,Destructor,Null,Class,By,In,<EOF>", 133))

#     def test_operator(self):
#         self.assertTrue(TestLexer.test("""
#                 + - * / % == != ! > < >= <= || && . :: ( ) { } [ ] ==. +.
#                 """, "+,-,*,/,%,==,!=,!,>,<,>=,<=,||,&&,.,::,(,),{,},[,],==.,+.,<EOF>", 134))

    def test_string_6(self):
        self.assertTrue(TestLexer.test("""
        "ahihi\\""
        ""","ahihi\\\",<EOF>",135))

    def test_string_7(self):
        self.assertTrue(TestLexer.test("\"abc\\nabc\"","abc\\nabc,<EOF>",136))
    
    def test_string_8(self):
        self.assertTrue(TestLexer.test("\"abc\\ta\\nbc\"","abc\\ta\\nbc,<EOF>",137))
    
    def test_string_9(self):
        self.assertTrue(TestLexer.test("\"abc\" 0 \"12ab\\fc0.1\"","abc,0,12ab\\fc0.1,<EOF>",138))
    
    def test_string_10(self):
        self.assertTrue(TestLexer.test("""
        "0.1anc\'cv" 0.mne "12\\\\3"
        ""","0.1anc'cv,0,.,mne,12\\3,<EOF>",139))

    def test_string_11(self):
        self.assertTrue(TestLexer.test("abc \"abc1!!@#$$%^i\\n\" 12yz","abc,abc1!!@#$$%^i\\n,12,yz,<EOF>",140))
    
    def test_string_12(self):
        self.assertTrue(TestLexer.test("\"!h$5FBi6\"_q\"!SZR,H}\"sIfpw","!h$5FBi6,_q,!SZR,H},sIfpw,<EOF>",141))
    
    def test_string_13(self):
        self.assertTrue(TestLexer.test("""
        4"&J^1a_." QGn"?67Sp"{,}6Asz"Yx]("
        ""","4,&J^1a_.,QGn,?67Sp,{,,,},6,Asz,Yx](,<EOF>",142))
    
    def test_string_14(self):
        self.assertTrue(TestLexer.test("0f1_\"^VLR@\\\\OusM;\"uGM+jE","0,f1_,^VLR@\\\\OusM;,uGM,+,jE,<EOF>",143))
    
    def test_string_15(self):
        self.assertTrue(TestLexer.test("\"(IFq+lq(\"IhK6we(*.*)GdvS{(}","(IFq+lq(,IhK6we,(,*,.,*,),GdvS,{,(,},<EOF>",144))

    # def test_illegal_escape_1(self):
    #     self.assertTrue(TestLexer.test("\"bac\\ma\"","Illegal Escape In String: bac\\m",145))

    # def test_illegal_escape_2(self):
    #     self.assertTrue(TestLexer.test("\"baMD\\HLSc\\na\"","Illegal Escape In String: baMD\\H",146))

    # def test_illegal_escape_3(self):
    #     self.assertTrue(TestLexer.test("\",dls\\F12!LS\\kc\\na\"","Illegal Escape In String: ,dls\\F",147))

    # def test_illegal_escape_4(self):
    #     self.assertTrue(TestLexer.test("\"ado\\mado\"","Illegal Escape In String: ado\\m",148))

    # def test_illegal_escape_5(self):
    #     self.assertTrue(TestLexer.test("123abc \"xyz\k 456","123,abc,Illegal Escape In String: xyz\k",149))

    # def test_illegal_escape_6(self):
    #     self.assertTrue(TestLexer.test("\"aa\wb\"","Illegal Escape In String: aa\w",150))

    # def test_illegal_escape_7(self):
    #     self.assertTrue(TestLexer.test("ba+12+\"na\"\"md+1.2-468\lb","ba,+,12,+,na,Illegal Escape In String: md+1.2-468\l",151))
    
    # def test_illegal_escape_8(self):
    #     self.assertTrue(TestLexer.test("\"1.2+1.3+1.4\\o'\"123","Illegal Escape In String: 1.2+1.3+1.4\\o",152))
    
    # def test_illegal_escape_9(self):
    #     self.assertTrue(TestLexer.test("(*nac*)+1.1 \"ba\\qm\f\"","+,1.1,Illegal Escape In String: ba\\q",153))
    
    # def test_illegal_escape_10(self):
    #     self.assertTrue(TestLexer.test("\"concaheo\\uabc","Illegal Escape In String: concaheo\\u",154))
    
    # def test_unclose_String_1(self):
    #     self.assertTrue(TestLexer.test("\"bacxyc","Unclosed String: bacxyc",155))
    
    # def test_unclose_String_2(self):
    #     self.assertTrue(TestLexer.test("NmkobYn{!}+I1+\"`YS2h.J(","NmkobYn,+,I1,+,Unclosed String: `YS2h.J(",156))
    
    # def test_unclose_String_3(self):
    #     self.assertTrue(TestLexer.test("\"acnv \" \"abc","acnv ,Unclosed String: abc",157))

    # def test_unclose_String_4(self):
    #     self.assertTrue(TestLexer.test("\"acms!,lds \" {\"abc\"} 123\"abc","acms!,lds ,123,Unclosed String: abc",158))
    
    # def test_unclose_String_5(self):
    #     self.assertTrue(TestLexer.test("a+11.2+\"mam.123\" 12 \"%^&","a,+,11.2,+,mam.123,12,Unclosed String: %^&",159))
    
    # def test_unclose_String_6(self):
    #     self.assertTrue(TestLexer.test("""
    #     38n"[#Ffs?0ED"0."T`#
    #     ""","38,n,[#Ffs?0ED,0.,Unclosed String: T`#7n",160))