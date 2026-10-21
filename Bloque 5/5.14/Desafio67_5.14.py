try:
    num1 = int(input("Ingrese el primer número: " ))
    num2 = int(input("Ingrese el segundo número: " ))
    print(num1 / num2)
except ValueError:
    print("Error: debe ingresar números enteros")
except ZeroDivisionError:
    print("Error: No se puede dividir por cero")