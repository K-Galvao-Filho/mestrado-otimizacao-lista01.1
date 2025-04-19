# Importa a função para fazer uma cópia profunda da solução (evita alterar o original)
from modulos.solucao import copiar_solucao

# Define a capacidade máxima permitida em cada bin (recipiente)
CAPACIDADE_MAXIMA = 1.0

# Função que gera vizinhos da solução atual
def gerar_vizinhos(solucao):
    # Percorre cada bin da solução
    for i in range(len(solucao)):
        # Percorre cada item dentro do bin i
        for j in range(len(solucao[i])):
            item = solucao[i][j]  # Seleciona o item atual
            
            # Tenta mover o item para outro bin já existente
            for k in range(len(solucao)):
                # Verifica se o bin k é diferente do bin i e se o item cabe no bin k
                if k != i and sum(solucao[k]) + item <= CAPACIDADE_MAXIMA:
                    nova = copiar_solucao(solucao)  # Faz uma cópia da solução atual
                    nova[k].append(item)            # Adiciona o item ao bin k
                    nova[i].remove(item)             # Remove o item do bin original (i)
                    # Retorna a nova solução como vizinho, ignorando bins vazios
                    yield [b for b in nova if b]
            
            # Tenta mover o item para um novo bin (criar um novo recipiente só para ele)
            nova = copiar_solucao(solucao)   # Faz uma cópia da solução atual
            nova.append([item])              # Cria um novo bin contendo apenas o item
            nova[i].remove(item)              # Remove o item do bin original (i)
            # Retorna a nova solução como vizinho, ignorando bins vazios
            yield [b for b in nova if b]
