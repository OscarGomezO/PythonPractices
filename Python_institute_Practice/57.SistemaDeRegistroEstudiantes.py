"""
Desarrolla un programa en Python para gestionar un sistema de registro de estudiantes. El sistema deberá permitir:
• Registro de Estudiantes:
• Capturar información de estudiantes desde la terminal, incluyendo nombre, edad y curso.
• Almacenar la información en un diccionario.
• Almacenamiento en una Lista:
• Guardar cada diccionario de estudiante en una lista central.
• Visualización del Registro:
• Mostrar el registro completo de estudiantes, incluyendo sus detalles como
nombre, edad y curso.
"""

from turtle import delay


registro_estudiantes = []

while True:
    print("1. Registrar Estudiante")
    print("2. Mostrar Registro")
    print("3. Salir")

    opcion = input("Seleccione una opción: ")

    if opcion == '1':
        nombre = input("Ingrese el nombre del estudiante: ")
        edad = int(input("Ingrese la edad del estudiante: "))
        curso = input("Ingrese el curso del estudiante: ")

        estudiante = {"Nombre":nombre, "Edad":edad, "Curso":curso}
        registro_estudiantes.append(estudiante)
        print("Estudiante registrado exitosamente! \n")

    elif opcion == '2':
        if registro_estudiantes:
            print("\nRegistro de estudiantes:")
            for estudiante in registro_estudiantes:
                print(f"Nombre: {estudiante["Nombre"]}, Edad: {estudiante["Edad"]}, Curso: {estudiante["Curso"]}")
        else: 
            print("El registro está vacio. Registre un estudiante primero.\n")

    elif opcion == '3':
        print("\nSaliendo del programa ...")
        delay(3)
        print("¡Hasta luego!")
        break

    else:
        print("Opción no valida, intentelo de nuevo.\n")



