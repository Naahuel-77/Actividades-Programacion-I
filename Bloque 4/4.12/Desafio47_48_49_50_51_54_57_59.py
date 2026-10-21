from datetime import date


class Autor:
    def __init__(self, nombre, nacionalidad, año_nacimiento=None, biografia=""):
        self._nombre = nombre
        self._nacionalidad = nacionalidad
        self.año_nacimiento = año_nacimiento
        self.biografia = biografia
        self.libros = []
        self.premios = []

    @property
    def nombre(self):
        return self._nombre

    @property
    def nacionalidad(self):
        return self._nacionalidad

    @nombre.setter
    def nombre(self, nuevo_nombre):
        if nuevo_nombre == "":
            print("El nombre no puede estar vacío")
        else:
            self._nombre = nuevo_nombre

    @nacionalidad.setter
    def nacionalidad(self, nueva_nacionalidad):
        if nueva_nacionalidad == "":
            print("La nacionalidad no puede estar vacía")
        else:
            self._nacionalidad = nueva_nacionalidad

    def agregar_libro(self, libro):
        self.libros.append(libro)
        print(f"Libro '{libro.titulo}' agregado a los libros de {self.nombre}.")

    def eliminar_libro(self, libro):
        if libro in self.libros:
            self.libros.remove(libro)
            print(f"Libro '{libro.titulo}' eliminado de los libros de {self.nombre}.")
        else:
            print(f"El libro '{libro.titulo}' no se encuentra entre los libros de {self.nombre}.")

    def agregar_premio(self, premio):
        self.premios.append(premio)
        print(f"Premio agregado a {self.nombre}: {premio}")

    def cantidad_libros(self):
        return len(self.libros)

    def listar_libros(self):
        return [libro.titulo for libro in self.libros]

    def calcular_edad(self):
        if self.año_nacimiento is None:
            return None
        return date.today().year - self.año_nacimiento

    def mostrar_info(self):
        edad = self.calcular_edad()
        print(f"Autor: {self.nombre}")
        print(f"Nacionalidad: {self.nacionalidad}")
        print(f"Edad: {edad} años" if edad is not None else "Edad: no especificada")
        print(f"Biografía: {self.biografia}" if self.biografia else "Biografía: no especificada")
        print(f"Libros ({self.cantidad_libros()}): {', '.join(self.listar_libros()) or 'ninguno'}")
        print(f"Premios: {', '.join(self.premios) or 'ninguno'}")


class Libro:
    def __init__(self, titulo, autor, isbn):
        self.titulo = titulo
        self.autor = autor
        self.isbn = isbn


autor1 = Autor("Rick Riordan", "estadounidense")
print(f"El nombre del autor es {autor1.nombre} y su nacionalidad es {autor1.nacionalidad}.")

autor1.nombre = "H.P Lovecraft"
print(f"El nombre del autor es {autor1.nombre}.")

autor1.nombre = ""
print(f"El nombre del autor es {autor1.nombre}.")
libro1 = Libro("Percy Jackson y el ladrón de rayos", "Fantasía", "978-84-08-12345-6")
autor1.agregar_libro(libro1)
print(f"Libros de {autor1.nombre}: {[libro.titulo for libro in autor1.libros]}")


class Poeta(Autor):
    def __init__(self, nombre, nacionalidad, tipo_poesia):
        super().__init__(nombre, nacionalidad)
        self.tipo_poesia = tipo_poesia

    def mostrar_info(self):
        print(f"El nombre del poeta es {self.nombre}, su nacionalidad es {self.nacionalidad} y escribe poesía de tipo {self.tipo_poesia}.")


poeta1 = Poeta("Mario Benedetti", "uruguaya", "romántica")
poeta2 = Poeta("Edgar Allan Poe", "estadounidense", "gótica")

poeta1.mostrar_info()
poeta2.mostrar_info()

libro2 = Libro("Poemas de amor", "Romántica", "978-84-08-54321-0")
poeta1.agregar_libro(libro2)
print(f"Libros de {poeta1.nombre}: {[libro.titulo for libro in poeta1.libros]}")


class LibroDigital(Libro):
    def __init__(self, titulo, autor, isbn, formato, tamaño_archivo):
        super().__init__(titulo, autor, isbn)
        self.formato = formato
        self.tamaño_archivo = tamaño_archivo

    def mostrar_informacion(self):
        print(f"Libro Digital: {self.titulo}, Autor: {self.autor}, ISBN: {self.isbn}, Formato: {self.formato}, Tamaño del archivo: {self.tamaño_archivo} MB.")

class EBook(LibroDigital):
    def __init__(self, titulo, autor, isbn, formato, tamaño_archivo, enlace_descarga):
        super().__init__(titulo, autor, isbn, formato, tamaño_archivo)
        self.enlace_descarga = enlace_descarga

    def mostrar_informacion(self):
        super().mostrar_informacion()
        print(f"Enlace de descarga: {self.enlace_descarga}")

