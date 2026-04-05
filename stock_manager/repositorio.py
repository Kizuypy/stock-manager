import json
from stock_manager.models import (
    Produto,
    ProdutoJaExisteError,
    ProdutoNaoEncontradoError,
)


class RepositorioProdutos:
    def __init__(self, arquivo="dados.json"):
        self.arquivo = arquivo
        self._produtos = []
        self._carregar()

    def _salvar(self):
        with open(self.arquivo, "w", encoding="utf-8") as f:
            dados = [vars(p) for p in self._produtos]
            json.dump(dados, f, indent=4, ensure_ascii=False)

    def _carregar(self):
        try:
            with open(self.arquivo, "r", encoding="utf-8") as f:
                conteudo = f.read()
                if not conteudo.strip():
                    self._produtos = []
                    return
                self._produtos = [Produto.from_dict(p) for p in json.loads(conteudo)]
        except FileNotFoundError:
            self._produtos = []

    def adicionar(self, produto):
        for p in self._produtos:
            if p.nome == produto.nome:
                raise ProdutoJaExisteError(produto.nome)
        self._produtos.append(produto)
        self._salvar()

    def buscar(self, nome):
        for p in self._produtos:
            if p.nome == nome:
                return p
        raise ProdutoNaoEncontradoError(nome)

    def listar(self):
        return self._produtos.copy()

    def atualizar(self, produto):
        for i, p in enumerate(self._produtos):
            if p.nome == produto.nome:
                self._produtos[i] = produto
                self._salvar()
                return
        raise ProdutoNaoEncontradoError(produto.nome)
