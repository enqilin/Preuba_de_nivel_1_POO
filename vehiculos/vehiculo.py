import csv
import config

class Vehiculo():
    def __init__(self,bastiodr,color,ruedas):
        self.color=color
        self.ruedas=ruedas
        self.bastiodr=bastiodr

    def __str__(self):
        return "{} ruedas, color {} ".format(self.ruedas,self.color)
    def to_dict():
        return {'color':self.color,'reudas':self.ruedas}


class Vehiculos():
    vehiculo=[]
    with open(config.DATABASE_PATH, newline="\n") as fichero:
        reader= csv.reader(fichero,delimiter=";")
        for bastidor,ruedas,color in reader:
            vehiculos=Vehiculo(bastidor,ruedas,color)
            vehiculo.append(vehiculos)
    
    @staticmethod
    def buscar(bastidor):
        for vehiculos in Vehiculos.vehiculo:
            if vehiculos.bastidor==bastidor:
                return vehiculos
    
    @staticmethod
    def crear(bastidor,ruedas, color):
        vehiculos=  Vehiculo(bastidor,ruedas,color)
        Vehiculos.vehiculo.append(vehiculos)
        Vehiculos.guardar()
        return vehiculos
    
    @staticmethod
    def modificar(bastidor,ruedas,color):
        for indice,vehiculos in enumerate(Vehiculos.vehiculo):
            if vehiculos.bastidor==bastidor:
                Vehiculos.vehiculos[indice].ruedas=ruedas
                Vehiculos.vehiculos[indice].color=color
                Vehiculos.guardar()
                return vehiculos

    @staticmethod
    def borrar(bastidor):
        for indice,vehiculos in enumerate(Vehiculos.vehiculo):
            if vehiculos.bastidor==bastidor:
                vehiculos=Vehiculos.vehiculo.pop(indice)

    @staticmethod
    def guardar():
        with open(config.DATABASE_PATH,'w',newline='\n') as fichero:
            writer=csv.writer(fichero,delimiter=';')
            for vehiculos in Vehiculos.vehiculo:
                writer.writerow((vehiculos.bastidor,vehiculos.ruedas,vehiculos.color))

    @staticmethod
    def buscar_por_otros_caracteres(*args):
        for vehiculos in Vehiculos.vehiculo :
            if vehiculos.args==args:
                return vehiculos

