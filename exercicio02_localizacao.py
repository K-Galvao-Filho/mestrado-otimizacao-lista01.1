# Importa as bibliotecas necessárias
import pulp
import networkx as nx
import matplotlib.pyplot as plt

# Função para resolver o Problema da Localização de Facilidades
def resolver_facility_location(depositos, clientes, custo_instalacao, custo_atendimento):
    problema = pulp.LpProblem("Problema_de_Localizacao_de_Facilidades", pulp.LpMinimize)

    y = {d: pulp.LpVariable(f"y_{d}", cat='Binary') for d in depositos}
    x = {(d, c): pulp.LpVariable(f"x_{d}_{c}", cat='Binary') for d in depositos for c in clientes}

    problema += (
        pulp.lpSum(custo_instalacao[d] * y[d] for d in depositos) +
        pulp.lpSum(custo_atendimento[d][c] * x[(d, c)] for d in depositos for c in clientes)
    ), "Custo_total"

    for c in clientes:
        problema += pulp.lpSum(x[(d, c)] for d in depositos) == 1, f"Cliente_{c}_atendido"

    for d in depositos:
        for c in clientes:
            problema += x[(d, c)] <= y[d], f"Atendimento_{d}_{c}_so_se_aberto"

    problema.solve()

    depositos_abertos = [d for d in depositos if pulp.value(y[d]) == 1]
    atribuicao_clientes = {c: d for d in depositos for c in clientes if pulp.value(x[(d, c)]) == 1}

    return depositos_abertos, atribuicao_clientes

# Função para desenhar o grafo da solução
def desenhar_facility_location(depositos, clientes, depositos_abertos, atribuicao_clientes):
    G = nx.DiGraph()

    for d in depositos:
        cor = 'blue' if d in depositos_abertos else 'gray'
        G.add_node(d, color=cor, tipo='depósito')

    for c in clientes:
        G.add_node(c, color='green', tipo='cliente')

    for c, d in atribuicao_clientes.items():
        G.add_edge(d, c)

    colors = [G.nodes[n]['color'] for n in G.nodes]

    pos = {}
    for i, d in enumerate(depositos):
        pos[d] = (0, i)
    for i, c in enumerate(clientes):
        pos[c] = (2, i)

    nx.draw(G, pos, with_labels=True, node_color=colors, node_size=800, arrows=True)
    plt.title('Solução do Problema de Localização de Facilidades')
    plt.show()

# Função para testar exemplos
def testar_facility_location():
    exemplos = [
        {
            "depositos": ['D1', 'D2', 'D3'],
            "clientes": ['C1', 'C2', 'C3'],
            "custo_instalacao": {'D1': 10, 'D2': 12, 'D3': 8},
            "custo_atendimento": {
                'D1': {'C1': 4, 'C2': 6, 'C3': 8},
                'D2': {'C1': 5, 'C2': 4, 'C3': 3},
                'D3': {'C1': 6, 'C2': 4, 'C3': 5}
            }
        },
        {
            "depositos": ['D1', 'D2', 'D3', 'D4', 'D5'],
            "clientes": ['C1', 'C2', 'C3', 'C4', 'C5', 'C6'],
            "custo_instalacao": {'D1': 9, 'D2': 7, 'D3': 10, 'D4': 8, 'D5': 6},
            "custo_atendimento": {
                'D1': {'C1': 5, 'C2': 6, 'C3': 4, 'C4': 7, 'C5': 8, 'C6': 9},
                'D2': {'C1': 6, 'C2': 5, 'C3': 7, 'C4': 8, 'C5': 9, 'C6': 6},
                'D3': {'C1': 8, 'C2': 9, 'C3': 5, 'C4': 6, 'C5': 7, 'C6': 8},
                'D4': {'C1': 7, 'C2': 6, 'C3': 8, 'C4': 5, 'C5': 6, 'C6': 7},
                'D5': {'C1': 9, 'C2': 8, 'C3': 7, 'C4': 6, 'C5': 5, 'C6': 6}
            }
        },
        {
            "depositos": ['D1', 'D2', 'D3', 'D4', 'D5', 'D6', 'D7', 'D8'],
            "clientes": ['C1', 'C2', 'C3', 'C4', 'C5', 'C6', 'C7', 'C8', 'C9', 'C10', 'C11', 'C12'],
            "custo_instalacao": {'D1': 15, 'D2': 14, 'D3': 13, 'D4': 16, 'D5': 11, 'D6': 12, 'D7': 10, 'D8': 9},
            "custo_atendimento": {
                'D1': {f'C{i}': (i % 5) + 4 for i in range(1, 13)},
                'D2': {f'C{i}': (i % 6) + 3 for i in range(1, 13)},
                'D3': {f'C{i}': (i % 7) + 2 for i in range(1, 13)},
                'D4': {f'C{i}': (i % 4) + 5 for i in range(1, 13)},
                'D5': {f'C{i}': (i % 3) + 6 for i in range(1, 13)},
                'D6': {f'C{i}': (i % 5) + 3 for i in range(1, 13)},
                'D7': {f'C{i}': (i % 4) + 4 for i in range(1, 13)},
                'D8': {f'C{i}': (i % 6) + 5 for i in range(1, 13)}
            }
        }
    ]

    for i, exemplo in enumerate(exemplos, start=1):
        print(f"\nExemplo {i}:")
        depositos_abertos, atribuicao_clientes = resolver_facility_location(
            exemplo["depositos"], exemplo["clientes"],
            exemplo["custo_instalacao"], exemplo["custo_atendimento"]
        )

        print("Depósitos abertos:")
        for d in depositos_abertos:
            print(f"- {d}")

        print("\nAtribuição dos clientes:")
        for c, d in atribuicao_clientes.items():
            print(f"- Cliente {c} atendido pelo depósito {d}")

        desenhar_facility_location(
            exemplo["depositos"], exemplo["clientes"],
            depositos_abertos, atribuicao_clientes
        )

# Bloco principal
def main():
    testar_facility_location()

if __name__ == "__main__":
    main()
