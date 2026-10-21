# Desafío 8: Verificar múltiplos de varios números 

# 1. Solicitamos al usuario un número entero
numero = int(input("Ingresa un número entero para verificar sus múltiplos: ")) 

# 2. Definimos la lista de divisores 
divisores = [2, 3, 5, 7, 9, 10, 11] 

print("-" * 40) 
print(f"Verificando múltiplos para el número: {numero}") 
print("-" * 40) 

# 3. Bucle para verificar cada divisor
for d in divisores: 
    if numero % d == 0: 
        print(f"El número {numero} ES múltiplo de {d}.")
    else:
        print(f"El número {numero} NO es múltiplo de {d}.") 

print("-" * 40)