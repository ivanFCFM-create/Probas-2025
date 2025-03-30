#Ej 3
agenda = []

def agregar_contacto(nombre, numero, correo):
    contacto = (nombre, numero, correo)
    agenda.append(contacto)
    return f"Contacto '{nombre}' agregado."

def buscar_contacto(nombre):
    for contacto in agenda:
        if contacto[0].lower() == nombre.lower():
            return f"Nombre: {contacto[0]}, Número: {contacto[1]}, Correo: {contacto[2]}"
    return f"Contacto '{nombre}' no encontrado."

def listar_contactos():
    if agenda:
        agenda_ordenada = sorted(agenda, key=lambda contacto: contacto[0].lower())
        contactos_listados = "Lista de contactos ordenada alfabéticamente:\n"
        for contacto in agenda_ordenada:
            contactos_listados += f"Nombre: {contacto[0]}, Número: {contacto[1]}, Correo: {contacto[2]}\n"
        return contactos_listados
    else:
        return "No hay contactos en la agenda."

def menu():
    while True:
        print("\n--- MENÚ DE AGENDA DE CONTACTOS ---")
        print("1. Agregar contacto")
        print("2. Buscar contacto")
        print("3. Listar todos los contactos")
        print("4. Salir")

        opcion = input("Elija una opción (1-4): ")

        if opcion == "1":
            nombre = input("Ingrese el nombre del contacto: ")
            numero = input("Ingrese el número del contacto: ")
            correo = input("Ingrese el correo del contacto: ")
            print(agregar_contacto(nombre, numero, correo))

        elif opcion == "2":
            nombre = input("Ingrese el nombre del contacto a buscar: ")
            print(buscar_contacto(nombre))

        elif opcion == "3":
            print(listar_contactos())

        elif opcion == "4":
            print("Saliendo del sistema de agenda.")
            break

        else:
            print("Opción inválida. Por favor, elija una opción válida (1-4).")

menu()


