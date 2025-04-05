import random

def gerar_instancia(n):
    """Gera n itens com tamanhos aleatórios entre 0.1 e 1.0"""
    return [round(random.uniform(0.1, 1.0), 2) for _ in range(n)]
