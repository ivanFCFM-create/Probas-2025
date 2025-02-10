



A=int(input('Introduzca un número:'))
B=int(input('Introduzca el segundo número:'))
C=int(input('Introduzca el tercer número:'))
continuar='si'
while A!=B!=C and continuar=='si':
    if A>B and A>C:
     print('El número mayor es:',A)
    elif B>A and B>C:
       print('El número mayor es:',B)
    else:
       print('El número mayor es:',C)
    continuar=str(input('seleccione no para continuar:'))
    
if A==B==C:
   print('Los números son iguales')
