ventas = [
    (101, 3, 10.0),
    (102, 1, 25.5),
    (101, 2, 10.0),
    (103, 6, 4.0),
    (102, 2, 25.5),
    (104, 1, 100.0),
]

ingreso_total = sum(cantidad * precio for _, cantidad, precio in ventas)

cantidades_por_producto = {}
for id_producto, cantidad, _ in ventas:
    cantidades_por_producto[id_producto] = cantidades_por_producto.get(id_producto, 0) + cantidad

mas_vendido = max(cantidades_por_producto, key=cantidades_por_producto.get)

print(f"Ventas registradas: {len(ventas)}")
print(f"Ingreso total: ${ingreso_total:.2f}")
print(f"Producto más vendido: {mas_vendido} ({cantidades_por_producto[mas_vendido]} unidades)")