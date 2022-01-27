import unittest
from TestUtils import TestLexer


class LexerSuite(unittest.TestCase):

    def test_comment(self):
        self.assertTrue(TestLexer.test("""
        ## Loreamsdadasfdksfsdksdljfs
        """, "Error Token #", 90))
    def test_comment_2(self):
        self.assertTrue(TestLexer.test("""
        ## adsadaa\\adadff ## saadaa ##
        """, "saadaa,Error Token #", 91))
    def test_random_number_1(self):
        self.assertTrue(TestLexer.test("""
        0001231 0b000000000001 0xAF_01 34_21.000002100000e000008 0.000000000
        """, "00,01231,0b0,00,00,00,00,00,1,0xAF01,3421.000002100000e000008,0.000000000,<EOF>", 92))
    def test_string_20(self):
        self.assertTrue(TestLexer.test("""
        \"Abdskasakla \\' ajwqwla \\y adaff
        """, "Illegal Escape In String: Abdskasakla \\' ajwqwla \\y", 93))
    def test_comment_5(self):
        self.assertTrue(TestLexer.test("""
        ##
        asdajfskdjfwqwqlqdk
        ##
        ffskss
        ##dfkss
        ###sfdjsls
        ##
        """, "ffskss,Error Token #", 94))
    def test_random_number_3(self):
        self.assertTrue(TestLexer.test("""
        1.2344 1_3_452_5.e000006  34_123___X3 345_2331___341_3 23_3_521_52_2 0x1_23A_345___5 0b0100A 002141_2211474 0x_12_2 0_21_4 0b_01 12_0001_111 1_33_351_31.45e19_231 0xAF221.451 098_09 12_311_ 31___211__2
        """, "1.2344,134525.e000006,34123,___X3,3452331,___341_3,233521522,0x123A345,___5,0b0,100,A,00,21412211474,0,x_12_2,0,_21_4,0,b_01,120001111,13335131.45e19,_231,0xAF221,.,451,0,9809,12311,_,31,___211__2,<EOF>", 95))
    def test_float_number(self):
        self.assertTrue(TestLexer.test("""
        1.2344 1_3_452_5.e000006 3e23391_393 5.45e-902_34 _1234.334 22___341___3
        """, "1.2344,134525.e000006,3e23391,_393,5.45e-902,_34,_1234,.,334,22,___341___3,<EOF>", 96))
    def test_compile_error(self):
        self.assertTrue(TestLexer.test("""
        "a\nbcvbddds"
        """, "Unclosed String: a", 97))
    def test_compile_error_2(self):
        self.assertTrue(TestLexer.test("""
        "a
        cdef"
        """, "Unclosed String: a", 98))
    def test111(self):
        self.assertTrue(TestLexer.test("0b0000001 0x00AFF 0004511","0b0,00,00,01,0x0,0,AFF,00,04511,<EOF>",99))
    def test_identifier_1(self):
        self.assertTrue(TestLexer.test("_ _123 __abc__", "_,_123,__abc__,<EOF>", 100))

    def test_identifier_2(self):
        self.assertTrue(TestLexer.test("aCBbdc", "aCBbdc,<EOF>", 101))

    def test_identifier_3(self):
        self.assertTrue(TestLexer.test("$12abc", "$12abc,<EOF>", 102))

    def test_identifier_4(self):
        self.assertTrue(TestLexer.test("123a123", "123,a123,<EOF>", 103))

    def test_identifier_5(self):
        self.assertTrue(TestLexer.test("_av45", "_av45,<EOF>", 104))

    def test_identifier_6(self):
        self.assertTrue(TestLexer.test(""" $_free """, "$_free,<EOF>", 105))

    def test_identifier_7(self):
        self.assertTrue(TestLexer.test("$saf afte", "$saf,afte,<EOF>", 106))

    def test_identifier_8(self):
        self.assertTrue(TestLexer.test(
            "_12343_my const", "_12343_my,const,<EOF>", 107))

    def test_identifier_9(self):
        self.assertTrue(TestLexer.test("1ABC", "1,ABC,<EOF>", 108))

    def test_identifier_10(self):
        self.assertTrue(TestLexer.test("@abcd!ed", "Error Token @", 109))

    def test_identifier_11(self):
        self.assertTrue(TestLexer.test("%eHello", "%,eHello,<EOF>", 110))

    def test_identifier_12(self):
        self.assertTrue(TestLexer.test("*abcd", "*,abcd,<EOF>", 111))

    def test_identifier_13(self):
        self.assertTrue(TestLexer.test("$", "Error Token $", 112))

    def test_identifier_14(self):
        self.assertTrue(TestLexer.test("$abc 1adv _123 df3df",
                        "$abc,1,adv,_123,df3df,<EOF>", 113))

    def test_var_declare(self):
        self.assertTrue(TestLexer.test("Var $dec, num: Int = 0b0101110, 0xAFF",
                        "Var,$dec,,,num,:,Int,=,0b0,101110,,,0xAFF,<EOF>", 114))

    def test_float_number_2(self):
        self.assertTrue(TestLexer.test(
            "12.45e67 12E-9 1E3 12.2 17.3E+9 2. .45 .e3 .4e5 4.e10 45.e1_234 19.4_456e3 1_234.3_456", "12.45e67,12E-9,1E3,12.2,17.3E+9,2.,.,45,.e3,.4e5,4.e10,45.e1,_234,19.4,_456e3,1234.3,_456,<EOF>", 115))

    def test_integer_number(self):
        self.assertTrue(TestLexer.test(
            "1_234 34 12_56_234 0189", "1234,34,1256234,01,89,<EOF>", 116))

    def test_hex_oct_number(self):
        self.assertTrue(TestLexer.test("0x1T 0XA100 0x123 0x0000 00123 0346 0895 0345","0x1,T,0XA100,0x123,0x0,00,0,00,123,0346,0,895,0345,<EOF>", 117))

    def test_string_2(self):
        self.assertTrue(TestLexer.test(
            """ "she \'\" """, "Unclosed String: she \'\" ", 118))
    def test_string_3(self):
        self.assertTrue(TestLexer.test(
            """ "she \'\"""", "Unclosed String: she \'\"", 119))

    def test_string_1(self):
        self.assertTrue(TestLexer.test("\"abc\\nabcde\" \"abc\\'\"",
                        "abc\\nabcde,abc\\',<EOF>", 120))

    def test_string_3(self):
        self.assertTrue(TestLexer.test("""
            "Hello from '"Python'""
        """, """Hello from '"Python'",<EOF>""", 121))

    def test_string_4(self):
        self.assertTrue(TestLexer.test("\"\r\"", """
,<EOF>""", 122))

    def test_expression_1(self):
        self.assertTrue(TestLexer.test("(23 >= 5 && a != 9) || 7 + 9",
                        "(,23,>=,5,&&,a,!=,9,),||,7,+,9,<EOF>", 123))

    def test_expression_2(self):
        self.assertTrue(TestLexer.test("34 < 9 + 12e3 - 1.34",
                        "34,<,9,+,12e3,-,1.34,<EOF>", 124))

    def test_comment_3(self):
        self.assertTrue(TestLexer.test("""
            ## This is comment ##
        """, "<EOF>", 125))

    def test_array(self):
        self.assertTrue(TestLexer.test("Array(1,2,3,4)",
                        "Array,(,1,,,2,,,3,,,4,),<EOF>", 126))

    def test_if_else_stmt(self):
        self.assertTrue(TestLexer.test("""
            If (a > b) {Return a;}
            Elseif (a == b) {a = a + b;}
            Else {Return b;}
            """, "If,(,a,>,b,),{,Return,a,;,},Elseif,(,a,==,b,),{,a,=,a,+,b,;,},Else,{,Return,b,;,},<EOF>", 127))

    def test_for_stmt(self):
        self.assertTrue(TestLexer.test("""
            Foreach ($x In 1 .. 100 By 1) {
                sum = sum + a[$x];
            }
            """, "Foreach,(,$x,In,1,..,100,By,1,),{,sum,=,sum,+,a,[,$x,],;,},<EOF>", 128))

    def test_for_block_stmt(self):
        self.assertTrue(TestLexer.test("""
            {
                Var r, s: Int;
                r = 2.0;
                Var a, b: Array[Int, 5];
                s = r * r * Self.myPI;
                a[0] = s;
            }
            """, "{,Var,r,,,s,:,Int,;,r,=,2.0,;,Var,a,,,b,:,Array,[,Int,,,5,],;,s,=,r,*,r,*,Self,.,myPI,;,a,[,0,],=,s,;,},<EOF>", 129))

    def test_array_2(self):
        self.assertTrue(TestLexer.test("""
            Var $arr : Array[Array[Int, 3], 3] = Array(
                                                        Array(1,2,5),
                                                        Array(2,5,6),
                                                        Array(5,8,7)
                                                        );
            )""", "Var,$arr,:,Array,[,Array,[,Int,,,3,],,,3,],=,Array,(,Array,(,1,,,2,,,5,),,,Array,(,2,,,5,,,6,),,,Array,(,5,,,8,,,7,),),;,),<EOF>", 130))

    def test_string_5(self):
        self.assertTrue(TestLexer.test("""
                Var s : String = \"adsfsdf\\vas\"
                """, "Var,s,:,String,=,Illegal Escape In String: adsfsdf\\v", 131))

    def test_literal(self):
            self.assertTrue(TestLexer.test("""
                    0b12 0b01 12.34 1560 0X1B
                    """, "0b1,2,0b0,1,12.34,1560,0X1B,<EOF>", 132))

    def test_keyword(self):
        self.assertTrue(TestLexer.test("""
                New Return True False Foreach If Elseif Else Float Int String Var Val Constructor Destructor Null Class By In
                """, "New,Return,True,False,Foreach,If,Elseif,Else,Float,Int,String,Var,Val,Constructor,Destructor,Null,Class,By,In,<EOF>", 133))

    def test_operator(self):
        self.assertTrue(TestLexer.test("""
                + - * / % == != ! > < >= <= || && . :: ( ) { } [ ] ==. +.
                """, "+,-,*,/,%,==,!=,!,>,<,>=,<=,||,&&,.,::,(,),{,},[,],==.,+.,<EOF>", 134))

    # "ahi"hi"
    def test_string_6(self):
        self.assertTrue(TestLexer.test("\"ahi\"hi\"",
        "ahi,hi,Unclosed String: ",135))
    # "abc\nabc"
    def test_string_7(self):
        self.assertTrue(TestLexer.test("\"abc\\nabc\"","abc\\nabc,<EOF>",136))

    # "abc\ta\nbc"
    def test_string_8(self):
        self.assertTrue(TestLexer.test("\"abc\\ta\\nbc\"","abc\\ta\\nbc,<EOF>",137))

    def test_string_9(self):
        self.assertTrue(TestLexer.test("\"abc\" 0 \"12ab\\fc0.1\"","abc,0,12ab\\fc0.1,<EOF>",138))

    def test_string_10(self):
        self.assertTrue(TestLexer.test("""
        "0.1anc\'cv" 0.mne "12\\\\3"
        ""","0.1anc'cv,0.,mne,12\\\\3,<EOF>",139))

    def test_string_11(self):
        self.assertTrue(TestLexer.test("abc \"abc1!!@#$$%^i\\n\" 12yz","abc,abc1!!@#$$%^i\\n,12,yz,<EOF>",140))

    def test_string_12(self):
        self.assertTrue(TestLexer.test("\"!h$5FBi6\"_q\"!SZR,H}\"sIfpw","!h$5FBi6,_q,!SZR,H},sIfpw,<EOF>",141))

    def test_string_13(self):
        self.assertTrue(TestLexer.test("""
        4"&J^1a_." QGn"?67Sp"{,}6Asz"Yx]("
        ""","4,&J^1a_.,QGn,?67Sp,{,,,},6,Asz,Yx](,<EOF>",142))

    def test_string_14(self):
        self.assertTrue(TestLexer.test("0f1_\"^VLR@\\\\OusM;\"uGM+jE","0,f1_,^VLR@\\\\OusM;,uGM,+,jE,<EOF>",143))

    def test_string_15(self):
        self.assertTrue(TestLexer.test("\"(IFq+lq(\"IhK6we(*.*)GdvS{(}","(IFq+lq(,IhK6we,(,*,.,*,),GdvS,{,(,},<EOF>",144))

    def test_illegal_escape_1(self):
        self.assertTrue(TestLexer.test("\"bac\\ma\"","Illegal Escape In String: bac\\m",145))

    def test_illegal_escape_2(self):
        self.assertTrue(TestLexer.test("\"baMD\\HLSc\\na\"","Illegal Escape In String: baMD\\H",146))

    def test_illegal_escape_3(self):
        self.assertTrue(TestLexer.test("\",dls\\F12!LS\\kc\\na\"","Illegal Escape In String: ,dls\\F",147))

    def test_illegal_escape_4(self):
        self.assertTrue(TestLexer.test("\"ado\\mado\"","Illegal Escape In String: ado\\m",148))

    def test_illegal_escape_5(self):
        self.assertTrue(TestLexer.test("123abc \"xyz\k 456","123,abc,Illegal Escape In String: xyz\k",149))

    def test_illegal_escape_6(self):
        self.assertTrue(TestLexer.test("\"aa\wb\"","Illegal Escape In String: aa\w",150))

    def test_illegal_escape_7(self):
        self.assertTrue(TestLexer.test("ba+12+\"na\"\"md+1.2-468\lb","ba,+,12,+,na,Illegal Escape In String: md+1.2-468\l",151))

    def test_illegal_escape_8(self):
        self.assertTrue(TestLexer.test("\"1.2+1.3+1.4\\o'\"123","Illegal Escape In String: 1.2+1.3+1.4\\o",152))

    def test_illegal_escape_9(self):
        self.assertTrue(TestLexer.test("(*nac*)+1.1 \"ba\\qm\f\"","(,*,nac,*,),+,1.1,Illegal Escape In String: ba\q",153))

    def test_illegal_escape_10(self):
        self.assertTrue(TestLexer.test("\"concaheo\\uabc","Illegal Escape In String: concaheo\\u",154))

    def test_unclose_String_1(self):
        self.assertTrue(TestLexer.test("\"bacxyc","Unclosed String: bacxyc",155))

    def test_unclose_String_2(self):
        self.assertTrue(TestLexer.test("NmkobYn{!}+I1+\"`YS2h.J(","NmkobYn,{,!,},+,I1,+,Unclosed String: `YS2h.J(",156))

    def test_unclose_String_3(self):
        self.assertTrue(TestLexer.test("\"acnv \" \"abc","acnv ,Unclosed String: abc",157))

    def test_unclose_String_4(self):
        self.assertTrue(TestLexer.test("\"acms!,lds \" {\"abc\"} 123\"abc","acms!,lds ,{,abc,},123,Unclosed String: abc",158))

    def test_unclose_String_5(self):
        self.assertTrue(TestLexer.test("a+11.2+\"mam.123\" 12 \"%^&","a,+,11.2,+,mam.123,12,Unclosed String: %^&",159))

    def test_unclose_String_6(self):
        self.assertTrue(TestLexer.test("38n\"[#Ffs?0ED\"0.\"T`#","38,n,[#Ffs?0ED,0.,Unclosed String: T`#",160))

    def test_string_16(self):
        self.assertTrue(TestLexer.test("\"str1  \\r ahihi \"","str1  \\r ahihi ,<EOF>",161))

    def test_unclose_string_7(self):
        self.assertTrue(TestLexer.test("\"He asked me: '\"Where \\t is John?'\"\"","He asked me: \'\"Where \\t is John?\'\",<EOF>",162))
    def test_unclose_string_8(self):
        self.assertTrue(TestLexer.test("\"  str \\\' \\\" str \"","Illegal Escape In String:   str \\' \\\"",163))
        #   str \' \"
    def test_string_17(self):
        self.assertTrue(TestLexer.test("\" \\\\ \\n \\t \\n fddd \\\\\" "," \\\\ \\n \\t \\n fddd \\\\,<EOF>",164))

    def test_21(self):
        self.assertTrue(TestLexer.test("{ 1,2  ,  32,  2}; {1.2,2., 3e8  , 4.0e-1}","{,1,,,2,,,32,,,2,},;,{,1.2,,,2.,,,3e8,,,4.0e-1,},<EOF>",165))
    def test_22(self):
        self.assertTrue(TestLexer.test("{true,false   ,  true, false}; {\" nam\", \" vat ly \"  ,  \" aaa \" }",
        """{,true,,,false,,,true,,,false,},;,{, nam,,, vat ly ,,, aaa ,},<EOF>""",166))

    def test_stmt_1(self):
        self.assertTrue(TestLexer.test("if(a != b)\nthen continuea=a+1;\nelse b=0;","if,(,a,!=,b,),then,continuea,=,a,+,1,;,else,b,=,0,;,<EOF>",167))
    def test_stmt_2(self):
        self.assertTrue(TestLexer.test("return newn then animal(a,b + c);","return,newn,then,animal,(,a,,,b,+,c,),;,<EOF>",168))
    def test_stmt_3(self):
        self.assertTrue(TestLexer.test("callFn then unction(a + b*c % (d+2));","callFn,then,unction,(,a,+,b,*,c,%,(,d,+,2,),),;,<EOF>",169))
    def test_stmt_4(self):
        self.assertTrue(TestLexer.test("""
        a[7+9] = 12;
        Foreach(i = 1 In 1 .. str.length) {
            b[i] = b[i] + 1;
        }
        """,
        "a,[,7,+,9,],=,12,;,Foreach,(,i,=,1,In,1,..,str,.,length,),{,b,[,i,],=,b,[,i,],+,1,;,},<EOF>", 170))

    def test_stmt_5(self):
        self.assertTrue(TestLexer.test("""
        a = 1;
        b[1+c] = (true && !f || _z) != false;
        """
        ,"a,=,1,;,b,[,1,+,c,],=,(,true,&&,!,f,||,_z,),!=,false,;,<EOF>",171))
    def test_stmt_6(self):
        self.assertTrue(TestLexer.test("""animal.cat.talk(s + "abc");""","""animal,.,cat,.,talk,(,s,+,abc,),;,<EOF>""",172))
    def test_stmt_7(self):
        self.assertTrue(TestLexer.test("return abc.getArea(1 true + 2) - (new obj()).arr[1];","return,abc,.,getArea,(,1,true,+,2,),-,(,new,obj,(,),),.,arr,[,1,],;,<EOF>",173))

    def test_stmt_8(self):
        self.assertTrue(TestLexer.test("""
        function_test(a: Int) {
            ## comment at here ##
            getString("input");
        }
        ""","function_test,(,a,:,Int,),{,getString,(,input,),;,},<EOF>", 174))

    def test_met_de_8(self):
        self.assertTrue(TestLexer.test("""
        String Return(input: String; l: Int) {
            classSTR.getData(input);
            if (l > 0) {
                return getS() + input;
            }
            else {
                return input;
            }
        }
        """
        ,"String,Return,(,input,:,String,;,l,:,Int,),{,classSTR,.,getData,(,input,),;,if,(,l,>,0,),{,return,getS,(,),+,input,;,},else,{,return,input,;,},},<EOF>", 175))
    def test_met_de_9(self):
        self.assertTrue(TestLexer.test("int return(){int data=?getINPUT();return data;}\nint[5] getArray(int l){int[5] arr;\nfor i:=0 to l do arr[i] := getData();\nreturn arr;}","int,return,(,),{,int,data,=,Error Token ?",176))
    def test_met_de_10(self):
        self.assertTrue(TestLexer.test(""" string get_Special_String(){return "abc\\g!!";}""","""string,get_Special_String,(,),{,return,Illegal Escape In String: abc\g""",177))

    def test_integer_real1(self):
        self.assertTrue(TestLexer.test("1.2 1.0 0.1 1e2 1.2E-2 1.2e-2 .1E2 9.0 12e8 0.33E-3 128e-42",
        "1.2,1.0,0.1,1e2,1.2E-2,1.2e-2,.1E2,9.0,12e8,0.33E-3,128e-42,<EOF>",178))
    def test_integer_real2(self):
        self.assertTrue(TestLexer.test("9.0 12e8 0.33E-3 128e-42","9.0,12e8,0.33E-3,128e-42,<EOF>",179))
    def test_integer_real3(self):

        self.assertTrue(TestLexer.test("11.0 12.0e8 0.11+E-3 145e-42","11.0,12.0e8,0.11,+,E,-,3,145e-42,<EOF>",180))
    def test_integer_real4(self):
        self.assertTrue(TestLexer.test("0.11E2 1.11 0.33 1.0e12 1E-15","0.11E2,1.11,0.33,1.0e12,1E-15,<EOF>",181))
    def test_integer_real5(self):
        self.assertTrue(TestLexer.test("e--12 e12 E-15 99e 1 1. 1","e,-,-,12,e12,E,-,15,99,e,1,1.,1,<EOF>",182))

    def test_integer_real7(self):
        self.assertTrue(TestLexer.test("12.2e0 -101 11E-2 11.1e2","12.2e0,-,101,11E-2,11.1e2,<EOF>",183))

    def test_comment_4(self):
        self.assertTrue(TestLexer.test("""
        ## Function(){} abcd
            abcde ##
            abcd_abcde
        ## ##
        ""","abcd_abcde,<EOF>",184))

    def test_random_1(self):
        input ="""
        add(s: Int, t: Int) {
            Var obj = New Bus();
            if (s > 0) {
                obj.insert(s,t);
            }
            else {
                return obj;
            }
        }
    """
        output = "add,(,s,:,Int,,,t,:,Int,),{,Var,obj,=,New,Bus,(,),;,if,(,s,>,0,),{,obj,.,insert,(,s,,,t,),;,},else,{,return,obj,;,},},<EOF>"
        self.assertTrue(TestLexer.test(input,output,185))
    def test_random_2(self):
        input = """
        remove(s: Int, t: Int, obj: Class) {
            obj.removeBus(t);
        }

        minPark() {
            return max;
        }
        """
        output = "remove,(,s,:,Int,,,t,:,Int,,,obj,:,Class,),{,obj,.,removeBus,(,t,),;,},minPark,(,),{,return,max,;,},<EOF>"
        self.assertTrue(TestLexer.test(input, output, 186))

    def test_unclose_string_9(self):
        # "str1 \" \n dd "
        self.assertTrue(TestLexer.test("\"str1 \\\" \n dd \" ","Illegal Escape In String: str1 \\\"",187))
    def test_unclose_string_10(self):
        self.assertTrue(TestLexer.test("\"line 1 df dfff","""Unclosed String: line 1 df dfff""",188))
    def test_illegal_escape_11(self):
        self.assertTrue(TestLexer.test("\"str11\\ \"","Illegal Escape In String: str11\\ ",189))
    def test_unclose_string_11(self):
        self.assertTrue(TestLexer.test("\"str1  Hello World\'\" ahihi ","Unclosed String: str1  Hello World\'\" ahihi ",190))

    def test_illegal_escape_12(self):
            """test identifiers"""
            self.assertTrue(TestLexer.test("\"GameDev\\dlub \\dHCMUT\";",
                            "Illegal Escape In String: GameDev\\d", 191))
    def test_string_18(self):
        """test identifiers"""
        self.assertTrue(TestLexer.test("\"GameDev\\nlub \\nHCMUT\";","""GameDev\\nlub \\nHCMUT,;,<EOF>""",192))
    
    def test_var_declare_2(self):
        """test identifiers"""
        self.assertTrue(TestLexer.test("""Var $arr : Array[Array[Int, 3], 3] = 
                                       Array(
                                           Array(1,2,5),
                                           Array(2,5,6),
                                           Array(5,8,7)
                                           );""","Var,$arr,:,Array,[,Array,[,Int,,,3,],,,3,],=,Array,(,Array,(,1,,,2,,,5,),,,Array,(,2,,,5,,,6,),,,Array,(,5,,,8,,,7,),),;,<EOF>",193))
    
    def test_random_3(self):
        self.assertTrue(TestLexer.test("""
                                       4"&J^1a_." QGn"?67Sp"{,}6Asz"Yx]("
                                       ""","4,&J^1a_.,QGn,?67Sp,{,,,},6,Asz,Yx](,<EOF>", 194)) 

    def test_foreach(self):
        self.assertTrue(TestLexer.test("""
            Foreach ($i In 1 .. 100 By 1) {
                e = e + $i;
                k[$i] = k[$i + 1];
                Foreach ($j In 1 .. 100 By 1) {
                    e = e - $j;
                    l[$i] = l[$j] + e; 
                }
            }
            """, "Foreach,(,$i,In,1,..,100,By,1,),{,e,=,e,+,$i,;,k,[,$i,],=,k,[,$i,+,1,],;,Foreach,(,$j,In,1,..,100,By,1,),{,e,=,e,-,$j,;,l,[,$i,],=,l,[,$j,],+,e,;,},},<EOF>", 195))
    def test_string_19(self):
        self.assertTrue(TestLexer.test("\"##This is a string, not a comment##\"", "##This is a string, not a comment##,<EOF>", 196))
    
    def test_var_declare_3(self):
        """test identifiers"""
        self.assertTrue(TestLexer.test("Var $x, num, $y, 9gh : Int = 5, 6, 7;","Var,$x,,,num,,,$y,,,9,gh,:,Int,=,5,,,6,,,7,;,<EOF>",197))
    def test_var_declare_4(self):
        """test identifiers"""
        self.assertTrue(TestLexer.test("Var $dec, num: Int = 0b0101110, 0xAFF;","Var,$dec,,,num,:,Int,=,0b0,101110,,,0xAFF,;,<EOF>",198))
    def test_if_stmt(self):
        """test identifiers"""
        self.assertTrue(TestLexer.test("""
            If (a >= b) {
                a = a + b;
            }
            Elseif (b >= c) {
                b = a + b || r;
            }
            Else {
                Return result;
            }
        ""","If,(,a,>=,b,),{,a,=,a,+,b,;,},Elseif,(,b,>=,c,),{,b,=,a,+,b,||,r,;,},Else,{,Return,result,;,},<EOF>",199))
    
