nombre = input("Ingrese nombre del producto: ")
cantidad = int(input("Ingrese la cantidad: "))
precio = float(input("Ingrese el precio: "))

subtotal = cantidad * precio

print("===== FACTURA =====")
print(f"Producto: {nombre}")
print(f"Cantidad: {cantidad}")
print(f"Precio: ${precio:.2f}")
print(f"Subtotal: ${subtotal:.2f}")
