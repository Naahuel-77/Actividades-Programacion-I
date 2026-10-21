class Usuario:
    def __init__(self, nombre, id_usuario):
        self.nombre = nombre
        self.id_usuario = id_usuario

    def mostrar_info(self):
        print(f"Usuario: {self.nombre} (ID: {self.id_usuario})")


class Bibliotecario(Usuario):
    def __init__(self, nombre, id_usuario, seccion, años_experiencia):
        super().__init__(nombre, id_usuario)
        self.seccion = seccion
        self.años_experiencia = años_experiencia

    def mostrar_info(self):
        super().mostrar_info()
        print(f"Sección: {self.seccion}")
        print(f"Años de experiencia: {self.años_experiencia}")


usuario = Usuario("Luis", 101)
usuario.mostrar_info()

bibliotecario = Bibliotecario("Ana", 1, "Literatura", 8)
bibliotecario.mostrar_info()
print(isinstance(bibliotecario, Usuario))