# import unittest
# from TestUtils import TestLexer

# class LexerSuite(unittest.TestCase):
#     def test1(self):
#         """test identifiers"""
#         self.assertTrue(TestLexer.test("Var $x, num : Int = 5, 6;","Var,$x,,,num,:,Int,=,5,,,6,;,<EOF>",101))
#     def test2(self):
#         """test identifiers"""
#         self.assertTrue(TestLexer.test("Var $x, num, $y, 9gh : Int = 5, 6, 7;","Var,$x,,,num,,,$y,,,9,gh,:,Int,=,5,,,6,,,7,;,<EOF>",102))
#     def test3(self):
#         """test identifiers"""
#         self.assertTrue(TestLexer.test("Var $dec, num: Int = 0b0101110, 0xAFF;","Var,$dec,,,num,:,Int,=,0b0,101110,,,0xAFF,;,<EOF>",103))
#     def test4(self):
#         """test identifiers"""
#         self.assertTrue(TestLexer.test("Var $dec: Int = -58910;","Var,$dec,:,Int,=,-,58910,;,<EOF>",104))
#     def test5(self):
#         """test identifiers"""
#         self.assertTrue(TestLexer.test("Var $dec: Float = -1.562e-90;","Var,$dec,:,Float,=,-,1.562e-90,;,<EOF>",105))
#     def test6(self):
#         """test identifiers"""
#         self.assertTrue(TestLexer.test("\"GameDevClub HCMUT\";","GameDevClub HCMUT,;,<EOF>",106))
#     def test7(self):
#         """test identifiers"""
#         self.assertTrue(TestLexer.test("\"GameDev\\Club HCMUT\";","Illegal Escape In String: GameDev\\C",107))
#     def test8(self):
#         """test identifiers"""
#         self.assertTrue(TestLexer.test("""\"GameDev'"lub '"HCMUT\";""","""GameDev'"lub '"HCMUT,;,<EOF>""",108))
#     def test9(self):
#         """test identifiers"""
#         self.assertTrue(TestLexer.test("\"GameDev\\tlub \\tHCMUT\";","GameDev\\tlub \\tHCMUT,;,<EOF>",109))
#     def test10(self):
#         """test identifiers"""
#         self.assertTrue(TestLexer.test("\"GameDev\\blub \\bHCMUT\";","GameDev\\blub \\bHCMUT,;,<EOF>",110))
#     def test11(self):
#         """test identifiers"""
#         self.assertTrue(TestLexer.test("\"GameDev\\dlub \\dHCMUT\";","Illegal Escape In String: GameDev\\d",111))
#     def test12(self):
#         """test identifiers"""
#         self.assertTrue(TestLexer.test("\"GameDev\\nlub \\nHCMUT\";","""GameDev\\nlub \\nHCMUT,;,<EOF>""",112))
#     def test13(self):
#         """test identifiers"""
#         self.assertTrue(TestLexer.test("\"GameDevClub HCMUT\\t;","Unclosed String: GameDevClub HCMUT\\t;",113))
#     def test14(self):
#         """test identifiers"""
#         self.assertTrue(TestLexer.test("a[6] = 6;","a,[,6,],=,6,;,<EOF>",114))
#     def test15(self):
#         """test identifiers"""
#         self.assertTrue(TestLexer.test("Var $arr : Array[Int, 5] = Array(1, 5, 6);","Var,$arr,:,Array,[,Int,,,5,],=,Array,(,1,,,5,,,6,),;,<EOF>",115))
#     def test16(self):
#         """test identifiers"""
#         self.assertTrue(TestLexer.test("Var $arr : Array[Array[Int, 6], 5];","Var,$arr,:,Array,[,Array,[,Int,,,6,],,,5,],;,<EOF>",116))
#     def test17(self):
#         """test identifiers"""
#         self.assertTrue(TestLexer.test("""Var $arr : Array[Array[Int, 3], 3] = 
#                                        Array(
#                                            Array(1,2,5),
#                                            Array(2,5,6),
#                                            Array(5,8,7)
#                                            );""","Var,$arr,:,Array,[,Array,[,Int,,,3,],,,3,],=,Array,(,Array,(,1,,,2,,,5,),,,Array,(,2,,,5,,,6,),,,Array,(,5,,,8,,,7,),),;,<EOF>",117))
#     def test18(self):
#         self.assertTrue(TestLexer.test("_", "_,<EOF>", 118))
#     def test19(self):
#         self.assertTrue(TestLexer.test("aCBbdc", "aCBbdc,<EOF>", 119))
#     def test20(self):
#         self.assertTrue(TestLexer.test("$12abc", "$12abc,<EOF>", 120))
#     def test21(self):
#         self.assertTrue(TestLexer.test("123a123", "123,a123,<EOF>", 121))
#     def test22(self):
#         self.assertTrue(TestLexer.test("123a##123##", "123,a,<EOF>", 122))
#     def test23(self):
#         self.assertTrue(TestLexer.test("_av45", "_av45,<EOF>", 123))
#     def test24(self):
#         self.assertTrue(TestLexer.test("$_free", "$_free,<EOF>", 124))
#     def test25(self):
#         self.assertTrue(TestLexer.test("$saf afte", "$saf,afte,<EOF>", 125)) 
#     def test26(self):
#         self.assertTrue(TestLexer.test("_12343_my const", "_12343_my,const,<EOF>", 126))
#     def test27(self):
#         self.assertTrue(TestLexer.test("1ABC", "1,ABC,<EOF>", 127))
#     def test28(self):
#         self.assertTrue(TestLexer.test("@abcd!ed", "Error Token @", 128))
#     def test29(self):
#         self.assertTrue(TestLexer.test("%eHello", "%,eHello,<EOF>", 129))
#     def test30(self):
#         self.assertTrue(TestLexer.test("*abcd", "*,abcd,<EOF>", 130))
#     def test31(self):
#         self.assertTrue(TestLexer.test("$", "Error Token $", 131))
#     def test32(self):
#         self.assertTrue(TestLexer.test("Var $dec, num: Int = 0b0101110, 0xAFF", "Var,$dec,,,num,:,Int,=,0b0,101110,,,0xAFF,<EOF>", 132))
#     def test33(self):
#         self.assertTrue(TestLexer.test("12.45e67", "12.45e67,<EOF>", 133))
#     def test34(self):
#         self.assertTrue(TestLexer.test("0x1T", "0x1,T,<EOF>", 134))
#     def test35(self):
#         self.assertTrue(TestLexer.test("\"aj\\elhadef\"", "Illegal Escape In String: aj\\e", 135)) 
#     def test36(self):
#         self.assertTrue(TestLexer.test("\"ab3j\\tlhadef\"", "ab3j\\tlhadef,<EOF>", 136))  
#     def test37(self):
#         self.assertTrue(TestLexer.test("""
#             "Hello from '"Python'""
#         """, """Hello from '"Python'",<EOF>""", 137))  
#     def test38(self):
#         self.assertTrue(TestLexer.test("\"abc \\r babc", """Unclosed String: abc \\r babc""", 138))
#     def test39(self):
#         self.assertTrue(TestLexer.test("(23 >= 5 && a != 9) || 7 + 9", "(,23,>=,5,&&,a,!=,9,),||,7,+,9,<EOF>", 139))
#     def test40(self):
#         self.assertTrue(TestLexer.test("34 < 9 + 12e3 - 1.34", "34,<,9,+,12e3,-,1.34,<EOF>", 140))
#     def test41(self):
#         self.assertTrue(TestLexer.test("""
#             ## This is comment ##
#         """, "<EOF>", 141))
#     def test42(self):
#         self.assertTrue(TestLexer.test("Array(1,2,3,4)", "Array,(,1,,,2,,,3,,,4,),<EOF>", 142))
#     def test43(self):
#         self.assertTrue(TestLexer.test("""
#             If (a > b) {Return a;}
#             Elseif (a == b) {a = a + b;}
#             Else {Return b;}
#             """, "If,(,a,>,b,),{,Return,a,;,},Elseif,(,a,==,b,),{,a,=,a,+,b,;,},Else,{,Return,b,;,},<EOF>", 143))
#     def test44(self):
#         self.assertTrue(TestLexer.test("""
#             Foreach ($x In 1 .. 100 By 1) {
#                 sum = sum + a[$x];
#             }
#             """, "Foreach,(,$x,In,1,..,100,By,1,),{,sum,=,sum,+,a,[,$x,],;,},<EOF>", 144))
#     def test45(self):
#         self.assertTrue(TestLexer.test("""
#             {
#                 Var r, s: Int; 
#                 r = 2.0; 
#                 Var a, b: Array[Int, 5]; 
#                 s = r * r * Self.myPI; 
#                 a[0] = s;
#             }
#             """, "{,Var,r,,,s,:,Int,;,r,=,2.0,;,Var,a,,,b,:,Array,[,Int,,,5,],;,s,=,r,*,r,*,Self,.,myPI,;,a,[,0,],=,s,;,},<EOF>", 145))
#     def test46(self):
#         self.assertTrue(TestLexer.test("\"##This is a string, not a comment##\"", "##This is a string, not a comment##,<EOF>", 146))
#     def test47(self):
#         self.assertTrue(TestLexer.test("\"Son Tung MTP", "Unclosed String: Son Tung MTP", 147))
#     def test48(self):
#         self.assertTrue(TestLexer.test("e12hcbdge", "e12hcbdge,<EOF>", 148))
#     def test49(self):
#         self.assertTrue(TestLexer.test("Val $arrayList : Array[String, 6] = Array(\"ABC\",\"DEF\",\"GHI\",\"JKL\",\"MNO\",\"PQR\");", "Val,$arrayList,:,Array,[,String,,,6,],=,Array,(,ABC,,,DEF,,,GHI,,,JKL,,,MNO,,,PQR,),;,<EOF>", 149))
#     def test50(self):
#         self.assertTrue(TestLexer.test("""
#             Foreach ($i In 1 .. 100 By 1) {
#                 e = e + $i;
#                 k[$i] = k[$i + 1];
#                 Foreach ($j In 1 .. 100 By 1) {
#                     e = e - $j;
#                     l[$i] = l[$j] + e; 
#                 }
#             }
#             """, "Foreach,(,$i,In,1,..,100,By,1,),{,e,=,e,+,$i,;,k,[,$i,],=,k,[,$i,+,1,],;,Foreach,(,$j,In,1,..,100,By,1,),{,e,=,e,-,$j,;,l,[,$i,],=,l,[,$j,],+,e,;,},},<EOF>", 150))
#     def test51(self):
#         self.assertTrue(TestLexer.test("Var $randNum : Int = 1_564_781_1235;", "Var,$randNum,:,Int,=,15647811235,;,<EOF>", 151))
#     def test52(self):
#         self.assertTrue(TestLexer.test("Val myString : String = \"abce\\t456\";", "Val,myString,:,String,=,abce\\t456,;,<EOF>", 152))
#     def test53(self):
#         self.assertTrue(TestLexer.test("Var henry, sofia, lucy, lina : Int = 0b01101, 0XABCD5, 0562, 1254_3;", "Var,henry,,,sofia,,,lucy,,,lina,:,Int,=,0b0,1101,,,0XABCD5,,,0562,,,12543,;,<EOF>", 153))
#     def test54(self):
#         self.assertTrue(TestLexer.test("Var s : String = \"ABC", "Var,s,:,String,=,Unclosed String: ABC", 154))
#     def test55(self):
#         self.assertTrue(TestLexer.test("""Var s : String = \"adsfsdf\\das\"""", "Var,s,:,String,=,Illegal Escape In String: adsfsdf\\d", 155))
#     def test56(self):
#         self.assertTrue(TestLexer.test("\"It\\'s me\"", "It\\'s me,<EOF>", 156))
#     def test57(self):
#         self.assertTrue(TestLexer.test("\"Faker!!! What was that !!!\"", "Faker!!! What was that !!!,<EOF>", 157))
#     def test58(self):
#         self.assertTrue(TestLexer.test("Var s : String = \"adsfsdfas\"", "Var,s,:,String,=,adsfsdfas,<EOF>", 158))
#     def test59(self):
#         self.assertTrue(TestLexer.test("Var a : Int;", "Var,a,:,Int,;,<EOF>", 159))
#     def test60(self):
#         self.assertTrue(TestLexer.test("""
#                                        4"&J^1a_." QGn"?67Sp"{,}6Asz"Yx]("
#                                        ""","4,&J^1a_.,QGn,?67Sp,{,,,},6,Asz,Yx](,<EOF>", 160))
#     def test61(self):
#         self.assertTrue(TestLexer.test("\"xin\\r\\b\\f\\tchao\"","""xin\\r\\b\\f\\tchao,<EOF>""", 161))
#     def test62(self):
#         self.assertTrue(TestLexer.test("""\"0.1anc\\'cv" 0.mne "12\\\\3\"""", """0.1anc\\'cv,0.,mne,12\\\\3,<EOF>""", 162))
#     def test63(self):
#         self.assertTrue(TestLexer.test("Var $a : Float = 1_25_6.5;", "Var,$a,:,Float,=,1256.5,;,<EOF>", 163))
#     def test64(self):
#         self.assertTrue(TestLexer.test("Var $a : Float = 1_25_6.005;", "Var,$a,:,Float,=,1256.005,;,<EOF>", 164))
#     def test65(self):
#         self.assertTrue(TestLexer.test("Var $a : Float = 1_25_6.005e123;", "Var,$a,:,Float,=,1256.005e123,;,<EOF>", 165))
#     def test66(self):
#         self.assertTrue(TestLexer.test("Var $a : Float = 0.2345;", "Var,$a,:,Float,=,0.2345,;,<EOF>", 166))
#     def test67(self):
#         self.assertTrue(TestLexer.test("Var $a : Float = 1e-125;", "Var,$a,:,Float,=,1e-125,;,<EOF>", 167))
#     def test68(self):
#         self.assertTrue(TestLexer.test("Var $a : Float = 1e+125;", "Var,$a,:,Float,=,1e+125,;,<EOF>", 168))
#     def test69(self):
#         self.assertTrue(TestLexer.test("Var $a : Float = 1.560000000000000e-125;", "Var,$a,:,Float,=,1.560000000000000e-125,;,<EOF>", 169))
#     def test70(self):
#         self.assertTrue(TestLexer.test("Var $b : Int = 0b1_0101_110_1_1_0;", "Var,$b,:,Int,=,0b10101110110,;,<EOF>", 170))
#     def test71(self):
#         self.assertTrue(TestLexer.test("Var $a : Int = 0x45_ABC_DF_89_A;", "Var,$a,:,Int,=,0x45ABCDF89A,;,<EOF>", 171))
#     def test72(self):
#         self.assertTrue(TestLexer.test("Var $a : Float = 1.000000;", "Var,$a,:,Float,=,1.000000,;,<EOF>", 172))
#     def test73(self):
#         self.assertTrue(TestLexer.test("Var $a : Float = 1.0000001;", "Var,$a,:,Float,=,1.0000001,;,<EOF>", 173))
#     def test74(self):
#         self.assertTrue(TestLexer.test("(*nac*)+1.1 \"ba\\qm\\f\"", "(,*,nac,*,),+,1.1,Illegal Escape In String: ba\\q", 174))
#     def test75(self):
#         self.assertTrue(TestLexer.test("NmkobYn{!}+I1+\"`YS2h.J(", "NmkobYn,{,!,},+,I1,+,Unclosed String: `YS2h.J(", 175))
#     def test76(self):
#         self.assertTrue(TestLexer.test("\"acms!,lds \" {\"abc\"} 123\"abc", """acms!,lds ,{,abc,},123,Unclosed String: abc""", 176))
#     def test77(self):
#         self.assertTrue(TestLexer.test("""38n"[#Ffs?0ED"0."T`#""", "38,n,[#Ffs?0ED,0.,Unclosed String: T`#", 177))
#     def test78(self):
#         self.assertTrue(TestLexer.test("\"abc\\tabc\"", "abc\\tabc,<EOF>", 178))
#     def test79(self):
#         self.assertTrue(TestLexer.test("""\"ab\\rc\\nd\\be\\fadb\\r\"""","""ab\\rc\\nd\\be\\fadb\\r,<EOF>""", 179))
#     def test80(self):
#         self.assertTrue(TestLexer.test("""\"ahi\"hi\"""", "ahi,hi,Unclosed String: ", 180))
#     def test81(self):
#         self.assertTrue(TestLexer.test("\"Look at the cleanse, look at the moves! Faker! What was that?!!\"", "Look at the cleanse, look at the moves! Faker! What was that?!!,<EOF>", 181))
#     def test82(self):
#         self.assertTrue(TestLexer.test("ab_____ced", "ab_____ced,<EOF>", 182))
#     def test83(self):
#         self.assertTrue(TestLexer.test("1_____345___6", "1,_____345___6,<EOF>", 183))
#     def test84(self):
#         self.assertTrue(TestLexer.test("1_2_3___345___6", "123,___345___6,<EOF>", 184))
#     def test85(self):
#         self.assertTrue(TestLexer.test("\"Thang 4 cua anh\"", "Thang 4 cua anh,<EOF>", 185))
#     def test86(self):
#         self.assertTrue(TestLexer.test("\"Thang 5 cua anh\"", "Thang 5 cua anh,<EOF>", 186))
#     def test87(self):
#         self.assertTrue(TestLexer.test("\"Thang 6 cua anh\"", "Thang 6 cua anh,<EOF>", 187))
#     def test88(self):
#         self.assertTrue(TestLexer.test("\"Thang 7 cua anh, em va co don\"", "Thang 7 cua anh, em va co don,<EOF>", 188))
#     def test89(self):
#         self.assertTrue(TestLexer.test("\"Thang 8 cua anh\"", "Thang 8 cua anh,<EOF>", 189))
#     def test90(self):
#         self.assertTrue(TestLexer.test("\"Thang 9 cua anh\"", "Thang 9 cua anh,<EOF>", 190))
#     def test91(self):
#         self.assertTrue(TestLexer.test(".2",
#                         ".,2,<EOF>", 191))
#     def test92(self):
#         self.assertTrue(TestLexer.test("\"  str \\\' \\\" str \"","Illegal Escape In String:   str \\' \\\"",192))
    
