%{


%}

/* tokens */
%token ADD
%token JUMP
%token JE
%token FDL

%%
contenu:
        input FDL programme     { ; }
    ;
input:

    ;
programme:
        