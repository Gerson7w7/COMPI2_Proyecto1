from .Instruccion import Instruccion
from ..extra.Scope import Scope
from ..extra.Console import Console
from ..extra.Retorno import RetornoExpresion
from ..extra.Tipos import TipoDato

class Bloque(Instruccion):
    def __init__(self, instrucciones:list, linea: int, columna: int):
        super().__init__(linea, columna)
        self.instrucciones = instrucciones;

    def ejecutar(self, console: Console, scope: Scope):
        # creando un nuevo entorno
        newScope = Scope(scope);

        for instruccion in self.instrucciones:
            try:
                val = instruccion.ejecutar(console, newScope);
                if (val != None):
                    return RetornoExpresion(val.valor, val.tipo);
            except:
                # errores para la recuperacion 
                pass;