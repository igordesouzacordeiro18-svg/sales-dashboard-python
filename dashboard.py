import tkinter as tk
from tkinter import ttk
from collections import Counter
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure


def abrir_dashboard(vendas):

    janela = tk.Tk()
    janela.title("Dashboard de Vendas")
    janela.geometry("1200x700")

    faturamento = sum(
        venda["valor"] * venda["quantidade"]
        for venda in vendas
    )

    total_itens = sum(
        venda["quantidade"]
        for venda in vendas
    )

    produtos = Counter()
    categorias = Counter()

    for venda in vendas:
        produtos[venda["produto"]] += venda["quantidade"]
        categorias[venda["categoria"]] += venda["quantidade"]

    produto_top = (
        produtos.most_common(1)[0][0]
        if produtos else "Nenhum"
    )

    titulo = tk.Label(
        janela,
        text="📊 DASHBOARD DE VENDAS",
        font=("Arial", 22, "bold")
    )
    titulo.pack(pady=10)

    frame_cards = tk.Frame(janela)
    frame_cards.pack()

    cards = [
        f"💰 Faturamento\nR$ {faturamento:.2f}",
        f"📦 Itens Vendidos\n{total_itens}",
        f"🏆 Mais Vendido\n{produto_top}"
    ]

    for i, texto in enumerate(cards):
        tk.Label(
            frame_cards,
            text=texto,
            font=("Arial", 12, "bold"),
            relief="ridge",
            padx=25,
            pady=15
        ).grid(row=0, column=i, padx=15)

    frame_graficos = tk.Frame(janela)
    frame_graficos.pack(fill="x", pady=15)

    # Gráfico de barras
    fig1 = Figure(figsize=(5, 3), dpi=100)
    ax1 = fig1.add_subplot(111)

    ax1.bar(
        list(produtos.keys()),
        list(produtos.values())
    )

    ax1.set_title("Vendas por Produto")

    canvas1 = FigureCanvasTkAgg(
        fig1,
        master=frame_graficos
    )
    canvas1.draw()
    canvas1.get_tk_widget().pack(
        side="left",
        padx=10
    )

    # Gráfico de pizza
    fig2 = Figure(figsize=(5, 3), dpi=100)
    ax2 = fig2.add_subplot(111)

    ax2.pie(
        list(categorias.values()),
        labels=list(categorias.keys()),
        autopct="%1.1f%%"
    )

    ax2.set_title("Categorias")

    canvas2 = FigureCanvasTkAgg(
        fig2,
        master=frame_graficos
    )
    canvas2.draw()
    canvas2.get_tk_widget().pack(
        side="right",
        padx=10
    )

    colunas = (
        "Dia",
        "Produto",
        "Categoria",
        "Valor",
        "Quantidade",
        "Total"
    )

    tabela = ttk.Treeview(
        janela,
        columns=colunas,
        show="headings",
        height=12
    )

    for coluna in colunas:
        tabela.heading(coluna, text=coluna)
        tabela.column(coluna, width=150)

    for venda in vendas:

        total = (
            venda["valor"]
            * venda["quantidade"]
        )

        tabela.insert(
            "",
            "end",
            values=(
                venda["dia"],
                venda["produto"],
                venda["categoria"],
                f"R$ {venda['valor']:.2f}",
                venda["quantidade"],
                f"R$ {total:.2f}"
            )
        )

    tabela.pack(
        fill="both",
        expand=True,
        padx=15,
        pady=15
    )

    janela.mainloop()