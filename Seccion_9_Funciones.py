
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


#Parametro y Variable con el mismo nombre: SOMBREADO
#Es posible tener una variable con el mismo nombre del parámetro de la función.
#El siguiente código muestra un ejemplo de esto:

def message(number):
    print("Ingresa un número:", number)

number = 1234
message(1)
print(number)


#Una situación como la anterior, activa un mecanismo denominado sombreado:
#El parámetro x sombrea cualquier variable con el mismo nombre, pero...
#... solo dentro de la función que define el parámetro.
#El parámetro llamado number es una entidad completamente diferente de la variable llamada number.
#Esto significa que el código anterior producirá la siguiente salida:

    ##Ingresa un número: 1
    ##1234


#Paso de parámetros posicionales
#La técnica que asigna cada argumento al parámetro correspondiente, es llamada paso de parámetros posicionales, 
#los argumentos pasados de esta manera son llamados argumentos posicionales.

def my_function(a, b, c):
    print(a, b, c)

my_function(1, 2, 3)


#Paso de argumentos con palabra clave
#Python ofrece otra manera de pasar argumentos, donde el significado del argumento está definido por su nombre, no su posición, 
# a esto se le denomina paso de argumentos con palabra clave.
#Observa el siguiente código:

def introduction(first_name, last_name):
    print("Hola, mi nombre es", first_name, last_name)

introduction(first_name = "James", last_name = "Bond")
introduction(last_name = "Skywalker", first_name = "Luke")

#no se debe de utilizar el nombre de un parámetro que no existe.

#Combinar argumentos posicionales y de palabra clave
#Es posible combinar ambos tipos si se desea, solo hay una regla inquebrantable: 
# se deben colocar primero los argumentos posicionales y después los de palabra clave.
def adding(a, b, c):
    print(a, "+", b, "+", c, "=", a + b + c)

adding(c = 1, a = 2, b = 3)
#Sé cuidadoso, ten cuidado de no cometer errores. Si se intenta pasar mas de un valor a un argumento, ocurrirá un error y se mostrará lo siguiente:
adding(3, a = 1, b = 2)


#Funciones parametrizadas: más detalles
def introduction(first_name, last_name="González"):
    print("Hola, mi nombre es", first_name, last_name)

introduction("Jorge", "Pérez")
    ##Hola, mi nombre es Jorge Pérez

introduction("Enrique")
    ##Hola, mi nombre es Enrique González

introduction(first_name="Guillermo")
    ##Hola, mi nombre es Guillermo González

introduction()
    ##TypeError: introduction() missing 1 required positional argument: 'first_name'

#Si solo se especifica un argumento de palabra clave, el restante tomará el valor por default:



#RETURN
#return sin una expresión
#La primera consiste en la palabra reservada en sí, sin nada que la siga.
#Cuando se emplea dentro de una función, provoca la terminación inmediata de la ejecución de la función, y un retorno instantáneo (de ahí el nombre) al punto de invocación.
#Nota: si una función no está destinada a producir un resultado, emplear la instrucción returnno es obligatorio, se ejecutará implícitamente al final de la función.

def happy_new_year(wishes = True):
    print("Tres...")
    print("Dos...")
    print("Uno...")
    if not wishes:
        return
    
    print("¡Feliz año nuevo!")

#return con una expresión
#Existen dos consecuencias de usarla:
#Provoca la terminación inmediata de la ejecución de la función (nada nuevo en comparación con la primer variante).
#Además, la función evaluará el valor de la expresión y lo devolverá (de ahí el nombre una vez más) como el resultado de la función.

def boring_function():
    return 123

x = boring_function()

print("La función boring_function ha devuelto su resultado. Es:", x)


#Efectos y resultados: listas y funciones
#¿Se puede enviar una lista a una función como un argumento?
def list_sum(lst):
    s = 0
    
    for elem in lst:
        s += elem
    
    return s
print(list_sum([5, 4, 3]))
#12

print(list_sum(5))
#TypeError: 'int' object is not iterable
#Esto se debe al hecho de que el bucle for no puede iterar un solo valor entero.


#¿Puede una lista ser el resultado de una función?
def strange_list_fun(n):
    strange_list = []
    
    for i in range(0, n):
        strange_list.insert(0, i)
    
    return strange_list

print(strange_list_fun(5))
#[4, 3, 2, 1, 0]
#¡Si, por supuesto! Cualquier entidad reconocible por Python puede ser un resultado de función.


#LABORATORIO 1
#Tu tarea es escribir y probar una función que toma un argumento (un año) y devuelve True si el año es un año bisiesto, o False si no lo es.
#Parte del esqueleto de la función ya está en el editor.
#Nota: también hemos preparado un breve código de prueba, que puedes utilizar para probar tu función.
#El código utiliza dos listas: una con los datos de prueba y la otra con los resultados esperados. El código te dirá si alguno de tus resultados no es válido.

def is_year_leap(year):
  """Determina si un año es bisiesto.

  Args:
    year: El año a evaluar.

  Returns:
    True si el año es bisiesto, False en caso contrario.
  """

  # Un año es bisiesto si es divisible por 4, pero no por 100, a menos que también sea divisible por 400.
  if year % 4 == 0 and (year % 100 != 0 or year % 400 == 0):
    return True
  else:
    return False

