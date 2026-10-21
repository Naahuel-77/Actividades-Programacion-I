# Desafío 14: Contador de palabras 
 
def contador_de_palabras(): 
    print("--- Contador de Palabras ---") 
     
    # 1. Pedimos al usuario que ingrese el texto 
    texto = input("Por favor, ingresá un texto o una frase: \n> ") 
     
    # 2. Validamos que el usuario no haya ingresado algo vacío 
    # .strip() elimina los espacios de más al principio y al final 
    if not texto.strip(): 
        print("\n[!] No ingresaste ningún texto válido.") 
        return 
 
    # 3. Separamos el texto en palabras usando .split() 
    # Por defecto, split() separa por espacios, tabulaciones o saltos de 
línea 
    lista_palabras = texto.split() 
     
    # 4. Contamos la cantidad de elementos en la lista 
    cantidad_palabras = len(lista_palabras) 
     
    # 5. Formateamos la salida para que quede prolijo 
    print("\n" + "="*30) 
    print(f"Resultado del análisis:") 
    print(f"-> Cantidad de palabras: {cantidad_palabras}") 
    print("="*30) 
 
# Ejecutamos la función 
contador_de_palabras() 