# Ejercicios de tuplas
# 1) Crear una tupla que contenga colores e imprimirla por consola
colores = ('azul','verde','amarillo','lila')
print(colores)

# 2) Mostrar la longitud de una tupla
print('La longitud de la tupla es: ',len(colores))

# 3) Crear una tupla que contenga el dni, nombre, apellido, edad y nacionalidad (que
# sean ingresados por el usuario.

#Entradas
'''
dni = int(input('Ingrese su DNI: '))
nombre= input('Ingrese su nombre: ')
apellido = input('Ingrese su apellido: ')
edad3 = int(input('Ingrese su edad: '))
nacionalidad =input('Ingrese su nacionalidad:')

#Proceso
datos = (dni,nombre.capitalize(),apellido.capitalize(),edad3,nacionalidad.upper())
#Salidas
print(datos)
'''
# 4) Escribir un programa que pregunte al usuario su edad y
# muestre por pantalla si es mayor de edad o no. (utilizando condicionales)
'''
edad4 = int(input('Ingrese su edad:'))
if edad4 >= 18:
    print('Es mayor de edad: ')
else:
    print('Es menor de edad')
'''
# 5) Calcular el mayor y el menor, ordenarlos (como quieras).Utilizando las funciones 
'''
edad1,edad2 = 12,13
mayor = max(edad1,edad2)
menor = min(edad1,edad2)
print(menor,mayor)
'''

# 6)Escribir un programa que almacene la cadena de caracteres
#contraseña en una variable, pregunte al usuario por la contraseña e
#imprima por pantalla si la contraseña introducida por el usuario coincide
#con la guardada en la variable sin tener en cuenta mayúsculas y minúsculas.
'''
contra = 'contraseña'
contraseña = input('Ingrese una contraseña: ')
if contraseña == contra:
    print('La clave ingresada coincide')
else:
    print('No coincide')
'''

# 7) Escribir un programa que pida al usuario un número entero y muestre
#por pantalla si es par o impar
'''
num = int(input('Ingrese un numero entero: '))
resultado = num % 2
if resultado == 0:
    print('Es par')
else:
    print('Es impar')
'''

#8) Para tributar un determinado impuesto se debe ser mayor de 16 años
#y tener unos ingresos iguales o superiores a 1000 € mensuales.
#Escribir un programa que pregunte al usuario su edad y sus ingresos mensuales
#y muestre por pantalla si el usuario tiene que tributar o no.
'''
edad8 = int(input('Ingrese su edad: '))
ingresos = int(input('Ingrese sus ingresos mensuales: '))
if edad8 > 16 and ingresos >=1000:
    print('Debe tributar')
else:
    print('No tributa')
'''             

#9) Escribir un programa para una empresa que tiene salas de juegos para todas las
#edades y quiere calcular de forma automática el precio que debe cobrar a sus clientes
#por entrar. El programa debe preguntar al usuario la edad del cliente y mostrar el precio
#de la entrada. Si el cliente es menor de 4 años puede entrar gratis, si tiene entre 4 y 18
#años debe pagar 5$ y si es mayor de 18 años, 10$.
'''
edad9= int(input('Ingrese su edad :'))
if edad9 < 4:
    print('Entra gratis')
elif edad9 >= 4 and edad9 < 18:
    print('Debe abonar 5$')
else:
    print('Debe abonar 10$')
'''

# 10)La pizzería Bella Napoli ofrece pizzas vegetarianas y no vegetarianas a sus clientes.
#Los ingredientes para cada tipo de pizza aparecen a continuación.
#Ingredientes vegetarianos: Pimiento y tofu.
#Ingredientes no vegetarianos: Peperoni, Jamón y Salmón.
#Escribir un programa que pregunte al usuario si quiere una pizza vegetariana o no,
#y en función de su respuesta le muestre un menú con los ingredientes disponibles
#para que elija. Solo se puede eligir un ingrediente además de la mozzarella y el
#tomate que están en todas la pizzas. Al final se debe mostrar por pantalla si la pizza
#elegida es vegetariana o no y todos los ingredientes que lleva.
'''
# Entradas
vegetariana = ('pimiento','tofu')
no_vegetariana = ('peperoni','jamon','salmon')
pizza = int(input('Ingrese cual desea : 1.vegetariana o 2.no vegetariana: '))
#Procesos y salidas
if pizza == 1:
    print(vegetariana)
    ingrediente = input('elija un ingrendiente:')
    if ingrediente == 'pimiento' or ingrediente == 'tofu':
        print('Su pizza es vegetariana y los ingredientes son: tomate, mozzarella y ',ingrediente)
elif pizza == 2:
    print(no_vegetariana)
    ingrediente = input('elija un ingrendiente:')
    if ingrediente == 'peperoni' or ingrediente == 'jamon' or ingrediente == 'salmon':
        print('Su pizza es no vegetariana y los ingredientes son: tomate, mozzarella y ',ingrediente)

'''
# 11) Una panadería vende barras de pan a 3.49€ cada una.
#El pan que no es el día tiene un descuento del 60%.
#Escribir un programa que comience leyendo el número de
#barras vendidas que no son del día. Después el programa
#debe mostrar el precio habitual de una barra de pan, el
#descuento que se le hace por no ser fresca y el coste final total.

#Entradas
barras = int(input('Ingrese la cant de barras vendidas (que no son del dia):'))
#Procesos
precio=20
descuento = precio*0.60
precio_total = precio*barras
precio_desc= precio_total-descuento
#Salidas
print('Precio total: ',precio_total)
print('Desc: ',descuento)
print('Precio a pagar: ',precio_desc)




#12) Los teléfonos de una empresa tienen el siguiente formato prefijo-caracteristica-numero
#donde el prefijo es el código del país +54, y la extensión tiene 6 dígitos
#(por ejemplo +54-2964-561232). Escribir un programa que pregunte por un
#número de teléfono (ingresando 10 digitos) y muestre por pantalla el número con el prefijo.
'''
prefijo = input('Ingrese el prefijo de su pais (por ejemplo +54):')
numero =input('Ingrese su numero de telefono :')
print('Su numero de telefono es: ',prefijo+'-'+numero)
'''
# Ejercicio 13
'''
Escribir un programa que almacene las asignaturas de un curso (por ejemplo Matemáticas,
Física, Química, Historia y Lengua) en una tupla, pregunte al usuario la nota que ha sacado
en cada asignatura, y después las muestre por pantalla con el mensaje En <asignatura> has
sacado <nota> donde <asignatura> es cada una des las asignaturas de la lista y <nota> cada una
de las correspondientes notas introducidas por el usuario.'''
# para cargar 2 o mas materias ( ejercicios de las materias)
'''
asignatura = input('ingrese una materia: ')
nota= float(input('Ingrese la nota:'))
materia =(asignatura)
print('En ',materia,'has sacado ',nota)'''