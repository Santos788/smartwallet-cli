# SmartWallet CLI

ARQUIVO_DADOS = "dados.txt"


def carregar_dados():
    dados = []

    try:
        with open(ARQUIVO_DADOS, "r", encoding="utf-8") as arquivo:
            for linha in arquivo:
                linha = linha.strip()

                if not linha:
                    continue

                partes = linha.split(",")

                if len(partes) == 3:
                    tipo, descricao, valor = partes
                    dados.append([tipo, descricao, float(valor)])

    except FileNotFoundError:
        pass

    return dados


def salvar_dados(dados):
    with open(ARQUIVO_DADOS, "w", encoding="utf-8") as arquivo:
        for tipo, descricao, valor in dados:
            arquivo.write(f"{tipo},{descricao},{valor}\n")


def adicionar_receita(dados):
    descricao = input("Descrição da receita: ").strip()

    try:
        valor = float(input("Valor: "))
    except ValueError:
        print("❌ Valor inválido.")
        return

    dados.append(["receita", descricao, valor])
    salvar_dados(dados)

    print("✅ Receita adicionada com sucesso!")


def adicionar_despesa(dados):
    descricao = input("Descrição da despesa: ").strip()

    try:
        valor = float(input("Valor: "))
    except ValueError:
        print("❌ Valor inválido.")
        return

    dados.append(["despesa", descricao, valor])
    salvar_dados(dados)

    print("✅ Despesa adicionada com sucesso!")


def listar_movimentacoes(dados):
    if not dados:
        print("Nenhuma movimentação encontrada.")
        return

    for tipo, descricao, valor in dados:
        print(f"{tipo.capitalize()} | {descricao} | R$ {valor:.2f}")


def ver_saldo(dados):
    saldo = 0

    for tipo, _, valor in dados:
        if tipo == "receita":
            saldo += valor
        else:
            saldo -= valor

    print(f"💰 Saldo atual: R$ {saldo:.2f}")


def menu():
    dados = carregar_dados()

    while True:
        print("\n=== SMARTWALLET ===")
        print("1 - Adicionar Receita")
        print("2 - Adicionar Despesa")
        print("3 - Listar Movimentações")
        print("4 - Ver Saldo")
        print("5 - Sair")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            adicionar_receita(dados)

        elif opcao == "2":
            adicionar_despesa(dados)

        elif opcao == "3":
            listar_movimentacoes(dados)

        elif opcao == "4":
            ver_saldo(dados)

        elif opcao == "5":
            print("Encerrando sistema...")
            break

        else:
            print("❌ Opção inválida.")


if __name__ == "__main__":
    menu()