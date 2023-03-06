import bicicleta


class Motocicleta(bicicleta):
    
    def __init__(self,bastidor,color, ruedas,tipo,velocidad,cilindrada):
        super().__init__(bastidor,color, ruedas, tipo)
        self.velocidad=velocidad
        self.cilindrada=cilindrada

    def __str__(self):
       return super().__str__(self) + ", + {} km/h, {} cc".format(self.velocidad,self.cilindrada)