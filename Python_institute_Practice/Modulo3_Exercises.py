
#######################################################################
################################---IF---###############################
#######################################################################
"""
var = int(input("Ingresa un número: "))

print(var != 55)
print(var != 99)
print(var == 100)
print(var == 101)
print(var != -5)
print(var == +123)
"""
"""
#EJEMPLO 1
#Se leen dos números
number1 = int(input("Ingresa el primer número: "))
number2 = int(input("Ingresa el segundo número: "))

# Elige el número más grande
if number1 > number2:
    larger_number = number1
else:
    larger_number = number2

# Imprime el resultado
print("El número más grande es:", larger_number)
"""
"""
#EJEMPLO 2 (CICLO)
largest_number = -999999999
number = int(input("Ingrese un número: "))
if number == -1:
    print(largest_number)
    exit()
if number > largest_number:
    largest_number = number
# Ir a la línea 02
"""
"""
#EJEMPLO 3
var = input("Ingrese el nombre de la planta: ")

if var == "ESPATIFILIO":
    print("Si, ¡El ESPATIFILIO es la mejor planta de todos los tiempos!")
    exit()
if var == "espatifilio":
    print("No, ¡quiero un gran ESPATIFILIO!")
    exit()
else:
    print("!ESPATIFILIO!, ¡No", var, "!")
"""

"""
#EJEMPLO 4
if the_weather_is_good:
    if nice_restaurant_is_found:
        have_lunch()
    else:
        eat_a_sandwich()
else:
    if tickets_are_available:
        go_to_the_theater()
    else:
        go_shopping()
"""
"""
#EJEMPLO 5
income = float(input("Introduce el ingreso anual:"))
tax = income
#
if income <= 85528:
    tax = (tax * 18 / 100) - 556.2
if income == 0:
    tax = 0
else:
    tax = 14839.2 + ((income - 85528)* 32 /100)
#

if tax <= 0:
    tax = 0
else:
    tax = tax

tax = round(tax, 0)
print("El impuesto es:", tax, "pesos")
"""

"""
#EJEMPLO 6
year = int(input("Introduce un año:"))

if year > 1582:
    if year % 4 == 0:
        print("año bisiesto")
    elif year % 100 == 0:
        print("año bisiesto")
    elif year % 400 == 0:
        print("año bisiesto")
    else:
        print("año común")
else:
    print("No dentro del período del calendario Gregoriano")
"""

"""
############################TIPS########################
#Una única sentencia if
x = 10
if x == 10: # condición
    print("x es igual a 10")  # Ejecutado si la condición es Verdadera.

#Una serie de sentencias if
x = 10
if x > 5: # primera condición
    print("x es mayor que 5")  # Ejecutado si la primera condición es Verdadera.
if x < 10: # segunda condición
    print("x is less than 10")  # Ejecutado si la segunda condición es Verdadera.
if x == 10: # tercera condición
    print("x is equal to 10")  # Ejecutado si la tercera condición es Verdadera.

#Una sentencia de if-else
x = 10
if x < 10:  # Condición
    print("x es menor que 10")  # Ejecutado si la condición es Verdadera.
else:
    print("x es mayor o igual a 10")  # Ejecutado si la condición es Falsa.

#Una serie de sentencias if seguidas de un else
x = 10
if x > 5:  # True
    print("x > 5")
if x > 8:  # True
    print("x > 8")
if x > 10:  # False
    print("x > 10")
else:
    print("se ejecutará el else")

#La sentencia if-elif-else
x = 10
if x == 10:  # True
    print("x == 10")
if x > 15:  # False
    print("x > 15")
elif x > 10:  # False
    print("x > 10")
elif x > 5:  # True
    print("x > 5")
else:
    print("else no será ejecutado")

#Sentencias condicionales anidadas
x = 10
if x > 5:  # True
    if x == 6:  # False
        print("anidado: x == 6")
    elif x == 10:  # True
        print("anidado: x == 10")
    else:
        print("anidado: else")
else:
    print("else")
############################TIPS########################
"""


