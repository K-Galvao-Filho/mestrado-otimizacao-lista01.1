# Importa a função copiar_solucao para fazer uma cópia segura da solução
from modulos.solucao import copiar_solucao

# Define a capacidade máxima permitida em cada bin
CAPACIDADE_MAXIMA = 1.0

# Função para construir uma solução inicial simples
def construir_solucao_inicial(itens):
    bins = []  # Lista para armazenar os bins (caixas ou recipientes)

    # Para cada item na lista de itens
    for item in itens:
        colocado = False  # Flag para verificar se o item foi colocado em algum bin

        # Tenta colocar o item em algum bin já existente
        for b in bins:
            if sum(b) + item <= CAPACIDADE_MAXIMA:  # Se couber no bin
                b.append(item)  # Adiciona o item ao bin
                colocado = True  # Marca como colocado
                break  # Não precisa testar outros bins, já foi colocado

        # Se o item não coube em nenhum bin existente
        if not colocado:
            bins.append([item])  # Cria um novo bin apenas com esse item

    # Retorna uma cópia da solução construída (sem bins vazios)
    return copiar_solucao(bins)
