# Importa as bibliotecas necessárias
import pulp
import matplotlib.pyplot as plt
import itertools

# Função para resolver o Problema de Corte de Estoque
def resolver_corte_estoque(tamanho_barra, tamanhos_pecas, demandas):
    problema = pulp.LpProblem("Problema_de_Corte_de_Estoque", pulp.LpMinimize)

    # Geração dinâmica dos padrões possíveis (todas combinações viáveis)
    padroes = []
    for combinacao in itertools.product(range(tamanho_barra + 1), repeat=len(tamanhos_pecas)):
        comprimento_total = sum(combinacao[i] * tamanhos_pecas[i] for i in range(len(tamanhos_pecas)))
        if 0 < comprimento_total <= tamanho_barra:
            padroes.append(list(combinacao))

    # Variáveis: número de vezes que cada padrão será usado
    x = [pulp.LpVariable(f"x_{i}", lowBound=0, cat='Integer') for i in range(len(padroes))]

    # Função objetivo: minimizar o número de barras usadas
    problema += pulp.lpSum(x)

    # Restrições: atender a demanda de cada peça
    for j in range(len(tamanhos_pecas)):
        problema += pulp.lpSum(padroes[i][j] * x[i] for i in range(len(padroes))) >= demandas[j], f"Demanda_peca_{j}"

    # Resolve o problema
    problema.solve()

    # Resultados
    padroes_utilizados = [(padroes[i], int(pulp.value(x[i]))) for i in range(len(padroes)) if pulp.value(x[i]) > 0]

    return padroes_utilizados

# Função para desenhar os cortes
def desenhar_cortes(tamanho_barra, tamanhos_pecas, padroes_utilizados):
    fig, ax = plt.subplots(figsize=(10, len(padroes_utilizados) * 0.6))

    barra_idx = 1
    for padrao, quantidade in padroes_utilizados:
        for q in range(quantidade):
            left = 0
            for peca_idx, num_pecas in enumerate(padrao):
                for _ in range(num_pecas):
                    ax.barh(f"Barra {barra_idx}", tamanhos_pecas[peca_idx], left=left, edgecolor='black')
                    left += tamanhos_pecas[peca_idx]
            barra_idx += 1

    ax.set_xlabel('Comprimento')
    ax.set_title('Padrões de Corte Utilizados')
    plt.tight_layout()
    plt.show()

# Função para testar exemplos maiores
def testar_corte_estoque():
    exemplos = [
        (10, [3, 5], [4, 2]),
        (15, [4, 5, 6], [6, 4, 5]),
        (20, [5, 7, 9], [8, 6, 7])
    ]

    for idx, (tamanho_barra, tamanhos_pecas, demandas) in enumerate(exemplos, start=1):
        print(f"\nExemplo {idx}:")
        padroes_utilizados = resolver_corte_estoque(tamanho_barra, tamanhos_pecas, demandas)

        print("Padrões de corte utilizados (formato: [quantidade de cada peça], vezes utilizado):")
        for padrao, qtd in padroes_utilizados:
            print(f"{padrao} usado {qtd} vez(es)")

        desenhar_cortes(tamanho_barra, tamanhos_pecas, padroes_utilizados)

# Bloco principal
def main():
    testar_corte_estoque()

if __name__ == "__main__":
    main()
