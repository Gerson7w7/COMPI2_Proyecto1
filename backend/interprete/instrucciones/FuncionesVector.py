from ..extra.Simbolo import Simbolo
from .Instruccion import Instruccion
from ..extra.Console import Console
from ..extra.Scope import Scope

class Push(Instruccion):
    def __init__(self, id:str, expresion, linea: int, columna: int):
        super().__init__(linea, columna);
        self.id = id;
        self.expresion = expresion;

    def ejecutar(self, console: Console, scope: Scope):
        # ejecutando la expresión
        val = self.expresion.ejecutar(console, scope);
        # obtenemos el vector
        vector:Simbolo = scope.getValor(self.id, self.linea, self.columna);
        if (vector.esVector != None):
            # ERROR. No es un vector
            pass;
        if (not vector.esVector):
            # ERROR. No es un vector
            pass;
        if (val.tipo != vector.tipo):
            # ERROR. Tipos incompatibles
            pass;
        vector.valor.append(val.valor);
        # ahora revisaremos si se trata de un vector con un tamaño definido
        if (vector.with_capacity != None):
            if (vector.with_capacity < len(vector.valor)):
                vector.with_capacity = vector.with_capacity * 2;
        scope.setValor(self.id, vector, self.linea, self.columna);