# Developer: Matias Alejandro Abarca Gatica
# Curso: Programación Backend
# Evaluación Sumativa N°1 - Sistema de Gestión de una Automotora
# archivo motocicleta

from vehiculo import Vehiculo


class Motocicleta(Vehiculo):
    def __init__(self, patente, marca, modelo, año, precio, cilindrada, tipo):
        super().__init__(patente, marca, modelo, año, precio)
        self.cilindrada = cilindrada        # int (cc)
        self.tipo = tipo                    # String

    def mostrarInfo(self):
        super().mostrarInfo()
        print(f"   Tipo: Motocicleta | Cilindrada: {self.cilindrada} cc | "
              f"Categoría: {self.tipo}")

    def encenderMotor(self):
        print(f"Encendiendo el motor de la {self.marca} {self.modelo}...")

    def esDeAltaCilindrada(self):
        # RN02: alta cilindrada cuando cilindrada >= 600 cc
        if self.cilindrada >= 600:
            return True
        return False
