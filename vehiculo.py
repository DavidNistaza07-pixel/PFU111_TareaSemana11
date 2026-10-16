
"""
PFU-111 Programación Fundamental - Semana 11
Proyecto grupal: Sistema de gestión de transporte universitario
Módulo: vehiculo.py
Estudiante: Apaza Nistaza David Abraham (Integrante 1)

Contiene la clase base Vehiculo, de la que heredan Trufi, Minibus y Radiotaxi.
"""

from abc import ABC, abstractmethod


class Vehiculo(ABC):
    """Clase base (abstracta) para todos los vehículos de la universidad.

    Atributos comunes (encapsulados):
        - codigo       : identificador único del vehículo
        - marca        : marca del vehículo
        - capacidad    : cantidad de pasajeros (no puede ser negativa)
        - kilometraje  : kilómetros recorridos (no puede ser negativo)

    Método abstracto:
        - calcular_costo_operativo(): cada clase derivada implementa su fórmula.
    """

    def __init__(self, codigo, marca, capacidad, kilometraje):
        self._codigo = codigo
        self._marca = marca
        # Se asignan a través de los setters para aplicar la validación
        self.capacidad = capacidad
        self.kilometraje = kilometraje

    # ------------------------------------------------------------------
    # Encapsulamiento: acceso controlado a los atributos
    # ------------------------------------------------------------------
    @property
    def codigo(self):
        return self._codigo

    @property
    def marca(self):
        return self._marca

    @property
    def capacidad(self):
        return self._capacidad

    @capacidad.setter
    def capacidad(self, valor):
        if not isinstance(valor, (int, float)) or valor < 0:
            raise ValueError("La capacidad debe ser un número mayor o igual a 0")
        self._capacidad = int(valor)

    @property
    def kilometraje(self):
        return self._kilometraje

    @kilometraje.setter
    def kilometraje(self, valor):
        if not isinstance(valor, (int, float)) or valor < 0:
            raise ValueError("El kilometraje debe ser un número mayor o igual a 0")
        self._kilometraje = float(valor)

    # ------------------------------------------------------------------
    # Comportamiento común: lo heredan todas las clases derivadas
    # ------------------------------------------------------------------
    def tipo(self):
        """Devuelve el nombre del tipo de vehículo (nombre de la clase)."""
        return self.__class__.__name__

    def mostrar_informacion(self):
        """Devuelve la información general del vehículo como texto."""
        return (
            f"[{self.tipo()}] Código: {self._codigo} | Marca: {self._marca} | "
            f"Capacidad: {self._capacidad} pasajeros | "
            f"Kilometraje: {self._kilometraje:.1f} km"
        )

    def __str__(self):
        return self.mostrar_informacion()

    # ------------------------------------------------------------------
    # Comportamiento específico: polimorfismo
    # ------------------------------------------------------------------
    @abstractmethod
    def calcular_costo_operativo(self):
        """Calcula el costo operativo del vehículo.

        Es abstracto: cada clase derivada (Trufi, Minibus, Radiotaxi) debe
        implementarlo con su propia regla de cálculo.
        """
        pass


# ----------------------------------------------------------------------
# Prueba rápida de la clase base (se ejecuta solo con: python vehiculo.py)
# ----------------------------------------------------------------------
if __name__ == "__main__":

    class VehiculoPrueba(Vehiculo):
        """Clase mínima solo para probar la base de forma aislada."""

        def calcular_costo_operativo(self):
            return 0.0

    v = VehiculoPrueba("V001", "Toyota", 20, 1500)
    print(v.mostrar_informacion())

    try:
        v.kilometraje = -5
    except ValueError as error:
        print("Validación correcta ->", error)

    try:
        Vehiculo("V002", "Nissan", 10, 100)
    except TypeError:
        print("Validación correcta -> Vehiculo es abstracta y no se puede instanciar")
