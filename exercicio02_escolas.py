# Importa bibliotecas
import pulp
import matplotlib.pyplot as plt
import networkx as nx
import random

# Função para resolver o Problema de Cobertura de Conjuntos
def resolver_cobertura(elementos, subconjuntos):
    problema = pulp.LpProblem("Problema_de_Cobertura_de_Conjuntos", pulp.LpMinimize)
    x = {s: pulp.LpVariable(f"x_{s}", cat='Binary') for s in subconjuntos}
    problema += pulp.lpSum(x[s] for s in subconjuntos), "Minimizar_numero_de_escolas"

    for e in elementos:
        problema += pulp.lpSum(x[s] for s in subconjuntos if e in subconjuntos[s]) >= 1, f"Cobrir_{e}"

    problema.solve()

    escolas_selecionadas = [s for s in subconjuntos if pulp.value(x[s]) == 1]
    return escolas_selecionadas

# Função para desenhar o grafo inicial (todos os elementos interconectados se aparecem juntos)
def desenhar_grafo_inicial(nome_exemplo, elementos, subconjuntos):
    G = nx.Graph()

    G.add_nodes_from(elementos)

    for s in subconjuntos:
        itens = subconjuntos[s]
        for i in range(len(itens)):
            for j in range(i + 1, len(itens)):
                G.add_edge(itens[i], itens[j])

    pos = nx.spring_layout(G, seed=42)

    plt.figure(figsize=(10, 6))
    nx.draw(G, pos, with_labels=True, node_color='lightblue', node_size=1000, edge_color='gray', font_size=10)

    plt.title(f"{nome_exemplo}: Grafo Inicial (antes da otimização)", fontsize=14)
    plt.axis('off')
    plt.show()

# Função para desenhar o grafo otimizado (após seleção dos subconjuntos)
def desenhar_grafo_otimizado(nome_exemplo, elementos, subconjuntos, selecionados):
    G = nx.Graph()

    G.add_nodes_from(elementos)

    subconjuntos_filtrados = {k: v for k, v in subconjuntos.items() if k in selecionados}

    for s in subconjuntos_filtrados:
        itens = subconjuntos_filtrados[s]
        for i in range(len(itens)):
            for j in range(i + 1, len(itens)):
                G.add_edge(itens[i], itens[j])

    pos = nx.spring_layout(G, seed=42)

    plt.figure(figsize=(10, 6))
    nx.draw(G, pos, with_labels=True, node_color='lightgreen', node_size=1000, edge_color='gray', font_size=10)

    plt.title(f"{nome_exemplo}: Grafo Otimizado (após seleção)", fontsize=14)
    plt.axis('off')
    plt.show()

# Função para testar um exemplo específico
def testar_exemplo(nome_exemplo, elementos, subconjuntos):
    print(f"\n{nome_exemplo}")
    escolas = resolver_cobertura(elementos, subconjuntos)
    print("Escolas selecionadas para cobertura:")
    for escola in escolas:
        print(f"- {escola} (cobre {subconjuntos[escola]})")
    desenhar_grafo_inicial(nome_exemplo, elementos, subconjuntos)
    desenhar_grafo_otimizado(nome_exemplo, elementos, subconjuntos, escolas)

# Bloco principal para vários testes
def main():
    # Exemplo 1
    elementos1 = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']
    subconjuntos1 = {
        'Escola1': ['A', 'B', 'C'],
        'Escola2': ['C', 'D', 'E'],
        'Escola3': ['E', 'F'],
        'Escola4': ['F', 'G', 'H'],
        'Escola5': ['B', 'D', 'G']
    }
    testar_exemplo("Exemplo 1", elementos1, subconjuntos1)

    # Exemplo 2
    elementos2 = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
    subconjuntos2 = {
        'Centro1': ['1', '2', '3'],
        'Centro2': ['2', '4', '5'],
        'Centro3': ['3', '6', '7'],
        'Centro4': ['5', '7', '8'],
        'Centro5': ['6', '8', '9']
    }
    testar_exemplo("Exemplo 2", elementos2, subconjuntos2)

    # Exemplo 3
    elementos3 = ['X1', 'X2', 'X3', 'Y1', 'Y2', 'Y3', 'Z1', 'Z2']
    subconjuntos3 = {
        'Ponto1': ['X1', 'Y1', 'Z1'],
        'Ponto2': ['X2', 'Y2'],
        'Ponto3': ['X3', 'Y3', 'Z2'],
        'Ponto4': ['Y1', 'Y2', 'Y3'],
        'Ponto5': ['Z1', 'Z2']
    }
    testar_exemplo("Exemplo 3", elementos3, subconjuntos3)

if __name__ == "__main__":
    main()