#######################################################################
##############################---WHILE---##############################
#######################################################################

"""
#EJERCICIO 1
secret_number = 777
print(
"
+==================================+
| ¡Bienvenido a mi juego, muggle!  |
| Introduce un número entero       |
| y adivina qué número he          |
| elegido para ti.                 |
| Entonces,                        |
| ¿Cuál es el número secreto?      |
+==================================+
")

while secret_number:
    var = int(input("Ingrese un número: "))
    if var == secret_number:
        print("¡Bien hecho, muggle! Eres libre ahora")
        exit()
    else:
        print("¡Ja, ja! ¡Estás atrapado en mi bucle!")

"""

"""
#EJERCICIO 1
counter = 5
while counter:
    print("Dentro del bucle.", counter)
    counter -= 1
print("Fuera del bucle.", counter)

#EJERCICIO 2
# Almacena el actual número más grande aquí.
largest_number = -999999999

# Ingresa el primer valor.
number = int(input("Introduce un número o escribe -1 para detener: "))

# Si el número no es igual a -1, continuaremos
while number != -1:
    # ¿Es el número más grande que el valor de largest_number?
    if number > largest_number:
        # Sí si, se actualiza largest_number.
        largest_number = number
    # Ingresa el siguiente número.
    number = int(input("Introduce un número o escribe -1 para detener: "))

# Imprime el número más grande
print("El número más grande es:", largest_number)

####---WHILE-ELSE---###
#EJERCICIO 1
i = 1
while i < 5:
    print(i)
    i += 1
else:
    print("else:", i)  #--> 1, 2, 3, 4 else:5


#EJERCICIO 2
i = 5
while i < 5:
    print(i)
    i += 1
else:
    print("else:", i) #--> else:5
"""

#######################################################################
##############################---FOR---################################
#######################################################################

"""
#EJERCICIO 1
for i in range(10):
    print("El valor de i es actualmente", i)

#EJERCICIO 2
power = 1
for expo in range(16):
    print("2 a la potencia de", expo, "es", power)
    power *= 2

#EJERCICIO 3
for i in range(2, 1):
    print("El valor de i es actualmente", i)

#EJERCICIO 4
for i in range(2, 8, 3):
    print("El valor de i es actualmente", i)

#EJERCICIO 5
import time

for i in range(1,6):
    print(i, " Mississippi ")
    i += 1
    time.sleep(1)
    # Escribe un bucle for que cuente hasta cinco.
    # Cuerpo del bucle: imprime el número de iteración del bucle y la palabra "Mississippi".
    # Cuerpo del bucle - usar: time.sleep (1)
print("¡Listos o no, ahí voy!")
# Escribe una función de impresión con el mensaje final.


#EJERCICIO 5
# break - ejemplo

print("La instrucción break:")
for i in range(1, 6):
    if i == 3:
        break
    print("Dentro del bucle.", i)
print("Fuera del bucle.")


# continue - ejemplo

print("\nLa instrucción continue:")
for i in range(1, 6):
    if i == 3:
        continue
    print("Dentro del bucle.", i)
print("Fuera del bucle.")

#EJERCICIO 6
var = input("Ingresa una palabra: ")

while True:
    if var == "chupacabra":
        break
    else:
        var = input("Ingresa una palabra")

#EJERCICIO 7
var = input("Ingresa una palabra: ")# Indicar al usuario que ingrese una palabra
user_word = var# y asignarlo a la variable user_word.
user_word = user_word.upper()


for letter in user_word:
    if letter == "A":  # Completa el cuerpo del bucle for.
        continue
    elif letter =="E":
        continue
    elif letter =="I":
        continue
    elif letter =="O":
        continue
    elif letter =="U":
        continue
    else:
        print(letter)
        
#EJERCICIO 8
var = input("Ingresa una palabra: ")# Indicar al usuario que ingrese una palabra
user_word = var# y asignarlo a la variable user_word.
user_word = user_word.upper()


for letter in user_word:
    if letter == "A":  # Completa el cuerpo del bucle for.
        continue
    elif letter =="E":
        continue
    elif letter =="I":
        continue
    elif letter =="O":
        continue
    elif letter =="U":
        continue
    else:
        word_without_vowels = letter
    
#print(word_without_vowels)
print(word_without_vowels, end=" ")


###---FOR-ELSE---###
#EJERCICIO 1
for i in range(5):
    print(i)
else:
    print("else:", i)   #--> 0, 1, 2, 3, 4, else:4

#EJERCICIO 2
i = 111
for i in range(2, 1):
    print(i)
else:
    print("else:", i)   #-->else:111


#EJERCICIO 3
blocks = int(input("Enter the number of blocks: "))
 
height = 0
 
inlayer = 1
 
while inlayer <= blocks:
 
    height += 1
    blocks -= inlayer       #Esta línea de código funciona distinto a la de arriba y abajo?
    inlayer += 1
 
print("The height of the pyramid: ", height)


#EJERCICIO 4
for i in range(3):
    print(i, end=" ")  # Salidas: 0 1 2

for i in range(6, 1, -2):
    print(i, end=" ")  # Salidas: 6, 4, 2
"""

