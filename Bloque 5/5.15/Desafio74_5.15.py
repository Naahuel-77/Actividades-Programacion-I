from itertools import zip_longest

lista1 = [1, 2, 3, 4, 5]
lista2 = [10, 20, 30]

suma = [a + b for a, b in zip_longest(lista1, lista2, fillvalue=0)]

print("Lista 1:", lista1)
print("Lista 2:", lista2)
print("Suma:", suma)

print(
    [a + b for a, b in zip_longest([7], [1, 2, 3], fillvalue=0)]
)
print(
    [a + b for a, b in zip_longest([], [], fillvalue=0)]
)