import pulp
import matplotlib.pyplot as plt

# Função que recebe listas de valores e pesos dos itens, e a capacidade da mochila
def resolver_mochila(valores, pesos, capacidade):
    problema = pulp.LpProblem("Problema_da_Mochila", pulp.LpMaximize)
    n = len(valores)
    x = [pulp.LpVariable(f"x{i}", cat='Binary') for i in range(n)]

    problema += pulp.lpSum(valores[i] * x[i] for i in range(n)), "Valor_total"
    problema += pulp.lpSum(pesos[i] * x[i] for i in range(n)) <= capacidade, "Capacidade"

    problema.solve()

    itens_selecionados = [i for i in range(n) if pulp.value(x[i]) == 1]
    valor_total = pulp.value(problema.objective)

    return itens_selecionados, valor_total

def exibir_resultados(itens, valores, pesos, capacidade, valor_total):
    print("Itens selecionados:")
    peso_total = 0
    for i in itens:
        print(f" - Item {i}: Peso = {pesos[i]} kg, Valor = R${valores[i]}")
        peso_total += pesos[i]

    print(f"\nPeso total carregado: {peso_total} kg de {capacidade} kg disponíveis")
    print(f"Valor total: R${valor_total}")

    # Exibir imagem/gráfico
    fig, ax = plt.subplots(figsize=(8, 5))

    # Dados dos itens selecionados
    pesos_selecionados = [pesos[i] for i in itens]
    valores_selecionados = [valores[i] for i in itens]
    labels = [f"Item {i}" for i in itens]

    # Tamanhos para a barra (opcionalmente proporcional ao valor)
    barras = valores_selecionados

    ax.barh(labels, barras, color='skyblue', edgecolor='black')
    ax.set_xlabel('Valor dos Itens (R$)')
    ax.set_title('Itens Selecionados para a Mochila')
    plt.grid(axis='x', linestyle='--', alpha=0.7)
    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    valores = [20, 30, 66, 40, 60]
    pesos = [30, 20, 40, 10, 50]
    capacidade = 50
    itens, valor = resolver_mochila(valores, pesos, capacidade)
    exibir_resultados(itens, valores, pesos, capacidade, valor)

    valores = [500, 400, 300, 350, 200]
    pesos = [5, 7, 4, 6, 3]
    capacidade = 15
    itens, valor = resolver_mochila(valores, pesos, capacidade)
    exibir_resultados(itens, valores, pesos, capacidade, valor)