import coche

class formul(coche):
    
    def __init__(self,bastidor,ruedas, color, velocidad, cilindrada,nombre_equipo):
        super().__init__(bastidor,ruedas, color, velocidad, cilindrada)
        self.nombre_equipo=nombre_equipo

    def __str__(self):
        return super().__str__(self) + ", {}".format(self.nombre_equipo)