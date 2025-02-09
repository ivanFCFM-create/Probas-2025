


Palabra=str(input('Introduzca una palabra:'))
inversa= ''.join(reversed(Palabra))
if Palabra==inversa:
   print('La palabra es un palíndromo')
else:
  print('No es un palíndormo')