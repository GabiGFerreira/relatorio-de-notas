alunos_notas = [
    {"matricula": 1, "nome": "Israel", "notas": [6.5, 9, 8]},
    {"matricula": 2, "nome": "Felipe", "notas": [3, 4.5, 6]},
    {"matricula": 3, "nome": "Nathan", "notas": [7, 8, 8.5]}
]

def calcular_media(notas):
    if not notas:
        return 0
    return sum(notas) / len(notas)

"""
Calcula a média das notas de cada aluno

Args:
    notas list[float]: dados das notas de aluno

Returns:
    float: Resultado do cálculo da média das notas de aluno
"""


def verificar_aprovacao(media, media_minima=7.0):

    """
    Verifica se a média das notas é suficiente para aprovação, de cada aluno

    Args:
        media (float): média das notas do aluno
        media_minima=7.0 (float): nota mínima necessária para aprovação, 7.0

    Returns:
        str: Se média das notas acima de 7, aluno está "aprovado". Caso contrário, "reprovado".

    """

    if media >= media_minima:
        return "Aprovado"
    else:
        return "Reprovado"


def gerar_relatorios(alunos):

    """
    Gera um relatório de cada aluno, contendo, respectivamente, seu nome, média de suas notas e sua situação de aprovação

    Args:
        alunos (list[dict]): dados dos alunos, contendo:
            "nome" (str): nome do aluno
            "notas" list[float]: notas do aluno

    Returns:
        Não há retorno, apenas imprime relatório

    """

    print(f"Nome | Média | Situação")

    for aluno in alunos:
        media = calcular_media(aluno["notas"])
        situacao = verificar_aprovacao(media)

        print(f"{aluno['nome']} {media:.1f} {situacao}")


if __name__ == '__main__':
    gerar_relatorios(alunos_notas)

