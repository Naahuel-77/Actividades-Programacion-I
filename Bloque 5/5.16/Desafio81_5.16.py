from collections import deque


class Nodo:
    def __init__(self, nombre, estudiantes):
        self.nombre = nombre
        self.estudiantes = estudiantes
        self.hijos = []


def recorrer_por_niveles(raiz):
    if raiz is None:
        return
    cola = deque([raiz])
    while cola:
        nodo = cola.popleft()
        print(f"{nodo.nombre}: {', '.join(nodo.estudiantes)}")
        for hijo in nodo.hijos:
            cola.append(hijo)


grado12 = Nodo("Grado 12", ["Ana", "Luis"])
grado11a = Nodo("Grado 11 A", ["Marta", "Pedro"])
grado11b = Nodo("Grado 11 B", ["Sofía", "Diego"])
grado10 = Nodo("Grado 10", ["Lucía", "Tomás"])

grado12.hijos = [grado11a, grado11b]
grado11a.hijos = [grado10]

recorrer_por_niveles(grado12)