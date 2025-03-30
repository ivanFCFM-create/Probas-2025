

#Simular una cuenta bancaria con

Cantinicial=int(input('Introduzca cuanto tiene en el banco '))
def retiro(Cant):
    Cantinicial=+Cant
    return Cantinicial
def deposito(Cant2):
    Cantinicial=+Cant2
continuar=input('Introduzca')
while continuar == 's ':
     print('Retiro/1, depositar/2')
     opcion=int(input('Introduzca la ocpion, 1/2'))
     if opcion==1:
         Cant=int(input('Introduzca la cantidad a retirrar:'))
         retiro(Cant)
     else:
        Cant2=int(input('Introduzca la cantidad a depositar:'))
        deposito(Cant2)
     continuar=int(input('Desea continuar:'))

    
    