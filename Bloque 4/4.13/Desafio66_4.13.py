class Operacion:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def resultado(self):
        return None


class Suma(Operacion):
    def resultado(self):
        return self.a + self.b


class Multiplicacion(Operacion):
    def resultado(self):
        return self.a * self.b


operaciones = [Suma(4, 5), Multiplicacion(4, 5), Suma(10, -3), Multiplicacion(2.5, 4)]

for operacion in operaciones:
    print(f"{type(operacion).__name__}({operacion.a}, {operacion.b}) = {operacion.resultado()}")