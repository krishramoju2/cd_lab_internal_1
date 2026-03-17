#include <stdio.h>
#include <string.h>
#include <ctype.h>
#define MAX 10000

char *keywords[] = {
    "int","return","if","else","while","for","float","char","double","void"
};

int isKeyword(char *word){
    int n = sizeof(keywords)/sizeof(keywords[0]);
    for(int i=0;i<n;i++){
        if(strcmp(word,keywords[i])==0)
            return 1;
    }
    return 0;
}

int main(){

    char line[256];
    char code[MAX] = "";

    printf("Enter code (press Enter twice to finish or type 'quit' to exit):\n");

    int empty = 0;

    while(1){
        fgets(line,sizeof(line),stdin);

        if(strncmp(line,"quit",4)==0)
            return 0;

        if(strcmp(line,"\n")==0){
            empty++;
            if(empty==2) break;
        }
        else empty=0;

        strcat(code,line);
    }

    printf("\nInput: %s\n",code);

    int keyword=0, identifier=0, number=0;
    int paren=0, brace=0, semicolon=0, operator=0;
    int total=0;

    printf("\nTokens:\n");

    for(int i=0; code[i] != '\0'; ){

        if(isalpha(code[i]) || code[i]=='_'){
            char word[100];
            int j=0;

            while(isalnum(code[i]) || code[i]=='_'){
                word[j++] = code[i++];
            }
            word[j]='\0';

            if(isKeyword(word)){
                printf("%s (KEYWORD)\n",word);
                keyword++;
            }
            else{
                printf("%s (IDENTIFIER)\n",word);
                identifier++;
            }
            total++;
        }

        else if(isdigit(code[i])){
            char num[100];
            int j=0;

            while(isdigit(code[i])){
                num[j++] = code[i++];
            }
            num[j]='\0';

            printf("%s (NUMBER)\n",num);
            number++;
            total++;
        }

        else if(code[i]=='(' || code[i]==')'){
            printf("%c (PAREN)\n",code[i]);
            paren++; total++; i++;
        }

        else if(code[i]=='{' || code[i]=='}'){
            printf("%c (BRACE)\n",code[i]);
            brace++; total++; i++;
        }

        else if(code[i]==';'){ 
            printf("; (SEMICOLON)\n");
            semicolon++; total++; i++;
        }

        else if(strchr("+-*/=<>&|!",code[i])){
            printf("%c (OPERATOR)\n",code[i]);
            operator++; total++; i++;
        }

        else{
            i++; // ignore spaces/newlines
        }
    }

    printf("\nKEYWORD: %d\n",keyword);
    printf("IDENTIFIER: %d\n",identifier);
    printf("NUMBER: %d\n",number);
    printf("PAREN: %d\n",paren);
    printf("BRACE: %d\n",brace);
    printf("SEMICOLON: %d\n",semicolon);
    printf("OPERATOR: %d\n",operator);

    printf("\nTotal Tokens: %d\n",total);

    return 0;
}
