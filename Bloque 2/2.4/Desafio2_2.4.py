total = 0

for i in range(5):
    nota = float(input("Ingresá una calificación: "))
    total = total + nota

promedio = total / 5
print("El promedio es:", promedio)