# importamos la libería lex
from ..ply import lex

# definimos los tokens de nuestro lenguaje
tokens = (
    # palabras reservadas
    'LET', 'MUT', 'NEW', 'AS', 'INTERROGACION', 'AMPERSON', 'MOD', 'PUB', # palabras reservadas
    'CORCHETE_ABRE', 'CORCHETE_CIERRA', 'PARENTESIS_ABRE', 'PARENTESIS_CIERRA', 'LLAVE_ABRE', 'LLAVE_CIERRA', # encapsulamiento
    'COMA', 'PUNTO_COMA', 'DOS_PUNTOS', 'PUNTO', #separaciones
    # tipos de datos
    'ENTERO', 'I64', 'DECIMAL', 'F64', # números
    'BOOL', 'TRUE', 'FALSE', # boolanos
    'CHAR', 'CARACTERES', # chars
    'STRING', 'STR', 'CADENA', # strings
    'USIZE', 'VEC', # vectores y arreglos
    'STRUCT', #structs
    # operadores
    'SUMA', 'RESTA', 'MULTIPLICACION', 'DIVISION', 'POTENCIA', 'MODULO', # aritméticos
    'IGUALDAD', 'DESIGUALDAD', 'IGUALACION', 'MENOR', 'MAYOR', 'MENOR_IGUAL', 'MAYOR_IGUAL', # relacionales
    'OR', 'AND', 'NOT', # lógicos
    # funciones
    'PRINTLN', # impresión
    'FN', 'FLECHA_GUION', # funciones y métodos
    'ABS', 'SQRT', 'TO_STRING', 'CLONE', # funciones nativas
    'LEN', 'PUSH', 'REMOVE', 'CONTAINS', 'INSERT', 'CAPACITY', 'WITH_CAPACITY', # funciones para vectores
    # sentencias de control
    'IF', 'ELSE', # if-else
    'MATCH', 'FLECHA_IGUAL', 'GUION_BAJO', # match (similar al switch)
    # sentencias cíclicas
    'LOOP', 'WHILE', 'FOR', 'IN',
    # sentencias de transferencias
    'BREAK', 'CONTINUE', 'RETURN',
    # identificadores
    'IDENTIFICADOR',
)

# ignora los espacios y tabulaciones
t_ignore = ' \t'

# tokens con expresiones regulares simples
t_LET = r'let';
t_MUT = r'mut';
t_NEW = r'new';
t_AS = r'as';
t_INTERROGACION = r'\?';
t_AMPERSON = r'\&';
t_MOD = r'mod';
t_PUB = r'pub';
t_CORCHETE_ABRE = r'\[';
t_CORCHETE_CIERRA = r'\]';
t_PARENTESIS_ABRE = r'\(';
t_PARENTESIS_CIERRA = r'\)';
t_LLAVE_ABRE = r'\{';
t_LLAVE_CIERRA = r'\}';
t_COMA = r',';
t_PUNTO_COMA = r';';
t_DOS_PUNTOS = r':';
t_PUNTO = r'\.';
t_I64 = r'i64';
t_F64 = r'f64';
t_BOOL = r'bool';
t_TRUE = r'true';
t_FALSE = r'false';
t_CHAR = r'char';
t_STRING = r'string';
t_STR = r'str';
t_USIZE = r'usize';
t_VEC = r'VEC';
t_STRUCT = r'struct'
t_SUMA = r'\+';
t_RESTA = r'\-';
t_MULTIPLICACION = r'\*';
t_DIVISION = r'/';
t_POTENCIA = r'pow';
t_MODULO = r'%';
t_IGUALDAD = r'==';
t_DESIGUALDAD = r'!=';
t_IGUALACION = r'=';
t_MENOR = r'<';
t_MAYOR = r'>';
t_MENOR_IGUAL = r'=<';
t_MAYOR_IGUAL = r'=>';
t_OR = r'\|\|';
t_AND = r'&&';
t_NOT = r'!';
t_PRINTLN = r'println';
t_FN = r'fn';
t_FLECHA_GUION = r'->';
t_ABS = r'abs';
t_SQRT = r'SQRT';
t_TO_STRING = r'to_string';
t_CLONE = r'clone';
t_LEN = r'len';
t_PUSH = r'push';
t_REMOVE = r'remove';
t_CONTAINS = r'contains';
t_INSERT = r'insert';
t_CAPACITY = r'capacity';
t_WITH_CAPACITY = r'with_capacity';
t_IF = r'if';
t_ELSE = r'else';
t_MATCH = r'match';
t_FLECHA_IGUAL = r'=>';
t_GUION_BAJO = r'_';
t_LOOP = r'loop';
t_WHILE = r'while';
t_FOR = r'for';
t_IN = r'in';
t_BREAK = r'break';
t_CONTINUE = r'continue';
t_RETURN = r'return';

# tokens con expresiones regulares más elaborados y con acciones de código
def t_ENTERO(t):
    r'\d+';
    t.value = int(t.value);
    return t;

def t_DECIMAL(t):
    r'\d+\.\d+';
    t.value = float(t.value);
    return t;

def t_CARACTERES(t):
    r'\'(\\)?.\'';
    t.value = t.value.replace('\'', '');
    return t;

def t_CADENA(t):
    r'\"[^\"]*\"';
    t.value = t.value.replace('\"', '');
    return t;

def t_IDENTIFICADOR(t):
    r'([a-zA-Z_])[a-zA-Z0-9_]*';
    return t;

# contamos las líneas del código
def t_nuevalinea(t):
    r'\n+';
    t.lexer.lineno += len(t.value)

# manejo de errores léxicos
def t_error(t):
    print(f'Caracter no reconocido {t.value[0]!r}. En la linea {t.lexer.lineno}')
    t.lexer.skip(1)

def t_comentario(t):
    r'//.*';
    pass;

# construímos el lexer (analizador léxico)
lex.lex();