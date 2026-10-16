from vehiculos_tipos import Trufi, Minibus, Radiotaxi

def main():
    # Colección común de tipo Vehiculo → DEMUESTRA POLIMORFISMO
    flota = []

    while True:
        print("\n" + "="*55)
        print("   SISTEMA DE GESTIÓN DE TRANSPORTE UNIVERSITARIO")
        print("="*55)
        print("1. Registrar Trufi")
        print("2. Registrar Minibús")
        print("3. Registrar Radiotaxi")
        print("4. Mostrar todos los vehículos")
        print("5. Calcular costo operativo individual")
        print("6. Calcular costo operativo TOTAL")
        print("7. Salir")
        print("="*55)

        opcion = input("Seleccione una opción: ")

        try:
            if opcion == "1":
                print("\n--- Registrar Trufi ---")
                veh = Trufi(
                    input("Código: "),
                    input("Marca: "),
                    int(input("Capacidad: ")),
                    float(input("Kilometraje recorrido: ")),
                    float(input("Costo por km ($): ")),
                    int(input("Número de rutas: "))
                )
                flota.append(veh)
                print(" Trufi registrado correctamente!")

            elif opcion == "2":
                print("\n--- Registrar Minibús ---")
                veh = Minibus(
                    input("Código: "),
                    input("Marca: "),
                    int(input("Capacidad: ")),
                    float(input("Kilometraje recorrido: ")),
                    float(input("Costo por km ($): ")),
                    int(input("Número de viajes: "))
                )
                flota.append(veh)
                print(" Minibús registrado correctamente!")

            elif opcion == "3":
                print("\n--- Registrar Radiotaxi ---")
                veh = Radiotaxi(
                    input("Código: "),
                    input("Marca: "),
                    int(input("Capacidad: ")),
                    float(input("Kilometraje recorrido: ")),
                    float(input("Costo por km ($): ")),
                    input("Área asignada: ")
                )
                flota.append(veh)
                print(" Radiotaxi registrado correctamente!")

            elif opcion == "4":
                print("\n--- Vehículos Registrados ---")
                if not flota:
                    print("No hay vehículos registrados.")
                for v in flota:
                    print(v.mostrar_informacion())  # ← polimorfismo

            elif opcion == "5":
                print("\n--- Costos Operativos ---")
                if not flota:
                    print("No hay vehículos registrados.")
                for v in flota:
                    print(f"{v.codigo} ({v.tipo()}) → Costo: ${v.calcular_costo_operativo():.2f}")
                    # ↑ MISMA LLAMADA → DIFERENTE CÁLCULO según el tipo de objeto

            elif opcion == "6":
                print("\n--- Costo Operativo TOTAL ---")
                total = sum(v.calcular_costo_operativo() for v in flota)
                print(f"COSTO TOTAL DE LA FLOTA: ${total:.2f}")

            elif opcion == "7":
                print(" Saliendo del sistema...")
                break

            else:
                print(" Opción no válida.")

        except ValueError as e:
            print(f" Error: {e}")

if __name__ == "__main__":
    main()