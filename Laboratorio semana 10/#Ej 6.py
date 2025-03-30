#Ej 6
class Vehiculo:
    def __init__(self, marca, modelo, ano, precio):
        self.marca = marca
        self.modelo = modelo
        self.ano = ano
        self.precio = precio

    def mostrar_informacion(self):
        return f"Marca: {self.marca}, Modelo: {self.modelo}, Año: {self.ano}, Precio: {self.precio}"

class Automovil(Vehiculo):
    def __init__(self, marca, modelo, ano, precio, numero_puertas):
        super().__init__(marca, modelo, ano, precio)
        self.numero_puertas = numero_puertas

    def mostrar_informacion(self):
        return f"{super().mostrar_informacion()}, Número de puertas: {self.numero_puertas}"

class Motocicleta(Vehiculo):
    def __init__(self, marca, modelo, ano, precio, cilindrada):
        super().__init__(marca, modelo, ano, precio)
        self.cilindrada = cilindrada

    def mostrar_informacion(self):
        return f"{super().mostrar_informacion()}, Cilindrada: {self.cilindrada}cc"

def ingresar_datos_vehiculo():
    marca = input("Introduce la marca del vehículo: ")
    modelo = input("Introduce el modelo del vehículo: ")
    ano = int(input("Introduce el año del vehículo: "))
    precio = float(input("Introduce el precio del vehículo: "))
    return marca, modelo, ano, precio

def ingresar_datos_automovil():
    marca, modelo, ano, precio = ingresar_datos_vehiculo()
    numero_puertas = int(input("Introduce el número de puertas del automóvil: "))
    return Automovil(marca, modelo, ano, precio, numero_puertas)

def ingresar_datos_motocicleta():
    marca, modelo, ano, precio = ingresar_datos_vehiculo()
    cilindrada = int(input("Introduce la cilindrada de la motocicleta: "))
    return Motocicleta(marca, modelo, ano, precio, cilindrada)

def mostrar_menu():
    print("1. Registrar Automóvil")
    print("2. Registrar Motocicleta")
    print("3. Mostrar Información de Vehículos")
    print("4. Salir")

def main():
    vehiculos = []
    while True:
        mostrar_menu()
        opcion = input("Elige una opción: ")
        
        if opcion == "1":
            vehiculo = ingresar_datos_automovil()
            vehiculos.append(vehiculo)
            print("Automóvil registrado correctamente.")
        elif opcion == "2":
            vehiculo = ingresar_datos_motocicleta()
            vehiculos.append(vehiculo)
            print("Motocicleta registrada correctamente.")
        elif opcion == "3":
            if vehiculos:
                for vehiculo in vehiculos:
                    print(vehiculo.mostrar_informacion())
            else:
                print("No hay vehículos registrados.")
        elif opcion == "4":
            print("end")
            break
        else:
            print("Opción no válida. Intenta de nuevo.")

if __name__ == "__main__":
    main()