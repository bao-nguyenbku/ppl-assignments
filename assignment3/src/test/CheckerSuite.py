import unittest
from TestUtils import TestChecker
from AST import *

class CheckerSuite(unittest.TestCase):
    '''!Warning: when method has not been visited, how to get return type?'''
    def test(self):
        input = """
        Class B { 
            Constructor() { }
        }
        Class A : B {
            Val c: Float = 4.3;
            Val b: Float = 5 + Self.c;
            Val a: Float = Self.b + 5; 
        }
        
        """
        expect = "[]"
        self.assertTrue(TestChecker.test(input,expect,400))
    # def test0(self):
    #     input = """
    #     Class Dog : Animal {
    #         Val $a : Int = 3.2;
    #         $getDog() { }
    #         Constructor () { }
    #         Destructor () { }
    #     }
    #     Class Meow {
    #         $set() { }
    #         Constructor () { }
    #         Destructor () { }
    #     }
    #     Class Program {main(){}}
    #     """
    #     expect = "Type Mismatch In Statement: ConstDecl(Id($a),IntType,FloatLit(3.2))"
    #     self.assertTrue(TestChecker.test(input,expect,400))
    # def test1(self):
    #     input = """
    #     Class A {
    #         Var $a: Int;
    #         Constructor () { }
    #         Destructor () { }
    #     }
    #     Class A {
    #         Val $b: Float;
    #         Constructor () { }
    #         Destructor () { }
    #     }
    #     Class Program {main(){}}
    #     """
    #     expect = "Redeclared Class: A"
    #     self.assertTrue(TestChecker.test(input,expect,401))

    # def test2(self):
    #     input = """
    #     Class Program {main(){}}
    #     Class A {
    #         Val $a: Int = 2 + True;
    #         Constructor () { }
    #         Destructor () { }
    #     }
    #     """
    #     expect = "Type Mismatch In Expression: BinaryOp(+,IntLit(2),BooleanLit(True))"
    #     self.assertTrue(TestChecker.test(input,expect,402))
    # def test3(self):
    #     input = """
    #     Class A {
    #         Val $a: Int = 3;
    #         Constructor () { }
    #         Destructor () { }
    #     }
    #     Class Program {main(){}}
    #     Class B {
    #         Val $b: A = New A();
    #         Constructor () { }
    #         Destructor () { }
    #     }
    #     """
    #     expect = "[]"
    #     self.assertTrue(TestChecker.test(input,expect,403))

    # def test4(self):
    #     input = """
    #     Class Program {main(){}}
    #     Class B: A {
    #         Val $r :Int = 2 + 2 * 2.5;
    #         Var a: Boolean = True;
    #         setA(a: Int) { }
    #         Constructor () { }
    #         Destructor () { }
    #     }
    #     """
    #     expect = "Type Mismatch In Statement: ConstDecl(Id($r),IntType,BinaryOp(+,IntLit(2),BinaryOp(*,IntLit(2),FloatLit(2.5))))"
    #     self.assertTrue(TestChecker.test(input,expect,404))
    # def test5(self):
    #     input = """
    #     Class Program {main(){}}
    #     Class B: A {
    #         Var t: Float = 1.4 % 3; 
    #         setA(a: Int) { }
    #         Constructor () { }
    #         Destructor () { }
    #     }
    #     """
    #     expect = "Type Mismatch In Expression: BinaryOp(%,FloatLit(1.4),IntLit(3))"
    #     self.assertTrue(TestChecker.test(input,expect,405))
    # def test6(self):
    #     input = """
    #     Class Program {main(){}}
    #     Class A {
    #         Var a: Array[Array[Int, 2], 2] = Array(
    #                                             Array(3,6),
    #                                             Array(8,9.2)
    #         );
    #         Constructor () { }
    #         Destructor () { }
    #     }
    #     """
    #     expect = "Illegal Array Literal: [IntLit(8),FloatLit(9.2)]"
    #     self.assertTrue(TestChecker.test(input,expect,406))
    # def test7(self):
    #     input = """
    #     Class Program {main(){}}
    #     Class A {
    #         Var a: Int = 120;
    #         Val $a: C = New C();
    #         Constructor () { }
    #         Destructor () { }
    #     }
    #     """
    #     expect = "Undeclared Class: C"
    #     self.assertTrue(TestChecker.test(input,expect,407))
    # def test8(self):
    #     input = """
    #     Class Program {main(){}}
    #     Class A {
    #         Var a, t, r: Int = 120, 12 * 60 - 9, 1e4;
    #         Constructor () { }
    #         Destructor () { }
    #     }
    #     """
    #     expect = "Type Mismatch In Statement: VarDecl(Id(r),IntType,FloatLit(10000.0))"
    #     self.assertTrue(TestChecker.test(input,expect,408))
    # def test9(self):
    #     input = """
    #     Class Program {main(){}}
    #     Class B {
    #         Val C: String;
    #         Constructor () { }
    #         Destructor () { }
    #     }
    #     """
    #     expect = "Illegal Constant Expression: None"
    #     self.assertTrue(TestChecker.test(input,expect,409))
    # def test10(self):
    #     input = """
    #     Class Program {main(){}}
    #     Class A {
    #         Val $a: Int = 3;
    #         Constructor(a: Float; b: Int) { }
    #         Destructor () { }
    #     }
    #     Class B {
    #         Val $b: A = New A(1, 3.2);
    #         Constructor () { }
    #         Destructor () { }
    #     }
    #     """
    #     expect = "Type Mismatch In Expression: NewExpr(Id(A),[IntLit(1),FloatLit(3.2)])"
    #     self.assertTrue(TestChecker.test(input,expect,410))
    # def test11(self):
    #     input = """
    #     Class Program {main(){}}
    #     Class A {
    #         Var z: Int;
    #         getA(a: Int) {
    #             Var b: Int;
    #             Foreach (b In 1 .. 10) { 
    #                 If (b > 4) { Var c: Float = 2; }
    #             }
    #         }
    #         Constructor () { }
    #         Destructor () { }
    #     }
    #     """
    #         # Var b: Int = A.c.a;
    #     expect = "Type Mismatch In Statement: VarDecl(Id(c),FloatType,IntLit(2))"
    #     self.assertTrue(TestChecker.test(input,expect,411))
    # def test12(self):
    #     input = """
    #     Class Program {main(){}}
    #     Class A {
    #         Var z: Int;
    #         getA(a: Int) {
    #             Foreach (b In 1 .. 10) { }
    #         }
    #         Constructor () { }
    #         Destructor () { }
    #     }
    #     """
    #         # Var b: Int = A.c.a;
    #     expect = "Undeclared Variable: b"
    #     self.assertTrue(TestChecker.test(input,expect,412))
    # def test13(self):
    #     input = """
    #     Class Program {main(){}}
    #     Class A {
    #         Var z: Int;
    #         getA(a: Int) {
    #             Var b: Int;
    #             Foreach (b In 1.2 .. 10.5) { }
    #         }
    #         Constructor () { }
    #         Destructor () { }
    #     }
    #     """
    #         # Var b: Int = A.c.a;
    #     expect = "Type Mismatch In Statement: For(Id(b),FloatLit(1.2),FloatLit(10.5),IntLit(1),Block([])])"
    #     self.assertTrue(TestChecker.test(input,expect,413))
    # def test14(self):
    #     input = """
    #     Class Program {main(){}}
    #     Class A {
    #         Var z: Int;
    #         getA(a: Int) {
    #             Var b: Int;
    #             Foreach (b In 1 .. 100) {
    #                 If (b + 4) { }
    #                 Else { Var e: String; }
    #             }
    #         }
    #         Constructor () { }
    #         Destructor () { }
    #     }
    #     """
    #         # Var b: Int = A.c.a;
    #     expect = "Type Mismatch In Statement: If(BinaryOp(+,Id(b),IntLit(4)),Block([]),Block([VarDecl(Id(e),StringType)]))"
    #     self.assertTrue(TestChecker.test(input,expect,414))
    # def test15(self):
    #     input = """
    #     Class Program {main(){}}
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
    #         Constructor () { }
    #         Destructor () { }
    #     }
    #     """
    #         # Var b: Int = A.c.a;
    #     expect = "Type Mismatch In Statement: If(BinaryOp(*,Id(a),IntLit(10)),Block([]))"
    #     self.assertTrue(TestChecker.test(input,expect,415))
    # def test16(self):
    #     input = """
    #     Class Program {main(){}}
    #     Class supsuper {
    #         Var ss: Int = 2;
    #         Constructor () { }
    #         Destructor () { }
    #     }
    #     Class super : supsuper {
    #         Var s: supsuper;
    #         Constructor () { }
    #         Destructor () { }
    #     }
    #     Class A : super {
    #         Var z: Int = 2;
    #         getA(a: Int) {
    #             Var b: Int = 2 + A.s.ss;
    #         }
    #         Constructor () { }
    #         Destructor () { }
    #     }
    #     """
    #     expect = "Illegal Member Access: FieldAccess(Id(A),Id(s))"
    #     self.assertTrue(TestChecker.test(input,expect,416))
    # def test17(self):
    #     input = """
    #     Class D {
    #         Var d : Int = 2 + 4 + 6 * 7;
    #         Constructor () { }
    #         Destructor () { }
    #     }
    #     Class Program {main(){}}
    #     Class C {
    #         Var c: Float = 5.2;
    #         Constructor(t: Float; c: String) {}
    #         Destructor () { }
    #     }
    #     Class A {
    #         Var b: Float = 3.4;
    #         getA(a: Float) {
    #             Var Cobj: C = New C(3.4, "Hello");
    #             a = Self.b + Cobj.c * D.d;
    #         }
    #         Constructor () { }
    #         Destructor () { }
    #     }
    #     """
    #         # Var b: Int = A.c.a;
    #     expect = "Illegal Member Access: FieldAccess(Id(Cobj),Id(c))"
    #     self.assertTrue(TestChecker.test(input,expect,417))
    # def test18(self):
    #     # input = Program([ClassDecl(Id('C'),[AttributeDecl(Static(),VarDecl(Id('$c'),IntType(),IntLiteral(2))),MethodDecl(Instance(),Id('get'),[],Block([])),MethodDecl(Instance(),Id('Constructor'),[VarDecl(Id('a'),FloatType()),VarDecl(Id('b'),StringType())],Block([]))]),ClassDecl(Id('A'),[AttributeDecl(Instance(),VarDecl(Id('b'),ArrayType(3,IntType()))),MethodDecl(Instance(),Id('getA'),[VarDecl(Id('a'),FloatType())],Block([VarDecl(Id('b'),IntType()),VarDecl(Id('Cobj'),ClassType(Id('C')),NewExpr(Id('C'),[FloatLiteral(3.4),StringLiteral('Hello')])),Assign(Id('b'),FieldAccess(Id('Cobj'),Id('$c')))]))])])
    #     input = """
    #     Class C {
    #         Var $c: Int = 2;
    #         get() { }
    #         Constructor(a: Float; b: String) { }
    #         Destructor () { }
    #     }
    #     Class Program {main(){}}
    #     Class A {
    #         Var b: Array[Int, 3];
    #         getA(a: Float) {
    #             Var b: Int;
    #             Var Cobj: C = New C(3.4, "Hello");
    #             b = Cobj::$c;
    #         }
    #         Constructor () { }
    #         Destructor () { }
    #     }
    #     """
    #     expect = "Undeclared Class: Cobj"
    #     self.assertTrue(TestChecker.test(input,expect,418))
    # def test19(self):
    #     input = """
    #     Class C {
    #         Var $c: Int = 2;
    #         get() { }
    #         Destructor () { }
    #         Constructor(a: Float; b: String) { }
    #     }
    #     Class Program {main(){}}
    #     Class A {
    #         Var b: Array[Int, 3];
    #         getA(a: Float) {
    #             Var a: Array[Int, 3];
    #             a = Array(4,5,6.7);
    #         }
    #         Constructor () { }
    #         Destructor () { }
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
    #         Constructor () { }
    #         Destructor () { }
    #     }
    #     Class Program {main(){}}
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
    #         Constructor () { }
    #         Destructor () { }
    #     }
    #     Class Program {main(){}}
    #     """
    #     expect = "Illegal Array Literal: [Id(b),IntLit(6)]"
    #     self.assertTrue(TestChecker.test(input,expect,421))
    # def test22(self):
    #     input = """
    #     Class C {
    #         getC(a: Int; b: Float) { }
    #         Constructor () { }
    #         Destructor () { }
    #     }
    #     Class Program {main(){}}
    #     Class A {
    #         method() {
    #             Var c: C;
    #             Var b: Int;
    #             b = c.getC(1,2.4);
    #         }
    #         Constructor () { }
    #         Destructor () { }
    #     }
    #     """
    #     expect = "Type Mismatch In Expression: CallExpr(Id(c),Id(getC),[IntLit(1),FloatLit(2.4)])"
    #     self.assertTrue(TestChecker.test(input,expect,422))
    # def test23(self):
    #     input = """
    #     Class D {getD(a, b: Int) { Return "Hello From D"; }
    #     Constructor () { }
    #         Destructor () { }}
    #     Class C : D {getC(a: Int; b: Float) {Return 3;}
    #     Constructor () { }
    #         Destructor () { }}
    #     Class A {method() {
    #             Var c: C;
    #             Var b: Int;
    #             b = c.getD(1,2);}
    #             Constructor () { }
    #         Destructor () { }}
    #     Class Program {main(){}}
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
    #         Constructor () { }
    #         Destructor () { }
    #     }
    #     Class Program {main(){}}
    #     Class C : D {
    #         getC(a: Int; b: Float) {
    #             Return 3;
    #         }
    #         Constructor () { }
    #         Destructor () { }
    #     }
    #     Class A {
    #         method() {
    #             Var c: C;
    #             Var b: Int;
    #             b = c.getD(1,2);
    #         }
    #         Constructor () { }
    #         Destructor () { }
    #     }
    #     """
    #     expect = "Type Mismatch In Statement: AssignStmt(Id(b),CallExpr(Id(c),Id(getD),[IntLit(1),IntLit(2)]))"
    #     self.assertTrue(TestChecker.test(input,expect,424))
    # def test25(self):
    #     input = """
    #     Class Animal{
    #         Var $name : String = "aaaaa";
    #         Var sex : String = "Male";
    #         Constructor () { }
    #         Destructor () { }
    #     }
    #     Class Program {main(){}}
    #     Class Dog : Animal{
    #         Var $a : Int = 5 + 6 - 7 * 8;
    #         Var $b : Float = 5.6 * 9;
    #         Var $c : Int = Dog::$a - 8;
    #         Var $d : Float = Dog::$a * Dog::$b;
    #         Var $e : String = Animal::$name;
    #         Var d : String = "Hello";
    #         Var e : String = Self.d;
    #         Var meomeo : Int = (Meo::$e - 89) * 9600;
    #         Bark(a, b, c : String; d, e, f : Float){}
    #         Constructor () { }
    #         Destructor () { }
    #     }
    #     Class Meo : Animal{
    #         Var $e : Int = 6;
    #         MeowMeow(a : Float){}
    #         Constructor () { }
    #         Destructor () { }
    #     }
    #     """
    #     expect = "[]"
    #     self.assertTrue(TestChecker.test(input,expect,425))
    # def test26(self):
    #     input = """
    #     Class Program{
            
    #     }
    #     Class Program{
            
    #     }
    #     """
    #     expect = "Redeclared Class: Program"
    #     self.assertTrue(TestChecker.test(input,expect,426))
    # def test27(self):
    #     input = """
    #     Class Animal{
    #         Var $name : String = "aaaaa";
    #         Var sex : String = "Male";
    #         Constructor(name : String) {
                
    #         }
    #         Destructor() { }
    #     }
    #     Class Dog : Animal{
    #         Var $meo : Meo = New Meo(5.6, 7);
    #         Var $a : Int = 5 + 6 - 7 * 8;
    #         Var $b : Float = Dog::$a;
    #         Var $c : Int = Dog::$a - 8;
    #         Var $d : Float = Dog::$a * Dog::$b;
    #         Var $e : String = Animal::$name;
    #         Var d : String = "Hello";
    #         Var e : String = Self.d;
    #         Var meomeo : Int = (Meo::$e - 89) * 9600;
    #         Var $arr : Array[Int, 5];
    #         Var $arr2 : Array[Int, 6] = Array(1, 2, 3, 4, 5, 6);
    #         Constructor(name : String) { }
    #         Bark(a, b, c : String; d, e, f : Float) { }
    #         Destructor() { }
    #         Val $ffff : Meo = New Animal("Cat");
    #     }
    #     Class Meo : Animal{
    #         Var $e : Int = 6;
    #         Constructor (a : Float; b : Int) { }
    #         Destructor() { }
    #     }
    #     Class Program {
    #         main () { }
    #     }
    #     """
    #     expect = "[]"
    #     self.assertTrue(TestChecker.test(input,expect,427))
    # def test28(self):
    #     input = """
    #     Class Program{
    #         Var $a : Array[Array[Int, 1],2] = Array(Array(1), Array(2.3));
    #         main() { }
    #     }
    #     """
    #     expect = "[]"
    #     self.assertTrue(TestChecker.test(input,expect,428))
    # def test29(self):
    #     input = """
    #     Class Program : Animal{
    #         Var a : Program = New Animal(Array(Array(1, 2), Array(3, 4)));
    #         main () { }
    #     }
    #     Class Animal {
    #         Constructor (a : Array[Array[Int, 2], 2]){ }
    #         Destructor() { }
    #     }
    #     """
    #     expect = "[]"
    #     self.assertTrue(TestChecker.test(input,expect,429))
    # def test30(self):
    #     input = """
    #     Class Unit 
    #     {
    #         Constructor (a : Int; b : String){ }
    #         Destructor () { }
    #     }
    #     Class Character : Unit
    #     {
    #         Constructor () { }
    #         Destructor () { }
    #     }
    #     Class Player : Character
    #     {
    #         Constructor (a : Array[Int, 7]; b : Float; c : String){}
    #         Destructor(){}
    #     }
    #     Class Health : Player
    #     {
    #         Constructor ()
    #         {}
    #         Destructor(){}
    #     }
    #     Class Program
    #     {
    #         Var a : Health = New Unit(2, "Hieu");
    #         Val $b : Character = New Character();
    #         Var player : Health = New Player(Array(1, 4, 5, 3, 5, 6, 6), 6.5, "Henry");
    #         main () { }
    #         Destructor(){}
    #     }
    #     """
    #     expect = "[]"
    #     self.assertTrue(TestChecker.test(input,expect,430))
    # def test31(self):
    #     input = """
    #     Class Program
    #     {
    #         Var a : Array[Array[Array[Int, 5], 2], 3] = 
    #             Array(
    #                 Array(
    #                     Array(1, 2, 3, 4, 5), 
    #                     Array(6, 7, 8, 9, 10)
    #                 ), 
    #                 Array(
    #                     Array(1, 2, 3, 4, 5),
    #                     Array(6, 7, 8, 9, 10)
    #                 ), 
    #                 Array(
    #                     Array(1, 2, 3, 4, 5), 
    #                     Array(6, 7, 8, 9, 10)
    #                 )
    #         );
    #         Var b : Array[Int, 5] = Self.a[1][0];
    #         Var c : Array[Array[Int, 5], 2] = Self.a[2];
    #         Var d : Array[Array[Array[Int, 5], 2], 3] = Self.a;
    #         Constructor ()
    #         {
                
    #         }
    #         Destructor() 
    #         {
                
    #         }
    #         main () { }
    #     }
    #     """
    #     expect = "[]"
    #     self.assertTrue(TestChecker.test(input,expect,431))
    # def test32(self):
    #     input = """
    #     Class Program {
    #         main() { }
    #     }
    #     Class Animal {
    #         Var d: String = "Hello" +. " World";
    #         Var e: Boolean = (2 > 4) && !(2 < 9);
    #         Var a: Animal;
    #         Var b: Int = 2 + 5 * 7;
    #         Var c: Float = 2 * 7 + 4.5 - e4;
    #         Constructor () { }
    #         Destructor () { }
    #     }
        
    #     """
    #     expect = "Undeclared Identifier: e4"
    #     self.assertTrue(TestChecker.test(input,expect,432))
    # def test33(self):
    #     input = """
    #     Class sieuSuper {
    #         Var s: Float = 2;
    #         getD() { Return 2; }
    #     }
    #     Class super : sieuSuper {
    #         Var a: Int = 2;
    #         Var $a: Int = 4;
    #     }
    #     Class child : super {
    #         Var b: Int = Self.getD();
    #     }
        
    #     """
    #     expect = "[]"
    #     self.assertTrue(TestChecker.test(input,expect,433))