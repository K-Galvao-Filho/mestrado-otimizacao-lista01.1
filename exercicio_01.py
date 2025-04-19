# Importa funções dos módulos personalizados
from modulos.instancia import gerar_instancia  # Para gerar itens aleatórios
from modulos.heuristica_inicial import construir_solucao_inicial  # Para montar a solução inicial
from modulos.busca_local import busca_local  # Para melhorar a solução inicial usando busca local
from modulos.solucao import avaliar  # Para contar quantos bins estão sendo usados
from modulos.utils import imprimir_solucao, imprimir_solucao_ordenada  # Para exibir as soluções de maneira organizada


def executar(num_itens, tempo_limite):
    # Gera uma lista de itens aleatórios
    itens = gerar_instancia(num_itens)
    print("\nInstância gerada:")
    print(itens)

    # Constrói uma solução inicial encaixando os itens em bins
    solucao_inicial = construir_solucao_inicial(itens)
    print(f"\nSolução inicial (bins usados: {avaliar(solucao_inicial)}):")
    imprimir_solucao(solucao_inicial)  # Mostra a solução inicial (não ordenada)

    # Aplica busca local para tentar melhorar a solução inicial
    solucao_final = busca_local(solucao_inicial, tempo_limite)
    print(f"\nSolução final (bins usados: {avaliar(solucao_final)}):")
    imprimir_solucao_ordenada(solucao_final)  # Mostra a solução otimizada e ordenada


def main():
    import sys  # Importa o módulo sys para acessar argumentos da linha de comando
    if len(sys.argv) != 3:
        print("Uso: python app.py <num_itens> <tempo_limite_segundos>")
        return

    n = int(sys.argv[1])  # Primeiro argumento: quantidade de itens
    tempo_limite = int(sys.argv[2])  # Segundo argumento: tempo limite de busca em segundos

    executar(n, tempo_limite)  # Executa o processo com os parâmetros fornecidos

executar(30,10)
