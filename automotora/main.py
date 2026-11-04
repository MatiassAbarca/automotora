# Developer: Matias Alejandro Abarca Gatica
# Curso: Programación Backend
# Evaluación Sumativa N°1 - Sistema de Gestión de una Automotora
# archivo main

from automotora import Automotora
from auto import Auto
from motocicleta import Motocicleta
from vendedor import Vendedor


def main():
    AÑO_ACTUAL = 2026

    # 1. Instanciar un objeto Automotora
    automotora = Automotora("Automotora Puente Alto")

    # 2. Crear dos automóviles
    auto_uno = Auto("ABCD12", "Toyota", "Yaris", 2018, 7500000, 5, "Bencina")
    auto_dos = Auto("EFGH34", "Hyundai", "Accent", 2021, 9800000, 4, "Bencina")

    # 3. Crear una motocicleta
    moto_uno = Motocicleta("MN123", "Yamaha", "MT-07", 2020, 6200000, 689, "Bencina")

    # 4. Agregar los vehículos a la automotora
    automotora.agregarVehiculo(auto_uno)
    automotora.agregarVehiculo(auto_dos)
    automotora.agregarVehiculo(moto_uno)

    # 5. Mostrar los vehículos registrados
    automotora.mostrarVehiculos()

    # 6. Probar los métodos del automóvil
    print("\n --- AUTO ---")
    auto_uno.abrirMaletero()
    print("¿Tiene aire acondicionado?", auto_uno.tieneAireAcondicionado())

    # 7. Calcular y mostrar años de uso del automóvil
    print(f"Años de uso del {auto_uno.marca} {auto_uno.modelo}: "
          f"{auto_uno.calcularAñosUso(AÑO_ACTUAL)} años")

    # 8. Probar los métodos de la motocicleta
    print("\n --- MOTOCICLETA ---")
    moto_uno.encenderMotor()
    print("¿Es de alta cilindrada?", moto_uno.esDeAltaCilindrada())

    # 9. Calcular y mostrar años de uso de la motocicleta
    print(f"Años de uso de la {moto_uno.marca} {moto_uno.modelo}: "
          f"{moto_uno.calcularAñosUso(AÑO_ACTUAL)} años")

    # 10. Crear un vendedor
    vendedor_uno = Vendedor("Pedro González", "12.345.678-9", "+56 9 1234 5678")

    # 11. Mostrar los datos del vendedor
    print("\n --- VENDEDOR ---")
    vendedor_uno.mostrarDatos()

    # 12 y 13. Calcular y mostrar comisiones
    venta_alta = auto_dos.precio     # >= 5.000.000 -> 10%
    venta_baja = 3000000             # < 5.000.000  -> 5%
    print(f"Comisión por venta de ${venta_alta:,.0f}: ${vendedor_uno.calcularComision(venta_alta):,.0f}")
    print(f"Comisión por venta de ${venta_baja:,.0f}: ${vendedor_uno.calcularComision(venta_baja):,.0f}")


# 14. main() como estructura principal
if __name__ == "__main__":
    main()
