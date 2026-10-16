Sistema de gestión de transporte universitario

Proyecto grupal de PFU-111 Programación Fundamental (Semana 11, Tema 7: Programación Orientada a Objetos). Programa de consola en Python que registra los vehículos que usa una universidad (trufis, minibuses y radiotaxis) y calcula su costo operativo aplicando herencia y polimorfismo.

Integrantes (Grupo 1)
Integrante	                                                              Responsabilidad
Apaza Nistaza David Abraham	                                              Diseño del diagrama de clase base Vehículod
Medinaceli Andrade Fernando Yeray                                         Diseño de clase minibus, radiotaxi, trufi; integración y pruebas
Magueño Cano Bwnajamin Mateo                                              Desarrollo del informe 


____________________________	Implementación de Trufi, Minibus y Radiotaxi (vehiculos_tipos.py) y menú (menu.py)

Docente: Ing. Rubén Gonzalo Soria Soria · Fecha de entrega: 16/10/2026

Descripción del proyecto

La universidad cuenta con distintos tipos de transporte que comparten información general (código, marca, capacidad y kilometraje), pero cada tipo tiene atributos propios y una forma específica de calcular su costo operativo. El programa modela esta situación con:

Una clase base abstracta Vehiculo que concentra los atributos comunes, los encapsula con propiedades que validan los datos y declara el método abstracto calcular_costo_operativo().
Tres clases derivadas (Trufi, Minibus, Radiotaxi) que heredan de Vehiculo, agregan sus atributos propios e implementan su propia fórmula de costo.
Un menú de consola que guarda todos los vehículos en una sola lista de tipo Vehiculo y, al calcular los costos, invoca el mismo método sobre cada objeto sin preguntar de qué clase es (polimorfismo).

Estructura del repositorio
PFU111_TareaSemana11/
├── vehiculo.py           # Clase base abstracta Vehiculo
├── vehiculos_tipos.py    # Clases derivadas: Trufi, Minibus, Radiotaxi
├── menu.py               # Programa principal (menú de consola)
├── Diagrama_clases.jpeg  # Diagrama UML de clases
└── README.md
Requisitos
Python 3.10 o superior (probado con Python 3.14).
No requiere librerías externas; solo usa el módulo estándar abc.
Instrucciones de ejecución
Clonar el repositorio:
   git clone https://github.com/DavidNistaza07-pixel/PFU111_TareaSemana11.git
   cd PFU111_TareaSemana11
Ejecutar el programa principal:
   python menu.py
Para probar únicamente la clase base de forma aislada:
   python vehiculo.py
Uso del menú
1. Registrar Trufi
2. Registrar Minibús
3. Registrar Radiotaxi
4. Mostrar todos los vehículos
5. Calcular costo operativo individual
6. Calcular costo operativo TOTAL
7. Salir

Al registrar un vehículo se piden los datos comunes (código, marca, capacidad, kilometraje recorrido y costo por km) y el dato propio de cada tipo: número de rutas (trufi), número de viajes (minibús) o área asignada (radiotaxi).

Clases y atributos
Clase	Atributos propios	Métodos
Vehiculo (abstracta)	codigo, marca, capacidad, kilometraje	mostrar_informacion(), tipo(), calcular_costo_operativo() (abstracto)
Trufi	numero_rutas, costo_por_km	calcular_costo_operativo(), mostrar_informacion()
Minibus	numero_viajes, costo_por_km	calcular_costo_operativo(), mostrar_informacion()
Radiotaxi	area_asignada, costo_por_km	calcular_costo_operativo(), mostrar_informacion()
Reglas de cálculo del costo operativo
Tipo	Fórmula
Trufi	kilometraje × costo_por_km × (1 + numero_rutas / 10)
Minibús	kilometraje × costo_por_km × (1 + numero_viajes / 8)
Radiotaxi	kilometraje × costo_por_km × 1.2 si el área contiene "Centro"; × 1.0 en otro caso

Ejemplo (datos de las pruebas): Trufi TR001 con 100 km, 2.5 por km y 5 rutas → 100 × 2.5 × 1.5 = 375.00.

Validaciones
La capacidad y el kilometraje no pueden ser negativos (se valida en los setters de Vehiculo).
El costo por km debe ser mayor a 0 (se valida en cada clase derivada).
Si se ingresa texto donde va un número, el programa muestra un mensaje de error y vuelve al menú sin cerrarse.
Pruebas realizadas
Prueba	Resultado
Registro de trufi, minibús y radiotaxi con datos válidos	Se registran correctamente
Mostrar vehículos (herencia)	Los tres tipos muestran los datos generales de la clase base
Calcular costos recorriendo la lista común (polimorfismo)	Cada objeto aplica la fórmula de su propia clase
Kilometraje negativo (−20)	Rechazado: "El kilometraje debe ser un número mayor o igual a 0"
Costo total	Coincide con la suma de los costos individuales (1428.75)

Las capturas de estas pruebas se incluyen en el informe PDF.

Conceptos aplicados
Herencia: Trufi, Minibus y Radiotaxi reutilizan el constructor (super().__init__), los atributos y el método mostrar_informacion() de Vehiculo.
Polimorfismo: la lista flota contiene objetos de las tres clases y v.calcular_costo_operativo() ejecuta la implementación correspondiente a cada uno, sin if/elif por tipo.
Encapsulamiento: los atributos son privados (prefijo _) y se acceden mediante @property con validación.
Abstracción: Vehiculo usa ABC y @abstractmethod, por lo que no puede instanciarse directamente y obliga a cada subclase a implementar el cálculo de costo.
