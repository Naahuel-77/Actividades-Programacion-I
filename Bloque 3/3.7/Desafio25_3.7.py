import numpy as np
import random
tablero = np.zeros((5, 5), dtype=int)
barcos_colocados = 0
while barcos_colocados < 3:
    fila = random.randint(0, 4)
    columna = random.randint(0, 4)
    if tablero[fila][columna] == 0:
        tablero[fila][columna] = 1
        barcos_colocados = barcos_colocados + 1
print("--- Tablero con barcos escondidos ---")
print(tablero)
def disparar(x, y):
    global tablero
    if tablero[x][y] == 1:
        print("¡Tocado! Golpeaste un barco")
    else:
        print("¡Agua! No hay barco en esa posición")
disparar (2, 3)
disparar (0, 4)
