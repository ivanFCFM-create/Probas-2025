

import random
#Busqueda lineal
lim=int(input('introduzca el limite:'))
list= [random.randint(1,lim) for num in range(1,lim+1) ]
print(list)
NumeroEnc=int(input('Introduzca el numero a buscar:'))
encontrado=False
for num in list:
    if NumeroEnc==num:
        encontrado=True
if not encontrado==True:
    print('El numero no pertenece a la lista')
else :
    print('El numero pertenece a la lista:')

#Busqueda Binaria
ordenada=sorted(list)
Lista2=[set(ordenada)]


ordenada = sorted(list)

print("Lista ordenada:", ordenada)


def busqueda_binaria(ordenada, numero_enc):
    menor = 0  
    mayor = len(ordenada) - 1  

    while menor <= mayor:
        medio = (menor + mayor) // 2
        if ordenada[medio] == numero_enc:  
            return medio  
        elif ordenada[medio] < numero_enc:  
            menor = medio + 1
        else:  
            mayor = medio - 1
    
    return -1  

numero_enc = int(input("Introduce el número a buscar: "))
resultado = busqueda_binaria(ordenada, NumeroEnc)

if resultado != -1:
    print("El número  está en la lista.")
else:
    print("El número  no está en la lista.")