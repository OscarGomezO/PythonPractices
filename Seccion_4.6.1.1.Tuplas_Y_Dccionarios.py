#TUPLAS.
#Una tupla es una secuencia inmutable. 
#Las tuplas utilizan paréntesis, mientras que las listas usan corchetes, aunque también es posible crear una tupla tan solo separando los valores por comas.

tuple_1 = (1, 2, 4, 8)
tuple_2 = 1., .5, .25, .125

tuple_1 = (1, 2, 4, 8)
tuple_2 = 1., .5, .25, .125

print(tuple_1)
print(tuple_2)

#¿Cómo crear una tupla?
empty_tuple = ()

#Si se desea crear una tupla de un solo elemento, se debe de considerar el hecho de que, debido a la sintaxis (una tupla debe de poder distinguirse de un valor entero ordinario), se debe de colocar una coma al final:
one_element_tuple_1 = (1, )
one_element_tuple_2 = 1.,

#¿Cómo utilizar un tupla? 1
# no intentes modificar el contenido de la tupla ¡No es una lista!
my_tuple = (1, 10, 100, 1000)

print(my_tuple[0])
print(my_tuple[-1])
print(my_tuple[1:])
print(my_tuple[:-2])

for elem in my_tuple:
    print(elem)

#¿Cómo utilizar un tupla? 2
#La función len() acepta tuplas, y regresa el número de elementos contenidos dentro.
#El operador + puede unir tuplas (ya se ha mostrado esto antes).
#El operador * puede multiplicar las tuplas, así como las listas.
#Los operadores in y not in funcionan de la misma manera que en las listas.
my_tuple = (1, 10, 100)

t1 = my_tuple + (1000, 10000)
t2 = my_tuple * 3

print(len(t2))
print(t1)
print(t2)
print(10 in my_tuple)
print(-10 not in my_tuple)

#SALIDA
#9
#(1, 10, 100, 1000, 10000)
#(1, 10, 100, 1, 10, 100, 1, 10, 100)
#True
#True


#¿Cómo utilizar un tupla? 3
print(phone_numbers['Suzy'])
#Las claves son sensibles a las mayúsculas y minúsculas: 'Suzy' sería diferente a 'suzy'.

#Ejemplo:
dictionary = {"gato" : "chat", "perro" : "chien", "caballo" : "cheval"}
words = ['gato', 'león', 'caballo']

for word in words:
    if word in dictionary:
        print(word, "->", dictionary[word])
    else:
        print(word, "no está en el diccionario")

# Ejemplo 1:
dictionary = {
              "gato": "chat",
              "perro": "chien",
              "caballo": "cheval"
              }

# Ejemplo 2:
phone_numbers = {'jefe': 5551234567,
                 'Suzy': 22657854310
                 }

#Este tipo de formato se llama sangría francesa.

#Ejemplo 3:
dictionary = {"gato" : "chat", "perro" : "chien", "caballo" : "cheval"}
phone_numbers = {'jefe' : 5551234567, 'Suzy' : 22657854310}
empty_dictionary = {}

print("imprimiendo los diccionarios")
print(dictionary)
print(phone_numbers)
print(empty_dictionary)


#¿Cómo utilizar un diccionario? El método keys()
#¿Pueden los diccionarios ser examinados utilizando el bucle for, como las listas o tuplas?
#No, porque un diccionario no es un tipo de dato secuencial - el bucle for no es útil aquí.
#Si, porque hay herramientas simples y muy efectivas que pueden adaptar cualquier diccionario a los requerimientos del bucle for (en otras palabras, se construye un enlace intermedio entre el diccionario y una entidad secuencial temporal).
# El método retorna o regresa una lista de todas las claves dentro del diccionario.

#El método keys()
dictionary = {"gato" : "chat", "perro" : "chien", "caballo" : "cheval"}

for key in dictionary.keys():
    print(key, "->", dictionary[key])

#La función sorted()
#¿Deseas que la salida este ordenada? Solo hay que agregar al bucle for lo siguiente:
for key in sorted(dictionary.keys()):

