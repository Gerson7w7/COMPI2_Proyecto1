# ejemplos: https://www.dabeaz.com/ply/ply.html#ply_nn33
from ply.yacc import yacc
from analizador import lexer

tokens = lexer.tokens;

# precedencia de operadores
precedence = (
    ('left', 'RESTA', 'SUMA'),
    ('left', 'MULTIPLICACION', 'DIVISION', 'MODULO'),
    ('right', 'UNARIO'),
)

def inicio(p):
    """
    inicio : instrucciones
    """
    p[0] = Ast(p[1]);

# lista de instrucciones
def instrucciones(p):
    """
    instrucciones : instrucciones instruccion
        | instruccion
    """
    if (len(p) == 3):
        p[0] = p[1].append(p[2]);
    elif (len(p) == 2):
        p[0] = [p[1]];     

# declaracion de variables
def instruccion(p):
    """
    instruccion : declaracion PUNTO_COMA
    """
    p[0] = p[1];

def declaracion1(p):
    """
    declaracion : LET MUT IDENTIFICADOR DOS_PUNTOS type igualacion PUNTO_COMA
    """
    p[0] = Declaracion(p[5], p[6], p.lineno(1), p.lexpos(1));

def declaracion2(p):
    """
    declaracion : LET MUT IDENTIFICADOR igualacion PUNTO_COMA
    """
    p[0] = Declaracion(None, p[4], p.lineno(1), p.lexpos(1));

def declaracion3(p):
    """
    declaracion : LET IDENTIFICADOR DOS_PUNTOS type igualacion PUNTO_COMA
    """
    p[0] = Declaracion(p[4], p[5], p.lineno(1), p.lexpos(1));

def declaracion4(p):
    """
    declaracion : LET IDENTIFICADOR igualacion PUNTO_COMA
    """
    p[0] = Declaracion(None, p[3], p.lineno(1), p.lexpos(1));

def type(p):
    """
    type : I64
        | F64
        | BOOL  
        | CHAR
        | STRING
        | AMPERSON STR
    """