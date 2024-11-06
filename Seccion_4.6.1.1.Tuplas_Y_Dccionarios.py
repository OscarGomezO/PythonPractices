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
