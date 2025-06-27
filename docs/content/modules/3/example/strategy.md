# 3. Strategy Pattern

**Categoria**: _Comportamental_

**Problema**: Como variar o comportamento de uma classe sem usar muitos if/else ou heranças complicadas?

## Quando usar?
No nosso sistema bancário, cada tipo de conta tem uma regra diferente para sacar dinheiro:

* ContaCorrente: pode usar o limite

* ContaPoupanca: só pode sacar o que tem

* (Futuramente): ContaPremium, ContaSalário, etc.

Ao invés de codificar essa lógica diretamente dentro das classes, podemos isolar o comportamento de saque em estratégias intercambiáveis.


### Conceito:
O padrão Strategy permite definir uma família de algoritmos, encapsulá-los e torná-los intercambiáveis. O objeto escolhe qual usar em tempo de execução.

* Sem Strategy (antes)
```python
# dominio/entidades.py
class ContaCorrente(Conta):
    """Conta corrente com limite de saque.

    Attributes:
        _limite (float): Limite adicional para saque.
    """

    def __init__(self, numero: str, cliente: Cliente, limite: float = 500):
        super().__init__(numero, cliente)
        self._limite = limite

    def sacar(self, valor: float):
        """Realiza um saque com limite adicional.

        Args:
            valor (float): Valor a ser sacado.
        """
        if valor <= self._saldo + self._limite:
            self._saldo -= valor
```
Isso força cada classe a implementar sua própria lógica. Se misturarmos tipos, vai virar um if gigante.


* Com Strategy(depois)

1. Criamos as estratégias de saque
```python
# domain/strategies.py
from abc import ABC, abstractmethod

class EstrategiaSaque(ABC):
    """Interface para estratégias de saque."""
    
    @abstractmethod
    def sacar(self, conta, valor: float):
        pass

class SaqueComLimite(EstrategiaSaque):
    def __init__(self, limite: float):
        self._limite = limite

    def sacar(self, conta, valor: float):
        if valor <= conta._saldo + self._limite:
            conta._saldo -= valor

class SaqueSimples(EstrategiaSaque):
    def sacar(self, conta, valor: float):
        if valor <= conta._saldo:
            conta._saldo -= valor
```

 2. Modificamos a classe Conta para usar uma estratégia
```python
# domain/entities.py
class Conta:
    def __init__(self, numero, cliente, estrategia_saque):
        self.numero = numero
        self.cliente = cliente
        self._saldo = 0.0
        self._estrategia_saque = estrategia_saque

    def sacar(self, valor):
        self._estrategia_saque.sacar(self, valor)
```
3. As subclasses passam a estratégia correta
```python
# domain/entities.py
from domain.strategies import SaqueComLimite, SaqueSimples

class ContaCorrente(Conta):
    def __init__(self, numero, cliente, limite=500):
        super().__init__(numero, cliente, SaqueComLimite(limite))

class ContaPoupanca(Conta):
    def __init__(self, numero, cliente):
        super().__init__(numero, cliente, SaqueSimples())
```

### Benefícios do Strategy no projeto

| Vantagem                             | Explicação                             |
| ------------------------------------ | -------------------------------------- |
| Lógica de saque isolada              | Fica fora das entidades                |
| Fácil adicionar novos comportamentos | Só criar nova classe `EstrategiaSaque` |
| Código mais limpo                    | Sem `if tipo == ...`                   |
| Testes mais fáceis                   | Pode testar estratégias separadamente  |

  
Exemplo de uso no main.py:
```python
conta = ContaCorrente("0001", cliente, limite=1000)
conta.depositar(100)
conta.sacar(500)  # usa SaqueComLimite por baixo dos panos
```