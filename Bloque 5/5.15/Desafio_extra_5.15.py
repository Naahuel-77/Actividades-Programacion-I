a = int(input("Ingresá el primer número: "))
b = int(input("Ingresá el segundo número: "))
c = int(input("Ingresá el tercer número: "))

if a == b == c:
    print(f"Los tres números son iguales ({a})")
else:
    mayor = max(a, b, c)
    repetido = [a, b, c].count(mayor)
    if repetido == 1:
        print(f"El número mayor es {mayor}")
    else:
        print(f"El número mayor es {mayor} (aparece {repetido} veces)")