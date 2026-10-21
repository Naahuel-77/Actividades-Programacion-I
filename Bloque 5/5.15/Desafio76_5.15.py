class Nodo:
    def __init__(self, valor):
        self.valor = valor
        self.izquierdo = None
        self.derecho = None


def preorden(nodo):
    if nodo is None:
        return
    print(nodo.valor)
    preorden(nodo.izquierdo)
    preorden(nodo.derecho)


raiz = Nodo(10)
raiz.izquierdo = Nodo(5)
raiz.derecho = Nodo(15)
raiz.izquierdo.izquierdo = Nodo(3)
raiz.izquierdo.derecho = Nodo(7)
raiz.derecho.izquierdo = Nodo(12)
raiz.derecho.derecho = Nodo(20)

print("Recorrido en preorden:")
preorden(raiz)