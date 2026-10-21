def procesar(valor):
    numero = float(valor)
    resultado = 100 / numero
    return numero, resultado


valores = [4, "5", 0, "abc", None, 2.5, [1, 2]]
exitosas = 0
total = 0

for valor in valores:
    try:
        numero, resultado = procesar(valor)
    except ZeroDivisionError:
        print(f"{valor!r}: no se puede dividir entre cero")
    except ValueError:
        print(f"{valor!r}: no es un número válido")
    except TypeError:
        print(f"{valor!r}: tipo de dato no permitido")
    else:
        print(f"{valor!r}: 100 / {numero} = {resultado}")
        exitosas += 1
        total += resultado

print(f"Operaciones exitosas: {exitosas}")
print(f"Suma de resultados: {total}")