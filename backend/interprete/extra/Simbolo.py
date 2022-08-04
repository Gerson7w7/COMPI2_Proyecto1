from .Tipos import TipoDato

class Simbolo:
    def __init__(self, valor, id: str, tipo: TipoDato, mut:bool):
        self.valor = valor;
        self.id = id;
        self.tipo = tipo;
        self.mut = mut;