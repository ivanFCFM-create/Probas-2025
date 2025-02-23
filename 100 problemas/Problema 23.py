import random

def generar_matriz(m, n):
    return [[random.randint(1, 10) for _ in range(n)] for _ in range(m)]

def suma_matrices(A, B):
    return [[A[i][j] + B[i][j] for j in range(len(A[0]))] for i in range(len(A))]

def resta_matrices(A, B):
    return [[A[i][j] - B[i][j] for j in range(len(A[0]))] for i in range(len(A))]

def multiplicacion_matrices(A, B):
    return [[sum(A[i][k] * B[k][j] for k in range(len(B))) for j in range(len(B[0]))] for i in range(len(A))]

A = generar_matriz(3, 3)
B = generar_matriz(3, 3)

print("Matriz A:")
for fila in A:
    print(fila)

print("\nMatriz B:")
for fila in B:
    print(fila)

suma = suma_matrices(A, B)
print("\nSuma de A y B:")
for fila in suma:
    print(fila)

resta = resta_matrices(A, B)
print("\nResta de A y B:")
for fila in resta:
    print(fila)

multiplicacion = multiplicacion_matrices(A, B)
print("\nMultiplicación de A y B:")
for fila in multiplicacion:
    print(fila)