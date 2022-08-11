# ejemplos: https://www.dabeaz.com/ply/ply.html#ply_nn33
from interprete.ply.yacc import yacc
from interprete.analizador import lexer

import re
from ..expresiones.Aritmetica import Aritmetica
from ..extra.Tipos import TipoAritmetica, TipoDato, TipoLogico, TipoRelacional
from ..extra.Ast import Ast
from ..instrucciones.Declaracion import Declaracion, Asignacion
from ..expresiones.Literal import Literal
from interprete.instrucciones.Imprimir import Imprimir
from interprete.expresiones.Relacional import Relacional
from ..expresiones.Logico import Logico
from ..expresiones.Acceso import Acceso
from interprete.instrucciones.Bloque import Bloque
from interprete.instrucciones.IfElse import IfElse
from interprete.instrucciones.Match import Case, Match

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
        p[1].append(p[2]); p[0] = p[1];
    else:
        p[0] = [p[1]];

# declaracion de variables
def p_instruccion(p):
    """
    instruccion : declaracion PUNTO_COMA
        | imprimir PUNTO_COMA
        | asignacion PUNTO_COMA
        | if
        | match
        | expresion
    """
    p[0] = p[1];

def p_declaracion(p):
    """
    declaracion : LET MUT IDENTIFICADOR DOS_PUNTOS type igualacion
        | LET MUT IDENTIFICADOR igualacion
        | LET IDENTIFICADOR DOS_PUNTOS type igualacion
        | LET IDENTIFICADOR igualacion
    """
    if (len(p) == 7):
        p[0] = Declaracion(True, p[3], p[5], p[6], p.lineno(1), p.lexpos(1));
    elif (len(p) == 5):
        p[0] = Declaracion(True, p[3], None, p[4], p.lineno(1), p.lexpos(1));
    elif (len(p) == 6):
        p[0] = Declaracion(False, p[2], p[4], p[5], p.lineno(1), p.lexpos(1));
    else:
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
    else:
        p[0] = p[2];

def p_igualacion(p):
    """
    igualacion : IGUALACION expresion
    """
    p[0] = p[2];

# unidad aritmética
def p_expresion_aritmetica(p):
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
        p[0] = Aritmetica(p[2], Literal('-1', p[2].tipo, p.lineno(1), p.lexpos(1)), TipoAritmetica.MULTIPLICACION, p.lineno(1), p.lexpos(1));
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

# unidad relacional
def p_expresion_relacional(p):
    """
    expresion : expresion IGUALDAD expresion
        | expresion DESIGUALDAD expresion
        | expresion MENOR_IGUAL expresion
        | expresion MAYOR_IGUAL expresion
        | expresion MENOR expresion
        | expresion MAYOR expresion
    """
    if (p[2] == '=='):
        p[0] = Relacional(p[1], p[3], TipoRelacional.IGUALDAD, p.lineno(1), p.lexpos(1));
    elif (p[2] == '!='):
        p[0] = Relacional(p[1], p[3], TipoRelacional.DESIGUALDAD, p.lineno(1), p.lexpos(1));
    elif (p[2] == '<='):
        p[0] = Relacional(p[1], p[3], TipoRelacional.MENOR_IGUAL, p.lineno(1), p.lexpos(1));
    elif (p[2] == '>='):
        p[0] = Relacional(p[1], p[3], TipoRelacional.MAYOR_IGUAL, p.lineno(1), p.lexpos(1));
    elif (p[2] == '<'):
        p[0] = Relacional(p[1], p[3], TipoRelacional.MENOR, p.lineno(1), p.lexpos(1));
    elif (p[2] == '>'):
        p[0] = Relacional(p[1], p[3], TipoRelacional.MAYOR, p.lineno(1), p.lexpos(1));

# unidad lógica
def p_expresion_logica(p):
    """
    expresion : NOT expresion
        | expresion OR expresion
        | expresion AND expresion
    """
    if (len(p) == 3):
        p[0] = Logico(p[2], None, TipoLogico.NOT, p.lineno(1), p.lexpos(1))
    elif (p[2] == '||'):
        p[0] = Logico(p[1], p[3], TipoLogico.OR, p.lineno(1), p.lexpos(1))
    elif (p[2] == '&&'):
        p[0] = Logico(p[1], p[3], TipoLogico.AND, p.lineno(1), p.lexpos(1))

