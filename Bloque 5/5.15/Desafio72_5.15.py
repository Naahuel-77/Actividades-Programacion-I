codigos = ["A101", "B205", "C310", "D415", "E520"]

codigo = input("Ingresá el código del producto: ").strip().upper()

posicion = None
for i, c in enumerate(codigos):
    if c == codigo:
        posicion = i
        break

if posicion is not None:
    print(f"El código {codigo} se encuentra en la posición {posicion}")
else:
    print(f"El código {codigo} no se ha encontrado")