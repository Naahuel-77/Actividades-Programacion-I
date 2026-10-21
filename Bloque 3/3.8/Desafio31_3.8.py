def es_palindromo(cadena):
    limpia = cadena.replace(" ", "").lower()
    return limpia == limpia[::-1]


print(es_palindromo("reconocer"))
print(es_palindromo("Anita lava la tina"))
print(es_palindromo("python"))