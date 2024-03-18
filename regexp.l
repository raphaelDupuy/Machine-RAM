%{

#include "regexp.tab.h"

%}

%%

\n                 { return FDL; }
[A-Z0-9(),@-]+     { yylval.lettre = yytext; return INSTRUCTION; }
.        		   { return yytext[0]; }

%%