#Ej 9
# Imperativa
a = 5
b = 3
resultado_suma = a + b
resultado_resta = a - b
resultado_multiplicacion = a * b
if b != 0:
    resultado_division = a / b
else:
    resultado_division = "No se puede dividir por cero"

print("Imperativa:")
print("Suma:", resultado_suma)
print("Resta:", resultado_resta)
print("Multiplicación:", resultado_multiplicacion)
print("División:", resultado_division)

# Estructurada
def suma(a, b):
    return a + b

def resta(a, b):
    return a - b

def multiplicacion(a, b):
    return a * b

def division(a, b):
    if b != 0:
        return a / b
    else:
        return "No se puede dividir por cero"

print("\nEstructurada:")
print("Suma:", suma(5, 3))
print("Resta:", resta(5, 3))
print("Multiplicación:", multiplicacion(5, 3))
print("División:", division(5, 3))

# Modular
def realizar_operaciones(a, b):
    suma_resultado = a + b
    resta_resultado = a - b
    multiplicacion_resultado = a * b
    if b != 0:
        division_resultado = a / b
    else:
        division_resultado = "No se puede dividir por cero"
    
    return suma_resultado, resta_resultado, multiplicacion_resultado, division_resultado

print("\nModular:")
suma_resultado, resta_resultado, multiplicacion_resultado, division_resultado = realizar_operaciones(5, 3)
print("Suma:", suma_resultado)
print("Resta:", resta_resultado)
print("Multiplicación:", multiplicacion_resultado)
print("División:", division_resultado)

# Orientada a Objetos
class Calculadora:
    def __init__(self):
        self.resultado = 0
    
    def sumar(self, a, b):
        self.resultado = a + b
        return self.resultado

    def restar(self, a, b):
        self.resultado = a - b
        return self.resultado

    def multiplicar(self, a, b):
        self.resultado = a * b
        return self.resultado

    def dividir(self, a, b):
        if b != 0:
            self.resultado = a / b
        else:
            self.resultado = "No se puede dividir por cero"
        return self.resultado

calculadora_obj = Calculadora()

print("\nOrientada a Objetos:")
print("Suma:", calculadora_obj.sumar(5, 3))
print("Resta:", calculadora_obj.restar(5, 3))
print("Multiplicación:", calculadora_obj.multiplicar(5, 3))
print("División:", calculadora_obj.dividir(5, 3))