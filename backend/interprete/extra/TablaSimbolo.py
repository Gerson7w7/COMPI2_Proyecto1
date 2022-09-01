class TablaSimbolo:
    def __init__(self, identificador:str, tipo:str, tipoDato:str, ambito:str, linea:int, columna:int):
        self.identificador = identificador;
        self.tipo = tipo;
        self.tipoDato = tipoDato;
        self.ambito = ambito;
        self.linea = linea;
        self.columna = columna;

    def serializar(self):
        return {
            'identificador': self.identificador,
            'tipo': self.tipo,
            'tipoDato': self.tipoDato,
            'ambito': self.ambito,
            'linea': self.linea,
            'columna': self.columna,
        }