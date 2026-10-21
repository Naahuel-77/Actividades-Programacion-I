def tienen_elemento_comun(lista1, lista2):
    for elemento in lista1:
        if elemento in lista2:
            return True
    return False


print(tienen_elemento_comun([1, 2, 3], [4, 5, 3]))
print(tienen_elemento_comun([1, 2, 3], [4, 5, 6]))