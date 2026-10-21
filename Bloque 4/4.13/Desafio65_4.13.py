class Figura:
    def area(self):
        pass

class Circulo(Figura):
    def __init__(self, radio): 
        self.radio = radio
    def area(self):
        return 3.1416 * self.radio ** 2

class Cuadrado(Figura):
    def __init__(self, lado):
        self.lado = lado
    def area(self):
        return self.lado ** 2

circulo = Circulo(5)
cuadrado = Cuadrado(4)
figuras = [circulo, cuadrado]

for figura in figuras:
    print(f"Figura: {type(figura).__name__}, Área: {round(figura.area(), 2)}")