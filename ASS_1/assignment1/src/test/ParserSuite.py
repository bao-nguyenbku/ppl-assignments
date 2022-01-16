import unittest
from TestUtils import TestParser

class ParserSuite(unittest.TestCase):
    def test_simple_program(self):

        input = ["""c = 4 + 5 / 12 * (a[1] + 19 - b[2][1])""",
                 """b != a[0] + 9 - 1.234e5 || 6""",
                 """"""
        ]
        expect = "successful"
        for i in input:
            self.assertTrue(TestParser.test(i, expect, input.index(i)+200))
    # def test_simple_program(self):
    #     input = """
    #         Class ChildClass: SuperClass {
    #             insertSound() {

    #             }
    #         }
    #         Class Program {
    #             Var $count: Int = 0;
    #             remove(){

    #             }
    #             insert(str: String) {

    #             }
                
    #             main() {

    #             }
    #         }
    #     """
    #     expect = "successful"
    #     self.assertTrue(TestParser.test(input,expect,201))
