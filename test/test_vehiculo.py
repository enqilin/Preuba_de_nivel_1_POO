import unittest
import csv
import copy
import helpers
import vehiculo as db

class TestVehiculos(unittest.TestCase):

    def setUp(self):
        db.Vehiculos.vehiculo=[ 
        db.Vehiculos('12J','2','Rojo'),
        db.Vehiculos('43J','4','Azul'),
        db.Vehiculos('76E','4','Verde')
        ]

def test_buscar_vehiculo(self):
    vehiculo_exitente=db.Vehiculos.buscar('12J')
    vehiculo_inexitente=db.Vehiculo.buscar('82Q')
    self.assertNotNone(vehiculo_exitente)
    self.assertIsNone(vehiculo_inexitente)

def test_crear_vehiculo(self):
    nuevo_vehiculo=db.Vehiculos.crear('24M','2','Naranja')
    self.assertEqual(len(db.Vehiculos.vehiculo),4)
    self.assertEqual(nuevo_vehiculo.bastidor,'24M')
    self.assertEqual(nuevo_vehiculo.ruedas, '2')
    self.assertEqual(nuevo_vehiculo.color, 'Naranja')

def test_modificar_vehiculo(self):
    vehiculo_a_modificar=copy.copy(db.Vehiculos.buscar('76E'))
    vehiculo_mofdificado=db.Vehiculos.modificar('76E')
    self.assertEqual(vehiculo_a_modificar.ruedas, '2')
    self.assertEqual(vehiculo_a_modificar.color,'Azul marino')

def test_borrar_vehiculo(self):
    vehiculo_a_borrar=db.Vehiculos.borrar('43J')
    vehiculo_rebuscado=db.Vehiculos.buscar('43J')
    self.assertEqual(vehiculo_a_borrar.bastidor,'43J')
    self.assertIsNone(vehiculo_rebuscado)

def tes


