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

program: (mptype 'main' LP RP LCB body? RCB) | CLASS_DECLARE+ EOF;

mptype: INT_TYPE | VOID_TYPE;

body: INTEGER_LITERAL;
// body: funcall SEMI;

exp: funcall | INTEGER_LITERAL;

funcall: ID LP exp? RP;
CLASS_DECLARE: CLASS ID (COLON ID)? LCB (MEMBER*) RCB;

MEMBER: METHODS; // Todo:
METHODS: ID LP LIST_PARAM? RP BLOCK_STATEMENT;
BLOCK_STATEMENT: LCB RCB;
LIST_PARAM: LIST_METHOD (SEMI LIST_METHOD)*;
LIST_METHOD: ID COLON PRIMITIVE_TYPE | ID COLON PRIMITIVE_TYPE COMMA LIST_METHOD;
// VAR_DECLARE: (VAR | VAL) 
//              ID_LIST COLON PRIMITIVE_TYPE 
//              (
//                 (ASSIGN LITERAL (COMMA LITERAL)*)
//                 | (ASSIGN EXP0 (COMMA EXP0)*)
//                 | (ASSIGN ARRAY_LIST (COMMA ARRAY_LIST)*)
//              )?
//              SEMI;

// LIST_DATA: ID EXPFULL? | ID EXPFULL? COMMA LIST_DATA;
INT_TYPE: 'Int';
FLOAT_TYPE: 'Float';
STRING: 'String';
BOOL_TYPE: TRUE | FALSE;

// -----------------------DATA TYPE--------------------------
VOID_TYPE: 'Void';
// ARRAY_TYPE: ARRAY LSB PRIMITIVE_TYPE COMMA INTEGER_LITERAL RSB;
// ARRAY_LIST: ARRAY LP LITERAL (COMMA LITERAL)* RP;
CLASS: 'class';
PRIMITIVE_TYPE:
    BOOL_TYPE
    | INT_TYPE
    | FLOAT_TYPE
    | STRING
    // | ARRAY_TYPE
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
REAL_LITERAL: DEC_DIGIT DOT? (DEC_DIGIT | EXPONENT)*;
LITERAL:
    INTEGER_LITERAL
    | BOOL_TYPE
    | REAL_LITERAL
    | STRING_LITERAL;
ARRAY: 'Array';
VAL: 'val';
VAR: 'var';
// EXPRESSION-------------------------------------------------
// EXP0:
//     EXP1 LT EXP1
//     | EXP1 LTE EXP1
//     | EXP1 GT EXP1
//     | EXP1 GTE EXP1
//     | EXP1; 
// EXP1: EQUAL EXP2 | NOTEQUAL EXP2 | EXP2;  
// EXP2: EXP3 | AND EXP3 | OR EXP3;  
// EXP3: ADD EXP4 | SUB EXP4 | EXP4; 
// EXP4: MUL EXP5 | DIV EXP5 | MOD EXP5 | EXP5; 

// EXP5: NOT EXP5 | EXP6; 
// EXP6: ADD EXP6 | SUB EXP6 | EXP7; 
// EXP7: EXP8 LSB EXP0 RSB | EXP8; 
// EXP8: DOT ID (LP LIST_EXP? RP)? | EXP9; 
// EXP9: NEW EXP9 LP LIST_EXP? RP | EXP10; 
// EXP10: LITERAL | ID | SELF | EXP11;
// EXP11: LP EXP0 RP; 
// LIST_EXP: EXP0 (COMMA EXP0)*;

//------------------Lexer component------------------

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
SCOPE: '::';
DOTDOT: '..';
DOT: '.';
fragment EXPONENT: [eE] SIGN? DEC_TYPE;
fragment DIGIT: [0-9];
fragment DEC_DIGIT: [0-9]|[1-9][0-9_]*;
fragment SIGN: [+-];
BREAK: 'Break';
FOREACH: 'Foreach';
BOOLEAN: 'Boolean';
NULL: 'Null';
CONTINUE: 'Continue';
TRUE: 'True';
FALSE: 'False';
IF: 'If';
ELSEIF: 'Elseif';
ELSE: 'Else';
SELF: 'self';
IN: 'In';
BY: 'By';
RETURN: 'return';
NEW: 'new';

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
LTE: '<=';
LT: '<';
EQUAL_STR: '==.';
ADD_STR: '+.';
// Identifier-----------------------------------------
ID: [_a-zA-Z][_a-zA-Z0-9]* | DOLLAR [_a-zA-Z0-9]+;
ID_LIST: ID (COMMA ID)*;

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