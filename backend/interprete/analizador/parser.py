# ejemplos: https://www.dabeaz.com/ply/ply.html#ply_nn33
from ply.yacc import yacc
from analizador import lexer

tokens = lexer.tokens;

# precedencia de operadores
precedence = (
    ('left', 'RESTA', 'SUMA'),
    ('left', 'MULTIPLICACION', 'DIVISION', 'MODULO'),
    ('right', 'UMENOS'),
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

def declaracion(p):
    """
    declaracion : LET MUT IDENTIFICADOR DOS_PUNTOS type igualacion PUNTO_COMA
        | LET MUT IDENTIFICADOR igualacion PUNTO_COMA
        | LET IDENTIFICADOR DOS_PUNTOS type igualacion PUNTO_COMA
        | LET IDENTIFICADOR igualacion PUNTO_COMA
    """
    if (len(p) == 8):
        p[0] = Declaracion(p[5], p[6], p.lineno(1), p.lexpos(1));
    elif (len(p) == 6):
        p[0] = Declaracion(None, p[4], p.lineno(1), p.lexpos(1));
    elif (len(p) == 7):
        p[0] = Declaracion(p[4], p[5], p.lineno(1), p.lexpos(1));
    elif (len(p) == 4):
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
    if (len(p) == 2):
        p[0] = p[1];
    elif (len(p) == 3):
        p[0] = p[2];

def igualacion(p):
    """
    igualacion : IGUALDAD expresion
    """
    p[0] = p[2];

# unidad aritmética
def expresion(p):
    """
    expresion : RESTA expresion %prec UMENOS
        | I64 DOS_PUNTOS DOS_PUNTOS POTENCIA PARENTESIS_ABRE expresion COMA expresion PARENTESIS_CIERRA
        | expresion SUMA expresion
        | expresion RESTA expresion
        | expresion MULTIPLICACION expresion
        | expresion DIVISION expresion
        | expresion MODULO expresion
    """
    if (len(p) == 3):
        # numero negativo
        p[0] = Aritmetica(p[2], -1, TipoAritmetica.MULTIPLICACION, p.lineno(1), p.lexpos(1));
    elif (len(p) == 10):
        p[0] = Aritmetica(p[6], p[8], TipoAritmetica.POTENCIA, p.lineno(1), p.lexpos(1));
    elif (p[2] == '+'):
        p[0] = Aritmetica(p[1], p[3], TipoAritmetica.SUMA, p.lineno(1), p.lexpos(1));
    elif (p[2] == '-'):
        p[0] = Aritmetica(p[1], p[3], TipoAritmetica.RESTA, p.lineno(1), p.lexpos(1));
    elif (p[2] == '*'):
        p[0] = Aritmetica(p[1], p[3], TipoAritmetica.MULTIPLICACION, p.lineno(1), p.lexpos(1));
    elif (p[2] == '/'):
        p[0] = Aritmetica(p[1], p[3], TipoAritmetica.DIVISION, p.lineno(1), p.lexpos(1));
    elif (p[2] == '%'):
        p[0] = Aritmetica(p[1], p[3], TipoAritmetica.MODULO, p.lineno(1), p.lexpos(1));


# construyendo el parser (analizador sintáctico)
parser = yacc();