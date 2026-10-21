astronomia = {"ana", "luis", "marta", "pedro", "sofia"}
matematica = {"ana", "marta", "diego", "sofia", "lucia"}
programacion = {"ana", "marta", "tomas", "lucia", "carlos", "sofia"}

en_todos = astronomia & matematica & programacion
solo_programacion = programacion - astronomia - matematica
al_menos_uno = astronomia | matematica | programacion

print("Participaron en todos los concursos:")
print(sorted(en_todos))

print("Solo participaron en Programación:")
print(sorted(solo_programacion))

print("Usuarios únicos en al menos un concurso:")
print(sorted(al_menos_uno))