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
    #p[0] = Ast(p[1]);

# lista de instrucciones
def instrucciones(p):
    """
    instrucciones : instrucciones instruccion
    """
    p[0] = p[1].append(p[2]);

# la primera instruccion y donde se crea la lista de instrucciones
def instrucciones2(p):
    """
    instrucciones : instruccion
    """
    p[0] = [p[1]];

# declaracion de variables
def instruccion(p):
    """
    instruccion : declaracion PUNTO_COMA
    """
    p[0] = p[1];

def declaracion(p):
    """
    declaracion : LET MUT IDENTIFICADOR DOS_PUNTOS type igualacion PUNTO_COMA
        | LET MUT IDENTIFICADOR igualacion PUNTO_COMA
    """