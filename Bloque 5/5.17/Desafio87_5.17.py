import os

ARCHIVO = os.path.join(os.path.dirname(os.path.abspath(__file__)), "libros.txt")


def buscar_por_autor(autor):
    encontrados = []
    with open(ARCHIVO, "r", encoding="utf-8") as archivo:
        for linea in archivo:
            partes = linea.strip().split(" | ")
            if len(partes) == 2 and partes[1].lower() == autor.lower():
                encontrados.append(partes[0])

    if encontrados:
        print(f"Libros de {autor}:")
        for titulo in encontrados:
            print(f"- {titulo}")
    else:
        print(f"No hay coincidencias para el autor {autor}")


buscar_por_autor("Julio Cortázar")
buscar_por_autor("Isabel Allende")