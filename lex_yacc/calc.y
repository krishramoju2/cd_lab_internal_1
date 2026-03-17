%{
#include <stdio.h>
#include <stdlib.h>

int yylex();
void yyerror(const char *s);
%}

%token NUMBER

%%

input:
      input line
    |
    ;

line:
      '\n'
    | expr '\n' { printf("Result = %d\n", $1); }
    ;

expr:
      expr '+' expr { $$ = $1 + $3; }
    | expr '-' expr { $$ = $1 - $3; }
    | expr '*' expr { $$ = $1 * $3; }
    | expr '/' expr { $$ = $1 / $3; }
    | '(' expr ')'  { $$ = $2; }
    | NUMBER        { $$ = $1; }
    ;

%%

void yyerror(const char *s) {
    printf("Error: %s\n", s);
}

int main() {
    printf("Simple Calculator\n");
    yyparse();
    return 0;
}


# sudo apt install flex bison gcc 
# nano calc.l
# nano calc.y
# bison -d calc.y
# flex calc.l
# gcc calc.tab.c lex.yy.c -o calculator 
# ./calculator
