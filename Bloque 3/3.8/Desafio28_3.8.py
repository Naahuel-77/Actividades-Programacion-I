def capitalizar_palabras(cadena):
    palabras = cadena.split(" ")
    resultado = []
    for palabra in palabras:
        resultado.append(palabra[:1].upper() + palabra[1:])
    return " ".join(resultado)


texto = "hola mundo, esto es una prueba"
print(capitalizar_palabras(texto))