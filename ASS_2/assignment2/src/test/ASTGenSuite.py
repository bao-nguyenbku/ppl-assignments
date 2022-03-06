# 1912683
# Nguyen Thien Bao
import unittest
from TestUtils import TestAST
from AST import *

class ASTGenSuite(unittest.TestCase):
    def test(self):
        input = """
        Class A {

        }
        Class B {
            foo() { 
                If (a) {
                    a = 4;
                }
                Elseif (b) {
                    a = 3;
                    b = 5;
                    c = 8;
                }
                Elseif (12 == 8) {
                    r = 1;
                    pi = 0.3;
                }
                Elseif (9) {
                    r = 6;
                }
                Else {
                    t = myElse;
                }
            }
        }
        """
        expect = """Program([ClassDecl(Id(A),[]),ClassDecl(Id(B),[MethodDecl(Id(foo),Instance,[],Block([If(Id(a),Block([AssignStmt(Id(a),IntLit(4))]),If(Id(b),Block([AssignStmt(Id(a),IntLit(3)),AssignStmt(Id(b),IntLit(5)),AssignStmt(Id(c),IntLit(8))]),If(BinaryOp(==,IntLit(12),IntLit(8)),Block([AssignStmt(Id(r),IntLit(1)),AssignStmt(Id(pi),FloatLit(0.3))]),If(IntLit(9),Block([AssignStmt(Id(r),IntLit(6))]),Block([AssignStmt(Id(t),Id(myElse))])))))]))])])"""
        self.assertTrue(TestAST.test(input,expect,300))
    def test1(self):
        input = """
        Class Dog { 
            Var r: Float = 0xA001;
            Val $a, $b: Boolean = True, True;
        }"""
        expect = """Program([ClassDecl(Id(Dog),[AttributeDecl(Instance,VarDecl(Id(r),FloatType,IntLit(40961))),AttributeDecl(Static,ConstDecl(Id($a),BoolType,BooleanLit(True))),AttributeDecl(Static,ConstDecl(Id($b),BoolType,BooleanLit(True)))])])"""
        self.assertTrue(TestAST.test(input,expect,301))
    def test2(self):
        input = """
        Class Dog { 
            f() {
                a = b[0][1][2];
            }
        }"""
        expect = """Program([ClassDecl(Id(Dog),[MethodDecl(Id(f),Instance,[],Block([AssignStmt(Id(a),ArrayCell(Id(b),[IntLit(0),IntLit(1),IntLit(2)]))]))])])"""
        self.assertTrue(TestAST.test(input,expect,302))

    def test3(self):
        input = """Class Dog : Animal { main(){} }"""
        expect = """Program([ClassDecl(Id(Dog),Id(Animal),[MethodDecl(Id(main),Instance,[],Block([]))])])"""
        self.assertTrue(TestAST.test(input,expect,303))
    def test4(self):
        input = """Class Dog : Animal { $test(){} main(){} }"""
        expect = """Program([ClassDecl(Id(Dog),Id(Animal),[MethodDecl(Id($test),Static,[],Block([])),MethodDecl(Id(main),Instance,[],Block([]))])])"""
        self.assertTrue(TestAST.test(input,expect,304))
    def test5(self):
        input = """Class Dog : Animal { $test(a, b, c:Int){} }"""
        expect = """Program([ClassDecl(Id(Dog),Id(Animal),[MethodDecl(Id($test),Static,[param(Id(a),IntType),param(Id(b),IntType),param(Id(c),IntType)],Block([]))])])"""
        self.assertTrue(TestAST.test(input,expect,305))
    def test6(self):
        input = """Class Dog : Animal { $test(a, b, c:Int){ Break; Continue; } }"""
        expect = """Program([ClassDecl(Id(Dog),Id(Animal),[MethodDecl(Id($test),Static,[param(Id(a),IntType),param(Id(b),IntType),param(Id(c),IntType)],Block([Break,Continue]))])])"""
        self.assertTrue(TestAST.test(input,expect,306))

    def test7(self):
        input = """
        Class Dog : Animal 
        { 
            $test(a, b, c:Int)
            { 
                Var a: Int; 
                Break; 
                Continue; 
            } 
        }"""
        expect = """Program([ClassDecl(Id(Dog),Id(Animal),[MethodDecl(Id($test),Static,[param(Id(a),IntType),param(Id(b),IntType),param(Id(c),IntType)],Block([VarDecl(Id(a),IntType),Break,Continue]))])])"""
        self.assertTrue(TestAST.test(input,expect,307))
    def test8(self):
        input = """
        Class Dog : Animal 
        { 
            $test(a, b, c:Int)
            { 
                Var a: Int; 
                Var b: Float;
                Var c: String;
                Break; 
                Continue; 
            } 
        }"""
        expect = """Program([ClassDecl(Id(Dog),Id(Animal),[MethodDecl(Id($test),Static,[param(Id(a),IntType),param(Id(b),IntType),param(Id(c),IntType)],Block([VarDecl(Id(a),IntType),VarDecl(Id(b),FloatType),VarDecl(Id(c),StringType),Break,Continue]))])])"""
        self.assertTrue(TestAST.test(input,expect,308))
    def test9(self):
        input = """
        Class Dog : Animal 
        { 
            $test()
            { 
                Var ast, bdafs, cdadsas: Int; 
                Break; 
                Continue; 
            } 
        }"""
        expect = """Program([ClassDecl(Id(Dog),Id(Animal),[MethodDecl(Id($test),Static,[],Block([VarDecl(Id(ast),IntType),VarDecl(Id(bdafs),IntType),VarDecl(Id(cdadsas),IntType),Break,Continue]))])])"""
        self.assertTrue(TestAST.test(input,expect,309))
    def test10(self):
        input = """
        Class Dog : Animal 
        { 
            Val $a : String;
            Var b, $c: Int;
            $test()
            { 
                Var ast, bdafs, cdadsas: Int; 
                Val bv : Float;
                Break; 
                Continue; 
            } 
        }"""
        expect = """Program([ClassDecl(Id(Dog),Id(Animal),[AttributeDecl(Static,ConstDecl(Id($a),StringType,None)),AttributeDecl(Instance,VarDecl(Id(b),IntType)),AttributeDecl(Static,VarDecl(Id($c),IntType)),MethodDecl(Id($test),Static,[],Block([VarDecl(Id(ast),IntType),VarDecl(Id(bdafs),IntType),VarDecl(Id(cdadsas),IntType),ConstDecl(Id(bv),FloatType,None),Break,Continue]))])])"""
        self.assertTrue(TestAST.test(input,expect,310))
    def test11(self):
        input = """
        Class Dog : Animal 
        { 
            Val $a : String;
            Var b, $c: Int;
            $test()
            { 
                Var ast, bdafs, cdadsas: Int; 
                Val bv : Float;
                Break; 
                Continue; 
            } 
            main(a, b, c : Int)
            {
                Var a : Boolean;
            }
        }"""
        expect = """Program([ClassDecl(Id(Dog),Id(Animal),[AttributeDecl(Static,ConstDecl(Id($a),StringType,None)),AttributeDecl(Instance,VarDecl(Id(b),IntType)),AttributeDecl(Static,VarDecl(Id($c),IntType)),MethodDecl(Id($test),Static,[],Block([VarDecl(Id(ast),IntType),VarDecl(Id(bdafs),IntType),VarDecl(Id(cdadsas),IntType),ConstDecl(Id(bv),FloatType,None),Break,Continue])),MethodDecl(Id(main),Instance,[param(Id(a),IntType),param(Id(b),IntType),param(Id(c),IntType)],Block([VarDecl(Id(a),BoolType)]))])])"""
        self.assertTrue(TestAST.test(input,expect,311))
    def test12(self):
        input = """
        Class Dog : Animal 
        { 
            $test()
            { 
                Var ast, d, c : Int = 1, 5, 7; 
            } 
        }"""
        expect = """Program([ClassDecl(Id(Dog),Id(Animal),[MethodDecl(Id($test),Static,[],Block([VarDecl(Id(ast),IntType,IntLit(1)),VarDecl(Id(d),IntType,IntLit(5)),VarDecl(Id(c),IntType,IntLit(7))]))])])"""
        self.assertTrue(TestAST.test(input,expect,312))
    def test13(self):
        input = """
        Class Dog : Animal 
        { 
            $test()
            { 
                Var ast, d, c : Int = 1, 5, 7; 
                Var a : Boolean = True; 
                Var a : String = "abc";
            } 
            Var c, $d, e, $f : Int = 1, 2, 2, 3;
            Var a, b : Int = 5 - 6 * 7, 6 / 7 + 2;
        }"""
        expect = """Program([ClassDecl(Id(Dog),Id(Animal),[MethodDecl(Id($test),Static,[],Block([VarDecl(Id(ast),IntType,IntLit(1)),VarDecl(Id(d),IntType,IntLit(5)),VarDecl(Id(c),IntType,IntLit(7)),VarDecl(Id(a),BoolType,BooleanLit(True)),VarDecl(Id(a),StringType,StringLit(abc))])),AttributeDecl(Instance,VarDecl(Id(c),IntType,IntLit(1))),AttributeDecl(Static,VarDecl(Id($d),IntType,IntLit(2))),AttributeDecl(Instance,VarDecl(Id(e),IntType,IntLit(2))),AttributeDecl(Static,VarDecl(Id($f),IntType,IntLit(3))),AttributeDecl(Instance,VarDecl(Id(a),IntType,BinaryOp(-,IntLit(5),BinaryOp(*,IntLit(6),IntLit(7))))),AttributeDecl(Instance,VarDecl(Id(b),IntType,BinaryOp(+,BinaryOp(/,IntLit(6),IntLit(7)),IntLit(2))))])])"""
        self.assertTrue(TestAST.test(input,expect,313))
    def test14(self):
        input = """
        Class Dog : Animal 
        { 
            $test()
            { 
                a = 5;
                b = 7;
                c = 5-8/3*8;
            } 
        }"""
        expect = """Program([ClassDecl(Id(Dog),Id(Animal),[MethodDecl(Id($test),Static,[],Block([AssignStmt(Id(a),IntLit(5)),AssignStmt(Id(b),IntLit(7)),AssignStmt(Id(c),BinaryOp(-,IntLit(5),BinaryOp(*,BinaryOp(/,IntLit(8),IntLit(3)),IntLit(8))))]))])])"""
        self.assertTrue(TestAST.test(input,expect,314))
    def test15(self):
        input = """
        Class Dog : Animal 
        { 
            $test()
            { 
                Var a, b, c : Int = 0, 0, 0;
                If (a == b)
                {
                    b = c;
                    Var div, mod, mul : Float = 0.25, 1.2e5, 0.3;
                    c = div / mod * mul;
                }
                Else
                {
                    b = 0;
                    c = 0;
                }
            } 
        }"""
        expect = """Program([ClassDecl(Id(Dog),Id(Animal),[MethodDecl(Id($test),Static,[],Block([VarDecl(Id(a),IntType,IntLit(0)),VarDecl(Id(b),IntType,IntLit(0)),VarDecl(Id(c),IntType,IntLit(0)),If(BinaryOp(==,Id(a),Id(b)),Block([AssignStmt(Id(b),Id(c)),VarDecl(Id(div),FloatType,FloatLit(0.25)),VarDecl(Id(mod),FloatType,FloatLit(120000.0)),VarDecl(Id(mul),FloatType,FloatLit(0.3)),AssignStmt(Id(c),BinaryOp(*,BinaryOp(/,Id(div),Id(mod)),Id(mul)))]),Block([AssignStmt(Id(b),IntLit(0)),AssignStmt(Id(c),IntLit(0))]))]))])])"""
        self.assertTrue(TestAST.test(input,expect,315))
    def test16(self):
        input = """
        Class Dog : Animal 
        { 
            $test()
            { 
                Var a, b, c : Int = 0, 0, 0;
                If (a == b)
                {
                    b = c;
                    Var div, mod, mul : Float = 0.25, 1.2e5, 0.3;
                    c = div / mod * mul;
                }
                Elseif (a != b)
                {
                    b = 0;
                    c = 0;
                }
                Else
                {
                    b = -1;
                    a = -2;
                }
            } 
        }"""
        expect = """Program([ClassDecl(Id(Dog),Id(Animal),[MethodDecl(Id($test),Static,[],Block([VarDecl(Id(a),IntType,IntLit(0)),VarDecl(Id(b),IntType,IntLit(0)),VarDecl(Id(c),IntType,IntLit(0)),If(BinaryOp(==,Id(a),Id(b)),Block([AssignStmt(Id(b),Id(c)),VarDecl(Id(div),FloatType,FloatLit(0.25)),VarDecl(Id(mod),FloatType,FloatLit(120000.0)),VarDecl(Id(mul),FloatType,FloatLit(0.3)),AssignStmt(Id(c),BinaryOp(*,BinaryOp(/,Id(div),Id(mod)),Id(mul)))]),If(BinaryOp(!=,Id(a),Id(b)),Block([AssignStmt(Id(b),IntLit(0)),AssignStmt(Id(c),IntLit(0))]),Block([AssignStmt(Id(b),UnaryOp(-,IntLit(1))),AssignStmt(Id(a),UnaryOp(-,IntLit(2)))])))]))])])"""
        self.assertTrue(TestAST.test(input,expect,316))
    def test17(self):
        input = """
        Class Dog : Animal 
        { 
            $test()
            { 
                Var a, b, c : Int = 0, 0, 0;
                If (a == b)
                {
                    b = c;
                    Var div, mod, mul : Float = 0.25, 1.2e5, 0.3;
                    c = div / mod * mul;
                }
                Elseif (a != b)
                {
                    b = 0;
                    c = 0;
                }
                Elseif (H == L)
                {
                    b = -1;
                    a = -2;
                }
            } 
        }"""
        expect = """Program([ClassDecl(Id(Dog),Id(Animal),[MethodDecl(Id($test),Static,[],Block([VarDecl(Id(a),IntType,IntLit(0)),VarDecl(Id(b),IntType,IntLit(0)),VarDecl(Id(c),IntType,IntLit(0)),If(BinaryOp(==,Id(a),Id(b)),Block([AssignStmt(Id(b),Id(c)),VarDecl(Id(div),FloatType,FloatLit(0.25)),VarDecl(Id(mod),FloatType,FloatLit(120000.0)),VarDecl(Id(mul),FloatType,FloatLit(0.3)),AssignStmt(Id(c),BinaryOp(*,BinaryOp(/,Id(div),Id(mod)),Id(mul)))]),If(BinaryOp(!=,Id(a),Id(b)),Block([AssignStmt(Id(b),IntLit(0)),AssignStmt(Id(c),IntLit(0))]),If(BinaryOp(==,Id(H),Id(L)),Block([AssignStmt(Id(b),UnaryOp(-,IntLit(1))),AssignStmt(Id(a),UnaryOp(-,IntLit(2)))]))))]))])])"""
        self.assertTrue(TestAST.test(input,expect,317))
    def test18(self):
        input = """
        Class Dog : Animal 
        { 
            $test()
            { 
                Var a, b, c : Int = 0, 0, 0;
                If (a == b)
                {
                    b = c;
                    Var div, mod, mul : Float = 0.25, 1.2e5, 0.3;
                    c = div / mod * mul;
                }
            } 
        }"""
        expect = """Program([ClassDecl(Id(Dog),Id(Animal),[MethodDecl(Id($test),Static,[],Block([VarDecl(Id(a),IntType,IntLit(0)),VarDecl(Id(b),IntType,IntLit(0)),VarDecl(Id(c),IntType,IntLit(0)),If(BinaryOp(==,Id(a),Id(b)),Block([AssignStmt(Id(b),Id(c)),VarDecl(Id(div),FloatType,FloatLit(0.25)),VarDecl(Id(mod),FloatType,FloatLit(120000.0)),VarDecl(Id(mul),FloatType,FloatLit(0.3)),AssignStmt(Id(c),BinaryOp(*,BinaryOp(/,Id(div),Id(mod)),Id(mul)))]))]))])])"""
        self.assertTrue(TestAST.test(input,expect,318))
    def test19(self):
        input = """
        Class Dog : Animal 
        { 
            $test()
            { 
                Var a, b, c : Int = 0, 0, 0;
                Var a : Array[Int, 5];
                Var b : Array[Float, 2] = Array(1.2, 5.2);
                Val ab: Array[Float, 5] = Array(1.2, 3.6, 34e5, 23e4, 12.7e-4);
                Var arr: Array[Array[Array[Float, 01], 0x3_23],4];
                Var aduvip : Array[Array[Int, 5], 3] = Array(Array(11,12,13,14,15),Array(6,7,8,9,10),Array(1,2,3,4,5));
            } 
        }"""
        expect = """Program([ClassDecl(Id(Dog),Id(Animal),[MethodDecl(Id($test),Static,[],Block([VarDecl(Id(a),IntType,IntLit(0)),VarDecl(Id(b),IntType,IntLit(0)),VarDecl(Id(c),IntType,IntLit(0)),VarDecl(Id(a),ArrayType(5,IntType)),VarDecl(Id(b),ArrayType(2,FloatType),[FloatLit(1.2),FloatLit(5.2)]),ConstDecl(Id(ab),ArrayType(5,FloatType),[FloatLit(1.2),FloatLit(3.6),FloatLit(3400000.0),FloatLit(230000.0),FloatLit(0.00127)]),VarDecl(Id(arr),ArrayType(4,ArrayType(803,ArrayType(1,FloatType)))),VarDecl(Id(aduvip),ArrayType(3,ArrayType(5,IntType)),[[IntLit(11),IntLit(12),IntLit(13),IntLit(14),IntLit(15)],[IntLit(6),IntLit(7),IntLit(8),IntLit(9),IntLit(10)],[IntLit(1),IntLit(2),IntLit(3),IntLit(4),IntLit(5)]])]))])])"""
        self.assertTrue(TestAST.test(input,expect,319))
    def test20(self):
        input = """
        Class Dog : Animal 
        { 
            $test()
            { 
                a[1] = 2;
                a[1][2][3][4] = 1 + 2 - 3 * 4 / 5;
            } 
        }"""
        expect = """Program([ClassDecl(Id(Dog),Id(Animal),[MethodDecl(Id($test),Static,[],Block([AssignStmt(ArrayCell(Id(a),[IntLit(1)]),IntLit(2)),AssignStmt(ArrayCell(Id(a),[IntLit(1),IntLit(2),IntLit(3),IntLit(4)]),BinaryOp(-,BinaryOp(+,IntLit(1),IntLit(2)),BinaryOp(/,BinaryOp(*,IntLit(3),IntLit(4)),IntLit(5))))]))])])"""
        self.assertTrue(TestAST.test(input,expect,320))
    def test21(self):
        input = """
        Class Dog : Animal 
        { 
            $test()
            { 
                Player::$name = "Hieu";
                a::$c = "Henry" +. "Le";
            } 
        }"""
        expect = """Program([ClassDecl(Id(Dog),Id(Animal),[MethodDecl(Id($test),Static,[],Block([AssignStmt(FieldAccess(Id(Player),Id($name)),StringLit(Hieu)),AssignStmt(FieldAccess(Id(a),Id($c)),BinaryOp(+.,StringLit(Henry),StringLit(Le)))]))])])"""
        self.assertTrue(TestAST.test(input,expect,321))
    def test22(self):
        input = """
            Class Dog: Animal {
                $gaugau() {
                    a = b[7][2];
                    c[2][3] = d;
                }
            }
            """
        expect = """Program([ClassDecl(Id(Dog),Id(Animal),[MethodDecl(Id($gaugau),Static,[],Block([AssignStmt(Id(a),ArrayCell(Id(b),[IntLit(7),IntLit(2)])),AssignStmt(ArrayCell(Id(c),[IntLit(2),IntLit(3)]),Id(d))]))])])"""
        self.assertTrue(TestAST.test(input,expect,322))
    def test23(self):
        input = """
            Class Dog: Animal { }
            Class Snake: De { }
            Class butterfly {
                __str__() {
                    Var a, b, c, d, e: Int = 0,0,0,0,0;
                    Val a,b,c,d,e: Int;
                }
            }
            """
        expect = """Program([ClassDecl(Id(Dog),Id(Animal),[]),ClassDecl(Id(Snake),Id(De),[]),ClassDecl(Id(butterfly),[MethodDecl(Id(__str__),Instance,[],Block([VarDecl(Id(a),IntType,IntLit(0)),VarDecl(Id(b),IntType,IntLit(0)),VarDecl(Id(c),IntType,IntLit(0)),VarDecl(Id(d),IntType,IntLit(0)),VarDecl(Id(e),IntType,IntLit(0)),ConstDecl(Id(a),IntType,None),ConstDecl(Id(b),IntType,None),ConstDecl(Id(c),IntType,None),ConstDecl(Id(d),IntType,None),ConstDecl(Id(e),IntType,None)]))])])"""
        self.assertTrue(TestAST.test(input,expect,323))
    def test24(self):
        input = """ 
            Class MeowMeow: Dog {
                Var b: Int;
                Var $a, c, d: Float = .e4, 2., 78.9;
                Var a: Array[Float, 5] = Array(1.2, 3.6, 34e5, 23e4, 12.7e4);
            }
            """
        expect = """Program([ClassDecl(Id(MeowMeow),Id(Dog),[AttributeDecl(Instance,VarDecl(Id(b),IntType)),AttributeDecl(Static,VarDecl(Id($a),FloatType,FloatLit(0.0))),AttributeDecl(Instance,VarDecl(Id(c),FloatType,FloatLit(2.0))),AttributeDecl(Instance,VarDecl(Id(d),FloatType,FloatLit(78.9))),AttributeDecl(Instance,VarDecl(Id(a),ArrayType(5,FloatType),[FloatLit(1.2),FloatLit(3.6),FloatLit(3400000.0),FloatLit(230000.0),FloatLit(127000.0)]))])])"""
        self.assertTrue(TestAST.test(input,expect,324))
    def test25(self):
        input = """ 
            Class MeowMeow: Dog {
                Var b: Int;
                Var $a, c, d: Float = .e4, 2., 78.9;
                Var a: Array[Float, 5] = Array(1.2, 3.6, 34e5, 23e4, 12.7e4);
                function (a, b, c: Int) {
                    Foreach (a In b .. c + 1) {
                        Return Self.method() + a[b];
                    }
                }
            }
            """
        expect = """Program([ClassDecl(Id(MeowMeow),Id(Dog),[AttributeDecl(Instance,VarDecl(Id(b),IntType)),AttributeDecl(Static,VarDecl(Id($a),FloatType,FloatLit(0.0))),AttributeDecl(Instance,VarDecl(Id(c),FloatType,FloatLit(2.0))),AttributeDecl(Instance,VarDecl(Id(d),FloatType,FloatLit(78.9))),AttributeDecl(Instance,VarDecl(Id(a),ArrayType(5,FloatType),[FloatLit(1.2),FloatLit(3.6),FloatLit(3400000.0),FloatLit(230000.0),FloatLit(127000.0)])),MethodDecl(Id(function),Instance,[param(Id(a),IntType),param(Id(b),IntType),param(Id(c),IntType)],Block([For(Id(a),Id(b),BinaryOp(+,Id(c),IntLit(1)),IntLit(1),Block([Return(BinaryOp(+,CallExpr(Self(),Id(method),[]),ArrayCell(Id(a),[Id(b)])))])])]))])])"""
        self.assertTrue(TestAST.test(input,expect,325))

    def test26(self):
        input = """
        Class Dog { Val d,b: Int = 9, 5;}"""
        expect = """Program([ClassDecl(Id(Dog),[AttributeDecl(Instance,ConstDecl(Id(d),IntType,IntLit(9))),AttributeDecl(Instance,ConstDecl(Id(b),IntType,IntLit(5)))])])"""
        self.assertTrue(TestAST.test(input,expect,326))
    def test27(self):
        input = """
        Class Dog 
        { 
            Val d,b: Int = 9, 5;
            main()
            {
                Player::$setName("Henry");
                Var player: String = Player::$getName();
                Player::$age = 22;
                Player::$Move(0,1,0);
            }
        }"""
        expect = """Program([ClassDecl(Id(Dog),[AttributeDecl(Instance,ConstDecl(Id(d),IntType,IntLit(9))),AttributeDecl(Instance,ConstDecl(Id(b),IntType,IntLit(5))),MethodDecl(Id(main),Instance,[],Block([Call(Id(Player),Id($setName),[StringLit(Henry)]),VarDecl(Id(player),StringType,CallExpr(Id(Player),Id($getName),[])),AssignStmt(FieldAccess(Id(Player),Id($age)),IntLit(22)),Call(Id(Player),Id($Move),[IntLit(0),IntLit(1),IntLit(0)])]))])])"""
        self.assertTrue(TestAST.test(input,expect,327))
    def test28(self):
        input = """
        Class Dog 
        { 
            Val d,b: Int = 9, 5;
            Var c,d: Float = .2e5, 0.5;
            main()
            {
            }
            Val d,b: Int = 9, 5;
            Var c,d: Float = .2e5, 0.5;
            main()
            {
            }
            Val d,b: Int = 9, 5;
            Var c,d: Float = .2e5, 0.5;
            main()
            {
            }
            Val d,b: Int = 9, 5;
            Var c,d: Float = .2e5, 0.5;
            main()
            {
            }
            main()
            {
            }
            main()
            {
            }
            main()
            {
            }
        }"""
        expect = """Program([ClassDecl(Id(Dog),[AttributeDecl(Instance,ConstDecl(Id(d),IntType,IntLit(9))),AttributeDecl(Instance,ConstDecl(Id(b),IntType,IntLit(5))),AttributeDecl(Instance,VarDecl(Id(c),FloatType,FloatLit(20000.0))),AttributeDecl(Instance,VarDecl(Id(d),FloatType,FloatLit(0.5))),MethodDecl(Id(main),Instance,[],Block([])),AttributeDecl(Instance,ConstDecl(Id(d),IntType,IntLit(9))),AttributeDecl(Instance,ConstDecl(Id(b),IntType,IntLit(5))),AttributeDecl(Instance,VarDecl(Id(c),FloatType,FloatLit(20000.0))),AttributeDecl(Instance,VarDecl(Id(d),FloatType,FloatLit(0.5))),MethodDecl(Id(main),Instance,[],Block([])),AttributeDecl(Instance,ConstDecl(Id(d),IntType,IntLit(9))),AttributeDecl(Instance,ConstDecl(Id(b),IntType,IntLit(5))),AttributeDecl(Instance,VarDecl(Id(c),FloatType,FloatLit(20000.0))),AttributeDecl(Instance,VarDecl(Id(d),FloatType,FloatLit(0.5))),MethodDecl(Id(main),Instance,[],Block([])),AttributeDecl(Instance,ConstDecl(Id(d),IntType,IntLit(9))),AttributeDecl(Instance,ConstDecl(Id(b),IntType,IntLit(5))),AttributeDecl(Instance,VarDecl(Id(c),FloatType,FloatLit(20000.0))),AttributeDecl(Instance,VarDecl(Id(d),FloatType,FloatLit(0.5))),MethodDecl(Id(main),Instance,[],Block([])),MethodDecl(Id(main),Instance,[],Block([])),MethodDecl(Id(main),Instance,[],Block([])),MethodDecl(Id(main),Instance,[],Block([]))])])"""
        self.assertTrue(TestAST.test(input,expect,328))
    def test29(self):
        input = """
        Class Dog 
        { 
            Var a : Int;
            Val b : Int;
        }"""
        expect = """Program([ClassDecl(Id(Dog),[AttributeDecl(Instance,VarDecl(Id(a),IntType)),AttributeDecl(Instance,ConstDecl(Id(b),IntType,None))])])"""
        self.assertTrue(TestAST.test(input,expect,329))
    def test30(self):
        input = """
            Class Dog { 
            Var r: Float = 0xA001;
            Val $a, $b: Boolean = True, True;
            }"""
        expect = """Program([ClassDecl(Id(Dog),[AttributeDecl(Instance,VarDecl(Id(r),FloatType,IntLit(40961))),AttributeDecl(Static,ConstDecl(Id($a),BoolType,BooleanLit(True))),AttributeDecl(Static,ConstDecl(Id($b),BoolType,BooleanLit(True)))])])"""
        self.assertTrue(TestAST.test(input,expect,330))
    def test31(self):
        input = """
            Class A: B {
                Var a: String = "Hello";
                main() {
                    myC.f();
                    a = myB.f();
                    Return Self.b;
                }
            }
            """
        expect = """Program([ClassDecl(Id(A),Id(B),[AttributeDecl(Instance,VarDecl(Id(a),StringType,StringLit(Hello))),MethodDecl(Id(main),Instance,[],Block([Call(Id(myC),Id(f),[]),AssignStmt(Id(a),CallExpr(Id(myB),Id(f),[])),Return(FieldAccess(Self(),Id(b)))]))])])"""
        self.assertTrue(TestAST.test(input,expect,331))
    def test32(self):
        input = """
        Class A: B {
            Var a: String = "Hello";
            Constructor(a,b,c: Float) {
                Return a[1][2][3] + b[1][3][4];
            }
            Destructor() {
                STD::$delete();
            }
        }"""
        expect = """Program([ClassDecl(Id(A),Id(B),[AttributeDecl(Instance,VarDecl(Id(a),StringType,StringLit(Hello))),MethodDecl(Id(Constructor),Instance,[param(Id(a),FloatType),param(Id(b),FloatType),param(Id(c),FloatType)],Block([Return(BinaryOp(+,ArrayCell(Id(a),[IntLit(1),IntLit(2),IntLit(3)]),ArrayCell(Id(b),[IntLit(1),IntLit(3),IntLit(4)])))])),MethodDecl(Id(Destructor),Instance,[],Block([Call(Id(STD),Id($delete),[])]))])])"""
        self.assertTrue(TestAST.test(input,expect,332))
    def test33(self):
        input = """
            Class Dog: Cat {
                Val a: Int = 0x6A;
                f() {
                    If (a) {
                        Foreach (i In 0 .. 100 By t <= 0b1) {
                            If (i > 10) {
                                If (y) {
                                    Return;
                                }
                                Elseif (b) {
                                    Break;
                                }
                            }
                        }
                    }
                }
            }
            """
        expect = """Program([ClassDecl(Id(Dog),Id(Cat),[AttributeDecl(Instance,ConstDecl(Id(a),IntType,IntLit(106))),MethodDecl(Id(f),Instance,[],Block([If(Id(a),Block([For(Id(i),IntLit(0),IntLit(100),BinaryOp(<=,Id(t),IntLit(1)),Block([If(BinaryOp(>,Id(i),IntLit(10)),Block([If(Id(y),Block([Return()]),If(Id(b),Block([Break])))]))])])]))]))])])"""
        self.assertTrue(TestAST.test(input,expect,333))
    def test34(self):
        input = """
            Class Program {
                main() {
                    a = New B();
                }
            }
            Class Main {
                main() {
                    Return a;
                }
            }
            """
        expect = """Program([ClassDecl(Id(Program),[MethodDecl(Id(main),Static,[],Block([AssignStmt(Id(a),NewExpr(Id(B),[]))]))]),ClassDecl(Id(Main),[MethodDecl(Id(main),Instance,[],Block([Return(Id(a))]))])])"""
        self.assertTrue(TestAST.test(input,expect,334))
    def test35(self):
        input = """
            Class Program {
                main() {
                    If (a < b) {
                        Return;
                    }
                }
                main(a, b, c: Int; e, f: Float) {
                    Return a + b + c - e - f;
                }
            }
            """
        expect = """Program([ClassDecl(Id(Program),[MethodDecl(Id(main),Static,[],Block([If(BinaryOp(<,Id(a),Id(b)),Block([Return()]))])),MethodDecl(Id(main),Instance,[param(Id(a),IntType),param(Id(b),IntType),param(Id(c),IntType),param(Id(e),FloatType),param(Id(f),FloatType)],Block([Return(BinaryOp(-,BinaryOp(-,BinaryOp(+,BinaryOp(+,Id(a),Id(b)),Id(c)),Id(e)),Id(f)))]))])])"""
        self.assertTrue(TestAST.test(input,expect,335))
    def test36(self):
        input = """
            Class A {
                main() {
                    Program.main();
                    Val a: Int;
                    Val b: Float = .2e6;
                    Lang::$e();
                }
            }
            """
        expect = """Program([ClassDecl(Id(A),[MethodDecl(Id(main),Instance,[],Block([Call(Id(Program),Id(main),[]),ConstDecl(Id(a),IntType,None),ConstDecl(Id(b),FloatType,FloatLit(200000.0)),Call(Id(Lang),Id($e),[])]))])])"""
        self.assertTrue(TestAST.test(input,expect,336))
    def test37(self):
        input = """
            Class Bname {
                f() {
                    If (a) {

                    }
                    Elseif (b) {
                        If (d + 2 == 7) {

                        }
                        Elseif (b - 9 < 0) {

                        }
                        Else {
                            Return;
                        }
                    }
                    Elseif (c < 8) {

                    }
                    Else {
                        If (d) {
                            a = b;
                        }
                    }
                }
            }
            """
        expect = """Program([ClassDecl(Id(Bname),[MethodDecl(Id(f),Instance,[],Block([If(Id(a),Block([]),If(Id(b),Block([If(BinaryOp(==,BinaryOp(+,Id(d),IntLit(2)),IntLit(7)),Block([]),If(BinaryOp(<,BinaryOp(-,Id(b),IntLit(9)),IntLit(0)),Block([]),Block([Return()])))]),If(BinaryOp(<,Id(c),IntLit(8)),Block([]),Block([If(Id(d),Block([AssignStmt(Id(a),Id(b))]))]))))]))])])"""
        self.assertTrue(TestAST.test(input,expect,337))
    def test38(self):
        input = """
        Class QuickSort : Sort
        {
            $partition(arr : Array[Int, 10]; start, end : Int)
            {
                Var pivot : Int = arr[start];
                Var count : Int = 0;
                Foreach (i In start + 1 .. end + 1 By 1)
                {
                    If (arr[i] <= pivot)
                    {
                        count = count + 1;
                    }
                }
                Var pivotIndex : Int = start + count;
                Swap::$swap(arr[pivotIndex], arr[start]);
                Var i : Int = start;
                Var j : Int = end;
                Foreach (k In 1 .. 100)
                {
                    If (arr[i] <= pivot)
                    {
                        i = i + 1;
                    }
                    If (arr[j] > pivot)
                    {
                        j = j - 1;
                    }
                    If (!((i < pivotIndex) && (j > pivotIndex)))
                    {
                        Break;
                    }
                    Else
                    {
                        i = i + 1;
                        j = j - 1;
                        Swap::$swap(arr[i], arr[j]);
                    }
                }
                Return pivotIndex;
            }
            $quickSort(arr : Array[Int, 10]; start, end : Int)
            {
                If (start >= end)
                {
                    Return ;
                }
                Var p : Int = QuickSort::$partition(arr, start, end);
                QuickSort::$quickSort(arr, start, p - 1);
                QuickSort::$quickSort(arr, p + 1, end);
            }
            $print()
            {
                Var arr : Array[Int, 10] = Array(9,3,4,2,1,8,4,9,5,6);
                Var n : Int = 6;
                QuickSort::$quickSort(arr, 0, n - 1);
                Foreach (i In 0 .. n By 1)
                {
                    System::$print(arr[i]);
                }
                Return 0;
            }
        }"""
        expect = """Program([ClassDecl(Id(QuickSort),Id(Sort),[MethodDecl(Id($partition),Static,[param(Id(arr),ArrayType(10,IntType)),param(Id(start),IntType),param(Id(end),IntType)],Block([VarDecl(Id(pivot),IntType,ArrayCell(Id(arr),[Id(start)])),VarDecl(Id(count),IntType,IntLit(0)),For(Id(i),BinaryOp(+,Id(start),IntLit(1)),BinaryOp(+,Id(end),IntLit(1)),IntLit(1),Block([If(BinaryOp(<=,ArrayCell(Id(arr),[Id(i)]),Id(pivot)),Block([AssignStmt(Id(count),BinaryOp(+,Id(count),IntLit(1)))]))])]),VarDecl(Id(pivotIndex),IntType,BinaryOp(+,Id(start),Id(count))),Call(Id(Swap),Id($swap),[ArrayCell(Id(arr),[Id(pivotIndex)]),ArrayCell(Id(arr),[Id(start)])]),VarDecl(Id(i),IntType,Id(start)),VarDecl(Id(j),IntType,Id(end)),For(Id(k),IntLit(1),IntLit(100),IntLit(1),Block([If(BinaryOp(<=,ArrayCell(Id(arr),[Id(i)]),Id(pivot)),Block([AssignStmt(Id(i),BinaryOp(+,Id(i),IntLit(1)))])),If(BinaryOp(>,ArrayCell(Id(arr),[Id(j)]),Id(pivot)),Block([AssignStmt(Id(j),BinaryOp(-,Id(j),IntLit(1)))])),If(UnaryOp(!,BinaryOp(&&,BinaryOp(<,Id(i),Id(pivotIndex)),BinaryOp(>,Id(j),Id(pivotIndex)))),Block([Break]),Block([AssignStmt(Id(i),BinaryOp(+,Id(i),IntLit(1))),AssignStmt(Id(j),BinaryOp(-,Id(j),IntLit(1))),Call(Id(Swap),Id($swap),[ArrayCell(Id(arr),[Id(i)]),ArrayCell(Id(arr),[Id(j)])])]))])]),Return(Id(pivotIndex))])),MethodDecl(Id($quickSort),Static,[param(Id(arr),ArrayType(10,IntType)),param(Id(start),IntType),param(Id(end),IntType)],Block([If(BinaryOp(>=,Id(start),Id(end)),Block([Return()])),VarDecl(Id(p),IntType,CallExpr(Id(QuickSort),Id($partition),[Id(arr),Id(start),Id(end)])),Call(Id(QuickSort),Id($quickSort),[Id(arr),Id(start),BinaryOp(-,Id(p),IntLit(1))]),Call(Id(QuickSort),Id($quickSort),[Id(arr),BinaryOp(+,Id(p),IntLit(1)),Id(end)])])),MethodDecl(Id($print),Static,[],Block([VarDecl(Id(arr),ArrayType(10,IntType),[IntLit(9),IntLit(3),IntLit(4),IntLit(2),IntLit(1),IntLit(8),IntLit(4),IntLit(9),IntLit(5),IntLit(6)]),VarDecl(Id(n),IntType,IntLit(6)),Call(Id(QuickSort),Id($quickSort),[Id(arr),IntLit(0),BinaryOp(-,Id(n),IntLit(1))]),For(Id(i),IntLit(0),Id(n),IntLit(1),Block([Call(Id(System),Id($print),[ArrayCell(Id(arr),[Id(i)])])])]),Return(IntLit(0))]))])])"""
        self.assertTrue(TestAST.test(input,expect,338))
    def test39(self):
        input = """
            Class SelectionSort {
                swap(xp: Int; yp: Int) {
                    Var temp: Int = xp;
                    xp = yp;
                    yp = temp;
                }
                selectionSort(arr: Array[Int, 100]; n: Int) {
                    Var i, j, min_idx: Int;
                    ##This is comment##
                    Foreach (i In 0 .. n - 1 By 1) {
                        ##Find minimum element in array that hasn't been sorted##
                        min_idx = i;
                        Foreach (j In i+1 .. n By 1) {
                            If (arr[j] < arr[min_idx]) {
                                min_idx = j;
                            }
                        }
                        ##swap minimum element with first element##
                        Self.swap(arr[min_idx], arr[i]);
                    }
                }
            }
            """
        expect = """Program([ClassDecl(Id(SelectionSort),[MethodDecl(Id(swap),Instance,[param(Id(xp),IntType),param(Id(yp),IntType)],Block([VarDecl(Id(temp),IntType,Id(xp)),AssignStmt(Id(xp),Id(yp)),AssignStmt(Id(yp),Id(temp))])),MethodDecl(Id(selectionSort),Instance,[param(Id(arr),ArrayType(100,IntType)),param(Id(n),IntType)],Block([VarDecl(Id(i),IntType),VarDecl(Id(j),IntType),VarDecl(Id(min_idx),IntType),For(Id(i),IntLit(0),BinaryOp(-,Id(n),IntLit(1)),IntLit(1),Block([AssignStmt(Id(min_idx),Id(i)),For(Id(j),BinaryOp(+,Id(i),IntLit(1)),Id(n),IntLit(1),Block([If(BinaryOp(<,ArrayCell(Id(arr),[Id(j)]),ArrayCell(Id(arr),[Id(min_idx)])),Block([AssignStmt(Id(min_idx),Id(j))]))])]),Call(Self(),Id(swap),[ArrayCell(Id(arr),[Id(min_idx)]),ArrayCell(Id(arr),[Id(i)])])])])]))])])"""
        self.assertTrue(TestAST.test(input,expect,339))
    def test40(self):
        input = """
        Class BinarySearch {
            binarySearch(arr: Array[Int, 100]; l: Int; r: Int; x: Int) {
                If (r >= l) {
                    Var mid: Int = l + (r - l) / 2;
                    ## If the element is present at the middle itself ##
                    If (arr[mid] == x) {
                        Return mid;
                    }
            
                    ## If element is smaller than mid, then ##
                    ## it can only be present in left subarray ##
                    If (arr[mid] > x) {
                        Return Self.binarySearch(arr, l, mid - 1, x);
                    }
            
                    ## Else the element can only be present ##
                    ## in right subarray ##
                    Return Self.binarySearch(arr, mid + 1, r, x);
                }
            
                ## We reach here when element is not ##
                ## present in array ##
                Return -1;
            }
        }"""
        expect = """Program([ClassDecl(Id(BinarySearch),[MethodDecl(Id(binarySearch),Instance,[param(Id(arr),ArrayType(100,IntType)),param(Id(l),IntType),param(Id(r),IntType),param(Id(x),IntType)],Block([If(BinaryOp(>=,Id(r),Id(l)),Block([VarDecl(Id(mid),IntType,BinaryOp(+,Id(l),BinaryOp(/,BinaryOp(-,Id(r),Id(l)),IntLit(2)))),If(BinaryOp(==,ArrayCell(Id(arr),[Id(mid)]),Id(x)),Block([Return(Id(mid))])),If(BinaryOp(>,ArrayCell(Id(arr),[Id(mid)]),Id(x)),Block([Return(CallExpr(Self(),Id(binarySearch),[Id(arr),Id(l),BinaryOp(-,Id(mid),IntLit(1)),Id(x)]))])),Return(CallExpr(Self(),Id(binarySearch),[Id(arr),BinaryOp(+,Id(mid),IntLit(1)),Id(r),Id(x)]))])),Return(UnaryOp(-,IntLit(1)))]))])])"""
        self.assertTrue(TestAST.test(input,expect,340))
    def test41(self):
        input = """
            Class Roman {
                convertToRoman(num: Int) {
                    Var lookup: Array[Array[Int, 2], 0x10] = Array(Array(M, 1000), Array(CM, 900), Array(D, 500), Array(CD, 400), Array(C, 100), Array(XC, 90), Array(L, 50), Array(XL, 40), Array(X, 10), Array(IX, 9), Array(V, 5), Array(IV, 4), Array(I, 1));
                    Var roman: String;
                    Foreach (i In 0 .. lookup.length()) {
                        Foreach (num In lookup[i] .. 0) {
                            roman = roman + i;
                            num = num - lookup[i];
                        }
                    }
                    Return roman;
                }
            }
            """
        expect = """Program([ClassDecl(Id(Roman),[MethodDecl(Id(convertToRoman),Instance,[param(Id(num),IntType)],Block([VarDecl(Id(lookup),ArrayType(16,ArrayType(2,IntType)),[[Id(M),IntLit(1000)],[Id(CM),IntLit(900)],[Id(D),IntLit(500)],[Id(CD),IntLit(400)],[Id(C),IntLit(100)],[Id(XC),IntLit(90)],[Id(L),IntLit(50)],[Id(XL),IntLit(40)],[Id(X),IntLit(10)],[Id(IX),IntLit(9)],[Id(V),IntLit(5)],[Id(IV),IntLit(4)],[Id(I),IntLit(1)]]),VarDecl(Id(roman),StringType),For(Id(i),IntLit(0),CallExpr(Id(lookup),Id(length),[]),IntLit(1),Block([For(Id(num),ArrayCell(Id(lookup),[Id(i)]),IntLit(0),IntLit(1),Block([AssignStmt(Id(roman),BinaryOp(+,Id(roman),Id(i))),AssignStmt(Id(num),BinaryOp(-,Id(num),ArrayCell(Id(lookup),[Id(i)])))])])])]),Return(Id(roman))]))])])"""
        self.assertTrue(TestAST.test(input,expect,341))
    def test42(self):
        input = """
            Class B {
                Val a, $b, c, $d: Int = 1 + 2, 4, 0b1, 06;
            }
            """
        expect = """Program([ClassDecl(Id(B),[AttributeDecl(Instance,ConstDecl(Id(a),IntType,BinaryOp(+,IntLit(1),IntLit(2)))),AttributeDecl(Static,ConstDecl(Id($b),IntType,IntLit(4))),AttributeDecl(Instance,ConstDecl(Id(c),IntType,IntLit(1))),AttributeDecl(Static,ConstDecl(Id($d),IntType,IntLit(6)))])])"""
        self.assertTrue(TestAST.test(input,expect,342))
    def test43(self):
        input = """
        Class JumpSearch {
            jumpSearch(arr: Array[Int, 0xAB]; x, n: Int) {
            ## Finding block size to be jumped ##
            Var step: Float = Math.sqrt(n);
        
            ## Finding the block where element is ##
            ## present (if it is present) ##
            Var prev: Int = 0;
            Foreach (i In 1 .. 100) {
                If (arr[STD.min(step, n)-1] < x) {
                    prev = step;
                    step = step + Math.sqrt(n);
                    If (prev >= n) {
                        Return -1;
                    }
                }
            }
        
            ## Doing a linear search for x in block ##
            ## beginning with prev. ##
            Foreach (i In 0 .. x) {
                prev = prev + 1;
                ## If we reached next block or end of ##
                ## array, element is not present. ##
                If (prev == STD.min(step, n)) {
                    Return -1;
                }
            }
            ## If element is found ##
            If (arr[prev] == x) {
                Return prev;
            }
            Return -1;
        }
    }"""
        expect = """Program([ClassDecl(Id(JumpSearch),[MethodDecl(Id(jumpSearch),Instance,[param(Id(arr),ArrayType(171,IntType)),param(Id(x),IntType),param(Id(n),IntType)],Block([VarDecl(Id(step),FloatType,CallExpr(Id(Math),Id(sqrt),[Id(n)])),VarDecl(Id(prev),IntType,IntLit(0)),For(Id(i),IntLit(1),IntLit(100),IntLit(1),Block([If(BinaryOp(<,ArrayCell(Id(arr),[BinaryOp(-,CallExpr(Id(STD),Id(min),[Id(step),Id(n)]),IntLit(1))]),Id(x)),Block([AssignStmt(Id(prev),Id(step)),AssignStmt(Id(step),BinaryOp(+,Id(step),CallExpr(Id(Math),Id(sqrt),[Id(n)]))),If(BinaryOp(>=,Id(prev),Id(n)),Block([Return(UnaryOp(-,IntLit(1)))]))]))])]),For(Id(i),IntLit(0),Id(x),IntLit(1),Block([AssignStmt(Id(prev),BinaryOp(+,Id(prev),IntLit(1))),If(BinaryOp(==,Id(prev),CallExpr(Id(STD),Id(min),[Id(step),Id(n)])),Block([Return(UnaryOp(-,IntLit(1)))]))])]),If(BinaryOp(==,ArrayCell(Id(arr),[Id(prev)]),Id(x)),Block([Return(Id(prev))])),Return(UnaryOp(-,IntLit(1)))]))])])"""
        self.assertTrue(TestAST.test(input,expect,343))
    def test44(self):
        input = """
            Class Factorial {
                Factorial(n: Int) {
                    If (n <= 1) {
                        Return 1;
                    }
                    Return n * Self.Factorial(n - 1);
                }
            }
            """
        expect = """Program([ClassDecl(Id(Factorial),[MethodDecl(Id(Factorial),Instance,[param(Id(n),IntType)],Block([If(BinaryOp(<=,Id(n),IntLit(1)),Block([Return(IntLit(1))])),Return(BinaryOp(*,Id(n),CallExpr(Self(),Id(Factorial),[BinaryOp(-,Id(n),IntLit(1))])))]))])])"""
        self.assertTrue(TestAST.test(input,expect,344))
    def test45(self):
        input = """
            Class Reverse {
                reverse() {
                    IO.input("Enter an integer: ");
                    Foreach (n In n .. 0) {
                        remainder = n % 10;
                        reversed_number = reversed_number * 10 + remainder;
                        n = n / 10;
                    }
                }
                Var n, reminder: Int;
                Var reversed_number: Int = 0;
                get() {
                    Return Self.reversed_number;
                }
            }
            """
        expect = """Program([ClassDecl(Id(Reverse),[MethodDecl(Id(reverse),Instance,[],Block([Call(Id(IO),Id(input),[StringLit(Enter an integer: )]),For(Id(n),Id(n),IntLit(0),IntLit(1),Block([AssignStmt(Id(remainder),BinaryOp(%,Id(n),IntLit(10))),AssignStmt(Id(reversed_number),BinaryOp(+,BinaryOp(*,Id(reversed_number),IntLit(10)),Id(remainder))),AssignStmt(Id(n),BinaryOp(/,Id(n),IntLit(10)))])])])),AttributeDecl(Instance,VarDecl(Id(n),IntType)),AttributeDecl(Instance,VarDecl(Id(reminder),IntType)),AttributeDecl(Instance,VarDecl(Id(reversed_number),IntType,IntLit(0))),MethodDecl(Id(get),Instance,[],Block([Return(FieldAccess(Self(),Id(reversed_number)))]))])])"""
        self.assertTrue(TestAST.test(input,expect,345))
    def test46(self):
        input = """
            Class Max {
                findMax(arr: Array[Int, 100]) {
                    Var maxElement: Int = arr[1];
                    Foreach (i In 2 .. arr.length()) {
                        If (maxElement < arr[i]) {
                            maxElement = arr[i];
                        }
                    }
                    Return maxElement;
                }
            }
            Class Program {
                main() {
                    arr = IO.input("Your array: ");
                    max = New Max();
                    Console.print(max.findMax(arr));
                }
            }
            """
        expect = """Program([ClassDecl(Id(Max),[MethodDecl(Id(findMax),Instance,[param(Id(arr),ArrayType(100,IntType))],Block([VarDecl(Id(maxElement),IntType,ArrayCell(Id(arr),[IntLit(1)])),For(Id(i),IntLit(2),CallExpr(Id(arr),Id(length),[]),IntLit(1),Block([If(BinaryOp(<,Id(maxElement),ArrayCell(Id(arr),[Id(i)])),Block([AssignStmt(Id(maxElement),ArrayCell(Id(arr),[Id(i)]))]))])]),Return(Id(maxElement))]))]),ClassDecl(Id(Program),[MethodDecl(Id(main),Static,[],Block([AssignStmt(Id(arr),CallExpr(Id(IO),Id(input),[StringLit(Your array: )])),AssignStmt(Id(max),NewExpr(Id(Max),[])),Call(Id(Console),Id(print),[CallExpr(Id(max),Id(findMax),[Id(arr)])])]))])])"""
        self.assertTrue(TestAST.test(input,expect,346))
    def test47(self):
        input = """
            Class Prime {
                Var i, n: Int;
                Var is_prime: Boolean = True;
                checkPrime(num: Int) {
                    ## 0 and 1 are not prime numbers ##
                    If ((n == 0) || (n == 1)) {
                        is_prime = False;
                    }

                    ## loop to check if n is prime ##
                    Foreach (i In 2 .. n/2) {
                        If (n % i == 0) {
                            is_prime = false;
                            Break;
                        }
                    }

                    If (is_prime) {
                        Return True;
                    }
                    Else {
                        Return False;
                    }
                }
            }
            """
        expect = """Program([ClassDecl(Id(Prime),[AttributeDecl(Instance,VarDecl(Id(i),IntType)),AttributeDecl(Instance,VarDecl(Id(n),IntType)),AttributeDecl(Instance,VarDecl(Id(is_prime),BoolType,BooleanLit(True))),MethodDecl(Id(checkPrime),Instance,[param(Id(num),IntType)],Block([If(BinaryOp(||,BinaryOp(==,Id(n),IntLit(0)),BinaryOp(==,Id(n),IntLit(1))),Block([AssignStmt(Id(is_prime),BooleanLit(False))])),For(Id(i),IntLit(2),BinaryOp(/,Id(n),IntLit(2)),IntLit(1),Block([If(BinaryOp(==,BinaryOp(%,Id(n),Id(i)),IntLit(0)),Block([AssignStmt(Id(is_prime),Id(false)),Break]))])]),If(Id(is_prime),Block([Return(BooleanLit(True))]),Block([Return(BooleanLit(False))]))]))])])"""
        self.assertTrue(TestAST.test(input,expect,347))
    def test48(self):
        input = """
            Class Fibonacci {
                ## program to generate fibonacci series up to n terms ##
                ## take input from the user ##
                $fibo() {
                    Val number: Int = Lib.parseInt("Enter the number of terms: ");
                    Var n1, n2: Int = 0, 1;
                    Var nextTerm: Int;
                    console.log("Fibonacci Series:");
                    Foreach (i In 1 .. number) {
                        console.log(n1);
                        nextTerm = n1 + n2;
                        n1 = n2;
                        n2 = nextTerm;
                    }
                }
            }
            """
        expect = """Program([ClassDecl(Id(Fibonacci),[MethodDecl(Id($fibo),Static,[],Block([ConstDecl(Id(number),IntType,CallExpr(Id(Lib),Id(parseInt),[StringLit(Enter the number of terms: )])),VarDecl(Id(n1),IntType,IntLit(0)),VarDecl(Id(n2),IntType,IntLit(1)),VarDecl(Id(nextTerm),IntType),Call(Id(console),Id(log),[StringLit(Fibonacci Series:)]),For(Id(i),IntLit(1),Id(number),IntLit(1),Block([Call(Id(console),Id(log),[Id(n1)]),AssignStmt(Id(nextTerm),BinaryOp(+,Id(n1),Id(n2))),AssignStmt(Id(n1),Id(n2)),AssignStmt(Id(n2),Id(nextTerm))])])]))])])"""
        self.assertTrue(TestAST.test(input,expect,348))
    def test49(self):
        input = """
            Class Program {
                main() {
                    LeapYear::$check(1990);
                }
            }
            Class LeapYear {
                $check(year: Int) {
                    Var year: Int;
                    If (year % 4 == 0) {
                        If (year % 100 == 0) {
                            If (year % 400 == 0) {
                                console.log(year, "is a leap year");
                            }
                            Else {
                                console.log(year, "is not a leap year");
                            }
                        }
                        Else {
                            console.log(year, "is a leap year");
                        }
                    }
                    Else {
                        console.log(year, "is not a leap year");
                    }
                }
            }
            """
        expect = """Program([ClassDecl(Id(Program),[MethodDecl(Id(main),Static,[],Block([Call(Id(LeapYear),Id($check),[IntLit(1990)])]))]),ClassDecl(Id(LeapYear),[MethodDecl(Id($check),Static,[param(Id(year),IntType)],Block([VarDecl(Id(year),IntType),If(BinaryOp(==,BinaryOp(%,Id(year),IntLit(4)),IntLit(0)),Block([If(BinaryOp(==,BinaryOp(%,Id(year),IntLit(100)),IntLit(0)),Block([If(BinaryOp(==,BinaryOp(%,Id(year),IntLit(400)),IntLit(0)),Block([Call(Id(console),Id(log),[Id(year),StringLit(is a leap year)])]),Block([Call(Id(console),Id(log),[Id(year),StringLit(is not a leap year)])]))]),Block([Call(Id(console),Id(log),[Id(year),StringLit(is a leap year)])]))]),Block([Call(Id(console),Id(log),[Id(year),StringLit(is not a leap year)])]))]))])])"""
        self.assertTrue(TestAST.test(input,expect,349))
    def test50(self):
        input = """
            Class BubbleSort {
                Var arr: Array[Int, 1000000];
                $sort() {
                    Var i, j: Int;
                    Foreach (i In 0 .. n - 1) {
                        Foreach (j In 0 .. n - i - 1) {
                            If (arr[j] > arr[j+1]) {
                                Std.swap(arr[j], arr[j+1]);
                            }
                        }
                    }
                }
                set(arr: Array[Int, 1000000]) {
                    Self.arr = arr;
                }
            }
            """
        expect = """Program([ClassDecl(Id(BubbleSort),[AttributeDecl(Instance,VarDecl(Id(arr),ArrayType(1000000,IntType))),MethodDecl(Id($sort),Static,[],Block([VarDecl(Id(i),IntType),VarDecl(Id(j),IntType),For(Id(i),IntLit(0),BinaryOp(-,Id(n),IntLit(1)),IntLit(1),Block([For(Id(j),IntLit(0),BinaryOp(-,BinaryOp(-,Id(n),Id(i)),IntLit(1)),IntLit(1),Block([If(BinaryOp(>,ArrayCell(Id(arr),[Id(j)]),ArrayCell(Id(arr),[BinaryOp(+,Id(j),IntLit(1))])),Block([Call(Id(Std),Id(swap),[ArrayCell(Id(arr),[Id(j)]),ArrayCell(Id(arr),[BinaryOp(+,Id(j),IntLit(1))])])]))])])])])])),MethodDecl(Id(set),Instance,[param(Id(arr),ArrayType(1000000,IntType))],Block([AssignStmt(FieldAccess(Self(),Id(arr)),Id(arr))]))])])"""
        self.assertTrue(TestAST.test(input,expect,350))
    def test51(self):
        input = """
            Class Program {
                main() {

                }
            }
            Class NotProgram {
                main() {
                    a[1 + 2][b.method()] = Name::$setName();
                }
            }
            """
        expect = """Program([ClassDecl(Id(Program),[MethodDecl(Id(main),Static,[],Block([]))]),ClassDecl(Id(NotProgram),[MethodDecl(Id(main),Instance,[],Block([AssignStmt(ArrayCell(Id(a),[BinaryOp(+,IntLit(1),IntLit(2)),CallExpr(Id(b),Id(method),[])]),CallExpr(Id(Name),Id($setName),[]))]))])])"""
        self.assertTrue(TestAST.test(input,expect,351))
    def test52(self):
        input = """
            Class Program {
                main(a, b, c, d: Int) {
                    Var str: Array[String, 200];
                    Var wrd: Array[String, 20];
                    Var i, j, strLen, wrdLen, tmp: Int;
                    Var chk: Int = 0;
                    std.gets(str);
                    strLen = std.strlen(str);
                    wrdLen = std.strlen(wrd);
                    Foreach (i In 0 .. strLen) {
                        tmp = i;
                        Foreach (j In 0 .. wrdLen) {
                            If(str[i]==wrd[j]) {
                                i = i + 1;
                            }
                        }
                        chk = i-tmp;
                        If(chk==wrdLen)
                        {
                            i = tmp;
                            Foreach(j In i .. (strLen-wrdLen)) {
                                str[j] = str[j+wrdLen];
                            }
                            strLen = strLen-wrdLen;
                            str[j] = "\\\\0";
                        }
                    }
                }
            }
            """
        expect = """Program([ClassDecl(Id(Program),[MethodDecl(Id(main),Instance,[param(Id(a),IntType),param(Id(b),IntType),param(Id(c),IntType),param(Id(d),IntType)],Block([VarDecl(Id(str),ArrayType(200,StringType)),VarDecl(Id(wrd),ArrayType(20,StringType)),VarDecl(Id(i),IntType),VarDecl(Id(j),IntType),VarDecl(Id(strLen),IntType),VarDecl(Id(wrdLen),IntType),VarDecl(Id(tmp),IntType),VarDecl(Id(chk),IntType,IntLit(0)),Call(Id(std),Id(gets),[Id(str)]),AssignStmt(Id(strLen),CallExpr(Id(std),Id(strlen),[Id(str)])),AssignStmt(Id(wrdLen),CallExpr(Id(std),Id(strlen),[Id(wrd)])),For(Id(i),IntLit(0),Id(strLen),IntLit(1),Block([AssignStmt(Id(tmp),Id(i)),For(Id(j),IntLit(0),Id(wrdLen),IntLit(1),Block([If(BinaryOp(==,ArrayCell(Id(str),[Id(i)]),ArrayCell(Id(wrd),[Id(j)])),Block([AssignStmt(Id(i),BinaryOp(+,Id(i),IntLit(1)))]))])]),AssignStmt(Id(chk),BinaryOp(-,Id(i),Id(tmp))),If(BinaryOp(==,Id(chk),Id(wrdLen)),Block([AssignStmt(Id(i),Id(tmp)),For(Id(j),Id(i),BinaryOp(-,Id(strLen),Id(wrdLen)),IntLit(1),Block([AssignStmt(ArrayCell(Id(str),[Id(j)]),ArrayCell(Id(str),[BinaryOp(+,Id(j),Id(wrdLen))]))])]),AssignStmt(Id(strLen),BinaryOp(-,Id(strLen),Id(wrdLen))),AssignStmt(ArrayCell(Id(str),[Id(j)]),StringLit(\\\\0))]))])])]))])])"""
        self.assertTrue(TestAST.test(input,expect,352))
    def test53(self):
        input = """
            Class Grade {
                grading() {
                    Var i: Int;
                    Var mark, sum, avg: Float;
                    sum = 0;
                    console.log("Enter Marks obtained in 5 Subjects: ");
                    Foreach(i In 0 .. 5 By 1)
                    {
                        std.cin(mark);
                        sum = sum + mark;
                    }
                    avg = sum / 5;
                    std.cout("\\nGrade = ");
                    If((avg>=91) && (avg<=100))
                    {    std.cout("A1"); }
                    Elseif((avg>=81) && (avg<91))
                    {    std.cout("A2"); }
                    Elseif((avg>=71) && (avg<81))
                    {    std.cout("B1"); }
                    Elseif((avg>=61) && (avg<71))
                    {    std.cout("B2"); }
                    Elseif((avg>=51) && (avg<61))
                    {    std.cout("C1"); }
                    Elseif((avg>=41) && (avg<51))
                    {    std.cout("C2"); }
                    Elseif((avg>=33) && (avg<41))
                    {    std.cout("D"); }
                    Elseif((avg>=21) && (avg<33))
                    {    std.cout("E1"); }
                    Elseif((avg>=0) && (avg<21))
                    {    std.cout("E2"); }
                    Else
                    {    std.cout("Invalid!"); }
                }
            }
            """
        expect = """Program([ClassDecl(Id(Grade),[MethodDecl(Id(grading),Instance,[],Block([VarDecl(Id(i),IntType),VarDecl(Id(mark),FloatType),VarDecl(Id(sum),FloatType),VarDecl(Id(avg),FloatType),AssignStmt(Id(sum),IntLit(0)),Call(Id(console),Id(log),[StringLit(Enter Marks obtained in 5 Subjects: )]),For(Id(i),IntLit(0),IntLit(5),IntLit(1),Block([Call(Id(std),Id(cin),[Id(mark)]),AssignStmt(Id(sum),BinaryOp(+,Id(sum),Id(mark)))])]),AssignStmt(Id(avg),BinaryOp(/,Id(sum),IntLit(5))),Call(Id(std),Id(cout),[StringLit(\\nGrade = )]),If(BinaryOp(&&,BinaryOp(>=,Id(avg),IntLit(91)),BinaryOp(<=,Id(avg),IntLit(100))),Block([Call(Id(std),Id(cout),[StringLit(A1)])]),If(BinaryOp(&&,BinaryOp(>=,Id(avg),IntLit(81)),BinaryOp(<,Id(avg),IntLit(91))),Block([Call(Id(std),Id(cout),[StringLit(A2)])]),If(BinaryOp(&&,BinaryOp(>=,Id(avg),IntLit(71)),BinaryOp(<,Id(avg),IntLit(81))),Block([Call(Id(std),Id(cout),[StringLit(B1)])]),If(BinaryOp(&&,BinaryOp(>=,Id(avg),IntLit(61)),BinaryOp(<,Id(avg),IntLit(71))),Block([Call(Id(std),Id(cout),[StringLit(B2)])]),If(BinaryOp(&&,BinaryOp(>=,Id(avg),IntLit(51)),BinaryOp(<,Id(avg),IntLit(61))),Block([Call(Id(std),Id(cout),[StringLit(C1)])]),If(BinaryOp(&&,BinaryOp(>=,Id(avg),IntLit(41)),BinaryOp(<,Id(avg),IntLit(51))),Block([Call(Id(std),Id(cout),[StringLit(C2)])]),If(BinaryOp(&&,BinaryOp(>=,Id(avg),IntLit(33)),BinaryOp(<,Id(avg),IntLit(41))),Block([Call(Id(std),Id(cout),[StringLit(D)])]),If(BinaryOp(&&,BinaryOp(>=,Id(avg),IntLit(21)),BinaryOp(<,Id(avg),IntLit(33))),Block([Call(Id(std),Id(cout),[StringLit(E1)])]),If(BinaryOp(&&,BinaryOp(>=,Id(avg),IntLit(0)),BinaryOp(<,Id(avg),IntLit(21))),Block([Call(Id(std),Id(cout),[StringLit(E2)])]),Block([Call(Id(std),Id(cout),[StringLit(Invalid!)])]))))))))))]))])])"""
        self.assertTrue(TestAST.test(input,expect,353))
    def test54(self):
        input = """
            Class favor {
                f() {
                    If(noOfDigit<2)
                    {
                        std.out("\\nIt is a Single-digit Number!");
                        std.out("\\nTry again with a Number with Two or More Digits!");
                    }
                    Elseif(noOfDigit==2)
                    {
                        temp = num;
                        std.out("\\nFirst and Last Digit Interchanged Successfully!");
                        std.out("\\n\\nNew Number = ");
                    }
                    Else
                    {
                        temp = num;
                        revNum = rev;
                        rev = 0;
                        temp = num;
                        noOfDigitTemp = noOfDigit;
                        Foreach(temp In 0 .. Infinity By 10)
                        {
                            remTemp = revNum%10;
                            If(noOfDigitTemp==noOfDigit)
                            {
                                rem = temp%10;
                                rev = (rev*10)+rem;
                            }
                            Elseif(noOfDigitTemp==1)
                            {
                                rem = temp%10;
                                rev = (rev*10)+rem;
                            }
                            Else
                            {
                                rev = (rev*10)+remTemp;
                            }
                            temp = temp/10;
                            revNum = revNum/10;
                            noOfDigitTemp = noOfDigitTemp - 1;
                        }
                    }
                }
            }
            """
        expect = """Program([ClassDecl(Id(favor),[MethodDecl(Id(f),Instance,[],Block([If(BinaryOp(<,Id(noOfDigit),IntLit(2)),Block([Call(Id(std),Id(out),[StringLit(\\nIt is a Single-digit Number!)]),Call(Id(std),Id(out),[StringLit(\\nTry again with a Number with Two or More Digits!)])]),If(BinaryOp(==,Id(noOfDigit),IntLit(2)),Block([AssignStmt(Id(temp),Id(num)),Call(Id(std),Id(out),[StringLit(\\nFirst and Last Digit Interchanged Successfully!)]),Call(Id(std),Id(out),[StringLit(\\n\\nNew Number = )])]),Block([AssignStmt(Id(temp),Id(num)),AssignStmt(Id(revNum),Id(rev)),AssignStmt(Id(rev),IntLit(0)),AssignStmt(Id(temp),Id(num)),AssignStmt(Id(noOfDigitTemp),Id(noOfDigit)),For(Id(temp),IntLit(0),Id(Infinity),IntLit(10),Block([AssignStmt(Id(remTemp),BinaryOp(%,Id(revNum),IntLit(10))),If(BinaryOp(==,Id(noOfDigitTemp),Id(noOfDigit)),Block([AssignStmt(Id(rem),BinaryOp(%,Id(temp),IntLit(10))),AssignStmt(Id(rev),BinaryOp(+,BinaryOp(*,Id(rev),IntLit(10)),Id(rem)))]),If(BinaryOp(==,Id(noOfDigitTemp),IntLit(1)),Block([AssignStmt(Id(rem),BinaryOp(%,Id(temp),IntLit(10))),AssignStmt(Id(rev),BinaryOp(+,BinaryOp(*,Id(rev),IntLit(10)),Id(rem)))]),Block([AssignStmt(Id(rev),BinaryOp(+,BinaryOp(*,Id(rev),IntLit(10)),Id(remTemp)))]))),AssignStmt(Id(temp),BinaryOp(/,Id(temp),IntLit(10))),AssignStmt(Id(revNum),BinaryOp(/,Id(revNum),IntLit(10))),AssignStmt(Id(noOfDigitTemp),BinaryOp(-,Id(noOfDigitTemp),IntLit(1)))])])])))]))])])"""
        self.assertTrue(TestAST.test(input,expect,354))
    def test55(self):
        input = """
            Class Program {
                main() {
                    console.log(NewProgram);
                }
            }
            Class newClass {
                Val a, b, c: Int = 0x7, 06, 0b1001;
                $staticMethod() {
                    If (a) {
                        If (b) {
                            If (c) { }
                            Else { }
                        }
                        Else { }
                        If (u == e) { }
                        Elseif (f) { }
                    }
                    Elseif (t) { } Else { }
                }
            }
            """
        expect = """Program([ClassDecl(Id(Program),[MethodDecl(Id(main),Static,[],Block([Call(Id(console),Id(log),[Id(NewProgram)])]))]),ClassDecl(Id(newClass),[AttributeDecl(Instance,ConstDecl(Id(a),IntType,IntLit(7))),AttributeDecl(Instance,ConstDecl(Id(b),IntType,IntLit(6))),AttributeDecl(Instance,ConstDecl(Id(c),IntType,IntLit(9))),MethodDecl(Id($staticMethod),Static,[],Block([If(Id(a),Block([If(Id(b),Block([If(Id(c),Block([]),Block([]))]),Block([])),If(BinaryOp(==,Id(u),Id(e)),Block([]),If(Id(f),Block([])))]),If(Id(t),Block([]),Block([])))]))])])"""
        self.assertTrue(TestAST.test(input,expect,355))
    def test56(self):
        input = """
            Class checkAttr {
                Val a, b: Float = .3e5, 3.e5;
                Var c: String;
                Val $e, t, $r: Boolean;
            }
            """
        expect = """Program([ClassDecl(Id(checkAttr),[AttributeDecl(Instance,ConstDecl(Id(a),FloatType,FloatLit(30000.0))),AttributeDecl(Instance,ConstDecl(Id(b),FloatType,FloatLit(300000.0))),AttributeDecl(Instance,VarDecl(Id(c),StringType)),AttributeDecl(Static,ConstDecl(Id($e),BoolType,None)),AttributeDecl(Instance,ConstDecl(Id(t),BoolType,None)),AttributeDecl(Static,ConstDecl(Id($r),BoolType,None))])])"""
        self.assertTrue(TestAST.test(input,expect,356))
    def test57(self):
        input = """
            Class checkArray {
                Val b: Array[Array[Float, 0b1101], 0x71];
            }
            Class check2 {
                f() {
                    b = Array("string 1" +. "string 2", 3 + !4, Self.a() * 0x6);
                }
            }
            """
        expect = """Program([ClassDecl(Id(checkArray),[AttributeDecl(Instance,ConstDecl(Id(b),ArrayType(113,ArrayType(13,FloatType)),None))]),ClassDecl(Id(check2),[MethodDecl(Id(f),Instance,[],Block([AssignStmt(Id(b),[BinaryOp(+.,StringLit(string 1),StringLit(string 2)),BinaryOp(+,IntLit(3),UnaryOp(!,IntLit(4))),BinaryOp(*,CallExpr(Self(),Id(a),[]),IntLit(6))])]))])])"""
        self.assertTrue(TestAST.test(input,expect,357))
    def test58(self):
        input = """
            Class expr {
                t() {
                    Return (a + b * d / 0x1) && (t >= 3) || (b + 9.3 - a[2][07 + 0x1]);
                }
            }
            """
        expect = """Program([ClassDecl(Id(expr),[MethodDecl(Id(t),Instance,[],Block([Return(BinaryOp(||,BinaryOp(&&,BinaryOp(+,Id(a),BinaryOp(/,BinaryOp(*,Id(b),Id(d)),IntLit(1))),BinaryOp(>=,Id(t),IntLit(3))),BinaryOp(-,BinaryOp(+,Id(b),FloatLit(9.3)),ArrayCell(Id(a),[IntLit(2),BinaryOp(+,IntLit(7),IntLit(1))]))))]))])])"""
        self.assertTrue(TestAST.test(input,expect,358))
    def test59(self):
        input = """
            Class expr2 {
                r() {
                    a = (3 - 9 * -4) % (0b1) - "string" ==. "hello";
                }
            }
            """
        expect = """Program([ClassDecl(Id(expr2),[MethodDecl(Id(r),Instance,[],Block([AssignStmt(Id(a),BinaryOp(==.,BinaryOp(-,BinaryOp(%,BinaryOp(-,IntLit(3),BinaryOp(*,IntLit(9),UnaryOp(-,IntLit(4)))),IntLit(1)),StringLit(string)),StringLit(hello)))]))])])"""
        self.assertTrue(TestAST.test(input,expect,359))
    def test60(self):
        input = """
            Class Room {
                Var length: Float;
                Var breadth: Float;
                Var height: Float;   

                Constructor(len, bre, height: Float) {
                    Self.length = len;
                }
                Destructor() {
                    os.RemoveAll();
                }
                calculateArea(){   
                    Return length * breadth;
                }

                calculateVolume(){   
                    Return length * breadth * height;
                }
            }
            """
        expect = """Program([ClassDecl(Id(Room),[AttributeDecl(Instance,VarDecl(Id(length),FloatType)),AttributeDecl(Instance,VarDecl(Id(breadth),FloatType)),AttributeDecl(Instance,VarDecl(Id(height),FloatType)),MethodDecl(Id(Constructor),Instance,[param(Id(len),FloatType),param(Id(bre),FloatType),param(Id(height),FloatType)],Block([AssignStmt(FieldAccess(Self(),Id(length)),Id(len))])),MethodDecl(Id(Destructor),Instance,[],Block([Call(Id(os),Id(RemoveAll),[])])),MethodDecl(Id(calculateArea),Instance,[],Block([Return(BinaryOp(*,Id(length),Id(breadth)))])),MethodDecl(Id(calculateVolume),Instance,[],Block([Return(BinaryOp(*,BinaryOp(*,Id(length),Id(breadth)),Id(height)))]))])])"""
        self.assertTrue(TestAST.test(input,expect,360))
    def test61(self):
        input = """
            Class build {
                func() {
                    build.func().func1().f2().f3();
                }
            }
            """
        expect = """Program([ClassDecl(Id(build),[MethodDecl(Id(func),Instance,[],Block([Call(CallExpr(CallExpr(CallExpr(Id(build),Id(func),[]),Id(func1),[]),Id(f2),[]),Id(f3),[])]))])])"""
        self.assertTrue(TestAST.test(input,expect,361))
    def test62(self):
        input = """
            Class Laptop: PC {
                Val mainboard: board;
                Val RAM: ram;
                start_up() {
                    Return "Hi" + pc.name + "Windows is booting";
                }
            }
            """
        expect = """Program([ClassDecl(Id(Laptop),Id(PC),[AttributeDecl(Instance,ConstDecl(Id(mainboard),ClassType(Id(board)),None)),AttributeDecl(Instance,ConstDecl(Id(RAM),ClassType(Id(ram)),None)),MethodDecl(Id(start_up),Instance,[],Block([Return(BinaryOp(+,BinaryOp(+,StringLit(Hi),FieldAccess(Id(pc),Id(name))),StringLit(Windows is booting)))]))])])"""
        self.assertTrue(TestAST.test(input,expect,362))
    def test63(self):
        input = """
            Class com {
                Val b: Int = 0xAFFFF;
            }
            Class com2: com {
                f() {
                    Program.main(program.main);
                }
            }
            Class com3: com2 {

            }
            Class Program {
                main() {
                    ## This is entry program ##
                    com4.name = com3.f() * com.b;
                }
            }
            """
        expect = """Program([ClassDecl(Id(com),[AttributeDecl(Instance,ConstDecl(Id(b),IntType,IntLit(720895)))]),ClassDecl(Id(com2),Id(com),[MethodDecl(Id(f),Instance,[],Block([Call(Id(Program),Id(main),[FieldAccess(Id(program),Id(main))])]))]),ClassDecl(Id(com3),Id(com2),[]),ClassDecl(Id(Program),[MethodDecl(Id(main),Static,[],Block([AssignStmt(FieldAccess(Id(com4),Id(name)),BinaryOp(*,CallExpr(Id(com3),Id(f),[]),FieldAccess(Id(com),Id(b))))]))])])"""
        self.assertTrue(TestAST.test(input,expect,363))
    def test64(self):
        input = """
            Class Program {
                function() {
                    If (a) {
                        If (b) { }
                        Elseif (r) { } Else { }
                    }
                    Else { }
                    If (t) {
                        Self.func();
                    }
                    Elseif (y) { }
                }
                f2 (t, g: Int; r, e: Array[Int, 0b11]) {}
                f3() { }
                Val f: String;
                Val b, $e: Int = 1, 3;
            }
            """
        expect = """Program([ClassDecl(Id(Program),[MethodDecl(Id(function),Instance,[],Block([If(Id(a),Block([If(Id(b),Block([]),If(Id(r),Block([]),Block([])))]),Block([])),If(Id(t),Block([Call(Self(),Id(func),[])]),If(Id(y),Block([])))])),MethodDecl(Id(f2),Instance,[param(Id(t),IntType),param(Id(g),IntType),param(Id(r),ArrayType(3,IntType)),param(Id(e),ArrayType(3,IntType))],Block([])),MethodDecl(Id(f3),Instance,[],Block([])),AttributeDecl(Instance,ConstDecl(Id(f),StringType,None)),AttributeDecl(Instance,ConstDecl(Id(b),IntType,IntLit(1))),AttributeDecl(Static,ConstDecl(Id($e),IntType,IntLit(3)))])])"""
        self.assertTrue(TestAST.test(input,expect,364))
    def test65(self):
        input = """
            Class A {
                t() {
                    r = 0x22;
                    Var e: Float = .4e2;
                    Break;
                    Continue;
                    classname::$staticmethod();
                    t.instance().method().call();
                    If ("This is" +. "expression") { }
                    Foreach (b In -4 .. -0x244 By -1) { }
                    Return !t + y || r;
                }
            }
            """
        expect = """Program([ClassDecl(Id(A),[MethodDecl(Id(t),Instance,[],Block([AssignStmt(Id(r),IntLit(34)),VarDecl(Id(e),FloatType,FloatLit(40.0)),Break,Continue,Call(Id(classname),Id($staticmethod),[]),Call(CallExpr(CallExpr(Id(t),Id(instance),[]),Id(method),[]),Id(call),[]),If(BinaryOp(+.,StringLit(This is),StringLit(expression)),Block([])),For(Id(b),UnaryOp(-,IntLit(4)),UnaryOp(-,IntLit(580)),UnaryOp(-,IntLit(1)),Block([])]),Return(BinaryOp(||,BinaryOp(+,UnaryOp(!,Id(t)),Id(y)),Id(r)))]))])])"""
        self.assertTrue(TestAST.test(input,expect,365))
    def test66(self):
        input = """
            Class Flatten {
                flatten (S: Array[Int, 04]) {
                    If (S == Array()) {
                        Return S;
                    }
                    If (list.isinstance(S[0], list)) {
                        Return Self.flatten(S[0]) + Self.flatten(list.from(1).to().of(S));
                    }
                    Return list.from().to(1).of(S) + Self.flatten(list.from(1).to().of(S));
                }
            }
            Class Program {
                main() {
                    Var s: Array[Int, 12] = Array(Array(1,2), Array(3,4));
                    os.print("Flattened list is: ",Flatten.flatten(s));
                }
            }
            """
        expect = """Program([ClassDecl(Id(Flatten),[MethodDecl(Id(flatten),Instance,[param(Id(S),ArrayType(4,IntType))],Block([If(BinaryOp(==,Id(S),[]),Block([Return(Id(S))])),If(CallExpr(Id(list),Id(isinstance),[ArrayCell(Id(S),[IntLit(0)]),Id(list)]),Block([Return(BinaryOp(+,CallExpr(Self(),Id(flatten),[ArrayCell(Id(S),[IntLit(0)])]),CallExpr(Self(),Id(flatten),[CallExpr(CallExpr(CallExpr(Id(list),Id(from),[IntLit(1)]),Id(to),[]),Id(of),[Id(S)])])))])),Return(BinaryOp(+,CallExpr(CallExpr(CallExpr(Id(list),Id(from),[]),Id(to),[IntLit(1)]),Id(of),[Id(S)]),CallExpr(Self(),Id(flatten),[CallExpr(CallExpr(CallExpr(Id(list),Id(from),[IntLit(1)]),Id(to),[]),Id(of),[Id(S)])])))]))]),ClassDecl(Id(Program),[MethodDecl(Id(main),Static,[],Block([VarDecl(Id(s),ArrayType(12,IntType),[[IntLit(1),IntLit(2)],[IntLit(3),IntLit(4)]]),Call(Id(os),Id(print),[StringLit(Flattened list is: ),CallExpr(Id(Flatten),Id(flatten),[Id(s)])])]))])])"""
        self.assertTrue(TestAST.test(input,expect,366))
    def test67(self):
        input = """
            Class Program {
                main() { }
                main(a,b: Int) { }
            }
            Class Program {
                main(a: Float) { }
            }
            """
        expect = """Program([ClassDecl(Id(Program),[MethodDecl(Id(main),Static,[],Block([])),MethodDecl(Id(main),Instance,[param(Id(a),IntType),param(Id(b),IntType)],Block([]))]),ClassDecl(Id(Program),[MethodDecl(Id(main),Instance,[param(Id(a),FloatType)],Block([]))])])"""
        self.assertTrue(TestAST.test(input,expect,367))
    def test68(self):
        input = """
            Class check {
                Val r: Int;
                Val t: Float = 3e4;
                Val r, t, e, w: Boolean;
                Var e: Int;
            }
            """
        expect = """Program([ClassDecl(Id(check),[AttributeDecl(Instance,ConstDecl(Id(r),IntType,None)),AttributeDecl(Instance,ConstDecl(Id(t),FloatType,FloatLit(30000.0))),AttributeDecl(Instance,ConstDecl(Id(r),BoolType,None)),AttributeDecl(Instance,ConstDecl(Id(t),BoolType,None)),AttributeDecl(Instance,ConstDecl(Id(e),BoolType,None)),AttributeDecl(Instance,ConstDecl(Id(w),BoolType,None)),AttributeDecl(Instance,VarDecl(Id(e),IntType))])])"""
        self.assertTrue(TestAST.test(input,expect,368))
    def test69(self):
        input = """
            Class complement {
                convert() {
                    Var i, fail: Int;
                    Var binary, comp: Array[String, 7];
                    binary = IO.input(" Input a bit binary number: ");

                    Foreach (i In 0 .. size) {
                        If (binary[i] == "1") {
                            comp[i] = "0";
                        }

                        Elseif (binary[i] == "0") {
                            comp[i] = "1";
                        } 
                        Else {
                            fail = 1;
                            Break;
                        }

                    }
                    comp[size] = "\\\\0";
                    If (fail == 0) {
                        IO.output("The original binary number = " + binary);
                        IO.output("Ones complement the number = " + comp);
                    }
                }
            }
            """
        expect = """Program([ClassDecl(Id(complement),[MethodDecl(Id(convert),Instance,[],Block([VarDecl(Id(i),IntType),VarDecl(Id(fail),IntType),VarDecl(Id(binary),ArrayType(7,StringType)),VarDecl(Id(comp),ArrayType(7,StringType)),AssignStmt(Id(binary),CallExpr(Id(IO),Id(input),[StringLit( Input a bit binary number: )])),For(Id(i),IntLit(0),Id(size),IntLit(1),Block([If(BinaryOp(==,ArrayCell(Id(binary),[Id(i)]),StringLit(1)),Block([AssignStmt(ArrayCell(Id(comp),[Id(i)]),StringLit(0))]),If(BinaryOp(==,ArrayCell(Id(binary),[Id(i)]),StringLit(0)),Block([AssignStmt(ArrayCell(Id(comp),[Id(i)]),StringLit(1))]),Block([AssignStmt(Id(fail),IntLit(1)),Break])))])]),AssignStmt(ArrayCell(Id(comp),[Id(size)]),StringLit(\\\\0)),If(BinaryOp(==,Id(fail),IntLit(0)),Block([Call(Id(IO),Id(output),[BinaryOp(+,StringLit(The original binary number = ),Id(binary))]),Call(Id(IO),Id(output),[BinaryOp(+,StringLit(Ones complement the number = ),Id(comp))])]))]))])])"""
        self.assertTrue(TestAST.test(input,expect,369))
    def test70(self):
        input = """
            Class test70 {
                method() { }
                method2() { }
                main() { }
                main(a,b: Int) { }
            }
            """
        expect = """Program([ClassDecl(Id(test70),[MethodDecl(Id(method),Instance,[],Block([])),MethodDecl(Id(method2),Instance,[],Block([])),MethodDecl(Id(main),Instance,[],Block([])),MethodDecl(Id(main),Instance,[param(Id(a),IntType),param(Id(b),IntType)],Block([]))])])"""
        self.assertTrue(TestAST.test(input,expect,370))
    def test71(self):
        input = """
            Class test71 {
                main() {
                    Val r, t, s, r, w, q: Int;
                    Val a: Float = 1203;
                    Var e: Boolean = "String" ==. "Char";
                }
            }
            """
        expect = """Program([ClassDecl(Id(test71),[MethodDecl(Id(main),Instance,[],Block([ConstDecl(Id(r),IntType,None),ConstDecl(Id(t),IntType,None),ConstDecl(Id(s),IntType,None),ConstDecl(Id(r),IntType,None),ConstDecl(Id(w),IntType,None),ConstDecl(Id(q),IntType,None),ConstDecl(Id(a),FloatType,IntLit(1203)),VarDecl(Id(e),BoolType,BinaryOp(==.,StringLit(String),StringLit(Char)))]))])])"""
        self.assertTrue(TestAST.test(input,expect,371))
    def test72(self):
        input = """
            Class expr {
                t() {
                    Self.a = Self.b + Self.c - Name::$method() * ((r >= 6) || e);
                }
            }
            """
        expect = """Program([ClassDecl(Id(expr),[MethodDecl(Id(t),Instance,[],Block([AssignStmt(FieldAccess(Self(),Id(a)),BinaryOp(-,BinaryOp(+,FieldAccess(Self(),Id(b)),FieldAccess(Self(),Id(c))),BinaryOp(*,CallExpr(Id(Name),Id($method),[]),BinaryOp(||,BinaryOp(>=,Id(r),IntLit(6)),Id(e)))))]))])])"""
        self.assertTrue(TestAST.test(input,expect,372))
    def test73(self):
        input = """
            Class test73 {
                Val r: tumLumType = ThisName.r().t().ea().era();
            }
            """
        expect = """Program([ClassDecl(Id(test73),[AttributeDecl(Instance,ConstDecl(Id(r),ClassType(Id(tumLumType)),CallExpr(CallExpr(CallExpr(CallExpr(Id(ThisName),Id(r),[]),Id(t),[]),Id(ea),[]),Id(era),[])))])])"""
        self.assertTrue(TestAST.test(input,expect,373))
    def test74(self):
        input = """
            Class Function {

            }
            Class Program: Function {

            }
            Class Method: Program {
                main() {
                    ThisFunction = New Function(a,b,c,d,e,f);
                }
            }
            """
        expect = """Program([ClassDecl(Id(Function),[]),ClassDecl(Id(Program),Id(Function),[]),ClassDecl(Id(Method),Id(Program),[MethodDecl(Id(main),Instance,[],Block([AssignStmt(Id(ThisFunction),NewExpr(Id(Function),[Id(a),Id(b),Id(c),Id(d),Id(e),Id(f)]))]))])])"""
        self.assertTrue(TestAST.test(input,expect,374))
    def test75(self):
        input = """
            Class test75 {
                t() {
                    Foreach (t In 0 .. -1203 By -99) {
                        Foreach (j In t .. Inf) {
                            If (a) {
                                r[t][r][s] = t[r];
                            }
                        }
                    }
                }
            }
            """
        expect = """Program([ClassDecl(Id(test75),[MethodDecl(Id(t),Instance,[],Block([For(Id(t),IntLit(0),UnaryOp(-,IntLit(1203)),UnaryOp(-,IntLit(99)),Block([For(Id(j),Id(t),Id(Inf),IntLit(1),Block([If(Id(a),Block([AssignStmt(ArrayCell(Id(r),[Id(t),Id(r),Id(s)]),ArrayCell(Id(t),[Id(r)]))]))])])])])]))])])"""
        self.assertTrue(TestAST.test(input,expect,375))
    def test76(self):
        input = """
            Class test76 {
                $method(r, t, w, r, w: Int) {
                    If (w) {
                        Foreach (r In 1 .. 0x123 + 0523) { }
                    }
                    Elseif (q) { Return statement; }
                }
            }
            """
        expect = """Program([ClassDecl(Id(test76),[MethodDecl(Id($method),Static,[param(Id(r),IntType),param(Id(t),IntType),param(Id(w),IntType),param(Id(r),IntType),param(Id(w),IntType)],Block([If(Id(w),Block([For(Id(r),IntLit(1),BinaryOp(+,IntLit(291),IntLit(339)),IntLit(1),Block([])])]),If(Id(q),Block([Return(Id(statement))])))]))])])"""
        self.assertTrue(TestAST.test(input,expect,376))
    def test77(self):
        input = """
            Class checkConstr {
                Constructor (a, r, t, w: Float) {
                    Self.constr = a + r + t * w;
                }
            }
            """
        expect = """Program([ClassDecl(Id(checkConstr),[MethodDecl(Id(Constructor),Instance,[param(Id(a),FloatType),param(Id(r),FloatType),param(Id(t),FloatType),param(Id(w),FloatType)],Block([AssignStmt(FieldAccess(Self(),Id(constr)),BinaryOp(+,BinaryOp(+,Id(a),Id(r)),BinaryOp(*,Id(t),Id(w))))]))])])"""
        self.assertTrue(TestAST.test(input,expect,377))
    def test78(self):
        input = """
            Class thisName {
                Destructor () {
                    Return Self.name || Self.age;
                }
            }
            """
        expect = """Program([ClassDecl(Id(thisName),[MethodDecl(Id(Destructor),Instance,[],Block([Return(BinaryOp(||,FieldAccess(Self(),Id(name)),FieldAccess(Self(),Id(age))))]))])])"""
        self.assertTrue(TestAST.test(input,expect,378))
    def test79(self):
        input = """
            Class smallestMissing {
                smallest_missing(arr: Array[Int, 1000]; start: Int; end: Int){
                    If (start > end) {
                        Return end + 1;
                    }

                    If (start != arr[start]) {
                        Return start;
                    }

                    Var mid: Int = (start + end) / 2;

                    If (arr[mid] == mid) {
                        Return Self.smallest_missing(arr, mid + 1, end);
                    }

                    Return Self.smallest_missing(arr, start, mid);
                }
            }
            """
        expect = """Program([ClassDecl(Id(smallestMissing),[MethodDecl(Id(smallest_missing),Instance,[param(Id(arr),ArrayType(1000,IntType)),param(Id(start),IntType),param(Id(end),IntType)],Block([If(BinaryOp(>,Id(start),Id(end)),Block([Return(BinaryOp(+,Id(end),IntLit(1)))])),If(BinaryOp(!=,Id(start),ArrayCell(Id(arr),[Id(start)])),Block([Return(Id(start))])),VarDecl(Id(mid),IntType,BinaryOp(/,BinaryOp(+,Id(start),Id(end)),IntLit(2))),If(BinaryOp(==,ArrayCell(Id(arr),[Id(mid)]),Id(mid)),Block([Return(CallExpr(Self(),Id(smallest_missing),[Id(arr),BinaryOp(+,Id(mid),IntLit(1)),Id(end)]))])),Return(CallExpr(Self(),Id(smallest_missing),[Id(arr),Id(start),Id(mid)]))]))])])"""
        self.assertTrue(TestAST.test(input,expect,379))
    def test80(self):
        input = """
            Class nthFibo {
                fib(n: Int)
                {
                    If (n <= 1)	## stopping condition ##
                    {    Return n; }

                    Else	## recursive part ##
                    { Return (nthFibo.fib(n - 1) + nthFibo.fib(n - 2)); }
                }
            }
            """
        expect = """Program([ClassDecl(Id(nthFibo),[MethodDecl(Id(fib),Instance,[param(Id(n),IntType)],Block([If(BinaryOp(<=,Id(n),IntLit(1)),Block([Return(Id(n))]),Block([Return(BinaryOp(+,CallExpr(Id(nthFibo),Id(fib),[BinaryOp(-,Id(n),IntLit(1))]),CallExpr(Id(nthFibo),Id(fib),[BinaryOp(-,Id(n),IntLit(2))])))]))]))])])"""
        self.assertTrue(TestAST.test(input,expect,380))
    def test81(self):
        input = """
            Class RemoveSpace
            {
                main()
                {
                    Var inp: Scanner = New Scanner(System.in);
                    System.out.print("\\n Enter String: ");
                    Var s: String = inp.nextLine();
                    Var k: Int = s.length();
                    Var i: Int;
                    Var z: String = "";
                    Var c: String;

                    Foreach(i In 0 .. k By 1)
                    {
                        c = s.charAt(i);
                        If(c!=32) {
                            z=z+c;
                        }
                    }
                    System.out.println("String After Removing Spaces: "+z);
                }
            }
            """
        expect = """Program([ClassDecl(Id(RemoveSpace),[MethodDecl(Id(main),Instance,[],Block([VarDecl(Id(inp),ClassType(Id(Scanner)),NewExpr(Id(Scanner),[FieldAccess(Id(System),Id(in))])),Call(FieldAccess(Id(System),Id(out)),Id(print),[StringLit(\\n Enter String: )]),VarDecl(Id(s),StringType,CallExpr(Id(inp),Id(nextLine),[])),VarDecl(Id(k),IntType,CallExpr(Id(s),Id(length),[])),VarDecl(Id(i),IntType),VarDecl(Id(z),StringType,StringLit()),VarDecl(Id(c),StringType),For(Id(i),IntLit(0),Id(k),IntLit(1),Block([AssignStmt(Id(c),CallExpr(Id(s),Id(charAt),[Id(i)])),If(BinaryOp(!=,Id(c),IntLit(32)),Block([AssignStmt(Id(z),BinaryOp(+,Id(z),Id(c)))]))])]),Call(FieldAccess(Id(System),Id(out)),Id(println),[BinaryOp(+,StringLit(String After Removing Spaces: ),Id(z))])]))])])"""
        self.assertTrue(TestAST.test(input,expect,381))
    def test82(self):
        input = """
            Class ConsVowel
            {
                main()
                {

                    If((z=="A") || (z=="E") || (z=="I") || (z=="O") || (z=="U")) {
                        System.out.println(c+" is a Vowel.");
                    } ## Checking if Vowel ##
                    Else
                    {
                        If(((c>=65) && (c<=90)) || ((c>=97) && (c<=122))) {
                            System.out.println(c+" is a Consonant.");
                        } ## Checking if character is special character. ##
                        Else {
                            System.out.println(c+" is a Special Character.");
                        }
                    }
                }
            }
            """
        expect = """Program([ClassDecl(Id(ConsVowel),[MethodDecl(Id(main),Instance,[],Block([If(BinaryOp(||,BinaryOp(||,BinaryOp(||,BinaryOp(||,BinaryOp(==,Id(z),StringLit(A)),BinaryOp(==,Id(z),StringLit(E))),BinaryOp(==,Id(z),StringLit(I))),BinaryOp(==,Id(z),StringLit(O))),BinaryOp(==,Id(z),StringLit(U))),Block([Call(FieldAccess(Id(System),Id(out)),Id(println),[BinaryOp(+,Id(c),StringLit( is a Vowel.))])]),Block([If(BinaryOp(||,BinaryOp(&&,BinaryOp(>=,Id(c),IntLit(65)),BinaryOp(<=,Id(c),IntLit(90))),BinaryOp(&&,BinaryOp(>=,Id(c),IntLit(97)),BinaryOp(<=,Id(c),IntLit(122)))),Block([Call(FieldAccess(Id(System),Id(out)),Id(println),[BinaryOp(+,Id(c),StringLit( is a Consonant.))])]),Block([Call(FieldAccess(Id(System),Id(out)),Id(println),[BinaryOp(+,Id(c),StringLit( is a Special Character.))])]))]))]))])])"""
        self.assertTrue(TestAST.test(input,expect,382))
    def test83(self):
        input = """
            Class A: Program {
                Val r: Program = New Program(main);
            }
            """
        expect = """Program([ClassDecl(Id(A),Id(Program),[AttributeDecl(Instance,ConstDecl(Id(r),ClassType(Id(Program)),NewExpr(Id(Program),[Id(main)])))])])"""
        self.assertTrue(TestAST.test(input,expect,383))
    def test84(self):
        input = """
            Class Largest {

                $main(args: Array[String, 10000]) {
                    Var numArray: Array[Float, 10000] = Array(23.4, -34.5, 50.0, 33.5, 55.5, 43.7, 5.7, -66.5);
                    Var largest: Float = numArray[0];
                    Foreach (num In 0 .. numArray.length) {
                        If(largest < num) {
                            largest = num;
                        }
                    }
                    System.out.format("Largest element = %.2f", largest);
                }
            }
            """
        expect = """Program([ClassDecl(Id(Largest),[MethodDecl(Id($main),Static,[param(Id(args),ArrayType(10000,StringType))],Block([VarDecl(Id(numArray),ArrayType(10000,FloatType),[FloatLit(23.4),UnaryOp(-,FloatLit(34.5)),FloatLit(50.0),FloatLit(33.5),FloatLit(55.5),FloatLit(43.7),FloatLit(5.7),UnaryOp(-,FloatLit(66.5))]),VarDecl(Id(largest),FloatType,ArrayCell(Id(numArray),[IntLit(0)])),For(Id(num),IntLit(0),FieldAccess(Id(numArray),Id(length)),IntLit(1),Block([If(BinaryOp(<,Id(largest),Id(num)),Block([AssignStmt(Id(largest),Id(num))]))])]),Call(FieldAccess(Id(System),Id(out)),Id(format),[StringLit(Largest element = %.2f),Id(largest)])]))])])"""
        self.assertTrue(TestAST.test(input,expect,384))
    def test85(self):
        input = """
            Class CharString {
                main(args: Array[String, 0x1111111]) {
                    Var ch: String = "c";
                    Var st: String = Character.toString(ch);
                    ## Alternatively ##
                    ## st = String.valueOf(ch); ##
                    System.out.println("The string is: " + st);
                }
            }
            """
        expect = """Program([ClassDecl(Id(CharString),[MethodDecl(Id(main),Instance,[param(Id(args),ArrayType(17895697,StringType))],Block([VarDecl(Id(ch),StringType,StringLit(c)),VarDecl(Id(st),StringType,CallExpr(Id(Character),Id(toString),[Id(ch)])),Call(FieldAccess(Id(System),Id(out)),Id(println),[BinaryOp(+,StringLit(The string is: ),Id(st))])]))])])"""
        self.assertTrue(TestAST.test(input,expect,385))
    def test86(self):
        input = """
            Class function: object {
                Var JSON: String;
                func() {
                    JSON.string("New Sting");
                    a = 23.e2;
                    b = 5.4e-321;
                }
            }
            """
        expect = """Program([ClassDecl(Id(function),Id(object),[AttributeDecl(Instance,VarDecl(Id(JSON),StringType)),MethodDecl(Id(func),Instance,[],Block([Call(Id(JSON),Id(string),[StringLit(New Sting)]),AssignStmt(Id(a),FloatLit(2300.0)),AssignStmt(Id(b),FloatLit(5.4e-321))]))])])"""
        self.assertTrue(TestAST.test(input,expect,386))
    def test87(self):
        input = """
            Class Name {
                Constructor(name: String; age: Int) {
                    Self.name = name;
                    Self.age = age;
                }
            }
            """
        expect = """Program([ClassDecl(Id(Name),[MethodDecl(Id(Constructor),Instance,[param(Id(name),StringType),param(Id(age),IntType)],Block([AssignStmt(FieldAccess(Self(),Id(name)),Id(name)),AssignStmt(FieldAccess(Self(),Id(age)),Id(age))]))])])"""
        self.assertTrue(TestAST.test(input,expect,387))
    def test88(self):
        input = """
            Class B: C {
                he() {
                    wall = smoke + he.explore();
                }
            }
            Class Program {
                main(a: Int) {
                    Return a * b;
                }
            }
            """
        expect = """Program([ClassDecl(Id(B),Id(C),[MethodDecl(Id(he),Instance,[],Block([AssignStmt(Id(wall),BinaryOp(+,Id(smoke),CallExpr(Id(he),Id(explore),[])))]))]),ClassDecl(Id(Program),[MethodDecl(Id(main),Instance,[param(Id(a),IntType)],Block([Return(BinaryOp(*,Id(a),Id(b)))]))])])"""
        self.assertTrue(TestAST.test(input,expect,388))
    def test89(self):
        input = """
            Class Func {
                f() {
                    Foreach (a In b - 1 .. c By 2) {
                        Foreach (b In c - 1 .. d) {

                        }
                    }
                }
            }
            """
        expect = """Program([ClassDecl(Id(Func),[MethodDecl(Id(f),Instance,[],Block([For(Id(a),BinaryOp(-,Id(b),IntLit(1)),Id(c),IntLit(2),Block([For(Id(b),BinaryOp(-,Id(c),IntLit(1)),Id(d),IntLit(1),Block([])])])])]))])])"""
        self.assertTrue(TestAST.test(input,expect,389))
    def test90(self):
        input = """
            Class For {
                Val count: Int = 0;
                f() { Return For.f(); }
            }
            """
        expect = """Program([ClassDecl(Id(For),[AttributeDecl(Instance,ConstDecl(Id(count),IntType,IntLit(0))),MethodDecl(Id(f),Instance,[],Block([Return(CallExpr(Id(For),Id(f),[]))]))])])"""
        self.assertTrue(TestAST.test(input,expect,390))
    def test91(self):
        input = """
            Class MeowMeow: Dog {
                Var b: Int;
                Var $a, c, d: Float = .e4, 2., 78.9;
                Var a: Array[Float, 5] = Array(1.2, 3.6, 34e5, 23e4, 12.7e4);
            }
            """
        expect = """Program([ClassDecl(Id(MeowMeow),Id(Dog),[AttributeDecl(Instance,VarDecl(Id(b),IntType)),AttributeDecl(Static,VarDecl(Id($a),FloatType,FloatLit(0.0))),AttributeDecl(Instance,VarDecl(Id(c),FloatType,FloatLit(2.0))),AttributeDecl(Instance,VarDecl(Id(d),FloatType,FloatLit(78.9))),AttributeDecl(Instance,VarDecl(Id(a),ArrayType(5,FloatType),[FloatLit(1.2),FloatLit(3.6),FloatLit(3400000.0),FloatLit(230000.0),FloatLit(127000.0)]))])])"""
        self.assertTrue(TestAST.test(input,expect,391))
    def test92(self):
        input = """
            Class Program {
                main(){

                }
            }
            Class Des {
                Destructor() {
                    Stand.Delete().All(0);
                }
            }
            """
        expect = """Program([ClassDecl(Id(Program),[MethodDecl(Id(main),Static,[],Block([]))]),ClassDecl(Id(Des),[MethodDecl(Id(Destructor),Instance,[],Block([Call(CallExpr(Id(Stand),Id(Delete),[]),Id(All),[IntLit(0)])]))])])"""
        self.assertTrue(TestAST.test(input,expect,392))
    def test93(self):
        input = """
            Class Pro {
                MainMenu(a: Int; b: Int) {
                    Self.arr[4] = b.getName() + a.exp();
                }
            }
            Class ProMax {
                iPhone13(){
                    Return 40000000;
                }
            }
            """
        expect = """Program([ClassDecl(Id(Pro),[MethodDecl(Id(MainMenu),Instance,[param(Id(a),IntType),param(Id(b),IntType)],Block([AssignStmt(ArrayCell(FieldAccess(Self(),Id(arr)),[IntLit(4)]),BinaryOp(+,CallExpr(Id(b),Id(getName),[]),CallExpr(Id(a),Id(exp),[])))]))]),ClassDecl(Id(ProMax),[MethodDecl(Id(iPhone13),Instance,[],Block([Return(IntLit(40000000))]))])])"""
        self.assertTrue(TestAST.test(input,expect,393))
    def test94(self):
        input = """
            Class Program {
                main() {
                    a[1][2][3][4] = b.c(d[1][2+4][0x5 * 0b1]);
                }
                method () { }
            }
            """
        expect = """Program([ClassDecl(Id(Program),[MethodDecl(Id(main),Static,[],Block([AssignStmt(ArrayCell(Id(a),[IntLit(1),IntLit(2),IntLit(3),IntLit(4)]),CallExpr(Id(b),Id(c),[ArrayCell(Id(d),[IntLit(1),BinaryOp(+,IntLit(2),IntLit(4)),BinaryOp(*,IntLit(5),IntLit(1))])]))])),MethodDecl(Id(method),Instance,[],Block([]))])])"""
        self.assertTrue(TestAST.test(input,expect,394))
    def test95(self):
        input = """
            Class E {
                method() {
                    Return a[1][2][3] + className.b()[4];
                }
            }
            """
        expect = """Program([ClassDecl(Id(E),[MethodDecl(Id(method),Instance,[],Block([Return(BinaryOp(+,ArrayCell(Id(a),[IntLit(1),IntLit(2),IntLit(3)]),ArrayCell(CallExpr(Id(className),Id(b),[]),[IntLit(4)])))]))])])"""
        self.assertTrue(TestAST.test(input,expect,395))
    def test96(self):
        input = """
            Class _R {
                Val $y: Int = 12;
                _F() {
                    Val _, _, _: String = 3, 4, 5;
                }
            }
            """
        expect = """Program([ClassDecl(Id(_R),[AttributeDecl(Static,ConstDecl(Id($y),IntType,IntLit(12))),MethodDecl(Id(_F),Instance,[],Block([ConstDecl(Id(_),StringType,IntLit(3)),ConstDecl(Id(_),StringType,IntLit(4)),ConstDecl(Id(_),StringType,IntLit(5))]))])])"""
        self.assertTrue(TestAST.test(input,expect,396))
    def test97(self):
        input = """
            Class test {
                Var t, y: Int = 1, 2;
                method(a,b,c:Int; r:Func) {
                    If (a + b > 0) {
                        Foreach(i In 1 .. 12 By r) {
                            If (2 + 5) {
                                If (f >= t) {
                                    Continue;
                                }
                            }
                        }
                    }
                    Elseif (t * 7) {
                        If (34) { }
                        Else { Return; }
                    }
                }
            }
            """
        expect = """Program([ClassDecl(Id(test),[AttributeDecl(Instance,VarDecl(Id(t),IntType,IntLit(1))),AttributeDecl(Instance,VarDecl(Id(y),IntType,IntLit(2))),MethodDecl(Id(method),Instance,[param(Id(a),IntType),param(Id(b),IntType),param(Id(c),IntType),param(Id(r),ClassType(Id(Func)))],Block([If(BinaryOp(>,BinaryOp(+,Id(a),Id(b)),IntLit(0)),Block([For(Id(i),IntLit(1),IntLit(12),Id(r),Block([If(BinaryOp(+,IntLit(2),IntLit(5)),Block([If(BinaryOp(>=,Id(f),Id(t)),Block([Continue]))]))])])]),If(BinaryOp(*,Id(t),IntLit(7)),Block([If(IntLit(34),Block([]),Block([Return()]))])))]))])])"""
        self.assertTrue(TestAST.test(input,expect,397))
    def test98(self):
        input = """
            Class B {
                Val b: Int = 0;
                Val a: Float = Self.a.b.c().t[1];
            }
            """
        expect = """Program([ClassDecl(Id(B),[AttributeDecl(Instance,ConstDecl(Id(b),IntType,IntLit(0))),AttributeDecl(Instance,ConstDecl(Id(a),FloatType,ArrayCell(FieldAccess(CallExpr(FieldAccess(FieldAccess(Self(),Id(a)),Id(b)),Id(c),[]),Id(t)),[IntLit(1)])))])])"""
        self.assertTrue(TestAST.test(input,expect,398))
    def test99(self):
        input = """
            Class Program {
                Var a: Program = New Program(1);
                Val b: Main;
                main() {
                    b = Main::$get()[1];
                    a = Main.get()[3][5][67];
                }
            }
            """
        expect = """Program([ClassDecl(Id(Program),[AttributeDecl(Instance,VarDecl(Id(a),ClassType(Id(Program)),NewExpr(Id(Program),[IntLit(1)]))),AttributeDecl(Instance,ConstDecl(Id(b),ClassType(Id(Main)),None)),MethodDecl(Id(main),Static,[],Block([AssignStmt(Id(b),ArrayCell(CallExpr(Id(Main),Id($get),[]),[IntLit(1)])),AssignStmt(Id(a),ArrayCell(CallExpr(Id(Main),Id(get),[]),[IntLit(3),IntLit(5),IntLit(67)]))]))])])"""
        self.assertTrue(TestAST.test(input,expect,399))
