def agregar_libro(biblioteca, titulo):
    biblioteca.append(titulo)
    print(f"Libro '{titulo}' agregado.")
def eliminar_libro(biblioteca, titulo):
    if titulo in biblioteca:
        biblioteca.remove(titulo)
        print(f"Libro '{titulo}' eliminado de la biblioteca.")
    else:
        print(f"El libro '{titulo}' no se encontró, no se puede eliminar.")
def buscar_libro(biblioteca, titulo):
    if titulo in biblioteca:
        print(f"El libro '{titulo}' SI está disponible.")
    else:
        print(f"El libro '{titulo}' NO está disponible.")
def mostrar_libros(biblioteca):
    if len(biblioteca) == 0:
        print("La biblioteca está vacía.")
    else:
        print("-- Libros disponibles --")
        for libro in biblioteca:
            print(f"- {libro}")
biblioteca_principal = []
biblioteca_secundaria = []
agregar_libro(biblioteca_principal, "Harry Potter y la piedra filosofal")
agregar_libro(biblioteca_principal, "1984")
agregar_libro(biblioteca_secundaria, "El Resplandor")
agregar_libro(biblioteca_secundaria, "El Principito")
buscar_libro(biblioteca_principal, "1984")
eliminar_libro(biblioteca_secundaria, "El Resplandor")
mostrar_libros(biblioteca_principal)
mostrar_libros(biblioteca_secundaria)