"""
1. SRP - Single Responsibility Principle (Princípio da Responsabilidade Única)
    "Uma classe deve ter uma única responsabilidade. Apenas uma razão para mudar."
    Teoria:
        Cada classe deve ter uma única responsabilidade clara.
        Evita classes que fazem tudo e mais um pouco (God Objects).
"""

from abc import ABC, abstractmethod


# 1. --- Exemplo que viola SRP ---
class ContaX:
    """
    Classe que representa uma conta bancária, violando o SRP ao incluir lógica de persistência.

    Attributes:
        numero (int): O número da conta.
        cliente (str): O nome do cliente associado à conta.
        saldo (float): O saldo atual da conta.
    """

    def __init__(self, numero, cliente):
        """
        Inicializa uma nova instância da classe Conta.

        Args:
            numero (int): O número da conta.
            cliente (str): O nome do cliente associado à conta.
        """
        self.numero = numero
        self.cliente = cliente
        self.saldo = 0

    def salvar_no_arquivo(self):
        """
        Salva as informações da conta em um arquivo.

        Este método viola o SRP ao misturar a lógica de persistência com a lógica da conta.
        """
        # responsabilidade de persistência misturada
        ...


# X --- A classe Conta está misturando:
# - Lógica de domínio (bancária)
# - Lógica de persistência


# 2. --- Exemplo respeitando SRP ---
class ContaY:
    """
    Classe que representa uma conta bancária, respeitando o SRP.

    Attributes:
        numero (int): O número da conta.
        cliente (str): O nome do cliente associado à conta.
        saldo (float): O saldo atual da conta.
    """

    def __init__(self, numero, cliente):
        self.numero = numero
        self.cliente = cliente
        self.saldo = 0.0


class ContaRepository:
    def salvar(self, conta):
        """
        Salva as informações da conta em um armazenamento persistente.

        Args:
            conta (ContaY): A instância da conta a ser salva.
        """

        # salvar a conta em JSON, banco etc.
        ...


# --- Agora cada classe tem uma só responsabilidade. ---


"""
2. OCP - Open-Closed Principle (Princípio Aberto-Fechado)
    "Entidades devem ser abertas para extensão, mas fechadas para modificação."
    Teoria:
        Você deve poder adicionar novos comportamentos sem modificar o código existente.
"""


# 1. --- Exemplo que viola OCP ---
class OperacoesBancarias:
    """
    Classe que executa operações bancárias, violando o OCP ao exigir modificações para novas operações.
    """

    @staticmethod
    def executar(tipo, conta, valor):
        """
        Executa uma operação bancária na conta especificada.

        Args:
            tipo (str): O tipo de operação ("deposito" ou "saque").
            conta (Conta): A conta na qual a operação será realizada.
            valor (float): O valor da operação.

        Raises:
            Exception: Se o tipo de operação não for suportado.
        """
        if tipo == 'deposito':
            conta.depositar(valor)
        elif tipo == 'saque':
            conta.sacar(valor)
        else:
            raise Exception('Tipo de operação não suportado.')


# X. --- Toda vez que surgir uma nova operação, você terá que modificar a classe. ---


# 2. --- Exemplo com poliformismo respeitando OCP ---
class Operacao(ABC):
    """
    Classe abstrata que define uma operação bancária.

    Methods:
        executar(self, conta, valor): Método abstrato para executar a operação.
    """

    @abstractmethod
    def executar(conta, valor):
        """
        Executa a operação bancária na conta especificada.

        Args:
            conta (Conta): A conta na qual a operação será realizada.
            valor (float): O valor da operação.

        Raises:
            NotImplementedError: Se o método não for implementado na subclasse.
        """
        raise NotImplementedError()


class Deposito(Operacao):
    """
    Classe que representa uma operação de depósito.

    Attributes:
        saldo (float): O saldo atual da conta.
    """

    @staticmethod
    def executar(conta, valor):
        """Executa a operação de depósito."""
        conta.depositar(valor)


class Saque(Operacao):
    """
    Classe que representa uma operação de saque.

    Attributes:
        saldo (float): O saldo atual da conta.
    """

    @staticmethod
    def executar(conta, valor):
        """Executa a operação de saque."""
        conta.sacar(valor)


# --- Agora você pode criar novas operações sem alterar a classe base. Basta herdar! ---


"""
3. LSP - Liskov Substitution Principle (Princípio da Substituição de Liskov)
    “Se S é subtipo de T, você deve poder usar S onde T é esperado sem quebrar o sistema.”
    Teoria:
        Classes filhas devem respeitar o comportamento esperado da classe base.
"""


# 1. --- Exemplo que viola LSP ---
class Conta:
    """
    Classe que representa uma conta bancária, servindo como classe base.

    Attributes:
        saldo (float): O saldo atual da conta.
    """

    def __init__(self):
        """
        Inicializa uma nova instância da classe Conta com saldo zero.
        """
        self._saldo = 0

    def sacar(self, valor):
        """
        Realiza um saque na conta.

        Args:
            valor (float): O valor a ser sacado.
        """
        self._saldo -= valor


