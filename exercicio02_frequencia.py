# Importa as bibliotecas necessárias
import pulp
import networkx as nx
import matplotlib.pyplot as plt

# Função para resolver o Problema de Atribuição de Frequências (Coloração de Grafos)
def resolver_atribuicao_frequencias(vertices, arestas, cores):
    problema = pulp.LpProblem("Problema_de_Atribuicao_de_Frequencias", pulp.LpMinimize)

    x = {(v, c): pulp.LpVariable(f"x_{v}_{c}", cat='Binary') for v in vertices for c in cores}
    y = {c: pulp.LpVariable(f"y_{c}", cat='Binary') for c in cores}

    problema += pulp.lpSum(y[c] for c in cores), "Minimizar_numero_de_cores"

    for v in vertices:
        problema += pulp.lpSum(x[v, c] for c in cores) == 1, f"Uma_cor_para_{v}"

    for (v, u) in arestas:
        for c in cores:
            problema += x[v, c] + x[u, c] <= y[c], f"Sem_conflito_{v}_{u}_cor_{c}"

    problema.solve()

    atribuicao = {v: c for v in vertices for c in cores if pulp.value(x[v, c]) == 1}

    return atribuicao

# Função para desenhar o grafo com as frequências atribuídas
def desenhar_grafo(vertices, arestas, atribuicao):
    G = nx.Graph()
    G.add_nodes_from(vertices)
    G.add_edges_from(arestas)

    cor_mapa = {
        1: 'red',
        2: 'blue',
        3: 'green',
        4: 'orange',
        5: 'purple',
        6: 'cyan',
        7: 'magenta'
    }
    cores = [cor_mapa.get(atribuicao[v], 'gray') for v in vertices]

    pos = nx.spring_layout(G)
    nx.draw(G, pos, with_labels=True, node_color=cores, node_size=800, font_weight='bold')
    plt.title("Atribuição de Frequências (Coloração de Grafo)")
    plt.show()

# Função para testar um exemplo específico
def testar_frequencias(nome_exemplo, vertices, arestas, cores):
    print(f"\n{nome_exemplo}")
    atribuicao = resolver_atribuicao_frequencias(vertices, arestas, cores)
    print("Frequências atribuídas a cada vértice:")
    for v in atribuicao:
        print(f"- Vértice {v}: Frequência {atribuicao[v]}")

    desenhar_grafo(vertices, arestas, atribuicao)

# Bloco principal para testar vários exemplos
def main():
    # Exemplo 1
    vertices1 = ['A', 'B', 'C', 'D']
    arestas1 = [('A', 'B'), ('A', 'C'), ('B', 'C'), ('B', 'D'), ('C', 'D')]
    cores1 = [1, 2, 3]
    testar_frequencias("Exemplo 1 de Atribuição de Frequências", vertices1, arestas1, cores1)

    # Exemplo 2
    vertices2 = ['1', '2', '3', '4', '5']
    arestas2 = [('1', '2'), ('2', '3'), ('3', '4'), ('4', '5'), ('1', '5')]
    cores2 = [1, 2, 3]
    testar_frequencias("Exemplo 2 de Atribuição de Frequências", vertices2, arestas2, cores2)

    # Exemplo 3
    vertices3 = ['P', 'Q', 'R', 'S', 'T', 'U']
    arestas3 = [('P', 'Q'), ('Q', 'R'), ('R', 'S'), ('S', 'T'), ('T', 'U'), ('U', 'P'), ('P', 'R'), ('Q', 'S')]
    cores3 = [1, 2, 3, 4]
    testar_frequencias("Exemplo 3 de Atribuição de Frequências", vertices3, arestas3, cores3)

if __name__ == "__main__":
    main()