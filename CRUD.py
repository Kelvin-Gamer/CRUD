# Função para exibir o menu
def exibir_menu():
    print("\nMenu:")
    print("1. Listar itens")
    print("2. Adicionar item")
    print("3. Atualizar item")
    print("4. Remover item")
    print("5. Sair")

# Função para listar os itens
def listar_itens(itens):
    print("\nItens:")
    for idx, item in enumerate(itens, start=1):
        print(f"{idx}. {item}")

# Função para adicionar um item
def adicionar_item(itens):
    novo_item = input("Digite o novo item: ")
    itens.append(novo_item)
    print("Item adicionado com sucesso!")

# Função para atualizar um item
def atualizar_item(itens):
    listar_itens(itens)
    idx = int(input("Digite o número do item que deseja atualizar: ")) - 1
    if 0 <= idx < len(itens):
        novo_valor = input("Digite o novo valor para o item: ")
        itens[idx] = novo_valor
        print("Item atualizado com sucesso!")
    else:
        print("Índice inválido!")

# Função para remover um item
def remover_item(itens):
    listar_itens(itens)
    idx = int(input("Digite o número do item que deseja remover: ")) - 1
    if 0 <= idx < len(itens):
        item_removido = itens.pop(idx)
        print(f"Item '{item_removido}' removido com sucesso!")
    else:
        print("Índice inválido!")

def main():
    itens = []
    while True:
        exibir_menu()
        opcao = input("Digite a opção desejada: ")

        if opcao == "1":
            listar_itens(itens)
        elif opcao == "2":
            adicionar_item(itens)
        elif opcao == "3":
            atualizar_item(itens)
        elif opcao == "4":
            remover_item(itens)
        elif opcao == "5":
            print("Saindo do programa. Até mais!")
            break
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    main()

