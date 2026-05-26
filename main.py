import os
from colorama import init, Fore, Style
from relatorio import gerar_relatorio
from dashboard import dashboard
import json
from vendas import cadastrar_venda
from historico import listar_vendas
from historico import listar_vendas, deletar_venda

with open("data/vendas.json", "r", encoding="utf-8") as arquivo:
    vendas = json.load(arquivo)

init()

while True:
    os.system('cls' if os.name == 'nt' else 'clear')  # limpa só o MENU

    print(Fore.CYAN + "\n📊 SISTEMA DE ANÁLISE DE VENDAS" + Style.RESET_ALL)
    print("1 - Relatório em texto")
    print("2 - Dashboard gráfico")
    print("3 - Cadastrar venda")
    print("4 - Histórico de vendas")
    print("5 - Deletar venda")
    print("6 - Sair")

    opcao = input("\nEscolha uma opção: ")

    if opcao == "1":
        gerar_relatorio(vendas)
        input("\nPressione ENTER para voltar ao menu...")

    elif opcao == "2":
        dashboard(vendas)
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