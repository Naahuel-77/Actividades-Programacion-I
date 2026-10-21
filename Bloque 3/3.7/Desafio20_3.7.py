# 1. Definimos la lista de números (códigos ASCII) a procesar
codigos_ascii = [72, 111, 108, 97, 33, 56, 48, 115]

print("--- Herramienta Educativa: Conversor ASCII ---")

# 2. Recorremos la lista con un bucle for
for numero in codigos_ascii:
    # Convertimos el número a su carácter correspondiente
    caracter = chr(numero)
    
    # Mostramos el resultado de forma clara para el usuario
    print(f"Número: {numero} -> Carácter: '{caracter}'")