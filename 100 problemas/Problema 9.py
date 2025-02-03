


Lím=int(input('Introduzca un límite:'))
Par=[]
Impar=[]
Lista=[]
for num in range(1, Lím+1):
    if num%2:
        Par.append(num)
    else:
        Impar.append(num)

lista=[Par, Impar]
print(lista)