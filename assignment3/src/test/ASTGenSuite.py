import unittest
from TestUtils import TestAST
from AST import *

class ASTGenSuite(unittest.TestCase):
    def test_simple_program(self):
       
        input = """
        Class C {
            Var $c: Int = 2;
            get() { }
            Constructor(a: Float; b: String) { }
        }
        Class A {
            Var b: Array[Int, 3];
            getA(a: Float) {
                Var b: Int;
                Var Cobj: C = New C(3.4, "Hello");
                b = Cobj::$c;
            }
        }
        """
        expect = ""
        self.assertTrue(TestAST.test(input,expect,300))

    
   