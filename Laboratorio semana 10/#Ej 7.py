#Ej 7
import random

def quicksort(lista):
    if len(lista) <= 1:
        return lista
    pivot = lista[0]
    menores = [x for x in lista[1:] if x <= pivot]
    mayores = [x for x in lista[1:] if x > pivot]
    return quicksort(menores) + [pivot] + quicksort(mayores)

def busqueda_binaria(lista, objetivo):
    bajo = 0
    alto = len(lista) - 1
    while bajo <= alto:
        medio = (bajo + alto) // 2
        if lista[medio] == objetivo:
            return medio
        elif lista[medio] < objetivo:
            bajo = medio + 1
        else:
            alto = medio - 1
    return -1

def main():
    n = int(input())
    lista = [random.randint(1, 100) for _ in range(n)]
    print(lista)
    lista_ordenada = quicksort(lista)
    print(lista_ordenada)
    objetivo = int(input())
    resultado = busqueda_binaria(lista_ordenada, objetivo)
    if resultado != -1:
        print(f"{objetivo} encontrado en la posición {resultado}")
    else:
        print(f"{objetivo} no encontrado")

if __name__ == "__main__":
    main()


