import unittest
from TestUtils import TestChecker
from AST import *

class CheckerSuite(unittest.TestCase):
    def test(self):
        input = """
        Class Dog {
            Val $r :Int = 2;
            Var a: Float = 2;
            get(a, b: Int; c: Float) { }
            
        }
        """
        # get(a, b: Int; c: Float) {  }
        expect = "[]"
        self.assertTrue(TestChecker.test(input,expect,400))
    # def test0(self):
    #     input = """
    #     Class Dog : Animal {
    #         Val $a : Int = 3.2;
    #         $getDog() { }
    #     }
    #     Class Meow {
    #         $set() { }
    #     }
    #     """
    #     expect = "Illegal Constant Expression: FloatLit(3.2)"
    #     self.assertTrue(TestChecker.test(input,expect,400))
    # def test1(self):
    #     input = """
    #     Class A {
    #         Var $a: Int;
    #     }
    #     Class A {
    #         Val $b: Float;
    #     }
    #     """
    #     expect = "Redeclared Class: A"
    #     self.assertTrue(TestChecker.test(input,expect,401))

    # def test2(self):
    #     input = """
    #     Class A {
    #         Val $a: Int = True;
    #     }
    #     """
    #     expect = "Illegal Constant Expression: BooleanLit(True)"
    #     self.assertTrue(TestChecker.test(input,expect,402))
    # def test3(self):
    #     input = """
    #     Class A {
    #         Val $a: Int = 3;
    #     }
    #     Class B {
    #         Val $b: Float = A::$a;
    #     }
    #     """
    #     expect = "Illegal Constant Expression: FieldAccess(Id(A),Id($a))"
    #     self.assertTrue(TestChecker.test(input,expect,403))

    