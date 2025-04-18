import gradio as gr
from modulos.instancia import gerar_instancia
from modulos.heuristica_inicial import construir_solucao_inicial
from modulos.busca_local import busca_local
from modulos.solucao import avaliar
import matplotlib.pyplot as plt
import copy

def plotar_bins(solucao, titulo):
    fig, ax = plt.subplots(figsize=(6, max(4, len(solucao) * 0.4)))
    for i, bin in enumerate(solucao):
        left = 0
        for item in bin:
            ax.barh(i, item, left=left, edgecolor='black')
            ax.text(left + item / 2, i, f"{item:.2f}", va='center', ha='center', color='white', fontsize=8)
            left += item

    ax.set_yticks(range(len(solucao)))
    ax.set_yticklabels([f'Bin {i+1}' for i in range(len(solucao))])
    ax.set_title(titulo)
    ax.set_xlim(0, 1.0)
    ax.set_xlabel("Capacidade do Bin (0–1)")
    ax.invert_yaxis()
    plt.tight_layout()
    return fig

def ordenar_bins(solucao):
    """Ordena os bins por soma decrescente e os itens dentro de cada bin do maior para o menor."""
    # Ordena itens dentro de cada bin
    bins_ordenados_internamente = [sorted(bin, reverse=True) for bin in solucao]
    # Ordena os bins pelo total (maior para menor)
    bins_ordenados_total = sorted(bins_ordenados_internamente, key=lambda b: sum(b), reverse=True)
    return bins_ordenados_total

def executar_binpacking(n, tempo):
    itens = gerar_instancia(n)
    solucao_inicial = construir_solucao_inicial(itens)
    solucao_inicial_copia = copy.deepcopy(solucao_inicial)
    solucao_final = busca_local(solucao_inicial_copia, tempo)

    # SOLUÇÃO INICIAL → não ordena nada (só exibe)
    fig_inicial = plotar_bins(solucao_inicial, f'Solução Inicial ({avaliar(solucao_inicial)} bins)')

    # SOLUÇÃO FINAL → organiza para exibição (ordem decrescente)
    solucao_final_ordenada = ordenar_bins(solucao_final)
    fig_final = plotar_bins(solucao_final_ordenada, f'Solução Otimizada ({avaliar(solucao_final_ordenada)} bins)')

    return (
        itens,
        f"{avaliar(solucao_inicial)} bins",
        fig_inicial,
        f"{avaliar(solucao_final_ordenada)} bins",
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
