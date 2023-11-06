# Funciones
'''Ejercicio 1:
Ingresar n numeros y mostrar su promedio'''
'''
def prom ():
    n = int(input('Ingrese la cantidad de numeros :'))
    suma = 0
    for i in range(n):
        num = int(input('Ingrese un num: '))
        suma += num
        prom =  suma / n
    print('el promedio es: ',prom)

prom()
'''
''' Ejercicio 2:
Ingresar un numero y mostrar el cuadrado del mismo.
El numero debe ser mayor que cero, en caso de error
que aparezca el mensaje "Error. Reingresar numero"'''
'''
def cuadrado ():
    num = int(input('Ingrese un numero: '))
    if num > 0:
        cuadrado = num **2
    else:
        print('error. reingresar numero')
    print('el cuadrado es: ',cuadrado)
cuadrado()

'''
'''Ejercicio 3:
De 10 numeros ingresados indicar cuantos son mayores a cero
y cuantos son menores a cero.'''

'''
def mayoresMenores():
    conMayores = 0
    conMenores =0 
    for i in range(10):
        num = int(input('Ingrese un numero: '))
        if num > 0:
            conMayores +=1
        elif num == 0:
           print('no esta dentro de los parametros')
        else:
            conMenores += 1
    print('mayores a 0',conMayores)
    print('menores  a 0: ', conMenores)
    
mayoresMenores()




'''


'''Ejercicio 4:
Diseñar un algoritmo que calcule la longitud de la circunferencia
y el area del circulo de radio dado'''
'''
def circunferencia (radio):
    pi = 3.1415
    longitud = pi*(2*radio)
    area = pi*(radio**2)
    print('La longitud del area es: ',longitud)
    print('El area de la circunferencia es: ', area)

circunferencia(2)
'''

'''Ejercicio 5:
Diseñar un algoritmo que calcule la superficie de un triangulo
a partir del ingreso de su base y altura, y muestre su
resultado.'''

def superficie(base,altura):
    sup = (base*altura)/2
    print(sup)
    
superficie(2,10)
    
def super():
    base = float(input('Ingrese la base: '))
    altura = float(input('Ingrese la altura: '))
    superficie = (base*altura)/2
    print('La superficie del triangulo es: ',superficie)
    
super()





'''Ejercicio 6:
Ingresar un numero e indicar si es positivo o negativo'''

'''Ejercicio 7:
Ingresar un numero y mostrar si es par o impar.'''

'''Ejercicio 8:
Equivalencia de grados celsius a grados fahrenheit'''

'''Ejercicio 9:
Ingresar una frase no mas de 20 caracteres y mostrar cuantas vocales tiene'''

'''Ejercicio 10:
Mostrar los numeros impares entre el 0 y el 100'''

'''Ejercicio 11:
Mostrar los numeros pares entre el 0 y el 100'''

'''Ejercicio 12:
Mostrar los numeros del 100 al 0'''

'''Ejercicio 13:
Mostrar los multiplos de 3 del 0 al 100'''

'''Ejercicio 14:
Ingresar un numero y mostrar la suma de los numeros que lo antecedan'''

'''Ejercicio 15:
Mostrar los numeros del 1 hasta el numero ingresado'''