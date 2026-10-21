estudiantes = [
    ("Ana", 8.5),
    ("Luis", 7.2),
    ("Marta", 9.1),
    ("Pedro", 6.8),
    ("Sofía", 8.9),
]


def ordenar_por_seleccion(lista):
    n = len(lista)
    for i in range(n - 1):
        indice_mayor = i
        for j in range(i + 1, n):
            if lista[j][1] > lista[indice_mayor][1]:
                indice_mayor = j
        lista[i], lista[indice_mayor] = lista[indice_mayor], lista[i]
    return lista


ordenar_por_seleccion(estudiantes)

for nombre, promedio in estudiantes:
    print(f"{nombre}: {promedio}")