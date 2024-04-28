%{

#include "regexp.tab.h"

%}

%%

\n                 { return FDL; }
[0-9]+             { yylval.lettre = yytext; return NUMB; }
","                { return VIRG; }
[A-Z0-9(),@-]+     { yylval.lettre = yytext; return INSTRUCTION; }
.        		   { return yytext[0]; }
"<<EOF>>"          { return YYEOF; }

%%