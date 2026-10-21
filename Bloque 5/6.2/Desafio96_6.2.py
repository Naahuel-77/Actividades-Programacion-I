inventario = {}


def agregar_producto(codigo, nombre, precio, stock):
    if codigo in inventario:
        print(f"El producto {codigo} ya existe")
        return
    inventario[codigo] = {"nombre": nombre, "precio": precio, "stock": stock}
    print(f"Producto {codigo} agregado")


def actualizar_stock(codigo, nuevo_stock):
    if codigo not in inventario:
        print(f"El producto {codigo} no existe")
        return
    inventario[codigo]["stock"] = nuevo_stock
    print(f"Stock de {codigo} actualizado a {nuevo_stock}")


def buscar_producto(codigo):
    if codigo not in inventario:
        print(f"El producto {codigo} no existe")
        return
    detalles = inventario[codigo]
    print(f"Código: {codigo}")
    print(f"Nombre: {detalles['nombre']}")
    print(f"Precio: ${detalles['precio']:.2f}")
    print(f"Stock: {detalles['stock']}")


agregar_producto("A001", "Cuaderno", 3.5, 40)
agregar_producto("A002", "Lapicera", 1.2, 100)
agregar_producto("A001", "Carpeta", 5.0, 10)
actualizar_stock("A002", 85)
actualizar_stock("A999", 10)
buscar_producto("A002")
buscar_producto("A999")