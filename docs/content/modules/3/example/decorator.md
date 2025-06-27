# 5. Decorator Pattern
**Catetoria**: _Estrutural_

**Problema** : Como adicionar responsabilidades ou comportamentos extras a um objeto de forma dinâmica, sem alterar a classe original?

## Quando usar?
Imagine que você deseja:

* Logar todas as operações

* Validar autenticação antes de um saque

* Adicionar taxas ou descontos

Você poderia mudar o método sacar() diretamente… mas isso quebraria o SRP e dificultaria manutenção.

**O Decorator resolve isso encapsulando objetos com novas funcionalidades, sem tocar na classe original.**

### Conceito:
O padrão Decorator permite envolver objetos com comportamento adicional, mantendo a mesma interface.

#### Aplicando Decorator ao projeto
Vamos decorar o comportamento de contas para adicionar logs de operações.

1. Criamos a interface Conta base
```python
# domain/contracts.py
from abc import ABC, abstractmethod

class IConta(ABC):
    """Interface comum para contas bancárias."""

    @abstractmethod
    def depositar(self, valor: float): pass

    @abstractmethod
    def sacar(self, valor: float): pass

    @property
    @abstractmethod
    def saldo(self): pass

```
2. Fazemos Conta implementar a interface
```python
# domain/entities.py
from domain.contracts import IConta

class Conta(IConta):
    ...
```
3. Criamos o decorator de conta
```python
# domain/decorators.py
from domain.contracts import IConta

class ContaComLog(IConta):
    """Decorator que adiciona logs a uma conta."""

    def __init__(self, conta: IConta):
        self._conta = conta

    def depositar(self, valor: float):
        print(f"[LOG] Depositando R${valor:.2f}")
        self._conta.depositar(valor)

    def sacar(self, valor: float):
        print(f"[LOG] Sacando R${valor:.2f}")
        self._conta.sacar(valor)

    @property
    def saldo(self):
        return self._conta.saldo

```
4. Uso no main.py
```python
from domain.decorators import ContaComLog

conta = ContaCorrente("0001", cliente, limite=1000)
conta = ContaComLog(conta)  # Aplica o decorator

conta.depositar(300)
conta.sacar(100)
```
### Benefícios do Decorator no projeto
| Vantagem                        | Explicação                         |
| ------------------------------- | ---------------------------------- |
| Comportamento adicional isolado | Sem alterar a classe original      |
| Pode combinar vários decorators | Segurança, log, validação etc.     |
| Desacoplamento total            | `Conta` não sabe que foi decorada  |
| Código mais limpo e testável    | Cada recurso em sua própria classe |

#### E se precisar combinar com outros?
```python
conta = ContaComAutenticacao(ContaComLog(conta))
```
