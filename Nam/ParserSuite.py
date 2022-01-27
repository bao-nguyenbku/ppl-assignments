import unittest
from TestUtils import TestParser
# def test_simple_program(self):
#     """Simple program: int main() {} """
#     input = """int main() {}"""
#     expect = "successful"
#     self.assertTrue(TestParser.test(input,expect,201))

# def test_more_complex_program(self):
#     """More complex program"""
#     input = """int main () {
#         putIntLn(4);
#     }"""
#     expect = "successful"
#     self.assertTrue(TestParser.test(input,expect,202))

# def test_wrong_miss_close(self):
#     """Miss ) int main( {}"""
#     input = """int main( {}"""
#     expect = "Error on line 1 col 10: {"
#     self.assertTrue(TestParser.test(input,expect,203))

class ParserSuite(unittest.TestCase):
    #======================================= 0-9 ==========================================
    # class declaration
    # class ParserSuite(unittest.TestCase):
    def test_13333(self):
        input = """class _nam{
                static int a=1, b= 1;
                final float x=2.1, c=2.4;
                float x,y,z; } """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,200))
    def test_3332(self):
        input = """class _nam{
                final float x=2.1, c=2.4;
                float x,y,z; } """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,201))

    def test_ffffm(self):
        input = """class _nam{
            string[4] x = {"nam","1","2"};
            cls a;
            cls1 b = "2";
            void main(){
                cls a = 1;
            }
        }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,202))
    
    def test_wse(self):
        input = """class _nam extends _hoai {                
            static final int x,y;}"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,203))
    def test_4(self):
        input = """class _nam extends _hoai {                
            static final int x,y = 1.2;
            void func1(){
                string x;
                return 1;
            }
            }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,204))
    def test_5(self):
        input = """class Example1 {
            int factorial(int n){
                x := io.readInt();
                io.writeIntLn(this.factorial(x));
            }
             }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,205))
    def test_6(self):
        input = """class Example1 {
            int factorial(int n){
                this.aPI := 3.14;
                value := x.foo(5);
                l[3] := value * 2;
            }
             }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,206))
    def test_7(self):
        input = """class Example1 { void func(){
            float r,s;
                int[5] a,b;
                #list of statements
                r:=2.0;
                    s:=r*r*this.myPI;
                    a[0]:= s;
                    } }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,207))
    def test_8(self):
        input = """class Example1 {
            void func(){
                return a*b-x.m()[3];
                    } }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,208))
    def test_9(self):
        input = """class Example1 {
            void func(){
                x := 3;
                int[3] m;
                m := {1,2,1.2};
                (a.b[3]).x := 1;
                    } }"""
        expect = "Error on line 4 col 16: int"
        self.assertTrue(TestParser.test(input,expect,209))
    def test_10(self):
        input = """class Example1 {
            void func(){
                x.m()[3] := x.d(3);
                    } }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,210))
    def test_11(self):
        input = """class Example1 {
            void func(){
                if x == 3 then return x; 
                if x == 1 then return x+1;
                else return -1;
                if m.x() != d.g[1] then if a[3]-1 == 3 then return a.x(2)[3]; else return 1;
                    } }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,211))
    def test_12(self):
        input = """class Example1 {
            void func(){
                 if x == 3 then return x; 
                if x == 1 then return x+1;
                else return -1;
                if m.x() != d.g[1] then if a[3]-1 == 3 then return a.x(2)[3]; else return 1; else return 2;
                    } }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,212))
    def test_13(self):
        input = """class Example1{int[] func(){
                 for i := 4 downto x.ss(3) do return a[3 + v.m(1)[5]];
                    } }"""
        expect = "Error on line 1 col 19: ]"
        self.assertTrue(TestParser.test(input,expect,213))
    def test_14(self):
        input = """class Example1 {
            void func(){
                for i := 4 to x.ss(3) 
                do{ if n == 1 then return a[3 + v.m(1)[5]]; else io.writeline("vc");
                    }} }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,214))
    def test_15(self):
        input = """class Example1 {
            void func(){
                cls1 x = new cls1();
                b.m(2,2)[3] := this + nil;
                } }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,215))
    def test_16(self):
        input = """class Example1 {int id;
            cl1 main(){
                io.write(this.id);
                } """
        expect = "Error on line 4 col 18: <EOF>"
        self.assertTrue(TestParser.test(input,expect,216))
    def test_attr_met_13(self):
        input = """
        class school {
            static boolean ID;
            scchool(int a,b) {}
            void makeSchool() {}
        }
        class University extends school {
            University(a,b) {}
        }"""
        expect = "Error on line 8 col 24: ,"
        self.assertTrue(TestParser.test(input, expect, 217))
    def test_attr_met_14(self):
        input = """
        class student {
            final static school sch;
            student(school scch, string ID) {}
        }"""
        expect = "Error on line 4 col 33: string"
        self.assertTrue(TestParser.test(input, expect, 218))
    def test_attr_met_15(self):
        input = """
        class teacher extends student {
            string[3] getDatca(boolean a; school D) {}
        }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 219))
    #======================================= 20-29 ==========================================\
    # test stmt and exp
    def test_assign_stmt(self):
        input = """
        class testData {
            testData(int a; float b) {
                a.b := z + a;
                
                if (a == b) then a := 1;
                if a > b then a : = 2; else a := 2;
            }
        }"""
        expect = "Error on line 7 col 32: :"
        self.assertTrue(TestParser.test(input, expect, 220))
    def test_if_stmt_1(self):
        input = """
        class testData {
            testData(int a,b; float b) {
                a.a.b := z + b;
                a.b[1] := 2 + 1 - 1.0023e-12;
                arr := {1,2,3,4};
                a := 1 + 2 - abc;
                a := new Doctor(1,2,3,z,t);
            }
        }class school {
            static boolean ID;
            school(int a,b) {}
            void makeSchool() {}
        }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 221))
    def test_if_stmt_2(self):
        input = """
        class testData {
            testData(int a,b; float b) {
                if a.v < z[2] then {
                    a := new Block(a.z, b+d);
                    a := a.v.x.a[1];
                }
                else {
                    this.B := Data.block.function(f, "abc");
                }
            }
        }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 222))
    def test_if_stmt_3(self):
        input = """
        class testData {
            testData(int a,b; float b) {
                if a.v < z[2] then {
                    if (a == 1) then {
                        if (a == 1) then {
                            if (a > 1) then {
                                a := 5;
                                b := 6;
                            }
                            else {
                                if a > b then a := 2; else a := 2;
                            }
                        }
                    }
                    else {
                        if a > b then a := 2; else a := 2;
                    }
                }
                
            }
        }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 223))
    def test_for_stmt_1(self):
        input = """
        class testFor {
            testFor() {
                for i:=1 to 10 do a:=a+1;
            }
            testClass callFor() {
                for a.b[2]:=5 downto 25 do a:=a+1;
            }
        }"""
        expect = "Error on line 7 col 21: ."
        self.assertTrue(TestParser.test(input, expect, 224))
    def test_for_stmt_2(self):
        input = """
        class testFor {
            
            testClass callFor() {
                for a:=5 downto 25 do {
                    a := a + 1;
                };
            }
        }"""
        expect = "Error on line 7 col 17: ;"
        self.assertTrue(TestParser.test(input, expect, 225))
    def test_for_stmt_3(self):
        input = """
        class testFor {
            testFor() {
                for i:=1 to 10 do a:=a+1;
            }
            testClass callFor() {
                for a:=5 downto 25 do {
                    a := a + 1;
                };
            }
        }"""
        expect = "Error on line 9 col 17: ;"
        self.assertTrue(TestParser.test(input, expect, 226))
    def test_for_stmt_4(self):
        input = """
        class testFor {
            testFor() {
                for i:=1 to 10 do a:=a+1;
            }
            testClass callFor() {
                for a:=5 downto 25 do {
                    a := a + 1;
                    for a:= 245 to 21 do {
                        a.Pi[5] := 1 + 2;
                    }
                }
            }
        }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 227))
    def test_for_stmt_5(self):
        input = """
        class testFor {
            testFor() {
                for i:=1 to 10 do a:=a+1;
            }
            testClass callFor() {
                for a:=5 downto 25 do {
                    a := a + 1;
                    for a:= 245 to 21 do {
                        a.Pi[5] := 1 + 2;
                        if a.v < z[2] then {
                            if (a == 1) then {
                                if (a == 1) then {
                                    
                                }
                            }
                            else {
                                if a > b then a := 2; else a := 2;
                            }
                        }
                    }
                }
            }
        }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 228))
    def test_for_stmt_6(self):
        input = """
        class testFor {
            testFor() {
                for i:=1 to 10 do a:=a+1;
            }
            testClass callFor() {
                for a:=5 downto 25 do {
                    a := a + 1;
                    for a:= 245 to 21 do {
                        a.Pi[5] := 1 + 2;
                        
                    }
                }
            }
        }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 229))
    # #======================================= 30-39 ==========================================
    def test_for_stmt_7(self):
        input = """
        class testFor {
            testFor() {
                for i:=1 to 10 do a:=a+1;
            }
            testClass callFor() {
                for a:=5 downto 25 do
                                    for a:=5 downto 25 do
                                        /*a:= 2;*/
            }
        }"""
        expect = "Error on line 10 col 12: }"
        self.assertTrue(TestParser.test(input, expect, 230))
    def test_for_stmt_8(self):
        input = """
        class testFor {
            testFor() {
                for i:=1 to 10 do a:=a+1;
            }
            testClass callFor() {
                for a:=5 downto 25 do
                    for a:=5 downto 25 do
                                for a:=5 downto 25 do
                                    for a:=5 downto 25 do
                                        a:= 2;
            }
        }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 231))
    def test_break_con_1(self):
        input = """
        class testData extends PPL {
            void loopTest(int a,v; float c,d; boolean a,s; string str1,str2; Room r1,r2) {
                for i := (a + c -d == f) downto a+(a >=d)/32 do {
                    if a > f-1 then break;
                }
            }
        }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 232))
    def test_break_con_2(self):
        input = """
        class testData extends PPL {
            void loopTest(int a,v; float c,d; boolean a,s; string str1,str2; Room r1,r2) {
            }
        }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 233))
    def test_break_con_3(self):
        input = """
        class testData extends PPL {
            void loopTest(int a,v; float c,d; boolean a,s; string str1,str2; Room r1,r2) {
                for i := (a + c -d == f) downto a+(a >=d)/32 do {
                }
            }
            void loopTest(int a,v; float c,d; boolean a,s; string str1,str2; Room r1,r2) {
                for i := (a + c -d == f) downto a+(a >=d)/32 do {
                    if a > f-1 then break; else continue;
                }
            }
        }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 234))
    def test_break_con_4(self):
        input = """
        class testData extends PPL {
            void loopTest(int a,v; float c,d; boolean a,s; string str1,str2; Room r1,r2) {
                for i := (a + c -d == f) downto a+(a >=d)/32 do {
                    for i := (a + c -d == f) downto a+(a >=d)/32 do {
                                for i := (a + c -d == f) downto a+(a >=d)/32 do {
                                    if a > f-1 then break;
                                }
                                if a > f-1 then break;
                            }
                }
            }
        }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 235))
    def test_break_con_5(self):
        input = """
        class testData extends PPL {
            void loopTest(int a,v; float c,d; boolean a,s; string str1,str2; Room r1,r2) {
                for i := (a + c -d == f) downto a+(a >=d)/32 do {
                    if a > f-1 then break;
                    for i := (a + c -d == f) downto a+(a >=d)/32 do {
                        for i := (a + c -d == f) downto a+(a >=d)/32 do {
                            if a > f-1 then break;
                        }
                        if a > f-1 then break
                    }
                }
            }
        }"""
        expect = "Error on line 11 col 20: }"
        self.assertTrue(TestParser.test(input, expect, 236))
    def test_break_con_6(self):
        input = """
        class testData extends PPL {
            void loopTest(int a,v; float c,d; boolean a,s; string str1,str2; Room r1,r2) {
                for i := (a + c -d == f) downto a+(a >=d)/32 do {
                    if a > f-1 then break;
                    
                    if a > f-1 then break;
                }
            }
        }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 237))
    def test_break_con_7(self):
        input = """
        class testData extends PPL {
            void loopTest(int a,v; float c,d; boolean a,s; string str1,str2; Room r1,r2) {
                for i := (a + c -d == f) downto a+(a >=d)/32 do {
                    if a > f-1 then break;
                }
            }
        }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 238))
    def test_return_1(self):
        input = """
        class School {
            Student cloneStudent(Student stu){
                Student clone = new Student();
                if clone != nil then
                return clone;
                else return nil;
            }
        }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 239))
    # #======================================= 40-49 ==========================================
    def test_return_2(self):
        input = """class Res {
            int Add(int a, b) {
                return a + b;
            }
            float Add(float a,b) {
                return a + b \\ c % 2 / 1 * a;
            }
            boolean Add(boolean a,b) {
                return a || !b && !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!(c == f);
            }
            string Add (string a, "abcd") {
                return a ^ b ^(c ^ d ^ ("abc" ^ fffffffffffffff));
            }
            doctor makeNew(int a; float b) {
                if a== 0 then
                return new doctor(a,b,c,d,1./2);
                else {
                    if a<1 then
                        return this.doctor;
                    else
                        return nil;
                }
            }
        }"""
        expect = '''Error on line 11 col 34: "abcd"'''
        self.assertTrue(TestParser.test(input, expect, 240))
    def test_return_3(self):
        input = """class Res {
            int Add(int a, b) {
                return a + b;
            }
            float Add(float a,b) {
                return a + b \\ c % 2 / 1 * a;
            }
            boolean Add(boolean a,b) {
                return a || !b && !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!(c == f);
            }
            string Add (string a) {
                return a ^ b ^(c ^ d ^ ("abc" ^ fffffffffffffff));
            }
            doctor makeNew(int a; float b) {
                if a== 0 then
                
            }
        }"""
        expect = "Error on line 17 col 12: }"
        self.assertTrue(TestParser.test(input, expect, 241))
    def test_return_4(self):
        input = """class Res {
            int[6] add (int[3] a,b) {
                int[6] res = copy.Array(a,b,res);
                if res.size() != 0 then
                    return res;
                else
                    return {0,0,0,0,0,0};
            }
            void getA() {
                for i:=0 to -1 do {
                    int a = io.getInt();
                    if (a > 0) then {
                        this.a = a;
                        break;
                    }
                }
                this.PrintA();
            }
        }"""
        expect = "Error on line 7 col 27: {"
        self.assertTrue(TestParser.test(input, expect, 242))
    def test_stmt_1(self):
        input = """
        class C1 {
            static int a;
            C1(int a) {
                this.a := a;
                if this.CheckA() == true then this.PrintA();
                else this.getA();
            }
            boolean CheckA() {
                if this.a <= 0 then return false;
                else return true;
            }
            void PrintA() {
                io.print("Data of list" ^ str.makeStr(a));
            }
            
        }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 243))
    def test_stmt_2(self):
        input = """
        class C1 {
            static int a;
            C1(int a) {
                this.a := a;
                if this.CheckA() == true then this.PrintA();
                else this.getA();
            }
            void getA() {
                for i:=0 to -1 do {
                    int a = io.getInt();
                    if (a > 0) then {
                        this.a := a;
                        break;
                    }
                }
                this.PrintA();
            }
        }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 244))
    def test_stmt_3(self):
        input = """
        class C2 {
            static C1 c;
            final static int[5] arr;
            C2(C1 c) {
                this.c := c;
                C1.PrintA();
            }
            void create_skill() {
        can_skill := false;
        have_button := false;
        system.Instantiate(water_skill, new Vector3(-10,0,0), transform.rotation);  
        skill_Audio.Play(0);   
    }
            int[5] getArr() {
                return arr;
            }
        }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 245))
    def test_stmt_4(self):
        input = """
        class C3 extends C2 {
            final string name;
            string getName() {
                return "Name of C3: " ^ name;
            }
            boolean checkName(string n1) {
                return n1 == name;
            }
        }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 246))
    def test_stmt_5(self):
        input = """
        class checkExp {
            void check1(boolean a,b,c) {
                a1:= a > b > c;
            }
        }"""
        expect = "Error on line 4 col 27: >"
        self.assertTrue(TestParser.test(input, expect, 247))
    def test_stmt_6(self):
        input = """
        class checkExp {
            void check1(boolean a,b,c) {
                a1:= a > (b > c);
            }
        }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 248))
    def test_stmt_7(self):
        input = """
        class checkExp {
            void check1(boolean a,b,c) {
                a1:= a > (b > c);
                a2:= ((a==b)!=c)==123;
            }
        }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 249))
    # #======================================= 50-59 ==========================================
    def test_stmt_8(self):
        input = """
        class C3 extends C2 {
            string name;
            C3(string n; C1 c) {
                this.name := n;
            }
            string getName() {
                return "Name of C3: " ^ name;
            }
            boolean checkName(string n1) {
                return n1 == name;
            }
        }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 250))
    def test_stmt_9(self):
        input = """
        class mainClass {
            void main() {
                C1 c1 = new C1();
                C2 c2 = new C2(c1);
                c3 := new C3("abc
                ",c1);
            }
        }"""
        expect = """"abc"""
        self.assertTrue(TestParser.test(input, expect, 251))
    def test_stmt_10(self):
        input = """
        class mainClass {
            void main() {
                c3 := new C3("abc",c1);
                c3.checkName("abcd");
                io.Print(c3.getName());
            }
        }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 252))
    # test random
    def test_only_EOF(self):
        input = """/*no have class
        *****************
        ******************/
        # only have cmt"""
        expect = "Error on line 4 col 23: <EOF>"
        self.assertTrue(TestParser.test(input, expect, 253))
    def test_random_1(self):
        input = """
        # class parent
        class Exp {
            float eval() {}
        }
        # class intlit and floatlit
        class IntLit extends Exp {
            int value;
            Intlit(int a) {
                this.value := a;
            }
            float eval() {
                return this.value;
            }
        }
        # class floatlit and floatlit
        class FloatLit extends Exp {
            float value;
            Intlit(float a) {
                this.value := a;
            }
            float eval() {
                return this.value;
            }
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 254))
    def test_random_2(self):
        input = """
        class UnExp extends Exp {
            string op;
            float value;
            UnExp(string op; float value) {
                this.value := value;
            }
            float eval() {
                if op == "+" then return value;
                else return value * (-1);
            }
            void create_skill() {
        can_skill := false;
        have_button := false;
        system.Instantiate(water_skill, new Vector3(-10,0,0), transform.rotation);  
        skill_Audio.Play(0);   
    }
    void shootWater() {
        for i := 0  to num_bullet do {
            system.Instantiate(bullet_water, fire_point.position, fire_point.rotation);  
            shoot_Audio.Play(0);       
        }
    }
        }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 255))
    def test_random_3(self):
        input = """
        class BinExp extends Exp {
            string op;
            float left,right;
            BinExp(string op; float l,r) {
                this.op := op;
                this.r := r;
            }
            float eval() {
                if op == "+" then return left + right;
                else if op == "-" then return lef - right;
                else if op == "/" then return lef / right;
            }
        }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 256))
    def test_random_4(self):
        input = """class follow_mouse {
    void FixedUpdate () {
        #Get the Screen positions of the object
        float angle = system.AngleBetweenTwoPoints(positionOnScreen, mouseOnScreen);
        transform.rotation =  Quaternion.Euler(new Vector3(0,0,angle - 180));
    }
    void changeState() {
        checkRun := !checkRun;
    }
    # FUNCTION FOR SKILL AND FIRE BULLET
    void create_button_skill() {
        system.Instantiate(button_skill, new Vector3(-6.5,-4,0), transform.rotation);
    }
    float AngleBetweenTwoPoints(Vector3 a, b) {
         return Math.Atan2(a.y - b.y, a.x - b.x) * Math.Rad2Deg;
    }
}"""
        expect = "Error on line 5 col 27: ="
        self.assertTrue(TestParser.test(input, expect, 257))
    def test_random_5(self):
        input = """
