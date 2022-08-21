# clase para manejar los entornos, ambitos, env o scopes
from ..extra.TablaSimbolo import TablaSimbolo
from .Tipos import TipoDato 
from .Simbolo import Simbolo

class Scope:
    def __init__(self, padre):
        self.padre = padre;
        self.simbolos = [];
        self.variables = {};
        self.funciones = {};
    
    # función para crear una variable
    def crearVariable(self, id: str, valor, tipo: TipoDato, mut:bool, esVector:bool, with_capacity:int, linea: int, columna: int):
        scope: Scope = self;

        while(scope != None):
            # verificamos que no se haya declarado antes la misma variable
            if(scope.variables.get(id)):
                pass;
                # ERROR: la variable ya ha sido declarada
            scope = scope.padre;
        # procedemos a crear la variable
        self.variables[id] = Simbolo(valor, id, tipo, mut, esVector, with_capacity);
        # lo guardamos en la tabla de simbolos
        self.simbolos.append(TablaSimbolo(id, 'variable', str(tipo), '', linea, columna))

    # función para obtener el valor de una variable
    def getValor(self, id:str, linea:int, columna:int):
        scope: Scope = self;
        while(scope != None):
            if (scope.variables.get(id) != None):
                return scope.variables.get(id);
            scope = scope.padre;
        # error: no se ha encontrado la variable

    # función para obtener el scopeo más general, el global
    def getGlobal(self):
        scope:Scope = self;
        while(scope.padre != None):
            scope = scope.padre;
        return scope;

    def setValor(self, id:str, valor, linea:int, columna:int):
        scope: Scope = self;
        while(scope != None):
            if (scope.variables.get(id) != None):
                val:Simbolo = scope.variables.get(id);
                if (val.tipo == valor.tipo):
                    if (val.mut):
                        scope.variables.update({id : Simbolo(valor.valor, id, valor.tipo, True, val.esVector)});
                    else:
                        # error, variable no mutable
                        pass;
                else:
                    # error tipos incopatibles
                    pass;
            scope = scope.padre;
    
    def setValorArreglo(self, id:str, valor, tipo, indices:list, linea:int, columna:int):
        scope: Scope = self;
        while(scope != None):
            if (scope.variables.get(id) != None):
                val:Simbolo = scope.variables.get(id);
                if (val.tipo != tipo):
                    # ERROR. Tipos imcompatible, un arreglo de tipo ... no puede contener una expresión de tipo ...
                    pass;
                val.valor = self.recorrerLista(valor, val.valor, indices, 0);
                scope.variables.update({id: val});
            scope = scope.padre;

    def recorrerLista(self, valor, lista, indices:list, iAux):
        # verificamos que aun se ana lista
        if (iAux < len(indices)):
            try:
                lista[indices[iAux]] = self.recorrerLista(valor, lista[indices[iAux]], indices, iAux + 1);
                return lista;
            except:
                # ERROR. Indice fuera de rango
                print("INDICE FUERA DE RANGO")
        else:
            # llegado a este punto es la expresion a cambiar
            return valor;

