import unittest
from TestUtils import TestCodeGen
from AST import *


class CheckCodeGenSuite(unittest.TestCase):
    def test(self):
        input = """
        Class Program {
            main() { 
                io.putBool(True);
            }
        }
        """
        expect = ""
        self.assertTrue(TestCodeGen.test(input,expect,500))
    # def test_int_ast(self):
    # 	input = Program([
    # 		FuncDecl(Id("main"),[],VoidType(),Block([],[
    # 			CallExpr(Id("putInt"),[IntLiteral(5)])]))])
    # 	expect = "5"
    # 	self.assertTrue(TestCodeGen.test(input,expect,501))