#     def test93(self):
#         self.assertTrue(TestLexer.test(
#             "12.45e67 12E-9 1E3 12.2 17.3E+9 2. .45 .e3 .4e5 4.e10 45.e1_234 19.4_456e3", "12.45e67,12E-9,1E3,12.2,17.3E+9,2.,.,45,.e3,.4e5,4.e10,45.e1,_234,19.4,_456e3,<EOF>", 193))
#     def test94(self):
#         self.assertTrue(TestLexer.test("\"hello\nworld\"","Unclosed String: hello", 194))
#     def test95(self):
#         self.assertTrue(TestLexer.test("""
#                                        "hello
#                                        world"
#                                        ""","Unclosed String: hello", 195))
#     def test96(self):
#         self.assertTrue(TestLexer.test("0b0000001 0x00AFF 0004511","0b0,00,00,01,0x0,0,AFF,00,04511,<EOF>",196))
#     def test97(self):
#         self.assertTrue(TestLexer.test("\"Thang 12 cua anh\"", "Thang 12 cua anh,<EOF>", 197))
#     def test98(self):
#         self.assertTrue(TestLexer.test("\"7 cuoc goi nho\"", "7 cuoc goi nho,<EOF>", 198))
#     def test99(self):
#         self.assertTrue(TestLexer.test("""
#                                        "W-n '"3107'" full album"
#                                        """, "W-n \'\"3107\'\" full album,<EOF>", 199))
#     def test100(self):
#         self.assertTrue(TestLexer.test("\"Khong lam ma doi co an, thi chi co an dau b***, an c** - Huan Rose\"", "Khong lam ma doi co an, thi chi co an dau b***, an c** - Huan Rose,<EOF>", 200))
    
