import vehiculo as db
import csv

class Coche(db.Vehiculo):
    def __init__(self, bastiodr, color, ruedas , velocidad, cilindrada):
        super().__init__(bastiodr, color, ruedas)
        self.velocidad=velocidad
        self.cilindrada=cilindrada

    def __str__(self):
        return db.Vehiculo.__str__(self) + ", {} km/h, {} cc ".format(self.velocidad,self.cilindrada)