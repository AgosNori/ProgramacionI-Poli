# Ejercicios de tuplas
# 1) Crear una tupla que contenga colores e imprimirla por consola
colores = ('azul','verde','amarillo','lila')
print(colores)

# 2) Mostrar la longitud de una tupla
print('La longitud de la tupla es: ',len(colores))

# 3) Crear una tupla que contenga el dni, nombre, apellido, edad y nacionalidad (que
# sean ingresados por el usuario.

#Entradas
dni = int(input('Ingrese su DNI: '))
nombre= input('Ingrese su nombre: ')
apellido = input('Ingrese su apellido: ')
edad = int(input('Ingrese su edad: '))
nacionalidad =input('Ingrese su nacionalidad:')

#Proceso
datos = (dni,nombre.capitalize(),apellido.capitalize(),edad,nacionalidad.upper())
#Salidas
print(datos)

# 4) Escribir un programa que pregunte al usuario su edad y
# muestre por pantalla si es mayor de edad o no. (utilizando condicionales)




# 5) Calcular el mayor y el menor, ordenarlos (como quieras).Utilizando las funciones 

# 6)Escribir un programa que almacene la cadena de caracteres
#contraseña en una variable, pregunte al usuario por la contraseña e
#imprima por pantalla si la contraseña introducida por el usuario coincide
#con la guardada en la variable sin tener en cuenta mayúsculas y minúsculas.

# 7) Escribir un programa que pida al usuario un número entero y muestre
#por pantalla si es par o impar

#8) Para tributar un determinado impuesto se debe ser mayor de 16 años
#y tener unos ingresos iguales o superiores a 1000 € mensuales.
#Escribir un programa que pregunte al usuario su edad y sus ingresos mensuales
#y muestre por pantalla si el usuario tiene que tributar o no.

#9) Escribir un programa para una empresa que tiene salas de juegos para todas las
#edades y quiere calcular de forma automática el precio que debe cobrar a sus clientes
#por entrar. El programa debe preguntar al usuario la edad del cliente y mostrar el precio
#de la entrada. Si el cliente es menor de 4 años puede entrar gratis, si tiene entre 4 y 18
#años debe pagar 5€ y si es mayor de 18 años, 10€.


# 10)La pizzería Bella Napoli ofrece pizzas vegetarianas y no vegetarianas a sus clientes.
#Los ingredientes para cada tipo de pizza aparecen a continuación.
#Ingredientes vegetarianos: Pimiento y tofu.
#Ingredientes no vegetarianos: Peperoni, Jamón y Salmón.
#Escribir un programa que pregunte al usuario si quiere una pizza vegetariana o no,
#y en función de su respuesta le muestre un menú con los ingredientes disponibles
#para que elija. Solo se puede eligir un ingrediente además de la mozzarella y el
#tomate que están en todas la pizzas. Al final se debe mostrar por pantalla si la pizza
#elegida es vegetariana o no y todos los ingredientes que lleva.


# 11) Una panadería vende barras de pan a 3.49€ cada una.
#El pan que no es el día tiene un descuento del 60%.
#Escribir un programa que comience leyendo el número de
#barras vendidas que no son del día. Después el programa
#debe mostrar el precio habitual de una barra de pan, el
#descuento que se le hace por no ser fresca y el coste final total.