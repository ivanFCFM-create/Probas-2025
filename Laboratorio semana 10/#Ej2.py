#Ej2
productos = {}

def agregar_producto(nombre, categoria, precio, cantidad):
    if nombre not in productos:
        productos[nombre] = [categoria, precio, cantidad]
        return f"Producto '{nombre}' agregado "
    else:
        return f"El producto '{nombre}' ya existe"

def eliminar_producto(nombre):
    if nombre in productos:
        del productos[nombre]
        return f"Producto '{nombre}' eliminado"
    else:
        return f"Producto '{nombre}' no encontrado."

def buscar_producto(nombre):
    if nombre in productos:
        categoria, precio, cantidad = productos[nombre]
        return f"Producto: {nombre}, Categoría: {categoria}, Precio: ${precio}, Cantidad: {cantidad}"
    else:
        return f"Producto '{nombre}' no encontrado."

def mostrar_productos():
    if productos:
        productos_mostrados = "Inventario de productos:\n"
        for nombre, datos in productos.items():
            categoria, precio, cantidad = datos
            productos_mostrados += f"Producto: {nombre}, Categoría: {categoria}, Precio: ${precio}, Cantidad: {cantidad}\n"
        return productos_mostrados
    else:
        return "No hay productos en el inventario."

def menu():
    while True:
        print("\nMENÚ DE INVENTARIO")
        print("1. Agregar producto")
        print("2. Eliminar producto")
        print("3. Buscar producto")
        print("4. Mostrar inventario completo")
        print("5. Salir")

        opcion = input("Elija una opción (1-5): ")

        if opcion == "1":
            cantidad_productos = int(input("¿Cuántos productos desea agregar? "))
            for _ in range(cantidad_productos):
                nombre = input("Ingrese el nombre del producto: ")
                categoria = input("Ingrese la categoría del producto: ")
                precio = float(input("Ingrese el precio del producto: "))
                cantidad = int(input("Ingrese la cantidad del producto: "))
                print(agregar_producto(nombre, categoria, precio, cantidad))

        elif opcion == "2":
            nombre = input("Ingrese el nombre del producto a eliminar: ")
            print(eliminar_producto(nombre))

        elif opcion == "3":
            nombre = input("Ingrese el nombre del producto a buscar: ")
            print(buscar_producto(nombre))

        elif opcion == "4":
            print(mostrar_productos())

        elif opcion == "5":
            print("Saliendo del sistema de inventario.")
            break

        else:
            print("Opción inválida. Por favor, elija una opción válida (1-5).")

menu()