# Importa o módulo random para gerar números aleatórios
import random

# Função para gerar uma instância de itens aleatórios
def gerar_instancia(n):
    """Gera n itens com tamanhos aleatórios entre 0.1 e 1.0"""
    # Cria uma lista com n itens
    # Cada item é um número aleatório entre 0.1 e 1.0, arredondado para 2 casas decimais
    return [round(random.uniform(0.1, 1.0), 2) for _ in range(n)]
