import csv
import os

ARCHIVO = os.path.join(os.path.dirname(os.path.abspath(__file__)), "inventario.csv")


def leer_inventario():
    with open(ARCHIVO, "r", encoding="utf-8", newline="") as archivo:
        return list(csv.reader(archivo))


def escribir_inventario(filas):
    with open(ARCHIVO, "w", encoding="utf-8", newline="") as archivo:
        csv.writer(archivo).writerows(filas)


def actualizar_copias(titulo, nuevas_copias):
    filas = leer_inventario()
    encontrado = False
    for fila in filas[1:]:
        if fila[0].lower() == titulo.lower():
            fila[1] = str(nuevas_copias)
            encontrado = True
    if encontrado:
        escribir_inventario(filas)
        print(f"Se actualizaron las copias de {titulo} a {nuevas_copias}")
    else:
        print(f"El libro {titulo} no está en el inventario")


actualizar_copias("Rayuela", 7)
actualizar_copias("Ficciones", 0)
actualizar_copias("Bestiario", 5)
actualizar_copias("Fervor de Buenos Aires", 1)