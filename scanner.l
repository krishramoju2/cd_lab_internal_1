%{
#include <stdio.h>
int sno = 1;
%}
%%
"int"|"float"|"char"|"double"
{
    printf("%-5d %-15s %-15s\n", sno++, yytext, "Keyword");
}
[a-zA-Z_][a-zA-Z0-9_]*
{
    printf("%-5d %-15s %-15s\n", sno++, yytext, "Identifier");
}
[0-9]+
{
    printf("%-5d %-15s %-15s\n", sno++, yytext, "Number");
}
"+"|"-"|"*"|"/"|"="
{
    printf("%-5d %-15s %-15s\n", sno++, yytext, "Operator");
}
"("|")"|"{"|"}"|";"|","|"<"|">"
{
    printf("%-5d %-15s %-15s\n", sno++, yytext, "Special Symbol");
}
[ \t\n]+    ;   /* Ignore whitespace */
{
    printf("%-5d %-15s %-15s\n", sno++, yytext, "Unknown");
}
%%
int yywrap()
{
    return 1;
}
int main()
{
    printf("\nS.No  Lexeme          Token\n");
    printf("-----------------------------------\n");
    yylex();
    return 0;
}


# nano scanner.l
#flex scanner.l
# gcc lex.yy.c -o scanner -lfl
# ./scanner
