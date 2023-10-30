#Resultados del repaso
#Ejercicio 1:

#entradas
'''
a = int(input('Porfavor ingrese un numero:'))
b= int(input('Porfavor ingrese otro numero:'))

#procesos y salidas
if a > b :
    print('Hola Mundo')
'''
#Ejercicio 2
    
#Entradas
'''
edad = int(input('Porfavor ingrese su edad: '))

#proceso y salidas
if edad >= 18:
    print('Bienvenid@, te esperamos en BigBayData.com')
else:
    print('Lo siento, eres menor de edad')
'''
#Ejercicio 3
#entradas
'''
puntos = int(input('Porfavor ingrese la cantidad de puntos que tiene: '))
precio = float(input('Porfavor ingrese el precio del producto a comprar :'))
#procesos y salidas
if puntos < 100:
    print('Tiene un descuento del 10%')
    precioFinal = precio - (precio *0.10)
    print('El precio final a pagar es: ',precioFinal)
elif puntos > 100 and puntos < 150:
    print('Tiene un descuento del 12%')
    precioFinal= precio - (precio*0.12)
    print('El precio final a pagar es: ',precioFinal)
elif puntos == 150:
    print('Tiene un descuento del 15%')
    precioFinal = precio - (precio*0.15)
    print('El precio final a pagar es: ',precioFinal)
else:
    print('Tiene un descuento del 20%')
    precioFinal = precio - (precio*0.20)
    print('El precio final a pagar es: ',precioFinal)
    '''
#Ejercicio 4
#entradas
'''
password = input('Porfavor ingrese la contraseña :')
contraseña = 'pepito'
#proceso y salida
if password == contraseña:
    print('Bienvenid@')
else:
    print('Ordenador bloqueado. Contraseña incorrecta')
'''

#Ejercicio 5
