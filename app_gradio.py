import gradio as gr
from modulos.instancia import gerar_instancia
from modulos.heuristica_inicial import construir_solucao_inicial
from modulos.busca_local import busca_local
from modulos.solucao import avaliar

import matplotlib.pyplot as plt
import copy  # ADICIONE no início

def plotar_bins(solucao, titulo):
    fig, ax = plt.subplots(figsize=(6, max(4, len(solucao) * 0.4)))
    for i, bin in enumerate(solucao):
        left = 0
        for item in bin:
            # Desenha a barra
            ax.barh(i, item, left=left, edgecolor='black')
            # Insere o valor dentro da barra
            ax.text(left + item / 2, i, f"{item:.2f}", va='center', ha='center', color='white', fontsize=8)
            left += item

    ax.set_yticks(range(len(solucao)))
    ax.set_yticklabels([f'Bin {i+1}' for i in range(len(solucao))])
    ax.set_title(titulo)
    ax.set_xlim(0, 1.0)
    ax.set_xlabel("Capacidade do Bin (0–1)")
    ax.invert_yaxis()  # opcional, deixa bin 1 no topo
    plt.tight_layout()
    return fig


def executar_binpacking(n, tempo):
    itens = gerar_instancia(n)
    solucao_inicial = construir_solucao_inicial(itens)
    solucao_inicial_copia = copy.deepcopy(solucao_inicial)  # <- garantir que a original não seja alterada
    solucao_final = busca_local(solucao_inicial_copia, tempo)

    fig_inicial = plotar_bins(solucao_inicial, f'Solução Inicial ({avaliar(solucao_inicial)} bins)')
    fig_final = plotar_bins(solucao_final, f'Solução Otimizada ({avaliar(solucao_final)} bins)')

    return (
        itens,
        f"{avaliar(solucao_inicial)} bins",
        fig_inicial,
        f"{avaliar(solucao_final)} bins",
        fig_final
    )

interface = gr.Interface(
    fn=executar_binpacking,
    inputs=[
        gr.Slider(5, 50, step=1, label="Quantidade de Itens"),
        gr.Slider(1, 30, step=1, label="Tempo Limite (segundos)")
    ],
    outputs=[
        gr.Textbox(label="Itens Gerados"),
        gr.Textbox(label="Solução Inicial"),
        gr.Plot(label="Visualização Inicial"),
        gr.Textbox(label="Solução Otimizada"),
        gr.Plot(label="Visualização Otimizada")
    ],
    title="Bin Packing com Busca Local",
    description="Escolha a quantidade de itens e o tempo limite para otimização com meta-heurística."
)

if __name__ == "__main__":
    interface.launch()
