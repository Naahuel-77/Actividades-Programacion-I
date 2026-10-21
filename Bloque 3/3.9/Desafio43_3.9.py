def contar_pila(total_pila, actual=1):
    if actual > total_pila:
        return 0
    print(f"  Cuenta la manzana {actual}")
    return 1 + contar_pila(total_pila, actual + 1)


def mono_cuenta(pilas, numero=1):
    if not pilas:
        return 0
    print(f"Pila {numero}: {pilas[0]} manzanas")
    contadas = contar_pila(pilas[0])
    print("  Termina la pila, olvida y vuelve a empezar")
    return contadas + mono_cuenta(pilas[1:], numero + 1)


pilas = [5, 3]
total = mono_cuenta(pilas)
print(f"Total: {total}")