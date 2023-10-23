'''Escribir un programa que pregunte al usuario su edad y
muestre por pantalla si es mayor de edad o no.'''
# entradas
edad = int(input('ingrese la edad:'))
#procesos
if edad >= 18:
    print('Usted es mayor de edad')
else:
    print('Usted es menor')
    
'''Escribir un programa que almacene la cadena de caracteres
contraseña en una variable, pregunte al usuario por la contraseña
e imprima por pantalla si la contraseña introducida por el usuario
coincide con la guardada en la variable sin tener en cuenta
mayúsculas y minúsculas.'''

#entrada
usuario= input('ingrese la contraseña:')
#procesos
contra = 'contraseña'


if usuario == contra:
    salida='Acceso valido'
else:
    salida='Denegado'


#salidas
print(salida)






