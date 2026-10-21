LIMITE = 1000


def factorial(n):
    if isinstance(n, bool) or not isinstance(n, int):
        raise TypeError("El número debe ser un entero")
    if n < 0:
        raise ValueError("El número no puede ser negativo")
    if n > LIMITE:
        raise OverflowError(f"El número es demasiado grande (máximo {LIMITE})")
    resultado = 1
    for i in range(2, n + 1):
        resultado *= i
    return resultado


for valor in [5, 0, 20, -3, 3.5, "7", 5000]:
    try:
        print(f"{valor!r}! = {factorial(valor)}")
    except TypeError as error:
        print(f"{valor!r}: {error}")
    except ValueError as error:
        print(f"{valor!r}: {error}")
    except OverflowError as error:
        print(f"{valor!r}: {error}")