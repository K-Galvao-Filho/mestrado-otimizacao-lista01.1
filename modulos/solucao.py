def avaliar(solucao):
    """Avalia a solução: número de bins utilizados"""
    return len(solucao)

def copiar_solucao(solucao):
    """Faz uma cópia profunda da solução, removendo bins vazios"""
    return [list(bin) for bin in solucao if bin]
