import os

ARCHIVO = os.path.join(os.path.dirname(os.path.abspath(__file__)), "prestamos.txt")


def leer_prestamos():
    with open(ARCHIVO, "r", encoding="utf-8") as archivo:
        return [linea.strip() for linea in archivo if linea.strip()]


def escribir_prestamos(prestamos):
    with open(ARCHIVO, "w", encoding="utf-8") as archivo:
        for prestamo in prestamos:
            archivo.write(prestamo + "\n")


def mostrar_prestamos(prestamos):
    for i, prestamo in enumerate(prestamos, start=1):
        print(f"{i}. {prestamo}")


def eliminar_prestamo():
    prestamos = leer_prestamos()
    if not prestamos:
        print("No hay préstamos registrados")
        return

    print("Préstamos actuales:")
    mostrar_prestamos(prestamos)

    try:
        numero = int(input("Número de préstamo a eliminar: "))
    except ValueError:
        print("Debe ingresar un número")
        return

    if 1 <= numero <= len(prestamos):
        eliminado = prestamos.pop(numero - 1)
        escribir_prestamos(prestamos)
        print(f"Se eliminó: {eliminado}")
    else:
        print("Número fuera de rango")


eliminar_prestamo()