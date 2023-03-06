import coche

class Camion(coche):

    def __init__(self, bastidor, color,ruedas,velocidad,cilindrada,carga ):
        super().__init__(bastidor,color,ruedas,velocidad,cilindrada)
        self.carga=carga

    def __str__(self):
        return super().__str__(self)+ ", {} kg ".format(self.carga)
