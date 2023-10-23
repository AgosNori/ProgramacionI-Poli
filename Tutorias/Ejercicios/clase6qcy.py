# Funciones
# Creamos la función saludo
'''
def saludo():
    return'Hola Mundo'
# guardamos en un variable la funcion
imprimir = saludo() 
print(imprimir)
'''

def saludoNomApe (nombre,apellido):
    saludo = 'Hola'+' '+nombre.capitalize()+' '+apellido
    print(saludo)
    
saludoNomApe('agos','noriega')


def nom_edad (nombre,edad):
    salida = 'El usuario '+nombre+' tiene '+edad +' años'
    print(salida)
nom_edad('agos','21')

#Variables Locales
def suma (n1,n2):
    resultado = n1 + n2
    print(resultado)
suma(12,2)
'''
Ejercicos de funciones, crear un programa  de calculadora, que
muestre un menu de opciones :
    1- Suma
    2- Resta
    3- Multiplicacion
    4- Division
    5- Potencia
tiene que elegir una opcion y realizar lo pedido.
Utilizar funciones  y  condicionales , y que solo pida
dos parametros.
'''