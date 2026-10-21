from datetime import datetime
texto_fecha1 = input("Ingrese la primera fecha (formato: dd/mm/aaaa): ")
fecha1 = datetime.strptime(texto_fecha1, "%d/%m/%Y")
texto_fecha2 = input("Ingrese la segunda fecha (formato: dd/mm/aaaa): ")
fecha2 = datetime.strptime(texto_fecha2, "%d/%m/%Y")
diferencia = fecha2 - fecha1
print(f"La diferencia entre las fechas es de {abs(diferencia.days)} días.")