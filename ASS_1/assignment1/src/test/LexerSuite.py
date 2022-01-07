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

    def test_identifier_5(self):
        self.assertTrue(TestLexer.test("##fdsjfsfhs##", "", 105))
