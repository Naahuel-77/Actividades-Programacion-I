inventario = ["manzanas", "bananas", "zanahorias", "espinacas", "brocoli", "cebolla", "kiwis"]
print(  len(inventario) )

print(inventario[2])

inventario.remove("bananas")
print(inventario)

inventario.append("frutillas")
inventario.append("apio")
inventario.append("papas")
print(inventario)

print("papas" in inventario)
print("tomates" in inventario)
print(inventario)

inventario.remove("espinacas")
inventario.append("dragonfruit")
print(inventario)

inventario.sort()
print(inventario)

fotocopia = inventario.copy()
fotocopia.append("limones")
print(inventario)
print(fotocopia)