def normalizar(texto):
    return (
        texto.strip()
        .lower()
        .replace("á", "a")
        .replace("à", "a")
        .replace("ã", "a")
        .replace("â", "a")
        .replace("é", "e")
        .replace("ê", "e")
        .replace("í", "i")
        .replace("ó", "o")
        .replace("ô", "o")
        .replace("õ", "o")
        .replace("ú", "u")
        .replace("ç", "c")
    )


def listar_vendas(vendas):
    if not vendas:
        print("Nenhuma venda encontrada.")
        return

    print("\n📜 HISTÓRICO DE VENDAS")
    print("1 - Todas as vendas")
    print("2 - Filtrar por dia")
    print("3 - Filtrar por produto")

    opcao = input("\nEscolha uma opção: ")

    if opcao == "1":
        for v in vendas:
            print_venda(v)

    elif opcao == "2":
        dia = normalizar(input("Digite o dia: "))

        filtradas = [
            v for v in vendas
            if normalizar(v["dia"]) == dia
        ]

        if not filtradas:
            print("❌ Nenhuma venda encontrada nesse dia.")
        else:
            for v in filtradas:
                print_venda(v)

    elif opcao == "3":
        produto = normalizar(input("Digite o produto: "))

        filtradas = [
            v for v in vendas
            if normalizar(v["produto"]) == produto
        ]

        if not filtradas:
            print("❌ Nenhuma venda encontrada para esse produto.")
        else:
            for v in filtradas:
                print_venda(v)

    else:
        print("❌ Opção inválida")


def print_venda(v):
    print(f"""
🧾 Produto: {v['produto']}
📦 Categoria: {v['categoria']}
📅 Dia: {v['dia']}
💰 Valor: R$ {v['valor']}
🔢 Quantidade: {v['quantidade']}
⏰ Data: {v.get('data_hora', 'N/A')}
-----------------------------
""")


def deletar_venda(vendas):
    if not vendas:
        print("Nenhuma venda para deletar.")
        return

    print("\n🗑️ DELETAR VENDA")
    listar_vendas_simples(vendas)

    try:
        index = int(input("\nDigite o número da venda para deletar: ")) - 1

        if index < 0 or index >= len(vendas):
            print("❌ Índice inválido.")
            return

        removida = vendas.pop(index)
        print(f"\n✅ Venda removida: {removida['produto']}")

    except ValueError:
        print("❌ Digite um número válido.")


def listar_vendas_simples(vendas):
    for i, v in enumerate(vendas, start=1):
        print(f"{i} - {v['produto']} | {v['dia']} | R$ {v['valor']}")