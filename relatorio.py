from collections import Counter, defaultdict


def gerar_relatorio(vendas):
    if not vendas:
        print("Nenhuma venda encontrada.")
        return

    total_faturamento = sum(v["valor"] * v["quantidade"] for v in vendas)
    total_itens = sum(v["quantidade"] for v in vendas)
    
    ticket_medio = (
        total_faturamento / total_itens
        if total_itens > 0 else 0
    )

    produtos = Counter()
    categorias = Counter()
    vendas_dia = defaultdict(float)

    for v in vendas:
        valor_total = v["valor"] * v["quantidade"]

        produtos[v["produto"]] += v["quantidade"]
        categorias[v["categoria"]] += v["quantidade"]
        vendas_dia[v["dia"]] += valor_total

    ordem_dias = [
        "Segunda",
        "Terça",
        "Quarta",
        "Quinta",
        "Sexta",
        "Sábado",
        "Domingo"
    ]

    print("\n📊 RELATÓRIO SEMANAL DA LOJA MASCULINA\n")

    # 💰 faturamento
    print(f"💰 Faturamento total: R$ {total_faturamento:.2f}")
    print(f"🧾 Ticket médio: R$ {ticket_medio:.2f}\n")

    # 🏆 produtos
    print("🏆 Produtos mais vendidos:")
    for produto, quantidade in produtos.most_common():
        print(f"- {produto}: {quantidade} unidades")

    # 📦 categorias
    print("\n📦 Categorias mais vendidas:")
    for categoria, quantidade in categorias.most_common():
        print(f"- {categoria}: {quantidade} unidades")

    # 📅 vendas por dia
    print("\n📅 Faturamento por dia:")
    for dia in ordem_dias:
        if dia in vendas_dia:
            print(f"- {dia}: R$ {vendas_dia[dia]:.2f}")

    # 🥇 melhor dia (CORRIGIDO)
    if vendas_dia:
        melhor_dia = max(vendas_dia.items(), key=lambda x: x[1])[0]
        valor_melhor_dia = vendas_dia[melhor_dia]
        print(f"\n🥇 Melhor dia de vendas: {melhor_dia} (R$ {valor_melhor_dia:.2f})")
    else:
        print("\n🥇 Melhor dia de vendas: N/A")

    print("\n🧠 INSIGHTS AUTOMÁTICOS")
    print("-" * 40)

    melhor_categoria = max(categorias, key=categorias.get)
    print(f"- Categoria mais forte: {melhor_categoria}")

    melhor_produto = max(produtos, key=produtos.get)
    print(f"- Produto mais vendido: {melhor_produto}")
    print("-" * 40)