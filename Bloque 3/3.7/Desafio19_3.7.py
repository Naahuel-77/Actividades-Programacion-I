codigos = [405, 222, 707, 150, 821]
ordenados = sorted(codigos, reverse=True)
print(ordenados)
print(codigos)

# ¿Por qué es importante no modificar la lista original?
# Porque si la ordeno y pierdo el orden original, no lo puedo recuperar. Esa lista puede hacer falta en su orden original para otra parte del programa, y si la cambio puedo generar errores.


# ¿Por qué no puedo usar sort sobre la original?
# Porque sort() modifica la lista misma, la deja ordenada y se pierde el orden original. En cambio sorted() devuelve una lista nueva y deja la original como estaba.