#EJERCICIO 5
#Crea un bucle for que cuente de 0 a 10, e imprima números impares en la pantalla. Usa el esqueleto de abajo:
"""
for i in range(1, 11):
    if i % 2 == 1:
        print(i, end=" ")
    else:
        pass
"""
#Crea un bucle while que cuente de 0 a 10, e imprima números impares en la pantalla. Usa el esqueleto de abajo:
"""
x = 1
while x < 11:
    if x % 2 == 1:
        print(x, end=" ")
    else:
        pass
    x = x+1
"""
#Crea un programa con un bucle for y una sentencia break. El programa debe iterar sobre los caracteres en una dirección de correo electrónico, salir del bucle cuando llegue al símbolo @ e imprimir la parte antes de @ en una línea. Usa el esqueleto de abajo:
"""
for ch in "john.smith@pythoninstitute.org":
    if ch == "@":
        break
    else:
        print(ch, end=" ")
        continue
"""

#Crea un programa con un bucle for y una sentenciacontinue. El programa debe iterar sobre una cadena de dígitos, reemplazar cada 0 con x, e imprimir la cadena modificada en la pantalla. Usa el esqueleto de abajo:
"""
for digit in "0165031806510":
    if digit == "0":
        print("x", end="")
        continue
    print(digit, end="")
"""

#Crear un programa que pida al usuario una lista de productos Ciclo While y listas.
#1
"""
lista_productos = []
producto = ''

while producto.lower() != 'echo':
    producto = input("Ingrese el nombre del producto: (escriba 'echo' para terminar): ")
    lista_productos.append(producto)

print("\n Lista de productos")
contador = 1
indice = 0

while indice < len(lista_productos):
    print(f"{contador}.{lista_productos[indice]}")
    indice += 1
    contador +=1
"""
#2
"""
lista_productos = []
producto = ''

while True:
    producto = input("Ingrese el nombre del producto: (escriba 'echo' para terminar): ")
    if producto.lower() == 'echo':
        break  #Break no incluye "echo" a la lista
    
    lista_productos.append(producto)

print("\n Lista de productos")
for indice, valor in enumerate(lista_productos, start=1):
    print(f"{indice}.{valor}")
"""

#Crear un codigo que pida al usuario una lista de productos, Ciclo for y Listas
"""
lista_productos = []
producto = ''

print("\n Lista de productos")
for indice, valor in enumerate(lista_productos, start=1):
    print(f"{indice}.{valor}")
"""


#######################################################################
##############################---LISTAS---#############################
#######################################################################

#LISTA VACIA 
#my_list = []

