import unittest
from TestUtils import TestLexer


class LexerSuite(unittest.TestCase):

    # def demoTest(self):
    #     """test demo"""
    #     self.assertTrue(TestLexer.test("123gfdgdsds", "", 600))
    # def test_iden(self):
    #     self.assertTrue(TestLexer.test("123gfdgdsds", "", 600))


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
    #     self.assertTrue(TestLexer.test("12.345e-6235", "", 105))

    # def test_string(self):
    #     self.assertTrue(TestLexer.test("\"abcdj\elhadef\"", "", 105)) 

    # def test_string(self):
    #     self.assertTrue(TestLexer.test("\"abcdj\tlhadef\"", "", 105))  

    # def test_string(self):
    #     self.assertTrue(TestLexer.test("\"abcdj\elhadef", "", 105))  

    # def test_string(self):
    #     self.assertTrue(TestLexer.test("\"He asked me: '\"Where \t is John?'\"\"", "", 105))

    # def test_expression(self):
    #     self.assertTrue(TestLexer.test("(23 >= 5 && a != 9) || 7 + 9", "", 105))
    
    def test_expression(self):
        self.assertTrue(TestLexer.test("", "", 105))

    