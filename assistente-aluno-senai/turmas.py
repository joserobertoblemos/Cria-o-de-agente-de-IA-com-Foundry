# ============================================================
# FUNÇÃO FICTÍCIA PARA CONSULTA DE TURMAS
# ============================================================

TURMAS = [
    {
        "curso": "Eletricista Industrial",
        "turma": "EI-2026-01",
        "horario": "18:30 às 22:30",
        "dias": "Segunda a Quinta",
        "vagas": 8,
        "status": "Inscrições abertas"
    },
    {
        "curso": "Eletricista Industrial",
        "turma": "EI-2026-02",
        "horario": "08:00 às 12:00",
        "dias": "Segunda a Sexta",
        "vagas": 3,
        "status": "Inscrições abertas"
    },
    {
        "curso": "Mecânico de Máquinas Industriais",
        "turma": "MMI-2026-01",
        "horario": "18:30 às 22:30",
        "dias": "Segunda a Quinta",
        "vagas": 5,
        "status": "Inscrições abertas"
    },
    {
        "curso": "Assistente Administrativo",
        "turma": "AA-2026-01",
        "horario": "13:30 às 17:30",
        "dias": "Segunda a Sexta",
        "vagas": 10,
        "status": "Inscrições abertas"
    }
]


def consultar_turmas(curso: str):
    """
    Consulta as turmas fictícias disponíveis
    para um determinado curso.
    """

    resultados = []

    for turma in TURMAS:
        if curso.lower() in turma["curso"].lower():
            resultados.append(turma)

    if not resultados:
        return {
            "encontrado": False,
            "mensagem": f"Nenhuma turma encontrada para o curso '{curso}'."
        }

    return {
        "encontrado": True,
        "quantidade": len(resultados),
        "turmas": resultados
    }