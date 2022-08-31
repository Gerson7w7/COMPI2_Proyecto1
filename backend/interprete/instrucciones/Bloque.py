from .Transferencia import Transferencia
from .Instruccion import Instruccion
from ..extra.Scope import Scope
from ..extra.Console import Console

class Bloque(Instruccion):
    def __init__(self, instrucciones:list, linea: int, columna: int):
        super().__init__(linea, columna)
        self.instrucciones = instrucciones;

    def ejecutar(self, console: Console, scope: Scope, ambito:str):
        # creando un nuevo entorno
        newScope = Scope(scope, ambito);
        for instruccion in self.instrucciones:
            try:
                val = instruccion.ejecutar(console, newScope);
                if (val != None):
                    return val;
            except Exception as e:
                # errores para recuperarse
                console.append(f'ERROR: {e.args[0].descripcion}. En la línea {e.args[0].linea}, columna {e.args[0].columna}\n');
                # agregamos a lista de errores
                console.error(e.args[0]);