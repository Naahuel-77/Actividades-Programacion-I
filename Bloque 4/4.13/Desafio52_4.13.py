class Libro:
    def __init__(self, titulo, autor, isbn):
        self.__titulo = titulo
        self.__autor = autor
        self.__isbn = isbn

    def get_titulo(self):
        return self.__titulo

    def set_titulo(self, nuevo_titulo):
        if nuevo_titulo == "":
            print("El título no puede estar vacío")
        else:
            self.__titulo = nuevo_titulo

    def get_autor(self):
        return self.__autor

    def set_autor(self, nuevo_autor):
        if nuevo_autor == "":
            print("El autor no puede estar vacío")
        else:
            self.__autor = nuevo_autor

    def get_isbn(self):
        return self.__isbn

    def set_isbn(self, nuevo_isbn):
        if nuevo_isbn == "":
            print("El ISBN no puede estar vacío")
        else:
            self.__isbn = nuevo_isbn


libro = Libro("Rayuela", "Julio Cortázar", "978-84-376-0494-7")
print(libro.get_titulo())
print(libro.get_autor())
print(libro.get_isbn())

libro.set_titulo("El Aleph")
libro.set_autor("Jorge Luis Borges")
libro.set_isbn("978-84-206-3306-3")
print(libro.get_titulo())
print(libro.get_autor())
print(libro.get_isbn())

libro.set_titulo("")
print(libro.get_titulo())