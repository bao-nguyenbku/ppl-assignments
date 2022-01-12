grammar D96;

@lexer::header {
from lexererr import *
}
@lexer::members {
def emit(self):
    tk = self.type
    result = super().emit() # result mean for input
    # delete later
    print('--------------------------------------------------------------------------------')
    
    print ("{:<30} {:<30} {:<50}".format(result.text, '|', self.symbolicNames[tk-1]))
    print('--------------------------------------------------------------------------------')
    if tk == self.STRING_LITERAL:
        if result.text.find('\'"') >= 0:
            result.text = result.text.replace('\'"', '"')
            return result
    if tk == self.INTEGER_LITERAL or tk == self.REAL_LITERAL:
        result.text = result.text.replace('_', '')
        return result
    return result
}
options {
	language = Python3;
}

program: (mptype 'main' LP RP LCB body? RCB | class_declare)+ EOF;

mptype: INT_TYPE | VOID_TYPE;

body: funcall SEMI;

exp: funcall | literal;

funcall: ID LP exp? RP;
class_declare: CLASS ID LCB member* RCB;

member: var_declare | METHOD;
METHOD: ID LP RP BLOCK_STATEMENT;
BLOCK_STATEMENT: LCB RCB;
// LIST_METHOD: ID COLON primitive_type | ID COLON primitive_type COMMA LIST_METHOD;
var_declare: (VAR | VAL) id_list COLON primitive_type SEMI;

INT_TYPE: 'Int';
FLOAT_TYPE: 'Float';
STRING: 'String';
BOOL_TYPE: TRUE | FALSE;

// -----------------------DATA TYPE--------------------------
VOID_TYPE: 'Void';
array_list: ARRAY LP literal (COMMA literal)* RP;
array_type: ARRAY LSB primitive_type COMMA INTEGER_LITERAL RSB;
primitive_type:
    BOOL_TYPE
    | INT_TYPE
    | FLOAT_TYPE
    | array_type
    | STRING
    | CLASS;


INTEGER_LITERAL: HEX_TYPE | OCT_TYPE | BIN_TYPE | DEC_TYPE;

HEX_TYPE: ('0x' | '0X') [0-9a-fA-F]+;
OCT_TYPE: '0' [0-9]+;
BIN_TYPE: ('0b' | '0B') [01]+;
DEC_TYPE: [0-9]|[1-9][0-9_]*;
// '\\' ~[bfnrt"\\]
STRING_LITERAL: '"' STR* '"'
{
    y = str(self.text)
    self.text = y[1:-1]
};
ILLEGAL_ESCAPE: '"' STR* ESC_ILLEGAL
{
    y = str(self.text)
    raise IllegalEscape(y[1:])
};
UNCLOSE_STRING: '"' STR* EOF
{
    x = str(self.text)
    raise UncloseString(x[1:])
};
fragment STR: '\\' [bfnrt"\\] | ~[\\"] | '\'"';

fragment ESC_SEQ: '\\' [btnfr"'\\] ;

fragment ESC_ILLEGAL: '\\' ~[bfnrt"\\] ;
literal:
    INTEGER_LITERAL
    | BOOL_TYPE
    | REAL_LITERAL
    | STRING_LITERAL;
REAL_LITERAL: DEC_DIGIT DOT? (DEC_DIGIT | EXPONENT)*;
VAL: 'Val';
VAR: 'Var';
// EXPRESSION-------------------------------------------------
exp0: exp1 (LT | LTE | GT | GTE | EQUAL | NOTEQUAL) exp1 | exp1; 
exp1: exp4 (AND | OR) exp1 | exp4;  
// EXP2: EXP2 (ADD | SUB) EXP3 | EXP3; 
// EXP3: EXP3 (MUL | DIV | MOD) EXP4 | EXP4; 
exp4: (NOT | SUB) exp4 | literal; 
// OPERAND: OPERAND LSB EXP RSB | LITERAL | LP EXP RP | ID ;
list_exp: exp0 (COMMA exp0)*;
//------------------Lexer component------------------

fragment DOLLAR: '$';
LP: '('; // Left Parenthesis
RP: ')'; // Right Parenthesis
LCB: '{'; // Left Curly Bracket
RCB: '}'; // Right Curly Bracket
LSB: '['; // Left Square Bracket
RSB: ']'; // Right Square Bracket

SEMI: ';'; // Semicolon
COMMA: ','; // Comma
COLON: ':'; // Colon
DOTDOT: '..';
fragment EXPONENT: [eE] SIGN? DEC_TYPE;
fragment DIGIT: [0-9];
fragment DEC_DIGIT: [0-9]|[1-9][0-9_]*;
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
SCOPE: '::';
// Identifier-----------------------------------------
ID: [_a-zA-Z][_a-zA-Z0-9]* | DOLLAR [_a-zA-Z0-9]+;
id_list: ID (COMMA ID)*;

// ----------------------------

WS: [ \t\r\n]+ -> skip; // skip spaces, tabs, newlines

BLOCK_COMMENT: ('##' .*? '##') -> skip;
// ERROR_CHAR: .; UNCLOSE_STRING: .; ILLEGAL_ESCAPE: .;

UNTERMINATED_COMMENT: '##' .*? 
{
    raise ErrorToken('UNTERMINATED_COMMENT')
};
ERROR_CHAR:. 
{
    raise ErrorToken(self.text)
};