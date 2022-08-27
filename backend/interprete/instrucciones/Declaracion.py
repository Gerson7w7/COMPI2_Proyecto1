from ..extra.Tipos import TipoDato
from .Instruccion import Instruccion
from ..extra.Console import Console
from ..extra.Scope import Scope
from ..extra.Retorno import RetornoExpresion

class Declaracion(Instruccion):
    def __init__(self, mut:bool, id: str, tipo: str, valor, linea: int, columna: int):
        super().__init__(linea, columna)
        self.mut = mut; 
        self.id = id;
        self.tipo = tipo;
        self.valor = valor;

    def ejecutar(self, console: Console, scope: Scope):
        # analizando el tipo de dato
        _tipo: TipoDato = None;
        if (self.tipo != None):
            if (self.tipo == 'i64'):
                _tipo = TipoDato.INT64
            elif (self.tipo == 'f64'):
                _tipo = TipoDato.FLOAT64
            elif (self.tipo == 'bool'):
                _tipo = TipoDato.BOOLEAN
            elif (self.tipo == 'char'):
                _tipo = TipoDato.CHAR
            elif (self.tipo == 'String'):
                _tipo = TipoDato.STRING
            elif (self.tipo == 'str'):
                _tipo = TipoDato.STR

        # variables inicializadas
        if (self.valor != None):
            # obteniendo el valor de la expresion
            val = self.valor.ejecutar(console, scope);
        # variables no inicializadas
        else:
            val = self.valorDefault(_tipo);

        _tipo = val.tipo if (_tipo == None) else _tipo;
        print("============= " + str(self.id) + "============")
        print("_tipo:" + str(_tipo));
        print("_tipo2:" + str(val.tipo));
        # asegurandonos de que sea el mismo tipo de dato para crear la variable
        if (val.tipo != _tipo):
            # error, diferentes tipos de datos
            print("error::: " + self.id)
            pass;
        scope.crearVariable(self.id, val.valor, val.tipo, self.mut, None, None, None, self.linea, self.columna);
    
    def valorDefault(_tipo:TipoDato):
        if (_tipo == TipoDato.INT64):
            return RetornoExpresion(0, TipoDato.INT64, None);
        elif (_tipo == TipoDato.FLOAT64):
            return RetornoExpresion(0.0, TipoDato.FLOAT64, None);
        elif (_tipo == TipoDato.BOOLEAN):
            return RetornoExpresion(False, TipoDato.BOOLEAN, None);
        elif (_tipo == TipoDato.CHAR):
            return RetornoExpresion('\0', TipoDato.CHAR, None);
        elif (_tipo == TipoDato.STRING):
            return RetornoExpresion('', TipoDato.STRING, None);
        elif (_tipo == TipoDato.STR):
            return RetornoExpresion('', TipoDato.STR, None);

class Asignacion(Instruccion):
    def __init__(self, id:str, expresion, linea: int, columna: int):
        super().__init__(linea, columna)
        self.id = id;
        self.expresion = expresion;

    def ejecutar(self, console: Console, scope: Scope):
        val = self.expresion.ejecutar(console, scope);
        scope.setValor(self.id, val, self.linea, self.columna);