#Funciones de la libreria de PY

#Retorna el valor absoluto del parametro
a = -23
print(' el valor absoluto es: ', abs(a))
#Obtiene la conversion a binario
b= 0
print('El valor en binario es: ',bin(b))

# Retorna el caracter en formato de string al valor Unicode
c = 45
print('El valor unicode es: ',chr(c))

# Retorna el cociente y el resto de la division
d,e =14,4
f,g = divmod(d,e)
print('El cociente de la division es:',f,'y el resto:',g)

# Convierte la cadena de txt a un numero en coma flotante
h = '23.4'
print(float(h))

# Obtiene la conversion a hexadecimal
i = 124
print(' El valor en hexadecimal es: ',hex(i))

# Obtiene una cadena de caracteres desde la entrada
j = input('Ingrese algo:')
print(j)

# Convierte la cadena de txt a un numero entero
k ='123'
print(int(k))

# Retorna la longiitud del objeto tomado como parametro
l =12,14,16
print(len(l))

# Retorna el mayor de  los parametros tomados
m,n = 12,15
mayor =max(m,n)
print(mayor)

# Retorna el menor de los parametros tomados
o,p = 9,4
menor=min(o,p)
print(menor)

#Obtiene la conversion en octal
q = 12
print('La conversion en octal es: ',oct(q))

# Retorna el entero Unicode que representa
r = 'a'
print(ord(r))

#Retorna el valor de x elevado a y
x,y=3,2
potencia=pow(x,y)
print('El resultado de la potencia es: ',potencia)

# Retorna el numero flotante pero redondeado a tantos digitos quiera
z=4.31234
print(round(z,2))

# Retorna una version en forma de cadena de txt
u= 2,4,1
print(str(u))