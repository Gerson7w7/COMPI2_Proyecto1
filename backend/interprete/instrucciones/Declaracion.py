from ..extra.Tipos import TipoDato
from .Instruccion import Instruccion
from ..extra.Console import Console
from ..extra.Scope import Scope

class Declaracion(Instruccion):
    def __init__(mut:bool, id: str, tipo: str, valor, self, linea: int, columna: int):
        super().__init__(linea, columna)
        self.id = id;
        self.tipo = tipo;
        self.valor = valor;

    def ejecutar(self, console: Console, scope: Scope):
        # analizando el tipo de dato
        tipo: TipoDato;
        if (self.tipo == 'i64'):
            tipo = TipoDato.INT64
        elif (self.tipo == 'f64'):
            tipo = TipoDato.FLOAT64
        elif (self.tipo == 'bool'):
            tipo = TipoDato.BOOLEAN
        elif (self.tipo == 'char'):
            tipo = TipoDato.CHAR
        elif (self.tipo == 'string'):
            tipo = TipoDato.STRING
        elif (self.tipo == 'str'):
            tipo = TipoDato.STR

        # variables inicializadas
        if (self.valor != None):
            # obteniendo el valor de la expresion
            val = self.valor.ejecutar(console, scope);
            if (val.tipo == tipo):
                scope.crearVariable()
            else:
                # error, diferentes tipos de datos
                pass;
        # variables no inicializadas
        else:
            pass;
