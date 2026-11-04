# Developer: Matias Alejandro Abarca Gatica
# Curso: Programación Backend
# Evaluación Sumativa N°1 - Sistema de Gestión de una Automotora
# archivo vendedor


class Vendedor:
    def __init__(self, nombre, rut, telefono):
        self.nombre = nombre                # String
        self.rut = rut                      # String
        self.telefono = telefono            # String

    def mostrarDatos(self):
        print(f"Vendedor: {self.nombre} | RUT: {self.rut} | Teléfono: {self.telefono}")

    def calcularComision(self, montoVenta):
        # RN03: venta >= $5.000.000 -> 10%; venta menor -> 5%
        if montoVenta >= 5000000:
            return montoVenta * 0.10
        else:
            return montoVenta * 0.05