libro_digital1 = LibroDigital("Juego de Tronos", "George R.R. Martin", "978-84-08-98765-4", "PDF", 5.2)

ebook1 = EBook("El Principito", "Antoine de Saint-Exupéry", "978-84-08-54321-0", "EPUB", 2.5, "https://descargas.ejemplo.com/el-principito")

libro_digital1.mostrar_informacion()
ebook1.mostrar_informacion()

autor3 = Autor("Laura Gómez", "uruguaya", 1980, "Escritora de cuentos y novelas.")
libro3 = Libro("Cuentos del sur", "Cuentos", "978-84-08-11111-1")
libro4 = Libro("La casa vacía", "Novela", "978-84-08-22222-2")
autor3.agregar_libro(libro3)
autor3.agregar_libro(libro4)
autor3.agregar_premio("Premio Nacional de Literatura")
autor3.mostrar_info()
autor3.eliminar_libro(libro4)
print(f"Cantidad de libros: {autor3.cantidad_libros()}")

class Biblioteca:
    def __init__(self):
        self.libros = []
        self.autores = []

    def agregar_libro(self, libro):
        self.libros.append(libro)

    def agregar_autor(self, autor):
        self.autores.append(autor)

    def buscar_libro(self, texto):
        texto = texto.lower()
        return [libro for libro in self.libros if texto in libro.titulo.lower()]

    def buscar_libro_por_isbn(self, isbn):
        for libro in self.libros:
            if libro.isbn == isbn:
                return libro
        return None

    def buscar_autor(self, texto):
        texto = texto.lower()
        return [autor for autor in self.autores if texto in autor.nombre.lower()]

    def libros_de_autor(self, texto):
        libros = []
        for autor in self.buscar_autor(texto):
            libros.extend(autor.libros)
        return libros


biblioteca = Biblioteca()
for libro in [libro1, libro2, libro3, libro4, libro_digital1, ebook1]:
    biblioteca.agregar_libro(libro)
for autor in [autor1, poeta1, poeta2, autor3]:
    biblioteca.agregar_autor(autor)

resultados = biblioteca.buscar_libro("poemas")
print(f"Libros con 'poemas': {[l.titulo for l in resultados]}")

encontrado = biblioteca.buscar_libro_por_isbn("978-84-08-98765-4")
print(f"ISBN 978-84-08-98765-4: {encontrado.titulo if encontrado else 'no encontrado'}")

autores = biblioteca.buscar_autor("poe")
print(f"Autores con 'poe': {[a.nombre for a in autores]}")

libros = biblioteca.libros_de_autor("benedetti")
print(f"Libros de benedetti: {[l.titulo for l in libros]}")

resultados = biblioteca.buscar_libro("dragón")
print(f"Libros con 'dragón': {[l.titulo for l in resultados] or 'sin resultados'}")

class Catalogo:
    def __init__(self):
        self.libros_por_isbn = {}
        self.autores_por_nombre = {}

    def agregar_autor(self, autor):
        self.autores_por_nombre[autor.nombre] = autor

    def agregar_libro(self, libro):
        if libro.isbn in self.libros_por_isbn:
            existente = self.libros_por_isbn[libro.isbn]
            print(f"El ISBN {libro.isbn} ya está registrado ('{existente.titulo}'), no se agrega '{libro.titulo}'.")
            return
        self.libros_por_isbn[libro.isbn] = libro

    def obtener_libro(self, isbn):
        return self.libros_por_isbn.get(isbn)

    def obtener_autor(self, nombre):
        return self.autores_por_nombre.get(nombre)

    def libros_de_autor(self, nombre):
        autor = self.obtener_autor(nombre)
        return autor.libros if autor else []

    def total_autores(self):
        return len(self.autores_por_nombre)

    def total_libros(self):
        return len(self.libros_por_isbn)


catalogo = Catalogo()
for autor in [autor1, poeta1, poeta2, autor3]:
    catalogo.agregar_autor(autor)
for libro in [libro1, libro2, libro3, libro4, libro_digital1, ebook1]:
    catalogo.agregar_libro(libro)

print(f"Autores: {catalogo.total_autores()}")
print(f"Libros: {catalogo.total_libros()}")
print(f"Libro con ISBN 978-84-08-12345-6: {catalogo.obtener_libro('978-84-08-12345-6').titulo}")
print(f"Nacionalidad de Mario Benedetti: {catalogo.obtener_autor('Mario Benedetti').nacionalidad}")
print(f"Libros de Laura Gómez: {[l.titulo for l in catalogo.libros_de_autor('Laura Gómez')]}")
print(f"Autor inexistente: {catalogo.obtener_autor('Cortázar')}")