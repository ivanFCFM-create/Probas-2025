

cont=1
Agregar='s'
Agendadecontactos=[]
while Agregar=='s':
   contactos=dict()
   contactos['Nombre del contacto']=input(f'Introduzca el nombre delcontacto:{cont}:')
   contactos['Número']=int(input(f'Introduzca el número del contacto{cont}:'))
   Agendadecontactos.append(contactos)
   Agregar=input('Desea agregar más contactos(s/n)?:')
   cont+=1

print(Agendadecontactos)
    