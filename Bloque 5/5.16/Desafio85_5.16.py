class Nodo:
    def __init__(self, nombre, promedio):
        self.nombre = nombre
        self.promedio = promedio
        self.izquierdo = None
        self.derecho = None


def insertar(nodo, nombre, promedio):
    if nodo is None:
        return Nodo(nombre, promedio)
    if promedio < nodo.promedio:
        nodo.izquierdo = insertar(nodo.izquierdo, nombre, promedio)
    else:
        nodo.derecho = insertar(nodo.derecho, nombre, promedio)
    return nodo


def construir_arbol(estudiantes):
    raiz = None
    for nombre, promedio in estudiantes:
        raiz = insertar(raiz, nombre, promedio)
    return raiz


def recorrer_inorden(nodo):
    if nodo is None:
        return
    recorrer_inorden(nodo.izquierdo)
    print(f"{nodo.nombre}: {nodo.promedio}")
    recorrer_inorden(nodo.derecho)


estudiantes = [
    ("Ana", 8.5),
    ("Luis", 7.2),
    ("Marta", 9.1),
    ("Pedro", 6.8),
    ("Sofía", 8.9),
]

raiz = construir_arbol(estudiantes)
recorrer_inorden(raiz)