class Libro:
    def __init__(self, titulo, autor):
        self.titulo = titulo
        self.autor = autor

    def mostrar_info(self):
        print(f"Título: {self.titulo}")
        print(f"Autor: {self.autor}")


class LibroEspecializado(Libro):
    NIVELES = ["basico", "intermedio", "avanzado"]

    def __init__(self, titulo, autor, campo_estudio, nivel):
        super().__init__(titulo, autor)
        if nivel.lower() not in self.NIVELES:
            raise ValueError(f"Nivel inválido: {nivel}. Opciones: {', '.join(self.NIVELES)}")
        self.campo_estudio = campo_estudio
        self.nivel = nivel.lower()

    def mostrar_info(self):
        super().mostrar_info()
        print(f"Campo de estudio: {self.campo_estudio}")
        print(f"Nivel de especialización: {self.nivel}")


libro = Libro("Rayuela", "Julio Cortázar")
libro.mostrar_info()

especializado = LibroEspecializado("Introducción a la Programación en Python", "Guido Pérez", "Informática", "basico")
especializado.mostrar_info()

try:
    LibroEspecializado("Física Cuántica", "Ana Ruiz", "Física", "experto")
except ValueError as error:
    print(error)