%{

#include "regexp.tab.h"

%}

%%

"ADD"       { return ADD }
"JUMP"      { return JUMP }
"JE"        { return JE }
\n          { return FDL }