

Frase=str(input('Introduzca una frase:'))
cont=0
cont2=0
Vocal={'a','e','i','o','u'} 

for character in Frase:
   if character.isalpha():
    if character in Vocal:
       cont+=1
    else:
        cont2+=1
    
    
print('La cadena:',Frase, 'Tiene', cont, 'vocales y tiene ', cont2, 'de consonantes' )