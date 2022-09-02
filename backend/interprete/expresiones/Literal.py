from .Expresion import Expresion
from ..extra.Tipos import TipoDato
from ..extra.Console import Console
from ..extra.Scope import Scope
from ..extra.Retorno import RetornoExpresion

class Literal(Expresion):
    def __init__(self, valor, tipo: TipoDato, linea: int, columna: int):
        super().__init__(linea, columna)
        self.valor = valor;
        self.tipo = tipo;
    
    def ejecutar(self, console: Console, scope: Scope):
        if (self.tipo == TipoDato.INT64):
            return RetornoExpresion(int(self.valor), TipoDato.INT64, None);
        elif (self.tipo == TipoDato.FLOAT64):
            return RetornoExpresion(float(self.valor), TipoDato.FLOAT64, None);
        elif (self.tipo == TipoDato.BOOLEAN):
            print("BOOOL:: " + str(self.valor) +" -> " + str(bool(self.valor)))
            return RetornoExpresion(self.valor, TipoDato.BOOLEAN, None);
        elif (self.tipo == TipoDato.CHAR):
            return RetornoExpresion(self.valor, TipoDato.CHAR, None);
        elif (self.tipo == TipoDato.STRING or self.tipo == TipoDato.STR):
            return RetornoExpresion(self.valor, TipoDato.STR, None);
        # sino error sintactico
