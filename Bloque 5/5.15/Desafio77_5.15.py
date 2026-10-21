class Nodo:
    def __init__(self, valor):
        self.valor = valor
        self.izquierdo = None
        self.derecho = None


def suma_inorden(nodo):
    if nodo is None:
        return 0
    return suma_inorden(nodo.izquierdo) + nodo.valor + suma_inorden(nodo.derecho)


raiz = Nodo(10)
raiz.izquierdo = Nodo(5)
raiz.derecho = Nodo(15)
raiz.izquierdo.izquierdo = Nodo(3)
raiz.izquierdo.derecho = Nodo(7)
raiz.derecho.izquierdo = Nodo(12)
raiz.derecho.derecho = Nodo(20)

print(suma_inorden(raiz))