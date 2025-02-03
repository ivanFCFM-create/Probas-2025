

Cont=0

Número=int(input('Introduzca un número:'))
for num in range(1, Número+1):
    R=Número%num
    if R==0:
        Cont=Cont+1

if Cont==2:
    print('El número es primo')
else:
    print('EL número no es primo')
    
