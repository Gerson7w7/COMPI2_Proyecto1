from enum import Enum 

class TipoDato(Enum):
    INT64 = 1
    FLOAT64 = 2
    BOOLEAN = 3
    CHAR = 4
    STRING = 5
    STR = 6

class TipoAritmetica(Enum):
    SUMA = 1
    RESTA = 2
    MULTIPLICACION = 3
    DIVISION = 4
    POTENCIA = 5
    MODULO = 6

class TipoRelacional(Enum):
    IGUALDAD = 1
    DESIGUALDAD = 2
    MENOR_IGUAL = 3
    MAYOR_IGUAL = 4
    MENOR = 5
    MAYOR = 6

class TipoLogico(Enum):
    NOT = 1
    AND = 2
    OR = 3