#1
"""
numbers = [10, 5, 7, 2, 1]
print("Contenido de la lista original:", numbers)  # Imprimiendo contenido de la lista original.
*Asignar un nuevo valor de 111 al primer elemento en la lista
numbers[0] = 111
print("\nPrevio contenido de la lista:", numbers)  # Imprimiendo contenido de la lista anterior.
*Copiar el valor del quinto elemento al segundo elemento
numbers[1] = numbers[4]  # Copiando el valor del quinto elemento al segundo elemento.
print("Nuevo contenido de la lista:", numbers)  # Imprimiendo el contenido de la lista actual.
*verificar la longitud actual de la lista
print("\nLongitud de la lista:", len(numbers))  # Imprimiendo la longitud de la lista.
"""

#2
"""
hat_list = [1, 2, 3, 4, 5]  # Esta es una lista existente de números ocultos en el sombrero.
# Paso 1: escribe una línea de código que solicite al usuario
var = int(input("Ingrese un número: "))
hat_list[2] = var
print("\nLa lista es:", hat_list)
# reemplazar el número de en medio con un número entero ingresado por el usuario.
# Paso 2: escribe aquí una línea de código que elimine el último elemento de la lista.
del hat_list[-1]
print("Eliminando el último elemento de la lista ...")
# Paso 3: escribe aquí una línea de código que imprima la longitud de la lista existente.
print("\nLongitud de la lista es:", len(hat_list))
print(hat_list)
"""

#2
"""
hat_list = [1, 2, 3, 4, 5]  # Esta es una lista existente de números ocultos en el sombrero.

# Paso 1: escribe una línea de código que solicite al usuario
var = int(input("Por favor ingrese un número: "))
# reemplazar el número de en medio con un número entero ingresado por el usuario.
hat_list[3] = var

# Paso 2: escribe aquí una línea de código que elimine el último elemento de la lista.
del hat_list[4]
# Paso 3: escribe aquí una línea de código que imprima la longitud de la lista existente.
print("Longitud de la lista", len(hat_list))

print(hat_list)
"""


#Inserta un número al final de la lista
#list.append(value)
#Inserta un número en cualquier lugar de la lista
#list.insert(location, value)

#EJEMPLO
"""
numbers = [111, 7, 2, 1]
print(len(numbers))
print(numbers)

###

numbers.append(4)

print(len(numbers))
print(numbers)

###

numbers.insert(0, 222)
print(len(numbers))
print(numbers)
"""


#Llenando una lista con un FOR orden ascendente METODO APEND
"""
my_list = []  # Creando una lista vacía.

for i in range(5):
    my_list.append(i + 1)

print(my_list)
"""
#Llenando una lista con un FOR orden descendente METODO INSERT
"""
my_list = []  # Creando una lista vacía.

for i in range(5):
    my_list.insert(0, i + 1)

print(my_list)
"""

#EJEMPLO1: Sumar los elementos de una lista.
"""
my_list = [10, 1, 8, 3, 5]
total = 0

for i in range(len(my_list)):
    total += my_list[i]

print(total)
"""
#EJEMPLO2: Sumar los elementos de una lista.
"""
my_list = [10, 1, 8, 3, 5]
total = 0

for i in my_list:
    total += i

print(total)
"""

#EJEMPLO3: Ordenar al contrario
"""
my_list = [10, 1, 8, 3, 5]

my_list[0], my_list[4] = my_list[4], my_list[0]
my_list[1], my_list[3] = my_list[3], my_list[1]

print(my_list)
"""
#EJEMPLO 4: Eliminar un elemento
#del my_list[0]

#EJERCICIO 3  <<<<<LOS BEATLES>>>>>
"""
# paso 1
Beatles = []
print("Paso 1:", Beatles)

# paso 2
Beatles.append("John Lennon")
Beatles.append("Paul McCartney")
Beatles.append("George Harrinson")
print("Paso 2:", Beatles)

# paso 3
for i in range(1):
    var1 = input("Ingrese un integrante de la banda: ")
    var2 = input("Ingrese otro integrante de la banda: ")
    Beatles.append(var1)
    Beatles.append(var2)

print("Paso 3:", Beatles)

# paso 4
del Beatles[-2:]
print("Paso 4:", Beatles)

# paso 5
Beatles.insert(0, "Ringo Starr")
print("Paso 5:", Beatles)
"""

