class Libro:
    def __init__(self, titulo, isbn):
        self.titulo = titulo
        self.isbn = isbn


class Autor:
    def __init__(self, nombre, nacionalidad):
        self.nombre = nombre
        self.nacionalidad = nacionalidad
        self.__libros = []

    def agregar_libro(self, libro):
        self.__libros.append(libro)
        print(f"Libro '{libro.titulo}' agregado a los libros de {self.nombre}.")

    def obtener_libros(self):
        return list(self.__libros)


def titulos_de_libros(autor):
    return [libro.titulo for libro in autor.obtener_libros()]


autor = Autor("Julio Cortázar", "argentina")
autor.agregar_libro(Libro("Rayuela", "978-84-376-0494-7"))
autor.agregar_libro(Libro("Bestiario", "978-84-206-3306-3"))

print(titulos_de_libros(autor))
print(hasattr(autor, "libros"))

copia = autor.obtener_libros()
copia.clear()
print(titulos_de_libros(autor))