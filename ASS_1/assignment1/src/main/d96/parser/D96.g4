
grammar D96;

@lexer::header {
from lexererr import *
}

options {
	language = Python3;
}

program: mptype 'main' LP RP LCB body? RCB EOF;

mptype: INT_TYPE | VOID_TYPE;

body: funcall SEMI;

exp: funcall | INTLIT;

funcall: ID LP exp? RP;
CLASS_DECLARE: CLASS ID (COLON ID)? LCB (MEMBER*) RCB;
VAR_DECLARE: (VAR|VAL) ID_LIST COLON PRIMITIVE_TYPE ()? SEMI;
MEMBER: METHODS;


LIST_DATA: ID EXPFULL? | ID EXPFULL? COMMA LIST_DATA;
EXPFULL: ASSIGN (exp0 | arrlist);
ID_LIST: ID (COMMA ID)*;
METHODS: ID LP () RP; // function
// -----------------------DATA TYPE--------------------------
INT_TYPE: 'Int';
BOOL_TYPE: TRUE | FALSE;
VOID_TYPE: 'Void';
ARRAY_TYPE: 'Array' LSB PRIMITIVE_TYPE COMMA INTLIT RSB;
FLOAT_TYPE: 'Float';
PRIMITIVE_TYPE:
	BOOL_TYPE
	| INT_TYPE
	| FLOAT_TYPE
	| STRING
	| ARRAY_TYPE
	| CLASS;
// ID: [a-zA-Z]+;

// EXPRESSION-------------------------------------------------
exp0:
	exp1 LT exp1
	| exp1 LTE exp1
	| exp1 GT exp1
	| exp1 GTE exp1
	| exp1; //< > <= >= none
exp1: exp2 EQUAL exp2 | exp2 NOTEQUAL exp2 | exp2; // == !=  
exp2: exp2 AND exp3 | exp2 OR exp3 | exp3; // && ||  
exp3: exp3 ADD exp4 | exp3 SUB exp4 | exp4; // + - 
exp4: exp4 MUL exp5 | exp4 DIV exp5 | exp4 MOD exp5 | exp5;  // * / %
exp5: exp5 | exp6;
exp6: NOT exp6 | exp7; // !
exp7: ADD exp7 | SUB exp7 | exp8; //  + - 
exp8: exp9 LSB exp0 RSB | exp9; //  [ , ]
exp9:
	exp9 DOT ID (LP listexp? RP)?
	| exp10; // . left   (exp.(id|method))| ID.ID(,)
exp10:
	NEW exp10 LP listexp? RP
	| exp11; //  new    right       new int
exp11: literal1 | ID | THISS | NILSTA | exp12;
exp12: LB exp0 RB; // (    )
listexp: exp0 | exp0 COMMA listexp;
// ids_list: ID (COMMA ID)*; 
// ------------------VARIABLES DECLARATION--------------------

// Lexer component
INTLIT: [0-9]+;
ID: [_a-zA-Z][_a-zA-Z0-9]*;
VAL: 'val';
VAR: 'var';
CLASS: 'class';
DOLLAR: '$';
LP: '('; // Left Parenthesis
RP: ')'; // Right Parenthesis
LCB: '{'; // Left Curly Bracket
RCB: '}'; // Right Curly Bracket
LSB: '['; // Left Square Bracket
RSB: ']'; // Right Square Bracket

SEMI: ';'; // Semicolon
COMMA: ','; // Comma
COLON: ':'; // Colon
DOTDOT: '..'; // Dot Dot should be before Dot
fragment DOT: '.';
BREAK: 'Break';
FOREACH: 'Foreach';
BOOLEAN: 'Boolean';
NULL: 'Null';
CONTINUE: 'Continue';
TRUE: 'True';
FALSE: 'False';
STRING: 'string';
IF: 'if';
ELSEIF: 'elseif';
ARRAYINT: 'Array Int';
ELSE: 'Else';
FLOAT: 'Float';
RETURN: 'return';
NEW: 'new';
fragment EXPONENT: [eE] SUB? DIGIT+;
fragment DIGIT: [0-9];
fragment SIGN: [+-];

INTEGER_LITERAL: DIGIT+;
STRING_LITERAL:
	'"' STR_CHAR* '"' {
		y = str(self.text)
		self.text = y[1:-1]
	};

REAL_LITERAL:
	DIGIT+ DOT (DIGIT | EXPONENT)* // 1 | 1.5 | 1.e-4
	| DIGIT* DOT DIGIT+ EXPONENT? // (1).5(e-4)
	| DIGIT+ EXPONENT ; // 12e-5
// Operator
ADD: '+';
ADD_STR: '+.';
SUB: '-';
MUL: '*';
DIV: '/';
MOD: '%';
NOT: '!';
NOTEQUAL: '!=';
EQUAL: '==';
EQUAL_STR: '==.';
AND: '&&';
OR: '||';
GT: '>';
LTE: '<=';
LT: '<';
GTE: '>=';
ASSIGN: '=';
// ----------------------------
WS: [ \t\r\n]+ -> skip; // skip spaces, tabs, newlines
BLOCK_COMMENT: ('##' .*? '##') -> skip;
fragment STR_CHAR: ~[\b\t\n\f\r"'\\] | ESC_SEQ;

fragment ESC_SEQ: '\\' [btnfr"'\\];

fragment ESC_ILLEGAL: '\\' ~[btnfr"'\\] | ~'\\';
// ERROR_CHAR: .; UNCLOSE_STRING: .; ILLEGAL_ESCAPE: .;
UNCLOSE_STRING:
	'"' STR_CHAR* ([\b\t\n\f\r"'\\] | EOF) {
		y = str(self.text)
		possible = ['\b', '\t', '\n', '\f', '\r', '"', "'", '\\']
		if y[-1] in possible:
			raise UncloseString(y[1:-1])
		else:
			raise UncloseString(y[1:])
	};

ILLEGAL_ESCAPE:
	'"' STR_CHAR* ESC_ILLEGAL {
		y = str(self.text)
		raise IllegalEscape(y[1:])
	};

ERROR_CHAR:
	. {
		raise ErrorToken(self.text)
	};
UNTERMINATED_COMMENT:
	'##' .*? {
	raise ErrorToken('UNTERMINATED_COMMENT');
};