class Libro:
    def __init__(self, titulo, isbn):
        self.titulo = titulo
        self.isbn = isbn


class Autor:
    def __init__(self, nombre, nacionalidad):
        self.nombre = nombre
        self.nacionalidad = nacionalidad
        self.libros = []

    def agregar_libro(self, libro):
        self.libros.append(libro)
        print(f"Libro '{libro.titulo}' agregado a los libros de {self.nombre}.")


autor = Autor("Julio Cortázar", "argentina")
autor.agregar_libro(Libro("Rayuela", "978-84-376-0494-7"))
autor.agregar_libro(Libro("Bestiario", "978-84-206-3306-3"))
print(f"Libros de {autor.nombre}: {[libro.titulo for libro in autor.libros]}")