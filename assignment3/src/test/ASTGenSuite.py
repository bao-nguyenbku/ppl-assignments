import unittest
from TestUtils import TestAST
from AST import *

class ASTGenSuite(unittest.TestCase):
    def test_simple_program(self):
       
        input = """
        Class A { }
        Class E {
            Var a : Int;
            Constructor(a: A) { }
        }
        Class Program {
            main() {
                Val a: Array[Array[Array[Int,2],2],2]
                = Array(1,2)
            }
        }
        """
        expect = ""
        self.assertTrue(TestAST.test(input,expect,300))

    
   