# Datos de prueba y verificación de resultados
test_data = [1900, 2000, 2016, 1987]
test_results = [False, True, True, False]
for i in range(len(test_data)):
  yr = test_data[i]
  print(yr,"->",end="")
  result = is_year_leap(yr)
  if result == test_results[i]:
    print("OK")
  else:
    print("Fallido")
    
    
# Para comprobar si el año 2024 es bisiesto:
resultado = is_year_leap(2024)
print(resultado)  # Imprimirá True

#LABORATORIO 2
#Tu tarea es escribir y probar una función que toma dos argumentos (un año y un mes) y devuelve el número de días del mes/año dado (mientras que solo febrero es sensible al valor year, tu función debería ser universal).
#La parte inicial de la función está lista. Ahora, haz que la función devuelva None si los argumentos no tienen sentido.


def days_in_month(month, year):
    """
    Determines the number of days in a given month and year.

    Args:
        year (int): The year.
        month (int): The month (1-12).

    Returns:
        int: The number of days in the given month and year.
    """

    # Check for February and leap year
    if month == 2 and is_leap_year(year):
        return 29
    elif month == 2:
        return 28

    # Handle other months
    if month in [1, 3, 5, 7, 8, 10, 12]:
        return 31
    else:
        return 30

def is_leap_year(year):
    """
    Checks if a given year is a leap year.

    Args:
        year (int): The year.

    Returns:
        bool: True if the year is a leap year, False otherwise.
    """
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        return "El año es Bisiesto."
    else:
        return "El año no es Bisiesto."
   # return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)

# Test cases
test_years = [1900, 2000, 2016, 1987]
test_months = [2, 2, 1, 11]
test_results = [28, 29, 31, 30]

month = int(input("Por favor ingrese el numero del mes: "))
year = int(input("Por favor ingrese el año: "))
print(is_leap_year(year))
print(f"El mes {month} tiene", days_in_month(month, year), "dias.")



#LABORATORIO 3
#Escenario
#Tu tarea es escribir y probar una función que toma tres argumentos (un año, un mes y un día del mes) y devuelve el día correspondiente del año, o devuelve None si cualquiera de los argumentos no es válido.
#Debes utilizar las funciones previamente escritas y probadas. Agrega algunos casos de prueba al código. Esta prueba es solo el comienzo.


def days_in_month(month, year):
    """
    Determines the number of days in a given month and year.

    Args:
        year (int): The year.
        month (int): The month (1-12).

    Returns:
        int: The number of days in the given month and year.
    """

    # Check for February and leap year
    if month == 2 and is_leap_year(year):
        return 29
    elif month == 2:
        return 28

    # Handle other months
    if month in [1, 3, 5, 7, 8, 10, 12]:
        return 31
    else:
        return 30

def is_leap_year(year):
    """
    Checks if a given year is a leap year.

    Args:
        year (int): The year.

    Returns:
        bool: True if the year is a leap year, False otherwise.
    """
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        return "El año es Bisiesto."
    else:
        return "El año no es Bisiesto."
   # return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)

def day_of_year(year, month, day):
    """Calcula el día del año para una fecha dada.

    Args:
        year: El año.
        month: El mes (1-12).
        day: El día del mes.

    Returns:
        El día del año.
    """

    if month >= 1 or month <= 12 or day >= 1 or day <= days_in_month(year, month):
        total_days = day
        for m in range(1, month):
            total_days += days_in_month(m, year)

        return total_days
    else:
        return"Fecha inválida"

    """
    # Validar que la fecha sea válida
    if month < 1 or month > 12 or day < 1 or day > days_in_month(year, month):
        return"Fecha inválida"

    # Sumar los días de los meses anteriores y el día del mes actual
    total_days = day
    for m in range(1, month):
        total_days += days_in_month(m, year)

    return total_days
    """

#Ingreso de datos

day = int(input("Por favor ingrese el día: "))
month = int(input("Por favor ingrese el numero del mes: "))
year = int(input("Por favor ingrese el año: "))

print(f"\nLa fecha ingresada es:  {day}-{month}-{year}")
print(f"La fecha registrada tiene", day_of_year(year, month, day), "dias")
print(is_leap_year(year))
print(f"El mes {month} tiene", days_in_month(month, year), "dias.\n")


#Prueba automatica
"""
day = 31
month = 12
year = 1999

print(f"\nLa fecha ingresada es:    ",{day},"-",{month},"-",{year})
print(f"La fecha registrada tiene", day_of_year(year, month, day), "dias")
print(is_leap_year(year))
print(f"El mes {month} tiene", days_in_month(month, year), "dias.\n")
"""


"""
month = int(input("Por favor ingrese el numero del mes: "))
year = int(input("Por favor ingrese el año: "))
print(is_leap_year(year))
print(f"El mes {month} tiene", days_in_month(month, year), "dias.")
"""



#NUMEROS PRIMOS

def is_prime(num):
	if num == 1 or num == 0:
		return False
	elif num == 2:
		return True
	else:
		for i in range (2, num):
			if num % 2 == 0:
				return False
			elif num % i == 1 and i == num-1:
				return True


for i in range(1, 20):
	if is_prime(i):
		result = is_prime(i)
		print(i,result, end=" ")