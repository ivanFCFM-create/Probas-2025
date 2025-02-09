
with open('archivo.txt', 'w') as archivo:
    archivo.write('Esta es la primera linea.\n')
    archivo.write('Aquí está la segunda linea.\n')
    archivo.write('Y esta es la tercera linea.\n')


with open('archivo.txt', 'r') as archivo:
    contenido = archivo.read()

with open('archivo.txt', 'r') as archivo:
    contenido = archivo.readlines()  

contenido[1] = "Esta es la linea modificada.\n"


with open('archivo.txt', 'w') as archivo:
    archivo.writelines(contenido)


with open('archivo.txt', 'a') as archivo:
    archivo.write('Esta es una linea añadida al final.\n')