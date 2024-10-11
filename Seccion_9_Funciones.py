
##########################################################################
####################################-FUNCIONES-###########################
##########################################################################
#1
def saludar():
    print("Holas, desde la función saludar")

saludar()

#2
def saludar(nombre):
    print("Hola, {nombre}")

saludar("Juan")

#3
def saludar(nombre):
    return f"Hola, {nombre}"

saludar("Juan")

#4
def suma(a,b):
    return a + b

suma(2,4)

#ALCANCE
#Variables globales:
    # Podemos acceder a una variable local desde una función, pero no podemos modificar su valor desde dentro de la función.
    # Para modificar su valor, utilizamos la intrucción global "Variable".
c = 0
globals()   #Devuelve un registro de variables globales.

#Variables locales:
# Variables que están dentro de una función.
# Desde fuera de la función no podemos acceder a variables locales.

def suma(a,b):
    r = a + b

suma(10,15)

locals()    #Devulve el regisro de las variables locales.


#Variables no locales
#Son variables que estan en una función que está en otra función.
def func1():
    c = 0       #Esta es la variable no local
    def func2():
        a = 0   #Esta es la variable local
        #Para acceder al valor de la cariable c utilizamos:
        nonlocal c
        c +=1

        func2()
        print(c)

func1()

#Funcion de varios argumentos, recibe argumentos indefinidos.
#1
def args_func(*args):
    print(args)


args_func("Hola", 400, True, 45.5) #Devuelve una tupla.

#2
def suma(a,b):
    print(f"a = {a} y b = {b}")
    return a + b

suma(50,10)
suma(b = 200, a = 700)
#900

#3
def kwargs_func(**kwargs): #el ** recibe argumentos indefinidos con clave o con nombre
    print(kwargs)

kwargs_func(nombre = "Alex", a = 100, b = 200)  #Devulve un diccionario
#{'nombre': 'Alex', 'a' = 100, 'b' = 200}

#4 
def argumentos(a, *args, **kwargs):
    print(a)
    print(args)
    print(kwargs)

argumentos(500, "Hola", True, 400, nombre = "Alex", b = 50)
#500
#('Hola', True, 400)
#{'nombre': 'Alex', 'b': 500}

#Anotaciones de tipos:
#Especifica el tipo de dato que se espera en una función o variable
#Sirve para que el código sea mas legible.
#1
a: int = 400

#2
def suma(a:int, b:int) ->int:
    return a + b
suma (2,5)

#3
def saludo(nombre:str, veces:int=1) -> str:  #Si nosotros no enviamos un parametros para "veces" ponemos 1 por defecto
    return f"Hola {nombre}" * veces

#Anotaciones
# int
#str
#float
#bool
#list
#tuple


#Modulos
#1
#crear el archivo saludos.py

import random


def formato_aleatorio()->str:       #Función que devuelve un formato aleatorio
    formatos = [
        "¡Hola, {}! ¡Bienvanido!",
        "¡Es genial verte, {}!",
        "¡Saludos, {}! ¡Encantado de conocerte!"
    ]
    return random.choice(formatos)

print(formato_aleatorio())


def hola(nombre:str)->str:          #Recive un nombre y devulve un saludo con uno de los formatos de forma aleatoria
    if nombre == "":
        return "Error: nombre vacio."
    saludo = formato_aleatorio().format(nombre)
    return saludo

print(hola("Alex"))

#2  - Función holas y modulo typing - Continuación del punto anterior
def holas(nombres:list)->dict:
    saludos = {}
    for nombre in nombres:
        saludo = hola(nombre)
        saludos[nombre] = saludo
    
    return saludos

nombres = ["Alex", "Juan", "Carlos", "Pedro"]

print(holas(nombres))

#Uso de typing 
from typing import List, Dict

def holas(nombres:List)->Dict:
    saludos = {}
    for nombre in nombres:
        saludo = hola(nombre)
        saludos[nombre] = saludo


#Importar modulo
#1
#Crear el archivo main.py
import saludos

#2
#para importar una función en especifico como la función hola 
from saludos import hola, holas

#Para importar todas la funciones
from saludos import *

#3
#usar las funciones
print(hola("Alex"))

nombre = ["Juan", "Pedro", "Carlos"]
saludos = holas(nombres)

for saludo in saludos.values():
    print(saludo)


#Docstring - Documentación de funciones - Se generan utilizando triple comillas dobles
#Escribir en el buscador python pep docstring
#Ir al enlace de PEP 257 - Docstring COnventions

import random


def formato_aleatorio()->str:       #Función que devuelve un formato aleatorio
    """
    Retorna un saludo aleatorio formateado con el nombre proporcionado

    Returns:
        str: Saludo aleatorio con el formato adecuado
    """
    formatos = [
        "¡Hola, {}! ¡Bienvanido!",
        "¡Es genial verte, {}!",
        "¡Saludos, {}! ¡Encantado de conocerte!"
    ]
    return random.choice(formatos)

print(formato_aleatorio())


def hola(nombre:str)->str:          #Recive un nombre y devulve un saludo con uno de los formatos de forma aleatoria
    """
    Genera un saludo personalizado utilizando un nombre

    Args:
        nombre (str): Nombre del destinatario del saludo

    Returns:
        str: saludo personalizado.
    """
    if nombre == "":
        return "Error: nombre vacio."
    saludo = formato_aleatorio().format(nombre)
    return saludo

print(hola("Alex"))

#2  - Función holas y modulo typing - Continuación del punto anterior
def holas(nombres:list)->dict:
    """
        Genera un saludo personalizado para una lista de nombres 
        Args:
            nombre (List[str]): Lista de nombres para los cuales se generan los saludos
        Returns:
            Dict[str, str]: Diccionario donde las claves son nombres y los valores son saludos personalizados.
    """
    saludos = {}
    for nombre in nombres:
        saludo = hola(nombre)
        saludos[nombre] = saludo
    
    return saludos

nombres = ["Alex", "Juan", "Carlos", "Pedro"]

print(holas(nombres))