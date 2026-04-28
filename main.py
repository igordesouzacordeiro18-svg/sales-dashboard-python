from dados import vendas
from relatorio import gerar_relatorio
from dashboard import dashboard

print("\n📊 SISTEMA DE ANÁLISE DE VENDAS\n")
print("1 - Relatório em texto")
print("2 - Dashboard gráfico")

opcao = input("Escolha uma opção: ")

if opcao == "1":
    gerar_relatorio(vendas)
elif opcao == "2":
    dashboard(vendas)
else:
    print("Opção inválida")    