#     def test_comment(self):
#         self.assertTrue(TestLexer.test("""
#         ## Loreamsdadasfdksfsdksdljfs
#         """, "Error Token #", 90))
#     def test_comment_2(self):
#         self.assertTrue(TestLexer.test("""
#         ## adsadaa\\adadff ## saadaa ##
#         """, "saadaa,Error Token #", 91))
#     def test_random_number_1(self):
#         self.assertTrue(TestLexer.test("""
#         0001231 0b000000000001 0xAF_01 34_21.000002100000e000008 0.000000000
#         """, "00,01231,0b0,00,00,00,00,00,1,0xAF01,3421.000002100000e000008,0.000000000,<EOF>", 92))
#     def test_string_20(self):
#         self.assertTrue(TestLexer.test("""
#         \"Abdskasakla \\' ajwqwla \\y adaff
#         """, "Illegal Escape In String: Abdskasakla \\' ajwqwla \\y", 93))
#     def test_comment_5(self):
#         self.assertTrue(TestLexer.test("""
#         ##
#         asdajfskdjfwqwqlqdk
#         ##
#         ffskss
#         ##dfkss
#         ###sfdjsls
#         ##
#         """, "ffskss,Error Token #", 94))
#     def test_random_number_3(self):
#         self.assertTrue(TestLexer.test("""
#         1.2344 1_3_452_5.e000006  34_123___X3 345_2331___341_3 23_3_521_52_2 0x1_23A_345___5 0b0100A 002141_2211474 0x_12_2 0_21_4 0b_01 12_0001_111 1_33_351_31.45e19_231 0xAF221.451 098_09 12_311_ 31___211__2
#         """, "1.2344,134525.e000006,34123,___X3,3452331,___341_3,233521522,0x123A345,___5,0b0,100,A,00,21412211474,0,x_12_2,0,_21_4,0,b_01,120001111,13335131.45e19,_231,0xAF221,.,451,0,9809,12311,_,31,___211__2,<EOF>", 95))
#     def test_float_number(self):
#         self.assertTrue(TestLexer.test("""
#         1.2344 1_3_452_5.e000006 3e23391_393 5.45e-902_34 _1234.334 22___341___3
#         """, "1.2344,134525.e000006,3e23391,_393,5.45e-902,_34,_1234,.,334,22,___341___3,<EOF>", 96))
#     def test_compile_error(self):
#         self.assertTrue(TestLexer.test("""
#         "a\nbcvbddds"
#         """, "Unclosed String: a", 97))
#     def test_compile_error_2(self):
#         self.assertTrue(TestLexer.test("""
#         "a
#         cdef"
#         """, "Unclosed String: a", 98))
#     def test111(self):
#         self.assertTrue(TestLexer.test("0b0000001 0x00AFF 0004511","0b0,00,00,01,0x0,0,AFF,00,04511,<EOF>",99))
#     def test_identifier_1(self):
#         self.assertTrue(TestLexer.test("_ _123 __abc__", "_,_123,__abc__,<EOF>", 100))

