from .Tipos import TipoDato, TipoTransferencia

class RetornoExpresion:
    def __init__(self, valor, tipo: TipoDato, retorno:TipoTransferencia):
        self.valor = valor;
        self.tipo = tipo;
        self.retorno = retorno;