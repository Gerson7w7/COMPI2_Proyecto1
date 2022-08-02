# clase para manejar los entornos, ambitos, env o scopes
import this
from ..extra.TablaSimbolo import TablaSimbolo
from .Tipos import TipoDato 
from .Simbolo import Simbolo

class Scope:
    def __init__(self, padre: this):
        self.padre = padre;
        self.simbolos = [];
        self.variables = {};
        self.funciones = {};
    
    # función para crear una variable
    def crearVariable(self, id: str, valor, tipo: TipoDato, linea: int, columna: int):
        scope: Scope = self;

        while(scope != None):
            # verificamos que no se haya declarado antes la misma variable
            if(scope.variables.get(id)):
                pass;
                # ERROR: la variable ya ha sido declarada
            scope = scope.padre;
        # procedemos a crear la variable
        self.variables[id] = Simbolo(valor, id, tipo);
        # lo guardamos en la tabla de simbolos
        self.simbolos.append(TablaSimbolo(id, 'variable', TipoDato[tipo], '', linea, columna))

    # función para obtener el valor de una variable
    def getValor(self, id:str, linea:int, columna:int):
        scope: Scope = self;
        while(scope != None):
            if (scope.variables.get(id) != None):
                return scope.variables.get(id);
            scope = scope.padre;
        # error: no se ha declarado la variable

    # función para obtener el scopeo más general, el global
    def getGlobal(self):
        scope:Scope = self;
        while(scope.padre != None):
            scope = scope.padre;
        return scope;