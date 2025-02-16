
import random

# 1. Distribución Uniforme (Generar números aleatorios entre 1 y 100)
u = [random.randint(1, 100) for _ in range(10)]
print("Distribución uniforme:", u)

# 2. Distribución Normal (Generar números aleatorios con media 0 y desviación estándar 1)
n = [random.gauss(0, 1) for _ in range(10)]
print("Distribución normal:", n)

# 3. Distribución Exponencial (Generar números aleatorios con tasa 1)
e = [random.expovariate(1) for _ in range(10)]
print("Distribución exponencial:", e)

# 4. Distribución Triangular (Generar números aleatorios entre 0 y 100 con moda en 50)
t = [random.triangular(0, 100, 50) for _ in range(10)]
print("Distribución triangular:", t)

# 5. Distribución Log-Normal (Generar números aleatorios con media 0 y desviación estándar 1)
ln = [random.lognormvariate(0, 1) for _ in range(10)]
print("Distribución log-normal:", ln)

# 6. Distribución de Pareto (Generar números aleatorios con parámetro de forma 2)
po = [random.paretovariate(2) for _ in range(10)]
print("Distribución de Pareto:", po)

# 7. Distribución Binomial (Generar números aleatorios con 10 intentos y probabilidad 0.5)
b = [random.betavariate(0.5, 0.5) for _ in range(10)]
print("Distribución binomial:", b)

# 8. Distribución Poisson (Generar números aleatorios con tasa de 5)
p = [random.gauss(5, 1) for _ in range(10)]
print("Distribución Poisson (simulada con Gaussiana):", p)