class smoke_run extends MonoBehaviour{
    float speed = 5f;
    float counter = 0;
    Vector3 scaleChange;
    void FixedUpdate()
    {
        transform.localScale := transform.localScale + scaleChange;
        if (counter == 100) then {
        }
    }
}"""
        expect = "Error on line 3 col 19: f"
        self.assertTrue(TestParser.test(input, expect, 258))
    def test_random_6(self):
        input = """
class skill_check {
    void FixedUpdate()
    {
        if (Input.GetKeyDown("s")) then {
        }
    }
}"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 259))
    #======================================= 60-69 ==========================================
    def test_random_7(self):
        input = """
class virus_move {
    GameObject myEffect;
    float speed_virus = -0.15;
    void FixedUpdate()
    {
    }
    void OnTriggerEnter2D(Collider2D col) {
        
        if (col.gameObject.tag == "bullet_water") || (col.gameObject.tag == "bullet_water_skill") then {
            system.Destroy(this);
            system.Instantiate(myEffect, transform.position, transform.rotation);
        }
        if (col.gameObject.tag == "bullet_mask") || (col.gameObject.tag == "bullet_water") then system.Destroy(col.gameObject);
    }
}"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 260))
    def test_random_8(self):
        input = """
class drop_victim {
    static float count_time = 0;
void changeState() {
        checkRun := !checkRun;
    }
    # FUNCTION FOR SKILL AND FIRE BULLET
    void create_button_skill() {
        system.Instantiate(button_skill, new Vector3(-6.5,-4,0), transform.rotation);
    }
    void create_skill() {
        can_skill := false;
        have_button := false;
        system.Instantiate(water_skill, new Vector3(-10,0,0), transform.rotation);  
        skill_Audio.Play(0);   
    }
    void shootWater() {
        for i := 0  to num_bullet do {
            system.Instantiate(bullet_water, fire_point.position, fire_point.rotation);  
            shoot_Audio.Play(0);       
        }
    }
    static void Update()
    {
        if (count_time < 5) then transform.position := transform.position + new Vector3(0.5, 0.2, 0);
        else transform.position := transform.position + new Vector3(0.5, -0.1, 0);
    }
}"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 261))
    def test_random_9(self):
        input = """
class control_victim {
    GameObject victim_die;
    GameObject eff;
    float speed_human = -0.15;

    void FixedUpdate()
    {
        transform.position := transform.position + new Vector3(speed_human, 0, 0);
    }
    void OnTriggerEnter2D(Collider2D col) {  
        if (col.gameObject.tag == "bullet_mask") || (col.gameObject.tag == "bullet_water_skill") then {
            system.Destroy(this);
            system.Instantiate(eff, transform.position, transform.rotation);
            system.Instantiate(victim_die, transform.position, transform.rotation);
        }
        if (!checkRun) then {
            # UPDATE PLAYER'S HP
            txt.text := myHP.ToString();
            if (transform.position.y > 6) || (transform.position.y < -6) then this.GameOver();
            # CONTROLL JUMP AND DROP OF PLAYER
            if Input.GetButtonDown("Jump") && !isJump then {
                jumpAudio.Play(0);
                countJump := 4;
                isJump := true;
                counting := 3;
                this.outSmoke();
                this.jumpUp(jumping / 2);
            }
            else if countJump != 0 then {
                if countJump > 3 then    this.jumpUp(jumping);
                else                 this.jumpUp(jumping / 3);
            }
            else {
                this.dropDown();
                if counting == 0 then isJump := false;
            }
        }
        if (col.gameObject.tag == "bullet_water") || (col.gameObject.tag == "bullet_mask") then system.Destroy(col.gameObject);
    }
}"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 262))
    def test_random_10(self):
        input = """
