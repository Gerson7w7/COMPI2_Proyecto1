from .Instruccion import Instruccion
from ..extra.Scope import Scope
from ..extra.Console import Console

class Struct(Instruccion):
    def __init__(self, id:str, parametros:list, linea: int, columna: int):
        super().__init__(linea, columna);
        self.id = id;
        self.parametros = parametros;

    def ejecutar(self, console: Console, scope: Scope):
        