class Autor:
    def __init__(self, nombre, nacionalidad):
        self.nombre = nombre
        self.nacionalidad = nacionalidad

    def biografia(self):
        return f"{self.nombre} es un autor de nacionalidad {self.nacionalidad}."


class Escritor(Autor):
    def __init__(self, nombre, nacionalidad, generos):
        super().__init__(nombre, nacionalidad)
        self.generos = generos

    def biografia(self):
        return f"{self.nombre} es un escritor de nacionalidad {self.nacionalidad} y escribe: {', '.join(self.generos)}."

    def biografia_autor(self):
        return super().biografia()


escritor = Escritor("Mario Benedetti", "uruguaya", ["poesía", "novela"])

print(escritor.biografia())
print(Autor.biografia(escritor))
print(escritor.biografia_autor())