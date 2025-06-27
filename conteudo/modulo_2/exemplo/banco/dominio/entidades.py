from abc import ABC, abstractmethod


class Cliente:
    """Representa um cliente do banco.

    Attributes:
        nome (str): Nome do cliente.
        cpf (str): CPF do cliente.
    """

    def __init__(self, nome: str, cpf: str):
        self.nome = nome
        self.cpf = cpf


class Conta(ABC):
    """Classe abstrata base para tipos de conta bancária.

    Attributes:
        numero (str): Número da conta.
        cliente (Cliente): Cliente dono da conta.
        _saldo (float): Saldo da conta.
    """

    def __init__(self, numero: str, cliente: Cliente):
        self.numero = numero
        self.cliente = cliente
        self._saldo = 0.0

    @property
    def saldo(self):
        """float: Retorna o saldo atual da conta."""
        return self._saldo

    def depositar(self, valor: float):
        """Realiza um depósito na conta.

        Args:
            valor (float): Valor a ser depositado.
        """
        if valor > 0:
            self._saldo += valor

    @abstractmethod
    def sacar(self, valor: float):
        """Realiza um saque da conta.

        Args:
            valor (float): Valor a ser sacado.
        """
        pass


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


class ContaPoupanca(Conta):
    """Conta poupança sem limite de saque adicional."""

    def sacar(self, valor: float):
        """Realiza um saque se houver saldo suficiente.

        Args:
            valor (float): Valor a ser sacado.
        """
        if valor <= self._saldo:
            self._saldo -= valor
