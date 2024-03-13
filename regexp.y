%{

 #include <stdio.h>
 #if YYBISON
 int yylex();
 int yyerror();
 #endif

%}

%union
{
    char *lettre;
};

/* tokens */
%token INSTRUCTION
%token FDL

%type <lettre> INSTRUCTION input ligne

%%
contenu:
       input FDL programme     { printf("{%s}", $1); }
    ;
input:
       INSTRUCTION              { printf("{%s}", $1); }
    ;
programme:
        ligne FDL ligne         { ; }
    |   FDL ligne               { ; }
    ;
ligne:
        INSTRUCTION             { printf("{%s}", yylval.lettre); }

%%

int main() {
    yyparse();
}