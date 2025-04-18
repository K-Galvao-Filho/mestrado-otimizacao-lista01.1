from modulos.instancia import gerar_instancia
from modulos.heuristica_inicial import construir_solucao_inicial
from modulos.busca_local import busca_local
from modulos.solucao import avaliar
from modulos.utils import imprimir_solucao, imprimir_solucao_ordenada

def executar(num_itens, tempo_limite):
    itens = gerar_instancia(num_itens)
    print("\nInstância gerada:")
    print(itens)

    solucao_inicial = construir_solucao_inicial(itens)
    print(f"\nSolução inicial (bins usados: {avaliar(solucao_inicial)}):")
    imprimir_solucao(solucao_inicial)

    solucao_final = busca_local(solucao_inicial, tempo_limite)
    print(f"\nSolução final (bins usados: {avaliar(solucao_final)}):")
    imprimir_solucao_ordenada(solucao_final)    

def main():
    import sys
    if len(sys.argv) != 3:
        print("Uso: python app.py <num_itens> <tempo_limite_segundos>")
        return

    n = int(sys.argv[1])
    tempo_limite = int(sys.argv[2])

    executar(n, tempo_limite)

executar(30,10)