#TIPS LISTAS
"""
# Las listas se pueden indexar y actualizar , por ejemplo:
my_list = [1, None, True, 'Soy una cadena', 256, 0]
print(my_list[3])  # salida: Soy una cadena
print(my_list[-1])  # salida: 0

my_list[1] = '?'
print(my_list)  # salida: [1, '?', True, 'Soy una cadena', 256, 0]

my_list.insert(0, "primero")
my_list.append("último")
print(my_list)  # outputs: ['primero', 1, '?', True, 'Soy una cadena', 256, 0, 'último']

#  Las listas pueden estar anidadas, por ejemplo:
my_list = [1, 'a', ["lista", 64, [0, 1], False]]

# Los elementos de la lista y las listas se pueden eliminar
my_list = [1, 2, 3, 4]
del my_list[2]
print(my_list)  # salida: [1, 2, 4]

del my_list  # borra la lista entera

# Las listas pueden ser iteradas mediante el uso del bucle for
my_list = ["blanco", "purpura", "azul", "amarillo", "verde"]

for color in my_list:
    print(color)

# La función len() se puede usar para verificar la longitud de la lista, 
my_list = ["blanco", "purpura", "azul", "amarillo", "verde"]
print(len(my_list))  # salida 5

del my_list[2]
print(len(my_list))  # salida 4
"""

#Una invocación típica de función tiene el siguiente aspecto: result = function(arg), mientras que una invocación típica de un método se ve así: result = data.method(arg).

#EJEMPLO 6
"""
lst = [1, 2, 3, 4, 5]
lst.insert(1, 6)
del lst[0]
lst.append(1)

print(lst)
"""

#EJEMPLO 7
""""
lst = [1, 2, 3, 4, 5]
lst_2 = []
add = 0

for number in lst:
    add += number
    lst_2.append(add)

print(lst_2)
"""

#Ordenamiento Burbuja
"""
#1
my_list = [8, 10, 6, 2, 4]  # lista a ordenar
swapped = True  # Lo necesitamos verdadero (True) para ingresar al bucle while.

while swapped:
    swapped = False  # no hay intercambios hasta ahora
    for i in range(len(my_list) - 1):
        if my_list[i] > my_list[i + 1]:
            swapped = True  # ¡ocurrió el intercambio!
            my_list[i], my_list[i + 1] = my_list[i + 1], my_list[i]

print(my_list)
"""

"""
#2
my_list = [8, 10, 6, 2, 4]  # lista a ordenar

for i in range(len(my_list) - 1):  # necesitamos (5 - 1) comparaciones
    if my_list[i] > my_list[i + 1]:  # compara elementos adyacentes
        my_list[i], my_list[i + 1] = my_list[i + 1], my_list[i]  # Si terminamos aquí, tenemos que intercambiar elementos.
print(my_list)
"""


#Metodo Sort
"""
lst = [5, 3, 1, 2, 4]
print(lst)
lst.sort()
print(lst)  # outputs: [1, 2, 3, 4, 5]
"""

#Metodo Reverse
"""
lst = [5, 3, 1, 2, 4]
print(lst)
lst.reverse()
print(lst)  # salida: [4, 2, 1, 3, 5]
"""

# AL INTERIOR DE LAS LISTAS
"""
list_1 = [1]
list_2 = list_1
list_1[0] = 2
print(list_2)

#La asignación: list_2 = list_1 copia el nombre del arreglo no su contenido. 
#En efecto, los dos nombres (list_1 y list_2) identifican la misma ubicación en la memoria de la computadora. 
#Modificar uno de ellos afecta al otro, y viceversa.
"""

#REBANADAS
# Hacer una copia nueva de una lista, o partes de una lista.
# Copia el contenido de la lista, no el nombre de la lista.
 # my_list[start:end]