class move {
    

    # FIRE
    Transform fire_point;
    GameObject bullet_water;
    GameObject bullet_mask;
    AudioSource shoot_Audio;
    float num_bullet = 1.;
    float count_trigger = 0;
    # special skill
    

    GameObject Heart;
    float count_kira = -1.0e12;
    void Update() {
        if (Input.GetKeyDown("f")) then {
            this.changeState();
        }
        
    }
    void shootMask() {
        for i := 0 to num_bullet do {
            system.Instantiate(bullet_mask, fire_point.position, fire_point.rotation);  
            shoot_Audio.Play(0);       
        }
    }
    # FUNCTION CONTROLL UFO AND EFFECT WHEN JUMPING
    void outSmoke() {
        system.Instantiate(smoke_pre, smoke_point.position, smoke_point.rotation);
    }
    void jumpUp(float upSize) {
        system.transform.position := transform.position + new Vector3(0, upSize, 0);
    }
    void dropDown() {
        system.transform.position := transform.position + new Vector3(0, falling, 0);
    }
    void GameOver() {
        SceneManager.LoadScene(SceneManager.GetActiveScene().buildIndex - 1);
    }
}"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 263))
    def test_random_11(self):
        input = """
class PlayerMoment extends MonoBehaviour{
    CharacterController ctrller;
    Transform groundCheck;
    float groundDistance = 0.4;
    LayerMask groundMask;

    float speed = 12;
    float gravity = -9.81* 10;
    # Update is called once per frame
    void Update()
    {
        isGrounded := Physics.CheckSphere(groundCheck.position, groundDistance, groundMask);

        if (isGrounded && velocity.y < 0) then {
            velocity.y := -2;
        }
    }
}"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 264))
    def test_random_12(self):
        input = """
