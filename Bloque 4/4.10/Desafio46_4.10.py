cadena = {
    "Centro": {
        "productos": {
            "Yerba": {"precio": 500, "stock": 40},
            "Café": {"precio": 800, "stock": 25},
        },
        "empleados": ["Ana", "Luis"],
        "transacciones": [],
    },
    "Costa": {
        "productos": {
            "Yerba": {"precio": 520, "stock": 30},
            "Azúcar": {"precio": 300, "stock": 50},
        },
        "empleados": ["Marta"],
        "transacciones": [],
    },
}


def vender(cadena, tienda, producto, cantidad, empleado):
    datos = cadena[tienda]
    if empleado not in datos["empleados"]:
        print(f"{empleado} no trabaja en {tienda}")
        return False
    item = datos["productos"].get(producto)
    if item is None:
        print(f"{tienda} no tiene {producto}")
        return False
    if item["stock"] < cantidad:
        print(f"Stock insuficiente de {producto} en {tienda}")
        return False
    item["stock"] -= cantidad
    total = item["precio"] * cantidad
    datos["transacciones"].append(
        {"producto": producto, "cantidad": cantidad, "empleado": empleado, "total": total}
    )
    print(f"{empleado} vendió {cantidad} {producto} en {tienda} por ${total}")
    return True


def total_vendido(cadena, tienda):
    return sum(t["total"] for t in cadena[tienda]["transacciones"])


def stock_total(cadena, producto):
    return sum(
        datos["productos"][producto]["stock"]
        for datos in cadena.values()
        if producto in datos["productos"]
    )


vender(cadena, "Centro", "Yerba", 5, "Ana")
vender(cadena, "Centro", "Café", 30, "Luis")
vender(cadena, "Costa", "Yerba", 10, "Marta")
vender(cadena, "Costa", "Café", 1, "Marta")
vender(cadena, "Costa", "Azúcar", 2, "Ana")

print(f"Total vendido en Centro: ${total_vendido(cadena, 'Centro')}")
print(f"Total vendido en Costa: ${total_vendido(cadena, 'Costa')}")
print(f"Stock total de Yerba: {stock_total(cadena, 'Yerba')}")