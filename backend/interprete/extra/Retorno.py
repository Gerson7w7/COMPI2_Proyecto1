from .Tipos import TipoDato

class RetornoExpresion:
    def __init__(self, valor, tipo: TipoDato):
        self.valor = valor;
        self.tipo = tipo;