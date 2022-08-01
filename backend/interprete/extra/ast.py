from .Console import Console

# clase con la que se formará el ast final
class Ast:
    def __init__(self, instrucciones):
        self.instrucciones: list = instrucciones;

    def ejecutar(self, console: Console, scope: Scope):
        for instruccion in self.instrucciones:
            instruccion.ejecutar(console, scope)