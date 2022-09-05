from ..extra.Console import Console

class Expresion:
    def __init__(self, linea, columna):
        self.linea: int = linea;
        self.columna: int = columna;

    def ejecutar(self, console: Console, scope):
        pass; 