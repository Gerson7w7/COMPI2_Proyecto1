# clase para poder accesar a las variables
from ..extra.Tipos import TipoDato
from ..extra.Simbolo import Simbolo
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
            return valor;
        # error, no se encontró la variable

class AccesoArreglo(Expresion):
    def __init__(self, id:str, indices:list, linea:int, columna:int):
        super().__init__(linea, columna);
        self.id = id;
        self.indices = indices;

    def ejecutar(self, console: Console, scope: Scope):
        # recuperamos el símbolo
        listaSimbolo:Simbolo = scope.getValor(self.id, self.linea, self.columna);
        # indices para obtener el valor deseado
        _indices:list = [];
        for i in self.indices:
            index = i.ejecutar(console, scope);
            if(index.tipo != TipoDato.INT64):
                # ERROR. No se puede acceder a la posicion val.valor
                pass; 
            _indices.append(index.valor);
        try:
            val = self.obtenerValor(listaSimbolo.valor, _indices, 0);
            return RetornoExpresion(val, listaSimbolo.tipo, None);
        except:
            print('ERROR. Indice fuera de rango');

    def obtenerValor(self, lista:list, _indices:list, i:int):
        if (i + 1 == len(_indices)):
            indice = _indices[i];
            return lista[indice];
        else:
            indice = _indices[i];
            return self.obtenerValor(lista[indice], _indices, i + 1);

# SIMBOLO:
# valor;
# id;
# tipo;
# mut;