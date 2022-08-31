from interprete.extra.Tipos import TipoDato
from .Instruccion import Instruccion
from ..expresiones.Expresion import Expresion
from ..extra.Console import Console
from ..extra.Scope import Scope

class IfElse(Instruccion):
    def __init__(self, condicion: Expresion, bloque:Instruccion, bloqueElse:Instruccion, linea: int, columna: int):
        super().__init__(linea, columna);
        self.condicion = condicion;
        self.bloque = bloque;
        self.bloqueElse = bloqueElse;

    def ejecutar(self, console: Console, scope: Scope):
        # obtenemos el valor de la condición
        valCondicion = self.condicion.ejecutar(console, scope);
        # sino es un boolean la condición, entonces es un error
        if (valCondicion.tipo != TipoDato.BOOLEAN):
            # error condicion debe de ser booleano
            pass;
        # verificamos si es true o false
        if (valCondicion.valor):
            return self.bloque.ejecutar(console, scope, 'If');
        elif (self.bloqueElse != None):
            return self.bloqueElse.ejecutar(console, scope);
