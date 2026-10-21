import random


def lanzar_dados(cantidad=2):
    return random.choices([1, 2, 3, 4, 5, 6], k=cantidad)


for lanzamiento in range(1, 4):
    dado1, dado2 = lanzar_dados()
    print(f"Lanzamiento {lanzamiento}: {dado1} y {dado2} (suma: {dado1 + dado2})")