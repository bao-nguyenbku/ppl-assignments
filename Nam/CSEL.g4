grammar CSEL;

@lexer::header {
from lexererr import *
}

@lexer::members {
def emit(self):
    tk = self.type
    result = super().emit()
    if tk == self.UNCLOSE_STRING:       
        raise UncloseString(result.text)
    elif tk == self.ILLEGAL_ESCAPE:
        raise IllegalEscape(result.text)
    elif tk == self.ERROR_CHAR:
        raise ErrorToken(result.text)
    elif tk == self.UNTERMINATED_COMMENT:
        raise UnterminatedComment()
    else:
        return result;
}

options {
	language = Python3;
}

/////////////////              Parser

program: (const_declare SEMI | var_declare SEMI | func_declare)* EOF;

//////// statements
list_stmt: stmt | stmt list_stmt;
stmt:
	var_declare SEMI
	| const_declare SEMI
	| assign_stmt SEMI
	| if_stmt
	| for_in_stmt
	| for_of_stmt
	| break_stmt SEMI
	| while_stmt
	| continue_stmt SEMI
	| return_stmt SEMI
	| call SEMI;

// expression
expr: expr1 (EQ | NE | B | BB | L | LB) expr1 | expr1;

expr1: expr1 (AND | OR) expr2 | expr2;

expr2: expr2 (ADD | SUB) expr3 | expr3;

expr3: expr3 (MUL | DIV | MODUL) expr4 | expr4;

expr4: NOT expr4 | expr5;

expr5: SUB expr5 | expr6;

expr6: expr6 index_expr | expr6 key_operator | expr7;


// key_expr:
// 	expr6 key_operator
// 	| expr7 key_operator; //b["acd"][b] {x:a}["x"]

key_operator: LSB expr RSB | LSB expr RSB key_operator;

index_expr: LSB id_operator RSB; // a[1,3+4] "abcd"[1,2,3]

id_operator: expr | expr COMMA id_operator;

expr7: call | expr8;

expr8:
	STRING_LITERAL
	| BOOL_LITERAL
	| NUM_LITERAL
	| array_literal
	| json_literal
	| ID_CONST
	| ID
	| expr9;
expr9: LP expr RP;

condition: LP expr RP;
//If statement
if_stmt: IF condition LCB list_stmt? RCB list_elif? else_stmt?;

list_elif: elif_stmt | elif_stmt list_elif;

elif_stmt: ELIF condition LCB list_stmt? RCB;

else_stmt: ELSE LCB list_stmt? RCB;

//For In/Of
for_in_stmt:
	FOR (ID | ID_CONST) IN (literal | expr) LCB list_stmt? RCB;

for_of_stmt:
	FOR (ID | ID_CONST) OF (literal | expr) LCB list_stmt? RCB;
//While
while_stmt: WHILE condition LCB list_stmt? RCB;

//Break
break_stmt: BREAK;

//Continue
continue_stmt: CONTINUE;

//Call: Call(foo,[1,2,3])
call: CALL LP ID COMMA LSB call_parameters? RSB RP;

call_parameters:
	call_parameter
	| call_parameter COMMA call_parameters;
call_parameter: expr;
// Return
return_stmt: RETURN expr | RETURN;
//Declare
func_declare:
	FUNCT ID LP (list_parameters)? RP LCB (list_stmt)? RCB;

list_parameters: parameter | parameter COMMA list_parameters;
parameter: ID | id_var_array | ID_CONST | id_const_array;

var_declare: LET list_declare_var;

const_declare: CONST list_declare_const;

list_declare_var:
	declare_var
	| declare_var COMMA list_declare_var;

list_declare_const:
	declare_const
	| declare_const COMMA list_declare_const;

id_var_array: ID LSB id_operator? RSB;
id_const_array: ID_CONST LSB id_operator? RSB;

declare_var: (ID | id_var_array) declare_type? declare_assign?;
declare_const: (ID_CONST | id_const_array) declare_type? declare_assign?;

