from .Funcion import Funcion
from .Instruccion import Instruccion
from ..extra.Console import Console
from ..extra.Scope import Scope

class LlamadaFuncion(Instruccion):
    def __init__(self, id:str, argumentos:list, linea: int, columna: int):
        super().__init__(linea, columna);
        self.id = id;
        self.argumentos = argumentos;
    
    def ejecutar(self, console: Console, scope: Scope):
        newScope = Scope(scope.getGlobal());
        # obtenemos la función 
        funcion:Funcion = scope.getFuncion(self.id, self.linea, self.columna);
        # verificando si la cantidad de argumentos son == a la cantidad de parámetros de la función
        if (len(self.argumentos) != len(funcion.parametros)):
            # ERROR. Se esperaban x parametros y se encontraron x argumentos
            pass;
        for i in range(len(self.argumentos)):
            val = self.argumentos[i].ejecutar(console, scope);
            # verificando el tipo correcto del argumento
            funcion.tipoArgumentos(val.tipo, i, console, scope);
            # obtenemos el id del parametro correspondiente
            idParam = funcion.parametros[i].id;
            if (isinstance(val.valor, list)):
                idReferencia = self.argumentos[i].id;
                referencia = Referencia(scope, idReferencia, val);
                newScope.crearVariable(idParam, val.valor, val.tipo, True, val.esVector, val.with_capacity, referencia, self.linea, self.columna);
            else:
                newScope.crearVariable(idParam, val.valor, val.tipo, True, None, None, None, self.linea, self.columna);
        # ejecutando las instrucciones de la función 
        valBloque = funcion.bloque.ejecutar(console, newScope);
        # verificando el retorno de la función
        if (valBloque != None):
            funcion.tipoRetorno(valBloque.tipo);
        else:
            funcion.tipoRetorno(None);
        return valBloque;

class Referencia:
    def __init__(self, scope:Scope, id:str, val):
        self.scope = scope;
        self.id = id;
        self.val = val;