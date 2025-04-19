# Função para imprimir a solução atual, mostrando os itens em cada bin
def imprimir_solucao(solucao):
    # Percorre cada bin da solução, com seu índice
    for i, b in enumerate(solucao):
        # Imprime o número do bin, os itens que ele contém e o total da soma dos itens
        print(f"Bin {i+1}: {b} (total: {sum(b):.2f})")

# Função para imprimir a solução de forma ordenada
def imprimir_solucao_ordenada(solucao):
    # Ordena os bins pela soma dos seus itens, do maior para o menor
    bins_ordenados = sorted(solucao, key=lambda b: sum(b), reverse=True)
    
    # Percorre cada bin ordenado, com seu índice
    for i, b in enumerate(bins_ordenados):
        # Ordena os itens dentro do bin, do maior para o menor
        b_itens_ordenados = sorted(b, reverse=True)
        
        # Imprime o número do bin, os itens ordenados e o total da soma dos itens
        print(f"Bin {i+1}: {b_itens_ordenados} (total: {sum(b_itens_ordenados):.2f})")
