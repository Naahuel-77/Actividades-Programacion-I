import math


class NegativeNumberError(Exception):
    def __init__(self, numero):
        self.numero = numero
        super().__init__(f"No se puede calcular la raíz cuadrada de un número negativo: {numero}")


def raiz_cuadrada(numero):
    if numero < 0:
        raise NegativeNumberError(numero)
    return math.sqrt(numero)


for valor in [16, 2, 0, -9, 2.25, -0.5]:
    try:
        print(f"Raíz cuadrada de {valor} = {raiz_cuadrada(valor)}")
    except NegativeNumberError as error:
        print(f"Error: {error}")