#     def test_identifier_2(self):
#         self.assertTrue(TestLexer.test("aCBbdc", "aCBbdc,<EOF>", 101))

#     def test_identifier_3(self):
#         self.assertTrue(TestLexer.test("$12abc", "$12abc,<EOF>", 102))

#     def test_identifier_4(self):
#         self.assertTrue(TestLexer.test("123a123", "123,a123,<EOF>", 103))

#     def test_identifier_5(self):
#         self.assertTrue(TestLexer.test("_av45", "_av45,<EOF>", 104))

#     def test_identifier_6(self):
#         self.assertTrue(TestLexer.test(""" $_free """, "$_free,<EOF>", 105))

#     def test_identifier_7(self):
#         self.assertTrue(TestLexer.test("$saf afte", "$saf,afte,<EOF>", 106))

#     def test_identifier_8(self):
#         self.assertTrue(TestLexer.test(
#             "_12343_my const", "_12343_my,const,<EOF>", 107))

#     def test_identifier_9(self):
#         self.assertTrue(TestLexer.test("1ABC", "1,ABC,<EOF>", 108))

#     def test_identifier_10(self):
#         self.assertTrue(TestLexer.test("@abcd!ed", "Error Token @", 109))

#     def test_identifier_11(self):
#         self.assertTrue(TestLexer.test("%eHello", "%,eHello,<EOF>", 110))

