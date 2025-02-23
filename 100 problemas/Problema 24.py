

suma=0
Suseción=list()
agregar='s'
while agregar=='s':
    Num=int(input('Introduzca un número:'))
    suma+=Num
    agregar=input('Desea agregar otro número?:')
    Suseción.append(Num)

print(f"La suma de la sucesión{Suseción},es:",suma)