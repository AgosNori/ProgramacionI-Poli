# Ejercicios entradas para el cine
# Entradas
'''
edad = int(input('Ingrese la edad: '))
#Procesos Y salidas
if edad > 5 and edad <= 13:
    precio_entrada = 500
    print('precio final: ',precio_entrada)
elif edad > 13 and edad <= 18:
    precio_entrada = 800
    print('precio final: ',precio_entrada)
elif edad > 18:
    precio_entrada = 1000
    print('precio final: ',precio_entrada)
else:
    print('No cobra entrada')
'''
print('Juego de adivinanza')
musica = ("cuarteto")
print('Ayuditasss!!')
print('Comienza con la letra ',musica[0])
print('Contiene ',len(musica),' letras')
print('Es un estilo de musica muy escuchado en Cordoba')
print('Finaliza con la letra ',musica[7])
musica_ingresada = input('Ingrese su respuesta: ')
if musica_ingresada == musica:
    print('Ganaste')
else:
    print('Perdiste la palabra era: ',musica)