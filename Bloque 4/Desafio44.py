biblioteca = []
def agregar_libro(titulo):
    biblioteca.append(titulo)
    print(f"Libro '{titulo}' agregado.")
def eliminar_libro(titulo):
    if titulo in biblioteca:
       biblioteca.remove(titulo)
       print(f"Libro '{titulo}' eliminado de la biblioteca.")
    else:
       print(f"El libro '{titulo}' no se encontró, no se puede eliminar.")
def buscar_libro(titulo):
    if titulo in biblioteca:
       print(f"El libro '{titulo}' SI está disponible.")
    else:
       print(f"El libro '{titulo}' NO está disponible.")
def mostrar_libros():
    if len(biblioteca) == 0:
        print("La biblioteca está vacía.")
    else:
        print("-- Libros disponibles --")
        for libro in biblioteca:
            print(f"- {libro}")

       agregar_libro("Harry Potter y la piedra filosofal")
       agregar_libro("El Principito")
       agregar_libro("1984")
       agregar_libro("El Resplandor")
mostrar_libros()
buscar_libro("1984")
eliminar_libro("1984")
mostrar_libros()