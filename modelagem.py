custos = [
    [12, 18, 15, 22, 9, 14, 20, 11, 17],
    [19, 8, 13, 25, 16, 10, 7, 21, 24],
    [6, 14, 27, 10, 12, 19, 23, 16, 8],
    [17, 11, 20, 9, 18, 13, 25, 14, 22],
    [10, 23, 16, 14, 7, 21, 12, 19, 15],
    [13, 25, 9, 17, 11, 8, 16, 22, 20],
    [21, 16, 24, 12, 20, 15, 9, 18, 10],
    [8, 19, 11, 16, 22, 17, 14, 10, 13],
    [15, 10, 18, 21, 13, 12, 22, 9, 16]
]


def custo(empresa, projeto):
    return custos[empresa][projeto]


def custo_total(solucao):
    total = 0
    for i in range(len(custos)):
        for j in solucao:
            total += custos[j][i]
            break
    return total


def trocar_empresa(solucao, posicao1, posicao2):
    solucao[posicao1], solucao[posicao2] = solucao[posicao2], solucao[posicao1]
    return solucao


def tamanho_matriz():
    return len(custos)
