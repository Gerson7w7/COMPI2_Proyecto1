import copy

from ..extra.Tipos import TipoDato
from ..extra.Simbolo import Simbolo
from .Instruccion import Instruccion
from ..extra.Console import Console
from ..extra.Scope import Scope
from ..extra.Retorno import RetornoExpresion

class Push(Instruccion):
    def __init__(self, id, expresion, linea: int, columna: int):
        super().__init__(linea, columna);
        self.id = id;
        self.expresion = expresion;

    def ejecutar(self, console: Console, scope: Scope):
        # ejecutando la expresión
        val = self.expresion.ejecutar(console, scope);
        # obtenemos el vector
        vector:Simbolo = copy.deepcopy(self.id.ejecutar(console, scope));
        if (vector.esVector != None):
            # ERROR. No es un vector
            pass;
        if (not vector.esVector):
            # ERROR. Los arreglos no contiene la función push
            pass;
        if (vector.tipo == None):
            vector.tipo = val.tipo;
        if (val.tipo != vector.tipo):
            # ERROR. Tipos incompatibles
            pass;
        vector.valor.append(val.valor);
        # ahora revisaremos si se trata de un vector con un tamaño definido
        if (vector.with_capacity != None):
            if (vector.with_capacity < len(vector.valor)):
                vector.with_capacity = vector.with_capacity * 2;
        scope.setValor(self.id.id, vector, self.linea, self.columna);

class Insert(Instruccion):
    def __init__(self, id:str, exp1, exp2, linea: int, columna: int):
        super().__init__(linea, columna);
        self.id = id;
        self.exp1 = exp1;
        self.exp2 = exp2;
    
    def ejecutar(self, console: Console, scope: Scope):
        # ejecutando las expresiones
        val1 = self.exp1.ejecutar(console, scope);
        val2 = self.exp2.ejecutar(console, scope);
        # obtenemos el vector
        vector:Simbolo = copy.deepcopy(self.id.ejecutar(console, scope));
        if (vector.esVector != None):
            # ERROR. No es un vector
            pass;
        if (not vector.esVector):
            # ERROR. Los arreglos no contiene la función insert
            pass;
        if (val2.tipo != vector.tipo):
            # ERROR. Tipos incompatibles
            pass;
        if (val1.tipo != TipoDato.INT64):
            # ERROR. No se puede acceder al indice val1.tipo.
            pass;
        vector.valor.insert(val1.valor, val2.valor);
        # ahora revisaremos si se trata de un vector con un tamaño definido
        if (vector.with_capacity != None):
            if (vector.with_capacity < len(vector.valor)):
                vector.with_capacity = vector.with_capacity * 2;
        scope.setValor(self.id.id, vector, self.linea, self.columna);

class Remove(Instruccion):
    def __init__(self, id:str, exp, linea: int, columna: int):
        super().__init__(linea, columna);
        self.id = id;
        self.exp = exp;

    def ejecutar(self, console: Console, scope: Scope):
        # indice del elemento a eliminar
        val = self.exp.ejecutar(console, scope);
        # obtenemos el vector
        vector:Simbolo = copy.deepcopy(self.id.ejecutar(console, scope));
        print("remove: " + str(vector.valor))
        if (vector.esVector != None):
            # ERROR. No es un vector
            pass;
        if (not vector.esVector):
            # ERROR. Los arreglos no contiene la función push
            pass;
        if (val.tipo != TipoDato.INT64):
            # ERROR. Tipos incompatibles
            pass;
        # primero obtenemos el elemento que se va a eliminar
        valorRetorno = vector.valor[val.valor];
        # ahora eliminamos el elemento
        vector.valor.remove(valorRetorno);
        # revisaremos si se trata de un vector con un tamaño definido
        if (vector.with_capacity != None):
            if (vector.with_capacity < len(vector.valor)):
                vector.with_capacity = vector.with_capacity * 2;
        scope.setValor(self.id.id, vector, self.linea, self.columna);
        return RetornoExpresion(valorRetorno, vector.tipo, None);

class Contains(Instruccion):
    def __init__(self, id:str, exp, linea: int, columna: int):
        super().__init__(linea, columna);
        self.id = id;
        self.exp = exp;
    
    def ejecutar(self, console: Console, scope: Scope):
        # expresion del elemento a buscar
        val = self.exp.ejecutar(console, scope);
        # obtenemos el vector
        vector:Simbolo = copy.deepcopy(self.id.ejecutar(console, scope));
        if (vector.esVector != None):
            # ERROR. No es un vector
            pass;
        if (not vector.esVector):
            # ERROR. Los arreglos no contiene la función push
            pass;
        if (val.tipo != vector.tipo):
            # ERROR. Tipos incompatibles
            pass;
        # revisamos si existe el elemento en la lista
        if (val.valor in vector.valor):
            return RetornoExpresion(True, TipoDato.BOOLEAN, None);
        return RetornoExpresion(False, TipoDato.BOOLEAN, None);

class Longitud(Instruccion):
    def __init__(self, id:str, linea: int, columna: int):
        super().__init__(linea, columna);
        self.id = id;

    def ejecutar(self, console: Console, scope: Scope):
        # obtenemos el vector
        vector:Simbolo = copy.deepcopy(self.id.ejecutar(console, scope));
        if (vector.esVector != None):
            # ERROR. No es un vector
            pass;
        if (not vector.esVector):
            # ERROR. Los arreglos no contiene la función push
            pass;
        # retornamos la longitud de la lista
        return RetornoExpresion(len(vector.valor), TipoDato.INT64, None);

class Capacity(Instruccion):
    def __init__(self, id:str, linea: int, columna: int):
        super().__init__(linea, columna);
        self.id = id;

    def ejecutar(self, console: Console, scope: Scope):
        # obtenemos el vector
        vector:Simbolo = copy.deepcopy(self.id.ejecutar(console, scope));
        if (vector.esVector != None):
            # ERROR. No es un vector
            pass;
        if (not vector.esVector):
            # ERROR. Los arreglos no contiene la función push
            pass;
        # retornamos la capacidad de la lista
        if (vector.with_capacity != None):
            return RetornoExpresion(vector.with_capacity, TipoDato.INT64, None);
        return RetornoExpresion(len(vector.valor) + 1, TipoDato.INT64, None);