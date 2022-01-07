grammar D96;

@lexer::header {
from lexererr import *
}

options {
	language = Python3;
}

program: (mptype 'main' LP RP LCB body? RCB) | CLASS_DECLARE+ EOF;

mptype: INT_TYPE | VOID_TYPE;

body: funcall SEMI;

exp: funcall | INTEGER_LITERAL;

funcall: ID LP exp? RP;
CLASS_DECLARE: CLASS ID (COLON ID)? LCB (MEMBER*) RCB;
VAR_DECLARE: (VAR | VAL) ID_LIST COLON PRIMITIVE_TYPE ()? SEMI;

MEMBER: VAR_DECLARE | METHODS;

LIST_DATA: ID EXPFULL? | ID EXPFULL? COMMA LIST_DATA;
EXPFULL: ASSIGN EXP0 | ARRAY_LIST;
ID_LIST: ID (COMMA ID)*;
METHODS: ID LP () RP; // function
// -----------------------DATA TYPE--------------------------
INT_TYPE: 'Int';
BOOL_TYPE: TRUE | FALSE;
VOID_TYPE: 'Void';
ARRAY_TYPE: 'Array' LSB PRIMITIVE_TYPE COMMA INTEGER_LITERAL RSB;
ARRAY_LIST: 'Array' LP ( LITERAL (COMMA LITERAL)?) RP;
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
EXP0:
    EXP1 LT EXP1
    | EXP1 LTE EXP1
    | EXP1 GT EXP1
    | EXP1 GTE EXP1
    | EXP1; //< > <= >= none
EXP1: EXP2 EQUAL EXP2 | EXP2 NOTEQUAL EXP2 | EXP2; // == !=  
EXP2: EXP3 | AND EXP3 | OR EXP3; // && ||  
EXP3: ADD EXP4 | SUB EXP4 | EXP4; // + - 
EXP4: MUL EXP5 | DIV EXP5 | MOD EXP5 | EXP5; // * / %
// EXP5: EXP5 | EXP6;
EXP5: NOT EXP5 | EXP6; // !
EXP6: ADD EXP6 | SUB EXP6 | EXP7; //  + - 
EXP7: EXP8 LSB EXP0 RSB | EXP8; //  [ , ]
EXP8: DOT ID (LP LIST_EXP? RP)? | EXP9; // . left   (exp.(id|method))| ID.ID(,)
EXP9: NEW EXP9 LP LIST_EXP? RP | EXP10; //  new    right       new int
EXP10: LITERAL | ID | SELF | EXP11;
EXP11: LP EXP0 RP; // (    )
LIST_EXP: EXP0 | EXP0 COMMA LIST_EXP;
// ids_list: ID (COMMA ID)*; ------------------VARIABLES DECLARATION--------------------

// Lexer component INTLIT: [0-9]+;
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
SELF: 'self';
RETURN: 'return';
NEW: 'new';
fragment EXPONENT: [eE] SUB? DIGIT+;
fragment DIGIT: [0-9];
fragment SIGN: [+-];
LITERAL:
    INTEGER_LITERAL
    | BOOL_TYPE
    | REAL_LITERAL
    | STRING_LITERAL;
HEX_TYPE: ('0x' | '0X') [0-9a-fA-F]+;
OCT_TYPE: '0' [1-9]+;
BIN_TYPE: ('0b' | '0B') [01]+;
DEC_TYPE: [0-9]|[1-9][0-9_]*;


INTEGER_LITERAL: HEX_TYPE | OCT_TYPE | BIN_TYPE | DEC_TYPE;

STRING_LITERAL: '"' STR_CHAR* '"' {
        y = str(self.text)
        self.text = y[1:-1]
	};

REAL_LITERAL: DIGIT+ DOT (DIGIT | EXPONENT)* // 1 | 1.5 | 1.e-4
| DIGIT* DOT DIGIT+ EXPONENT? // (1).5(e-4)
| DIGIT+ EXPONENT; // 12e-5
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
UNCLOSE_STRING: '"' STR_CHAR* ([\b\t\n\f\r"'\\] | EOF) 
{
    y = str(self.text)
    possible = ['\b', '\t', '\n', '\f', '\r', '"', "'", '\\']
    if y[-1] in possible:
        raise UncloseString(y[1:-1])
    else:
        raise UncloseString(y[1:])
};

ILLEGAL_ESCAPE: '"' STR_CHAR* ESC_ILLEGAL 
{
    y = str(self.text)
    raise IllegalEscape(y[1:])
};

ERROR_CHAR:. 
{
    raise ErrorToken(self.text)
};
UNTERMINATED_COMMENT: '##' .*? 
{
    raise ErrorToken('UNTERMINATED_COMMENT')
};