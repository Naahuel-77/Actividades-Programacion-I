# Desafío 7: Convertidor de temperaturas 

# 1. Solicitamos la temperatura al usuario y la convertimos a float
celsius = float(input("Ingresa la temperatura en grados Celsius: "))

# 2. Realizamos los cálculos directamente en las nuevas variables 
fahrenheit = (celsius * 9/5) + 32 
kelvin = celsius + 273.15 

# 3. Mostramos los resultados de forma clara 
print("-" * 30) 
print(f"Resultados de la conversión:") 
print(f"{celsius} °C equivalen a {fahrenheit} °F")
print(f"{celsius} °C equivalen a {kelvin} K") 
print("-" * 30)