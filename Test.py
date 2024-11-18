onemilla = 1609.344		#Una milla a metros
onegallon = 3.785411784	#Un galón a litros

def liters_100km_to_miles_gallon(liters):
    result = (100 * onegallon) / (liters * (onemilla/1000))
    return result

def miles_gallon_to_liters_100km(miles):
    result = (100 * onegallon)/ (miles * (onemilla/1000))
    return result

print(liters_100km_to_miles_gallon(3.9))
print(liters_100km_to_miles_gallon(7.5))
print(liters_100km_to_miles_gallon(10.))
print(miles_gallon_to_liters_100km(60.3))
print(miles_gallon_to_liters_100km(31.4))
print(miles_gallon_to_liters_100km(23.5))

                     
#print(is_prime(1))


#########################-TUPLAS-#########################################
#Tuplas PUNTOS CLAVE.
#1 Las Tuplas son colecciones de datos ordenadas e inmutables. Se puede pensar en ellas como listas inmutables. Se definen con paréntesis:
my_tuple = (1, 2, True, "una cadena", (3, 4), [5, 6], None)
print(my_tuple)

#2 Crear tupla vacia
empty_tuple = ()
print(type(empty_tuple))    # salida: <class 'tuple'>

#3 tupla con un solo elemento
one_elem_tuple_1 = ("uno", )    # Paréntesis y una coma.
one_elem_tuple_2 = "uno",       # Sin paréntesis, solo la coma.
#Si se elimina la coma, Python creará una variable no una tupla:

#4 acceder los elementos de la tupla al indexarlos:
my_tuple = (1, 2.0, "cadena", [3, 4], (5, ), True)
print(my_tuple[3])    # salida: [3, 4]

#5 Las tuplas son immutable
my_tuple = (1, 2.0, "cadena", [3, 4], (5, ), True)
my_tuple[2] = "guitarra"    # La excepción TypeError será lanzada.

#6 Eliminar una tupla por completo
my_tuple = 1, 2, 3, 
del my_tuple
print(my_tuple)    # NameError: name 'my_tuple' is not defined

#7 (Ejemplo 1) Puedes iterar a través de los elementos de una tupla con un bucle 
tuple_1 = (1, 2, 3)
for elem in tuple_1:
    print(elem)

# (Ejemplo 2) verificar si un elemento o no esta presente en la tupla
tuple_2 = (1, 2, 3, 4)
print(5 in tuple_2)
print(5 not in tuple_2)

# (Ejemplo 3) emplear la función len() para verificar cuantos elementos existen en la tupla 
tuple_3 = (1, 2, 3, 5)
print(len(tuple_3))

# (Ejemplo 4) unir o multiplicar tuplas:
tuple_4 = tuple_1 + tuple_2
tuple_5 = tuple_3 * 2

# Crear una tupla utilizando la función integrada de Python tuple()
# Es útil cuando se desea convertir un iterable (por ejemplo, una lista, rango, cadena, etcétera) en una tupla
my_tuple = tuple((1, 2, "cadena"))
print(my_tuple)

my_list = [2, 4, 6]
print(my_list)    # salida: [2, 4, 6]
print(type(my_list))    # salida: <class 'list'>
tup = tuple(my_list)
print(tup)    # salida: (2, 4, 6)
print(type(tup))    # salida: <class 'tuple'>

#Cuando deseemos convertir un iterable en una lista, empleamos la función list()
tup = 1, 2, 3, 
my_list = list(tup)
print(type(my_list))    # salida: <class 'list'>


#########################-DICCIONARIOS-#########################################
#1  Los diccionarios son *colecciones indexadas de datos, mutables y desordenadas. (*En Python 3.6x los diccionarios están ordenados de manera predeterminada.
# Cada diccionario es un par de clave 
my_dictionary = {
    key1: value1,
    key2: value2,
    key3: value3,
    }

#2 Acceder a un elemento del diccionario.
pol_esp_dictionary = {
    "kwiat": "flor",
    "woda": "agua",
    "gleba": "tierra"
    }

item_1 = pol_esp_dictionary["gleba"]    # Ejemplo 1.
print(item_1)    # salida: tierra

item_2 = pol_esp_dictionary.get("woda")    # Ejemplo 2.
print(item_2)    # salida: agua

