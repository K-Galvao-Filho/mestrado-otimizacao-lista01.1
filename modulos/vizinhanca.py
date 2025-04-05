from modulos.solucao import copiar_solucao

CAPACIDADE_MAXIMA = 1.0

def gerar_vizinhos(solucao):
    for i in range(len(solucao)):
        for j in range(len(solucao[i])):
            item = solucao[i][j]
            for k in range(len(solucao)):
                if k != i and sum(solucao[k]) + item <= CAPACIDADE_MAXIMA:
                    nova = copiar_solucao(solucao)
                    nova[k].append(item)
                    nova[i].remove(item)
                    yield [b for b in nova if b]
            # Tentar mover para novo bin
            nova = copiar_solucao(solucao)
            nova.append([item])
            nova[i].remove(item)
            yield [b for b in nova if b]
