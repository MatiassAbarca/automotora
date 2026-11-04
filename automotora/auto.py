# Developer: Matias Alejandro Abarca Gatica
# Curso: Programación Backend
# Evaluación Sumativa N°1 - Sistema de Gestión de una Automotora
# archivo auto

from vehiculo import Vehiculo


class Auto(Vehiculo):
    def __init__(self, patente, marca, modelo, año, precio, numPuertas, combustible):
        super().__init__(patente, marca, modelo, año, precio)
        self.numPuertas = numPuertas        # int
        self.combustible = combustible      # String

    def mostrarInfo(self):
        super().mostrarInfo()
        print(f"   Tipo: Auto | Puertas: {self.numPuertas} | "
              f"Combustible: {self.combustible}")

    def abrirMaletero(self):
        print(f"Abriendo el maletero del {self.marca} {self.modelo}...")

    def tieneAireAcondicionado(self):
        # Se asume que los autos de la automotora incluyen aire acondicionado
        return True
