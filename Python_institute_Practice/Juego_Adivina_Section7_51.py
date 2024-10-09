import random

print("Bienvenido al Juego de adivinar el Número ")

num_secreto = random.randint(1,100)
intentos_maximos = 10
intentos_realizados = 0

while intentos_realizados < intentos_maximos:
    intento = int(input("Adivina el número (entre 1 y 100): "))
    intentos_realizados += 1
    
    if intento == num_secreto:
        print(f"¡Felicidades! Adivinaste el número en {intentos_realizados} intentos.")
        break
    elif intento < num_secreto:
        print(f"El número es mayor. \n Te quedan {intentos_maximos-intentos_realizados} intentos.")
    else:
        print(f"El número es menor. \n Te quedan {intentos_maximos-intentos_realizados} intentos.")
        print()
        
if intentos_realizados == intentos_maximos:
    print("GAME OVER")