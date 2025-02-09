
#JUEVES


#operadores relacionales
#igualdad, desigualdad, mayor que 

#operadores lógicos: and, or o not
#tipo de dato bool , solo puede tener dos valores, true o false 
#variables básicos 
#La tupla desde que se crea no se puede modifcar (o,o,o) ni se puede agregar 
#Conjunto si yo quiero agregar un numero pero si ya esta , no se agrega 
#Diccionario "Hola": "Saludo",,,,  "Español":" hola mundo",
#"Ingles:""Hello word"
#keys:Value 
#Concepto : significado 
#se agrega una sola vez , es un set el set y el significado se maneja como una lisra
saludos=dict()
saludos['Español']= "Hola mundo "
saludos['English']= "Hello word"
saludos["Fracais"]= "Bonjour Mondieu"
saludos["Nihongo"]="Ohayo Warudo"
saludos["Portugues"]= "Saludos al macaco"

#for {idioms;saludos} in saludos:
#    print(saludos)
#studiambre=dict()
estudiambre=[]
#estudiambre["Nombre"]="Luis gutierrez"
#estudiambre["Carrera"]="DISI"
#estudiambre
#CICLOS
#For se utiliza para iterar sobre una secuencia (como una lista , tupla, diccionario, conjunto o cadena ) o cualquier objeto 
#COMPONENTES ESCENCUIALES DE Los ciclos 
#inicializacion, actualizacion, cuerpo de cilco


#Uso de bool en los ciclos
#Condicion de continuacion
#En los ciclos , la conidicion se avlua un valor booleano para determinar 

primos=[1,2,3,5,7,11,13,17,19,23,29,31]
for impar in range (0,32):
    if impar in primos:
        print(impar)






#lista=[]
#print(bool(lista))