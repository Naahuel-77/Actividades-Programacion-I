def suma_y_promedio(numeros):
    if len(numeros) == 0:
        return 0, 0
    suma = sum(numeros)
    promedio = suma / len(numeros)
    return suma, promedio


lista = [4, 8, 15, 16, 23, 42]
total, prom = suma_y_promedio(lista)
print(f"Suma: {total}")
print(f"Promedio: {prom}")