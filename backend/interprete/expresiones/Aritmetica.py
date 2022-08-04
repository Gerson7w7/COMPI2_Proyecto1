from ..extra.Retorno import RetornoExpresion
from ..extra.Tipos import TipoAritmetica, TipoDato
from .Expresion import Expresion
from ..extra.Console import Console
from ..extra.Scope import Scope

class Aritmetica(Expresion):
    def __init__(self, izquierda, derecha, tipo: TipoAritmetica, linea: int, columna: int):
        super().__init__(linea, columna)
        self.izquierda = izquierda;
        self.derecha = derecha;
        self.tipo = tipo;

    def ejecutar(self, console: Console, scope: Scope):
        # valor y tipo de la izquierda
        valIzquierda = self.izquierda.ejecutar(console, scope);
        # valor y tipo de la derecha
        valDerecha = self.derecha.ejecutar(console, scope);

        # verificando que sea del mismo tipo de dato
        if ((valIzquierda.tipo == valDerecha.tipo) or (valIzquierda.tipo == TipoDato.STRING and valIzquierda.tipo == TipoDato.STR)):
            # si es una suma
            if (self.tipo == TipoAritmetica.SUMA):  
                if (valIzquierda.tipo == TipoDato.INT64 or valIzquierda.tipo == TipoDato.FLOAT64 or valIzquierda.tipo == TipoDato.STRING):
                    # se hace la operacion correspondiente y se pasa el tipo
                    print("suma : " + str(valIzquierda.valor + valDerecha.valor))
                    return RetornoExpresion((valIzquierda.valor + valDerecha.valor), valIzquierda.tipo);
                # error no se puede operar izq con der
            elif (self.tipo == TipoAritmetica.RESTA):
                if (valIzquierda.tipo == TipoDato.INT64 or valIzquierda.tipo == TipoDato.FLOAT64):
                    # se hace la operacion correspondiente y se pasa el tipo
                    print("resta : " + str(valIzquierda.valor - valDerecha.valor))
                    return RetornoExpresion((valIzquierda.valor - valDerecha.valor), valIzquierda.tipo);
                # error no se puede operar izq con der
            elif (self.tipo == TipoAritmetica.MULTIPLICACION):
                if (valIzquierda.tipo == TipoDato.INT64 or valIzquierda.tipo == TipoDato.FLOAT64):
                    # se hace la operacion correspondiente y se pasa el tipo
                    print("mult : " + str(valIzquierda.valor * valDerecha.valor))
                    return RetornoExpresion((valIzquierda.valor * valDerecha.valor), valIzquierda.tipo);
                # error no se puede operar izq con der
            elif (self.tipo == TipoAritmetica.DIVISION):
                if (valIzquierda.tipo == TipoDato.INT64 or valIzquierda.tipo == TipoDato.FLOAT64):
                    # se hace la operacion correspondiente y se pasa el tipo
                    print("div : " + str(valIzquierda.valor / valDerecha.valor))
                    return RetornoExpresion((valIzquierda.valor / valDerecha.valor), TipoDato.FLOAT64);
                # error no se puede operar izq con der
            elif (self.tipo == TipoAritmetica.POTENCIA):
                if (valIzquierda.tipo == TipoDato.INT64 or valIzquierda.tipo == TipoDato.FLOAT64):
                    # se hace la operacion correspondiente y se pasa el tipo
                    print("pow : " + str(pow(valIzquierda.valor, valDerecha.valor)))
                    return RetornoExpresion(pow(valIzquierda.valor, valDerecha.valor), valIzquierda.tipo);
                # error no se puede operar izq con der
            elif (self.tipo == TipoAritmetica.MODULO):
                if (valIzquierda.tipo == TipoDato.INT64 or valIzquierda.tipo == TipoDato.FLOAT64):
                    # se hace la operacion correspondiente y se pasa el tipo
                    print("mod : " + str(valIzquierda.valor % valDerecha.valor))
                    return RetornoExpresion((valIzquierda.valor % valDerecha.valor), valIzquierda.tipo);
                # error no se puede operar izq con der
        #error, tipos diferentes