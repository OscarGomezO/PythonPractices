nombre = "Oscar"
edad = 27
talla = 1.85

#1
mensaje = "Hola, me llamo %s , tengo %d y mido %.2f metros" % (nombre, edad, talla)
#%s para caracteres     %d para enteros     %f para flotantes
#2
mensaje = "Hola, me llamo %s , tengo %d y mido %.2f metros" % (nombre, edad, talla)
#3
mensaje = f"Hola, me llamo {nombre} , tengo {edad} y mido {talla:.2f} metros"

print(mensaje)