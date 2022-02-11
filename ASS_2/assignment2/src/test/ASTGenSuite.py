import unittest
from TestUtils import TestAST
from AST import *

class ASTGenSuite(unittest.TestCase):
    # def test(self):
    #     input = """
    #     Class A {

    #     }
    #     Class B {
    #         foo() { 
    #             If (a) {
    #                 a = 4;
    #             }
    #             Elseif (b) {
    #                 a = 3;
    #                 b = 5;
    #                 c = 8;
    #             }
    #             Elseif (12 == 8) {
    #                 r = 1;
    #                 pi = 0.3;
    #             }
    #             Elseif (9) {
    #                 r = 6;
    #             }
    #             Else {
    #                 t = myElse;
    #             }
    #         }
    #     }
    #     """
    #     expect = """Program([ClassDecl(Id(A),[]),ClassDecl(Id(B),[MethodDecl(Id(foo),Instance,[],Block([],[If(Id(a),Block([],[AssignStmt(Id(a),IntLit(4))]),If(Id(b),Block([],[AssignStmt(Id(a),IntLit(3)),AssignStmt(Id(b),IntLit(5)),AssignStmt(Id(c),IntLit(8))]),If(BinaryOp(==,IntLit(12),IntLit(8)),Block([],[AssignStmt(Id(r),IntLit(1)),AssignStmt(Id(pi),FloatLit(0.3))]),If(IntLit(9),Block([],[AssignStmt(Id(r),IntLit(6))]),Block([],[AssignStmt(Id(t),Id(myElse))])))))]))])])"""
    #     self.assertTrue(TestAST.test(input,expect,300))
    # def test1(self):
    #     input = """
    #     Class Dog { 
    #         Var r: Float = 0xA001;
    #         Val $a, $b: Boolean = True, True;
    #     }"""
    #     expect = """Program([ClassDecl(Id(Dog),[AttributeDecl(Instance,VarDecl(Id(r),FloatType,IntLit(40961))),AttributeDecl(Static,ConstDecl(Id($a),BoolType,BooleanLit(True))),AttributeDecl(Static,ConstDecl(Id($b),BoolType,BooleanLit(True)))])])"""
    #     self.assertTrue(TestAST.test(input,expect,301))
    # def test2(self):
    #     input = """
    #     Class Cat {
    #         f() {
    #             a = b[1][2][3];
    #         }
    #     }"""
    #     expect = """"""
    #     self.assertTrue(TestAST.test(input,expect,302))
    # def test3(self):
    #     input = """
    #     Class Cat {
    #         f() {
    #             a = b[1][2][3];
    #         }
    #     }"""
    #     expect = """"""
    #     self.assertTrue(TestAST.test(input,expect,303))

    def test1(self):
        input = """
        Class Program {
            main () {
                a = 1;
            }
        } 
        """
        expect = """Program([ClassDecl(Id(Dog),[])])"""
        self.assertTrue(TestAST.test(input,expect,301))
    # def test2(self):
    #     input = """Class Dog : Animal { }"""
    #     expect = """Program([ClassDecl(Id(Dog),Id(Animal),[])])"""
    #     self.assertTrue(TestAST.test(input,expect,302))
    # def test3(self):
    #     input = """Class Dog : Animal { main(){} }"""
    #     expect = """Program([ClassDecl(Id(Dog),Id(Animal),[MethodDecl(Id(main),Instance,[],Block([],[]))])])"""
    #     self.assertTrue(TestAST.test(input,expect,303))
    # def test4(self):
    #     input = """Class Dog : Animal { $test(){} main(){} }"""
    #     expect = """Program([ClassDecl(Id(Dog),Id(Animal),[MethodDecl(Id($test),Static,[],Block([],[])),MethodDecl(Id(main),Instance,[],Block([],[]))])])"""
    #     self.assertTrue(TestAST.test(input,expect,304))
    # def test5(self):
    #     input = """Class Dog : Animal { $test(a, b, c:Int){} }"""
    #     expect = """Program([ClassDecl(Id(Dog),Id(Animal),[MethodDecl(Id($test),Static,[param(Id(a),IntType),param(Id(b),IntType),param(Id(c),IntType)],Block([],[]))])])"""
    #     self.assertTrue(TestAST.test(input,expect,305))
    # def test6(self):
    #     input = """Class Dog : Animal { $test(a, b, c:Int){ Break; Continue; } }"""
    #     expect = """Program([ClassDecl(Id(Dog),Id(Animal),[MethodDecl(Id($test),Static,[param(Id(a),IntType),param(Id(b),IntType),param(Id(c),IntType)],Block([],[Break,Continue]))])])"""
    #     self.assertTrue(TestAST.test(input,expect,306))
    # def test7(self):
    #     input = """
    #     Class Dog : Animal 
    #     { 
    #         $test(a, b, c:Int)
    #         { 
    #             Var a: Int; 
    #             Break; 
    #             Continue; 
    #         } 
    #     }"""
    #     expect = """Program([ClassDecl(Id(Dog),Id(Animal),[MethodDecl(Id($test),Static,[param(Id(a),IntType),param(Id(b),IntType),param(Id(c),IntType)],Block([VarDecl(Id(a),IntType)],[Break,Continue]))])])"""
    #     self.assertTrue(TestAST.test(input,expect,307))
    # def test8(self):
    #     input = """
    #     Class Dog : Animal 
    #     { 
    #         $test(a, b, c:Int)
    #         { 
    #             Var a: Int; 
    #             Var b: Float;
    #             Var c: String;
    #             Break; 
    #             Continue; 
    #         } 
    #     }"""
    #     expect = """Program([ClassDecl(Id(Dog),Id(Animal),[MethodDecl(Id($test),Static,[param(Id(a),IntType),param(Id(b),IntType),param(Id(c),IntType)],Block([VarDecl(Id(a),IntType),VarDecl(Id(b),FloatType),VarDecl(Id(c),StringType)],[Break,Continue]))])])"""
    #     self.assertTrue(TestAST.test(input,expect,308))
    # def test9(self):
    #     input = """
    #     Class Dog : Animal 
    #     { 
    #         $test()
    #         { 
    #             Var ast, bdafs, cdadsas: Int; 
    #             Break; 
    #             Continue; 
    #         } 
    #     }"""
    #     expect = """Program([ClassDecl(Id(Dog),Id(Animal),[MethodDecl(Id($test),Static,[],Block([VarDecl(Id(ast),IntType),VarDecl(Id(bdafs),IntType),VarDecl(Id(cdadsas),IntType)],[Break,Continue]))])])"""
    #     self.assertTrue(TestAST.test(input,expect,309))
    # def test10(self):
    #     input = """
    #     Class Dog : Animal 
    #     { 
    #         Val $a : String;
    #         Var b, $c: Int;
    #         $test()
    #         { 
    #             Var ast, bdafs, cdadsas: Int; 
    #             Val bv : Float;
    #             Break; 
    #             Continue; 
    #         } 
    #     }"""
    #     expect = """Program([ClassDecl(Id(Dog),Id(Animal),[ConstDecl(Id($a),StringType,None),VarDecl(Id(b),IntType),VarDecl(Id($c),IntType),MethodDecl(Id($test),Static,[],Block([VarDecl(Id(ast),IntType),VarDecl(Id(bdafs),IntType),VarDecl(Id(cdadsas),IntType),ConstDecl(Id(bv),FloatType,None)],[Break,Continue]))])])"""
    #     self.assertTrue(TestAST.test(input,expect,310))
    # def test11(self):
    #     input = """
    #     Class Dog : Animal 
    #     { 
    #         Val $a : String;
    #         Var b, $c: Int;
    #         $test()
    #         { 
    #             Var ast, bdafs, cdadsas: Int; 
    #             Val bv : Float;
    #             Break; 
    #             Continue; 
    #         } 
    #         main(a, b, c : Int)
    #         {
    #             Var a : Boolean;
    #         }
    #     }"""
    #     expect = """Program([ClassDecl(Id(Dog),Id(Animal),[ConstDecl(Id($a),StringType,None),VarDecl(Id(b),IntType),VarDecl(Id($c),IntType),MethodDecl(Id($test),Static,[],Block([VarDecl(Id(ast),IntType),VarDecl(Id(bdafs),IntType),VarDecl(Id(cdadsas),IntType),ConstDecl(Id(bv),FloatType,None)],[Break,Continue])),MethodDecl(Id(main),Instance,[param(Id(a),IntType),param(Id(b),IntType),param(Id(c),IntType)],Block([VarDecl(Id(a),BoolType)],[]))])])"""
    #     self.assertTrue(TestAST.test(input,expect,311))
    # def test12(self):
    #     input = """
    #     Class Dog : Animal 
    #     { 
    #         $test()
    #         { 
    #             Var ast, d, c : Int = 1, 5, 7; 
    #         } 
    #     }"""
    #     expect = """Program([ClassDecl(Id(Dog),Id(Animal),[MethodDecl(Id($test),Static,[],Block([VarDecl(Id(ast),IntType,IntLit(1)),VarDecl(Id(d),IntType,IntLit(5)),VarDecl(Id(c),IntType,IntLit(7))],[]))])])"""
    #     self.assertTrue(TestAST.test(input,expect,312))
    # def test13(self):
    #     input = """
    #     Class Dog : Animal 
    #     { 
    #         $test()
    #         { 
    #             Var ast, d, c : Int = 1, 5, 7; 
    #             Var a : Boolean = True; 
    #             Var a : String = "abc";
    #         } 
    #         Var c, $d, e, $f : Int = 1, 2, 2, 3;
    #         Var a, b : Int = 5 - 6 * 7, 6 / 7 + 2;
    #     }"""
    #     expect = """Program([ClassDecl(Id(Dog),Id(Animal),[MethodDecl(Id($test),Static,[],Block([VarDecl(Id(ast),IntType,IntLit(1)),VarDecl(Id(d),IntType,IntLit(5)),VarDecl(Id(c),IntType,IntLit(7)),VarDecl(Id(a),BoolType,BooleanLit(True)),VarDecl(Id(a),StringType,StringLit(abc))],[])),VarDecl(Id(c),IntType,IntLit(1)),VarDecl(Id($d),IntType,IntLit(2)),VarDecl(Id(e),IntType,IntLit(2)),VarDecl(Id($f),IntType,IntLit(3)),VarDecl(Id(a),IntType,BinaryOp(-,IntLit(5),BinaryOp(*,IntLit(6),IntLit(7)))),VarDecl(Id(b),IntType,BinaryOp(+,BinaryOp(/,IntLit(6),IntLit(7)),IntLit(2)))])])"""
    #     self.assertTrue(TestAST.test(input,expect,313))
    # def test14(self):
    #     input = """
    #     Class Dog : Animal 
    #     { 
    #         $test()
    #         { 
    #             a = 5;
    #             b = 7;
    #             c = 5-8/3*8;
    #         } 
    #     }"""
    #     expect = """Program([ClassDecl(Id(Dog),Id(Animal),[MethodDecl(Id($test),Static,[],Block([],[AssignStmt(Id(a),IntLit(5)),AssignStmt(Id(b),IntLit(7)),AssignStmt(Id(c),BinaryOp(-,IntLit(5),BinaryOp(*,BinaryOp(/,IntLit(8),IntLit(3)),IntLit(8))))]))])])"""
    #     self.assertTrue(TestAST.test(input,expect,314))
    # def test15(self):
    #     input = """
    #     Class Dog : Animal 
    #     { 
    #         $test()
    #         { 
    #             Var a, b, c : Int = 0, 0, 0;
    #             If (a == b)
    #             {
    #                 b = c;
    #                 Var div, mod, mul : Float = 0.25, 1.2e5, 0.3;
    #                 c = div / mod * mul;
    #             }
    #             Else
    #             {
    #                 b = 0;
    #                 c = 0;
    #             }
    #         } 
    #     }"""
    #     expect = """Program([ClassDecl(Id(Dog),Id(Animal),[MethodDecl(Id($test),Static,[],Block([VarDecl(Id(a),IntType,IntLit(0)),VarDecl(Id(b),IntType,IntLit(0)),VarDecl(Id(c),IntType,IntLit(0))],[If(BinaryOp(==,a,b),Block([VarDecl(Id(div),FloatType,FloatLit(0.25)),VarDecl(Id(mod),FloatType,FloatLit(120000.0)),VarDecl(Id(mul),FloatType,FloatLit(0.3))],[AssignStmt(Id(b),c),AssignStmt(Id(c),BinaryOp(*,BinaryOp(/,div,mod),mul))]),Block([],[AssignStmt(Id(b),IntLit(0)),AssignStmt(Id(c),IntLit(0))]))]))])])"""
    #     self.assertTrue(TestAST.test(input,expect,315))
    # def test16(self):
    #     input = """
    #     Class Dog : Animal 
    #     { 
    #         $test()
    #         { 
    #             Var a, b, c : Int = 0, 0, 0;
    #             If (a == b)
    #             {
    #                 b = c;
    #                 Var div, mod, mul : Float = 0.25, 1.2e5, 0.3;
    #                 c = div / mod * mul;
    #             }
    #             Elseif (a != b)
    #             {
    #                 b = 0;
    #                 c = 0;
    #             }
    #             Else
    #             {
    #                 b = -1;
    #                 a = -2;
    #             }
    #         } 
    #     }"""
    #     expect = """Program([ClassDecl(Id(Dog),Id(Animal),[MethodDecl(Id($test),Static,[],Block([VarDecl(Id(a),IntType,IntLit(0)),VarDecl(Id(b),IntType,IntLit(0)),VarDecl(Id(c),IntType,IntLit(0))],[If(BinaryOp(==,a,b),Block([VarDecl(Id(div),FloatType,FloatLit(0.25)),VarDecl(Id(mod),FloatType,FloatLit(120000.0)),VarDecl(Id(mul),FloatType,FloatLit(0.3))],[AssignStmt(Id(b),c),AssignStmt(Id(c),BinaryOp(*,BinaryOp(/,div,mod),mul))]),If(BinaryOp(!=,a,b),Block([],[AssignStmt(Id(b),IntLit(0)),AssignStmt(Id(c),IntLit(0))]),Block([],[AssignStmt(Id(b),UnaryOp(-,IntLit(1))),AssignStmt(Id(a),UnaryOp(-,IntLit(2)))])))]))])])"""
    #     self.assertTrue(TestAST.test(input,expect,316))
    # def test17(self):
    #     input = """
    #     Class Dog : Animal 
    #     { 
    #         $test()
    #         { 
    #             Var a, b, c : Int = 0, 0, 0;
    #             If (a == b)
    #             {
    #                 b = c;
    #                 Var div, mod, mul : Float = 0.25, 1.2e5, 0.3;
    #                 c = div / mod * mul;
    #             }
    #             Elseif (a != b)
    #             {
    #                 b = 0;
    #                 c = 0;
    #             }
    #             Elseif (H == L)
    #             {
    #                 b = -1;
    #                 a = -2;
    #             }
    #         } 
    #     }"""
    #     expect = """Program([ClassDecl(Id(Dog),Id(Animal),[MethodDecl(Id($test),Static,[],Block([VarDecl(Id(a),IntType,IntLit(0)),VarDecl(Id(b),IntType,IntLit(0)),VarDecl(Id(c),IntType,IntLit(0))],[If(BinaryOp(==,a,b),Block([VarDecl(Id(div),FloatType,FloatLit(0.25)),VarDecl(Id(mod),FloatType,FloatLit(120000.0)),VarDecl(Id(mul),FloatType,FloatLit(0.3))],[AssignStmt(Id(b),c),AssignStmt(Id(c),BinaryOp(*,BinaryOp(/,div,mod),mul))]),If(BinaryOp(!=,a,b),Block([],[AssignStmt(Id(b),IntLit(0)),AssignStmt(Id(c),IntLit(0))]),If(BinaryOp(==,H,L),Block([],[AssignStmt(Id(b),UnaryOp(-,IntLit(1))),AssignStmt(Id(a),UnaryOp(-,IntLit(2)))]))))]))])])"""
    #     self.assertTrue(TestAST.test(input,expect,317))
    # def test18(self):
    #     input = """
    #     Class Dog : Animal 
    #     { 
    #         $test()
    #         { 
    #             Var a, b, c : Int = 0, 0, 0;
    #             If (a == b)
    #             {
    #                 b = c;
    #                 Var div, mod, mul : Float = 0.25, 1.2e5, 0.3;
    #                 c = div / mod * mul;
    #             }
    #         } 
    #     }"""
    #     expect = """Program([ClassDecl(Id(Dog),Id(Animal),[MethodDecl(Id($test),Static,[],Block([VarDecl(Id(a),IntType,IntLit(0)),VarDecl(Id(b),IntType,IntLit(0)),VarDecl(Id(c),IntType,IntLit(0))],[If(BinaryOp(==,a,b),Block([VarDecl(Id(div),FloatType,FloatLit(0.25)),VarDecl(Id(mod),FloatType,FloatLit(120000.0)),VarDecl(Id(mul),FloatType,FloatLit(0.3))],[AssignStmt(Id(b),c),AssignStmt(Id(c),BinaryOp(*,BinaryOp(/,div,mod),mul))]))]))])])"""
    #     self.assertTrue(TestAST.test(input,expect,318))