#3 Cambiar el valor asociado a una clave específica.
pol_esp_dictionary = {
    "zamek" : "castillo",
    "woda"  : "agua",
    "gleba" : "tierra"
    }

pol_esp_dictionary["zamek"] = "cerradura"
item = pol_esp_dictionary["zamek"]    
print(item)  # salida: cerradura

#4 Agregar o eliminar una clave (junto con su valor asociado)
phonebook = {}    # un diccionario vacío

phonebook["Adán"] = 3456783958    # crear/agregar un par clave-valor
print(phonebook)    # salida: {'Adán': 3456783958}

del phonebook["Adán"]
print(phonebook)    # salida: {}

#Insertar un elemento a un diccionario utilizando el método update()
pol_esp_dictionary = {"kwiat": "flor"}

pol_esp_dictionary.update({"gleba": "tierra"})
print(pol_esp_dictionary)    # salida: {'kwiat': 'flor', 'gleba': 'tierra'}

#Eliminar el ultimo elemento con el método popitem()
pol_esp_dictionary = {"kwiat": "flor"}

pol_esp_dictionary.popitem()
print(pol_esp_dictionary)    # salida: {'kwiat': 'flor'}

#5 Bucle for para iterar a través del diccionario
pol_esp_dictionary = {
    "zamek": "castillo",
    "woda": "agua",
    "gleba": "tierra"
    }

for item in pol_esp_dictionary:
    print(item) 

#6 Examinar los elementos (claves y valores) del diccionario empleando el método items()
pol_esp_dictionary = {
    "zamek" : "castillo",
    "woda"  : "agua",
    "gleba" : "tierra"
    }

for key, value in pol_esp_dictionary.items():
    print("Pol/Esp ->", key, ":", value)

#Para comprobar si una clave existe en un diccionario, clave reservada in
pol_esp_dictionary = {
    "zamek" : "castillo",
    "woda"  : "agua",
    "gleba" : "tierra"
    }

if "zamek" in pol_esp_dictionary:
    print("Si")
else:
    print("No")

#8 Emplear la palabra reservada "del" para eliminar un elemento, o un diccionario entero.
#Para eliminar todos los elementos de un diccionario se debe emplear el método clear()
pol_esp_dictionary = {
    "zamek" : "castillo",
    "woda"  : "agua",
    "gleba" : "tierra"
    }

print(len(pol_esp_dictionary))    # salida: 3
del pol_esp_dictionary["zamek"]    # eliminar un elemento
print(len(pol_esp_dictionary))    # salida: 2

pol_esp_dictionary.clear()   # eliminar todos los elementos
print(len(pol_esp_dictionary))    # salida: 0

del pol_esp_dictionary    # elimina el diccionario

#9 Para copiar un diccionario, emplea el método copy()
pol_esp_dictionary = {
    "zamek" : "castillo",
    "woda"  : "agua",
    "gleba" : "tierra"
    }

copy_dictionary = pol_esp_dictionary.copy()


#EJERCICIOS
#1 Completa el código para emplear correctamente el método count() para encontrar la cantidad de 2 duplicados en la tupla siguiente.
tup = 1, 2, 3, 2, 4, 5, 6, 2, 7, 2, 8, 9
duplicates = tup.count(2)

print(duplicates)    # salida: 4

#2 Escribe un programa que "una" los dos diccionarios (d1 y d2) para crear uno nuevo (d3).
d1 = {'Adam Smith': 'A', 'Judy Paxton': 'B+'}
d2 = {'Mary Louis': 'A', 'Patrick White': 'C'}
d3 = {}

for item in (d1, d2):
    d3.update(item)

print(d3)

#3 Escribe un programa que convierta la lista my_list en una tupla.
my_list = ["car", "Ford", "flower", "Tulip"]

t = tuple(my_list)
print(t)

#4 Cual es la salida del siguiente código?
colors = {
    "blanco": (255, 255, 255),
    "gris": (128, 128, 128),
    "rojo": (255, 0, 0),
    "verde": (0, 128, 0)
    }

for col, rgb in colors.items():
    print(col, ":", rgb)

#white : (255, 255, 255)
#grey : (128, 128, 128)
#red : (255, 0, 0)
#green : (0, 128, 0)

