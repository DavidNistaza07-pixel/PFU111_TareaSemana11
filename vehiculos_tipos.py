from vehiculo import Vehiculo

# ==============================================
# CLASE 1: TRUFI
# ==============================================
class Trufi(Vehiculo):
    def __init__(self, codigo, marca, capacidad, kilometraje, costo_por_km, numero_rutas):
        # Reutilizamos el constructor de la clase padre
        super().__init__(codigo, marca, capacidad, kilometraje)
        # Atributos propios de Trufi
        if costo_por_km <= 0:
            raise ValueError("El costo por kilómetro debe ser mayor a 0")
        self._costo_por_km = costo_por_km
        self._numero_rutas = numero_rutas

    @property
    def costo_por_km(self):
        return self._costo_por_km

    @property
    def numero_rutas(self):
        return self._numero_rutas

    # Implementación OBLIGATORIA del método abstracto → POLIMORFISMO
    def calcular_costo_operativo(self):
        return self.kilometraje * self._costo_por_km * (1 + self._numero_rutas / 10)

    # Sobreescribimos para agregar datos propios
    def mostrar_informacion(self):
        return (
            f"[{self.tipo()}] Código: {self.codigo} | Marca: {self.marca} | "
            f"Capacidad: {self.capacidad} pasajeros | "
            f"Kilometraje: {self.kilometraje:.1f} km | "
            f"Costo/km: ${self._costo_por_km:.2f} | Rutas: {self._numero_rutas}"
        )


# ==============================================
# CLASE 2: MINIBÚS
# ==============================================
class Minibus(Vehiculo):
    def __init__(self, codigo, marca, capacidad, kilometraje, costo_por_km, numero_viajes):
        super().__init__(codigo, marca, capacidad, kilometraje)
        if costo_por_km <= 0:
            raise ValueError("El costo por kilómetro debe ser mayor a 0")
        self._costo_por_km = costo_por_km
        self._numero_viajes = numero_viajes

    @property
    def costo_por_km(self):
        return self._costo_por_km

    @property
    def numero_viajes(self):
        return self._numero_viajes

    def calcular_costo_operativo(self):
        return self.kilometraje * self._costo_por_km * (1 + self._numero_viajes / 8)

    def mostrar_informacion(self):
        return (
            f"[{self.tipo()}] Código: {self.codigo} | Marca: {self.marca} | "
            f"Capacidad: {self.capacidad} pasajeros | "
            f"Kilometraje: {self.kilometraje:.1f} km | "
            f"Costo/km: ${self._costo_por_km:.2f} | Viajes: {self._numero_viajes}"
        )


# ==============================================
# CLASE 3: RADIOTAXI
# ==============================================
class Radiotaxi(Vehiculo):
    def __init__(self, codigo, marca, capacidad, kilometraje, costo_por_km, area_asignada):
        super().__init__(codigo, marca, capacidad, kilometraje)
        if costo_por_km <= 0:
            raise ValueError("El costo por kilómetro debe ser mayor a 0")
        self._costo_por_km = costo_por_km
        self._area_asignada = area_asignada

    @property
    def costo_por_km(self):
        return self._costo_por_km

    @property
    def area_asignada(self):
        return self._area_asignada

    def calcular_costo_operativo(self):
        factor = 1.2 if "Centro" in self._area_asignada else 1.0
        return self.kilometraje * self._costo_por_km * factor

    def mostrar_informacion(self):
        return (
            f"[{self.tipo()}] Código: {self.codigo} | Marca: {self.marca} | "
            f"Capacidad: {self.capacidad} pasajeros | "
            f"Kilometraje: {self.kilometraje:.1f} km | "
            f"Costo/km: ${self._costo_por_km:.2f} | Área: {self._area_asignada}"
        )