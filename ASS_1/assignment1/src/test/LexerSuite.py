import unittest
from TestUtils import TestLexer


class LexerSuite(unittest.TestCase):

    def test_iden(self):
        self.assertTrue(TestLexer.test("""
        Int main() {
            a = 20;
        }
        """, "", 600))


    # def test_identifier_1(self):
    #     self.assertTrue(TestLexer.test("abc", "abc,<EOF>", 101))

    # def test_identifier_2(self):
    #     self.assertTrue(TestLexer.test("aCBbdc", "aCBbdc,<EOF>", 102))

    # def test_identifier_3(self):
    #     self.assertTrue(TestLexer.test("aAsVN3", "aAsVN3,<EOF>", 103))

    # def test_identifier_4(self):
    #     self.assertTrue(TestLexer.test("123a123", "123,a123,<EOF>", 104))

    # def test_var_declare(self):
    #     self.assertTrue(TestLexer.test("var $dec, num: Int = 0b0101110, 0xaff", "", 105))
    
    # def test_float_number(self):
    #     self.assertTrue(TestLexer.test("12.45e67", "", 105))
    # def test_hex_number(self):
    #     self.assertTrue(TestLexer.test("0x1T", "", 105))

    # def test_string_1(self):
    #     self.assertTrue(TestLexer.test("\"aj\elhadef\"", "", 105)) 

    # def test_string_2(self):
    #     self.assertTrue(TestLexer.test("\"ab3j\tlhadef\"", "", 106))  

    # def test_string_3(self):
    #     self.assertTrue(TestLexer.test("""
    #         "Hello from '"fdsss"
    #     """, "", 107))  

    # def test_string_4(self):
    #     self.assertTrue(TestLexer.test("\"abc \r babc\"", "", 108))

    # def test_expression(self):
    #     self.assertTrue(TestLexer.test("(23 >= 5 && a != 9) || 7 + 9", "", 105))
    
    # def test_expression(self):
    #     self.assertTrue(TestLexer.test("34<9", "", 105))

    # def test_expression(self):
    #     self.assertTrue(TestLexer.test("a = b.get();", "", 105))

    # def test_expression(self):
    #     self.assertTrue(TestLexer.test("a + b", "", 105))

    # def test_expression(self):
    #     self.assertTrue(TestLexer.test("""
    #         \"Hello\" ==. \"World\" 
    #         """, "", 105))

    # def test_comment(self):
    #     self.assertTrue(TestLexer.test("##This is comment", "", 105))

    # def test_array(self):
    #     self.assertTrue(TestLexer.test("Array(1,2,3,4)", "", 105))

    # def test_array(self):
    #     self.assertTrue(TestLexer.test("Array(\"Hello\",\"World\",3,4)", "", 105))
    # def test_array(self):
    #     self.assertTrue(TestLexer.test("""
    #         Array(
    #             Array(1,2,3),
    #             Array(\"a,b,c\"),
    #             Array(12.4, 45e4, 0b1001)
    #         )""", "", 105))
    # def test_if_else_stmt(self):
    #     self.assertTrue(TestLexer.test("""
    #         If (a > b) {return a;}
    #         Elseif (a == b) {a = a + b;}
    #         Else {return b;}
    #         """, "", 105))
    # def test_for_stmt(self):
    #     self.assertTrue(TestLexer.test("""
    #         For ($x In 1 .. 100 By 1) {
    #             sum = sum + a[$x];
    #         }
    #         """, "", 105))
    # def test_for_stmt(self):
    #     self.assertTrue(TestLexer.test("""
    #         Shape::$getNum();
    #         """, "", 105))
    
    # def test_for_block_stmt(self):
    #     self.assertTrue(TestLexer.test("""
    #         {
    #             var r, s: Int; 
    #             r = 2.0; 
    #             var a, b: Array[Int, 5]; 
    #             s = r * r * self.myPI; 
    #             a[0] = s;
    #         }
    #         """, "", 106))
    

    