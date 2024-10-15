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
class Mascota(Animal):          #Ponemos la clase de la que vamos a hereda
    """Clase para representar una mascota, hereda de la clase Animal"""
    def __init__(self, especie, edad, nombre)->None:
        super().__init__(especie, edad)     #La función super se refiere a la superclase, la cual debemos pasar los atributos de especie y edad
        self.nombre = nombre
    
    def __str__(self) ->str:
        print(f"Mascota[Nombre: {self.nombre}, Especie: {self.especie}, Edad: {self.especie}]")


class registroMascota:
    "CLase para representar un registro de mascotas."
    def __init__(self)->None:
        self.mascotas = []      #Creamos la lista para guardar el registro de las mascotas.

    def agregar_mascota(self, mascota):
        """
            Agregar una mascota al registro.

            Parameter:
            mascota(Mascota): La mascota a agregar al registro
        """
        self.mascotas.append(mascota)
    
    def listar_mascota(self):
        """
        Lista todas las mascotas registradas
        """
        if self.mascotas:
            print("Lista de mascotas \n", "="*30)
            for i, mascota in enumerate(self.mascotas, start=1):
                print(f"{i}. {mascota}")
        else:
            print("No hay mascotas registradas.")

    def editar_mascota(self, indice, nueva_mascota):
        """
        Editar una mascota en el registro.

        Parameter
            indice (int): El indice de la mascota a editar
            nueva_mascota (Mascota): la nueva información de la mascota
        """
        if indice < 0 or indice >= len(self.mascotas):
            print("No hay registro con ese indice")
        else:
            self.mascotas[indice] = nueva_mascota

    def eliminar_mascota(self, indice):
        """
        Eliminar una mascota en el registro.

        Parameter
            indice (int): El indice de la mascota a eliminar
        """
        if indice < 0 or indice >= len(self.mascotas):
            print("No hay registro con indice")
        else:
            del self.mascotas[indice]
            print("Mascota eliminada correctamente")