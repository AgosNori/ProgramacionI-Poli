# Ejercicio 1
'''Solicitar al usuario que ingrese su dirección email.
Imprimir un mensaje indicando si la dirección es válida o no,
valiéndose de una función para decidirlo. Una dirección se considerará
válida si contiene el símbolo "@".'''
'''
casilla=input('Ingrese su email:') # ingresa la
def email (mail):
    if "@" in mail:
        return True
    else:
        return False
    
es_valido = email(casilla)
if es_valido == True:
    print('La direccion es valida')
else:
    print('La direccion no es valida')
'''
#Ejercicio 2
'''Solicitar números al usuario hasta que ingrese el cero. Por cada uno,
mostrar la sumatoria de los numeros ingresado (utilizando una función que realice dicha suma).'''
'''
def sumatoria (num):
    sumaTotal = 0
    while num != 0:
        
        sumaTotal = sumaTotal + num
    return sumaTotal

def sumatoria(numero):
    suma=0
  
    while numero != 0:
        suma =+ numero

        1return suma

 
num=int(input("Número a procesar: "))
while num!=0:
    #print("Suma:",sumatoria(num))
    print(sumatoria(num))
    num=int(input("Número a procesar: "))  
    
''''''
def sumatoria(numero):
    suma = 0
    while numero != 0:
        suma += numero
        numero = int(input("Número a procesar (0 para salir): "))
    return suma

num = int(input("Número a procesar (0 para salir): "))
while num != 0:
    print("Suma:", sumatoria(num))
    break 
    num = int(input("Número a procesar (0 para salir): "))
'''

#Ejercicio 3
'''Solicitar números al usuario hasta que ingrese el cero. Por cada uno, mostrar la suma de sus dígitos. Al finalizar, mostrar la sumatoria de todos los números ingresados y la suma de sus dígitos. Reutilizar la misma función realizada en el ejercicio 2.'''

#Ejercicio 4
'''Requerir al usuario que ingrese un número entero e informar si es par  o no, utilizando una función booleana que lo decida.'''










# Ejercicio 5
'''Escribir un programa que pida números al usuario,
motrar el factorial de cada uno y, al finalizar,
la cantidad total de números leídos en total.
Utilizar una o más funciones, según sea necesario.'''
'''
def factorial (num):
    factorial = 1 #incializo el factorial en 1
    if num != 0: # si num es distinto de cero ingresa al for
        for i in range (1,num+1): # recorre desde 1 hasta el num ingresado
            factorial = factorial * i #formula del factorial
    return factorial    # devuelve el valor del factorial
#inicializamos el contador para saber cuanto 
contador = 0   
num = int(input('Porfavor ingrese un numero ( con 10 corta): '))
while num != 10:
    print('El factorial del num :',num ,' es:',factorial(num))
    contador += 1
    num = int(input('Porfavor ingrese un numero (con 10 corta): '))
print('La cantidad de numeros leidos son: ',contador)
'''


#Ejercicio 6 
''''´¿ Que hace el siguiente codigo?
determinar cuál es la salida en pantalla
si se ingresan los valores x=6, y=7:'''
'''
def coordenadaZ(x,y):
    x=x+10   
    y=y+15   
    return x+y 
x=int(input("Coordenada eje x: "))
y=int(input("Coordenada eje y: "))
for i in range(3):
  z=coordenadaZ(x,y)  
  x=x+1                          
  y=y+1
print(x,".",y)
'''
#Ejercicio 7
'''El siguiente programa debería imprimir el
número 2 si se le ingresan como valores x=5, y=1
pero en su lugar imprime 5. ¿Qué hay que corregir?

def maximo(a,b): 
  if a>b:  
    return a
  else:
    return b 
def minimo(a,b):
  if a<b: 
    return a 
  else:
    return b 
#programa principal
a=int(input("Un número: "))
b=int(input("Otro número: "))
print(maximo(a-3, minimo(a+2, b-5)))
 '''   
#Ejercicio 8
'''Escribir una función que, dado un número de DNI,
retorne True si el número es válido y False si no lo es.
Para que un número de DNI sea válido debe tener entre 7 y
8 dígitos.
num = input('ingrese su dni')
def dni (num):
    if len(num)>=7 and len(num)<=8:  
        return True
    else:
        return False
dni_valido = dni(num)
if dni_valido == True:
    print('Su dni es correcto')
else:
    print('Su dni es incorrecto')
'''
#Ejercicio 9
'''Escribir una función que muestre por pantalla el
saludo ¡Hola amiga! cada vez que se la invoque.'''
'''
def saludo ():
    print('¡Hola Amiga!')
saludo()

'''


# Ejercicio 10
'''Escribir una función a la que se le pase una
cadena <nombre> y muestre por pantalla el saludo
¡hola <nombre>!'''

def funcion(nombre1,nombre2):  # creamos la funcion y le pasamos el parametro
    print('¡Hola',nombre1,' y ',nombre2) # imprimimos el saludo
    
funcion('Agos','Pablo') # invocamos a la funcion , y le pasamos el parametro


#Ejercicio 11
'''Escribir una función que calcule el total de una factura tras aplicarle el IVA. La función debe recibir la cantidad sin IVA y el porcentaje de IVA a aplicar, y devolver el total de la factura. Si se invoca la función sin pasarle el porcentaje de IVA, deberá aplicar un 21%.'''

# Ejercicio 12
''' Escribir un programa que pregunte al usuario por el numero de horas trabajadas y el coste por hora. Despues debe mostrar por pantalla la paga que le corresponde'''

#Ejercicio 13
''' Escribir un programa que pida al usuario su peso (en kg) y estatura (en metros), calcule el indice de masa corporal y lo almacene en una variable, y muestre por pantalla la frase " tu indice de masa corporal es <imc> " donde <imc> es el indice de masa corporal calculado redondeado con dos decimales'''