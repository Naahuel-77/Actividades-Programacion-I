numeros = [4, 7, 2, 7, 4, 9, 2, 1]
sin_duplicados = []
for numero in numeros:
    if numero not in sin_duplicados:
        sin_duplicados.append(numero)
print("Lista original:", numeros)
print("Lista sin duplicados:", sin_duplicados)