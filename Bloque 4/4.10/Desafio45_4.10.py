class Arma:
    def __init__(self, nombre, dano):
        self.nombre = nombre
        self.dano = dano


class Personaje:
    def __init__(self, nombre, vida, arma):
        self.nombre = nombre
        self.vida = vida
        self.arma = arma

    def atacar(self, objetivo):
        print(f"{self.nombre} ataca a {objetivo.nombre} con {self.arma.nombre}")
        objetivo.recibir_dano(self.arma.dano)

    def recibir_dano(self, dano):
        self.vida -= dano
        print(f"{self.nombre} recibe {dano} de daño (vida: {self.vida})")

    def habilidad_especial(self, objetivo):
        print(f"{self.nombre} no tiene habilidad especial")


class Guerrero(Personaje):
    def habilidad_especial(self, objetivo):
        print(f"{self.nombre} usa Golpe Doble")
        objetivo.recibir_dano(self.arma.dano * 2)


class Mago(Personaje):
    def habilidad_especial(self, objetivo):
        print(f"{self.nombre} lanza Bola de Fuego")
        objetivo.recibir_dano(30)


class Arquero(Personaje):
    def habilidad_especial(self, objetivo):
        print(f"{self.nombre} dispara Flecha Certera")
        objetivo.recibir_dano(self.arma.dano + 10)


class Ladron(Personaje):
    def habilidad_especial(self, objetivo):
        print(f"{self.nombre} usa Ataque Furtivo")
        objetivo.recibir_dano(self.arma.dano * 3)


personajes = [
    Guerrero("Thor", 100, Arma("Espada", 20)),
    Mago("Merlín", 70, Arma("Bastón", 10)),
    Arquero("Legolas", 80, Arma("Arco", 15)),
    Ladron("Sombra", 60, Arma("Daga", 8)),
]

enemigo = Personaje("Orco", 200, Arma("Garrote", 5))

for p in personajes:
    p.atacar(enemigo)
    p.habilidad_especial(enemigo)

print(f"Vida final del Orco: {enemigo.vida}")