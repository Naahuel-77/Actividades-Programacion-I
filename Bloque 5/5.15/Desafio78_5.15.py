class Nodo:
    def __init__(self, valor):
        self.valor = valor
        self.izquierdo = None
        self.derecho = None


def maximo_postorden(nodo):
    if nodo is None:
        return None
    maximo_izq = maximo_postorden(nodo.izquierdo)
    maximo_der = maximo_postorden(nodo.derecho)
    maximo = nodo.valor
    if maximo_izq is not None and maximo_izq > maximo:
        maximo = maximo_izq
    if maximo_der is not None and maximo_der > maximo:
        maximo = maximo_der
    return maximo


raiz = Nodo(10)
raiz.izquierdo = Nodo(5)
raiz.derecho = Nodo(15)
raiz.izquierdo.izquierdo = Nodo(3)
raiz.izquierdo.derecho = Nodo(7)
raiz.derecho.izquierdo = Nodo(12)
raiz.derecho.derecho = Nodo(20)

print(maximo_postorden(raiz))