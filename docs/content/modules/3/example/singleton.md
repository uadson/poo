# 1. Singleton Pattern
**Catetoria**: _criacional_

**Problema** : Garantir que exista apenas uma instância de uma classe no sistema (por exemplo, um
banco de dados, configurações, logger etc.)

## Quando usar?
Nosso projeto bancário, um exemplo comum é o repositório:
Queremos ter uma única instância centralizada de onde buscamos e salvamos contas e clientes.

### Conceito:
O padrão Singleton garante que uma classe tenha apenas uma instância, fornece um ponto de
acesso global a ela.

#### Exemplo aplicado ao projeto: Repositório em memória (RepositorioEmMemoria()) como Singleton
* Antes (instância criada toda vez)

```python
# cli.py
repo = RepositorioEmMemoria()

repo2 = RepositorioEmMemoria()

assert repo is not repo2  # False
```

Cada vez que você cria repo = RepositorioEmMemoria(), é uma nova instância separada.

* Depois (com singleton)

```python
# infra/repo_singleton.py
from domain.interfaces import ContaRepositoryInterface, ClienteRepositoryInterface


class RepositorioEmMemoriaSingleton(
    ContaRepositoryInterface, ClienteRepositoryInterface
):
    """Implementação de repositório em memória que segue o padrão Singleton.

    Garante que apenas uma instância do repositório exista em todo o sistema,
    fornecendo um ponto de acesso global para os dados de contas e clientes
    armazenados em memória.

    Attributes:
        _instancia (RepositorioEmMemoriaSingleton): A única instância da classe.
        contas (dict): Um dicionário para armazenar contas, com o número da conta como chave.
        clientes (dict): Um dicionário para armazenar clientes, com o CPF como chave.
    """

    _instancia = None

    def __new__(cls):
        """Cria ou retorna a instância única da classe.

        Se a instância ainda não existir, ela é criada e inicializada com
        dicionários vazios para contas e clientes. Caso contrário, a instância
        existente é retornada.

        Returns:
            RepositorioEmMemoriaSingleton: A instância única do repositório.
        """
        if cls._instancia is None:
            cls._instancia = super().__new__(cls) [¹]
            cls._instancia.contas = {}
            cls._instancia.clientes = {}
        return cls._instancia

    def salvar_conta(self, conta):
        """Salva uma instância de Conta no repositório.

        Args:
            conta (Conta): O objeto de conta a ser armazenado.
        """
        self.contas[conta.numero] = conta

    def obter_conta(self, numero):
        """Busca uma conta pelo seu número.

        Args:
            numero (str): O número da conta a ser buscada.

        Returns:
            Conta | None: O objeto da conta, se encontrado, caso contrário None.
        """
        return self.contas.get(numero)

    def salvar_cliente(self, cliente):
        """Salva uma instância de Cliente no repositório.

        Args:
            cliente (Cliente): O objeto de cliente a ser armazenado.
        """
        self.clientes[cliente.cpf] = cliente

    def obter_cliente(self, cpf):
        """Busca um cliente pelo seu CPF.

        Args:
            cpf (str): O CPF do cliente a ser buscado.

        Returns:
            Cliente | None: O objeto do cliente, se encontrado, caso contrário None.
        """
        return self.clientes.get(cpf)
```
* Uso no código
  
```python
# main.py
from infra.repositorio_memoria import RepositorioEmMemoriaSingleton

repo = RepositorioEmMemoriaSingleton()

# Pode chamar de novo sem problemas — será sempre a mesma instância
repo2 = RepositorioEmMemoriaSingleton()

assert repo is repo2  # True
```
### Benefícios no projeto
- Repositório único e centralizado

- Evita bugs por múltiplas instâncias com dados diferentes

- Pode ser usado para loggers, configs, cache...


**Esse padrão é ideal quando precisamos de um recurso compartilhado por todo o sistema.**



######  [¹] _"Muitas vezes nos referimos ao ```__init__``` como o método construtor, mas isso é porque adotamos o jargão de outras linguagens. No Python, ```__init__``` recebe self como primeiro argumentos, portanto o objeto já existe quando ```__init__``` é invocado pelo interpretador. Além disso, ```__init__``` não pode devolver nada. Então, na verdade, esse método é um inicializador, não um construtor._ 

###### _Quando uma classe é chamada para criar uma instância, o método especial chamado pelo Python naquela classe para construir a instância é ```__new__```. - Ramalho, Luciano - [Python Fluente](https://pythonfluente.com/2/#flexible_new_sec) (2ª Edição - 2023)"_