class PlayerMoment extends MonoBehaviour{
    float speed = 12;
    float gravity = -9.81 * 10;
    float jumpHeight = 7;
    Vector3 velocity;
    bool isGrounded;
    # Update is called once per frame
    void Update()
    {
        move := transform.right * x + transform.forward * z;
        ctrller.Move(move  * speed * Time.deltaTime);

        if Input.GetButtonDown("Jump") && isGrounded then {
            velocity.y := Mathf.Sqrt(jumpHeight * -2 * gravity);
        }
        io.getInt(num);
            sLec := num;
        velocity.y := velocity.y + gravity * Time.deltaTime;
        ctrller.Move(velocity * Time.deltaTime);
    }
}"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 265))
    def test_random_13(self):
        input = """
class Faculty {
        string name;
        Faculty(string n = "") : name(n) {}
        string getNameFaculty() { return name;  }
        void setNameFaculty(string n) { name := n;  }
}"""
        expect = "Error on line 4 col 25: ="
        self.assertTrue(TestParser.test(input, expect, 266))
    def test_random_14(self):
        input = """
# LECTURER

class Lecturer {
        string name;
        Faculty lecFaculty;
        Lecturer(string n)  { name:=n; }
        Lecturer(string n; Faculty f) { name := n; lecFaculty := f; }
        string getNameFacultyOfLecturer() { return lecFaculty.getNameFaculty(); }
        void setNameFacultyOfLecturer(string n) { lecFaculty.setNameFaculty(n); }
};

# CLASSROOM

class Classroom {
        string nameRoom;
        Classroom(string n) { nameRoom:=n;}
        string getNameClassroom() { return nameRoom; }
        void setNameClassroom(string n) { nameRoom := n; }
}"""
        expect = "Error on line 11 col 1: ;"
        self.assertTrue(TestParser.test(input, expect, 267))
    def test_random_15(self):
        input = """
class Subject {
        string name;
        Lecturer[5] subLecturer;
        int sLec;
        Student(string n; int i; int nS) { name:=n; id:=i; nSub:=nS; }
        void setNameStudent(string n) { name := n;  }
        void setID(int n) { id := n;  }
        void setNameFacultyStudent(string n) { facul := n; }
        string getNameStudent() {io.Print("How many Lecturer? ");
            
            io.print("---------------\\n");
            for j := 0 to num do {
                io.print("Input name of Lecturer " ^ str.toString(j + 1) ^ ":\\n");
                io.fflush(stdin);
                io.getline(n);
                subLecturer.setNameLecturer(n);
                io.print("Input Lecturer's Faculty " ^ str.toString(j + 1) ^ ":\\n");
                io.fflush(stdin);
                io.getline(n);
                subLecturer.setNameFacultyOfLecturer(n);
            } return name;  }
        int getID() { return id;  }
        string getNameFacultyStudent() { return facul.getNameFaculty();  }
};"""
        expect = "Error on line 25 col 1: ;"
        self.assertTrue(TestParser.test(input, expect, 268))
    def test_random_16(self):
        input = """
class Subject {
        string name;
        Lecturer subLecturer;
        int sLec;
        Classroom subRoom;
        Subject(string n) { name:=n; sLec:=0;}
        string getNameSubject() { return name; }
        void setNameSubject(string n) { name := n; }
        void inputData() {
            string n;
            int num;
            io.print("---------------\\n");
            io.print("Input name of Subject: ");
            io.fflush(stdin);
            io.getline(n);
            name := n;
        }
        bool checkRoom(string name) {
            string className = subRoom.getNameClassroom();
            if (className == name) then    return 1;
            return false;
        }
        void checkLect() {
            io.print("List Lecturers of " ^ name ^ ":\\n");
            for i := 0 to sLec do
                io.print(subLecturer.getNameLecturer() ^ endl);
        }
}"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 269))
    # #======================================= 70-79 ==========================================
    def test_random_17(self):
        input = """
