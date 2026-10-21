import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation


def crear_tablero(n, m):
    tablero = np.zeros((n, m), dtype=int)
    return tablero


def contar_vecinos(tablero, i, j):
    n, m = tablero.shape
    total = 0
    for di in (-1, 0, 1):
        for dj in (-1, 0, 1):
            if di == 0 and dj == 0:
                continue  # no contamos la celda misma
            ni, nj = i + di, j + dj
            if 0 <= ni < n and 0 <= nj < m:  # los bordes cuentan como celdas muertas
                total += tablero[ni, nj]
    return total


def siguiente_generacion(tablero):
    n, m = tablero.shape
    nuevo = crear_tablero(n, m)
    for i in range(n):
        for j in range(m):
            vecinos = contar_vecinos(tablero, i, j)
            if tablero[i, j] == 1:
                # Viva: sobrevive con 2 o 3 vecinos, si no muere
                if vecinos == 2 or vecinos == 3:
                    nuevo[i, j] = 1
            else:
                # Muerta: nace con exactamente 3 vecinos
                if vecinos == 3:
                    nuevo[i, j] = 1
    return nuevo


# Tablero inicial (el "parpadeador")
mi_tablero = crear_tablero(5, 5)
mi_tablero[2, 1] = 1
mi_tablero[2, 2] = 1
mi_tablero[2, 3] = 1
print(mi_tablero)

# Animación
fig, ax = plt.subplots()
imagen = ax.imshow(mi_tablero, cmap="binary")
ax.set_title("Juego de la vida - Generación 0")
ax.set_xticks([])
ax.set_yticks([])


def actualizar(frame):
    global mi_tablero
    mi_tablero = siguiente_generacion(mi_tablero)
    imagen.set_data(mi_tablero)
    ax.set_title(f"Juego de la vida - Generación {frame + 1}")
    return (imagen,)


def inicio():
    return (imagen,)


animacion = FuncAnimation(
    fig, actualizar, frames=20, init_func=inicio, interval=500, repeat=False
)
plt.show()