# 📦 Stock Manager

CLI inventory management system built with Python and OOP — dataclasses, custom exceptions, repository pattern and JSON persistence.

---

## Sobre o projeto

Sistema de controle de estoque via terminal desenvolvido em Python puro com foco em boas práticas de Orientação a Objetos. O projeto aplica conceitos como composição de classes, hierarquia de exceptions, dataclasses e separação de responsabilidades em camadas.

---

## Funcionalidades

- Cadastrar produtos com nome, preço, categoria e quantidade
- Registrar entradas e saídas de estoque com validação de regras de negócio
- Listar todos os produtos do estoque
- Gerar relatório de quantidade por categoria
- Persistência automática em JSON — os dados continuam entre execuções

---

## Conceitos aplicados

| Conceito | Onde aparece |
|---|---|
| `@dataclass` + `__post_init__` | `models.py` — validação de dados do Produto |
| Hierarquia de exceptions | `models.py` — `ErroEstoque` e subclasses |
| Repository Pattern | `repositorio.py` — separação da camada de dados |
| Composição de classes | `gerenciador.py` — usa o repositório sem herdar dele |
| Context Manager | `repositorio.py` — leitura e escrita segura do JSON |
| `@classmethod` | `models.py` — `Produto.from_dict()` para reconstruir do JSON |

---

## Estrutura do projeto

```
stock-manager/
├── stock_manager/
│   ├── __init__.py
│   ├── models.py        # Produto + exceptions de domínio
│   ├── repositorio.py   # Persistência em JSON
│   └── gerenciador.py   # Regras de negócio
├── main.py              # CLI — interface do usuário
├── dados.json           # Gerado automaticamente
└── README.md
```

---

## Como rodar

**Requisitos:** Python 3.13+

```bash
# clone o repositório
git clone https://github.com/Kizuypy/stock-manager.git
cd stock-manager

# rode o programa
python main.py
```

---

## Demonstração

```
=== Stock Manager ===
1. Cadastrar produto
2. Registrar entrada
3. Registrar saída
4. Listar estoque
5. Relatório por categoria
0. Sair

Escolha: 1
Nome: Teclado
Preço: 250.0
Categoria: Periféricos
Quantidade inicial: 10
✓ Produto cadastrado com sucesso!

Escolha: 4

=== Estoque ===
[001] Teclado | R$250.00 | Periféricos | Qtd: 10

Escolha: 3
Nome: Teclado
Quantidade: 999
✗ Estoque insuficiente para 'Teclado' (disponível: 10, solicitado: 999)
```

---

## Autor

**Vinicius Henrique**
[LinkedIn](https://linkedin.com/in/vinicius-henrique-dev) · [GitHub](https://github.com/Kizuypy)
