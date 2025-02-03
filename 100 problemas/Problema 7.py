

L=int(input('Intorduzca un numero:'))
R= L%2
Divisores=[]
if R==0:
    print('El numero', L, 'es par')
else:
    print('El numero', L, 'es impar')

for i in range(1,L+1):
    D=L%i
    if i!=1 and i!=L:
        if D==0:
         Divisores.append(i)

print('Sus divisores son aparte del 1 y el mismo número son:', Divisores)