#     def test_identifier_12(self):
#         self.assertTrue(TestLexer.test("*abcd", "*,abcd,<EOF>", 111))

#     def test_identifier_13(self):
#         self.assertTrue(TestLexer.test("$", "Error Token $", 112))

#     def test_identifier_14(self):
#         self.assertTrue(TestLexer.test("$abc 1adv _123 df3df",
#                         "$abc,1,adv,_123,df3df,<EOF>", 113))

#     def test_var_declare(self):
#         self.assertTrue(TestLexer.test("Var $dec, num: Int = 0b0101110, 0xAFF",
#                         "Var,$dec,,,num,:,Int,=,0b0,101110,,,0xAFF,<EOF>", 114))

#     def test_float_number_2(self):
#         self.assertTrue(TestLexer.test(
#             "12.45e67 12E-9 1E3 12.2 17.3E+9 2. .45 .e3 .4e5 4.e10 45.e1_234 19.4_456e3 1_234.3_456", "12.45e67,12E-9,1E3,12.2,17.3E+9,2.,.,45,.e3,.4e5,4.e10,45.e1,_234,19.4,_456e3,1234.3,_456,<EOF>", 115))

#     def test_integer_number(self):
#         self.assertTrue(TestLexer.test(
#             "1_234 34 12_56_234 0189", "1234,34,1256234,01,89,<EOF>", 116))

#     def test_hex_oct_number(self):
#         self.assertTrue(TestLexer.test("0x1T 0XA100 0x123 0x0000 00123 0346 0895 0345","0x1,T,0XA100,0x123,0x0,00,0,00,123,0346,0,895,0345,<EOF>", 117))

#     def test_string_2(self):
#         self.assertTrue(TestLexer.test(
#             """
#             "a\nbc"
#             """, "Unclosed String: a", 118))

#     def test_hex_number_2(self):
#         self.assertTrue(TestLexer.test("0xFG 0FAA X123",
#                         "0xF,G,0,FAA,X123,<EOF>", 119))
#     def test_string_1(self):
#         self.assertTrue(TestLexer.test("\"abc\\nabcde\"",
#                         "abc\\nabcde,<EOF>", 120))

#     def test_string_3(self):
#         self.assertTrue(TestLexer.test("""
#             "Hello from '"Python'""
#         """, """Hello from '"Python'",<EOF>""", 121))

#     def test_string_4(self):
#         self.assertTrue(TestLexer.test("\"\r\"", """
# ,<EOF>""", 122))

#     def test_expression_1(self):
#         self.assertTrue(TestLexer.test("(23 >= 5 && a != 9) || 7 + 9",
#                         "(,23,>=,5,&&,a,!=,9,),||,7,+,9,<EOF>", 123))

#     def test_expression_2(self):
#         self.assertTrue(TestLexer.test("34 < 9 + 12e3 - 1.34",
#                         "34,<,9,+,12e3,-,1.34,<EOF>", 124))

#     def test_comment_3(self):
#         self.assertTrue(TestLexer.test("""
#             ## This is comment ##
#         """, "<EOF>", 125))

#     def test_array(self):
#         self.assertTrue(TestLexer.test("Array(1,2,3,4)",
#                         "Array,(,1,,,2,,,3,,,4,),<EOF>", 126))

#     def test_if_else_stmt(self):
#         self.assertTrue(TestLexer.test("""
#             If (a > b) {Return a;}
#             Elseif (a == b) {a = a + b;}
#             Else {Return b;}
#             """, "If,(,a,>,b,),{,Return,a,;,},Elseif,(,a,==,b,),{,a,=,a,+,b,;,},Else,{,Return,b,;,},<EOF>", 127))

#     def test_for_stmt(self):
#         self.assertTrue(TestLexer.test("""
#             Foreach ($x In 1 .. 100 By 1) {
#                 sum = sum + a[$x];
#             }
#             """, "Foreach,(,$x,In,1,..,100,By,1,),{,sum,=,sum,+,a,[,$x,],;,},<EOF>", 128))

#     def test_for_block_stmt(self):
#         self.assertTrue(TestLexer.test("""
#             {
#                 Var r, s: Int;
#                 r = 2.0;
#                 Var a, b: Array[Int, 5];
#                 s = r * r * Self.myPI;
#                 a[0] = s;
#             }
#             """, "{,Var,r,,,s,:,Int,;,r,=,2.0,;,Var,a,,,b,:,Array,[,Int,,,5,],;,s,=,r,*,r,*,Self,.,myPI,;,a,[,0,],=,s,;,},<EOF>", 129))

#     def test_array_2(self):
#         self.assertTrue(TestLexer.test("""
#             Var $arr : Array[Array[Int, 3], 3] = Array(
#                                                         Array(1,2,5),
#                                                         Array(2,5,6),
#                                                         Array(5,8,7)
#                                                         );
#             )""", "Var,$arr,:,Array,[,Array,[,Int,,,3,],,,3,],=,Array,(,Array,(,1,,,2,,,5,),,,Array,(,2,,,5,,,6,),,,Array,(,5,,,8,,,7,),),;,),<EOF>", 130))

