class TablaSimbolo:
    def __init__(self, identificador:str, tipo:str, tipoDato:str, entorno:str, linea:int, columna:int):
        self.identificador = identificador;
        self.tipo = tipo;
        self.tipoDato = tipoDato;
        self.entorno = entorno;
        self.linea = linea;
        self.columna = columna;