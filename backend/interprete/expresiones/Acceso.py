# clase para poder accesar a las variables
from .Expresion import Expresion
from ..extra.Console import Console
from ..extra.Scope import Scope
from ..extra.Retorno import RetornoExpresion

class Acceso(Expresion):
    def __init__(self, linea, columna, id: str):
        super().__init__(linea, columna)

    def ejecutar(self, console: Console, scope: Scope):
        valor = scope.getValor(self.id, self.linea, self.columna);
        if (valor != None):
            return RetornoExpresion(valor.valor, valor.tipo);
        # error, no se encontró la variable