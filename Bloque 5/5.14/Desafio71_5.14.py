with open("ejemplo.txt", "w", encoding="utf-8") as f:
    f.write("Primera línea\nSegunda línea\nTercera línea")


def leer_archivo(ruta):
    archivo = None
    try:
        archivo = open(ruta, "r", encoding="utf-8")
        contenido = archivo.read()
        print(contenido)
    except FileNotFoundError:
        print(f"El archivo '{ruta}' no existe")
    finally:
        if archivo is not None:
            archivo.close()
            print(f"Archivo '{ruta}' cerrado")
        else:
            print("No había archivo que cerrar")


leer_archivo("ejemplo.txt")
leer_archivo("inexistente.txt")