def processar_vendas():
    vendas = []
    total_vendas = 0

    print("Sistema de vendas - Digite 'fim' para encerrar")

    while True:
        produto = input("Nome do produto (ou 'fim')")

        if produto.lower() == 'fim':
            break

        while True:
            try:
                preco = float(input("Preço do produto: R$ "))
                if preco <= 0:
                    print("Preço deve ter um valor positivo")
                    continue
                break
            except ValueError:
                print("Digite um numero válido")

            while True:
                try:
                    quantidade = int(input("Quantidade: "))
                    if quantidade <= 0:
                        print("Quantidade deve ser positiva!")
                        continue
                    break
                except ValueError:
                    print("Digite um numero inteiro válido")
                subtotal = preco * quantidade
                vendas.append({
                    'produto': produto,
                    'preco': preco,
                    'quantidade': quantidade,
                    'subtotal': subtotal
                })
                total_vendas += subtotal
                print(f"Subtotal: R$ {subtotal:.2f}")

                print("\n" + "=" *40)
                print("Relatório de vendas")
                print("="*40)

                for venda in vendas:
                    print(f"{venda['produto']}: {vendas['quantidade']}x R$ {venda['preco']:.2f} = R$ {venda['subtotal']:.2f}")

                print(f"\nTotal: R$ {total_vendas: .2f}")

processar_vendas()