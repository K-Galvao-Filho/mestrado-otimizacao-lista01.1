# Importa as bibliotecas necessárias
import gradio as gr  # Para criar a interface gráfica interativa
from modulos.instancia import gerar_instancia  # Para gerar itens aleatórios
from modulos.heuristica_inicial import construir_solucao_inicial  # Para construir a solução inicial
from modulos.busca_local import busca_local  # Para aplicar a otimização (busca local)
from modulos.solucao import avaliar  # Para avaliar o número de bins usados na solução
import matplotlib.pyplot as plt  # Para desenhar gráficos dos bins
import copy  # Para fazer cópias de listas sem alterar o original

def plotar_bins(solucao, titulo):
    # Cria uma figura para desenhar o gráfico, ajustando a altura baseada no número de bins
    fig, ax = plt.subplots(figsize=(6, max(4, len(solucao) * 0.4)))

    # Para cada bin, desenha os itens como barras horizontais
    for i, bin in enumerate(solucao):
        left = 0  # Começa do lado esquerdo
        for item in bin:
            # Desenha uma barra para o item
            ax.barh(i, item, left=left, edgecolor='black')
            # Escreve o valor do item dentro da barra
            ax.text(left + item / 2, i, f"{item:.2f}", va='center', ha='center', color='white', fontsize=8)
            left += item  # Atualiza a posição para o próximo item

    # Ajusta o gráfico: marca os bins, define título, limites e rótulos
    ax.set_yticks(range(len(solucao)))
    ax.set_yticklabels([f'Bin {i+1}' for i in range(len(solucao))])
    ax.set_title(titulo)
    ax.set_xlim(0, 1.0)
    ax.set_xlabel("Capacidade do Bin (0–1)")
    ax.invert_yaxis()  # Bin 1 no topo
    plt.tight_layout()  # Ajusta o layout
    return fig  # Retorna a figura


def ordenar_bins(solucao):
    """Ordena os bins por soma decrescente e os itens dentro de cada bin do maior para o menor."""
    # Ordena os itens de cada bin, do maior para o menor
    bins_ordenados_internamente = [sorted(bin, reverse=True) for bin in solucao]
    # Ordena os bins pelo total de capacidade (do maior para o menor)
    bins_ordenados_total = sorted(bins_ordenados_internamente, key=lambda b: sum(b), reverse=True)
    return bins_ordenados_total


def executar_binpacking(n, tempo):
    # Gera 'n' itens aleatórios (pesos entre 0.1 e 1.0)
    itens = gerar_instancia(n)
    
    # Constrói uma solução inicial simples (encaixando os itens em bins)
    solucao_inicial = construir_solucao_inicial(itens)
    
    # Faz uma cópia da solução para não alterar o original durante a otimização
    solucao_inicial_copia = copy.deepcopy(solucao_inicial)
    
    # Aplica a busca local para tentar melhorar a solução
    solucao_final = busca_local(solucao_inicial_copia, tempo)

    # Cria o gráfico da solução inicial
    fig_inicial = plotar_bins(solucao_inicial, f'Solução Inicial ({avaliar(solucao_inicial)} bins)')

    # Ordena a solução final para exibição mais organizada
    solucao_final_ordenada = ordenar_bins(solucao_final)
    
    # Cria o gráfico da solução otimizada
    fig_final = plotar_bins(solucao_final_ordenada, f'Solução Otimizada ({avaliar(solucao_final_ordenada)} bins)')

    # Retorna todos os resultados para a interface
    return (
        itens,  # Lista de itens gerados
        f"{avaliar(solucao_inicial)} bins",  # Quantidade de bins na solução inicial
        fig_inicial,  # Gráfico da solução inicial
        f"{avaliar(solucao_final_ordenada)} bins",  # Quantidade de bins na solução otimizada
        fig_final  # Gráfico da solução otimizada
    )

interface = gr.Interface(
    fn=executar_binpacking,  # Função que será executada ao usar a interface
    inputs=[
        gr.Slider(5, 50, step=1, label="Quantidade de Itens"),  # Slider para escolher quantidade de itens
        gr.Slider(1, 30, step=1, label="Tempo Limite (segundos)")  # Slider para escolher tempo limite
    ],
    outputs=[
        gr.Textbox(label="Itens Gerados"),  # Caixa de texto para exibir a lista de itens
        gr.Textbox(label="Solução Inicial"),  # Caixa de texto para mostrar bins iniciais
        gr.Plot(label="Visualização Inicial"),  # Gráfico da solução inicial
        gr.Textbox(label="Solução Otimizada"),  # Caixa de texto para mostrar bins após otimização
        gr.Plot(label="Visualização Otimizada")  # Gráfico da solução otimizada
    ],
    title="Bin Packing com Busca Local",  # Título da aplicação
    description="Escolha a quantidade de itens e o tempo limite para otimização com meta-heurística."  # Descrição da aplicação
)

# Lança a interface se o arquivo for executado diretamente
if __name__ == "__main__":
    interface.launch()
