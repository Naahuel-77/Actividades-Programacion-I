registros = [
    ("2026-01-10", "ana", "gripe"),
    ("2026-02-15", "luis", "fractura"),
    ("2026-03-02", "ana", "alergia"),
    ("2026-03-20", "marta", "gripe"),
    ("2026-04-05", "ana", "gripe"),
    ("2026-05-12", "luis", "migraña"),
]


def historial_paciente(paciente):
    return [registro for registro in registros if registro[1] == paciente]


def mostrar_historial(paciente):
    historial = historial_paciente(paciente)
    if not historial:
        print(f"No hay registros para el paciente {paciente}")
        return
    print(f"Historial de {paciente}:")
    for fecha, _, diagnostico in historial:
        print(f"{fecha} - {diagnostico}")


def contar_diagnosticos_distintos():
    return len({diagnostico for _, _, diagnostico in registros})


mostrar_historial("ana")
mostrar_historial("pedro")
print(f"Diagnósticos distintos registrados: {contar_diagnosticos_distintos()}")