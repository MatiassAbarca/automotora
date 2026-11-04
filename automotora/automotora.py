# Developer: Matias Alejandro Abarca Gatica
# Curso: Programación Backend
# Evaluación Sumativa N°1 - Sistema de Gestión de una Automotora
# archivo automotora


class Automotora:
    def __init__(self, nombre):
        self.nombre = nombre                # String
        self.vehiculos = []                 # list<Vehiculo>

    def agregarVehiculo(self, vehiculo):
        self.vehiculos.append(vehiculo)

    def mostrarVehiculos(self):
        print(f"--- Vehículos de {self.nombre} ({len(self.vehiculos)} registrados) ---")
        for vehiculo in self.vehiculos:
            vehiculo.mostrarInfo()
