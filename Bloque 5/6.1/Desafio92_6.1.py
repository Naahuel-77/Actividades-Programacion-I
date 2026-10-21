import random


def sortear_ganadores(participantes, cantidad):
    if cantidad > len(participantes):
        raise ValueError("No hay suficientes participantes para esa cantidad de ganadores")
    return random.sample(participantes, cantidad)


participantes = [f"Participante {i}" for i in range(1, 101)]

ganadores = sortear_ganadores(participantes, 5)

print("Ganadores del sorteo:")
for i, ganador in enumerate(ganadores, start=1):
    print(f"{i}. {ganador}")