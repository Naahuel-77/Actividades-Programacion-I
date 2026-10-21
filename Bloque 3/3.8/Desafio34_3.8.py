import string

texto = "  hola, mundo! esto es un procesador de texto 123.  "

capitalizado = string.capwords(texto)
sin_puntuacion = texto.translate(str.maketrans("", "", string.punctuation)).strip()
letras = sum(1 for c in texto if c in string.ascii_letters)
digitos = sum(1 for c in texto if c in string.digits)

print(capitalizado)
print(sin_puntuacion)
print(f"Letras: {letras}")
print(f"Dígitos: {digitos}")