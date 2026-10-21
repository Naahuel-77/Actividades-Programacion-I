class Musico:
    def __init__(self, nombre):
        self.nombre = nombre

    def instrumento(self):
        return f"{self.nombre} toca un instrumento"


class Guitarrista(Musico):
    def instrumento(self):
        return f"{self.nombre} toca la guitarra"


class Baterista(Musico):
    def instrumento(self):
        return f"{self.nombre} toca la batería"


musico = Musico("Pablo")
guitarrista = Guitarrista("Nahuel")
baterista = Baterista("Luis")

for m in [musico, guitarrista, baterista]:
    print(m.instrumento())