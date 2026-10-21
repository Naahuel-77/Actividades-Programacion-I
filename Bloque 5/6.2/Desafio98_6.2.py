estudiantes = {}
cursos_ofrecidos = {"Python", "Matemática", "Física"}


def registrar_curso(estudiante, curso):
    estudiantes.setdefault(estudiante, set()).add(curso)


def completaron_todos_los_cursos():
    return sorted(
        nombre for nombre, cursos in estudiantes.items()
        if cursos.issuperset(cursos_ofrecidos)
    )


def solo_completaron(curso):
    return sorted(
        nombre for nombre, cursos in estudiantes.items()
        if cursos == {curso}
    )


registros = [
    ("ana", "Python"), ("ana", "Matemática"), ("ana", "Física"),
    ("luis", "Python"),
    ("marta", "Python"), ("marta", "Matemática"), ("marta", "Física"),
    ("pedro", "Matemática"),
    ("sofia", "Física"),
    ("diego", "Python"), ("diego", "Física"),
]

for estudiante, curso in registros:
    registrar_curso(estudiante, curso)

print("Estudiantes que completaron todos los cursos:")
print(completaron_todos_los_cursos())

print("Solo completaron Python:")
print(solo_completaron("Python"))

print("Solo completaron Física:")
print(solo_completaron("Física"))