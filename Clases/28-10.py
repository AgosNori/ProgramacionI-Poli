#Repaso
#Ejercicio 1:
'''Imprime <Hola Mundo> si a es mayor a b '''
'''
# entradas
a = 36
b = 65

#procesos y salidas
if a > b :
    print('HOLA MUNDO')
else:
    print('chau')
'''
#Ejercicio 2:
''' Determinar si alguien es menor de edad o no.
Pide al usuario la edad por pantalla e imprime por
pantalla si puede acceder a nuestra fiesta nocturna de
BigBayData.com'''

'''
#entradas
edad = int(input('Porfavor ingrese su edad : '))
#procesos y salidas

if edad > 18:
    print('Puede ingresar')
else:
    print('No puede ingresar')

'''

#Ejercicio 3:
'''Imaginemos que en nuestra tienda hay un carnet por
puntos y que alguien debe pagar el precio final de compra.
Si tiene menos de 100 puntos realizaremos un descuento
del 10%. Si es mayor a 100 y menor a 150 aplicamos un 12%.
Si tiene 150 un 15% y sino, el resto de los casos de mas
de 150 , un 20% ¡ Crea la variable puntos y juega con ella!
'''
'''

# entradas
carnetDescuentos = int(input('Porfavor ingrese sus puntos: '))
precio = 35000
if carnetDescuentos < 100:
    print('Se aplica un descuento del 10%')
    total = precio - (precio* 0.10)
    print('El total a pagar es: ',total)
elif carnetDescuentos  > 100 and carnetDescuentos < 150:
    print('Se aplica un descuento del 12%')
    total = precio - (precio* 0.12)
    print('El total a pagar es: ',total)
elif carnetDescuentos == 150:
    print('Se aplica un descuento del 15%') 
    total = precio - (precio* 0.15)
    print('El total a pagar es: ',total)
elif carnetDescuentos > 150:
    print('Se aplica un descuento del 20%')
    total = precio - (precio* 0.20)
    print('El total a pagar es: ',total)
'''

#Ejercicio 4:
'''Guardar una contraseña como password. Crea un sistema de seguridad
donde el ordenador muestre un mensaje <Ordenador  Bloqueado. contraseña
incorrecta> si el usuario falla la contraseña. En caso contrario ,
que muestre por pantalla <Bienvenid@>'''
'''
# entradas
contraseña = 1234
password = int(input('Porfavor ingrese la contraseña: '))

#procesos y salidas

if password == contraseña:
    print('Bienvenido')
else:
    print('Ordenandor Bloqueado. Contraseña incorrecta')


'''
#Ejercicio 5:
'''Partiendo de la tarifa anual (que puede cambiar), nos piden que
debemos calcular el precio de la tarifa de nuestro polideportivo,
sabiendo las siguientes condiciones:
Criterio 1: Si es mayor de edad y esta trabajando -> Paga el 100%
Criterio 2: Si es menor de edad y esta trabajando -> Paga el 95%
Criterio 3: Si es mayor de edad y no esta trabajando -> Paga el 75%
Criterio 4: Si es menor de edad y no esta trabajando -> Paga el 50%
'''
'''
# entradas
edad = int(input('Porfavor ingrese su edad:'))
situacionLaboral = input('Activo o No: ')
tarifa = int(input('Porfavor ingrese la tarifa por persona: '))

if edad > 18 and situacionLaboral == "Activo":
    print('Paga el 100%')
    print('Debe abonar: ', tarifa)
    
elif edad < 18 and situacionLaboral == "Activo":
    print('Paga el 95%')
    total = tarifa - (tarifa* 0.05)
    print('Debe abonar:',total)

elif edad > 18 and situacionLaboral == "No":
    print('Paga el 75%')
    total = tarifa - (tarifa* 0.25)
    print('Debe abonar:',total)

elif edad < 18 and situacionLaboral == "No":
    print('Paga el 50%')
    total= tarifa - (tarifa * 0.5)
    print('Debe abonar: ',total)
'''



# Ejercicio 6:
''' Imprimir los numeros del 1 al 10 '''


#Ejercicio 7:
''' Tenemos la pantalla del celular bloqueada.
Partiendo de un pin secreto, intentaremos desbloquear
la pantalla. Tenemos hasta tres intentos.Simula el proceso con
Python. En caso de acceder, lanza al usuario <Login Correcto> ,
sino <Llamando a la policia>'''









