import time
from modulos.vizinhanca import gerar_vizinhos
from modulos.solucao import avaliar

def busca_local(solucao_inicial, tempo_limite):
    inicio = time.time()
    atual = solucao_inicial
    custo_atual = avaliar(atual)

    while time.time() - inicio < tempo_limite:
        melhorou = False
        for vizinho in gerar_vizinhos(atual):
            if avaliar(vizinho) < custo_atual:
                atual = vizinho
                custo_atual = avaliar(vizinho)
                melhorou = True
                break  # First improvement
        if not melhorou:
            break

    return atual
