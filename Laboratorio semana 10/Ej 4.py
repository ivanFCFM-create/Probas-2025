

def calcular_estadisticas(*args):
    promedio = sum(args) / len(args)

    argsordenados = sorted(args)
    n = len(argsordenados)
    if n % 2 == 0:
        mediana = (argsordenados[n // 2 - 1] + argsordenados[n // 2]) / 2
    else:
        mediana = argsordenados[n // 2]

    suma_cuadrados = 0
    for x in args:
        suma_cuadrados += (x - promedio) ** 2
    varianza = suma_cuadrados / len(args)
    
    desviacionestandar = varianza ** 0.5  

    return promedio, mediana, desviacionestandar
#Introduzca la lista que desee:
numeros = [1,2,3,4,5,6,7,8,9,10,1,12,34,56,78,9,55,123,46]
promedio, mediana, desviacionestandar = calcular_estadisticas(*numeros)

print("Promedio:",promedio)
print("Mediana:", mediana)
print('Desviación estándar:', desviacionestandar)