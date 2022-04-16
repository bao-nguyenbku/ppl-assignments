import unittest
from TestUtils import TestAST
from AST import *

class ASTGenSuite(unittest.TestCase):
    def test_simple_program(self):
       
        input = """
        Class A {
            Var a: Array[Int, 2]= Array(1,2);
        }
        """
        expect = ""
        self.assertTrue(TestAST.test(input,expect,300))

    
   