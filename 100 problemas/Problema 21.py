
def areaTriangulo(base,altura):
    Area=(base*altura)/2
    print('El area es:',Area)
    return Area
def areaCuadrado(lado):
    area=lado**2
    print('El area es:',area)
    return area
def arearectangulo(base, altura):
    area=base**altura
    print('El area es:',area)
    return area
def areacirculo(radio,pi):
    pi=3.1416
    area=pi*radio**2
    print('El area es:',area)
    return area

def volesfera(pi,radio):
    pi=3.1416
    volumen=4/3*pi*radio**3
    print('El volumen es:',volumen)
    return volumen
def volpirámide(abase,altura):
    volumen=1/3*abase*altura
    print('El volumen es :',volumen)
    return volumen 
def volcubo(lado):
    volcubo=lado**3
    print('El volumen es:',volcubo)
    return volcubo
def parelelepípedo(abase,altura):
    volparelelepipedo=abase*altura
    print('El volumen es:',volparelelepipedo)
    return(volparelelepipedo)
continuar='s'
while continuar=='s':
    print('Menú')
    print('Seleccione la figura deseada, Triángulo/1, cuadrado/2, rectángulo/3, círculo/4,esfera/5,Pirámide/6,Cubo/7,Paralelepípedo/8')
    Figura=int(input('Introduzca la figura que desea:'))
    if Figura==1:
        base=int(input('Introduzca la base:'))
        altura=int(input('Introduzca la altura:'))
        areaTriangulo
    elif Figura==2:
        areaCuadrado(lado=int(input('Introduzca el lado:')))
    elif Figura==3:
        arearectangulo(base=int(input('Intorduzca la base:')), altura=int(input('Introduzca la altura:')))
    elif Figura==4:
        areacirculo(pi=3.1416, radio=int(input('Introduzca el radio del círculo:')))
    elif Figura==5:
        volesfera(pi=3.1416,radio=int(input('Introduzca el radio:')))
    elif Figura==6:
        volpirámide(abase=int(input('Introduzca el área de la base:')),altura=int(input('Introduzca la altura:')))
    elif Figura==7:
        volcubo(lado=int(input('Introduzca la medida del lado:')))
    elif Figura==8:
        parelelepípedo(abase=int(input('Introduzca el area de la base')), altura=int(input('Introduzca la altura:')))
    
        


