# Clase 25-09
# Ejercicio de while 37
'''Leer números enteros del teclado, hasta que el usuario ingrese 0. Finalmente,
mostrar la sumatoria de todos los números ingresados.'''
'''
total = 0
numero = int(input('Ingrese un numero :'))
while numero != 0:
    total = total+numero # total += numero
    numero = int(input('Ingrese un numero :'))
print(total)
'''
# 38
'''Leer números enteros de teclado, hasta que el usuario ingrese el 0.
Finalmente mostrar la sumatoria de todos los números positivos ingresados.'''
'''
# incializa la variable total en (sumatoria)
total = 0
#pide q se ingrese un numero
numero = int(input('Ingrese un numero :'))
# si el numero ingresado es distinto de cero entra al while, sino directamente se va a la linea 28 
while numero != 0:
    if numero >0: # valida q el numero ingresado sea positivo o no
        total = total + numero # si es positivo, lo suma en la variable total
        numero = int(input('Ingrese otro numero :')) # pide que se ingrese otro numero
    else: # si el numero no es positivo 
        numero = int(input('Ingrese un numero :')) # pide ingresar otro numero y se repite el ciclo while
print(total) # cuando el numero ingresado sea cero (0) se muestra el total


'''
# Ciclo for
#Iterar una tupla
'''
nombres= ('Gustavo','Ignacio','Pablo','Nai','Lionel','Sandra')
for nom in nombres:
    print(nom)
'''
#Iterar una cadena de texto
'''
ciudad ="Cordoba"
for letra in ciudad:
    print(letra)
'''

#In range
#no toma el ultimo valor
'''
for i in range(1,9):
    print(i)
'''
# ejercicio 1
'''
sumatoria = 0
for num in range(1,11):
    sumatoria += num
print(sumatoria)
'''
# ejercicio 40
'''Cargar una tupla con 5 herramientas y luego imprime una
debajo de la otra.'''

herramientas =('martillo','llave','pala','pico','tornillo')
for h in herramientas :
    print(h)



# Ejercicio 41
'''Escribe un programa que cuente y muestre la cantidad de
vocales (a, e, i, o, u) en una palabra dada por el usuario.'''

contVocales = 0
vocales = 'aeiou'
#vocales =('a','e','i','o','u')
palabra = input('Ingrese una palabra: ')

for letra in palabra:
    if letra in vocales:
        contVocales +=1
print(contVocales)

'''
for i in palabra:
    if i in vocales:
        contVocales +=1
print(contVocales)
    

for ind in palabra:
    if vocales[0] == ind:
        contVocales +=1
    elif vocales[1] == ind:
        contVocales +=1
    elif vocales[2] == ind:
        contVocales +=1
    elif vocales[3] == ind:
        contVocales +=1
    elif vocales[4] == ind:
        contVocales +=1
print(contVocales)'''





#Ejercicio 42
'''imprimir los números entre el 5 y el 20,
saltando de tres en tres.'''


#Ejercicio 43
'''Requerir al usuario que ingrese un número entero positivo
e imprimir todos
los números correlativos entre el ingresado por el usuario y
uno menos del
doble del mismo.
'''

