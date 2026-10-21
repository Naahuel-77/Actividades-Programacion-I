def resaltar_recursivo(texto, palabra):
    if palabra == "":
        return texto
    indice = texto.lower().find(palabra.lower())
    if indice == -1:
        return texto
    fin = indice + len(palabra)
    return texto[:indice] + "**" + texto[indice:fin] + "**" + resaltar_recursivo(texto[fin:], palabra)


texto = "El gato duerme. El perro corre. El gato juega con el perro y el gato come."
print(resaltar_recursivo(texto, "gato"))
print(resaltar_recursivo(texto, "pez"))