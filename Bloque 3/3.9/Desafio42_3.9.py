def invertir_palabras(palabras):
    if len(palabras) <= 1:
        return palabras
    
    return [palabras[-1]] + invertir_palabras(palabras[:-1])

oracion = input("Ingrese una oración: ")

lista_palabras = oracion.split()

palabras_invertidas = invertir_palabras(lista_palabras)

resultado = " ".join(palabras_invertidas)
print(f"Oración invertida: {resultado}")