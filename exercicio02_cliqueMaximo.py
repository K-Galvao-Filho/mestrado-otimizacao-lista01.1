# Importa as bibliotecas necessárias
import pulp
import networkx as nx
import matplotlib.pyplot as plt

# Função para resolver o Problema da Clique Máxima
def resolver_clique_maxima(vertices, arestas):
    problema = pulp.LpProblem("Problema_da_Clique_Maxima", pulp.LpMaximize)

    # Cria variáveis binárias para cada vértice
    x = {v: pulp.LpVariable(f"x_{v}", cat='Binary') for v in vertices}

    # Função objetivo: maximizar o número de vértices escolhidos
    problema += pulp.lpSum(x[v] for v in vertices), "Maximizar_tamanho_da_clique"

    # Restrição: se dois vértices não são adjacentes, não podem ambos estar na clique
    for i in vertices:
        for j in vertices:
            if i != j and (i, j) not in arestas and (j, i) not in arestas:
                problema += x[i] + x[j] <= 1, f"Restricao_{i}_{j}"

    problema.solve()

    clique = [v for v in vertices if pulp.value(x[v]) == 1]

    return clique

# Função para desenhar o grafo
def desenhar_grafo(vertices, arestas, clique, nome):
    G = nx.Graph()
    G.add_nodes_from(vertices)
    G.add_edges_from(arestas)

    pos = nx.spring_layout(G, seed=42)

    plt.figure(figsize=(8, 6))
    # Desenha nós
    nx.draw_networkx_nodes(G, pos, nodelist=vertices, node_color='lightblue', node_size=700)
    nx.draw_networkx_edges(G, pos, edgelist=arestas, width=2)
    nx.draw_networkx_labels(G, pos, font_size=12, font_weight='bold')

    # Destaca a clique
    if clique:
        clique_arestas = [(i, j) for i in clique for j in clique if i != j and (i, j) in arestas or (j, i) in arestas]
        nx.draw_networkx_nodes(G, pos, nodelist=clique, node_color='red', node_size=800)
        nx.draw_networkx_edges(G, pos, edgelist=clique_arestas, edge_color='red', width=3)

    plt.title(nome)
    plt.axis('off')
    plt.show()

# Função para testar um exemplo específico
def testar_clique(nome_exemplo, vertices, arestas):
    print(f"\n{nome_exemplo}")
    clique = resolver_clique_maxima(vertices, arestas)
    print("Vértices da clique máxima encontrada:")
    for v in clique:
        print(f"- {v}")
    desenhar_grafo(vertices, arestas, clique, nome_exemplo)

# Bloco principal para testar vários exemplos
def main():
    vertices1 = ['A', 'B', 'C', 'D', 'E']
    arestas1 = [('A', 'B'), ('A', 'C'), ('B', 'C'), ('B', 'D'), ('C', 'D'), ('D', 'E')]
    testar_clique("Exemplo 1 de Clique Máxima", vertices1, arestas1)

    vertices2 = ['1', '2', '3', '4']
    arestas2 = [('1', '2'), ('2', '3'), ('3', '4'), ('1', '3'), ('2', '4')]
    testar_clique("Exemplo 2 de Clique Máxima", vertices2, arestas2)

    vertices3 = ['X', 'Y', 'Z', 'W']
    arestas3 = [('X', 'Y'), ('Y', 'Z'), ('Z', 'W'), ('X', 'W')]
    testar_clique("Exemplo 3 de Clique Máxima", vertices3, arestas3)

if __name__ == "__main__":
    main()