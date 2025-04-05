from modulos.solucao import copiar_solucao

CAPACIDADE_MAXIMA = 1.0

def construir_solucao_inicial(itens):
    bins = []
    for item in itens:
        colocado = False
        for b in bins:
            if sum(b) + item <= CAPACIDADE_MAXIMA:
                b.append(item)
                colocado = True
                break
        if not colocado:
            bins.append([item])
    return copiar_solucao(bins)
