import os
from colorama import init, Fore, Style
from dados import vendas
from relatorio import gerar_relatorio
from dashboard import dashboard

init()

while True:
    os.system('cls')  # limpa só o MENU

    print(Fore.CYAN + "\n📊 SISTEMA DE ANÁLISE DE VENDAS" + Style.RESET_ALL)
    print("1 - Relatório em texto")
    print("2 - Dashboard gráfico")
    print("3 - Sair")

    opcao = input("\nEscolha uma opção: ")

    if opcao == "1":
        gerar_relatorio(vendas)
        input("\nPressione ENTER para voltar ao menu...")  #  pausa importante

    elif opcao == "2":
        dashboard(vendas)
        input("\nPressione ENTER para voltar ao menu...")

    elif opcao == "3":
        print("Saindo...")
        break

    else:
        print("Opção inválida!")
        input("Pressione ENTER...")