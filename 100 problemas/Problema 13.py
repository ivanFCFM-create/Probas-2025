

grados=int(input('Iintroduzca los grados:'))
Escala=str(input('Introduzca el tipo de escala, c:celsius,f:farenheit,k:kelvin'))
if Escala=='c':
    F=9/5*grados+32
    K=grados+273.15
    print('en grados fahrenheit:',F,'En grados Kelvin',K)
elif Escala=='f':
    C=5/9*(grados-32) 
    K=C+273.15
    print('en grados celsius:',C,'En grados Kelvin',K)

else:
    C=grados-273.15
    F=9/5*C+32
    print('en grados celsius:',C,'En grados fahrenheit',F)