"""
# Copiando la lista entera.
list_1 = [1]
list_2 = list_1[:]
list_1[0] = 2
print(list_2)

# Copiando parte de la lista.
my_list = [10, 8, 6, 4, 2]
new_list = my_list[1:3]
print(new_list)
"""
#Una rebanada de este tipo crea una nueva lista (de destino), tomando elementos de la lista de origen: los elementos de los índices desde el principio hasta el fin - 1.


#REBANADAS - índices negativos
#start es el índice del primer elemento incluido en la rebanada.
#end es el índice del primer elemento no incluido en la rebanada.
""""
my_list = [10, 8, 6, 4, 2]
new_list = my_list[1:-1]
print(new_list)
"""
#Si start especifica un elemento que se encuentra más allá del descrito por end (desde el punto de vista inicial de la lista), la rebanada estará vacía:


#REBANADAS - Continuación
#Si omites el start en tu rebanada, se supone que deseas obtener un segmento que comienza en el elemento con índice 0.
#my_list[:end]
#my_list[0:end]
""""
my_list = [10, 8, 6, 4, 2]
new_list = my_list[:3]
print(new_list)
"""

#Si omites el end en tu rebanada, se supone que deseas que el segmento termine en el elemento con el índice len(my_list)
#my_list[start:]
"""
my_list = [10, 8, 6, 4, 2]
new_list = my_list[3:]
print(new_list)
"""

#el omitir el inicio y fin crea una copia de toda la lista:
""""
my_list = [10, 8, 6, 4, 2]
new_list = my_list[:]
print(new_list)
"""

    #La instrucción del descrita anteriormente puede eliminar más de un elemento de la lista a la vez, también puede eliminar rebanadas
""""
my_list = [10, 8, 6, 4, 2]
del my_list[1:3]
print(my_list)
"""
#Elimina todos los elementos
"""
my_list = [10, 8, 6, 4, 2]
del my_list[:]
print(my_list)
"""
#La instrucción del eliminará la lista, no su contenido
"""
my_list = [10, 8, 6, 4, 2]
del my_list
print(my_list)
"""


#OPERADORES IN / ON
#capaces de revisar la lista para verificar si un valor específico está almacenado dentro de la lista o no.

#(in) verifica si un elemento dado (el argumento izquierdo) está actualmente almacenado en algún lugar dentro de la lista (el argumento derecho) - el operador devuelve True en este caso
#(on) (not in) comprueba si un elemento dado (el argumento izquierdo) está ausente en una lista - el operador devuelve True en este caso.
""""
my_list = [0, 3, 12, 8, 2]

print(5 in my_list)
print(5 not in my_list)
print(12 in my_list)
"""

#EJEMPLOS LISTAS 1 ENCONTRAR EL NÚMERO MAYOR
"""
my_list = [17, 3, 11, 5, 1, 9, 7, 15, 13]
largest = my_list[0]

for i in my_list:
    if i > largest:
        largest = i

print(largest)
"""
#EJEMPLOS LISTAS 1 ENCONTRAR EL NÚMERO MAYOR
"""
my_list = [17, 3, 11, 5, 1, 9, 7, 15, 13]
largest = my_list[0]

for i in range(1, len(my_list)):
    if my_list[i] > largest:
        largest = my_list[i]

print(largest)
"""
#EJEMPLOS LISTAS 3 ENCONTRAR EL NÚMERO MAYOR (REBANADA)
"""
my_list = [17, 3, 11, 5, 1, 9, 7, 15, 13]
largest = my_list[0]

for i in my_list[1:]:
    if i > largest:
        largest = i

print(largest)
"""

#EJEMPLOS LISTAS 3 (REBANADA)
"""
colors = ['rojo', 'verde', 'naranja']
copy_whole_colors = colors[:]  # copia la lista entera
copy_part_colors = colors[0:2]  # copia parte de la lista

sample_list = ["A", "B", "C", "D", "E"]
new_list = sample_list[2:-1]

my_list = [1, 2, 3, 4, 5]
slice_one = my_list[2: ]
slice_two = my_list[ :2]
slice_three = my_list[-2: ]

print(slice_one)  # salida: [3, 4, 5]
print(slice_two)  # salida: [1, 2]
print(slice_three)  # salida: [4, 5]
"""


