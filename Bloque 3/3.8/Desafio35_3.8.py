import random
import string


def generar_contrasena(longitud=8):
    contrasena = [
        random.choice(string.ascii_lowercase),
        random.choice(string.ascii_uppercase),
        random.choice(string.digits),
    ]
    todos = string.ascii_letters + string.digits
    for _ in range(longitud - 3):
        contrasena.append(random.choice(todos))
    random.shuffle(contrasena)
    return "".join(contrasena)


print(generar_contrasena())