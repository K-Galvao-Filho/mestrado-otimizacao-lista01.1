# Importa a biblioteca time para controlar o tempo de execução
import time

# Importa a função para gerar vizinhos da solução atual
from modulos.vizinhanca import gerar_vizinhos

# Importa a função para avaliar a solução (número de bins usados)
from modulos.solucao import avaliar

# Função de busca local para tentar melhorar a solução inicial
def busca_local(solucao_inicial, tempo_limite):
    inicio = time.time()  # Marca o tempo inicial
    atual = solucao_inicial  # Começa com a solução inicial
    custo_atual = avaliar(atual)  # Avalia o custo da solução inicial (número de bins)

    # Enquanto não ultrapassar o tempo limite
    while time.time() - inicio < tempo_limite:
        melhorou = False  # Flag para verificar se alguma melhoria foi feita

        # Gera todos os vizinhos da solução atual
        for vizinho in gerar_vizinhos(atual):
            # Se encontrar um vizinho melhor (com menos bins)
            if avaliar(vizinho) < custo_atual:
                atual = vizinho           # Atualiza a solução atual
                custo_atual = avaliar(vizinho)  # Atualiza o custo atual
                melhorou = True           # Marca que houve melhoria
                break  # Para no primeiro vizinho que melhorar (First Improvement)

        # Se nenhum vizinho melhorar a solução, encerra a busca
        if not melhorou:
            break

    return atual  # Retorna a melhor solução encontrada
