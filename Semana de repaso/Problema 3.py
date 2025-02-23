
#18 de febrero, martes 
#problema 3
num=int(input('Introduzca número '))
import math
factirial=math.factorial(num)
print('El factorial de un numero es :', factirial)
A=1
for i in range (1,num+1):
    A=i*A
print(A)

# problema 4 Fibbonaci
#(0,1,1,2,3,5,8)
#YO
fibbonaci=[]
B=0
C=1
fibbonaci.append(B)
fibbonaci.append(C)

Lim=int(input('Introduzca el termino enésimo'))
for i in range(3,Lim+1):
    D=B+C
    B=C
    C=D
    fibbonaci.append(D)
print('La secuencia de fibbonaci hasta el termino',Lim,'es:', fibbonaci)
#Maestro 


def multiplicación(NUM1,NUM2):
 NUM1=int(input('introduzca el primer número '))
 NUM2=int(input('Introduzca el segundo número :'))
 multi=NUM1*NUM2
 print(f"multiplicacion={multi}")


#Yo solo sé que no sé nada 
