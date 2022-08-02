from .Expresion import Expresion
from ..extra.Tipos import TipoDato
from ..extra.Console import Console
from ..extra.Scope import Scope
from ..extra.Retorno import RetornoExpresion

class Literal(Expresion):
    def __init__(self, linea: int, columna: int, valor, tipo: TipoDato):
        super().__init__(linea, columna)
        self.valor = valor;
        self.tipo = tipo;
    
    def ejecutar(self, console: Console, scope: Scope):
        if (self.tipo == TipoDato.INT64):
            return RetornoExpresion(int(self.valor), TipoDato.INT64);
        elif (self.tipo == TipoDato.FLOAT64):
            return RetornoExpresion(float(self.valor), TipoDato.FLOAT64);
        elif (self.tipo == TipoDato.BOOLEAN):
            return RetornoExpresion(self.valor, TipoDato.BOOLEAN);
        elif (self.tipo == TipoDato.CHAR):
            return RetornoExpresion(self.valor, TipoDato.CHAR);
        elif (self.tipo == TipoDato.STRING or self.tipo == TipoDato.STR):
            return RetornoExpresion(float(self.valor), TipoDato.BOOLEAN);
        # sino error sintactico
