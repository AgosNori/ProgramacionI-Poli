#Entradas
precio_actual = int(input('Ingrese el precio actual: '))
#Procesos
descuento = precio_actual*0.35
monto_final=precio_actual-descuento
#Salidas
print('El precio actual de su medicamento es: ',precio_actual)
print('El monto del descuento: ', descuento)
print('El monto final con el descuento es: ',monto_final)