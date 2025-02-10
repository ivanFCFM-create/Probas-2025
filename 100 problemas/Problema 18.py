

print('AX**2+BX+C=0')
A=int(input('introduzca el coeficiente del termino cuadratico: '))
B=int(input('Introduzca el termino del coeficiente lineal:'))
C=int(input('Leer introduzca el termino independiente:'))
print(A,'X**2+',B,'X+',C,'=0')
D=B**2-4*A*C

X1=(-B-D**(1/2))/2*A
X2=(-B+D**(1/2))/2*A


if X1==X2:
    print('Hay raices doble y es ', X1,',', X2)
else:
    print('xe', {X1,X2})
