from ..extra.Console import Console

class Instruccion:
    def __init__(self):
        self.linea: int;
        self.columna: int;

    def ejecutar(self, console: Console, scope: Scope):
        pass;