#     def test_string_5(self):
#         self.assertTrue(TestLexer.test("""
#                 Var s : String = \"adsfsdf\\vas\"
#                 """, "Var,s,:,String,=,Illegal Escape In String: adsfsdf\\v", 131))

#     def test_literal(self):
#             self.assertTrue(TestLexer.test("""
#                     0b12 0b01 12.34 1560 0X1B
#                     """, "0b1,2,0b0,1,12.34,1560,0X1B,<EOF>", 132))

#     def test_keyword(self):
#         self.assertTrue(TestLexer.test("""
#                 New Return True False Foreach If Elseif Else Float Int String Var Val Constructor Destructor Null Class By In
#                 """, "New,Return,True,False,Foreach,If,Elseif,Else,Float,Int,String,Var,Val,Constructor,Destructor,Null,Class,By,In,<EOF>", 133))

#     def test_operator(self):
#         self.assertTrue(TestLexer.test("""
#                 + - * / % == != ! > < >= <= || && . :: ( ) { } [ ] ==. +.
#                 """, "+,-,*,/,%,==,!=,!,>,<,>=,<=,||,&&,.,::,(,),{,},[,],==.,+.,<EOF>", 134))

#     # "ahi"hi"
#     def test_string_6(self):
#         self.assertTrue(TestLexer.test("\"ahi\"hi\"",
#         "ahi,hi,Unclosed String: ",135))
#     # "abc\nabc"
#     def test_string_7(self):
#         self.assertTrue(TestLexer.test("\"abc\\nabc\"","abc\\nabc,<EOF>",136))

#     # "abc\ta\nbc"
#     def test_string_8(self):
#         self.assertTrue(TestLexer.test("\"abc\\ta\\nbc\"","abc\\ta\\nbc,<EOF>",137))

#     def test_string_9(self):
#         self.assertTrue(TestLexer.test("\"abc\" 0 \"12ab\\fc0.1\"","abc,0,12ab\\fc0.1,<EOF>",138))

#     def test_string_10(self):
#         self.assertTrue(TestLexer.test("""
#         "0.1anc\'cv" 0.mne "12\\\\3"
#         ""","0.1anc'cv,0.,mne,12\\\\3,<EOF>",139))

#     def test_string_11(self):
#         self.assertTrue(TestLexer.test("abc \"abc1!!@#$$%^i\\n\" 12yz","abc,abc1!!@#$$%^i\\n,12,yz,<EOF>",140))

#     def test_string_12(self):
#         self.assertTrue(TestLexer.test("\"!h$5FBi6\"_q\"!SZR,H}\"sIfpw","!h$5FBi6,_q,!SZR,H},sIfpw,<EOF>",141))

#     def test_string_13(self):
#         self.assertTrue(TestLexer.test("""
#         4"&J^1a_." QGn"?67Sp"{,}6Asz"Yx]("
#         ""","4,&J^1a_.,QGn,?67Sp,{,,,},6,Asz,Yx](,<EOF>",142))

#     def test_string_14(self):
#         self.assertTrue(TestLexer.test("0f1_\"^VLR@\\\\OusM;\"uGM+jE","0,f1_,^VLR@\\\\OusM;,uGM,+,jE,<EOF>",143))

#     def test_string_15(self):
#         self.assertTrue(TestLexer.test("\"(IFq+lq(\"IhK6we(*.*)GdvS{(}","(IFq+lq(,IhK6we,(,*,.,*,),GdvS,{,(,},<EOF>",144))

#     def test_illegal_escape_1(self):
#         self.assertTrue(TestLexer.test("\"bac\\ma\"","Illegal Escape In String: bac\\m",145))

#     def test_illegal_escape_2(self):
#         self.assertTrue(TestLexer.test("\"baMD\\HLSc\\na\"","Illegal Escape In String: baMD\\H",146))

#     def test_illegal_escape_3(self):
#         self.assertTrue(TestLexer.test("\",dls\\F12!LS\\kc\\na\"","Illegal Escape In String: ,dls\\F",147))

#     def test_illegal_escape_4(self):
#         self.assertTrue(TestLexer.test("\"ado\\mado\"","Illegal Escape In String: ado\\m",148))

#     def test_illegal_escape_5(self):
#         self.assertTrue(TestLexer.test("123abc \"xyz\k 456","123,abc,Illegal Escape In String: xyz\k",149))

#     def test_illegal_escape_6(self):
#         self.assertTrue(TestLexer.test("\"aa\wb\"","Illegal Escape In String: aa\w",150))

#     def test_illegal_escape_7(self):
#         self.assertTrue(TestLexer.test("ba+12+\"na\"\"md+1.2-468\lb","ba,+,12,+,na,Illegal Escape In String: md+1.2-468\l",151))

#     def test_illegal_escape_8(self):
#         self.assertTrue(TestLexer.test("\"1.2+1.3+1.4\\o'\"123","Illegal Escape In String: 1.2+1.3+1.4\\o",152))

#     def test_illegal_escape_9(self):
#         self.assertTrue(TestLexer.test("(*nac*)+1.1 \"ba\\qm\f\"","(,*,nac,*,),+,1.1,Illegal Escape In String: ba\q",153))

#     def test_illegal_escape_10(self):
#         self.assertTrue(TestLexer.test("\"concaheo\\uabc","Illegal Escape In String: concaheo\\u",154))

#     def test_unclose_String_1(self):
#         self.assertTrue(TestLexer.test("\"bacxyc","Unclosed String: bacxyc",155))

#     def test_unclose_String_2(self):
#         self.assertTrue(TestLexer.test("NmkobYn{!}+I1+\"`YS2h.J(","NmkobYn,{,!,},+,I1,+,Unclosed String: `YS2h.J(",156))

#     def test_unclose_String_3(self):
#         self.assertTrue(TestLexer.test("\"acnv \" \"abc","acnv ,Unclosed String: abc",157))

#     def test_unclose_String_4(self):
#         self.assertTrue(TestLexer.test("\"acms!,lds \" {\"abc\"} 123\"abc","acms!,lds ,{,abc,},123,Unclosed String: abc",158))

#     def test_unclose_String_5(self):
#         self.assertTrue(TestLexer.test("a+11.2+\"mam.123\" 12 \"%^&","a,+,11.2,+,mam.123,12,Unclosed String: %^&",159))

#     def test_unclose_String_6(self):
#         self.assertTrue(TestLexer.test("38n\"[#Ffs?0ED\"0.\"T`#","38,n,[#Ffs?0ED,0.,Unclosed String: T`#",160))

#     def test_string_16(self):
#         self.assertTrue(TestLexer.test("\"str1  \\r ahihi \"","str1  \\r ahihi ,<EOF>",161))

#     def test_unclose_string_7(self):
#         self.assertTrue(TestLexer.test("\"He asked me: '\"Where \\t is John?'\"\"","He asked me: \'\"Where \\t is John?\'\",<EOF>",162))
#     def test_unclose_string_8(self):
#         self.assertTrue(TestLexer.test("\"  str \\\' \\\" str \"","Illegal Escape In String:   str \\' \\\"",163))
#         #   str \' \"
#     def test_string_17(self):
#         self.assertTrue(TestLexer.test("\" \\\\ \\n \\t \\n fddd \\\\\" "," \\\\ \\n \\t \\n fddd \\\\,<EOF>",164))

#     def test_21(self):
#         self.assertTrue(TestLexer.test("{ 1,2  ,  32,  2}; {1.2,2., 3e8  , 4.0e-1}","{,1,,,2,,,32,,,2,},;,{,1.2,,,2.,,,3e8,,,4.0e-1,},<EOF>",165))
#     def test_22(self):
#         self.assertTrue(TestLexer.test("{true,false   ,  true, false}; {\" nam\", \" vat ly \"  ,  \" aaa \" }",
#         """{,true,,,false,,,true,,,false,},;,{, nam,,, vat ly ,,, aaa ,},<EOF>""",166))

#     def test_stmt_1(self):
#         self.assertTrue(TestLexer.test("if(a != b)\nthen continuea=a+1;\nelse b=0;","if,(,a,!=,b,),then,continuea,=,a,+,1,;,else,b,=,0,;,<EOF>",167))
#     def test_stmt_2(self):
#         self.assertTrue(TestLexer.test("return newn then animal(a,b + c);","return,newn,then,animal,(,a,,,b,+,c,),;,<EOF>",168))
#     def test_stmt_3(self):
#         self.assertTrue(TestLexer.test("callFn then unction(a + b*c % (d+2));","callFn,then,unction,(,a,+,b,*,c,%,(,d,+,2,),),;,<EOF>",169))
#     def test_stmt_4(self):
#         self.assertTrue(TestLexer.test("""
#         a[7+9] = 12;
#         Foreach(i = 1 In 1 .. str.length) {
#             b[i] = b[i] + 1;
#         }
#         """,
#         "a,[,7,+,9,],=,12,;,Foreach,(,i,=,1,In,1,..,str,.,length,),{,b,[,i,],=,b,[,i,],+,1,;,},<EOF>", 170))

