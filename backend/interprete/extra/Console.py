# clase para manejar la salida del código
class Console:
    def __init__(self):
        self.output = "";

    def append(self, text):
        self.output += text; 