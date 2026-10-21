class Escritor:
    def __init__(self, nombre, generos, **kwargs):
        super().__init__(**kwargs)
        self.nombre = nombre
        self.generos = generos

    def escribir(self):
        print(f"{self.nombre} escribe en los géneros: {', '.join(self.generos)}")


class Academico:
    def __init__(self, universidad, area, **kwargs):
        super().__init__(**kwargs)
        self.universidad = universidad
        self.area = area

    def investigar(self):
        print(f"{self.nombre} investiga en {self.area} ({self.universidad})")


class EscritorAcademico(Escritor, Academico):
    def __init__(self, nombre, generos, universidad, area):
        super().__init__(nombre=nombre, generos=generos, universidad=universidad, area=area)
        self.articulos = []

    def publicar_articulo(self, titulo):
        self.articulos.append(titulo)
        print(f"Artículo publicado: '{titulo}'")


autor = EscritorAcademico("Laura Gómez", ["novela", "ensayo"], "Universidad de la República", "Literatura")
autor.escribir()
autor.investigar()
autor.publicar_articulo("La memoria en la narrativa uruguaya")
autor.publicar_articulo("Ficción y realidad en el cuento")
print(f"Artículos publicados: {autor.articulos}")
print([clase.__name__ for clase in EscritorAcademico.__mro__])