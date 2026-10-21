class Nodo:
    def __init__(self, valor):
        self.valor = valor
        self.izquierdo = None
        self.derecho = None


def insertar(nodo, valor):
    if nodo is None:
        return Nodo(valor)
    if valor < nodo.valor:
        nodo.izquierdo = insertar(nodo.izquierdo, valor)
    elif valor > nodo.valor:
        nodo.derecho = insertar(nodo.derecho, valor)
    return nodo


def buscar(nodo, valor):
    if nodo is None:
        return False
    if valor == nodo.valor:
        return True
    if valor < nodo.valor:
        return buscar(nodo.izquierdo, valor)
    return buscar(nodo.derecho, valor)


valores = [10, 5, 15, 3, 7, 12, 20]
raiz = None
for valor in valores:
    raiz = insertar(raiz, valor)

print(buscar(raiz, 7))
print(buscar(raiz, 8))