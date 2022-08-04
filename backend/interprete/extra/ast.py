from .Console import Console
from .Scope import Scope

# clase con la que se formará el ast final
class Ast:
    def __init__(self, instrucciones):
        self.instrucciones: list = instrucciones;

    def ejecutar(self, console: Console, scope: Scope):
        for instruccion in self.instrucciones:
            if (instruccion != None): # QUITAAAAAAAAAAAAAAAAAAAAR!!!! SOLO ES PARA PROBAR LA GRMAÁTICA !!!! QUITARRR !!!
                instruccion.ejecutar(console, scope)