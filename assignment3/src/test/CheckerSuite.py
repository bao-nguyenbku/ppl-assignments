import unittest
from TestUtils import TestChecker
from AST import *

class CheckerSuite(unittest.TestCase):
    def test(self):
        # Class A {
        #     Constructor() { }
        # }
        input = """
        Class Animal{
            Var $name : String = "aaaaa";
            Var sex : String = "Male";
            Constructor () { }
            Destructor () { }
        }
        Class Dog : Animal{
            Var $a : Int = 5 + 6 - 7 * 8;
            Var $b : Float = 5.6 * 9;
            Var $c : Int = Dog::$a - 8;
            Var $d : Float = Dog::$a * Dog::$b;
            Var $e : String = Animal::$name;
            Var d : String = "Hello";
            Var e : String = Self.d;
            Var meomeo : Int = (Meo::$e - 89) * 9600;
            Bark(a, b, c : String; d, e, f : Float)
            {
                
            }
            Constructor () { }
            Destructor () { }
        }
        Class Meo : Animal{
            Var $e : Int = 6;
            MeowMeow(a : Float)
            {
                
            }
            Constructor () { }
            Destructor () { }
        }
        Class Program {
            main() { }
        }
        """
        # input = """
        # Class Program {
        #     main() { }
        #     Constructor () { }
        #     Destructor () { }
        # }
        # Class A {
        #     Var a: Int;
        #     Constructor (a: Int; b: Float) { 
        #         a = 4;
        #     }
        #     Destructor () { }
        # }
        # """
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
    #     expect = "Type Mismatch In Statement: ConstDecl(Id($a),IntType,FloatLit(3.2))"
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
    #         Val $a: Int = 2 + True;
    #     }
    #     """
    #     expect = "Type Mismatch In Expression: BinaryOp(+,IntLit(2),BooleanLit(True))"
    #     self.assertTrue(TestChecker.test(input,expect,402))
    # def test3(self):
    #     input = """
    #     Class A {
    #         Val $a: Int = 3;
    #     }
    #     Class B {
    #         Val $b: A = New A();
    #     }
    #     """
    #     expect = "Undeclared Method: Constructor"
    #     self.assertTrue(TestChecker.test(input,expect,403))

    # def test4(self):
    #     input = """
    #     Class B: A {
    #         Val $r :Int = 2 + 2 * 2.5;
    #         Var a: Boolean = True;
    #         setA(a: Int) { }
    #     }
    #     """
    #     expect = "Type Mismatch In Statement: ConstDecl(Id($r),IntType,BinaryOp(+,IntLit(2),BinaryOp(*,IntLit(2),FloatLit(2.5))))"
    #     self.assertTrue(TestChecker.test(input,expect,404))
    # def test5(self):
    #     input = """
    #     Class B: A {
    #         Var t: Float = 1.4 % 3; 
    #         setA(a: Int) { }
    #     }
    #     """
    #     expect = "Type Mismatch In Expression: BinaryOp(%,FloatLit(1.4),IntLit(3))"
    #     self.assertTrue(TestChecker.test(input,expect,405))
    # def test6(self):
    #     input = """
    #     Class A {
    #         Var a: Array[Array[Int, 2], 2] = Array(
    #                                             Array(3,6),
    #                                             Array(8,9.2)
    #         );
    #     }
    #     """
    #     expect = "Illegal Array Literal: [IntLit(8),FloatLit(9.2)]"
    #     self.assertTrue(TestChecker.test(input,expect,406))
    # def test7(self):
    #     input = """
    #     Class A {
    #         Var a: Int = 120;
    #         Val $a: C = New C();
    #     }
    #     """
    #     expect = "Undeclared Class: C"
    #     self.assertTrue(TestChecker.test(input,expect,407))
    # def test8(self):
    #     input = """
    #     Class A {
    #         Var a, t, r: Int = 120, 12 * 60 - 9, 1e4;
    #     }
    #     """
    #     expect = "Type Mismatch In Statement: VarDecl(Id(r),IntType,FloatLit(10000.0))"
    #     self.assertTrue(TestChecker.test(input,expect,408))
    # def test9(self):
    #     input = """
    #     Class B {
    #         Val C: String;
    #     }
    #     """
    #     expect = "Illegal Constant Expression: None"
    #     self.assertTrue(TestChecker.test(input,expect,409))
    # def test10(self):
    #     input = """
    #     Class A {
    #         Val $a: Int = 3;
    #         Constructor(a: Float; b: Int) { }
    #     }
    #     Class B {
    #         Val $b: A = New A(1, 3.2);
    #     }
    #     """
    #     expect = "Type Mismatch In Expression: NewExpr(Id(A),[IntLit(1),FloatLit(3.2)])"
    #     self.assertTrue(TestChecker.test(input,expect,410))
    # def test11(self):
    #     input = """
    #     Class A {
    #         Var z: Int;
    #         getA(a: Int) {
    #             Var b: Int;
    #             Foreach (b In 1 .. 10) { 
    #                 If (b > 4) { Var c: Float = 2; }
    #             }
    #         }
    #     }
    #     """
    #         # Var b: Int = A.c.a;
    #     expect = "Type Mismatch In Statement: VarDecl(Id(c),FloatType,IntLit(2))"
    #     self.assertTrue(TestChecker.test(input,expect,411))
    # def test12(self):
    #     input = """
    #     Class A {
    #         Var z: Int;
    #         getA(a: Int) {
    #             Foreach (b In 1 .. 10) { }
    #         }
    #     }
    #     """
    #         # Var b: Int = A.c.a;
    #     expect = "Undeclared Variable: b"
    #     self.assertTrue(TestChecker.test(input,expect,412))
    # def test13(self):
    #     input = """
    #     Class A {
    #         Var z: Int;
    #         getA(a: Int) {
    #             Var b: Int;
    #             Foreach (b In 1.2 .. 10.5) { }
    #         }
    #     }
    #     """
    #         # Var b: Int = A.c.a;
    #     expect = "Type Mismatch In Statement: For(Id(b),FloatLit(1.2),FloatLit(10.5),IntLit(1),Block([])])"
    #     self.assertTrue(TestChecker.test(input,expect,413))
    # def test14(self):
    #     input = """
    #     Class A {
    #         Var z: Int;
    #         getA(a: Int) {
    #             Var b: Int;
    #             Foreach (b In 1 .. 100) {
    #                 If (b + 4) { }
    #                 Else { Var e: String; }
    #             }
    #         }
    #     }
    #     """
    #         # Var b: Int = A.c.a;
    #     expect = "Type Mismatch In Statement: If(BinaryOp(+,Id(b),IntLit(4)),Block([]),Block([VarDecl(Id(e),StringType)]))"
    #     self.assertTrue(TestChecker.test(input,expect,414))
    # def test15(self):
    #     input = """
    #     Class A {
    #         Var z: Int;
    #         getA(a: Int) {
    #             Var b: Int;
    #             Foreach (b In 1 .. 100) {
    #                 If (b > 6) { 
    #                     If (b < 120) { }
    #                     Elseif (a > 10) { }
    #                     Elseif (a * 10) { }
    #                 }
    #                 Else { Var e: String; }
    #             }
    #         }
    #     }
    #     """
    #         # Var b: Int = A.c.a;
    #     expect = "Type Mismatch In Statement: If(BinaryOp(*,Id(a),IntLit(10)),Block([]))"
    #     self.assertTrue(TestChecker.test(input,expect,415))
    # def test16(self):
    #     input = """
    #     Class supsuper {
    #         Var ss: Int = 2;
    #     }
    #     Class super : supsuper {
    #         Var s: supsuper;
    #     }
    #     Class A : super {
    #         Var z: Int = 2;
    #         getA(a: Int) {
    #             Var b: Int = 2 + A.s.ss;
    #         }
    #     }
    #     """
    #         # Var b: Int = A.c.a;
    #     expect = "[]"
    #     self.assertTrue(TestChecker.test(input,expect,416))
    # def test17(self):
    #     input = """
    #     Class D {
    #         Var d : Int = 2 + 4 + 6 * 7;
    #     }
    #     Class C {
    #         Var c: Float = 5.2;
    #         Constructor(t: Float; c: String) {

    #         }
    #     }
    #     Class A {
    #         Var b: Float = 3.4;
    #         getA(a: Float) {
    #             Var Cobj: C = New C(3.4, "Hello");
    #             a = Self.b + Cobj.c * D.d;
    #         }
    #     }
    #     """
    #         # Var b: Int = A.c.a;
    #     expect = "[]"
    #     self.assertTrue(TestChecker.test(input,expect,417))
    # def test18(self):
    #     # input = Program([ClassDecl(Id('C'),[AttributeDecl(Static(),VarDecl(Id('$c'),IntType(),IntLiteral(2))),MethodDecl(Instance(),Id('get'),[],Block([])),MethodDecl(Instance(),Id('Constructor'),[VarDecl(Id('a'),FloatType()),VarDecl(Id('b'),StringType())],Block([]))]),ClassDecl(Id('A'),[AttributeDecl(Instance(),VarDecl(Id('b'),ArrayType(3,IntType()))),MethodDecl(Instance(),Id('getA'),[VarDecl(Id('a'),FloatType())],Block([VarDecl(Id('b'),IntType()),VarDecl(Id('Cobj'),ClassType(Id('C')),NewExpr(Id('C'),[FloatLiteral(3.4),StringLiteral('Hello')])),Assign(Id('b'),FieldAccess(Id('Cobj'),Id('$c')))]))])])
    #     input = """
    #     Class C {
    #         Var $c: Int = 2;
    #         get() { }
    #         Constructor(a: Float; b: String) { }
    #     }
    #     Class A {
    #         Var b: Array[Int, 3];
    #         getA(a: Float) {
    #             Var b: Int;
    #             Var Cobj: C = New C(3.4, "Hello");
    #             b = Cobj::$c;
    #         }
    #     }
    #     """
    #     expect = "[]"
    #     self.assertTrue(TestChecker.test(input,expect,418))
    # def test19(self):
    #     input = """
    #     Class C {
    #         Var $c: Int = 2;
    #         get() { }
    #         Constructor(a: Float; b: String) { }
    #     }
    #     Class A {
    #         Var b: Array[Int, 3];
    #         getA(a: Float) {
    #             Var a: Array[Int, 3];
    #             a = Array(4,5,6.7);
    #         }
    #     }
    #     """
    #     expect = "Illegal Array Literal: [IntLit(4),IntLit(5),FloatLit(6.7)]"
    #     self.assertTrue(TestChecker.test(input,expect,419))
    # def test20(self):
    #     input = """
    #     Class A {
    #         Var b: Array[Int, 3];
    #         getA(a: Float) {
    #             Var a: Array[Array[Int, 2], 3];
    #             a = Array(4,5,6);
    #         }
    #     }
    #     """
    #     expect = "Type Mismatch In Statement: AssignStmt(Id(a),[IntLit(4),IntLit(5),IntLit(6)])"
    #     self.assertTrue(TestChecker.test(input,expect,420))
    # def test21(self):
    #     input = """
    #     Class A {
    #         Var b: Array[Int, 3];
    #         getA(a: Float) {
    #             Var b: Float = 12.5;
    #             Var a: Array[Array[Int, 2], 2];
    #             a = Array(
    #                 Array(2,3),
    #                 Array(b,6)
    #             );
    #         }
    #     }
    #     """
    #     expect = "Illegal Array Literal: [Id(b),IntLit(6)]"
    #     self.assertTrue(TestChecker.test(input,expect,421))
    # def test22(self):
    #     input = """
    #     Class C {
    #         getC(a: Int; b: Float) { }
    #     }
    #     Class A {
    #         method() {
    #             Var c: C;
    #             Var b: Int;
    #             b = c.getC(1,2.4);
    #         }
    #     }
    #     """
    #     expect = "Type Mismatch In Expression: CallExpr(Id(c),Id(getC),[IntLit(1),FloatLit(2.4)])"
    #     self.assertTrue(TestChecker.test(input,expect,422))
    # def test23(self):
    #     input = """
    #     Class D {getD(a, b: Int) { Return "Hello From D"; }}
    #     Class C : D {getC(a: Int; b: Float) {Return 3;}}
    #     Class A {method() {
    #             Var c: C;
    #             Var b: Int;
    #             b = c.getD(1,2);}}
    #     """
    #     expect = "Type Mismatch In Statement: AssignStmt(Id(b),CallExpr(Id(c),Id(getD),[IntLit(1),IntLit(2)]))"
    #     self.assertTrue(TestChecker.test(input,expect,423))
    # def test24(self):
    #     input = """
    #     Class D {
    #         getD2() {
    #             Return 2.4 / 5;
    #         }
    #         getD(a, b: Int) { 
    #             Return Self.getD2();
    #         }
    #     }
    #     Class C : D {
    #         getC(a: Int; b: Float) {
    #             Return 3;
    #         }
    #     }
    #     Class A {
    #         method() {
    #             Var c: C;
    #             Var b: Int;
    #             b = c.getD(1,2);
    #         }
    #     }
    #     """
    #     expect = "Type Mismatch In Statement: AssignStmt(Id(b),CallExpr(Id(c),Id(getD),[IntLit(1),IntLit(2)]))"
    #     self.assertTrue(TestChecker.test(input,expect,424))