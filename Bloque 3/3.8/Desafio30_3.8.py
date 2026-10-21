def mcd(a, b):
    while b != 0:
        a, b = b, a % b
    return abs(a)


print(mcd(48, 18))
print(mcd(100, 75))
print(mcd(17, 5))