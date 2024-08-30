#######################################################################
###############################---FUNCIONES-###########################
#######################################################################

#transformar una parte de código que se está repitiendo en una función.
"""
print("Ingresa un valor: ")
a = int(input())

print("Ingresa un valor: ")
b = int(input())

print("Ingresa un valor: ")
c = int(input())
"""

#def my_function():      #comienza con la palabra reservada def
    # cuerpo de la función
"""
def message():
    print("Ingresa un valor: ")

print("Se comienza aquí.")
message()
print("Se termina aquí.")
"""

#-Consideraciones:
#	No se debe invocar una función antes de que se haya definido.
#   Una función y una variable no pueden compartir el mismo nombre.


#Función sin Argumetnos: 
"""
def message():    # definiendo una función
    print("Hello")    # cuerpo de la función

message()    # invocación de la función

"""
#Función con argumentos:
"""
def hello(name):    # definiendo una función
    print("Hola,", name)    # cuerpo de la función


name = input("Ingresa tu nombre: ")

hello(name)    # invocación de la función
"""

#*Funciones parametrizadas
#def function(parameter):
    ###
"""
def message(number):
    print("Ingresa un número:", number)
"""




