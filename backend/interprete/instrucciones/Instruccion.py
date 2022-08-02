from ..extra.Console import Console
from ..extra.Scope import Scope

class Instruccion:
    def __init__(self, linea: int, columna: int):
        self.linea: int = linea;
        self.columna: int = linea;

    def ejecutar(self, console: Console, scope: Scope):
        pass;