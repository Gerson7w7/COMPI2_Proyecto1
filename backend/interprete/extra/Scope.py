# clase para manejar los entornos, ambitos, env o scopes
import copy
from ..extra.TablaSimbolo import TablaSimbolo
from .Tipos import TipoDato 
from .Simbolo import Simbolo
from .Console import _Error
from datetime import datetime

class Scope:
    def __init__(self, padre, ambito:str):
        self.padre = padre;
        self.ambito = ambito;
        self.simbolos = [];
        self.variables = {};
        self.funciones = {};
        self.structs = {};
    
    # función para crear una variable
    def crearVariable(self, id: str, valor, tipo: TipoDato, mut:bool, esVector:bool, with_capacity:int, referencia, linea: int, columna: int):
        scope: Scope = self;
        while(scope != None):
            # verificamos que no se haya declarado antes la misma variable
            if(scope.variables.get(id)):
                # ERROR: la variable ya ha sido declarada
                _error = _Error(f'No se ha podido efectuar la operacion {self.tipo} con {val1.valor} y {val2.valor}', scope.ambito, self.linea, self.columna, datetime.now())
                raise Exception(_error);
            scope = scope.padre;
        # procedemos a crear la variable
        self.variables[id] = Simbolo(valor, id, tipo, mut, esVector, with_capacity, referencia);
        # lo guardamos en la tabla de simbolos
        self.simbolos.append(TablaSimbolo(id, 'variable', str(tipo), '', linea, columna))

    # función para obtener el valor de una variable
    def getValor(self, id:str, linea:int, columna:int):
        scope: Scope = self;
        while(scope != None):
            if (scope.variables.get(id) != None):
                return scope.variables.get(id);
            scope = scope.padre;
        print("error: no se ha encontrado la variable");
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
                        scope.variables.update({id : Simbolo(valor.valor, id, valor.tipo, True, val.esVector, val.with_capacity, val.referencia)});
                        # si se pasó por referencia cambiamos también la original
                        if (val.referencia != None):
                            ref = val.referencia;
                            ref.scope.variables.update({ref.id : Simbolo(valor.valor, ref.id, valor.tipo, ref.val.mut, ref.val.esVector, ref.val.with_capacity, ref.val.referencia)});
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
                if (not val.mut):
                    # ERROR. Variable no mutable.
                    pass;
                valNuevo = self.recorrerLista(valor, copy.deepcopy(val.valor), indices, 0);
                scope.variables.update({id: Simbolo(valNuevo, id, val.tipo, True, val.esVector, val.with_capacity, val.referencia)});
                # si se pasó por referencia cambiamos también la original
                if (val.referencia != None):
                    ref = val.referencia;
                    ref.scope.variables.update({ref.id : Simbolo(valNuevo, ref.id, val.tipo, ref.val.mut, ref.val.esVector, ref.val.with_capacity, ref.val.referencia)});
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

    def guardarFuncion(self, id:str, fn, tipo_retorno:TipoDato, linea:int, columna:int):
        scope: Scope = self;
        while(scope != None):
            # verificamos que no se haya declarado antes la misma funcion
            if(scope.funciones.get(id)):
                pass;
                # ERROR: la funcion ya ha sido declarada
            scope = scope.padre;
        # procedemos a guardar la funcion
        self.funciones[id] = fn;
        # lo guardamos en la tabla de simbolos
        self.simbolos.append(TablaSimbolo(id, 'función', str(tipo_retorno), '', linea, columna));

    def getFuncion(self, id:str, linea:int, columna:int):
        scope: Scope = self;
        while(scope != None):
            if (scope.funciones.get(id) != None):
                return scope.funciones.get(id);
            scope = scope.padre;
        # error: no se ha encontrado la variable

    def guardarStruct(self, id:str, struct, linea:int, columna:int):
        scope: Scope = self;
        while(scope != None):
            # verificamos que no se haya declarado antes la misma funcion
            if(scope.structs.get(id)):
                pass;
                # ERROR: la funcion ya ha sido declarada
            scope = scope.padre;
        # procedemos a guardar la funcion
        self.structs[id] = struct;
        # lo guardamos en la tabla de simbolos
        self.simbolos.append(TablaSimbolo(id, 'struct', id, '', linea, columna));

    def getStruct(self, id:str, linea:int, columna:int):
        scope: Scope = self;
        while(scope != None):
            if (scope.structs.get(id) != None):
                return scope.structs.get(id);
            scope = scope.padre;
        # error: no se ha encontrado la variable