from dataclasses import dataclass, field

@dataclass
class Produto:
    _contador = 0
    id: int = field(init=False)
    nome: str
    preco:float
    categoria:str
    quantidade:int = 0

    def __post_init__(self):
        if self.preco <= 0:
            raise ValueError("Preço deve ser maior que zero")
        if self.quantidade < 0: 
            raise ValueError("Quantidade não pode ser negativa")
        if not isinstance(self.nome, str) or not self.nome.strip():
            raise ValueError("String não pode ser vazia!")
        Produto._contador += 1
        self.id = Produto._contador

    def __str__(self):
        return f"[{self.id:03d}] {self.nome} | R${self.preco:.2f} | {self.categoria} | Qtd: {self.quantidade}"

    @classmethod
    def from_dict(cls, data):
        data = data.copy()

        id_original = data.get("id")
        data.pop("id", None)
        obj = cls(**data)

        if id_original is not None:
            obj.id = id_original
            cls._contador = max(cls._contador, obj.id)

        return obj        


class ErroEstoque(Exception):
    """Erro base para os outros"""

class ProdutoNaoEncontradoError(ErroEstoque):
    def __init__(self,nome):
        mensagem = f"Produto '{nome}' não encontrado"
        super().__init__(mensagem)

class EstoqueInsuficienteError(ErroEstoque):
    def __init__(self, nome, disponivel, solicitado):
        mensagem = f"Estoque insuficiente para o produto '{nome}' (disponível: {disponivel}, solicitado: {solicitado})."
        super().__init__(mensagem)

class ProdutoJaExisteError(ErroEstoque):
    def __init__(self,nome ):
        mensagem = f"Produto '{nome}'já existe no estoque"
        super().__init__(mensagem)


# teste nome vazio
try:
    Produto("", 100.0, "Geral")
except ValueError as e:
    print(f"✓ Nome vazio bloqueado: {e}")

# teste preco invalido
try:
    Produto("X", -10.0, "Geral")
except ValueError as e:
    print(f"✓ Preço inválido bloqueado: {e}")

# teste quantidade negativa
try:
    Produto("X", 10.0, "Geral", -1)
except ValueError as e:
    print(f"✓ Quantidade negativa bloqueada: {e}")
