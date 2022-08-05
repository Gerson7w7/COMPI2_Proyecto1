# clase para poder accesar a las variables
from .Expresion import Expresion
from ..extra.Console import Console
from ..extra.Scope import Scope
from ..extra.Retorno import RetornoExpresion

class Acceso(Expresion):
    def __init__(self,  id: str, linea:int, columna:int):
        super().__init__(linea, columna)
        self.id = id;

    def ejecutar(self, console: Console, scope: Scope):
        # buscamos y obtenemos el valor
        valor = scope.getValor(self.id, self.linea, self.columna);
        if (valor != None):
            return RetornoExpresion(valor.valor, valor.tipo);
        # error, no se encontró la variable