

#Simular una cuenta bancaria con dep´ositos y retiros.
Cantinicial=float(input('¿Cuánto tiene en el banco?:'))
continuar='s'

while continuar=='s':
    print('Seleccione que desea hacer:')
    print('(1), retirar,'
          '(2) depositar')
    opcion=int(input('Introduzca la opción:'))
    if opcion==1:
        retiro=int(input('¿Cuánto desea retirar?:'))
        Cantinicial-=retiro
    else:
        depósito=int(input('¿Cúanto desea depositar?:'))
        Cantinicial+=depósito
    continuar=input('¿Desea realizar más movimientos?si/s, no/n:')
    print(Cantinicial)
