

#AÑO BISIESITO
Año=int(input('Leer Introduzca el año:'))

if Año%4==0:
    if Año%100==0:
       if Año%400==0:
        print('El año es bisisesto')
       else:
          print('El año no es bisiesto')
    else:
       print('El año es bisiesto')
else:
   print('El año es bisiesto')