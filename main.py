import os
from colorama import init
from dados import vendas
from dashboard import abrir_dashboard

init()


def cadastrar_venda(vendas):

    print("\n" + "=" * 40)
    print("📝 CADASTRO DE VENDAS")
    print("=" * 40)

    dia = input("📅 Dia da venda: ")
    produto = input("📦 Produto: ")
    categoria = input("🏷️ Categoria: ")

    valor_texto = input("💰 Valor (R$): ")
    valor_texto = valor_texto.replace("R$", "").replace(",", ".").strip()
    valor = float(valor_texto)

    quantidade = int(input("🔢 Quantidade: "))

    vendas.append({
        "dia": dia,
        "produto": produto,
        "categoria": categoria,
        "valor": valor,
        "quantidade": quantidade
    })

    print("\n✅ Venda cadastrada com sucesso!")
    print(f"📦 Produto: {produto}")
    print(f"🏷️ Categoria: {categoria}")
    print(f"💰 Valor: R$ {valor:.2f}")
    print(f"🔢 Quantidade: {quantidade}")

    input("\nPressione ENTER para continuar...")


while True:

    os.system("cls" if os.name == "nt" else "clear")

    print("=" * 45)
    print("📊 SISTEMA DE CONTROLE DE VENDAS")
    print("=" * 45)
    print("1 - Registrar Venda")
    print("2 - Abrir Dashboard")
    print("3 - Sair")
    print("=" * 45)

    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        cadastrar_venda(vendas)

    elif opcao == "2":
        abrir_dashboard(vendas)

    elif opcao == "3":
        print("\n👋 Encerrando sistema...")
        break

    else:
        print("\n❌ Opção inválida!")
        input("Pressione ENTER...")