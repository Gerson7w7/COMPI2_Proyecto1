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
            print("entro acua")
            for expresion in self.expresiones:
                val = expresion.ejecutar(console, scope)
                self.cadena = self.cadena.replace('\{\}', str(val), 1);
            print(self.cadena);
            console.append(self.cadena + '\n');
        else:
            print(self.cadena);
            console.append(self.cadena + '\n');