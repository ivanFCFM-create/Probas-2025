


Lím=int(input('Introduzca un limite:'))
fibonacci=[]
A=0
B=1
fibonacci.append(A)
fibonacci.append(B)
for num in range(3,Lím+1):
    C=A+B
    A=B
    B=C
    fibonacci.append(C)
print(fibonacci)

