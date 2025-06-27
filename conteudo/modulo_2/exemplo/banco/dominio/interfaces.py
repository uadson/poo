from abc import ABC, abstractmethod


class ContaRepositoryInterface(ABC):
    """Interface para operações de persistência de contas."""

    @abstractmethod
    def salvar_conta(self, conta):
        """Salva uma conta no repositório.

        Args:
            conta (Conta): Conta a ser salva.
        """
        pass

    @abstractmethod
    def obter_conta(self, numero: str):
        """Obtém uma conta pelo número.

        Args:
            numero (str): Número da conta.

        Returns:
            Conta (Conta): Conta correspondente.
        """
        pass


class ClienteRepositoryInterface(ABC):
    """Interface para operações de persistência de clientes."""

    @abstractmethod
    def salvar_cliente(self, cliente):
        """Salva um cliente no repositório.

        Args:
            cliente (Cliente): Cliente a ser salvo.
        """
        pass

    @abstractmethod
    def obter_cliente(self, cpf: str):
        """Obtém um cliente pelo CPF.

        Args:
            cpf (str): CPF do cliente.

        Returns:
            Cliente (Cliente): Cliente correspondente.
        """
        pass
