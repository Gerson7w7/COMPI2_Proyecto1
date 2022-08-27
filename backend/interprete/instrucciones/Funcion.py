from ..extra.Tipos import TipoDato
from .Arreglo import Arreglo, Dimension
from .Instruccion import Instruccion
from ..extra.Scope import Scope
from ..extra.Console import Console

class Funcion(Instruccion):
    def __init__(self, id:str, parametros:list, retorno_fn, bloque:Instruccion, linea: int, columna: int):
        super().__init__(linea, columna);
        self.id = id;
        self.parametros = parametros;
        self.retorno_fn = retorno_fn;
        self.bloque = bloque;

    def ejecutar(self, console: Console, scope: Scope):
        if (isinstance(self.retorno_fn, Dimension)):
            scope.guardarFuncion(self.id, self, self.retorno_fn.tipo, self.linea, self.columna);
        else:
            scope.guardarFuncion(self.id, self, self.retorno_fn, self.linea, self.columna);
        # si es el main se ejecuta de una vez
        if (self.id == 'main'):
            _main = self.bloque.ejecutar(console, scope);
            if (_main != None):
                # ERROR. no se esperaba una sentencia de control de tipo _main.retorno
                pass;

    def tipoArgumentos(self, argTipo, i:int, console:Console, scope:Scope):
        if (isinstance(self.parametros[i], Arreglo)):
            if (argTipo != self.devolverTipo(self.parametros[i].dimension.tipo)):
                print("ERROR. Tipos incompatibles. se esperaba un str(paramTipo) y se encontró un str(argTipo)")
                # ERROR. Tipos incompatibles. se esperaba un str(paramTipo) y se encontró un str(argTipo) 
                pass;
        else:
            if (argTipo != self.devolverTipo(self.parametros[i].tipo)):
                print("ERROR. Tipos incompatibles. se esperaba un str(paramTipo) y se encontró un str(argTipo)")
                # ERROR. Tipos incompatibles. se esperaba un str(paramTipo) y se encontró un str(argTipo) 
                pass;

    def tipoRetorno(self, returnTipo):
        if (self.retorno_fn == None):
            # ERROR. No se puede retornar una expresión en un método.
            return;
        if (isinstance(self.retorno_fn, Dimension)):
            tipo = self.devolverTipo(self.retorno_fn.tipo);
            if (returnTipo == None):
                print("ERROR. Se esperaba que se retornara str(tipo) y no se devolvió nada.")
                # ERROR. Se esperaba que se retornara str(tipo) y no se devolvió nada.
                pass;
            if (returnTipo != tipo):
                print("ERROR. Tipos incompatibles. se esperaba un str(paramTipo) y se encontró un str(argTipo) ")
                # ERROR. Tipos incompatibles. se esperaba un str(paramTipo) y se encontró un str(argTipo) 
                pass;
        else:
            tipo = self.devolverTipo(self.retorno_fn);
            if (returnTipo == None):
                # ERROR. Se esperaba que se retornara str(tipo) y no se devolvió nada.
                pass;
            if (returnTipo != tipo):
                # ERROR. Tipos incompatibles. se esperaba un str(paramTipo) y se encontró un str(argTipo) 
                pass;

    def devolverTipo(self, tipo:str):
        if (tipo == 'i64'):
            return TipoDato.INT64;
        elif (tipo == 'f64'):
            return TipoDato.FLOAT64;
        elif (tipo == 'char'):
            return TipoDato.CHAR;
        elif (tipo == 'str'):
            return TipoDato.STR;
        elif (tipo == 'String'):
            return TipoDato.STRING;