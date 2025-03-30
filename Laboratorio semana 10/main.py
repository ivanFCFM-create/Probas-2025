import conversor

def menu():
    print("1. Kilometros a Millas")
    print("2. Celsius a Fahrenheit")
    print("3. Litros a Galones")
    print("4. Salir")

def main():
    while True:
        menu()
        opcion = input("Opcion: ")
        
        if opcion == "1":
            kilometros = float(input("Kilometros: "))
            print(conversor.kilometrosAMillas(kilometros))
        elif opcion == "2":
            celsius = float(input("Celsius: "))
            print(conversor.celsiusAFahrenheit(celsius))
        elif opcion == "3":
            litros = float(input("Litros: "))
            print(conversor.litrosAGalones(litros))
        elif opcion == "4":
            break

if __name__ == "__main__":
    main()