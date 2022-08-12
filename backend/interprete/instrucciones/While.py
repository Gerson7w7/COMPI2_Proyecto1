from ..extra.Tipos import TipoDato, TipoTransferencia
from .Instruccion import Instruccion
from ..extra.Console import Console
from ..extra.Scope import Scope

class While(Instruccion):
    def __init__(self, condicion, bloque: Instruccion, linea: int, columna: int):
        super().__init__(linea, columna)
        self.condicion = condicion;
        self.bloque = bloque;

    def ejecutar(self, console: Console, scope: Scope):
        # primero ejecutamos la condición
        valCondicion = self.condicion.ejecutar(console, scope);
        # verificando de que se trate de un boolean
        if (valCondicion.tipo != TipoDato.BOOLEAN): pass; # error tiene que se bool 
        while(valCondicion.valor):
            # ejecutamos las instrucciones dentro del loop
            val = self.bloque.ejecutar(console, scope);
            # si es una instruccion de transferencia se analiza
            if (val != None):
                # break
                if (val.retorno == TipoTransferencia.BREAK):
                    if (val.valor != None):
                        # error no se puede retornar un valor en un while
                        pass;
                    break;
                # return
                elif (val.retorno == TipoTransferencia.RETURN):
                    return val;
                # continua
                elif (val.retorno == TipoTransferencia.CONTINUE):
                    continue;
            # ejecutamos otra vez la condición
            valCondicion = self.condicion.ejecutar(console, scope);
            if (valCondicion.tipo != TipoDato.BOOLEAN): pass; # error tiene que se bool 