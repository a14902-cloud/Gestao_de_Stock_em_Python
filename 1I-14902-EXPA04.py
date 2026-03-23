def adicionar_material(stock):
    nome = input("Nome do material: ")
    if nome in stock:
        print("O material já existe no stock!")
    else:
        quantidade = int(input(f"Quantidade inicial de {nome}: "))
        stock[nome] = quantidade
        print(f"{nome} adicionado com sucesso!")



def consultar_stock(stock):
    nome = input("Nome do material para consulta: ")
    if nome in stock:
        print(f"O stock atual de {nome} é: {stock[nome]}")
    else:
        print(f"{nome} não encontrado no stock.")



def atualizar_stock(stock):
    nome = input("Nome do material a atualizar: ")
    if nome in stock:
        operacao = input("Deseja adicionar (A) ou remover (R)? ").upper()
        quantidade = int(input("Quantidade: "))
        if operacao == "A":
            stock[nome] += quantidade
            print(f"{quantidade} unidade(s) adicionada(s) ao stock de {nome}.")
        elif operacao == "R":
            if quantidade <= stock[nome]:
                stock[nome] -= quantidade
                print(f"{quantidade} unidade(s) removida(s) do stock de {nome}.")
            else:
                print("Quantidade insuficiente em stock!")
        else:
            print("Operação inválida!")
    else:
        print(f"{nome} não encontrado no stock.")



def exibir_stock(stock):
    print("\nEstado Geral do Stock:")
    print("Material\tQuantidade")
    print("-" * 30)
    for material, quantidade in stock.items():
        print(f"{material}\t\t{quantidade}")


menu = """
┌───────────────────────────────────────┐
│            Gestão de Stocks           │
├───────────────────────────────────────┤
│ 1-Registar novos materiais no stock.  │
│ 2-Consultar o stock de um material    │
│ específico.                           │
│ 3-Atualizar o stock .                 │
│ 4-Exibir o estado geral do stock.     │
│ 5-Sair                                │
└───────────────────────────────────────┘
"""

def main():
    stock = {}
    while True:
        print(menu)
        opcao = input("Escolha uma opção: ")
        
        if opcao == "1":
            adicionar_material(stock)
        elif opcao == "2":
            consultar_stock(stock)
        elif opcao == "3":
            atualizar_stock(stock)
        elif opcao == "4":
            exibir_stock(stock)
        elif opcao == "5":
            print("Encerrando o programa...")
            break
        else:
            print("Opção inválida! Tente novamente.")

if __name__ == "__main__":
    main()




