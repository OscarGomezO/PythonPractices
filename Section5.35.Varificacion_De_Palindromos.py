palabra = input("Ingrese una palabra: ")

palabra_edit = palabra.lower()

palabra_edit = palabra.replace(" ", "")

palabra_invertida = palabra_edit[::-1]

if palabra_edit == palabra_invertida:
    print(f"{palabra} es un palindromo")
else:
    print(f"{palabra} no es un palindromo")