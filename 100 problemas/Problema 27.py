


print("Selecciona el tipo de conversión:")
print("1. SI a Sistema Británico")
print("2. Sistema Británico a SI")

opcion = int(input("Opción: "))

if opcion == 1:
    print("Conversor de unidades SI a Sistema Británico")
    print("Selecciona la opción:")
    print("1. Longitud (metros a unidades del sistema británico)")
    print("2. Masa (kilogramos a libras, onzas y piedras)")
    print("3. Temperatura (Celsius a Fahrenheit)")

    sub_opcion = int(input("Opción: "))

    if sub_opcion == 1:
        metros = float(input("Introduce la longitud en metros: "))
        pulgadas = metros * 39.3701
        pies = metros * 3.28084
        yardas = metros * 1.09361
        millas = metros / 1609.34
        
        print(f"{metros} metros son:")
        print(f"{pulgadas} pulgadas")
        print(f"{pies} pies")
        print(f"{yardas} yardas")
        print(f"{millas} millas")

    elif sub_opcion == 2:
        kilogramos = float(input("Introduce la masa en kilogramos: "))
        libras = kilogramos * 2.20462
        onzas = kilogramos * 35.274
        piedras = kilogramos * 0.157473
        
        print(f"{kilogramos} kilogramos son:")
        print(f"{libras} libras")
        print(f"{onzas} onzas")
        print(f"{piedras} piedras")

    elif sub_opcion == 3:
        celsius = float(input("Introduce la temperatura en grados Celsius: "))
        fahrenheit = (celsius * 9/5) + 32
        print(f"{celsius} grados Celsius son {fahrenheit} grados Fahrenheit.")

    else:
        print("Opción no válida. Por favor, selecciona una opción entre 1 y 3.")

elif opcion == 2:
    print("Conversor de unidades Sistema Británico a SI")
    print("Selecciona la opción:")
    print("1. Longitud (pulgadas, pies, yardas, millas a metros)")
    print("2. Masa (libras, onzas, piedras a kilogramos)")
    print("3. Temperatura (Fahrenheit a Celsius)")

    sub_opcion = int(input("Opción: "))

    if sub_opcion == 1:
        unidad = input("¿Qué unidad deseas convertir (pulgadas, pies, yardas, millas)? ").lower()
        valor = float(input("Introduce el valor a convertir: "))

        if unidad == "pulgadas":
            metros = valor / 39.3701
            print(f"{valor} pulgadas son {metros} metros.")
        elif unidad == "pies":
            metros = valor / 3.28084
            print(f"{valor} pies son {metros} metros.")
        elif unidad == "yardas":
            metros = valor / 1.09361
            print(f"{valor} yardas son {metros} metros.")
        elif unidad == "millas":
            metros = valor * 1609.34
            print(f"{valor} millas son {metros} metros.")
        else:
            print("Unidad no válida. Elige entre pulgadas, pies, yardas o millas.")

    elif sub_opcion == 2:
        unidad = input("¿Qué unidad deseas convertir (libras, onzas, piedras)? ").lower()
        valor = float(input("Introduce el valor a convertir: "))

        if unidad == "libras":
            kilogramos = valor / 2.20462
            print(f"{valor} libras son {kilogramos} kilogramos.")
        elif unidad == "onzas":
            kilogramos = valor / 35.274
            print(f"{valor} onzas son {kilogramos} kilogramos.")
        elif unidad == "piedras":
            kilogramos = valor / 0.157473
            print(f"{valor} piedras son {kilogramos} kilogramos.")
        else:
            print("Unidad no válida. Elige entre libras, onzas o piedras.")

    elif sub_opcion == 3:
        fahrenheit = float(input("Introduce la temperatura en grados Fahrenheit: "))
        celsius = (fahrenheit - 32) * 5/9
        print(f"{fahrenheit} grados Fahrenheit son {celsius} grados Celsius.")

    else:
        print("Opción no válida. Por favor, selecciona una opción entre 1 y 3.")

else:
    print("Opción no válida. Por favor, selecciona una opción entre 1 y 2.")