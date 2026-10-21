ARCHIVO = "prestamos.txt"


def agregar_prestamo(libro, prestatario, fecha):
    with open(ARCHIVO, "a", encoding="utf-8") as archivo:
        archivo.write(f"{libro} | {prestatario} | {fecha}\n")


libro = input("Nombre del libro: ")
prestatario = input("Nombre del prestatario: ")
fecha = input("Fecha del préstamo (dd/mm/aaaa): ")

agregar_prestamo(libro, prestatario, fecha)
print("Préstamo registrado correctamente")