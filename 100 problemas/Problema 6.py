

C=int(input('Introduzca el capital:'))
Time=int(input('Introduzca el tiempo:'))
Tasa=float(input('Introduzca la tasa de interés:'))
IC=C*(1+Tasa)**Time

print('El interés compuesto despúes de aplicarlo una vez al año es:',IC)
