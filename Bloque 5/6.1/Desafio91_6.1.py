import random


def generar_temperaturas(cantidad, minimo=-10.0, maximo=40.0):
    return [round(random.uniform(minimo, maximo), 2) for _ in range(cantidad)]


temperaturas = generar_temperaturas(10)

print("Temperaturas generadas:")
for i, temperatura in enumerate(temperaturas, start=1):
    print(f"{i}. {temperatura} °C")

print(f"Mínima: {min(temperaturas)} °C")
print(f"Máxima: {max(temperaturas)} °C")
print(f"Promedio: {round(sum(temperaturas) / len(temperaturas), 2)} °C")