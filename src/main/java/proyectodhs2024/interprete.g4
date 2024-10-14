grammar interprete;

LETRA : [A-Za-z] ;
DIGITO : [0-9] ;

s : DIGITO s
    LETRA s
    EOF
    ;