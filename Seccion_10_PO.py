
##########################################################################
#################-PROGRAMACION_ORIENTADA_A_OBJETOS-############_PO_#######
##########################################################################
#OBJETOS
#Abstraer objetos de la vida real al sistema

#Entidad: Auto
#Atributos: Marca, Placa, Color
#Clase: Plano o plantilla que describe como debe ser un objeto.

#Clases
    #Atributos:
        #-Especie
        #-Edad
    #Métodos:
        #-Hablar
        #-Correr

#Objetos
    #Animal1:
        #*Perro
        #*1 Año

    #Animal2:
        #*Gato
        #*6 Meses


help(str)   #Trae la documentación de la clase str en Python

###Clases - Atributos
class Animal:
    especie = ""        #Atributo
    edad = 0            #Atributo
    pass

perro = Animal()        #Creamos el objeto de la clase Animal
perro.especie = "Perro"
perro.edad = "1 Año"
print(perro)               #Trae información. Pertenece al objeto Animal y que es un objeto
print(perro.especie)       #Trae información. Valor "Perro" 

gato = Animal()
gato.especie = "Gato"
gato.edad = "6 Meses"
print(gato)               #Trae información. Pertenece al objeto Animal y que es un objeto
print(gato.especie)       #Trae información. Valor "Gato" 

print(type(perro))          #Trae el tipo de dato de perro

###Metodos y Atributos de instancias
class Animal:
    #Constructor
    def __init__(self, especie, edad)->None:    
        self.especie = especie              #Creamos los atributos de instancia
        self.edad = edad

    #Metodo para mostrar información del Animal
    def info(self):
        print(f"Especie: {self.especie}, Edad: {self.edad}")

animal1 = Animal("Perro", "1 Año")
animal2 = Animal("Gato", "6 Meses")

print(animal1.especie)       #Trae información. Valor "Perro" 
print(animal2.especie)       #Trae información. Valor "Gato" 
#print(Animal.especie)       #Con los atributos de instancia no podemos acceder de esta forma.

animal1.info()       #Trae información. Valor "Perro" 
animal2.info()       #Trae información. Valor "Gato" 


###Herencia
#Desde una clase hija podemos heredar el contructor, los atributos y los metodos de una clase padre.

#EJEMPLO:
#Clase Animal
class Animal:
    #Constructor
    def __init__(self, especie, edad)->None:    
        self.especie = especie              #Creamos los atributos de instancia
        self.edad = edad

    #Metodo para mostrar información del Objeto Animal
    def __str__(self) ->str:
        print(f"Animal[Especie: {self.especie}, Edad: {self.especie}]")

#Clase Mascota
class Mascota(Animal):          #Ponemos la clase de la que vamos a heredar
    def __init__(self, especie, edad, nombre)->None:
        super().__init__(especie, edad)     #La función super se refiere a la superclase, la cual debemos pasar los atributos de especie y edad
        self.nombre = nombre
    def info(self):
        print(f"Nombre: {self.nombre}, Especie {self.especie}, Edad {self.edad}")
    def __str__(self) ->str:
        print(f"Mascota[Nombre: {self.nombre}, Especie: {self.especie}, Edad: {self.especie}]")

mascota = Mascota("Perro", "2 Años", "Bobby")
print(mascota)                  #
mascota.info()                   

###Polimorfismo
#Capacidad de los objetos de diferentes clases de responder al mismo mensaje de manera distinta.

#EJEMPLO:
#Clase Animal
class Animal:
    #Constructor
    def __init__(self, especie, edad)->None:    
        self.especie = especie              #Creamos los atributos de instancia
        self.edad = edad

    #Metodo para mostrar información del Objeto Animal
    def __str__(self) ->str:
        print(f"Animal[Especie: {self.especie}, Edad: {self.especie}]")

#Clase Mascota
class Mascota(Animal):          #Ponemos la clase de la que vamos a heredar
    def __init__(self, especie, edad, nombre)->None:
        super().__init__(especie, edad)     #La función super se refiere a la superclase, la cual debemos pasar los atributos de especie y edad
        self.nombre = nombre
    def hablar(self):
        pass

    def __str__(self) ->str:
        print(f"Mascota[Nombre: {self.nombre}, Especie: {self.especie}, Edad: {self.especie}]")

#Polimorfismo Heredamos un método de la superclase Mascota para que nos responda de forma distinta.
class Perro(Mascota):
    def hablar(self):               #Reescribimos el método de la clase Mascota
        return "Woof!"
class Gato(Mascota):
    def hablar(self):
        return "Miau!"              #Reescribimos el método de la clase Mascota
        
p = Perro("Perro", "1 Año", "Bobby")
g = Gato("Gato", "1 Año", "Pelusa")

print(p.hablar())
print(g.hablar())


###Encapsulación.
#Nos permite ocultar los detalles de la implementación de una clase
#En Python no  exiten palabras claves para ocultar atributos o ponerlos públicos o privados.
#En Pyhton podemos ocultar los atrobutos poniendo barra baja "_"
# _ Hace al atributo privado
# __ 

#EJEMPLO
#Clase Animal
class Animal:
    #Constructor
    def __init__(self, especie, edad)->None:    
        self.especie = especie              #Creamos los atributos de instancia
        self.edad = edad

    #Metodo para mostrar información del Objeto Animal
    def __str__(self) ->str:
        print(f"Animal[Especie: {self.especie}, Edad: {self.especie}]")

#Clase Mascota
class Mascota(Animal):          #Ponemos la clase de la que vamos a heredar
    def __init__(self, especie, edad, nombre)->None:
        super().__init__(especie, edad)     #La función super se refiere a la superclase, la cual debemos pasar los atributos de especie y edad
        self.__nombre = nombre        #Encapsulamiento Hacemos privado el atributo "nombre"
    
    #Metodos para modificar el valor de un atributo privado / "nombre"
    def get_nombre(self):
        return self.__nombre
    
    def set_nombre(self, nombre):
        self.__nombre = nombre

    def __str__(self) ->str:
        print(f"Mascota[Nombre: {self.__nombre}, Especie: {self.especie}, Edad: {self.especie}]")


