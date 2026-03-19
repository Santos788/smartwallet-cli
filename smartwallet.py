# smartwallet.py

"""
SmartWallet CLI
Sistema simples de controle financeiro no terminal.

Funcionalidades:
- Adicionar receitas
- Adicionar despesas
- Listar movimentações
- Ver saldo

Autor: Clayton Santos
"""

ARQUIVO_DADOS = "dados.txt"


def carregar_dados():
    """Carrega os dados do arquivo."""
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
        # Arquivo ainda não existe (primeira execução)
        pass

    return dados


def salvar_dados(dados):
    """Salva os dados no arquivo."""
    with open(ARQUIVO_DADOS, "w", encoding="utf-8") as arquivo:
        for tipo, descricao, valor in dados:
            arquivo.write(f"{tipo},{descricao},{valor}\n")


def adicionar_receita(dados):
    """Adiciona uma nova receita."""
    descricao = input("Descrição da receita: ").strip()

    try:
        valor = float(input("Valor: R$ "))
    except ValueError:
        print("❌ Valor inválido.")
        return

    dados.append(["receita", descricao, valor])
    salvar_dados(dados)

    print("✅ Receita adicionada!")


def adicionar_despesa(dados):
    """Adiciona uma nova despesa."""
    descricao = input("Descrição da despesa: ").strip()

    try:
        valor = float(input("Valor: R$ "))
    except ValueError:
        print("❌ Valor inválido.")
        return

    dados.append(["despesa", descricao, valor])
    salvar_dados(dados)

    print("✅ Despesa adicionada!")


def listar_movimentacoes(dados):
    """Lista todas as movimentações."""
    if not dados:
        print("⚠️ Nenhuma movimentação encontrada.")
        return

    print("\n📋 MOVIMENTAÇÕES")
    print("-" * 30)

    for tipo, descricao, valor in dados:
        print(f"{tipo.capitalize():<10} | {descricao:<15} | R$ {valor:.2f}")


def ver_saldo(dados):
    """Calcula e exibe o saldo."""
    saldo = 0

    for tipo, _, valor in dados:
        if tipo == "receita":
            saldo += valor
        else:
            saldo -= valor

    print(f"\n💰 Saldo atual: R$ {saldo:.2f}")


def exibir_menu():
    """Exibe o menu principal."""
    print("\n=== SMARTWALLET ===")
    print("1 - Adicionar Receita")
    print("2 - Adicionar Despesa")
    print("3 - Listar Movimentações")
    print("4 - Ver Saldo")
    print("5 - Sair")


def main():
    """Função principal do sistema."""
    dados = carregar_dados()

    while True:
        exibir_menu()
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
    main()
