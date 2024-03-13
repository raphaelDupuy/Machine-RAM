%{

#include "regexp.tab.h"

%}

%%


[A-Z0-9()]*     { return INSTRUCTION; }
\n              { return FDL; }

%%