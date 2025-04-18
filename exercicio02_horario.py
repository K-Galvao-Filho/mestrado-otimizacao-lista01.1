# Importa as bibliotecas necessárias
import pulp
import matplotlib.pyplot as plt

# Função para resolver o Problema de Escalonamento de Horários
def resolver_escalonamento(demanda):
    dias = len(demanda)
    problema = pulp.LpProblem("Problema_de_Escalonamento", pulp.LpMinimize)

    # Variáveis: x[i] = número de trabalhadores que começam no dia i
    x = {i: pulp.LpVariable(f"x_{i}", lowBound=0, cat='Integer') for i in range(dias)}

    # Função objetivo: minimizar o número total de trabalhadores
    problema += pulp.lpSum(x[i] for i in range(dias)), "Minimizar_total_trabalhadores"

    # Restrição: atender a demanda de cada dia
    for d in range(dias):
        problema += pulp.lpSum(x[(d - i) % dias] for i in range(5)) >= demanda[d], f"Demanda_dia_{d}"

    # Resolve o problema
    problema.solve()

    # Extrai a quantidade de trabalhadores começando em cada dia
    escalonamento = {i: int(pulp.value(x[i])) for i in range(dias)}

    return escalonamento

# Função para plotar a demanda e escalonamento
def plotar_escalonamento(demanda, escalonamento, nome_exemplo):
    dias_semana = ['Dom', 'Seg', 'Ter', 'Qua', 'Qui', 'Sex', 'Sab']
    dias = range(len(demanda))

    fig, ax = plt.subplots(figsize=(10,6))

    ax.bar(dias, demanda, label='Demanda', alpha=0.7)
    ax.bar(dias, [escalonamento[i] for i in dias], label='Trabalhadores Iniciando', alpha=0.7)

    ax.set_xticks(dias)
    ax.set_xticklabels(dias_semana)
    ax.set_ylabel('Quantidade')
    ax.set_title(nome_exemplo)
    ax.legend()

    plt.grid(True, linestyle='--', alpha=0.5)
    plt.tight_layout()
    plt.show()

# Função para testar um exemplo de escalonamento
def testar_escalonamento(nome_exemplo, demanda):
    print(f"\n{nome_exemplo}")
    escalonamento = resolver_escalonamento(demanda)
    print("Trabalhadores iniciando em cada dia:")
    dias_semana = ['Dom', 'Seg', 'Ter', 'Qua', 'Qui', 'Sex', 'Sab']
    for i in range(len(demanda)):
        print(f"- {dias_semana[i]}: {escalonamento[i]} trabalhador(es)")

    # Plota o gráfico
    plotar_escalonamento(demanda, escalonamento, nome_exemplo)

# Bloco principal para testar vários exemplos
def main():
    # Exemplo 1
    demanda1 = [3, 2, 4, 5, 3, 2, 4]  # Domingo a Sábado
    testar_escalonamento("Exemplo 1 de Escalonamento de Horários", demanda1)

    # Exemplo 2
    demanda2 = [2, 3, 5, 4, 2, 1, 3]  # Domingo a Sábado
    testar_escalonamento("Exemplo 2 de Escalonamento de Horários", demanda2)

    # Exemplo 3
    demanda3 = [4, 4, 4, 4, 4, 4, 4]  # Demanda constante todos os dias
    testar_escalonamento("Exemplo 3 de Escalonamento de Horários", demanda3)

if __name__ == "__main__":
    main()
