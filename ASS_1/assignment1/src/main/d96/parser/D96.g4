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
    result = super().emit()
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
// official program
// program: class_declares_list class_program class_declares_list EOF;
// test program
program: (instance_attr_call | exp | assign_statement)+ EOF;

// "Program" class is class where program is started
class_program: CLASS PROGRAM class_members;

// members in "Program" class can be only one method named "main" or variety of member of common class. But "main" method always present
// class_program_member: LCB member_list RCB;

// Common class declaration
class_declares_list: class_declares |;
class_declares: class_declare class_declares | class_declare;
class_declare: CLASS NORMAL_ID extend class_members;
extend: COLON NORMAL_ID |;
class_members: LCB member_list RCB;

// extend from super class
// member_list: members | ;
member_list: members |;
members: member members | member;

member: var_declare | constructor_method | destructor_method | main_method | method_declare;
main_method: MAIN LP RP block_statements;

constructor_method: CONSTRUCTOR LP param_list RP block_statements;
destructor_method: DESTRUCTOR LP RP block_des_statements;
block_des_statements: LCB des_statements_list RCB;
des_statements_list: des_statements | ;
des_statements: des_statement | des_statement des_statements;
des_statement: var_declare 
            | assign_statement 
            | break_statement
            | continue_statement
            | instance_method_call SEMI
            | static_method_call SEMI
            | instance_attr_call SEMI
            | instance_method_call SEMI
            | if_else_statement
            | foreach_statement
            ;
method_declare: (NORMAL_ID | DOLLAR_ID) LP param_list RP block_statements;

param_list: parameters |;
parameters: parameter SEMI parameters | parameter;

parameter: id_list COLON (BOOLEAN|INT_TYPE|FLOAT_TYPE|array_type|STRING|NORMAL_ID);

block_statements: LCB statements_list RCB;
statements_list: statements |;
statements: statement statements | statement;
statement 
        : assign_statement 
        | var_declare
        | break_statement
        | continue_statement
        | return_statement
        | instance_method_call SEMI
        | instance_attr_call SEMI
        | static_attr_call SEMI
        | static_method_call SEMI
        | if_else_statement
        | foreach_statement
        ;
break_statement: BREAK SEMI;
continue_statement: CONTINUE SEMI;
return_statement: RETURN exp? SEMI;
assign_statement: lhs ASSIGN exp SEMI;
// IF ELSE STATEMENT---------------------------------
// If (expression) {}
if_else_statement: IF LP exp RP block_statements elseif_stmt_list else_stmt;

// Elseif (expression) {}
elseif_stmt_list: elseif_stmts | ;
elseif_stmts: elseif_stmt | elseif_stmt elseif_stmts;
elseif_stmt: ELSEIF LP exp RP block_statements;

// Else {}
else_stmt: ELSE block_statements | ;

// Foreach statement----------------------------------------
foreach_statement: FOREACH LP (NORMAL_ID | DOLLAR_ID) IN exp DOTDOT exp increment RP block_statements;
increment: BY exp | ;
// lhs stand for "left hand side"
lhs: NORMAL_ID | DOLLAR_ID | index;
index:  (NORMAL_ID | DOLLAR_ID) index_operator;

// function_call: (NORMAL_ID | DOLLAR_ID) LP list_exp RP ;

// Class member access-------------------------------------
static_attr_call: NORMAL_ID SCOPE DOLLAR_ID;
static_method_call: NORMAL_ID SCOPE DOLLAR_ID LP list_exp RP;

instance_attr_call: exp DOT (NORMAL_ID | DOLLAR_ID);
instance_method_call: exp DOT NORMAL_ID LP list_exp RP;

var_declare: (VAR | VAL) dec_and_init_list SEMI;
// {
// # print(self._input.getText(0,2))
// #pass
// #raise Exception("Error from me")
// };
dec_and_init_list: (NORMAL_ID | DOLLAR_ID) pair exp 
                | id_list COLON (BOOLEAN|INT_TYPE|FLOAT_TYPE|array_type|STRING|NORMAL_ID)
                ;  
pair: COMMA (NORMAL_ID | DOLLAR_ID) pair exp COMMA
    | COLON (BOOLEAN|INT_TYPE|FLOAT_TYPE|array_type|STRING|NORMAL_ID) ASSIGN
    ;
// catch[RecognitionException as e] 
// { 
//     localctx.exception = e 
//     self._errHandler.reportError(self, e) 
//     self._errHandler.recover(self, e)
// }
// initial_value: ASSIGN list_exp | ;
VAL: 'Val';
VAR: 'Var';
LP: '('; // Left Parenthesis
RP: ')'; // Right Parenthesis
LCB: '{'; // Left Curly Bracket
RCB: '}'; // Right Curly Bracket
LSB: '['; // Left Square Bracket
RSB: ']'; // Right Square Bracket
SEMI: ';';
COMMA: ',';
COLON: ':';
fragment EXPONENT: [eE] [+-]? DEC_DIGIT;
fragment DEC_DIGIT: [0-9]+;
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

