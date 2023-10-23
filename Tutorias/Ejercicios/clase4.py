# Ejercicios basicos para py

#Ejercicio 1
'''Escribí un programa que solicite al usuario que ingrese su nombre.
El nombre se debe almacenar en una variable llamada nombre.
A continuación se debe mostrar en pantalla el texto “Ahora estás en la matrix, [usuario]”,
donde “[usuario]” se reemplazará por el nombre que el usuario haya ingresado.'''

#Entradas
nombre= input('Ingrese su nombre: ')
# Salidas
print('Ahora estas en la matrix, ',nombre)


#Ejercicio 2
'''Escribí un programa que solicite al usuario ingresar un número con decimales y
almacenalo en una variable. A continuación, el programa debe solicitar al usuario
que ingrese un número entero y guardarlo en otra variable. En una tercera variable
se deberá guardar el resultado de la suma de los dos números ingresados por el usuario.
Por último, se debe mostrar en pantalla el texto “El resultado de la suma es [suma]”,
donde “[suma]” se reemplazará por el resultado de la operación.'''

#Entradas
numD= float(input('Porfavor ingrese un numero decimal: '))
numE = int(input('Porfavor ingrese un numero entero: '))
#Procesos
suma = numD+numE
#Salidas
print('El resultado de la suma es: ',suma)


#Ejercicio 3
'''Escribí un programa que solicite al usuario dos números y los almacene en dos variables.
En otra variable, almacená el resultado de la suma de esos dos números y luego mostrá ese
resultado en pantalla.
A continuación, el programa debe solicitar al usuario que ingrese un tercer número,
el cual se debe almacenar en una nueva variable. Por último, mostrá en pantalla el resultado
de la multiplicación de este nuevo número por el resultado de la suma anterior.'''


#Entradas
num1 = int(input('Ingrese un numero: '))
num2 = int(input('Ingrese otro numero: '))
num3=  int(input('Ingrese otro numero mas: '))
#Procesos
suma = num1+num2
multiplicacion = suma*num3
#Salidas
print('El resultado de la suma es: ',suma)
print('El resultado de la multiplacion es: ',multiplicacion)

#Ejercicio 4
'''Escribí un programa que solicite al usuario ingresar la cantidad de kilómetros recorridos
por una motocicleta y la cantidad de litros de combustible que consumió durante ese recorrido.
Mostrar el consumo de combustible por kilómetro.'''

#Entradas
km = float(input('Porfavor ingrese la cantidad de km recorridos por una moto: '))
litros = float(input('Ingrese la cantidad de litros que consumio: '))
#Procesos
consumo = km/litros
#Salidas
print('El consumo final es: ',consumo)

#Ejercicio 5
'''Escribí un programa que solicite al usuario ingresar tres números para luego mostrarle
el promedio de los tres.'''


#Entradas
n1 = int(input('Ingrese el primer numero : '))
n2 = int(input('Ingrese el segundo numero :'))
n3 = int(input('Ingrese el tercer numero: '))
#Procesos
promedio= (n1+n2+n3)/3
#Salidas
print('El promedio de los tres numeros es: ',round(promedio,2))

#Ejercicio 6
'''Escribí un programa que solicite al usuario un número y le reste el 15%, almacenando
todo en una única variable. A continuación, mostrar el resultado final en pantalla.'''

#Entradas
numerito = int(input('Ingrese un numero cualquiera :'))

#Procesos
resultFinal = numerito -numerito*0.15

#Salidas
print(resultFinal)



#Ejercicio 7
'''Escribí un programa que solicite al usuario el ingreso de dos palabras, las cuales se
guardarán en dos variables distintas. A continuación, almacená en una variable la
concatenación de la primera palabra, más un espacio, más la segunda palabra.
Mostrá este resultado en pantalla.'''

#Entradas
palabra1 = input('Ingrese una palabra: ')
palabra2 = input('Ingrese otra palabra: ')
#Procesos
palabrafinal= palabra1+' '+palabra2
#Salidas
print(palabrafinal)



#Ejercicio 8
'''Escribí un programa que solicite al usuario el ingreso de un texto y almacene ese
texto en una variable. A continuación, mostrar en pantalla la primera letra del texto
ingresado. Luego, solicitar al usuario que ingrese un número positivo menor a la cantidad
de caracteres que tiene el texto que ingresó (por ejemplo, si escribió la palabra “HOLA”,
tendrá que ser un número entre 0 y 4) y almacenar este número en una variable llamada indice.
Mostrar en pantalla el carácter del texto ubicado en la posición dada por indice.'''










#Ejercicio 9
'''Escribí un programa que le solicite al usuario ingresar una fecha formada por 8 números,
donde los primeros dos representan el día, los siguientes dos el mes y los últimos cuatro
el año (DDMMAAAA). Este dato debe guardarse en una variable con tipo int (número entero).
Finalmente, mostrar al usuario la fecha con el formato DD / MM / AAAA.'''

#Ejercicio 10
'''Escribí un programa para solicitar al usuario el ingreso de un número entero y que luego
imprima un valor de verdad dependiendo de si el número es par o no. Recordar que un número
es par si el resto, al dividirlo por 2, es 0.'''

#Ejercicio 11
'''Escribí un programa que, dado un número entero, muestre su valor absoluto.
Recordá que, para los números positivos su valor absoluto es igual al número
(el valor absoluto de 52 es 52), mientras que, para los negativos, su valor absoluto
es el número multiplicado por -1 (el valor absoluto de -52 es 52).'''

#Ejercicio 12
'''Escribí un programa que solicite al usuario el ingreso de dos números diferentes y
muestre en pantalla al mayor de los dos.'''

#Ejercicio 13
'''Escribí un programa que solicite ingresar un nombre de usuario y una contraseña.
Si el nombre es “Gwenevere” y la contraseña es “excalibur”, mostrar en pantalla
“Usuario y contraseña correctos. Puede ingresar a Camelot”. Si el nombre o la
contraseña no coinciden, mostrar “Acceso denegado”.'''
