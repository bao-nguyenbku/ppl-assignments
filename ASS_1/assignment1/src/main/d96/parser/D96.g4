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
    if tk == self.LITERAL:
        # string type
        if (result.text[0] == result.text[-1] and result.text[-1] == '"'):
            if result.text.find('\'"') >= 0:
                result.text = result.text.replace('\'"', '"')
            return result
        result.text = result.text.replace('_', '')
    return result
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

MEMBER: VAR_DECLARE | METHODS;
METHODS: ID LP LIST_PARAM? RP BLOCK_STATEMENT; // function
BLOCK_STATEMENT: LCB VAR_DECLARE RCB;
LIST_PARAM: LIST_METHOD (SEMI LIST_METHOD)*;
LIST_METHOD: ID COLON PRIMITIVE_TYPE | ID COLON PRIMITIVE_TYPE COMMA LIST_METHOD;
VAR_DECLARE: (VAR | VAL) 
             ID_LIST COLON PRIMITIVE_TYPE 
             (
                (ASSIGN LITERAL (COMMA LITERAL)*)
                | (ASSIGN EXP0 (COMMA EXP0)*)
                | (ASSIGN ARRAY_LIST (COMMA ARRAY_LIST)*)
             )?
             SEMI;

// LIST_DATA: ID EXPFULL? | ID EXPFULL? COMMA LIST_DATA;
INT_TYPE: 'Int';
FLOAT_TYPE: 'Float';
STRING: 'string';
BOOL_TYPE: TRUE | FALSE;

// -----------------------DATA TYPE--------------------------
VOID_TYPE: 'Void';
ARRAY_TYPE: ARRAY LSB PRIMITIVE_TYPE COMMA INTEGER_LITERAL RSB;
ARRAY_LIST: ARRAY LP LITERAL (COMMA LITERAL)* RP;
PRIMITIVE_TYPE:
    BOOL_TYPE
    | INT_TYPE
    | FLOAT_TYPE
    | STRING
    | ARRAY_TYPE
    | CLASS;

LITERAL:
    INTEGER_LITERAL
    | BOOL_TYPE
    | REAL_LITERAL
    | STRING_LITERAL;

INTEGER_LITERAL: HEX_TYPE | OCT_TYPE | BIN_TYPE | DEC_TYPE;

STRING_LITERAL: '"' STR1* '"';
// {
//         y = str(self.text)
//         self.text = y[1:-1]
// };

REAL_LITERAL: DEC_TYPE DOT (DEC_TYPE | EXPONENT)*; // 1 | 1.5 | 1.e-4
            //   | DIGIT* DOT DEC_TYPE EXPONENT? // (1).5(e-4)
            //   | DIGIT+ EXPONENT; // 12e-5
HEX_TYPE: ('0x' | '0X') [0-9a-fA-F]+;
OCT_TYPE: '0' [0-9]+;
BIN_TYPE: ('0b' | '0B') [01]+;
DEC_TYPE: [0-9]|[1-9][0-9_]*;
ARRAY: 'Array';
VAL: 'val';
VAR: 'var';
CLASS: 'class';
// EXPRESSION-------------------------------------------------
EXP0:
    EXP1 LT EXP1
    | EXP1 LTE EXP1
    | EXP1 GT EXP1
    | EXP1 GTE EXP1
    | EXP1; //< > <= >= none
EXP1: EQUAL EXP2 | NOTEQUAL EXP2 | EXP2; // == !=  
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
LIST_EXP: EXP0 (COMMA EXP0)*;
// ids_list: ID (COMMA ID)*; ------------------VARIABLES DECLARATION--------------------
// Lexer component

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
fragment EXPONENT: [eE] SIGN? DEC_TYPE;
fragment DIGIT: [0-9];
fragment SIGN: [+-];
BREAK: 'Break';
FOREACH: 'Foreach';
BOOLEAN: 'Boolean';
NULL: 'Null';
CONTINUE: 'Continue';
TRUE: 'True';
FALSE: 'False';
IF: 'if';
ELSEIF: 'elseif';
ARRAYINT: 'Array Int';
ELSE: 'Else';
SELF: 'self';
RETURN: 'return';
NEW: 'new';

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
// Identifier-----------------------------------------
ID_LIST: ID (COMMA ID)*;
ID: [_a-zA-Z][_a-zA-Z0-9]* | DOLLAR ID;
// ----------------------------
fragment STR1: '\\' [bfnrt"\\] | ~[\\"\n\r] | '\'"';
// fragment STR1: '\\' [bfnrt"\\] | ~[\\"\n\r];

WS: [ \t\r\n]+ -> skip; // skip spaces, tabs, newlines
BLOCK_COMMENT: ('##' .*? '##') -> skip;
// ERROR_CHAR: .; UNCLOSE_STRING: .; ILLEGAL_ESCAPE: .;
UNCLOSE_STRING: '"' STR1* EOF
{
    x = str(self.text)
    raise UncloseString(x[1:])
}
;


    // y = str(self.text)
    // possible = ['\b', '\t', '\n', '\f', '\r', '"', "'", '\\']
    // if y[-1] in possible:
    //     raise UncloseString(y[1:-1])
    // else:
    //     raise UncloseString(y[1:])

ILLEGAL_ESCAPE: '"' STR1* '\\' ~[bfnrt"\\] 
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