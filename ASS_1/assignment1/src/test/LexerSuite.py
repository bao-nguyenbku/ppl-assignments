import unittest
from TestUtils import TestLexer


class LexerSuite(unittest.TestCase):

#     def test_identifier_1(self):
#         self.assertTrue(TestLexer.test("_", "_,<EOF>", 101))

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
#         self.assertTrue(TestLexer.test("_12343_my const", "_12343_my,const,<EOF>", 108))

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

#     def test_var_declare(self):
#         self.assertTrue(TestLexer.test("Var $dec, num: Int = 0b0101110, 0xaff", "Var,$dec,,,num,:,Int,=,0b0101110,,,0xaff,<EOF>", 114))
    
#     def test_float_number(self):
#         self.assertTrue(TestLexer.test("12.45e67", "12.45e67,<EOF>", 115))

#     def test_hex_number(self):
#         self.assertTrue(TestLexer.test("0x1T", "0x1,T,<EOF>", 116))

#     def test_string_1(self):
#         self.assertTrue(TestLexer.test("\"aj\elhadef\"", "Illegal Escape In String: aj\e", 117)) 

#     def test_string_2(self):
#         self.assertTrue(TestLexer.test("\"ab3j\tlhadef\"", "ab3j	lhadef,<EOF>", 118))  

#     def test_string_3(self):
#         self.assertTrue(TestLexer.test("""
#             "Hello from '"Python'""
#         """, """Hello from "Python",<EOF>""", 119))  

#     def test_string_4(self):
#         self.assertTrue(TestLexer.test("\"abc \r babc", """Unclosed String: abc 
#  babc""", 120))

#     def test_expression_1(self):
#         self.assertTrue(TestLexer.test("(23 >= 5 && a != 9) || 7 + 9", "(,23,>=,5,&&,a,!=,9,),||,7,+,9,<EOF>", 121))
    
#     def test_expression_2(self):
#         self.assertTrue(TestLexer.test("34 < 9 + 12e3 - 1.34", "34,<,9,+,12e3,-,1.34,<EOF>", 122))

#     def test_comment(self):
#         self.assertTrue(TestLexer.test("""
#             ## This is comment ##
#         """, "<EOF>", 123))

#     def test_array(self):
#         self.assertTrue(TestLexer.test("Array(1,2,3,4)", "Array,(,1,,,2,,,3,,,4,),<EOF>", 124))

#     def test_if_else_stmt(self):
#         self.assertTrue(TestLexer.test("""
#             If (a > b) {Return a;}
#             Elseif (a == b) {a = a + b;}
#             Else {Return b;}
#             """, "If,(,a,>,b,),{,Return,a,;,},Elseif,(,a,==,b,),{,a,=,a,+,b,;,},Else,{,Return,b,;,},<EOF>", 125))
#     def test_for_stmt(self):
#         self.assertTrue(TestLexer.test("""
#             Foreach ($x In 1 .. 100 By 1) {
#                 sum = sum + a[$x];
#             }
#             """, "Foreach,(,$x,In,1,..,100,By,1,),{,sum,=,sum,+,a,[,$x,],;,},<EOF>", 126))
    
#     def test_for_block_stmt(self):
#         self.assertTrue(TestLexer.test("""
#             {
#                 Var r, s: Int; 
#                 r = 2.0; 
#                 Var a, b: Array[Int, 5]; 
#                 s = r * r * Self.myPI; 
#                 a[0] = s;
#             }
#             """, "{,Var,r,,,s,:,Int,;,r,=,2.0,;,Var,a,,,b,:,Array,[,Int,,,5,],;,s,=,r,*,r,*,Self,.,myPI,;,a,[,0,],=,s,;,},<EOF>", 127))
    
#     def test_array(self):
#         self.assertTrue(TestLexer.test("""
#             Var $arr : Array[Array[Int, 3], 3] = 
#                                        Array(
#                                            Array(1,2,5),
#                                            Array(2,5,6),
#                                            Array(5,8,7)
#                                            );
#             )""", "", 128))
    def test_string(self):
            self.assertTrue(TestLexer.test("""
            "adada \vdsfs"
            """, "", 129))
    # def test_declare(self):
    #         self.assertTrue(TestLexer.test("""
    #         Var s : String = \"adsfsdf\vas\"
    #         """, "", 130))

    