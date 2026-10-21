def mcd_recursivo(a, b):
    if b == 0:
        return abs(a)
    return mcd_recursivo(b, a % b)


print(mcd_recursivo(8, 12))
print(mcd_recursivo(48, 18))
print(mcd_recursivo(17, 5))