from collections import Counter
import matplotlib.pyplot as plt

entrada = input("Ingresá las notas separadas por comas: ")
partes = entrada.split(",")

notas = []
for parte in partes:
    notas.append( float(parte) )

promedio = sum(notas) / len(notas)
print(promedio)

print(min(notas))
print(max(notas))

conteo = Counter(notas)
print(conteo.most_common(1))

plt.bar( conteo.keys(), conteo.values() )
plt.title("Notas de la clase")
plt.xlabel("Nota")
plt.ylabel("Cantidad de estudiantes")
plt.show()