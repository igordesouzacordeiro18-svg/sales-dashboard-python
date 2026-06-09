import os
import csv
from colorama import init, Fore, Style
from relatorio import gerar_relatorio
from vendas import cadastrar_venda
from historico import listar_vendas
from historico import listar_vendas, deletar_venda

vendas = []

if os.path.exists("data/vendas.csv"):
    with open("data/vendas.csv", "r", encoding="utf-8") as arquivo:
        reader = csv.DictReader(arquivo)

        for linha in reader:
            vendas.append({
                "dia": linha["dia"],
                "produto": linha["produto"],
                "categoria": linha["categoria"],
                "valor": float(linha["valor"]),
                "quantidade": int(linha["quantidade"]),
                "data_hora": linha["data_hora"]
            })

init()

while True:
    os.system('cls' if os.name == 'nt' else 'clear')  # limpa só o MENU

    print(Fore.CYAN + "\n📊 SISTEMA DE ANÁLISE DE VENDAS" + Style.RESET_ALL)
    print("1 - Relatório em texto")
    print("2 - Abrir Dashboard no Power BI")
    print("3 - Cadastrar venda")
    print("4 - Histórico de vendas")
    print("5 - Deletar venda")
    print("6 - Sair")

    opcao = input("\nEscolha uma opção: ")

    if opcao == "1":
        gerar_relatorio(vendas)
        input("\nPressione ENTER para voltar ao menu...")

    elif opcao == "2":
        print("\n📊 Abra o arquivo do Power BI conectado ao vendas.csv")
        input("\nPressione ENTER para voltar ao menu...")

    elif opcao == "3":
        cadastrar_venda(vendas)
        input("\nPressione ENTER para voltar ao menu...")

    elif opcao == "4":
        listar_vendas(vendas)
        input("\nPressione ENTER para voltar ao menu...")

    elif opcao == "5":
        deletar_venda(vendas)
        input("\nPressione ENTER para voltar ao menu...")

    elif opcao == "6":
        print("Saindo...")
        break

    else:
        print("Opção inválida!")
        input("Pressione ENTER...")