// Operator-----------------------------
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
PROGRAM: 'Program';
MAIN: 'main';
// -----------------------DATA TYPE--------------------------
CLASS: 'Class';
FLOAT_TYPE: 'Float';
STRING: 'String';
INT_TYPE: 'Int';
array_type: ARRAY LSB (BOOLEAN|INT_TYPE|FLOAT_TYPE|array_type|STRING|NORMAL_ID) COMMA INTEGER_LITERAL RSB;
BOOL_LITERAL: TRUE | FALSE;
INTEGER_LITERAL: OCT_TYPE | BIN_TYPE | DEC_TYPE | HEX_TYPE;

fragment HEX_TYPE: ('0x'|'0X') [0-9A-F]
                | ('0x'|'0X') [1-9A-F]('_'? [0-9A-F]+)*;

fragment OCT_TYPE: '0'[0-7]
                | '0'[1-7]('_'? [0-7]+)*;
                

fragment BIN_TYPE: ('0b'|'0B')[01]
                | ('0b'|'0B') [1] ('_'? [01]+)*;

fragment DEC_TYPE: [0-9]                            // Only one digit
                | [1-9] ('_'? [0-9]+)*;

fragment STR: '\'"' | ~[\\"] | ESC_SEQ;

fragment ESC_SEQ: '\\' [btnfr'\\];
fragment ESC_ILLEGAL: '\\' ~[btnfr'\\] | '\\';
STRING_LITERAL: '"' STR* '"'
{ 
    y = str(self.text)
    idx = y.find('\n')
    if idx >= 0:
        raise UncloseString(y[1:idx-1])
    self.text = y[1:-1]
};
ILLEGAL_ESCAPE: '"' STR* ESC_ILLEGAL
{
    raise IllegalEscape(str(self.text)[1:])
};
UNCLOSE_STRING: '"' STR*
{
    raise UncloseString(str(self.text)[1:])
};
 
array_literal: ARRAY LP literal_list RP;
literal_list: literals | ;
literals: exp COMMA literals | exp;
REAL_LITERAL: DEC_TYPE DOT (DEC_DIGIT | EXPONENT)?      // 1. or 1.2 or 1.e2
              | DEC_TYPE EXPONENT                       // 1e4
              | DEC_TYPE? DOT DEC_DIGIT EXPONENT        // 2.4e6 or .5e7
              | DOT EXPONENT;                            // .e56

// EXPRESSION-------------------------------------------------

// string expression
// exp: 'expr';
exp: exp0 EQUAL_STR exp0
    | exp0 ADD_STR exp0
    | exp0
    ; 
// <, <=, >, >=, ==, !=
exp0: exp1 LT exp1 
    | exp1 LTE exp1 
    | exp1 GT exp1 
    | exp1 EQUAL exp1 
    | exp1 NOTEQUAL exp1 
    | exp1 GTE exp1 
    | exp1
    ; 
// &&, ||
exp1: exp1 AND exp2
    | exp1 OR exp2 
    | exp2
    ;
// +, -
exp2: exp2 ADD exp3
    | exp2 SUB exp3
    | exp3
    ;
// *, /, %
exp3: exp3 MUL exp4
    | exp3 DIV exp4
    | exp3 MOD exp4
    | exp4
    ;
// !
exp4: NOT exp4 
    | exp5
    ;
// - (Sign)
exp5: SUB exp5 
    | exp6
    ;
// a[exp]
exp6: exp6 LSB exp RSB
    | exp7
    ;
// a[exp][exp][....
index_operator: LSB exp RSB 
                | LSB exp RSB index_operator
                ;

// 
exp7: exp7 DOT (NORMAL_ID | DOLLAR_ID) LP list_exp RP
    | exp7 DOT (NORMAL_ID | DOLLAR_ID)
    | exp8
    ;
exp8: NORMAL_ID SCOPE DOLLAR_ID LP list_exp RP
    | NORMAL_ID SCOPE DOLLAR_ID
    | exp9
    ;
// New operator
exp9: NEW exp9 LP list_exp RP
     | exp10
     ;
// exp can be number, identifier
exp10
    : INTEGER_LITERAL
    | array_literal
    | BOOL_LITERAL
    | REAL_LITERAL
    | STRING_LITERAL
    | NORMAL_ID
    | DOLLAR_ID
    | SELF 
    | exp11
    ;

// exp inside Parenthesis: Highest precedence
exp11: LP exp RP;

// list of expressions separated by ',' (COMMA)
list_exp: exps |;
exps: exp COMMA exps | exp;

// Identifier-----------------------------------------
NORMAL_ID: [_a-zA-Z][_a-zA-Z0-9]*;
DOLLAR_ID: '$' [_0-9a-zA-Z]+;
id_list: (NORMAL_ID | DOLLAR_ID) COMMA id_list | (NORMAL_ID | DOLLAR_ID);

BLOCK_COMMENT: '##' .*? '##' -> skip;
WS: [ \t\r\n]+ -> skip; // skip spaces, tabs, newlines
ERROR_CHAR:. {raise ErrorToken(self.text)};
