try:
    first_prompt = input("Ingresa el primer valor: ")
    a = len(first_prompt)
    second_prompt = input("Ingresa el segundo valor: ")
    b= len(second_prompt)
    print(a/b)
except ZeroDivisionError:
    print("¡No divida entre cero!")
except ValueError:
    print("Valor incorrecto.")
except:
    print("Error. Error. Error.")