import matplotlib.pyplot as plt
from collections import Counter, defaultdict

def dashboard(vendas):
    if not vendas:
        print("Sem dados para exibir.")
        return

    # =================
    # 📊 CÁLCULOS
    # =================

    faturamento_total = sum(v["valor"] * v["quantidade"] for v in vendas)
    ticket_medio = faturamento_total / len(vendas)

    vendas_dia = defaultdict(float)
    categorias = Counter()
    produtos = Counter()

    for v in vendas:
        valor_total = v["valor"] * v["quantidade"]

        vendas_dia[v["dia"]] += valor_total
        categorias[v["categoria"]] += valor_total
        produtos[v["produto"]] += valor_total

    melhor_dia = max(vendas_dia, key=vendas_dia.get)

    # =========================
    # 🖼️ LAYOUT DO DASHBOARD
    # =========================

    fig = plt.figure(figsize=(16, 10))

    # =========================
    # 📌 KPIs (TEXTO NO TOPO)
    # =========================
    plt.figtext(0.1, 0.95, f"💰 Faturamento: R$ {faturamento_total:.2f}", fontsize=12)
    plt.figtext(0.4, 0.95, f"🧾 Ticket médio: R$ {ticket_medio:.2f}", fontsize=12)
    plt.figtext(0.7, 0.95, f"🥇 Melhor dia: {melhor_dia}", fontsize=12)

    # =========================
    # 📊 1. FATURAMENTO POR DIA
    # =========================
    ax1 = plt.subplot(2, 2, 1)
    ax1.plot(list(vendas_dia.keys()), list(vendas_dia.values()), marker='o')
    ax1.set_title("Faturamento por Dia")
    ax1.set_xlabel("Dia")
    ax1.set_ylabel("R$")

    # =========================
    # 📦 2. CATEGORIAS
    # =========================
    ax2 = plt.subplot(2, 2, 2)
    ax2.bar(categorias.keys(), categorias.values())
    ax2.set_title("Faturamento por Categoria")
    ax2.set_xlabel("Categoria")
    ax2.set_ylabel("R$")

    # =========================
    # 🏆 3. TOP PRODUTOS
    # =========================
    ax3 = plt.subplot(2, 1, 2)
    top_produtos = produtos.most_common(5)

    nomes = [p[0] for p in top_produtos]
    valores = [p[1] for p in top_produtos]

    ax3.barh(nomes, valores)
    ax3.set_title("Top Produtos (Faturamento)")
    ax3.set_xlabel("R$")

    plt.tight_layout(rect=[0, 0, 1, 0.93])
    plt.show()