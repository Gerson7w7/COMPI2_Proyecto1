# clase para manejar los entornos, ambitos, env o scopes
import this


class Scope:
    def __init__(self, padre: Scope):
        self.padre = padre;
        self.simbolos = [];
        self.variables = {};
        self.funciones = {};
    
    def crearVariable(id: str, valor, type: Tipo, linea: int, columna: int):
        scope: Scope = this;

        while(scope != None):
            # verificamos que no se haya declarado antes la misma variable
            if(scope.variables.get(id)):
                pass;
                # la variable ya ha sido declarada
            scope = scope.padre;
        # procedemos a crear la variable
        if (valor == None):
            # si no se inicializa;
            pass
        else:
            
