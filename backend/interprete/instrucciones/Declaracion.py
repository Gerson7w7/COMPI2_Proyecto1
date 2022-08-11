from ..extra.Tipos import TipoDato
from .Instruccion import Instruccion
from ..extra.Console import Console
from ..extra.Scope import Scope

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
            elif (self.tipo == 'string'):
                _tipo = TipoDato.STRING
            elif (self.tipo == 'str'):
                _tipo = TipoDato.STR

        # variables inicializadas
        if (self.valor != None):
            # obteniendo el valor de la expresion
            val = self.valor.ejecutar(console, scope);
            _tipo = val.tipo if (_tipo == None) else _tipo;
            # asegurandonos de que si es un &str se cambie de string str
            if (_tipo == TipoDato.STR and val.tipo == TipoDato.STRING):
                val.tipo = _tipo;
            if (val.tipo == _tipo):
                scope.crearVariable(self.id, val.valor, val.tipo, self.mut, self.linea, self.columna);
            else:
                # error, diferentes tipos de datos
                print("error " + self.id)
                pass;
        # variables no inicializadas
        else:
            pass;

class Asignacion(Instruccion):
    def __init__(self, id:str, expresion, linea: int, columna: int):
        super().__init__(linea, columna)
        self.id = id;
        self.expresion = expresion;

    def ejecutar(self, console: Console, scope: Scope):
        val = self.expresion.ejecutar(console, scope);
        scope.setValor(self.id, val, self.linea, self.columna);