# STUDENT

class Student {
        bool findSubject(string name) {
            for i := 0 do
                if (subs.getNameSubject() == name)then return 1;
            return 0;
        }
        void checkLec() {
            for i := 0 to nSub do {
                io.print("\\n----------\\n");
                subs.checkLect();
            }
        }
        bool checkFacuSub(string facu; string sub) {
            if (facul.getNameFaculty() != facu) then   return 0;
            return this.findSubject(sub);
        }
}"""
        expect = "Error on line 6 col 23: do"
        self.assertTrue(TestParser.test(input, expect, 270))
    def test_random_18(self):
        input = """
# STUDENT

class Student {
        bool findSubject(string name) {
            for i := 0 to nSub do
                if (subs.getNameSubject() == name)then return 1;
            return 0;
        }
        void checkLec() {
            for i := 0 to nSub do {
                io.print("\\n----------\\n");
                subs.checkLect();
            }
        }
        bool checkFacuSub(string facu; string sub) {
            if (facul.getNameFaculty() != facu) then   return 0;
            return this.findSubject(sub);
        }
}"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 271))
    def test_random_19(self):
        input =  """
class mainClass {
int main() {
    Faculty facul;
    Lecturer lect;
    Student stud;
    Classroom classR;
    Subject subj;
    int sFacu, sLect, sStud, sRoom, sSubj;
    int n;

    
    #=========================CLASSROOM===========================//
    io.print("\\n=============================================================\\n");
    io.print("How many Classroom? ");
    io.getInt(n);
    sRoom := n;
    for i:=0 to n do {
        string name;
        io.print("---------------------------------\\n");
        io.print("Input details for Classroom " ^ str.toString(i + 1) ^ ":\\n");
        io.print("Input name of Classroom: ");
        io.fflush(stdin);
        io.getline(name);
        classR.setNameClassroom(name);
    }
}

}"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 272))
    def test_random_20(self):
        input = """
