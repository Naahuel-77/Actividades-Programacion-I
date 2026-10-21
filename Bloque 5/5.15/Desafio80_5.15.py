import re


class Nodo:
    def __init__(self, valor):
        self.valor = valor
        self.izquierdo = None
        self.derecho = None


def tokenizar(expresion):
    return re.findall(r"\d+|[+\-*/]", expresion)


def construir_arbol(expresion):
    tokens = tokenizar(expresion)
    posicion = 0

    def parsear_numero():
        nonlocal posicion
        nodo = Nodo(int(tokens[posicion]))
        posicion += 1
        return nodo

    def parsear_termino():
        nonlocal posicion
        nodo = parsear_numero()
        while posicion < len(tokens) and tokens[posicion] in ("*", "/"):
            operador = Nodo(tokens[posicion])
            posicion += 1
            operador.izquierdo = nodo
            operador.derecho = parsear_numero()
            nodo = operador
        return nodo

    def parsear_expresion():
        nonlocal posicion
        nodo = parsear_termino()
        while posicion < len(tokens) and tokens[posicion] in ("+", "-"):
            operador = Nodo(tokens[posicion])
            posicion += 1
            operador.izquierdo = nodo
            operador.derecho = parsear_termino()
            nodo = operador
        return nodo

    return parsear_expresion()


def evaluar(nodo):
    if nodo.izquierdo is None and nodo.derecho is None:
        return nodo.valor
    izquierda = evaluar(nodo.izquierdo)
    derecha = evaluar(nodo.derecho)
    if nodo.valor == "+":
        return izquierda + derecha
    if nodo.valor == "-":
        return izquierda - derecha
    if nodo.valor == "*":
        return izquierda * derecha
    return izquierda / derecha


arbol = construir_arbol("5 + 3 * 4")
print(evaluar(arbol))