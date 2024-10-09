lista_productos = []
producto = ''

producto = input("Ingrese el nombre del producto: (escriba 'echo' para terminar): ")

while producto.lower() != 'echo':
    producto = input("Ingrese el nombre del producto: (escriba 'echo' para terminar): ")
    lista_productos.append(producto)

print("\n Lista de productos")
contador = 1
indice = 0

while indice < len(lista_productos):
    print(f"{contador}.{lista_productos[indice]}")
    indice += 1
    contador +=1