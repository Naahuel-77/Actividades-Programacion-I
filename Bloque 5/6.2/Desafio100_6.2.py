torneos = {
    "Verano": {"ana", "luis", "marta", "pedro", "sofia"},
    "Otoño": {"ana", "marta", "diego", "lucia", "sofia"},
    "Invierno": {"ana", "tomas", "lucia", "marta", "sofia", "carlos"},
    "Primavera": {"ana", "marta", "sofia", "julia", "pedro", "carlos"},
}

participantes = list(torneos.values())

en_todos = set.intersection(*participantes)

solo_un_torneo = set()
for nombre, atletas in torneos.items():
    otros = set.union(*(a for n, a in torneos.items() if n != nombre))
    solo_un_torneo |= atletas - otros

total_unicos = set.union(*participantes)

print("Participaron en todos los torneos:")
print(sorted(en_todos))

print("Participaron en un único torneo:")
print(sorted(solo_un_torneo))

print(f"Total de atletas únicos en el año: {len(total_unicos)}")