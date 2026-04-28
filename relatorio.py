from collections import Counter, defaultdict

def gerar_relatorio(vendas):
    if not vendas:
        print("Nenhuma venda encontrada.")
        return

    total_faturamento = sum(v["valor"] * v["quantidade"] for v in vendas)
    ticket_medio = total_faturamento / len(vendas)

    produtos = Counter()
    categorias = Counter()
    vendas_dia = defaultdict(float)

    for v in vendas:
        valor_total = v["valor"] * v["quantidade"]

        produtos[v["produto"]] += v["quantidade"]
        categorias[v["categoria"]] += v["quantidade"]
        vendas_dia[v["dia"]] += valor_total

    print("\n📊 RELATÓRIO SEMANAL DA LOJA MASCULINA\n")

    # 💰 faturamento
    print(f"💰 Faturamento total: R$ {total_faturamento:.2f}")
    print(f"🧾 Ticket médio: R$ {ticket_medio:.2f}\n")

    # 🏆 produtos
    print("🏆 Produtos mais vendidos:")
    for p, q in produtos.most_common():
        print(f"- {p}: {q} unidades")

    # 📦 categorias
    print("\n📦 Categorias mais vendidas:")
    for c, q in categorias.most_common():
        print(f"- {c}: {q} unidades")

    # 📅 vendas por dia
    print("\n📅 Faturamento por dia:")
    for dia, valor in sorted(vendas_dia.items()):
        print(f"- {dia}: R$ {valor:.2f}")

    # 🥇 melhor dia
    melhor_dia = max(vendas_dia, key=vendas_dia.get)
    print(f"\n🥇 Melhor dia de vendas: {melhor_dia} (R$ {vendas_dia[melhor_dia]:.2f})")