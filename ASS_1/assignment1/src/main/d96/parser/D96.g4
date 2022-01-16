grammar D96;

// @lexer::header {
// from lexererr import *
// }
// @lexer::members {
// def emit(self):
//     tk = self.type
//     # result mean for input
//     result = super().emit() 
    
//     if tk == self.INTEGER_LITERAL or tk == self.REAL_LITERAL:
//         result.text = result.text.replace('_', '')
//     return result
// }
@lexer::header {
from lexererr import *
import inspect
}
@lexer::members {
def emit(self):
    tk = self.type
    result = super().emit() # result mean for input
    # delete later
    print('--------------------------------------------------------------------------------')
    attributes = inspect.getmembers(D96Lexer, lambda a:not(inspect.isroutine(a)))
    user_defined_attr = [a for a in attributes if not(a[0].startswith('__') and a[0].endswith('__'))]
    for i in user_defined_attr:
        if tk == i[1]:
            print ("{:<30} {:<30} {:<50}".format(result.text, '|', i[0]))
    print('--------------------------------------------------------------------------------')

    if tk == self.INTEGER_LITERAL or tk == self.REAL_LITERAL:
        result.text = result.text.replace('_', '')

    return result
}
options {
	language = Python3;
}
// program: class_declare* class_program class_declare* EOF;
program: var_declare EOF;
// "Program" class is class where program is started
class_program: CLASS 'Program' LCB 'main' LP RP LCB body_main RCB RCB;
body_main: var_declare | function_call | ;
// Common class declaration
class_declare: CLASS NORMAL_ID extend LCB member RCB;
extend: COLON NORMAL_ID | ;
member: var_declare | method ;

constructor_method: CONSTRUCTOR LP param_list? RP block_statement;
destructor_method: DESTRUCTOR LP RP block_statement;
method: (NORMAL_ID | DOLLAR_ID) LP RP block_statement;

param_list: parameter
            | parameter SEMI param_list
            ;

parameter: id_list COLON primitive_type;

block_statement: LCB statement RCB;

statement: var_declare | assign_statement | function_call | ;

assign_statement: 'assign_statement';
function_call: ID LP exp? RP;
var_declare: (VAR | VAL) id_list COLON primitive_type (init_value)? SEMI;
init_value: ASSIGN list_exp;

// -----------------------DATA TYPE--------------------------
BOOL_TYPE: TRUE | FALSE;
FLOAT_TYPE: 'Float';
STRING: 'String';
INT_TYPE: 'Int';
VOID_TYPE: 'Void';
array_list: ARRAY LP literal_list RP;
literal_list: literal COMMA literal_list | literal | ;


array_type: ARRAY LSB primitive_type COMMA INTEGER_LITERAL RSB;
primitive_type:
    BOOL_TYPE
    | INT_TYPE
    | FLOAT_TYPE
    | array_type
    | STRING
    | CLASS;

INTEGER_LITERAL: HEX_TYPE | OCT_TYPE | BIN_TYPE | DEC_TYPE
{
    self.text = self.text.replace('_', '')
}
;

HEX_TYPE: ('0x' | '0X') [0-9a-fA-F][0-9a-fA-F_]*[0-9a-fA-F_]
          | ('0x' | '0X') [0-9a-fA-F]
{
    self.text = self.text.replace('_', '')
};
OCT_TYPE: '0'[0-9][0-9_]*[0-9]
           | '0'[0-9]
{
    self.text = self.text.replace('_', '')
};
BIN_TYPE: ('0b' | '0B')[01][01_]*[01]
          | ('0b' | '0B')[01]
{
    self.text = self.text.replace('_', '')
};
DEC_TYPE: [0-9]
          | [1-9][0-9_]*[0-9]
{
    self.text = self.text.replace('_', '')
};

