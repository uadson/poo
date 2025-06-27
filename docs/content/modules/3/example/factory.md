# 2. Factory Method Pattern

**Categoria**: _Criacional_

**Problema**: Como criar objetos sem expor a lógica concreta de construção ao cliente e ainda permitir a extensão futura?

## Quando usar?
No projeto bancário, temos dois tipos de contas:

* ContaCorrente

* ContaPoupanca

Ambas herdam de Conta.

Se deixarmos o código principal (principal.py) decidir qual tipo de conta criar, quebramos o princípio da responsabilidade única e da abertura para extensão (SRP e OCP).

### Conceito:
O padrão Factory Method define uma interface para criar um objeto, mas permite que as subclasses escolham qual classe instanciar.

* Sem o padrão (antes)
```python
# cli.py
cliente = Cliente("Maria", "123")
conta = ContaCorrente("0001", cliente)
```
Aqui o código de criação está espalhado e acoplado ao tipo da conta.


* Com o padrão Factory Method (depois)

1. Criamos uma classe ContaFactory
```python
# domain/factories.py
from domain.entities import Conta, ContaCorrente, ContaPoupanca, Cliente

class ContaFactory:
    """Fábrica para criação de contas bancárias."""

    @staticmethod
    def criar(tipo: str, numero: str, cliente: Cliente, **kwargs) -> Conta:
        """Cria uma conta de acordo com o tipo especificado.

        Args:
            tipo (str): Tipo da conta ('corrente' ou 'poupanca').
            numero (str): Número da conta.
            cliente (Cliente): Cliente associado.
            **kwargs: Parâmetros opcionais (ex: limite da corrente).

        Returns:
            Conta: Instância da conta criada.
        """
        if tipo == "corrente":
            return ContaCorrente(numero, cliente, limite=kwargs.get("limite", 500))
        elif tipo == "poupanca":
            return ContaPoupanca(numero, cliente)
        else:
            raise ValueError(f"Tipo de conta desconhecido: {tipo}")
```

2. Uso no código principal
```python
# main.py
from domain.factories import ContaFactory
from domain.entities import Cliente
from infra.singleton_repo import RepositorioEmMemoriaSingleton

repo = RepositorioEmMemoriaSingleton()

cliente = Cliente("Maria", "123")
repo.salvar_cliente(cliente)

conta = ContaFactory.criar("corrente", "0001", cliente, limite=1000)
repo.salvar_conta(conta)
```

### Benefícios no projeto

* Criação centralizada e flexível
* Novo tipo de conta? Basta adicionar na fábrica
* Facilita testes e validações
* Evita if-else espalhado no código
  
### Recapitulando

| Antes                       | Depois                                |
| --------------------------- | ------------------------------------- |
| `ContaCorrente(...)` direto | `ContaFactory.criar("corrente", ...)` |
| Acoplamento ao tipo         | Desacoplado, fácil de estender        |
| Difícil de testar e manter  | Testável, extensível e limpo          |
