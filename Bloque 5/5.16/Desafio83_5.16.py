estudiantes = ["Ana", "Diego", "Lucía", "Luis", "Marta", "Pedro", "Sofía", "Tomás"]


def busqueda_binaria(lista, nombre):
    inicio = 0
    fin = len(lista) - 1
    while inicio <= fin:
        medio = (inicio + fin) // 2
        if lista[medio] == nombre:
            return medio
        if lista[medio] < nombre:
            inicio = medio + 1
        else:
            fin = medio - 1
    return -1


def buscar_estudiante(lista, nombre):
    posicion = busqueda_binaria(lista, nombre)
    if posicion != -1:
        print(f"{nombre} está en la posición {posicion}")
    else:
        print(f"{nombre} no se encuentra en la lista")


buscar_estudiante(estudiantes, "Marta")
buscar_estudiante(estudiantes, "Carlos")