declare_type: COLON KEYWORDS;
declare_assign: EQUAL expr;

assign_stmt: lhs EQUAL (expr | str_expr);
lhs: ID | ID_CONST | index | key;

index:(ID | ID_CONST) id_operator;
key: (ID | ID_CONST) key_operator;

//String operators
str_expr: str_operand | str_operand str_op str_expr;
str_op: MS | CS;
str_operand: expr;
//////////////// Lexer Key words
KEYWORDS: 'Number' | 'Boolean' | 'String' | 'JSON' | 'Array';
BREAK: 'Break';
CONTINUE: 'Continue';
IF: 'If';
ELIF: 'Elif';
ELSE: 'Else';
WHILE: 'While';
FOR: 'For';
OF: 'Of';
IN: 'In';
FUNCT: 'Function';
LET: 'Let';
CALL: 'Call';
RETURN: 'Return';
CONST: 'Constant';

ID: [a-z][a-zA-Z0-9_]*;
ID_CONST: '$' [a-zA-Z0-9_]+;

EQUAL: '=';
SEMI: ';';
LP: '(';
RP: ')';
LCB: '{';
RCB: '}';
LSB: '[';
RSB: ']';
COLON: ':';
PERIOD: '.';
COMMA: ',';

COMMMENT: '##' .*? '##' -> skip;

UNTERMINATED_COMMENT:
	'##' .*? {
                raise UnterminatedComment()
            };
//Literals

NUM_LITERAL:
	DIGIT PERIOD?
	| DIGIT PERIOD DIGIT
	| DIGIT (PERIOD DIGIT)? [eE] [+-]? DIGIT
	| DIGIT PERIOD [eE] [+-]? DIGIT;

BOOL_LITERAL: 'True' | 'False';

STRING_LITERAL:
	'"' STR_CHAR* '"' {
    self.text = self.text[1:-1]
};

UNCLOSE_STRING:
	'"' STR_CHAR* {
                raise UncloseString(self.text[1:])
            };
ILLEGAL_ESCAPE:
	'"' STR_CHAR* ESC_ILLEGAL {
                raise IllegalEscape(self.text[1:])
            };

// [ 1 , 2 , 3 ] , [ [ 2, 3 ] , [ ] ]
array_literal: LSB array_list? RSB;
literal:
	array_literal
	| NUM_LITERAL
	| BOOL_LITERAL
	| STRING_LITERAL
	| json_literal;
array_list: expr | expr COMMA array_list;

num_list: NUM_LITERAL | NUM_LITERAL COMMA num_list;
bool_list: BOOL_LITERAL | BOOL_LITERAL COMMA bool_list;
str_list: STRING_LITERAL | STRING_LITERAL COMMA str_list;
json_list: json_literal | json_literal COMMA json_literal;

json_literal: LCB json_decls? RCB;
json_decls: json_declare COMMA json_decls | json_declare;
json_declare:
	(ID | ID_CONST | id_var_array | id_const_array) COLON expr;

ADD: '+';
SUB: '-';
MODUL: '%';
MUL: '*';
DIV: '/';
NOT: '!';
NE: '!=';
AND: '&&';
OR: '||';
EQ: '==';
L: '>';
LB: '>=';
B: '<';
BB: '<=';
CS: '==.';
MS: '+.';

// Fragments :
fragment STR_CHAR: '\'"' | ~[\b\t\n\f\r'"\\] | ESC_SEQ;
fragment DIGIT: [0-9]+;
fragment ESC_SEQ: '\\' [btnfr'\\];
fragment ESC_ILLEGAL: '\\' ~[btnfr'\\] | '\'' ~'"' | '\\';

WS: [ \t\r\f]+ -> skip; // skip spaces, tabs, form feed, newline
NEWLINE: '\n'+ -> skip;

ERROR_CHAR:
	. {
		raise ErrorToken(self.text)
	};
