def imprimir_solucao(solucao):
    for i, b in enumerate(solucao):
        print(f"Bin {i+1}: {b} (total: {sum(b):.2f})")

def imprimir_solucao_ordenada(solucao):
    # Ordenar bins pelo total (soma dos itens) do maior para o menor
    bins_ordenados = sorted(solucao, key=lambda b: sum(b), reverse=True)
    for i, b in enumerate(bins_ordenados):
        b_itens_ordenados = sorted(b, reverse=True)  # Itens dentro do bin do maior para o menor
        print(f"Bin {i+1}: {b_itens_ordenados} (total: {sum(b_itens_ordenados):.2f})")