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
        expect = """Program([ClassDecl(Id(Dog),Id(Animal),[MethodDecl(Id($test),Static,[],Block([VarDecl(Id(a),IntType,IntLit(0)),VarDecl(Id(b),IntType,IntLit(0)),VarDecl(Id(c),IntType,IntLit(0)),VarDecl(Id(a),ArrayType(IntLit(5),IntType)),VarDecl(Id(b),ArrayType(IntLit(2),FloatType),[FloatLit(1.2),FloatLit(5.2)]),ConstDecl(Id(ab),ArrayType(IntLit(5),FloatType),[FloatLit(1.2),FloatLit(3.6),FloatLit(3400000.0),FloatLit(230000.0),FloatLit(0.00127)]),VarDecl(Id(arr),ArrayType(IntLit(4),ArrayType(IntLit(803),ArrayType(IntLit(1),FloatType)))),VarDecl(Id(aduvip),ArrayType(IntLit(3),ArrayType(IntLit(5),IntType)),[[IntLit(11),IntLit(12),IntLit(13),IntLit(14),IntLit(15)],[IntLit(6),IntLit(7),IntLit(8),IntLit(9),IntLit(10)],[IntLit(1),IntLit(2),IntLit(3),IntLit(4),IntLit(5)]])]))])])"""
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
        expect = """Program([ClassDecl(Id(MeowMeow),Id(Dog),[AttributeDecl(Instance,VarDecl(Id(b),IntType)),AttributeDecl(Static,VarDecl(Id($a),FloatType,FloatLit(0.0))),AttributeDecl(Instance,VarDecl(Id(c),FloatType,FloatLit(2.0))),AttributeDecl(Instance,VarDecl(Id(d),FloatType,FloatLit(78.9))),AttributeDecl(Instance,VarDecl(Id(a),ArrayType(IntLit(5),FloatType),[FloatLit(1.2),FloatLit(3.6),FloatLit(3400000.0),FloatLit(230000.0),FloatLit(127000.0)]))])])"""
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
        expect = """Program([ClassDecl(Id(MeowMeow),Id(Dog),[AttributeDecl(Instance,VarDecl(Id(b),IntType)),AttributeDecl(Static,VarDecl(Id($a),FloatType,FloatLit(0.0))),AttributeDecl(Instance,VarDecl(Id(c),FloatType,FloatLit(2.0))),AttributeDecl(Instance,VarDecl(Id(d),FloatType,FloatLit(78.9))),AttributeDecl(Instance,VarDecl(Id(a),ArrayType(IntLit(5),FloatType),[FloatLit(1.2),FloatLit(3.6),FloatLit(3400000.0),FloatLit(230000.0),FloatLit(127000.0)])),MethodDecl(Id(function),Instance,[param(Id(a),IntType),param(Id(b),IntType),param(Id(c),IntType)],Block([For(Id(a),Id(b),BinaryOp(+,Id(c),IntLit(1)),Block([Return(BinaryOp(+,CallExpr(Self(),Id(method),[]),ArrayCell(Id(a),[Id(b)])))])])]))])])"""
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
        expect = """Program([ClassDecl(Id(QuickSort),Id(Sort),[MethodDecl(Id($partition),Static,[param(Id(arr),ArrayType(IntLit(10),IntType)),param(Id(start),IntType),param(Id(end),IntType)],Block([VarDecl(Id(pivot),IntType,ArrayCell(Id(arr),[Id(start)])),VarDecl(Id(count),IntType,IntLit(0)),For(Id(i),BinaryOp(+,Id(start),IntLit(1)),BinaryOp(+,Id(end),IntLit(1)),IntLit(1),Block([If(BinaryOp(<=,ArrayCell(Id(arr),[Id(i)]),Id(pivot)),Block([AssignStmt(Id(count),BinaryOp(+,Id(count),IntLit(1)))]))])]),VarDecl(Id(pivotIndex),IntType,BinaryOp(+,Id(start),Id(count))),Call(Id(Swap),Id($swap),[ArrayCell(Id(arr),[Id(pivotIndex)]),ArrayCell(Id(arr),[Id(start)])]),VarDecl(Id(i),IntType,Id(start)),VarDecl(Id(j),IntType,Id(end)),For(Id(k),IntLit(1),IntLit(100),Block([If(BinaryOp(<=,ArrayCell(Id(arr),[Id(i)]),Id(pivot)),Block([AssignStmt(Id(i),BinaryOp(+,Id(i),IntLit(1)))])),If(BinaryOp(>,ArrayCell(Id(arr),[Id(j)]),Id(pivot)),Block([AssignStmt(Id(j),BinaryOp(-,Id(j),IntLit(1)))])),If(UnaryOp(!,BinaryOp(&&,BinaryOp(<,Id(i),Id(pivotIndex)),BinaryOp(>,Id(j),Id(pivotIndex)))),Block([Break]),Block([AssignStmt(Id(i),BinaryOp(+,Id(i),IntLit(1))),AssignStmt(Id(j),BinaryOp(-,Id(j),IntLit(1))),Call(Id(Swap),Id($swap),[ArrayCell(Id(arr),[Id(i)]),ArrayCell(Id(arr),[Id(j)])])]))])]),Return(Id(pivotIndex))])),MethodDecl(Id($quickSort),Static,[param(Id(arr),ArrayType(IntLit(10),IntType)),param(Id(start),IntType),param(Id(end),IntType)],Block([If(BinaryOp(>=,Id(start),Id(end)),Block([Return()])),VarDecl(Id(p),IntType,CallExpr(Id(QuickSort),Id($partition),[Id(arr),Id(start),Id(end)])),Call(Id(QuickSort),Id($quickSort),[Id(arr),Id(start),BinaryOp(-,Id(p),IntLit(1))]),Call(Id(QuickSort),Id($quickSort),[Id(arr),BinaryOp(+,Id(p),IntLit(1)),Id(end)])])),MethodDecl(Id($print),Static,[],Block([VarDecl(Id(arr),ArrayType(IntLit(10),IntType),[IntLit(9),IntLit(3),IntLit(4),IntLit(2),IntLit(1),IntLit(8),IntLit(4),IntLit(9),IntLit(5),IntLit(6)]),VarDecl(Id(n),IntType,IntLit(6)),Call(Id(QuickSort),Id($quickSort),[Id(arr),IntLit(0),BinaryOp(-,Id(n),IntLit(1))]),For(Id(i),IntLit(0),Id(n),IntLit(1),Block([Call(Id(System),Id($print),[ArrayCell(Id(arr),[Id(i)])])])]),Return(IntLit(0))]))])])"""
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
        expect = """Program([ClassDecl(Id(SelectionSort),[MethodDecl(Id(swap),Instance,[param(Id(xp),IntType),param(Id(yp),IntType)],Block([VarDecl(Id(temp),IntType,Id(xp)),AssignStmt(Id(xp),Id(yp)),AssignStmt(Id(yp),Id(temp))])),MethodDecl(Id(selectionSort),Instance,[param(Id(arr),ArrayType(IntLit(100),IntType)),param(Id(n),IntType)],Block([VarDecl(Id(i),IntType),VarDecl(Id(j),IntType),VarDecl(Id(min_idx),IntType),For(Id(i),IntLit(0),BinaryOp(-,Id(n),IntLit(1)),IntLit(1),Block([AssignStmt(Id(min_idx),Id(i)),For(Id(j),BinaryOp(+,Id(i),IntLit(1)),Id(n),IntLit(1),Block([If(BinaryOp(<,ArrayCell(Id(arr),[Id(j)]),ArrayCell(Id(arr),[Id(min_idx)])),Block([AssignStmt(Id(min_idx),Id(j))]))])]),Call(Self(),Id(swap),[ArrayCell(Id(arr),[Id(min_idx)]),ArrayCell(Id(arr),[Id(i)])])])])]))])])"""
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
        expect = """Program([ClassDecl(Id(BinarySearch),[MethodDecl(Id(binarySearch),Instance,[param(Id(arr),ArrayType(IntLit(100),IntType)),param(Id(l),IntType),param(Id(r),IntType),param(Id(x),IntType)],Block([If(BinaryOp(>=,Id(r),Id(l)),Block([VarDecl(Id(mid),IntType,BinaryOp(+,Id(l),BinaryOp(/,BinaryOp(-,Id(r),Id(l)),IntLit(2)))),If(BinaryOp(==,ArrayCell(Id(arr),[Id(mid)]),Id(x)),Block([Return(Id(mid))])),If(BinaryOp(>,ArrayCell(Id(arr),[Id(mid)]),Id(x)),Block([Return(CallExpr(Self(),Id(binarySearch),[Id(arr),Id(l),BinaryOp(-,Id(mid),IntLit(1)),Id(x)]))])),Return(CallExpr(Self(),Id(binarySearch),[Id(arr),BinaryOp(+,Id(mid),IntLit(1)),Id(r),Id(x)]))])),Return(UnaryOp(-,IntLit(1)))]))])])"""
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
        expect = """Program([ClassDecl(Id(Roman),[MethodDecl(Id(convertToRoman),Instance,[param(Id(num),IntType)],Block([VarDecl(Id(lookup),ArrayType(IntLit(16),ArrayType(IntLit(2),IntType)),[[Id(M),IntLit(1000)],[Id(CM),IntLit(900)],[Id(D),IntLit(500)],[Id(CD),IntLit(400)],[Id(C),IntLit(100)],[Id(XC),IntLit(90)],[Id(L),IntLit(50)],[Id(XL),IntLit(40)],[Id(X),IntLit(10)],[Id(IX),IntLit(9)],[Id(V),IntLit(5)],[Id(IV),IntLit(4)],[Id(I),IntLit(1)]]),VarDecl(Id(roman),StringType),For(Id(i),IntLit(0),CallExpr(Id(lookup),Id(length),[]),Block([For(Id(num),ArrayCell(Id(lookup),[Id(i)]),IntLit(0),Block([AssignStmt(Id(roman),BinaryOp(+,Id(roman),Id(i))),AssignStmt(Id(num),BinaryOp(-,Id(num),ArrayCell(Id(lookup),[Id(i)])))])])])]),Return(Id(roman))]))])])"""
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
        expect = """Program([ClassDecl(Id(JumpSearch),[MethodDecl(Id(jumpSearch),Instance,[param(Id(arr),ArrayType(IntLit(171),IntType)),param(Id(x),IntType),param(Id(n),IntType)],Block([VarDecl(Id(step),FloatType,CallExpr(Id(Math),Id(sqrt),[Id(n)])),VarDecl(Id(prev),IntType,IntLit(0)),For(Id(i),IntLit(1),IntLit(100),Block([If(BinaryOp(<,ArrayCell(Id(arr),[BinaryOp(-,CallExpr(Id(STD),Id(min),[Id(step),Id(n)]),IntLit(1))]),Id(x)),Block([AssignStmt(Id(prev),Id(step)),AssignStmt(Id(step),BinaryOp(+,Id(step),CallExpr(Id(Math),Id(sqrt),[Id(n)]))),If(BinaryOp(>=,Id(prev),Id(n)),Block([Return(UnaryOp(-,IntLit(1)))]))]))])]),For(Id(i),IntLit(0),Id(x),Block([AssignStmt(Id(prev),BinaryOp(+,Id(prev),IntLit(1))),If(BinaryOp(==,Id(prev),CallExpr(Id(STD),Id(min),[Id(step),Id(n)])),Block([Return(UnaryOp(-,IntLit(1)))]))])]),If(BinaryOp(==,ArrayCell(Id(arr),[Id(prev)]),Id(x)),Block([Return(Id(prev))])),Return(UnaryOp(-,IntLit(1)))]))])])"""
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
        expect = """Program([ClassDecl(Id(Reverse),[MethodDecl(Id(reverse),Instance,[],Block([Call(Id(IO),Id(input),[StringLit(Enter an integer: )]),For(Id(n),Id(n),IntLit(0),Block([AssignStmt(Id(remainder),BinaryOp(%,Id(n),IntLit(10))),AssignStmt(Id(reversed_number),BinaryOp(+,BinaryOp(*,Id(reversed_number),IntLit(10)),Id(remainder))),AssignStmt(Id(n),BinaryOp(/,Id(n),IntLit(10)))])])])),AttributeDecl(Instance,VarDecl(Id(n),IntType)),AttributeDecl(Instance,VarDecl(Id(reminder),IntType)),AttributeDecl(Instance,VarDecl(Id(reversed_number),IntType,IntLit(0))),MethodDecl(Id(get),Instance,[],Block([Return(FieldAccess(Self(),Id(reversed_number)))]))])])"""
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
        expect = """Program([ClassDecl(Id(Max),[MethodDecl(Id(findMax),Instance,[param(Id(arr),ArrayType(IntLit(100),IntType))],Block([VarDecl(Id(maxElement),IntType,ArrayCell(Id(arr),[IntLit(1)])),For(Id(i),IntLit(2),CallExpr(Id(arr),Id(length),[]),Block([If(BinaryOp(<,Id(maxElement),ArrayCell(Id(arr),[Id(i)])),Block([AssignStmt(Id(maxElement),ArrayCell(Id(arr),[Id(i)]))]))])]),Return(Id(maxElement))]))]),ClassDecl(Id(Program),[MethodDecl(Id(main),Static,[],Block([AssignStmt(Id(arr),CallExpr(Id(IO),Id(input),[StringLit(Your array: )])),AssignStmt(Id(max),NewExpr(Id(Max),[])),Call(Id(Console),Id(print),[CallExpr(Id(max),Id(findMax),[Id(arr)])])]))])])"""
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
        expect = """Program([ClassDecl(Id(Prime),[AttributeDecl(Instance,VarDecl(Id(i),IntType)),AttributeDecl(Instance,VarDecl(Id(n),IntType)),AttributeDecl(Instance,VarDecl(Id(is_prime),BoolType,BooleanLit(True))),MethodDecl(Id(checkPrime),Instance,[param(Id(num),IntType)],Block([If(BinaryOp(||,BinaryOp(==,Id(n),IntLit(0)),BinaryOp(==,Id(n),IntLit(1))),Block([AssignStmt(Id(is_prime),BooleanLit(False))])),For(Id(i),IntLit(2),BinaryOp(/,Id(n),IntLit(2)),Block([If(BinaryOp(==,BinaryOp(%,Id(n),Id(i)),IntLit(0)),Block([AssignStmt(Id(is_prime),Id(false)),Break]))])]),If(Id(is_prime),Block([Return(BooleanLit(True))]),Block([Return(BooleanLit(False))]))]))])])"""
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
        expect = """Program([ClassDecl(Id(Fibonacci),[MethodDecl(Id($fibo),Static,[],Block([ConstDecl(Id(number),IntType,CallExpr(Id(Lib),Id(parseInt),[StringLit(Enter the number of terms: )])),VarDecl(Id(n1),IntType,IntLit(0)),VarDecl(Id(n2),IntType,IntLit(1)),VarDecl(Id(nextTerm),IntType),Call(Id(console),Id(log),[StringLit(Fibonacci Series:)]),For(Id(i),IntLit(1),Id(number),Block([Call(Id(console),Id(log),[Id(n1)]),AssignStmt(Id(nextTerm),BinaryOp(+,Id(n1),Id(n2))),AssignStmt(Id(n1),Id(n2)),AssignStmt(Id(n2),Id(nextTerm))])])]))])])"""
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
        expect = """"""
        self.assertTrue(TestAST.test(input,expect,350))
    def test51(self):
        input = """
            Class Program {
                main() {

                }
            }
            Class NotProgram {
                main() {

                }
            }
            """
        expect = """"""
        self.assertTrue(TestAST.test(input,expect,351))
    def test52(self):
        input = """
            Class Program {
                main(a, b, c, d: Int) {

                }
            }
            """
        expect = """"""
        self.assertTrue(TestAST.test(input,expect,352))
    def test53(self):
        input = """
            
            """
        expect = """"""
        self.assertTrue(TestAST.test(input,expect,353))
    # def test(self):
    #     input = """
            
    #         """
    #     expect = """"""
    #     self.assertTrue(TestAST.test(input,expect,))
    # def test(self):
    #     input = """
            
    #         """
    #     expect = """"""
    #     self.assertTrue(TestAST.test(input,expect,))
    # def test(self):
    #     input = """
            
    #         """
    #     expect = """"""
    #     self.assertTrue(TestAST.test(input,expect,))
    # def test(self):
    #     input = """
            
    #         """
    #     expect = """"""
    #     self.assertTrue(TestAST.test(input,expect,))
    # def test(self):
    #     input = """
            
    #         """
    #     expect = """"""
    #     self.assertTrue(TestAST.test(input,expect,))
    # def test(self):
    #     input = """
            
    #         """
    #     expect = """"""
    #     self.assertTrue(TestAST.test(input,expect,))
    # def test(self):
    #     input = """
            
    #         """
    #     expect = """"""
    #     self.assertTrue(TestAST.test(input,expect,))
    # def test(self):
    #     input = """
            
    #         """
    #     expect = """"""
    #     self.assertTrue(TestAST.test(input,expect,))
    # def test(self):
    #     input = """
            
    #         """
    #     expect = """"""
    #     self.assertTrue(TestAST.test(input,expect,))
    # def test(self):
    #     input = """
            
    #         """
    #     expect = """"""
    #     self.assertTrue(TestAST.test(input,expect,))
    # def test(self):
    #     input = """
            
    #         """
    #     expect = """"""
    #     self.assertTrue(TestAST.test(input,expect,))
    # def test(self):
    #     input = """
            
    #         """
    #     expect = """"""
    #     self.assertTrue(TestAST.test(input,expect,))
    # def test(self):
    #     input = """
            
    #         """
    #     expect = """"""
    #     self.assertTrue(TestAST.test(input,expect,))
    # def test(self):
    #     input = """
            
    #         """
    #     expect = """"""
    #     self.assertTrue(TestAST.test(input,expect,))
    # def test(self):
    #     input = """
            
    #         """
    #     expect = """"""
    #     self.assertTrue(TestAST.test(input,expect,))
    # def test(self):
    #     input = """
            
    #         """
    #     expect = """"""
    #     self.assertTrue(TestAST.test(input,expect,))
    # def test(self):
    #     input = """
            
    #         """
    #     expect = """"""
    #     self.assertTrue(TestAST.test(input,expect,))
    # def test(self):
    #     input = """
            
    #         """
    #     expect = """"""
    #     self.assertTrue(TestAST.test(input,expect,))
    # def test(self):
    #     input = """
            
    #         """
    #     expect = """"""
    #     self.assertTrue(TestAST.test(input,expect,))
    # def test(self):
    #     input = """
            
    #         """
    #     expect = """"""
    #     self.assertTrue(TestAST.test(input,expect,))
    # def test(self):
    #     input = """
            
    #         """
    #     expect = """"""
    #     self.assertTrue(TestAST.test(input,expect,))
    # def test(self):
    #     input = """
            
    #         """
    #     expect = """"""
    #     self.assertTrue(TestAST.test(input,expect,))
    # def test(self):
    #     input = """
            
    #         """
    #     expect = """"""
    #     self.assertTrue(TestAST.test(input,expect,))
    # def test(self):
    #     input = """
            
    #         """
    #     expect = """"""
    #     self.assertTrue(TestAST.test(input,expect,))
    # def test(self):
    #     input = """
            
    #         """
    #     expect = """"""
    #     self.assertTrue(TestAST.test(input,expect,))
    # def test(self):
    #     input = """
            
    #         """
    #     expect = """"""
    #     self.assertTrue(TestAST.test(input,expect,))
    