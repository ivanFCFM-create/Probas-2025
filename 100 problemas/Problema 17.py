


import random

def gen_lista(t, lim=100):
    return [random.randint(1, lim) for _ in range(t)]

class Pila:
    def __init__(self):
        self.items = []

    def vacia(self):
        return len(self.items) == 0

    def agregar(self, v):
        self.items.append(v)

    def quitar(self):
        if not self.vacia():
            return self.items.pop()
        return None

    def cima(self):
        if not self.vacia():
            return self.items[-1]
        return None

    def tamanio(self):
        return len(self.items)

class Cola:
    def __init__(self):
        self.items = []

    def vacia(self):
        return len(self.items) == 0

    def agregar(self, v):
        self.items.append(v)

    def quitar(self):
        if not self.vacia():
            return self.items.pop(0)
        return None

    def frente(self):
        if not self.vacia():
            return self.items[0]
        return None

    def tamanio(self):
        return len(self.items)

class Nodo:
    def __init__(self, v):
        self.val = v
        self.siguiente = None

class Lista:
    def __init__(self):
        self.cabeza = None

    def vacia(self):
        return self.cabeza is None

    def insertar(self, v):
        nuevo = Nodo(v)
        nuevo.siguiente = self.cabeza
        self.cabeza = nuevo

    def eliminar(self, v):
        actual = self.cabeza
        previo = None
        while actual:
            if actual.val == v:
                if previo:
                    previo.siguiente = actual.siguiente
                else:
                    self.cabeza = actual.siguiente
                return
            previo = actual
            actual = actual.siguiente
        print("Valor no encontrado.")

    def buscar(self, v):
        actual = self.cabeza
        while actual:
            if actual.val == v:
                return True
            actual = actual.siguiente
        return False

    def mostrar(self):
        actual = self.cabeza
        while actual:
            print(actual.val, end=" -> ")
            actual = actual.siguiente
        print("None")

# Crear lista aleatoria
t_lista = 10
lst = gen_lista(t_lista)

# Operaciones con Pila
print("Pila:")
p = Pila()
for n in lst:
    p.agregar(n)
print("Pila:", p.items)
print("Cima:", p.cima())
print("Tamaño:", p.tamanio())
print("Eliminado:", p.quitar())
print("Pila después de eliminar:", p.items)
print()

# Operaciones con Cola
print("Cola:")
c = Cola()
for n in lst:
    c.agregar(n)
print("Cola:", c.items)
print("Frente:", c.frente())
print("Tamaño:", c.tamanio())
print("Eliminado:", c.quitar())
print("Cola después de eliminar:", c.items)
print()

# Operaciones con Lista Enlazada
print("Lista Enlazada:")
l = Lista()
for n in lst:
    l.insertar(n)
l.mostrar()

print("Buscar valor", lst[0], ":", l.buscar(lst[0]))
print("Eliminar valor", lst[1], ":")
l.eliminar(lst[1])
l.mostrar()