def p_expresion_terminales(p):
    """
    expresion : ENTERO
        | DECIMAL   
        | TRUE
        | FALSE
        | CARACTER
        | CADENA
    """
    # terminales
    if (type(p[1]) == int):
        # enteros
        p[0] = Literal(p[1], TipoDato.INT64, p.lineno(1), p.lexpos(1));
    elif (type(p[1]) == float):
        # decimales
        p[0] = Literal(p[1], TipoDato.FLOAT64, p.lineno(1), p.lexpos(1));
    elif (p[1] == 'true' or p[1] == 'false'):
        # bools
        p[0] = Literal(p[1], TipoDato.BOOLEAN, p.lineno(1), p.lexpos(1));
    elif (re.fullmatch(r'.', p[1])):
        # chars
        p[0] = Literal(p[1], TipoDato.CHAR, p.lineno(1), p.lexpos(1));
    else:
        # strings
        p[0] = Literal(p[1], TipoDato.STRING, p.lineno(1), p.lexpos(1));

def p_expresion_identificador(p):
    """
    expresion : IDENTIFICADOR
    """
    p[0] = Acceso(p[1], p.lineno(1), p.lexpos(1))

def p_expresion_inst(p):
    """
    expresion : if
        | match
        | imprimir
    """
    p[0] = p[1];

# impresión en consola (println)
def p_imprimir(p):
    """
    imprimir : PRINTLN NOT PARENTESIS_ABRE CADENA COMA expresiones PARENTESIS_CIERRA
        | PRINTLN NOT PARENTESIS_ABRE CADENA PARENTESIS_CIERRA
    """
    if (len(p) == 8):
        p[0] = Imprimir(p[4], p[6], p.lineno(1), p.lexpos(1));
    else:
        p[0] = Imprimir(p[4], None, p.lineno(1), p.lexpos(1));

# expresiones para el println
def p_expresiones(p):
    """
    expresiones : expresiones COMA expresion
        | expresion
    """
    if (len(p) == 4):
        p[1].append(p[3]); p[0] = p[1];
    else:
        p[0] = [p[1]];  

def p_asignacion(p):
    """
    asignacion : IDENTIFICADOR igualacion
    """
    p[0] = Asignacion(p[1], p[2], p.lineno(1), p.lexpos(1))

def p_if(p):
    """
    if : IF expresion bloque else
    """
    p[0] = IfElse(p[2], p[3], p[4], p.lineno(1), p.lexpos(1));

def p_else(p):
    """
    else : ELSE bloque
        | ELSE if
        | empty
    """
    if (len(p) == 3):
        p[0] = p[2];
    else:
        p[0] = p[1];

def p_bloque(p):
    """
    bloque : LLAVE_ABRE instrucciones LLAVE_CIERRA
        | LLAVE_ABRE LLAVE_CIERRA
    """
    if (len(p) == 4):
        p[0] = Bloque(p[2], p.lineno(1), p.lexpos(1));
    else:
        p[0] = Bloque([], p.lineno(1), p.lexpos(1));

def p_match(p):
    """
    match : MATCH expresion LLAVE_ABRE case_list LLAVE_CIERRA
    """
    p[0] = Match(p[2], p[4], p.lineno(1), p.lexpos(1));

def p_case_list(p):
    """
    case_list : case_list case
        | case
    """
    if (len(p) == 3):
        p[1].append(p[2]); p[0] = p[1];
    else:
        p[0] = [p[1]];   

def p_case(p):
    """
    case : coincidencias FLECHA_IGUAL cuerpo_match
    """
    p[0] = Case(p[1], p[3], p.lineno(1), p.lexpos(1));

def p_coincidencias(p):
    """
    coincidencias : coincidencias BARRA expresion
        | expresion
        | GUION_BAJO
    """
    if (len(p) == 4):
        p[1].append(p[2]); p[0] = p[1];
    else:
        p[0] = [p[1]];  

def p_cuerpo_match(p):
    """
    cuerpo_match : expresion COMA
        | bloque
    """
    p[0] = p[1];

def p_empty(p):
    """
    empty :
    """
    p[0] = None;

# error sintáctico
# def p_error(p):
#     print(f'Error de sintaxis {p.type}, linea: {p.lineno}, columna: {p.lexpos}')

# construyendo el parser (analizador sintáctico)
parser = yacc()