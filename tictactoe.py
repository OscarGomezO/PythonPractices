#Tu tarea es escribir un simple programa que simule jugar a tic-tac-toe (nombre en inglés) con el usuario. Para hacerlo más fácil, hemos decidido simplificar el juego. Aquí están nuestras reglas:

#La maquina (por ejemplo, el programa) jugará utilizando las 'X's.
#El usuario (por ejemplo, tu) jugarás utilizando las 'O's.
#El primer movimiento es de la maquina: siempre coloca una 'X' en el centro del tablero.
#Todos los cuadros están numerados comenzando con el 1 (observa el ejemplo para que tengas una referencia).
#El usuario ingresa su movimiento introduciendo el número de cuadro elegido. El número debe de ser valido, por ejemplo un valor entero mayor que 0 y menor que 10, y no puede ser un cuadro que ya esté ocupado.
#El programa verifica si el juego ha terminado. Existen cuatro posibles veredictos: el juego continua, el juego termina en empate, tu ganas, o la maquina gana.
#La maquina responde con su movimiento y se verifica el estado del juego.
#No se debe implementar algún tipo de inteligencia artificial, la maquina elegirá un cuadro de manera aleatoria, eso es suficiente para este juego.

#Requerimientos
#Implementa las siguientes características:
#El tablero debe ser almacenado como una lista de tres elementos, mientras que cada elemento es otra lista de tres elementos (la lista interna representa las filas) de manera que todos los cuadros puedas ser accedidos empleado la siguiente sintaxis:
#board[row][column]
#Cada uno de los elementos internos de la lista puede contener 'O', 'X', o un digito representando el número del cuadro (dicho cuadro se considera como libre).
#La apariencia de tablero debe de ser igual a la presentada en el ejemplo.
#Implementa las funciones definidas para ti en el editor.
#Para obtener un valor numérico aleatorio se puede emplear una función integrada de Python denominada randrange(). El siguiente ejemplo muestra como utilizarla (El programa imprime 10 números aleatorios del 1 al 8).
#Nota: La instrucción from-import provee acceso a la función randrange definida en un módulo externo de Python denominado random.

"""
from random import randrange

for i in range(10):
    print(randrange(8))


def DisplayBoard(board):
    # La función acepta un parámetro el cual contiene el estado actual del tablero
    # y lo muestra en la consola.

def EnterMove(board):
    # La función acepta el estado actual del tablero y pregunta al usuario acerca de su movimiento, 
    # verifica la entrada y actualiza el tablero acorde a la decisión del usuario.

def MakeListOfFreeFields(board):
    # La función examina el tablero y construye una lista de todos los cuadros vacíos.
    # La lista esta compuesta por tuplas, cada tupla es un par de números que indican la fila y columna.

def VictoryFor(board, sign):
    # La función analiza el estatus del tablero para verificar si
    # el jugador que utiliza las 'O's o las 'X's ha ganado el juego.

def DrawMove(board):
    # La función dibuja el movimiento de la máquina y actualiza el tablero.
"""

from random import randrange

def DisplayBoard(board):
    print("+-------+")
    for row in board:
        print("|", end=" ")
        for cell in row:
            print(cell, end=" | ")
        print("\n+-------+")

def EnterMove(board):
    free = False
    while not free:
        move = int(input('Enter your move: ')) - 1
        row, col = move // 3, move % 3
        if board[row][col] in 'XO':
            print('Field already occupied')
        else:
            board[row][col] = 'O'
            free = True

def MakeListOfFreeFields(board):
    free = []
    for i in range(3):
        for j in range(3):
            if board[i][j] in '123456789':
                free.append((i, j))
    return free


# Función para verificar si hay un ganador
def VictoryFor(board, sign):
    # ... (implementación)
    print("Hello")

def DrawMove(board):
    free = MakeListOfFreeFields(board)
    move = randrange(len(free))
    row, col = free[move]
    board[row][col] = 'X'

# Función principal del juego
def main():
    # Inicializar el tablero
    board = [
        ['1', '2', '3'],
        ['4', 'X', '6'],
        ['7', '8', '9']
    ]

    # Bucle principal del juego
    while True:
        DisplayBoard(board)
        EnterMove(board)
        if VictoryFor(board, 'O'):
            print('¡Has ganado!')
            break
        DrawMove(board)
        if VictoryFor(board, 'X'):
            print('¡La máquina ha ganado!')
            break
        if len(MakeListOfFreeFields(board)) == 0:
            print('¡Empate!')
            break

if __name__ == "__main__":
    main()