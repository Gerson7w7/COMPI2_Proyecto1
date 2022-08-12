from ..extra.Console import Console
from ..extra.Scope import Scope

class Expresion:
    def __init__(self, linea, columna):
        self.linea: int = linea;
        self.columna: int = columna;

    def ejecutar(self, console: Console, scope: Scope):
        pass; 