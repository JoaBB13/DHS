grammar compiladores;

fragment LETRA : [A-Za-z] ;
fragment DIGITO : [0-9] ;

//INST: (LETRA | DIGITO | [- ,;{}{}+=>] )+ '\n' ;

PA: '(' ;
PC: ')' ;
PYC: ';' ;
LLA: '{' ;
LLC: '}' ;
SUMA: '+' ;
RESTA: '-' ;
MULT: '*' ;
DIV: '/' ;
MOD: '%';
MAYOR: '>' ;
MENOR: '<' ;
MAYORIG: '>=' ;
MENORIG: '<=' ;
DIF: '=!' ;

ASIG: '=' ;
IGUAL: '==' ;
PUNTO: '.' ;
GUION_BAJO: '_' ;
ARROBA: '@' ;
NUMERAL: '#' ;
COMA: ',';

logicos: AND | OR ;
comparadores: MAYOR | MENOR | MAYORIG | MENORIG | IGUAL | DIF ;
NUMERO : DIGITO+ | DIGITO+ '.' DIGITO+ ;

AND : '&&' ;
OR : '||' ;

INT: 'int' ;
WHILE : 'while' ;
FOR : 'for' ;
IF: 'if' ;
DO: 'do' ;
ELSE: 'else' ;
RETURN: 'return' ;
ID : (LETRA | '_')(LETRA | DIGITO | '_')* ;

WS : [ \n\t\r] -> skip;
OTRO : . ;

//s : ID     {print("ID ->" + $ID.text + "<--") }            s
//  | NUMERO {print("NUMERO ->" + $NUMERO.text + "<--") }    s
//  | WHILE {print("WHILE ->" + $WHILE.text + "<--") }       s
//  | IF {print("IF ->" + $IF.text + "<--") }                s
//  | DO {print("DO ->" + $DO.text + "<--") }                s
//  | FOR {print("FOR ->" + $FOR.text + "<--") }             s
//  | OTRO   {print("Otro ->" + $OTRO.text + "<--") }        s
 // | EOF
//  ;

//Analizador sintactico
//si : s EOF ;

//s : PA s PC s
//  |
//  ;

programa : instrucciones EOF; //desde aca arranca el parser(se puede cambiar )

instrucciones : instruccion instrucciones
              |
              ;

//instruccion : INST {print($INST.text{:-1})};
instruccion : declaracion 
            | iwhile
            | ifor
            | iif
            | bloque
            | asignacion PYC
            ;
            
declaracion: INT ID PYC ;

asignacion : ID ASIG opal;

opal : log ; //completar

//trabajo en proceso
log : comp lor;

lor : land lorp ;

lorp : OR land lor
  | land
  |
  ;

land: comp landp;

landp : AND comp land
    | 
    ;


comp : exp comparadores exp 
    | exp;

exp : term e ;

e : SUMA term e
  | RESTA term e
  | 
  ;

term : factor t;

t : MULT factor t
  | DIV factor t
  | MOD factor t
  |
  ;

factor : NUMERO
       | ID
       | PA exp PC
       ;

iwhile : WHILE PA ID PC instruccion ;

bloque : LLA instrucciones LLC ;

ifor : FOR PA init PYC cond PYC iter PC instruccion ;
init : ID ASIG opal;
cond : ID comparadores (NUMERO | ID);
iter : opal | ID SUMA SUMA | ID RESTA RESTA | SUMA SUMA ID | RESTA RESTA ID;

iif : IF PA ID comparadores (ID | NUMERO) PC  LLA instruccion LLC ielse?;

ielse: ELSE bloque | ELSE iif ;
