# ejemplos: https://www.dabeaz.com/ply/ply.html#ply_nn33
from interprete.ply.yacc import yacc
from interprete.analizador import lexer

import re
from ..expresiones.Aritmetica import Aritmetica
from ..extra.Tipos import TipoAritmetica, TipoDato
from ..extra.Ast import Ast
from ..instrucciones.Declaracion import Declaracion
from ..expresiones.Literal import Literal

tokens = lexer.tokens;

# precedencia de operadores
precedence = (
    ('left', 'RESTA', 'SUMA'),
    ('left', 'MULTIPLICACION', 'DIVISION', 'MODULO'),
    ('right', 'UMENOS'),
)

def p_inicio(p):
    """
    inicio : instrucciones
    """
    p[0] = Ast(p[1])

# lista de instrucciones
def p_instrucciones(p):
    """
    instrucciones : instrucciones instruccion
        | instruccion
    """
    if (len(p) == 3):
        p[0] = p[1].append(p[2]);
    elif (len(p) == 2):
        p[0] = [p[1]];     

# declaracion de variables
def p_instruccion(p):
    """
    instruccion : declaracion PUNTO_COMA
    """
    p[0] = p[1];

def p_declaracion(p):
    """
    declaracion : LET MUT IDENTIFICADOR DOS_PUNTOS type igualacion
        | LET MUT IDENTIFICADOR igualacion
        | LET IDENTIFICADOR DOS_PUNTOS type igualacion
        | LET IDENTIFICADOR igualacion
    """
    if (len(p) == 8):
        p[0] = Declaracion(True, p[3], p[5], p[6], p.lineno(1), p.lexpos(1));
    elif (len(p) == 6):
        p[0] = Declaracion(True, p[3], None, p[4], p.lineno(1), p.lexpos(1));
    elif (len(p) == 7):
        p[0] = Declaracion(False, p[2], p[4], p[5], p.lineno(1), p.lexpos(1));
    elif (len(p) == 4):
        p[0] = Declaracion(False, p[2], None, p[3], p.lineno(1), p.lexpos(1));

def p_type(p):
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

def p_igualacion(p):
    """
    igualacion : IGUALACION expresion
    """
    p[0] = p[2];

# unidad aritmética
def p_expresion(p):
    """
    expresion : ENTERO
        | DECIMAL   
        | TRUE
        | FALSE
        | CARACTER
        | CADENA
        | RESTA expresion %prec UMENOS
        | I64 DOS_PUNTOS DOS_PUNTOS POTENCIA PARENTESIS_ABRE expresion COMA expresion PARENTESIS_CIERRA
        | expresion SUMA expresion
        | expresion RESTA expresion
        | expresion MULTIPLICACION expresion
        | expresion DIVISION expresion
        | expresion MODULO expresion
    """
    if (len(p) == 2): 
        print("val: " + str(p[1]) + " type: " + type(p[1]))
        # terminales
        if (type(p[1] == int)):
            print("soi dfafd")
            # enteros
            p[0] = Literal(p[1], TipoDato.INT64, p.lineno(1), p.lexpos(1));
        elif (type(p[1] == float)):
            # decimales
            print("soi decimal")
            p[0] = Literal(p[1], TipoDato.FLOAT64, p.lineno(1), p.lexpos(1));
        elif (p[1] == 'true' or p[1] == 'false'):
            # bools
            print("soi bool")
            p[0] = Literal(p[1], TipoDato.BOOLEAN, p.lineno(1), p.lexpos(1));
        elif (re.fullmatch(r'.', p[1])):
            # chars
            print("soi char")
            p[0] = Literal(p[1], TipoDato.CHAR, p.lineno(1), p.lexpos(1));
        else:
            # strings
            print("soi str")
            p[0] = Literal(p[1], TipoDato.STRING, p.lineno(1), p.lexpos(1));
    elif (len(p) == 3):
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

# error sintáctico
def p_error(p):
    print(f'Error de sintaxis {p.type}')

# construyendo el parser (analizador sintáctico)
parser = yacc()