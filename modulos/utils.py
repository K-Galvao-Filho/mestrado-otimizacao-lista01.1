def imprimir_solucao(solucao):
    for i, b in enumerate(solucao):
        print(f"Bin {i+1}: {b} (total: {sum(b):.2f})")