#EJEMPLO LISTAS 4 CUANTOS ELEMENTOS COINCIDEN ENTRE DOS LISTAS
"""
drawn = [5, 11, 9, 42, 3, 49]
bets = [3, 7, 11, 42, 34, 49]
hits = 0

for number in bets:
    if number in drawn:
        hits += 1

print(hits)
"""


#EJEMPLO LISTAS 5 ELEMENTO ENCONTRADO EN EL INDICE - ENCONTRAR LA UBICACIÓN DE UN ELEMENTO EN UNA LISTA
"""
my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
to_find = 5
found = False

for i in range(len(my_list)):
    found = my_list[i] == to_find
    if found:
        break

if found:
    print("Elemento encontrado en el índice", i)
else:
    print("ausente")
"""

#EJEMPLO ELIMINAR DUPLICADOS
"""
my_list = [1, 2, 4, 4, 1, 4, 2, 6, 2, 9]
no_dups = []
#
for i in my_list:
    if i not in no_dups:
        #print("Encontrado")
        no_dups.append(i) 
#
print("La lista con elementos únicos:")
print(no_dups)
"""


### TIPS - LISTAS

#Si tienes una lista list_1, y la siguiente asignación: list_2 = list_1 esto no hace una copia de la lista list_1
#pero hace que las variables list_1 y list_2 apunten a la misma lista en la memoria. 
#colors = ['rojo', 'verde', 'naranja']
#copy_whole_colors = colors[:]  # copia la lista entera
#copy_part_colors = colors[0:2]  # copia parte de la lista

#copiar una lista o parte de la lista, puedes hacerlo haciendo uso de rebanadas:
#sample_list = ["A", "B", "C", "D", "E"]
#new_list = sample_list[2:-1]
#print(new_list)  # outputs: ['C', 'D']

#Utilizar índices negativos para hacer uso de rebanadas. Por ejemplo:
#sample_list = ["A", "B", "C", "D", "E"]
#new_list = sample_list[2:-1]
#print(new_list)  # outputs: ['C', 'D']

#Los parámetros start y end son opcionales al partir en rebanadas una lista: list[start:end]
#my_list = [1, 2, 3, 4, 5]
#slice_one = my_list[2: ]
#slice_two = my_list[ :2]
#slice_three = my_list[-2: ]

#print(slice_one)  # salida: [3, 4, 5]
#print(slice_two)  # salida: [1, 2]
#print(slice_three)  # salida: [4, 5]

#Puedes eliminar rebanadas utilizando la instrucción del:
#my_list = [1, 2, 3, 4, 5]
#del my_list[0:2]
#print(my_list)  # salida: [3, 4, 5]

#del my_list[:]
#print(my_list)  # delimina el contenido de la lista, genera: []

#probar si algunos elementos existen en una lista o no utilizando las palabras clave in y not in
#my_list = ["A", "B", 1, 2]

#print("A" in my_list)  # salida: True
#print("C" not in my_list)  # salida: True
#print(2 not in my_list)  # salida: False



#######################################################################
######################---LISTAS-DENTRO-DE-LISTAS-#########MATRICES#####
#######################################################################

#Arreglos
#Ejemplo #1: genera una lista de diez elementos y la rellena con cuadrados de diez números enteros que comienzan desde cero (0, 1, 4, 9, 16, 25, 36, 49, 64, 81)
#squares = [x ** 2 for x in range(10)]

#Ejemplo #2:crea un arreglo de ocho elementos que contiene las primeras ocho potencias del numero dos (1, 2, 4, 8, 16, 32, 64, 128)
#twos = [2 ** i for i in range(8)]

#Ejemplo #3:  crea una lista con solo los elementos impares de la lista squares.
#odds = [x for x in squares if x % 2 != 0 ]


#Arreglos bidimensionales - Matrices
"""
board = []

for i in range(8):
    row = [EMPTY for i in range(8)]
    board.append(row)
"""

