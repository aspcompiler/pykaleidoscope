// ANTLR4 Grammar for the LLVM Tutorial Sample Kaleidoscope language
// To support a progression through the chapters the language features are
// selectable and dynamically adjust the parsing accordingly. This allows a
// single parser implementation for all chapters, which allows the tutorial
// to focus on the actual use of Llvm.NET itself rather than on parsing.
//
grammar Kaleidoscope;

// Lexer Rules -------
fragment NonZeroDecimalDigit_: [1-9];
fragment DecimalDigit_: [0-9];
fragment Digits_: '0' | [1-9][0-9]*;
fragment EndOfFile_: '\u0000' | '\u001A';
fragment EndOfLine_
    : ('\r' '\n')
    | ('\r' |'\n' | '\u2028' | '\u2029')
    | EndOfFile_
    ;

LPAREN: '(';
RPAREN: ')';
COMMA: ',';
SEMICOLON: ';';
DEF: 'def';
EXTERN: 'extern';

ASSIGN:'=';
ASTERISK: '*';
PLUS: '+';
MINUS:'-';
LEFTANGLE: '<';

IF: 'if';
THEN: 'then';
ELSE: 'else';

LineComment: '#' ~[\r\n]* EndOfLine_ -> skip;
WhiteSpace: [ \t\r\n\f]+ -> skip;

Identifier: [a-zA-Z][a-zA-Z0-9]*;
Number: Digits_ ('.' DecimalDigit_+)?;

// Parser rules ------

// Non Left recursive expressions (a.k.a. atoms)
primaryExpression
    : Number                                                                # NumberExpression
    | LPAREN expression RPAREN                                              # ParenExpression
    | Identifier                                                            # IdentifierExpression
    | Identifier (LPAREN (expression (COMMA expression)*)? RPAREN)          # CallExpression
    ;

// We use antlr4 adaptive parsing to resolve precedence and recurcion.
// See https://www.antlr.org/papers/allstar-techreport.pdf
expression
    : lhs=expression bop=ASTERISK rhs=expression                                    
    | lhs=expression bop=( PLUS | MINUS ) rhs=expression                           
    | lhs=expression bop=LEFTANGLE rhs=expression                                       
    | primaryExpression                                                     
    ;

prototype
    : Identifier LPAREN (Identifier)* RPAREN                                # FunctionPrototype
    ;

topLevel
    : DEF prototype expression                                              # FunctionDefinition
    | EXTERN prototype                                                      # ExternalDeclaration
    | expression                                                            # TopLevelExpression
    ;
