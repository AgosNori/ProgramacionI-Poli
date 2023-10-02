# Ejercicio 1
'''Solicitar al usuario que ingrese su dirección email. Imprimir un mensaje indicando si la dirección es válida o no, valiéndose de una función para decidirlo. Una dirección se considerará válida si contiene el símbolo "@".'''

#Ejercicio 2
'''Solicitar números al usuario hasta que ingrese el cero. Por cada uno, mostrar la suma de sus dígitos (utilizando una función que realice dicha suma).'''

#Ejercicio 3
'''Solicitar números al usuario hasta que ingrese el cero. Por cada uno, mostrar la suma de sus dígitos. Al finalizar, mostrar la sumatoria de todos los números ingresados y la suma de sus dígitos. Reutilizar la misma función realizada en el ejercicio 2.'''

#Ejercicio 4
'''Requerir al usuario que ingrese un número entero e informar si es par  o no, utilizando una función booleana que lo decida.'''

# Ejercicio 5
'''Escribir un programa que pida números al usuario, motrar el factorial de cada uno y, al finalizar, la cantidad total de números leídos en total. Utilizar una o más funciones, según sea necesario.'''

#Ejercicio 6 
''''´¿ Que hace el siguiente codigo?
def coordenadaZ(x,y):
  x=x+10
  y=y+15
  return x+y

 
#programa principal
x=int(input("Coordenada eje x: "))
y=int(input("Coordenada eje y: "))
for i in range(3):
  z=coordenadaZ(x,y)
  x=x+1
  y=y+1
print(x," . ",y)'''

#Ejercicio 7
'''El siguiente programa debería imprimir el número 2 si se le ingresan como valores x=5, y=1 pero en su lugar imprime 5. ¿Qué hay que corregir?
def maximo(a,b):
  if x>y:
    return x
  else:
    return y

 
def minimo(a,b):
  if x<y:
    return x
  else:
    return y

 
#programa principal
x=int(input("Un número: "))
y=int(input("Otro número: "))
print(maximo(x-3, minimo(x+2, y-5)))

''' 

#Ejercicio 8
'''Escribir una función que, dado un número de DNI, retorne True si el número es válido y False si no lo es. Para que un número de DNI sea válido debe tener entre 7 y 8 dígitos.'''

#Ejercicio 9
'''Escribir una función que muestre por pantalla el saludo ¡Hola amiga! cada vez que se la invoque.'''

# Ejercicio 10
'''Escribir una función a la que se le pase una cadena <nombre> y muestre por pantalla el saludo ¡hola <nombre>!.'''

#Ejercicio 11
'''Escribir una función que calcule el total de una factura tras aplicarle el IVA. La función debe recibir la cantidad sin IVA y el porcentaje de IVA a aplicar, y devolver el total de la factura. Si se invoca la función sin pasarle el porcentaje de IVA, deberá aplicar un 21%.'''


