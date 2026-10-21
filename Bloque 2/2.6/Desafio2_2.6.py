entrada = input("Ingresá las calificaciones separadas por comas: ")
partes = entrada.split(",")

calificaciones = []
for parte in partes:
    calificaciones.append( float(parte) )

promedio = sum(calificaciones) / len(calificaciones)
print(promedio)