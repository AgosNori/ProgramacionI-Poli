vocal  = 0
vocales = ('aeiou')
palabra = input('Ingrese una palabra: ')
for letra in palabra:
    if letra.lower() in vocales:
        vocal +=1
print(vocal)