#     def test_stmt_5(self):
#         self.assertTrue(TestLexer.test("""
#         a = 1;
#         b[1+c] = (true && !f || _z) != false;
#         """
#         ,"a,=,1,;,b,[,1,+,c,],=,(,true,&&,!,f,||,_z,),!=,false,;,<EOF>",171))
#     def test_stmt_6(self):
#         self.assertTrue(TestLexer.test("""animal.cat.talk(s + "abc");""","""animal,.,cat,.,talk,(,s,+,abc,),;,<EOF>""",172))
#     def test_stmt_7(self):
#         self.assertTrue(TestLexer.test("return abc.getArea(1 true + 2) - (new obj()).arr[1];","return,abc,.,getArea,(,1,true,+,2,),-,(,new,obj,(,),),.,arr,[,1,],;,<EOF>",173))

#     def test_stmt_8(self):
#         self.assertTrue(TestLexer.test("""
#         function_test(a: Int) {
#             ## comment at here ##
#             getString("input");
#         }
#         ""","function_test,(,a,:,Int,),{,getString,(,input,),;,},<EOF>", 174))

#     def test_met_de_8(self):
#         self.assertTrue(TestLexer.test("""
#         String Return(input: String; l: Int) {
#             classSTR.getData(input);
#             if (l > 0) {
#                 return getS() + input;
#             }
#             else {
#                 return input;
#             }
#         }
#         """
#         ,"String,Return,(,input,:,String,;,l,:,Int,),{,classSTR,.,getData,(,input,),;,if,(,l,>,0,),{,return,getS,(,),+,input,;,},else,{,return,input,;,},},<EOF>", 175))
#     def test_met_de_9(self):
#         self.assertTrue(TestLexer.test("int return(){int data=?getINPUT();return data;}\nint[5] getArray(int l){int[5] arr;\nfor i:=0 to l do arr[i] := getData();\nreturn arr;}",
#                                        "int,return,(,),{,int,data,=,Error Token ?",176))
#     def test_met_de_10(self):
#         self.assertTrue(TestLexer.test(""" string get_Special_String(){return "abc\\g!!";}""","""string,get_Special_String,(,),{,return,Illegal Escape In String: abc\g""",177))

#     def test_integer_real1(self):
#         self.assertTrue(TestLexer.test("1.2 1.0 0.1 1e2 1.2E-2 1.2e-2 .1E2 9.0 12e8 0.33E-3 128e-42",
#         "1.2,1.0,0.1,1e2,1.2E-2,1.2e-2,.1E2,9.0,12e8,0.33E-3,128e-42,<EOF>",178))
#     def test_integer_real2(self):
#         self.assertTrue(TestLexer.test("9.0 12e8 0.33E-3 128e-42","9.0,12e8,0.33E-3,128e-42,<EOF>",179))
#     def test_integer_real3(self):

#         self.assertTrue(TestLexer.test("11.0 12.0e8 0.11+E-3 145e-42","11.0,12.0e8,0.11,+,E,-,3,145e-42,<EOF>",180))
#     def test_integer_real4(self):
#         self.assertTrue(TestLexer.test("0.11E2 1.11 0.33 1.0e12 1E-15","0.11E2,1.11,0.33,1.0e12,1E-15,<EOF>",181))
#     def test_integer_real5(self):
#         self.assertTrue(TestLexer.test("e--12 e12 E-15 99e 1 1. 1","e,-,-,12,e12,E,-,15,99,e,1,1.,1,<EOF>",182))

#     def test_integer_real7(self):
#         self.assertTrue(TestLexer.test("12.2e0 -101 11E-2 11.1e2","12.2e0,-,101,11E-2,11.1e2,<EOF>",183))

#     def test_comment_4(self):
#         self.assertTrue(TestLexer.test("""
#         ## Function(){} abcd
#             abcde ##
#             abcd_abcde
#         ## ##
#         ""","abcd_abcde,<EOF>",184))

#     def test_random_1(self):
#         input ="""
#         add(s: Int, t: Int) {
#             Var obj = New Bus();
#             if (s > 0) {
#                 obj.insert(s,t);
#             }
#             else {
#                 return obj;
#             }
#         }
#     """
#         output = "add,(,s,:,Int,,,t,:,Int,),{,Var,obj,=,New,Bus,(,),;,if,(,s,>,0,),{,obj,.,insert,(,s,,,t,),;,},else,{,return,obj,;,},},<EOF>"
#         self.assertTrue(TestLexer.test(input,output,185))
#     def test_random_2(self):
#         input = """
#         remove(s: Int, t: Int, obj: Class) {
#             obj.removeBus(t);
#         }

#         minPark() {
#             return max;
#         }
#         """
#         output = "remove,(,s,:,Int,,,t,:,Int,,,obj,:,Class,),{,obj,.,removeBus,(,t,),;,},minPark,(,),{,return,max,;,},<EOF>"
#         self.assertTrue(TestLexer.test(input, output, 186))

#     def test_unclose_string_9(self):
#         # "str1 \" \n dd "
#         self.assertTrue(TestLexer.test("\"str1 \\\" \n dd \" ","Illegal Escape In String: str1 \\\"",187))
#     def test_unclose_string_10(self):
#         self.assertTrue(TestLexer.test("\"line 1 df dfff","""Unclosed String: line 1 df dfff""",188))
#     def test_illegal_escape_11(self):
#         self.assertTrue(TestLexer.test("\"str11\\ \"","Illegal Escape In String: str11\\ ",189))
#     def test_unclose_string_11(self):
#         self.assertTrue(TestLexer.test("\"str1  Hello World\'\" ahihi ","Unclosed String: str1  Hello World\'\" ahihi ",190))

#     def test_illegal_escape_12(self):
#             """test identifiers"""
#             self.assertTrue(TestLexer.test("\"GameDev\\dlub \\dHCMUT\";",
#                             "Illegal Escape In String: GameDev\\d", 191))
#     def test_string_18(self):
#         """test identifiers"""
#         self.assertTrue(TestLexer.test("\"GameDev\\nlub \\nHCMUT\";","""GameDev\\nlub \\nHCMUT,;,<EOF>""",192))
    
#     def test_var_declare_2(self):
#         """test identifiers"""
#         self.assertTrue(TestLexer.test("""Var $arr : Array[Array[Int, 3], 3] = 
#                                        Array(
#                                            Array(1,2,5),
#                                            Array(2,5,6),
#                                            Array(5,8,7)
#                                            );""","Var,$arr,:,Array,[,Array,[,Int,,,3,],,,3,],=,Array,(,Array,(,1,,,2,,,5,),,,Array,(,2,,,5,,,6,),,,Array,(,5,,,8,,,7,),),;,<EOF>",193))
    
#     def test_random_3(self):
#         self.assertTrue(TestLexer.test("""
#                                        4"&J^1a_." QGn"?67Sp"{,}6Asz"Yx]("
#                                        ""","4,&J^1a_.,QGn,?67Sp,{,,,},6,Asz,Yx](,<EOF>", 194)) 

#     def test_foreach(self):
#         self.assertTrue(TestLexer.test("""
#             Foreach ($i In 1 .. 100 By 1) {
#                 e = e + $i;
#                 k[$i] = k[$i + 1];
#                 Foreach ($j In 1 .. 100 By 1) {
#                     e = e - $j;
#                     l[$i] = l[$j] + e; 
#                 }
#             }
#             """, "Foreach,(,$i,In,1,..,100,By,1,),{,e,=,e,+,$i,;,k,[,$i,],=,k,[,$i,+,1,],;,Foreach,(,$j,In,1,..,100,By,1,),{,e,=,e,-,$j,;,l,[,$i,],=,l,[,$j,],+,e,;,},},<EOF>", 195))
#     def test_string_19(self):
#         self.assertTrue(TestLexer.test("\"##This is a string, not a comment##\"", "##This is a string, not a comment##,<EOF>", 196))
    
#     def test_var_declare_3(self):
#         """test identifiers"""
#         self.assertTrue(TestLexer.test("Var $x, num, $y, 9gh : Int = 5, 6, 7;","Var,$x,,,num,,,$y,,,9,gh,:,Int,=,5,,,6,,,7,;,<EOF>",197))
#     def test_var_declare_4(self):
#         """test identifiers"""
#         self.assertTrue(TestLexer.test("Var $dec, num: Int = 0b0101110, 0xAFF;","Var,$dec,,,num,:,Int,=,0b0,101110,,,0xAFF,;,<EOF>",198))
#     def test_if_stmt(self):
#         """test identifiers"""
#         self.assertTrue(TestLexer.test("""
#             If (a >= b) {
#                 a = a + b;
#             }
#             Elseif (b >= c) {
#                 b = a + b || r;
#             }
#             Else {
#                 Return result;
#             }
#         ""","If,(,a,>=,b,),{,a,=,a,+,b,;,},Elseif,(,b,>=,c,),{,b,=,a,+,b,||,r,;,},Else,{,Return,result,;,},<EOF>",199))
#     def test_string_2(self):
#         self.assertTrue(TestLexer.test(
#             """ "she \'\" """, "Unclosed String: she \'\" ", 118))
#     def test_string_3(self):
#         self.assertTrue(TestLexer.test(
#             """ "she \'\"""", "Unclosed String: she \'\"", 119))
#     def test_float_next(self):
#         self.assertTrue(TestLexer.test(
#             """0.00000""", "0.00000,<EOF>", 119))
