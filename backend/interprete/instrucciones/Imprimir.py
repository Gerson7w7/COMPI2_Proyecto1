from .Instruccion import Instruccion
from ..extra.Console import Console
from ..extra.Scope import Scope

class Imprimir(Instruccion):
    def __init__(self, cadena:str, expresiones:list, linea: int, columna: int):
        super().__init__(linea, columna)
        self.cadena = cadena;
        self.expresiones = expresiones;

    def ejecutar(self, console: Console, scope: Scope):
        if (self.expresiones != None):
            nuevaCadena:str = "";
            for expresion in self.expresiones:
                val = expresion.ejecutar(console, scope)
                if (isinstance(val.valor, list) == True):
                    nuevaCadena = self.cadena.replace("{:?}", str(val.valor), 1);
                else:
                    nuevaCadena = self.cadena.replace("{}", str(val.valor), 1);
            console.append(nuevaCadena + '\n');
        else:
            console.append(self.cadena + '\n');