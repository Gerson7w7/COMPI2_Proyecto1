from ..extra.Tipos import TipoDato
from .Expresion import Expresion
from ..extra.Console import Console
from ..extra.Scope import Scope
from ..extra.Retorno import RetornoExpresion

import math

class Abs(Expresion):
    def __init__(self, expresion,  linea: int, columna: int):
        super().__init__(linea, columna)
        self.expresion = expresion;

    def ejecutar(self, console: Console, scope: Scope):
        val = self.expresion.ejecutar(console, scope);
        # verificamos que sea un tipo de dato numérico
        if (val.tipo == TipoDato.INT64 or val.tipo == TipoDato.FLOAT64):
            return RetornoExpresion(abs(val.valor), val.tipo, None);
        # error, solo se aceptan datos numéricos

class Sqrt(Expresion):
    def __init__(self, expresion, linea, columna):
        super().__init__(linea, columna)
        self.expresion = expresion;

    def ejecutar(self, console: Console, scope: Scope):
        val = self.expresion.ejecutar(console, scope);
        # verificamos que sea un tipo de dato numérico
        if (val.tipo == TipoDato.INT64 or val.tipo == TipoDato.FLOAT64):
            if (val.valor < 0):
                # error, no existe raiz de numeros negativos 
                pass;
            return RetornoExpresion(math.sqrt(val.valor), val.tipo, None);
        # error, solo se aceptan datos numéricos

# sirve tanto par to_string() como para to_owned() xd
class ToString(Expresion):
    def __init__(self, expresion, linea, columna):
        super().__init__(linea, columna)
        self.expresion = expresion;

    def ejecutar(self, console: Console, scope: Scope):
        val = self.expresion.ejecutar(console, scope);
        # verificamos que sea un tipo de dato str o string
        if (val.tipo == TipoDato.STR or val.tipo == TipoDato.STRING):
            return RetornoExpresion(val.valor, TipoDato.STRING, None);
        # error, solo se aceptan datos numéricos

class Clone(Expresion):
    def __init__(self, expresion, linea, columna):
        super().__init__(linea, columna)
        self.expresion = expresion;

    def ejecutar(self, console: Console, scope: Scope):
        # retorna lo que sea que venga, ya que solo es una copia
        return self.expresion.ejecutar(console, scope);

class Chars(Expresion):
    def __init__(self, expresion, linea, columna):
        super().__init__(linea, columna)
        self.expresion = expresion;

    def ejecutar(self, console: Console, scope: Scope):
        # retorna lo que sea que venga, ya que solo es una copia
        return self.expresion.ejecutar(console, scope);