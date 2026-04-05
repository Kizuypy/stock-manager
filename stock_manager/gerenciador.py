# Stock Manager — Arquivo 3
# gerenciador.py — Regras de negócio

# O que esse arquivo representa:
# O gerenciador é a camada que contém as regras de negócio do sistema. Ele não sabe como salvar dados — delega isso pro repositório. Ele não sabe como mostrar dados pro usuário — isso é responsabilidade do CLI. Ele só sabe as regras: o que pode e o que não pode acontecer no estoque.
# Essa separação é o que torna o código profissional — cada camada tem uma responsabilidade clara.

# Crie a classe GerenciadorEstoque com:

# __init__ recebe repositorio (um RepositorioProdutos) — composição
# Nunca acessa o arquivo JSON diretamente, sempre usa o repositório

# Métodos:

# cadastrar(nome, preco, categoria, quantidade) — cria um Produto e chama repositorio.adicionar(). Lança ProdutoJaExisteError se já existir
# entrada(nome, quantidade) — busca o produto, soma a quantidade, chama repositorio.atualizar(). Lança ProdutoNaoEncontradoError se não existir
# saida(nome, quantidade) — busca o produto, subtrai a quantidade. Lança EstoqueInsuficienteError se não tiver suficiente
# listar() — retorna todos os produtos via repositório
# relatorio_categoria() — retorna um dict com categoria como chave e quantidade total como valor


from stock_manager.models import (
    Produto,
    EstoqueInsuficienteError,
)


class GerenciadorEstoque:
    def __init__(self, repositorio):
        self.repositorio = repositorio

    def cadastrar(self, nome, preco, categoria, quantidade):
        produto = Produto(nome, preco, categoria, quantidade)
        self.repositorio.adicionar(produto)

    def entrada(self, nome, quantidade):
        if quantidade <= 0:
            raise ValueError("Quantidade deve ser maior que zero")
        produto = self.repositorio.buscar(nome)
        produto.quantidade += quantidade
        self.repositorio.atualizar(produto)

    def saida(self, nome, quantidade):
        if quantidade <= 0:
            raise ValueError("Quantidade deve ser maior que zero")
        produto = self.repositorio.buscar(nome)
        if quantidade > produto.quantidade:
            raise EstoqueInsuficienteError(nome, produto.quantidade, quantidade)
        produto.quantidade -= quantidade
        self.repositorio.atualizar(produto)

    def listar(self):
        return self.repositorio.listar()

    def relatorio_categoria(self):
        categorias = {}
        for produto in self.repositorio.listar():
            categorias[produto.categoria] = (
                categorias.get(produto.categoria, 0) + produto.quantidade
            )
        return categorias
