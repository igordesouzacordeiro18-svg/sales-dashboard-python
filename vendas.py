from datetime import datetime
import json


def cadastrar_venda(vendas):
    print("\n🛒 NOVA VENDA")

    # Produto (não pode ser vazio)
    while True:
        produto = input("Produto: ").strip()
        if produto:
            break
        print("❌ Produto não pode ser vazio.")

    # Categoria (não pode ser vazio)
    while True:
        categoria = input("Categoria: ").strip()
        if categoria:
            break
        print("❌ Categoria não pode ser vazia.")

    # Valor (validado)
    while True:
        try:
            valor = float(input("Valor unitário: "))
            if valor > 0:
                break
            print("❌ Valor deve ser maior que 0.")
        except ValueError:
            print("❌ Digite um número válido para o valor.")

    # Quantidade (validado)
    while True:
        try:
            quantidade = int(input("Quantidade: "))
            if quantidade > 0:
                break
            print("❌ Quantidade deve ser maior que 0.")
        except ValueError:
            print("❌ Digite um número inteiro válido.")

    # 🔥 DIA (CORRIGIDO: aceita erro de digitação, acento e caixa baixa)
    dias_validos = {
        "segunda": "Segunda",
        "terca": "Terça",
        "terça": "Terça",
        "quarta": "Quarta",
        "quinta": "Quinta",
        "sexta": "Sexta",
        "sabado": "Sábado",
        "sábado": "Sábado",
        "domingo": "Domingo"
    }

    while True:
        dia_input = input("Dia da semana: ").strip().lower()

        # remove espaços extras e tenta normalizar
        dia_input = dia_input.replace("ç", "c")

        if dia_input in dias_validos:
            dia = dias_validos[dia_input]
            break

        print("❌ Dia inválido! Ex: Segunda, Terça, Quarta, Quinta, Sexta, Sábado, Domingo")

    data_hora = datetime.now().strftime("%d/%m/%Y %H:%M")

    nova_venda = {
        "dia": dia,
        "produto": produto,
        "categoria": categoria,
        "valor": valor,
        "quantidade": quantidade,
        "data_hora": data_hora
    }

    vendas.append(nova_venda)

    try:
        with open("data/vendas.json", "w", encoding="utf-8") as arquivo:
            json.dump(vendas, arquivo, indent=4, ensure_ascii=False)
    except Exception as e:
        print(f"Erro ao salvar vendas: {e}")

    print("\n✅ Venda cadastrada com sucesso!")