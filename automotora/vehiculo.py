# Developer: Matias Alejandro Abarca Gatica
# Curso: Programación Backend
# Evaluación Sumativa N°1 - Sistema de Gestión de una Automotora
# archivo vehiculo (clase base)


class Vehiculo:
    """Clase base: características generales de un vehículo."""

    def __init__(self, patente, marca, modelo, año, precio):
        self.patente = patente      # String
        self.marca = marca          # String
        self.modelo = modelo        # String
        self.año = año              # int
        self.precio = precio        # double

    def mostrarInfo(self):
        print(f"Patente: {self.patente} | Marca: {self.marca} | "
              f"Modelo: {self.modelo} | Año: {self.año} | "
              f"Precio: ${self.precio:,.0f}")

    def calcularAñosUso(self, añoActual):
        # RN01: años de uso = añoActual - año de fabricación (retorna int)
        return int(añoActual - self.año)
