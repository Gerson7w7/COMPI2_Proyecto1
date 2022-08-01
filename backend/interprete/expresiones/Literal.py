from .Expresion import Expresion
from ..extra.Tipos import TipoDato

class Literal(Expresion):
    def __init__(self, linea: int, columna: int, valor, tipo: TipoDato):
        super().__init__(linea, columna)
        self.valor = valor;
        self.tipo = tipo;
    
    def ejecutar(self, console: Console, scope: Scope):
        if (self.tipo == TipoDato.INT64):
            return 