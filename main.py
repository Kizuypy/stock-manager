from stock_manager.repositorio import RepositorioProdutos
from stock_manager.gerenciador import GerenciadorEstoque
from stock_manager.models import ErroEstoque


def menu():
    print("\n=== Stock Manager ===")
    print("1. Cadastrar produto")
    print("2. Registrar entrada")
    print("3. Registrar saída")
    print("4. Listar estoque")
    print("5. Relatório por categoria")
    print("0. Sair")


def main():
    repo = RepositorioProdutos("dados.json")
    gerenciador = GerenciadorEstoque(repo)

    while True:
        menu()
        opcao = input("\nEscolha: ").strip()

        if opcao == "1":
            try:
                nome = input("Nome: ").strip()
                preco = float(input("Preço: "))
                categoria = input("Categoria: ").strip()
                quantidade = int(input("Quantidade inicial: "))
                gerenciador.cadastrar(nome, preco, categoria, quantidade)
                print("✓ Produto cadastrado com sucesso!")
            except ErroEstoque as e:
                print(f"✗ {e}")
            except ValueError as e:
                print(f"✗ {e}")

        elif opcao == "2":
            try:
                nome = input("Nome do produto: ").strip()
                quantidade = int(input("Quantidade: "))
                gerenciador.entrada(nome, quantidade)
                print("✓ Entrada registrada!")
            except ErroEstoque as e:
                print(f"✗ {e}")
            except ValueError as e:
                print(f"✗ {e}")

        elif opcao == "3":
            try:
                nome = input("Nome do produto: ").strip()
                quantidade = int(input("Quantidade: "))
                gerenciador.saida(nome, quantidade)
                print("✓ Saída registrada!")
            except ErroEstoque as e:
                print(f"✗ {e}")
            except ValueError as e:
                print(f"✗ {e}")

        elif opcao == "4":
            produtos = gerenciador.listar()
            if not produtos:
                print("\nEstoque vazio.")
            else:
                print("\n=== Estoque ===")
                for p in produtos:
                    print(p)

        elif opcao == "5":
            relatorio = gerenciador.relatorio_categoria()
            if not relatorio:
                print("\nNenhum produto cadastrado.")
            else:
                print("\n=== Relatório por categoria ===")
                for categoria, total in relatorio.items():
                    print(f"{categoria}: {total} unidades")

        elif opcao == "0":
            print("Encerrando...")
            break

        else:
            print("✗ Opção inválida.")


if __name__ == "__main__":
    main()
