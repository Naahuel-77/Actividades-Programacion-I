registros = [
    ("Montevideo", 18.5, 70),
    ("Buenos Aires", 22.0, 65),
    ("Santiago", 28.5, 40),
    ("Lima", 20.0, 80),
    ("Quito", 14.0, 75),
]

ciudad_mas_calida = max(registros, key=lambda registro: registro[1])
ciudad_mas_fria = min(registros, key=lambda registro: registro[1])
promedio_humedad = sum(humedad for _, _, humedad in registros) / len(registros)

print(f"Registros climáticos: {len(registros)}")
print(f"Temperatura más alta: {ciudad_mas_calida[0]} ({ciudad_mas_calida[1]} °C)")
print(f"Temperatura más baja: {ciudad_mas_fria[0]} ({ciudad_mas_fria[1]} °C)")
print(f"Promedio general de humedad: {promedio_humedad:.1f} %")