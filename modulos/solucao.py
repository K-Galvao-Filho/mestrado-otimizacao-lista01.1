# Função para avaliar a qualidade da solução
def avaliar(solucao):
    """Avalia a solução: número de bins utilizados"""
    # A avaliação é simplesmente o número de bins usados
    return len(solucao)

# Função para fazer uma cópia da solução
def copiar_solucao(solucao):
    """Faz uma cópia profunda da solução, removendo bins vazios"""
    # Cria uma nova lista copiando cada bin (e seus itens) apenas se ele não estiver vazio
    return [list(bin) for bin in solucao if bin]
