from mascotas import Mascota, registroMascota

registro = registroMascota()   #Aquí vamos a guardar los datos

while True:
    menu = """---Menú ---
1. Agregar mascota
2. Listar mascota
3. Editar mascota
4. Eliminar mascota
5. Salir
Ingrese una opción: 
"""

    opcion = input(menu)
    if opcion == "1":
        nombre = input("Nombre de la mascota: ")
        especie = input("Especie de la mascota: ")
        edad = input("Edad de la mascota: ")

        mascota = Mascota(especie, edad, nombre)
        registro.agregar_mascota(mascota)

    elif opcion == "2":
        registro.listar_mascota()

    elif opcion == "3":
        indice = int(input("Ingrese indice del registro: "))
        nombre = input("Nombre de la mascota: ")
        especie = input("Especie de la mascota: ")
        edad = input("Edad de la mascota: ")

        nueva_mascota = Mascota(especie, edad, nombre)
        registro.editar_mascota(indice-1, nueva_mascota)

    elif opcion == "4":
        indice = int(input("Ingrese el indice de la mascota a eliminar: "))
        registro.eliminar_mascota(indice)

    elif opcion == "5":
        print("¡Hasta luego!")
        break
    else:
        print("opción invalida, digite un número valido. ")