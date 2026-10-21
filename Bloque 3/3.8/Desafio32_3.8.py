def es_primo(numero):
    if numero < 2:
        return False
    for i in range(2,numero): 
        if numero % i == 0:
           return False
    return True
def contar_primos(lista_de_numeros):
    contador = 0
    for num in lista_de_numeros:
        if es_primo(num) == True:
           contador = contador + 1
    return contador
def main():
    numeros = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 13, 14, 15]
    print("--- Probando nuestro programa de números primos ---")
    print(f"Lista de números a revisar: {numeros}")
    cantidad_primos = contar_primos(numeros)
    print(f"La cantidad de números primos en la lista es: {cantidad_primos}")
if __name__ == "__main__":
        main()