from datetime import date, timedelta


class Libro:
    def __init__(self, codigo, titulo, autor):
        self.codigo = codigo
        self.titulo = titulo
        self.autor = autor
        self.disponible = True


class Usuario:
    def __init__(self, id_usuario, nombre):
        self.id_usuario = id_usuario
        self.nombre = nombre
        self.prestamos = []
        self.multas = []

    def deuda(self):
        return sum(m.monto for m in self.multas if not m.pagada)


class Prestamo:
    def __init__(self, libro, usuario, fecha_prestamo, dias=14):
        self.libro = libro
        self.usuario = usuario
        self.fecha_prestamo = fecha_prestamo
        self.fecha_limite = fecha_prestamo + timedelta(days=dias)
        self.fecha_devolucion = None


class Multa:
    def __init__(self, usuario, prestamo, monto):
        self.usuario = usuario
        self.prestamo = prestamo
        self.monto = monto
        self.pagada = False


class Biblioteca:
    MULTA_POR_DIA = 10

    def __init__(self):
        self.libros = {}
        self.usuarios = {}
        self.prestamos = []

    def agregar_libro(self, libro):
        self.libros[libro.codigo] = libro

    def registrar_usuario(self, usuario):
        self.usuarios[usuario.id_usuario] = usuario

    def prestar(self, codigo, id_usuario, fecha):
        libro = self.libros[codigo]
        usuario = self.usuarios[id_usuario]
        if not libro.disponible:
            print(f"'{libro.titulo}' no está disponible")
            return None
        if usuario.deuda() > 0:
            print(f"{usuario.nombre} tiene multas pendientes")
            return None
        prestamo = Prestamo(libro, usuario, fecha)
        libro.disponible = False
        usuario.prestamos.append(prestamo)
        self.prestamos.append(prestamo)
        print(f"{usuario.nombre} se llevó '{libro.titulo}'")
        return prestamo

    def devolver(self, prestamo, fecha):
        prestamo.fecha_devolucion = fecha
        prestamo.libro.disponible = True
        dias_tarde = (fecha - prestamo.fecha_limite).days
        if dias_tarde > 0:
            monto = dias_tarde * self.MULTA_POR_DIA
            prestamo.usuario.multas.append(Multa(prestamo.usuario, prestamo, monto))
            print(
                f"{prestamo.usuario.nombre} devolvió '{prestamo.libro.titulo}' "
                f"con {dias_tarde} días de retraso. Multa: ${monto}"
            )
        else:
            print(f"{prestamo.usuario.nombre} devolvió '{prestamo.libro.titulo}' a tiempo")

    def pagar_multas(self, id_usuario):
        usuario = self.usuarios[id_usuario]
        total = usuario.deuda()
        for multa in usuario.multas:
            multa.pagada = True
        print(f"{usuario.nombre} pagó ${total} en multas")


biblioteca = Biblioteca()
biblioteca.agregar_libro(Libro(1, "Rayuela", "Cortázar"))
biblioteca.agregar_libro(Libro(2, "El Aleph", "Borges"))
biblioteca.registrar_usuario(Usuario(1, "Ana"))
biblioteca.registrar_usuario(Usuario(2, "Luis"))

prestamo1 = biblioteca.prestar(1, 1, date(2026, 10, 1))
biblioteca.prestar(1, 2, date(2026, 10, 1))
biblioteca.devolver(prestamo1, date(2026, 10, 20))
biblioteca.prestar(2, 1, date(2026, 10, 21))
biblioteca.pagar_multas(1)
biblioteca.prestar(2, 1, date(2026, 10, 21))
print(f"Préstamos registrados: {len(biblioteca.prestamos)}")