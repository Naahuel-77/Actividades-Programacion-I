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

    def cantidad_libros(self):
        return len(self.__libros)


def autor_con_mas_libros(autores):
    if not autores:
        return None
    return max(autores, key=lambda autor: autor.cantidad_libros())


cortazar = Autor("Julio Cortázar", "argentina")
cortazar.agregar_libro(Libro("Rayuela", "978-84-376-0494-7"))
cortazar.agregar_libro(Libro("Bestiario", "978-84-206-3306-3"))

borges = Autor("Jorge Luis Borges", "argentina")
borges.agregar_libro(Libro("El Aleph", "978-84-206-3307-0"))
borges.agregar_libro(Libro("Ficciones", "978-84-206-3308-7"))
borges.agregar_libro(Libro("El libro de arena", "978-84-206-3309-4"))

bioy = Autor("Adolfo Bioy Casares", "argentina")
bioy.agregar_libro(Libro("La invención de Morel", "978-84-206-3310-0"))

mejor = autor_con_mas_libros([cortazar, borges, bioy])
print(f"Autor con más libros: {mejor.nombre} ({mejor.cantidad_libros()} libros)")
print(autor_con_mas_libros([]))