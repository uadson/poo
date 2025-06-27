# 4. Observer Pattern
**Catetoria**: _Comportamental_

**Problema** : Como notificar múltiplos objetos automaticamente quando o estado de outro objeto muda?

## Quando usar?
Imagine que o sistema bancário precise:

* Enviar notificações por e-mail quando alguém saca

* Registrar logs de auditoria

* Atualizar o histórico de transações

Se colocarmos essa lógica dentro do método sacar() da Conta, isso quebra o princípio de responsabilidade única (SRP).

**O Observer permite que a conta emita eventos, e outros objetos reajam de forma desacoplada.**

### Conceito:
O padrão Observer define uma dependência 1:N entre objetos. Quando um objeto muda de estado, todos os observadores são notificados automaticamente.

#### Implementando Observer no projeto
Vamos decorar o comportamento de contas para adicionar logs de operações.

1. Criamos a interface do observador
```python
# domain/observers.py
from abc import ABC, abstractmethod

class OperacaoObserver(ABC):
    """Interface de observador de operações em conta."""

    @abstractmethod
    def notificar(self, conta, tipo, valor): pass

```
2. Exemplo de dois observadores
```python
class AuditoriaLogger(OperacaoObserver):
    def notificar(self, conta, tipo, valor):
        print(f"[AUDITORIA] Conta {conta.numero} fez {tipo} de R${valor:.2f}")

class NotificadorEmail(OperacaoObserver):
    def notificar(self, conta, tipo, valor):
        print(f"[EMAIL] Olá {conta.cliente.nome}, você fez um {tipo} de R${valor:.2f}")
```
3. Adicionamos suporte a observadores na Conta
```python
# domain/entities.py
class Conta:
    def __init__(self, numero, cliente, estrategia_saque):
        self.numero = numero
        self.cliente = cliente
        self._saldo = 0.0
        self._estrategia_saque = estrategia_saque
        self._observadores = []

    def adicionar_observador(self, obs):
        self._observadores.append(obs)

    def _notificar_observadores(self, tipo, valor):
        for obs in self._observadores:
            obs.notificar(self, tipo, valor)

    def depositar(self, valor):
        if valor > 0:
            self._saldo += valor
            self._notificar_observadores("depósito", valor)

    def sacar(self, valor):
        self._estrategia_saque.sacar(self, valor)
        self._notificar_observadores("saque", valor)
```
4. Usando os observadores no main.py
```python
from domain.observers import AuditoriaLogger, NotificadorEmail

conta = ContaCorrente("0001", cliente, limite=1000)
conta.adicionar_observador(AuditoriaLogger())
conta.adicionar_observador(NotificadorEmail())

conta.depositar(200)
conta.sacar(150)

```
### Benefícios do Observer no projeto
| Vantagem                       | Explicação                                    |
| ------------------------------ | --------------------------------------------- |
| Total desacoplamento           | `Conta` não sabe quem reage                   |
| Responsabilidade única mantida | Conta não cuida de notificação                |
| Extensível                     | Adicione novos observadores sem mudar a conta |
| Testável                       | Pode testar notificações isoladamente         |


