estudiantes = ["Ana", "Luis", "Marta", "Pedro"]
materias = ["Matemática", "Lengua", "Historia", "Física"]

calificaciones = [
    [8, 9, 7, 10],
    [6, 5, 9, 8],
    [10, 7, 8, 6],
    [9, 8, 5, 7],
]


def buscar_calificacion(matriz, objetivo):
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            if matriz[i][j] == objetivo:
                return estudiantes[i], materias[j]
    return None


resultado = buscar_calificacion(calificaciones, 5)
if resultado:
    print(f"Estudiante: {resultado[0]}, Materia: {resultado[1]}")
else:
    print("Calificación no encontrada")

resultado = buscar_calificacion(calificaciones, 3)
if resultado:
    print(f"Estudiante: {resultado[0]}, Materia: {resultado[1]}")
else:
    print("Calificación no encontrada")