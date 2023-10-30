# 1- definir una funcion max() que tome como argumento dos
#numeros y devuelva el mayor de ellos.
'''
def max(num1,num2):
    if num1> num2:
        mayor = num1
    else:
        mayor = num2
    print('el mayor de los dos numeros es: ',mayor)
    
max(38,5)

def mayor():
    num1= int(input('num1:'))
    num2= int(input('num2:'))
    result = max(num1,num2)
    return result

print('El mayor es: ',mayor())

'''


# 2- Definir una funcion max_de_tres() que tome tres numeros
#como argumento y devuelva el mayor de ellos.
'''
def max_de_tres(num1,num2,num3):
    if num1>num2 and num1> num3:
        mayor= num1
    elif num2>num1 and num2>num3:
        mayor = num2
    else:
        mayor = num3
        
    print('El mayor es: ',mayor)
max_de_tres(1,2,3)

def mayor():
    num1= int(input('num1:'))
    num2= int(input('num2:'))
    num3= int(input('num3:'))
    result = max(num1,num2,num3)
    return result

print('El mayor es: ',mayor())

'''





# 3- Definir una funcion que calcule la longitud de una tupla
#o cadena que es recibida por parametro.
'''
def calculeLongitud(tupla):
    longitud= len(tupla)
    print('La longitud es: ',longitud)

edades = (1,34,21,2)
calculeLongitud(edades)

'''



# 4- Definir una funcion inversa() que calcule la inversion
#de una cadena. Por ejemplo, la cadena "estoy probando"
#deberia devolver la cadena "odnaborp yotse"


def inversa(cadena):
    
    cadena_inversa= cadena[::-1]
    return cadena_inversa
    
txt= "hola"
cadInversa= inversa(txt)

print('Cadena original: ',txt)
print('Cadena inversa: ',cadInversa)


# 5- Definir una funcion es_palindromo() que reconoce
#palindromos ( es decir, palabras que tienen el mismo
#aspecto escritas invertidas), por ejemplo "radar".

def es_palindromo(palabra):
    if palabra == inversa(palabra):
        print('Son palindromos')
    else:
        print('No lo son')

palabraPrueba="radarsito"
es_palindromo(palabraPrueba)

# 6- Definir una funcion generar_n_caracteres() que
#tome un entero n y devuelva el caracter multiplicado por n.
#Por ejemplo: generar_n_caracteres(5,"x") deberia devolver "xxxxx".

def generar_n_caracteres(n,caracter):
    print(n*caracter)
    
generar_n_caracteres(3,"~")



# 7 -Definir un histograma procedimiento() que tome una tupla de
#numeros enteros e imprima un histograma en la pantalla.
#Ejemplo : procedimiento((2,3,4)) deberia imprimir lo siguiente
# **
# ***
# ****



# 8- Escribir un pequeño programa donde: 
# se ingrese el año en curso
# se ingrese el nombre y el año de nacimiento de tres personas
# se calcula cuantos años cumpliran durante el año en curso
# se imprime en pantalla
# 9- Definir una tupla con 10 edades de personas. Imprimir la cantidad de personas con edades superiores a 20. Puedes variar el ejercicio para que sea el usuario quien ingrese las edades.
# 10- Crear una funcion contar_vocales(), que reciba una palabra y cuente cuantas letras "a" tiene, cuantas letras "e" tiene y asi hasta completar todas las vocales.
#Se puede hacer que el usuario ingrese quien elija la palabra