class ContaRestritaX(Conta):
    @staticmethod
    def sacar(valor):
        """
        Tenta realizar um saque em uma conta restrita, o que sempre levanta uma exceção.

        Args:
            valor (float): O valor a ser sacado.

        Raises:
            Exception: Sempre levantada, indicando que saques não são permitidos.
        """
        raise Exception('Contas restritas não podem sacar!')


# X. --- Você espera que sacar() funcione, mas essa subclasse quebra a expectativa. ---


# 2. --- Exemplo respeitando OCP ---
class ContaRestritaY(Conta):
    def __init__(self, limite=50):
        super().__init__()
        self._limite = limite

    def sacar(self, valor):
        print('Saque permitido até R$50')
        """
        Realiza um saque na conta, respeitando o limite máximo de R$50.

        Args:
            valor (float): O valor a ser sacado.
        """
        if valor <= self._limite:
            self._saldo -= valor
        else:
            print('Limite excedido.')


# --- Mesmo com restrições, o método sacar() continua respeitando a interface da base. ---


"""
4. ISP - Interface Segregation Principle (Princípio da Segregação da Interface)
    “Clientes não devem ser forçados a depender de métodos que não usam.”
    Teoria:
        Classes devem implementar apenas métodos que fazem sentido para elas.
        Em Python, isso se aplica mais à herança de classes abstratas do que interfaces puras.
"""


# 1. --- Exemplo que viola ISP ---
class Conta(ABC):
    """
    Classe abstrata que representa uma conta bancária, violando o ISP ao incluir um método não
    aplicável a todas as subclasses.
    """

    @abstractmethod
    def aplicar_juros(self):
        """
        Aplica juros à conta.

        Raises:
            NotImplementedError: Se o método não for implementado na subclasse.
        """
        raise NotImplementedError()


class ContaCorrente(Conta):
    def aplicar_juros(self):
        """
        Tenta aplicar juros em uma conta corrente, o que não é suportado.

        Raises:
            NotImplementedError: Sempre levantada, indicando que a operação não é suportada.
        """
        raise NotImplementedError()


# 2. --- Exemplo respeitando ISP (dividindo interfaces) ---
class Conta(ABC):
    """
    Classe abstrata que representa uma conta bancária com operações básicas.

    Methods:
        sacar(self, valor): Método abstrato para realizar um saque.
    """

    @abstractmethod
    def sacar(self, valor):
        """
        Realiza um saque na conta.

        Args:
            valor (float): O valor a ser sacado.

        Raises:
            NotImplementedError: Se o método não for implementado na subclasse.
        """
        raise NotImplementedError()


class Rendavel(ABC):
    """
    Interface que define a capacidade de aplicar juros a uma conta.

    Methods:
        aplicar_juros(self): Método abstrato para aplicar juros.
    """

    @abstractmethod
    def aplicar_juros(self):
        """
        Aplica juros à conta.

        Raises:
            NotImplementedError: Se o método não for implementado na subclasse.
        """
        raise NotImplementedError()


class ContaPoupanca(Conta, Rendavel):
    def aplicar_juros(self):
        self._saldo *= 1.01


# --- Agora apenas as classes que precisam de juros implementam aplicar_juros. ---


"""
5. DIP - Dependency Inversion Principle (Princípio da Inversão de Dependência)
    “Dependa de abstrações, não de implementações concretas.”
    Teoria:
        Use classes e funções que recebem objetos genéricos, não instanciam eles diretamente.
"""


# 1. --- Exemplo que viola DIP ---
class BancoX:
    """
    Classe que representa um banco, violando o DIP ao depender de uma implementação concreta.

    Attributes:
        repositorio (ContaRepository): Uma instância do repositório de contas.
    """

    def __init__(self):
        """
        Inicializa uma nova instância da classe Banco.

        Depende da classe concreta ContaRepository(), violando o DIP.
        """
        self.repositorio = ContaRepository()


# X --- Depende da classe concreta ContaRepository() ---


# 2. --- Exemplo respeitando DIP ---
class BancoY:
    """
    Classe que representa um banco, respeitando o DIP ao depender de uma abstração.

    Attributes:
        repositorio (ContaRepository): Uma instância de um repositório de contas, que pode ser
                                       qualquer implementação que siga a interface.
    """

    def __init__(self, repositorio):
        """
        Inicializa uma nova instância da classe Banco.

        Args:
            repositorio (object): Uma instância de um repositório de contas, que deve ser uma
                                  abstração (interface).
        """
        self.repositorio = repositorio  # ✔ depende de abstração


banco = BancoY(ContaRepository())
# --- Pode passar qualquer implementação ---
