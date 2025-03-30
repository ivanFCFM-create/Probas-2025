
#ej1

def Analizartexto(Texto):
    Contadorpalabras = {}
    únicas = set()
    Cont = 0
    A = 0
    new = Texto.split()

    for itm in new:
        b = itm
        A=len(new)

        if itm in Contadorpalabras:
            Contadorpalabras[b] += 1
        else:
            Contadorpalabras[b] = 1

        if Contadorpalabras.get(b) == 1:
            únicas.add(b)
            Cont += 1

    mayor_palabra = max(Contadorpalabras, key=Contadorpalabras.get)
    frecuencia_mayor = Contadorpalabras[mayor_palabra]

    return {
        'La cantidad de palabras es': A,
        'La frecuencia de cada palabra es': Contadorpalabras,
        'Palabras únicas son': list(únicas),
        'Cantidad de palabras únicas': Cont,
        'La palabra que más se repite es': mayor_palabra,
        'Número de repeticiones': frecuencia_mayor
    }
print(Analizartexto(Texto=input('Introduzca un texto ')))
