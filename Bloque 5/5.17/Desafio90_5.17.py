import os
import re
from collections import Counter

ARCHIVO = os.path.join(os.path.dirname(os.path.abspath(__file__)), "libros.txt")


def contar_palabras(ruta):
    with open(ruta, "r", encoding="utf-8") as archivo:
        texto = archivo.read().lower()
    palabras = re.findall(r"\w+", texto)
    return Counter(palabras)


def mostrar_mas_comunes(ruta, cantidad=5):
    conteo = contar_palabras(ruta)
    for palabra, veces in conteo.most_common(cantidad):
        print(f"{palabra}: {veces}")


mostrar_mas_comunes(ARCHIVO)