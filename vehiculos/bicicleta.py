import vehiculo as db
import csv

class Bicicleta(db.Vehiculo):
    def __init__(self, bastidor ,ruedas, color,tipo):
        super().__init__(bastidor,ruedas, color)
        self.tipo=tipo

    def __str__(self):
        return db.Vehiculo.__str__(self) + ", El bicicleta es de tipo {}".format(self.tipo)
