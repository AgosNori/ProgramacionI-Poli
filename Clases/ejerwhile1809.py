dia = 0
semana= ('Lunes','Martes','Miercoles','Jueves','Viernes','Sabado','Domingo')
while dia <7:
    print('hoy es: ',semana[dia])
    dia = dia+1 # dia +=1
# Crear una variable e inicializarla con el valor 0 , imprimirla siempre
# que la variable sea menor que 6:

x= 0
while x < 6:
    print(x)
    x += 1
    
#Imprimir por pantalla los números desde el 1 hasta el 10
num = 1
while num <11:
    print(num)
    num+=1
    
# Escriba un programa que pregunte una y otra vez si
# desea continuar con el programa, siempre que se
# conteste exactamente sí ( en minúscula y con tilde)

respuesta = input('¿ Desea continuar con el programa?')
while respuesta == 'sí':
    respuesta = input('¿ Desea continuar con el programa?')
print('Nos vemos, gracias')
    
# Escriba un programa que solicite una contraseña
# ( el texto de la contraseña no es importante) y
# la vuelva a solicitar hasta que las dos contraseñas coincidan.

contraseña = input('Ingrese la contraseña: ')
contraseñaDeNuevo= input('Ingrese nuevamente: ')
while contraseña != contra:
    contraseña = input('Ingrese la contraseña: ')
    contraseñaDeNuevo= input('Ingrese nuevamente: ')
print('Contraseña correcta')   