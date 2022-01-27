import unittest
from TestUtils import TestLexer

class LexerSuite(unittest.TestCase):
    #======================================= 0-9 ==========================================
    # test ID
    def test_000(self):
        self.assertTrue(TestLexer.test(" 2cd?","2,cd,Error Token ?",100))
    def test_1(self):
        self.assertTrue(TestLexer.test("ab 2cd?","ab,2,cd,Error Token ?",101))
    def test_2(self):
        self.assertTrue(TestLexer.test("12. + 4e1 * 5.1 - 55.2e-1 / 2e-4","12.,+,4e1,*,5.1,-,55.2e-1,/,2e-4,<EOF>",102))
    def test_3(self):
        self.assertTrue(TestLexer.test("1dfe1.35e2+? ","1,dfe1,.,35e2,+,Error Token ?",103))
    def test_4(self):
        self.assertTrue(TestLexer.test("/* \n 1jsjsufu d11s*/ 12e1 df */","12e1,df,*,/,<EOF>",104))
    def test_5(self):
        self.assertTrue(TestLexer.test("12 xxx/* df\ns*?\rfg*/ 12*/","12,xxx,12,*,/,<EOF>",105))
    def test_6(self):
        self.assertTrue(TestLexer.test("#dfggd \r aa","aa,<EOF>",106))
    def test_7(self):
        self.assertTrue(TestLexer.test("if#dfggd 0.1 true break\n continue","if,continue,<EOF>",107))
    def test_8(self):
        self.assertTrue(TestLexer.test("He#dfggd# 0.1 true break\n llo","He,llo,<EOF>",108))
    def test_9(self):
        self.assertTrue(TestLexer.test("\"xin\\r \\b \\f \\tchao\"",""""xin\\r \\b \\f \\tchao",<EOF>""",109))
    def test_10(self):
        self.assertTrue(TestLexer.test("\"str1?\\n\\r str1\\\" \"",""""str1?\\n\\r str1\\\" ",<EOF>""",110))
    def test_11(self):
        self.assertTrue(TestLexer.test("\"str1 \\\" str1\" \" str2 ?*^&%^$ \\\" str2\"",""""str1 \\\" str1"," str2 ?*^&%^$ \\\" str2",<EOF>""",111))
    def test_12(self):
        self.assertTrue(TestLexer.test("\"str1 \\\" \n \\n str1 1.23 4 10\\b \\f str1\" ","""Unclosed String: "str1 \\\" """,112))
    def test_13(self):
        self.assertTrue(TestLexer.test("\"str1\" int a = 12; \n \" str2 ^%^&*&^%$%#\"",""""str1",int,a,=,12,;," str2 ^%^&*&^%$%#",<EOF>""",113))
    def test_14(self):
        self.assertTrue(TestLexer.test("\"str1 \\\" \n dd \" ","""Unclosed String: "str1 \\\" """,114))
    def test_15(self):
        self.assertTrue(TestLexer.test("\"line 1 df dfff","""Unclosed String: "line 1 df dfff""",115))
    def test_16(self):
        self.assertTrue(TestLexer.test("\"str11\\ \"","""Illegal Escape In String: "str11\ """,116))
    def test_17(self):
        self.assertTrue(TestLexer.test("\"str1  \r ahihi \"","""Unclosed String: "str1  """,117))
    def test_18(self):
        self.assertTrue(TestLexer.test("\"He ask\ned me: \\\"Where \\t is \\a John?\\\"\"","""Unclosed String: "He ask""",118))
    def test_19(self):
        self.assertTrue(TestLexer.test("\"  str \\\" \\\" \n str \"","""Unclosed String: "  str \\\" \\\" """,119))
    def test_20(self):
        self.assertTrue(TestLexer.test("\" \\\\ \\n \\t \\n fddd \\\\\" ","\" \\\\ \\n \\t \\n fddd \\\\\",<EOF>",120))
    def test_21(self):
        self.assertTrue(TestLexer.test("{ 1,2  ,  32,  2}; {1.2,2., 3e8  , 4.0e-1}","{,1,,,2,,,32,,,2,},;,{,1.2,,,2.,,,3e8,,,4.0e-1,},<EOF>",121))
    def test_22(self):
        self.assertTrue(TestLexer.test("{true,false   ,  true, false}; {\" nam\", \" vcl \"  ,  \" aaa \" }",
        """{,true,,,false,,,true,,,false,},;,{," nam",,," vcl ",,," aaa ",},<EOF>""",122))
    def test_el_2(self):
        self.assertTrue(TestLexer.test("12 + 22 - (+110)","12,+,22,-,(,+,110,),<EOF>",123))
    def test_el_3(self):
        self.assertTrue(TestLexer.test("1.0001 * c * 1.9e23","1.0001,*,c,*,1.9e23,<EOF>",124))
    def test_el_4(self):
        self.assertTrue(TestLexer.test("0e123 / // 0E123 \\ 1.e* 0E+123","0e123,/,/,/,0E123,\,1.,e,*,0E+123,<EOF>",125))
    def test_el_5(self):
        self.assertTrue(TestLexer.test("123 + 0.1e12","123,+,0.1e12,<EOF>",126))
    def test_el_6(self):
        self.assertTrue(TestLexer.test("2 + animal.ggf","2,+,animal,.,ggf,<EOF>",127))
    def test_el_7(self):
        self.assertTrue(TestLexer.test("(true || A && || true * false) == (1 == + 2 * pi > 15)", "(,true,||,A,&&,||,true,*,false,),==,(,1,==,+,2,*,pi,>,15,),<EOF>", 128))
    def test_el_8(self):
        self.assertTrue(TestLexer.test("!(a <= b) != /*!!((_f == - (af */ 1.0e-12 + 123)) > 22)","!,(,a,<=,b,),!=,1.0e-12,+,123,),),>,22,),<EOF>",129))
    def test_arrlit_1(self):
        self.assertTrue(TestLexer.test("{1,2}","{,1,,,2,},<EOF>",130))
    def test_arrlit_2(self):
        self.assertTrue(TestLexer.test("{2,true,1}","{,2,,,true,,,1,},<EOF>",131))
    def test_arrlit_3(self):
        self.assertTrue(TestLexer.test("{13.3e2}","{,13.3e2,},<EOF>",132))
    def test_arrlit_4(self):
        self.assertTrue(TestLexer.test("{1, 1 , 34 + 1","{,1,,,1,,,34,+,1,<EOF>",133))
    def test_arrlit_5(self):
        self.assertTrue(TestLexer.test("{1.001, 1.-12, 0e+23}","{,1.001,,,1.,-,12,,,0e+23,},<EOF>",134))
    def test_arrlit_6(self):
        self.assertTrue(TestLexer.test("{true, true, true, a && b - c}","{,true,,,true,,,true,,,a,&&,b,-,c,},<EOF>",135))
    def test_arrlit_7(self):
        self.assertTrue(TestLexer.test("{a + b * 2, dc - sss-_123}","{,a,+,b,*,2,,,dc,-,sss,-,_123,},<EOF>",136))
    def test_arrlit_8(self):
        self.assertTrue(TestLexer.test("{a (a + c)f <= 22, 2 != -_123, -(-23) == _as * pi}","{,a,(,a,+,c,),f,<=,22,,,2,!=,-,_123,,,-,(,-,23,),==,_as,*,pi,},<EOF>",137))
    def test_arrlit_9(self):
        self.assertTrue(TestLexer.test("""{"abcd? as;", "\\"Hi.!\\" Bob said."}""","""{,"abcd? as;",,,"\\\"Hi.!\\\" Bob said.",},<EOF>""",138))
    def test_arrlit_10(self):
        self.assertTrue(TestLexer.test("""{"abc" ^ "123 !!", "\n"}""",'''{,"abc",^,"123 !!",,,Unclosed String: "''',139))
    def test_var_de_1(self):
        self.assertTrue(TestLexer.test("int a =df 2;","int,a,=,df,2,;,<EOF>",140))
    def test_var_de_2(self):
        self.assertTrue(TestLexer.test("float ad3, b = 2;","float,ad3,,,b,=,2,;,<EOF>",141))
    def test_var_de_3(self):
        self.assertTrue(TestLexer.test("int _z3 = 2 + 2 *3 a - (-12) + a / 2;","int,_z3,=,2,+,2,*,3,a,-,(,-,12,),+,a,/,2,;,<EOF>",142))
    def test_var_de_4(self):
        self.assertTrue(TestLexer.test("boolean x=false true;\nboolean z =false;","boolean,x,=,false,true,;,boolean,z,=,false,;,<EOF>",143))
    def test_var_de_5(self):
        self.assertTrue(TestLexer.test("int[4] a;","int,[,4,],a,;,<EOF>",144))
    def test_var_de_6(self):
        self.assertTrue(TestLexer.test("boolean[2] x={true && a || b, (false == z) || t};","boolean,[,2,],x,=,{,true,&&,a,||,b,,,(,false,==,z,),||,t,},;,<EOF>",145))
    def test_var_de_7(self):
        self.assertTrue(TestLexer.test("""string a = "99\\\\ ''", b= "x a!", c ="a \\z" ""","""string,a,=,"99\\\\ ''",,,b,=,"x a!",,,c,=,Illegal Escape In String: "a \z""",146))
    def test_var_de_8(self):
        self.assertTrue(TestLexer.test("int a =0;\n 0.22e-12;\nboolean z = a !=b;","int,a,=,0,;,0.22e-12,;,boolean,z,=,a,!=,b,;,<EOF>",147))
    # check WS and NEWLINE -> SKIP
    def test_ws_1(self):
        self.assertTrue(TestLexer.test("abc\\bb\t\fabc","abc,\,bb,abc,<EOF>",148))
    def test_ws_2(self):
        self.assertTrue(TestLexer.test("a\n\nb\tc\fd\r\r\t\f\tac+123?","a,b,c,d,ac,+,123,Error Token ?",149))
    def test_stmt_1(self):
        self.assertTrue(TestLexer.test("break continue;","break,continue,;,<EOF>",150))
    def test_stmt_2(self):
        self.assertTrue(TestLexer.test("continue;","continue,;,<EOF>",151))
    def test_stmt_3(self):
        self.assertTrue(TestLexer.test("if(a != b)\nthen continuea=a+1;\nelse b=0;","if,(,a,!=,b,),then,continuea,=,a,+,1,;,else,b,=,0,;,<EOF>",152))
    def test_stmt_4(self):
        self.assertTrue(TestLexer.test("return animal(a,b + c);","return,animal,(,a,,,b,+,c,),;,<EOF>",153))
    def test_stmt_5(self):
        self.assertTrue(TestLexer.test("callFunction(1 + 2 * a >= b, 12)","callFunction,(,1,+,2,*,a,>=,b,,,12,),<EOF>",154))
    def test_stmt_6(self):
        self.assertTrue(TestLexer.test("""
            function (a) {
                Var a: Array[Int,2];
                a[1] = 1;
                a[2] = 2;
            }
        """,
        "", 155))
    def test_stmt_7(self):
        self.assertTrue(TestLexer.test("a:=1;\nb[1+c]:=(true && !f || _z)!=false;","a,:=,1,;,b,[,1,+,c,],:=,(,true,&&,!,f,||,_z,),!=,false,;,<EOF>",156))
    def test_stmt_8(self):
        self.assertTrue(TestLexer.test("""animal.cat.talk(s + "abc");""","""animal,.,cat,.,talk,(,s,+,abc,),;,<EOF>""",157))
    def test_stmt_9(self):
        self.assertTrue(TestLexer.test("return abc.getArea(1 true + 2) - (new obj()).arr[1];","return,abc,.,getArea,(,1,true,+,2,),-,(,new,obj,(,),),.,arr,[,1,],;,<EOF>",158))
    def test_stmt_10(self):
        self.assertTrue(TestLexer.test("for i:=10 downto true 0 do {\ncallFunction(); if a == arr[1] then break; else callF();}",
                                       "for,i,:=,10,downto,true,0,do,{,callFunction,(,),;,if,a,==,arr,[,1,],then,break,;,else,callF,(,),;,},<EOF>", 159))
    # #======================================= 60 - 69 ==========================================
    # test method declaration
    def test_met_de_1(self):
        self.assertTrue(TestLexer.test("void true(){}","void,true,(,),{,},<EOF>",160))
    def test_met_de_2(self):
        self.assertTrue(TestLexer.test("int cacul(int true falsea,b) {return a +b;}","int,cacul,(,int,true,falsea,,,b,),{,return,a,+,b,;,},<EOF>",161))
    def test_met_de_3(self):
        self.assertTrue(TestLexer.test("float classCheck(int a,b; float c) { if (a < b) then return c; else return a + b;}",
                                       "float,classCheck,(,int,a,,,b,;,float,c,),{,if,(,a,<,b,),then,return,c,;,else,return,a,+,b,;,},<EOF>",162))
    def test_met_de_4(self):
        self.assertTrue(TestLexer.test("float ?function_test() {}","float,Error Token ?",163))
    def test_met_de_5(self):
        self.assertTrue(TestLexer.test("""void function_test(int a) {/*comment at here*/ getString("input\n");}""",
                                       """void,function_test,(,int,a,),{,getString,(,Unclosed String: "input""",164))
    def test_met_de_6(self):
        self.assertTrue(TestLexer.test("int add(int a,b) {return a+b;}\nfloat add(float a,b) {return a+b;}",
                                       "int,add,(,int,a,,,b,),{,return,a,+,b,;,},float,add,(,float,a,,,b,),{,return,a,+,b,;,},<EOF>", 165))
    def test_met_de_7(self):
        self.assertTrue(TestLexer.test("dog return(int h,t) {#make new dog with h and t\nif(h > t) then return new dog(h,t); else return nil;}#end function",
                                       "dog,return,(,int,h,,,t,),{,if,(,h,>,t,),then,return,new,dog,(,h,,,t,),;,else,return,nil,;,},<EOF>", 166))
    def test_met_de_8(self):
        self.assertTrue(TestLexer.test("string return(string input; int l) {classSTR.getData(input);\nif (l > 0) then return getS()^input; else return input;}",
                                       "string,return,(,string,input,;,int,l,),{,classSTR,.,getData,(,input,),;,if,(,l,>,0,),then,return,getS,(,),^,input,;,else,return,input,;,},<EOF>", 167))
    def test_met_de_9(self):
        self.assertTrue(TestLexer.test("int return(){int data=?getINPUT();return data;}\nint[5] getArray(int l){int[5] arr;\nfor i:=0 to l do arr[i] := getData();\nreturn arr;}",
                                       "int,return,(,),{,int,data,=,Error Token ?",168))
    def test_met_de_10(self):
        self.assertTrue(TestLexer.test(""" string get_Special_String(){return "abc\\g!!";}""",
                                       """string,get_Special_String,(,),{,return,Illegal Escape In String: "abc\g""",169))
    #======================================= 70 - 79 ==========================================
    # test class
    def test_class_1(self):
        self.assertTrue(TestLexer.test("class A{df }","class,A,{,df,},<EOF>",170))
    def test_class_2(self):
        self.assertTrue(TestLexer.test("class A class extends B {}","class,A,class,extends,B,{,},<EOF>",171))
    def test_class_3(self):
        self.assertTrue(TestLexer.test("class A{final int a = 5;/*this is cmt*/}","class,A,{,final,int,a,=,5,;,},<EOF>",172))
    def test_class_4(self):
        self.assertTrue(TestLexer.test("""class str{final static string[3] a_str= {"abc","a\nb","xyz "}}""",
                                       """class,str,{,final,static,string,[,3,],a_str,=,{,"abc",,,Unclosed String: "a""", 173))
    def test_class_5(self):
        self.assertTrue(TestLexer.test("class A {A(int a,b; float c) { callFunction(a + b - c);}}",
                                       "class,A,{,A,(,int,a,,,b,;,float,c,),{,callFunction,(,a,+,b,-,c,),;,},},<EOF>", 174))
    def test_class_6(self):
        self.assertTrue(TestLexer.test("""class A {void float foo() {print("abc")}}\nclass B extends A {int[5] arr;}""",
                                       """class,A,{,void,float,foo,(,),{,print,(,"abc",),},},class,B,extends,A,{,int,[,5,],arr,;,},<EOF>""", 175))
    def test_class_7(self):
        self.assertTrue(TestLexer.test("class A {B makeNew@B()class { return new B();}}","class,A,{,B,makeNew,Error Token @",176))
    def test_class_8(self):
        self.assertTrue(TestLexer.test("class A{} class B {} class C extends A{/*cmt}","class,A,{,},class,B,{,},class,C,extends,A,{,/,*,cmt,},<EOF>",177))
    def test_class_9(self):
        self.assertTrue(TestLexer.test("class A{for i downto := 1 downto 1.0E+123 do x := x + 2;#abc}",
                                       "class,A,{,for,i,downto,:=,1,downto,1.0E+123,do,x,:=,x,+,2,;,<EOF>", 178))
    def test_class_10(self):
        self.assertTrue(TestLexer.test("""class downto obj_zz {if a == b them "string\\"\\"\\"" else "string\\s"}""",
                                       """class,downto,obj_zz,{,if,a,==,b,them,"string\\\"\\\"\\\"",else,Illegal Escape In String: "string\s""",179))
    def test_random_1(self):
        self.assertTrue(TestLexer.test("ascn downto +nad xmmc skc / 223 2.341 + sad - asc ___asint Initlit C++",
                        "ascn,downto,+,nad,xmmc,skc,/,223,2.341,+,sad,-,asc,___asint,Initlit,C,+,+,<EOF>", 180))
    def test_random_2(self):
        self.assertTrue(TestLexer.test("check downto ant downto void ++ 2030/12 if a == b: z++; ",
                                       "check,downto,ant,downto,void,+,+,2030,/,12,if,a,==,b,:,z,+,+,;,<EOF>", 181))
    def test_random_3(self):
        self.assertTrue(TestLexer.test("#downto <stdio.h>\nint main(){}","int,main,(,),{,},<EOF>",182))
    def test_random_4(self):
        self.assertTrue(TestLexer.test("# include <main.h>\n#include <stdlib.h>\n#include <assert.h>\n#include <pthread.h>\n#include <time.h>\nstatic volatile long long incircle=0;\npthread_mutex_t lock;",
                                       "static,volatile,long,long,incircle,=,0,;,pthread_mutex_t,lock,;,<EOF>", 183))
    def test_random_5(self):
        self.assertTrue(TestLexer.test("1x  1z\n3y  main3t(x + z + y + 1) % 3(x + z + t + 1) % 3(x + y + t + 3) % 3(y + t + z + 3) % 3",
                                       "1,x,1,z,3,y,main3t,(,x,+,z,+,y,+,1,),%,3,(,x,+,z,+,t,+,1,),%,3,(,x,+,y,+,t,+,3,),%,3,(,y,+,t,+,z,+,3,),%,3,<EOF>", 184))
    def test_random_6(self):
        self.assertTrue(TestLexer.test(
            "class,A,{,void,foo,(,),{,print,(,abc,),},},class,B,extends,A,{,int,[,5,],arr,;,}",
            "class,,,A,,,{,,,void,,,foo,,,(,,,),,,{,,,print,,,(,,,abc,,,),,,},,,},,,class,,,B,,,extends,,,A,,,{,,,int,,,[,,,5,,,],,,arr,,,;,,,},<EOF>", 185))
    def test_random_7(self):
        self.assertTrue(TestLexer.test("""#include <iostream>
using namespace std;
int main() {
    for (int x = 1; x < 10; x++)
        for (int y = 1; y < 10; y++)
            
                }
}""", "using,namespace,std,;,int,main,(,),{,for,(,int,x,=,1,;,x,<,10,;,x,+,+,),for,(,int,y,=,1,;,y,<,10,;,y,+,+,),},},<EOF>", 186))
    def test_random_8(self):
        self.assertTrue(TestLexer.test("""if (N >= 10000)	num_of_thread = 1000;
	                                      else  if = 1;""",
                                          "if,(,N,>=,10000,),num_of_thread,=,1000,;,else,if,=,1,;,<EOF>", 187))
    def test_random_9(self):
        input = """printf("PI = %f\n", 4.0 * incircle / N);
	printf("TIME = %d sec\n", (if int)(time(NULL) - start));
	if(&lock);
	pthread_exit(NULL);"""
        output = """printf,(,Unclosed String: "PI = %f"""
        self.assertTrue(TestLexer.test(input,output,188))
    def test_random_10(self):
        input = """for(void void i = 0; i <= num_of_thread; i++) {
		if (i != num_of_thread)
			void(&threads[i], NULL, runner, (void *) loop_per_thread);
		else
			pthread_create(&threads[i], NULL, runner, (void *) (N % num_of_thread));
	}"""
        output = """for,(,void,void,i,=,0,;,i,<=,num_of_thread,;,i,+,+,),{,if,(,i,!=,num_of_thread,),void,(,Error Token &"""
        self.assertTrue(TestLexer.test(input, output, 189))
    # #======================================= 90 - 99 ==========================================
    def test_random_11(self):
        input ="""
        void add(int s, int t) {
        Interval newBus;
        else if (insertBus(newBus)) {
            insertData(1, s);
            insertData(0, t);newBus.start = s;
        newBus.end = t;
        }
    }"""
        output = "void,add,(,int,s,,,int,t,),{,Interval,newBus,;,else,if,(,insertBus,(,newBus,),),{,insertData,(,1,,,s,),;,insertData,(,0,,,t,),;,newBus,.,start,=,s,;,newBus,.,end,=,t,;,},},<EOF>"
        self.assertTrue(TestLexer.test(input,output,190))
    def test_random_12(self):
        input = """    void remove(int s, int t) {
        Interval deleteBus;
        deleteBus.start = s;
        deleteBus.end = t;
        else if (insertBus(deleteBus)) {
            insertData(1, s);
newBus.start = s;
        newBus.end = t;            findMax();
        }
    }
    int minPark() {
        return max;
    }"""
        output = "void,remove,(,int,s,,,int,t,),{,Interval,deleteBus,;,deleteBus,.,start,=,s,;,deleteBus,.,end,=,t,;,else,if,(,insertBus,(,deleteBus,),),{,insertData,(,1,,,s,),;,newBus,.,start,=,s,;,newBus,.,end,=,t,;,findMax,(,),;,},},int,minPark,(,),{,return,max,;,},<EOF>"
        self.assertTrue(TestLexer.test(input, output, 191))
    def test_random_13(self):
        input = """/*cmt cmt cmt##### /*/*findMax abcd #123123\n\\z\t \\" 123 abc##### \\" \n"""
        output = """*,findMax,abcd,\,z,\,Unclosed String: " 123 abc##### \\\" """
        self.assertTrue(TestLexer.test(input, output, 192))
    def test_random_14(self):
        input = """Interval(findMax start = 0, int end = 0) {
            this->start = start;
            this->end = end;
        }
        bool operator<(Interval &a) {
            if (this->start < a.start)    return 1;
            if (this->start > a.start)    return 0;
findMax()            return 0;
        }
        
        }"""
        output = "Interval,(,findMax,start,=,0,,,int,end,=,0,),{,this,-,>,start,=,start,;,this,-,>,end,=,end,;,},bool,operator,<,(,Interval,Error Token &"
        self.assertTrue(TestLexer.test(input, output, 193))
    def test_random_15(self):
        input = """void create_button_skill() {
        Instantiate(button_skill, new Vector3(-6.5f,-4f,0f), transform.rotation);
    }
    void shootMask() {
        for (int i = 0; i < num_bullet; i++) {
            Instantiate(bullet_mask, fire_point.position, fire_point.rotation);  
            shoot_Audio.Play(0);       
        }
    }"""
        output = "void,create_button_skill,(,),{,Instantiate,(,button_skill,,,new,Vector3,(,-,6.5,f,,,-,4,f,,,0,f,),,,transform,.,rotation,),;,},void,shootMask,(,),{,for,(,int,i,=,0,;,i,<,num_bullet,;,i,+,+,),{,Instantiate,(,bullet_mask,,,fire_point,.,position,,,fire_point,.,rotation,),;,shoot_Audio,.,Play,(,0,),;,},},<EOF>"
        self.assertTrue(TestLexer.test(input, output, 194))
    def test_random_16(self):
        input = """void GameOver() {
        /*  UPDATE LATE
        **  EXPLOSION :))
        */
    }"""
        output = "void,GameOver,(,),{,},<EOF>"
        self.assertTrue(TestLexer.test(input, output, 195))
    def test_random_17(self):
        input = """using System.Collections;
using System.Collections.Generic;
using UnityEngine.SceneManagement;
using UnityEngine.UI;voidvoid void
findMax
public class move : MonoBehaviour"""
        output = "using,System,.,Collections,;,using,System,.,Collections,.,Generic,;,using,UnityEngine,.,SceneManagement,;,using,UnityEngine,.,UI,;,voidvoid,void,findMax,public,class,move,:,MonoBehaviour,<EOF>"
        self.assertTrue(TestLexer.test(input, output, 196))
    def test_random_18(self):
        input = """n = int(input("Nhap n = "))
count  = 0
for i in range(n) :
    count += i*i
count3 = 0.0
for i in range(1,n + 1):
    count3 += 1/i
count5 = 0.0
    fac *= i
    s += fac"""
        output = '''n,=,int,(,input,(,"Nhap n = ",),),count,=,0,for,i,in,range,(,n,),:,count,+,=,i,*,i,count3,=,0.0,for,i,in,range,(,1,,,n,+,1,),:,count3,+,=,1,/,i,count5,=,0.0,fac,*,=,i,s,+,=,fac,<EOF>'''
        self.assertTrue(TestLexer.test(input, output, 197))
    def test_random_19(self):
        input = """num  = float(input("Moi ban nhap so :"))
fl = num - int(num)
#[0,0.25)    => 0
#[0.25,0.75) => 0.5
fl = int(fl * 4)
print("So lam tron :",float(int(num) + myroud[fl]))"""
        output = """num,=,float,(,input,(,"Moi ban nhap so :",),),fl,=,num,-,int,(,num,),fl,=,int,(,fl,*,4,),print,(,"So lam tron :",,,float,(,int,(,num,),+,myroud,[,fl,],),),<EOF>"""
        self.assertTrue(TestLexer.test(input, output, 198))
    def test_random_20(self):
        input = """money = int(input("dd"))
print(f"{money//50} to 50 ,{money%50//20} to 20 ,{money%50%20//10} to 10 ,{money%50%20%10//5} to 5,{money%50%20%10%5//2} to 2,{money%50%20%10%5%2} to 1")"""
        output = """money,=,int,(,input,(,"dd",),),print,(,f,"{money//50} to 50 ,{money%50//20} to 20 ,{money%50%20//10} to 10 ,{money%50%20%10//5} to 5,{money%50%20%10%5//2} to 2,{money%50%20%10%5%2} to 1",),<EOF>"""
        self.assertTrue(TestLexer.test(input, output, 199))