#Arreglos bidimensionales - Matrices - Tablero de Ajedrez
""""
EMPTY = "-"
PAWN = "PEON"
ROOK = "TORRE"
KNIGHT = "CABALLO"
board = []

for i in range(8):
    row = [EMPTY for i in range(8)]
    board.append(row)

board[0][0] = ROOK
board[0][7] = ROOK
board[7][0] = ROOK
board[7][7] = ROOK
board[4][2] = KNIGHT
board[3][4] = PAWN

print(board)
"""

#Arreglos bidimensionales - Matrices - Estación Meteorologica
"""
#(h es para las horas, d para el día):
temps = [[0.0 for h in range(24)] for d in range(31)]
#
# La matriz se actualiza aquí.
#

total = 0.0             #Para la temperatura promedio mensual del mediodía
highest = -100.0        #Para la temperatura más alta durante todo el mes
hot_days = 0            #Para los días en que la temperatura al mediodía fue de al menos 20 ℃


#temperatura promedio mensual del mediodía
for day in temps:
    total += day[11]

average = total / 31
print("Temperatura promedio al mediodía:", average)

#temperatura más alta durante todo el mes
for day in temps:
    for temp in day:
        if temp > highest:
            highest = temp
print("La temperatura más alta fue:", highest)

#cuenta los días en que la temperatura al mediodía fue de al menos 20 ℃:
for day in temps:
    if day[11] > 20.0:
        hot_days += 1

print(hot_days, "fueron los días calurosos.")
"""

#Arreglos tridimensionales  -- Reserva Hotel
"""
#Primer paso: El tipo de elementos del arreglo. En este caso, sería un valor Booleano (True/False).
#Paso dos: análisis de la situación. Resume la información disponible: tres edificios, 15 pisos, 20 habitaciones.
rooms = [[[False for r in range(20)] for f in range(15)] for t in range(3)]
#asignar una habitación en el segundo edificio, en el décimo piso, habitación 14:
rooms[1][9][13] = True
#desocupar el segundo cuarto en el quinto piso ubicado en el primer edificio:
rooms[0][4][1] = False

rooms[2][14][10] = True
rooms[2][14][11] = True
rooms[2][14][12] = True
rooms[2][14][13] = True

#Verifica si hay disponibilidad en el piso 15 del tercer edificio:
vacancy = 0

for room_number in range(20):
    if not rooms[2][14][room_number]:
        vacancy += 1
"""

#TIPS Puntos Clave
"""
#La comprensión de listas te permite crear nuevas listas a partir de las existentes de una manera concisa y elegante. 
# La sintaxis de una comprensión de lista es la siguiente:
[expression for element in list if conditional]
#Es decir:
for element in list:
    if conditional:
        expression

#lista de cinco elementos con los primeros cinco números naturales elevados a la potencia de 3:
cubed = [num ** 3 for num in range(5)]
print(cubed)  # outputs: [0, 1, 8, 27, 64]

#Arreglo bidimensional
#  Una tabla de cuatro columnas y cuatro filas: un arreglo bidimensional (4x4)
table = [[":(", ":)", ":(", ":)"],
         [":)", ":(", ":)", ":)"],
         [":(", ":)", ":)", ":("],
         [":)", ":)", ":)", ":("]]
print(table)
print(table[0][0])  # outputs: ':('
print(table[0][3])  # outputs: ':)'

#Arreglo tridimensional
# Cubo - un arreglo tridimensional (3x3x3)
cube = [[[':(', 'x', 'x'],
         [':)', 'x', 'x'],
         [':(', 'x', 'x']],

        [[':)', 'x', 'x'],
         [':(', 'x', 'x'],
         [':)', 'x', 'x']],

        [[':(', 'x', 'x'],
         [':)', 'x', 'x'],
         [':)', 'x', 'x']]]
print(cube)
print(cube[0][0][0])  # outputs: ':('
print(cube[2][2][0])  # outputs: ':)'
"""

