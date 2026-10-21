alumnos = [
    ("Juan", 8),
    ("Maria", 12),
    ("Pedro", 5),
    ("Ana", 5),
    ("Carlos", 8),
    ("Paula", 2),
    ("Agustin", 8),
    ("Lucas", 9),
    ("Anthony", 12),
    ("Maria", 11)
]

aprobados = 0
desaprobados = 0

for nombre, nota in alumnos:
    if nota >= 7:
        aprobados = aprobados + 1
    else:
        desaprobados = desaprobados + 1

print(f"Aprobados: {aprobados}")
print(f"Desaprobados: {desaprobados}")