class mainClass {
int main() {
    io.print("\\n=============================================================\\n");
    io.print("How many Classroom? ");
    io.getInt(n);
    sRoom := n;
    for i:=0 to n do {
        string name;
        io.print("---------------------------------\\n");
        io.print("Input details for Classroom " ^ str.toString(i + 1) ^ ":\\n");
        io.print("Input name of Classroom: ");
        io.fflush(stdin);
        io.getline(name);
        classR.setNameClassroom(name);
    }
}

}"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 273))
    def test_random_21(self):
        input = """
class display {
    static display dis_instance;
    Text txt;
    void Start()
    {
        if (dis_instance == null) then {
            dis_instance := this;
        }
    }
    static void Display(string str) {
        txt.text := str;
    }
}"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 274))
    def test_random_22(self):
        input = """
class skill{
    string name = "";
    skill(){
        if (this.name == "") then
            this.name := "Skill";
    }
    string getName() {
        return this.name;
    }
    void displayData() {}
}
class factory_skil{
    static skill get_skill(all_skill i) {
        if i == all_skill.FireBall then
                return new FireBall();
        else if i == all_skill.WaterHealing then
                return new WaterHealing();
        else if i == all_skill.RockShield then
                return new RockShield();
        else
                return new skill();
    }
}
class WaterHealing extends skill{
    WaterHealing(){ this.name := "WaterHealing";}
    void displayData() {
        display.dis_instance.Display(this.name);
    }
}"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 275))
    def test_random_23(self):
        input = """
class ButtonRun {
    skill my_skill;
    Text txt;
    void InitButton(skill input_skill) {
        this.my_skill := input_skill;
        txt.text := my_skill.getName();
    }
    void clickButton() {
        my_skill.displayData();
    }
}
class manager_skill {
    ButtonRun list_button;
    manager_skill(all_skill i) {
        list_button.InitButton(factory_skill.get_skill(i));
    }
}"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 276))
    def test_random_24(self):
        input = """
