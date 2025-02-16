import random
límite=int(input('Introduzca un límite'))
list=[random.randint(1,100) for _ in range(límite)]
print(list)
cont=0
encontrado=False
Númeroaencontrar=int(input('Introduzca un número:'))
for itm in list:
    if itm==Númeroaencontrar:
        encontrado=True
        cont=list.index(itm)
        cont2=cont+1
        print('El numero pertenece a la lista en la posicion:', cont2)

list.sort()
print(f'Lista ordenada: {list}')

Númeroaencontrar = int(input('Introduzca un número: '))

def busqueda_binaria(ilst, val):
    bajo, alto = 0, len(list) - 1
    while bajo <= alto:
        medio = (bajo + alto) // 2
        if list[medio] == val:
            return medio
        elif list[medio] < val:
            bajo = medio + 1
        else:
            alto = medio - 1
    return -1

posicion = busqueda_binaria(list, Númeroaencontrar)

if posicion != -1:
    print(f'El número {Númeroaencontrar} se encuentra en la posición {posicion + 1}.')
else:
    print(f'El número {Númeroaencontrar} no se encuentra en la lista.')
   