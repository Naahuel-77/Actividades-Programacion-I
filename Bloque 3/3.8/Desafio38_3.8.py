import os

carpeta = "documentos"
ruta = os.path.join(carpeta, "nota.txt")

os.makedirs(carpeta, exist_ok=True)


def guardar_archivo(ruta, contenido):
    with open(ruta, "w", encoding="utf-8") as archivo:
        archivo.write(contenido)


def leer_archivo(ruta):
    if not os.path.exists(ruta):
        return None
    with open(ruta, "r", encoding="utf-8") as archivo:
        return archivo.read()


guardar_archivo(ruta, "Hola, este es mi procesador de texto.\nSegunda línea del documento.")
print(f"Archivo guardado en: {ruta}")
print("Contenido:")
print(leer_archivo(ruta))
print("Archivos en la carpeta:", os.listdir(carpeta))