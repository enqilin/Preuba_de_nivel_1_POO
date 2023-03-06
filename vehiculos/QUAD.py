import bicicleta
import coche

class quad(*args):
    if args==coche:
        def __init__(self,bastidor,ruedas, color, velocidad, cilindrada,modelo):
            super().__init__(bastidor,ruedas, color, velocidad, cilindrada,)
            self.modelo=modelo
        
        def __str__(self) -> str:
            return super().__str__(self) + ", {} ".format(self.modelo)
        
    elif args==bicicleta:
        def __init__(self,bastidor,ruedas, color, tipo,modelo):
            super().__init__(bastidor,ruedas, color, tipo)
            self.modelo=modelo
        
        def __str__(self) -> str:
            return super().__str__(self) + ", {} ".format(self.modelo)
    