class Bank {
    string bankName;

    void doSomething()
    {
        #
    }
} 
class Vietcombank extends Bank{
    Student(int ID; string name) {
            this.studentID := ID;
            this.name := name;
            numOfGrade := 0;
            sumMark := 0;
        }
        void insertGrade(string nameOfCourse; int mark) {
            grades.setName(nameOfCourse);
            grades.setMark(mark);
            numOfGrade := numOfGrade+1;
            sumMark := sumMark+ mark;
        }
        void setName(string name) { this.nameOfCourse := name; }
        void setMark(int mark)  { this.mark := mark;}
        int getMark()      { return mark; }
}"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 277))
    def test_random_25(self):
        input = """
class Grade {
        string nameOfCourse;
        int mark;
        Grade() {
            nameOfCourse := "";
            mark := 0;
        }
        Grade(string nameOfCourse; int mark) {
            this.nameOfCourse := nameOfCourse;
            this.mark := mark;
        }
}"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 278))
    def test_random_26(self):
        input = """
class Student {
        int studentID;
        float getAverage()  {
            return (float)sumMark / numOfGrade;
        }
};"""
        expect = "Error on line 5 col 20: float"
        self.assertTrue(TestParser.test(input, expect, 279))
    # #======================================= 80-89 ==========================================
    def test_random_27(self):
        input = """
class mainClass {
int main() {
    int n;
    Student students;
    int ID;
    io.print("Enter number of Students? ");
    io.getInt(n);
        # GET INFORMATION
        io.print("Input details for Student " ^ (i + 1) ^ ":\\n");
        students.insertGrade(nameMark, mark);
    n := 1;
    # GET AVERAGE
    for i := true to 1.234E-12 do {
        io.print("Which student average grade? ");
        io.getInt(n);
        if (n > 0) && (n <= students.size()) then
            io.print("Average grade for student " ^ n ^ ": " ^ students.getAverage());
        else
            io.print("Don't have student " ^ n ^ endl);          
        io.print("Mark of Grade " ^ (j + 1) ^ ": ");
        io.getInt(mark);
        students.insertGrade(nameMark, mark);
    n := 1;
        
        if (n == 1) then   io.print("-----\\n");
    }
    return 0;
}
}"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 280))
    def test_random_28(self):
        input = """
class mainClass {
    static void getline(string a) {
        string test = system.getIO();
        a := "";
        for i:=(true && false==true) downto 1. + 2e-123 do{
            a := a^test;
            test := system.getIO();
            if test == "\\n" then break;
            else continue;
        }
    }
    static void fflush(typeIO s) {
        if s == stdin then system.clear_console();
    }
int main() {
    int n;
    Student students;
    int ID;
    io.print("Enter number of Students? ");
    io.getInt(n);
        # GET INFORMATION
        io.print("Input details for Student " ^ (i + 1) ^ ":\\n");
        students.push(new Student(ID, name));
        # GET MARK
        for i := true to 1.234E-12 do {
            io.print("How many Grades? ");
            io.getInt(numOfMark);
            if (numOfMark < 10) then   break;
            io.print("Number of Mark must less than or equal 10!\\n");
        }    
    # GET AVERAGE
    for i := true to 1.234E-12 do {
        io.print("Which student average grade? ");
        io.getInt(n);
        if (n > 0) && (n <= students.size()) then
            io.print("Average grade for student " ^ n ^ ": " ^ students.getAverage());
        else
            io.print("Don't have student " ^ n ^ endl);

        for i := true to 1.234E-12 do  {
            io.print("\\nIf your want to continues, press 1, else, press 0: ");
            io.getInt(n);
            if (n == 1) || (n == 0) then    break;
            io.print("\\"Input 0 or 1!\\"\\n");
        }  
        if (n == 1) then   io.print("-----\\n");
    }
    return 0;
}
}"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 281))
    def test_random_29(self):
        input = """
class io {
    static void getInt(int a) {
        int data = (system.checkIntLitForm(system.getIO())).toInt();
        a := data;
    }
    static void getFloat(float a) {
        float data = (system.checkFloatLitForm(system.getIO())).toFloat();
        a := data;
    }    
}"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 282))
    def test_random_30(self):
        input = """
class heap {
int minWaitingTime(int n; int arrvalTime[]; int[5] completeTime) {
    int curTime = 0;
    int totalWaitTime = 0;

    return totalWaitTime;   
}
}"""
        expect = "Error on line 3 col 40: ["
        self.assertTrue(TestParser.test(input, expect, 283))
    def test_random_31(self):
        input = """
class heap {
int minWaitingTime(int n; int[] arrvalTime; int[5] completeTime) {
    int curTime = 0;

    return totalWaitTime;   
    for i:=((-1!=true||false)==(2\\2/15)) downto xyz do {
        for i := 0 to n do {
            if ((curTime >= arrvalTime[i]) && ((serCos == -1) || (serTime > completeTime[i]))) then {
                    serCos := i;
                    serTime := completeTime[i];
            }
            if (min == -1) || (min > arrvalTime[i]) then   min := arrvalTime[i];
        }
        else    curTime := min;
        if n < 0 then break;
    }
}

}"""
        expect = "Error on line 3 col 30: ]"
        self.assertTrue(TestParser.test(input, expect, 284))
    def test_random_32(self):
        input = """
class heap {
int minWaitingTime(int n; int[5] arrvalTime, completeTime) {
    int curTime = 0;
    return totalWaitTime;   
}
int main() {
    {
        int n = 3;
        int[5] arrvalTime = {0, 1, 2, 3, 4};
        int[5] completeTime = {3, 9, 6, 10, 8};

        io.print(this.minWaitingTime(n, arrvalTime, completeTime));
    }
    io.print(endl);
    string ID;
}
}"""
        expect = "Error on line 16 col 4: string"
        self.assertTrue(TestParser.test(input, expect, 285))
    def test_random_33(self):
        input = """
class student {
    static int num_student;
    string name;
    string[100] getSkill() {
        return list_skill_special;
    }
    int getNumStudent() {
        return num_student;
    }
}"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 286))
    def test_random_34(self):
        input = """
