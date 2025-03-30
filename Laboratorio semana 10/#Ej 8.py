#Ej 8
def mergesort(lista):
    if len(lista) <= 1:
        return lista
    medio = len(lista) // 2
    izquierda = mergesort(lista[:medio])
    derecha = mergesort(lista[medio:])
    return merge(izquierda, derecha)

def merge(izquierda, derecha):
    resultado = []
    i = j = 0
    while i < len(izquierda) and j < len(derecha):
        if izquierda[i] < derecha[j]:
            resultado.append(izquierda[i])
            i += 1
        else:
            resultado.append(derecha[j])
            j += 1
    resultado.extend(izquierda[i:])
    resultado.extend(derecha[j:])
    return resultado

def main():
    n = int(input("Introduzca el número de elementos? "))
    lista = [int(input(f"Ingrese el número {i+1}: ")) for i in range(n)]
    
    print("Lista antes del ordenamiento:")
    print(lista)
    
    lista_ordenada = mergesort(lista)
    
    print("Lista después del ordenamiento:")
    print(lista_ordenada)

if __name__ == "__main__":
    main()