#¿Cómo utilizar un diccionario? Los métodos item() y values()
#El método items() regresa una lista de tuplas (este es el primer ejemplo en el que las tuplas son mas que un ejemplo de si mismas) donde cada tupla es un par de cada clave con su valor.
dictionary = {"gato" : "chat", "perro" : "chien", "caballo" : "cheval"}

for spanish, french in dictionary.items():
    print(spanish, "->", french)

#El método values(), funciona de manera muy similar al de keys(), pero regresa una lista de valores.
dictionary = {"gato" : "chat", "perro" : "chien", "caballo" : "cheval"}

for french in dictionary.values():
    print(french)

#¿Cómo utilizar un diccionario? Modificar, agregar y eliminar valores
#Modificando claves existentes
dictionary = {'gato': 'minou', 'perro': 'chien', 'caballo': 'cheval'}

dictionary['gato'] = 'minou'
print(dictionary)

#Agregando nuevas claves
dictionary = {"gato" : "chat", "perro" : "chien", "caballo" : "cheval"}

dictionary['cisne'] = 'cygne'
print(dictionary)

    #método update()
dictionary = {"gato" : "chat", "perro" : "chien", "caballo" : "cheval"}

dictionary.update({"pato": "canard"})
print(dictionary)


#Eliminado una clave
#al eliminar la clave también se removerá el valor asociado. Los valores no pueden existir sin sus claves.
    #Instrucción del
dictionary = {"gato" : "chat", "perro" : "chien", "caballo" : "cheval"}

del dictionary['perro']
print(dictionary)


    #método popitem()
dictionary = {"gato" : "chat", "perro" : "chien", "caballo" : "cheval"}

dictionary.popitem()
print(dictionary)    # salida: {'gato': 'chat', 'perro': 'chien'}


#Las tuplas y los diccionarios trabajando juntos.
"""
Necesitas un programa para calcular los promedios de tus alumnos.
El programa pide el nombre del alumno seguido de su calificación.
Los nombres son ingresados en cualquier orden.
El ingresar un nombre vacío finaliza el ingreso de los datos (nota 1: ingresar una puntuación vacía generará la excepción ValueError, pero no te preocupes por eso ahora, verás cómo manejar tales casos cuando hablemos de excepciones en el segundo parte de la serie del curso).
Una lista con todos los nombre y el promedio de cada alumno debe ser mostrada al final.
Observa el código en el editor, se muestra la solución.

Ahora se analizará línea por línea:

Línea 1: crea un diccionario vacío para ingresar los datos: el nombre del alumno es empleado como clave, mientras que todas las calificaciones asociadas son almacenadas en una tupla (la tupla puede ser el valor de un diccionario, esto no es un problema).
Línea 3: se ingresa a un bucle "infinito" (no te preocupes, saldrémos de el en el momento indicado).
Línea 4: se lee el nombre del alumno aquí.
Línea 5-6: si el nombre es una cadena vacía (), salimos del bucle.
Línea 8: se pide la calificación del estudiante (un valor entero en el rango del 1-10).
Línea 9-10: si la puntuación ingresada no está dentro del rango de 0 a 10, se abandona el bucle.
Línea 12-13: si el nombre del estudiante ya se encuentra en el diccionario, se alarga la tupla asociada con la nueva calificación (observa el operador +=).
Línea 14-15: si el estudiante es nuevo (desconocido para el diccionario), se crea una entrada nueva, su valor es una tupla de un solo elemento la cual contiene la calificación ingresada.
Línea 17: se itera a través de los nombres ordenados de los estudiantes.
Línea 18-19: inicializa los datos necesarios para calcular el promedio (sum y counter).
Línea 20-22: se itera a través de la tupla, tomado todas las calificaciones subsecuentes y actualizando la suma junto con el contador.
Línea 23: se calcula e imprime el promedio del alumno junto con su nombre.
"""

school_class = {}

while True:
    name = input("Ingresa el nombre del estudiante: ")
    if name == '':
        break
    
    score = int(input("Ingresa la calificación del estudiante (0-10): "))
    if score not in range(0, 11):
	    break
    
    if name in school_class:
        school_class[name] += (score,)
    else:
        school_class[name] = (score,)
        
for name in sorted(school_class.keys()):
    adding = 0
    counter = 0
    for score in school_class[name]:
        adding += score
        counter += 1
    print(name, ":", adding / counter)