class special_student extends student {
    string[100] list_skill_special;
    int num_skill;
    special_student(string name, id; Class c) {
        this.student(name, id, c);
        num_skill := 0;
        void updateSkill(string skill) {
        this.list_skill_special[num_skill] := skill; 
        num_skill := num_skill + 1;
    }
    }
}"""
        expect = "Error on line 8 col 8: void"
        self.assertTrue(TestParser.test(input, expect, 287))
    def test_random_35(self):
        input = """
class  Class {
    string name;
    student getdStudent(string name, id; Class c; boolean option) {
        if option == true then
            return new special_student(name,id,c);
    }
}"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 288))
    def test_random_36(self):
        input = """
class School {
    static string[50] class_name;
    static int num_class;
    static int getNumClass() {
        return num_class;
    }
    static updateClass(string name) {
        class_name[num_class] := name;
        num_class := num_class + 1;
    }
    void setData(int data) {    }
}"""
        expect = "Error on line 8 col 22: ("
        self.assertTrue(TestParser.test(input, expect, 289))
    # #======================================= 90-99 ==========================================
    def test_random_37(self):
        input = """
class makeSchool {
    void main() {
        for i:=true downto z-1 do {
            string class;
            io.fflush(stdin);
            io.getline(class);
            if class != "-1" then
                School.updateClass(class);
            else break;
        }
    }
    void setNext(node next) {
        this.next := next;
    }
}"""
        expect = "Error on line 5 col 19: class"
        self.assertTrue(TestParser.test(input, expect, 290))
    def test_random_38(self):
        input = """
class makeSchool {
    void main() {
        for i:=true downto z-1 do {
            string new_class;
            io.fflush(stdin);
            io.getline(new_class);
            if new_class != "-1" then
                School.updateClass(new_class);
            else break;
        }
    }
    node getNext() {
        return next;
    }
    
}"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 291))
    def test_random_39(self):
        input = """
class getStudent {
    int main() {
        int n;
        io.getInt(n);
        for i:= 0 to n do {
            string id;
            string new_stu;
            io.fflush(stdin);
            io.getBoolean(option);
            student new_student = (School.getNameClass(range.random() % School.num_class)).getStudent(name,id,option);
            Class.updateStudent(new_student);
        }
    }
}"""
        expect = "Error on line 11 col 20: new_student"
        self.assertTrue(TestParser.test(input, expect, 292))
    def test_random_40(self):
        input = """
class node {
    int data;
    node next;
    node(int data; node next) {
        this.data := data;
        this.next := next;
    }
    int getData() {
        return data;
    }
    
    static void putNode(node n) {
        if n.getNext() == nil then {
            io.getInt(data);
            n.setNext(new node(data, nil));
        }
    }
}"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 293))
    def test_random_41(self):
        input = """
class linked_list {
    static node start;
    linked_list(node s) {
        this.start := s;
    }
    static node getNode(int index; node n) {
        if index == 0 then
            return n;
        else
            return this.getNode(index - 1, n.getNext());
    }
}"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 294))
    def test_random_42(self):
        input = """
class mainFuncion {
    void insert (int index; node root, n) {
        if index == 0 then
            n.setNext(root.getNext());
        else 
            insert(index - 1, root.getNext(), n);
    }
}"""
        expect = "Error on line 7 col 18: ("
        self.assertTrue(TestParser.test(input, expect, 295))
    def test_random_43(self):
        input = """
class mainFuncion {
    void insert (int index; node root, n) {
        if index == 0 then {
            root.setNext(n);
            if index == 0 then
            n.setNext(root.getNext());
        else 
            insert(index - 1, root.getNext(), n);
        }
        else
            array.insert(index - 1, root.getNext(), n);
    }
}"""
        expect = "Error on line 9 col 18: ("
        self.assertTrue(TestParser.test(input, expect, 296))
    # test array literal
    def test_arraylit_1(self):
        input = """
class tesster {
    int[5] getCaculatorInt(int a,b) {
        int[5] arr = {1, a - b, a * bb};
    }
}"""
        expect = "Error on line 4 col 25: a"
        self.assertTrue(TestParser.test(input, expect, 297))
    def test_arraylit_2(self):
        input = """
class tesster {
    int[5] getCaculatorInt(int a,b) {
        cls[5] arr; arr1sd := {a + b, a - b, a * b, a % b, a \\ b};
    }
}"""
        expect = "Error on line 4 col 31: a"
        self.assertTrue(TestParser.test(input, expect, 298))
    def test_arraylit_3(self):
        input = """
class tesster {
    int[5] getCaculatorInt(int a,b) {
        int[5] arr;
        int a132 = a + b;
        int a2 = a- b;
        arr := {a1,a2,a3,a4,a5};
    }
}"""
        expect = "Error on line 7 col 16: a1"
        self.assertTrue(TestParser.test(input, expect, 299))

    
        

