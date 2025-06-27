# Princípios SOLID aplicados sistema bancário:

| Princípio   | Aplicação no projeto                                                            |
| ----------- | ------------------------------------------------------------------------------- |
| **S** - SRP | `Conta` só cuida do saldo, `Repositorio` da persistência                        |
| **O** - OCP | Pode adicionar `ContaInvestimento` sem mudar o código antigo                    |
| **L** - LSP | `ContaCorrente` e `ContaPoupanca` substituem `Conta` sem quebrar                |
| **I** - ISP | Separação clara entre `ContaRepositoryInterface` e `ClienteRepositoryInterface` |
| **D** - DIP | `main.py` depende da **interface**, não da implementação                        |


# Estrutura do projeto

```bash
banco/
├── dominio/                     -> Lógica de negócio
│   ├── entidades.py             -> Entidades: Conta, Cliente, ContaCorrente, ContaPoupanca
│   └── interfaces.py            -> Abstrações (repositorio, operacoes)
├── infra/                       -> Implementações concretas
│   └── repositorio_memoria.py   -> Repositório em memória
└── principal.py                 -> CLI ou interface
```