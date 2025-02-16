


Cadena= input("Introduce una cadena: ")

Cadena = Cadena.replace(" ", "").lower()
if Cadena == Cadena[::-1]:
    print("Es un palíndromo")
else:
    print("No es un palíndromo")

