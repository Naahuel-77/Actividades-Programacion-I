import re
from collections import Counter
import matplotlib.pyplot as plt

texto = """El perro corre en el parque. El gato duerme en la casa.
El perro y el gato juegan en el parque y en la casa.
La casa es grande y el parque es verde."""

palabras = re.findall(r"\w+", texto.lower())
contador = Counter(palabras)
top10 = contador.most_common(10)

print(f"Total de palabras: {len(palabras)}")
print(f"Palabras distintas: {len(contador)}")
print("Las 10 más comunes:")
for palabra, frecuencia in top10:
    print(f"{palabra}: {frecuencia}")

nombres = [p for p, f in top10]
frecuencias = [f for p, f in top10]

plt.figure(figsize=(10, 6))
plt.bar(nombres, frecuencias, color="steelblue")
plt.title("Las 10 palabras más frecuentes")
plt.xlabel("Palabra")
plt.ylabel("Frecuencia")
plt.show()