fragment STR: '\'"' | ~[\\"] | ESC_SEQ;

fragment ESC_SEQ: '\\' [btnfr'\\];
fragment ESC_ILLEGAL: '\\' ~[btnfr'\\] | '\'' ~'"' | '\\';
STRING_LITERAL: '"' STR* '"'
{
    illegal_escape = ['\v']
    for i in self.text:
        if i in illegal_escape:
            y = str(self.text)
            ill_idx = y.index(i)
            raise IllegalEscape(y[1:ill_idx+1])
    
    y = str(self.text)
    if y.find('\'"') >= 0:
        y = y.replace('\'"', '"')
    self.text = y[1:-1]
};
ILLEGAL_ESCAPE: '"' STR* ESC_ILLEGAL
{
    y = str(self.text)
    raise IllegalEscape(y[1:])
};
UNCLOSE_STRING: '"' STR*
{
    x = str(self.text)
    raise UncloseString(x[1:])
};
 
literal:
    INTEGER_LITERAL
    | BOOL_TYPE
    | REAL_LITERAL
    | STRING_LITERAL
    | array_list
    ;
REAL_LITERAL: DEC_TYPE DOT DEC_TYPE
              | DEC_TYPE EXPONENT
              | DEC_TYPE DOT DEC_TYPE EXPONENT
{
    self.text = self.text.replace('_', '')
};
VAL: 'Val';
VAR: 'Var';
// EXPRESSION-------------------------------------------------
exp: STRING_LITERAL EQUAL_STR STRING_LITERAL
     | STRING_LITERAL ADD_STR STRING_LITERAL
     | exp0
     ; 
exp0: exp1 LT exp1 
     | exp1 LTE exp1 
     | exp1 GT exp1 
     | exp1 GTE exp1 
     | exp1 EQUAL exp1 
     | exp1 NOTEQUAL exp1 
     | exp1; 
exp1: exp1 AND exp2
     |exp1 OR exp2 
     | exp2
     ;
exp2: exp2 ADD exp3
     | exp2 SUB exp3
     | exp3
     ;
exp3: exp3 MUL exp4
     | exp3 DIV exp4
     | exp3 MOD exp4
     | exp4
     ;
exp4: NOT exp4 
     | exp5
     ;
exp5: SUB exp5 
     | exp6
     ;

exp6: exp7 LSB exp RSB
     | exp7
     ;
exp7: exp7 DOT NORMAL_ID (LP list_exp? RP)?
     | exp7 SCOPE NORMAL_ID (LP list_exp? RP)?
     | exp8
     ;
exp8: NEW NORMAL_ID LP list_exp? RP
     | exp9
     ;
exp9: LP exp RP
     | exp10
     ;
exp10: literal | NORMAL_ID | SELF;

list_exp: exp | exp COMMA list_exp;
//------------------Lexer component------------------

fragment DOLLAR: '$';
LP: '('; // Left Parenthesis
RP: ')'; // Right Parenthesis
LCB: '{'; // Left Curly Bracket
RCB: '}'; // Right Curly Bracket
LSB: '['; // Left Square Bracket
RSB: ']'; // Right Square Bracket

SEMI: ';';
COMMA: ',';
COLON: ':';
fragment EXPONENT: [eE] SIGN? DEC_TYPE;
fragment DIGIT: [0-9];
fragment DEC_DIGIT: [0-9]|[1-9][0-9_]*[0-9];
fragment SIGN: [+-];
CLASS: 'Class';
BREAK: 'Break';
CONTINUE: 'Continue';
IF: 'If';
ELSEIF: 'Elseif';
ELSE: 'Else';
FOREACH: 'Foreach';
TRUE: 'True';
FALSE: 'False';
ARRAY: 'Array';
IN: 'In';
BOOLEAN: 'Boolean';
RETURN: 'Return';
NULL: 'Null';
CONSTRUCTOR: 'Constructor';
DESTRUCTOR: 'Destructor';
NEW: 'New';
BY: 'By';
SELF: 'Self';

// Operator
ADD: '+';
SUB: '-';
MUL: '*';
DIV: '/';
MOD: '%';
NOT: '!';
AND: '&&';
OR: '||';
EQUAL: '==';
ASSIGN: '=';
NOTEQUAL: '!=';
GT: '>';
GTE: '>=';
LT: '<';
LTE: '<=';
EQUAL_STR: '==.';
ADD_STR: '+.';
DOT: '.';
DOTDOT:'..';
SCOPE: '::';
// Identifier-----------------------------------------
normal_id_list: NORMAL_ID
		 | NORMAL_ID COMMA normal_id_list
		 ;
dollar_id_list: DOLLAR_ID
				| DOLLAR_ID COMMA dollar_id_list
                ;
id_list: normal_id_list | dollar_id_list;
NORMAL_ID: [_a-zA-Z][_a-zA-Z0-9]*;
DOLLAR_ID: DOLLAR [_0-9a-zA-Z]+;
ID: NORMAL_ID | DOLLAR_ID;
WS: [ \t\r\n\f]+ -> skip; // skip spaces, tabs, newlines
BLOCK_COMMENT: ('##' .*? '##') -> skip;

ERROR_CHAR:. {raise ErrorToken(self.text)};