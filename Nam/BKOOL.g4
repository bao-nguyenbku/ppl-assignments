grammar BKOOL;

@lexer::header {
from lexererr import *
}

options {
	language = Python3;
}

program: class1+ EOF;
// Class declaration
class1:
	CLS1 ID extend1? LP members* RP; // class a extends? { ....  }
extend1: EXTENDSTA ID;
members: attribute1 | method1 | instance1;
static1: STAT | FINA | STAT FINA | FINA STAT;
instance1: typefunc listins SEMI;
// Attribute declaration
attribute1: static1 typefunc listins SEMI; // static int a, b=2;

// Method declaration
method1: (STAT? typefunc)? ID LB listpara? RB block1; // void func(){...}
listpara: typefunc listmethod (SEMI typefunc listmethod)*;
listmethod: ID | ID COMMA listmethod;

//----------------------- type ------------------------------
typeins1:
	STRINGTYPE
	| FLOATTYPE
	| INTTYPE
	| BOOLEANS
	| ID; // extends cl1
typefunc: typeins1 | arrtype | VOIDTYPE;
arrtype: typeins1 LS exp0 RS; // int[2]
//------------------------ lit ---------------------------
literal1: INTLIT | BOOLLIT | FLOATLIT | STRLIT;
arrlist: LP literal1 (COMMA literal1)* RP;

listins: ID expfull? | ID expfull? COMMA listins;
expfull: ASSG1 (exp0 | arrlist);

//---------------------- block --------------------------
stmt:
	assignsta
	| ifstate
	| forstate
	| method2
	| contista
	| breaksta
	| return1
	| block1;
block1: LP body1 RP;
body1: decl* stmt*;
decl:
	FINA? (arrtype | typeins1) listins SEMI; ///  int a; int[1] b; =
assignsta: lhs ASSG (ID | arrlist | exp0) SEMI; // lhs := 1+ 2;
lhs: ID | exp8 | exp9; // this.a | a | a.b[1]
ifstate: IFSTA exp0 THENSTA stmt (ELSES stmt)?; // if a == b then
forstate:
	FORSTA ID ASSG exp0 (TOS | DOWNTOS) exp0 DOSTA stmt; // for
contista: CONTISTA SEMI;
breaksta: BREAKSTA SEMI;

method2: (ID | exp9) DOT ID LB listexp? RB SEMI;
	//(exp9 | ID) (DOT ID)? LB listexp? RB SEMI;			// a.b(1,2) / a()
return1: RETU exp0 SEMI;

// -----------------------expression------------------------------

exp0:
	exp1 LT exp1
	| exp1 LTE exp1
	| exp1 GT exp1
	| exp1 GTE exp1
	| exp1; //< > <= >= none
exp1: exp2 EQUAL exp2 | exp2 NEQUA exp2 | exp2; // == !=  none
exp2: exp2 AND1 exp3 | exp2 OR1 exp3 | exp3; // && ||  left
exp3: exp3 ADD exp4 | exp3 SUB exp4 | exp4; // + - left
exp4:
	exp4 MUL exp5
	| exp4 DIV exp5
	| exp4 FDIV exp5
	| exp4 MOD exp5
	| exp5; // * / \ % left
exp5: exp5 CONC exp6 | exp6; // ^ left
exp6: NOT1 exp6 | exp7; // ! right
exp7: ADD exp7 | SUB exp7 | exp8; //  + - right
exp8: exp9 LS exp0 RS | exp9; //  [ , ]
exp9:
	exp9 DOT ID (LB listexp? RB)?
	| exp10; // . left   (exp.(id|method))| ID.ID(,)
exp10:
	NEWS exp10 LB listexp? RB
	| exp11; //  new    right       new int
exp11: literal1 | ID | THISS | NILSTA | exp12;
exp12: LB exp0 RB; // (    )
listexp: exp0 | exp0 COMMA listexp;

/*---------------------------LEXER-----------------------------*/
EXTENDSTA: 'extends';
CLS1: 'class';
THENSTA: 'then';
NILSTA: 'nil';
BREAKSTA: 'break';
CONTISTA: 'continue';
FORSTA: 'for';
THISS: 'this';
IFSTA: 'if';
NEWS: 'new';
DOSTA: 'do';
TOS: 'to';
ELSES: 'else';
DOWNTOS: 'downto';
FLOATTYPE: 'float';
STRINGTYPE: 'string';
INTTYPE: 'int';
VOIDTYPE: 'void';
STAT: 'static';
FINA: 'final';
RETU: 'return';
BOOLEANS: 'boolean';
LB: '(';
RB: ')';
LP: '{';
RP: '}';
LS: '[';
RS: ']';
COLO: ':';
SEMI: ';';
COMMA: ',';
ADD: '+';
SUB: '-';
MUL: '*';
DIV: '\\';
FDIV: '/';
MOD: '%';
EQUAL: '==';
NEQUA: '!=';
GT: '>';
GTE: '>=';
LT: '<';
LTE: '<=';
OR1: '||';
AND1: '&&';
CONC: '^';
NOT1: '!';
DOT: '.';
ASSG: ':=';
ASSG1: '=';

BOOLLIT: 'true' | 'false';
fragment STR1: '\\' [bfnrt"\\] | ~[\\"\n\r];
STRLIT: '"' STR1* '"';
ID: [a-zA-Z_][0-9a-zA-Z_]*;
fragment INT: [0-9]+;
fragment PART1: '.' INT;
fragment PART2: ('e' | 'E') (SUB | ADD |) INT;
FLOATLIT:
	INT ('.' | ('.' PART2) | (PART1 | PART2) | (PART1 PART2));
INTLIT: INT;

CMTS: '/*' .*? '*/' -> skip;
CMT: '#' ~[\r\n]* -> skip;
WS: [ \t\r\f\n]+ -> skip; // skip spaces, tabs, newlines

ERROR_CHAR: .{raise ErrorToken(self.text)};
UNCLOSE_STRING1: '"' STR1* EOF {raise UncloseString(self.text)};
UNCLOSE_STRING:
	'"' STR1* [\n\r]{self.text=self.text[0:-1]} {raise UncloseString(self.text)};
ILLEGAL_ESCAPE:
	'"' STR1* '\\' ~[bfnrt"\\] {raise IllegalEscape(self.text)};