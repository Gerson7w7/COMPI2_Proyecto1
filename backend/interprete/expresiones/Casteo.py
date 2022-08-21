from ..extra.Tipos import TipoDato
from .Expresion import Expresion
from ..extra.Scope import Scope
from ..extra.Console import Console
from ..extra.Retorno import RetornoExpresion

class Casteo(Expresion):
    def __init__(self, expresion, tipo:str, linea, columna):
        super().__init__(linea, columna);
        self.expresion = expresion;
        self.tipo = tipo;

    def ejecutar(self, console: Console, scope: Scope):
        # recuperamos la expresion
        val = self.expresion.ejecutar(console, scope);
        if (self.tipo == 'i64'):
            print("int: " +str(int(val.valor)))
            return RetornoExpresion(int(val.valor), TipoDato.INT64, None);
        elif (self.tipo == 'f64'):
            print("float: " +str(float(val.valor)))
            return RetornoExpresion(float(val.valor), TipoDato.FLOAT64, None);
        elif (self.tipo == 'bool'):
            try:
                return RetornoExpresion(bool(val.valor), TipoDato.BOOLEAN, None);   
            except:
                # ERROR. no se puede convertir en bool
                pass; 
        elif (self.tipo == 'char'):
            if (len(val.valor) == 1):
                return RetornoExpresion(str(val.valor), TipoDato.CHAR, None);
            # ERROR. no se puede convertir en char
        elif (self.tipo == 'string'):
            return RetornoExpresion(str(val.valor), TipoDato.STRING, None);
        elif (self.tipo == 'str'):
            return RetornoExpresion(str(val.valor), TipoDato.STR, None);