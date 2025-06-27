from dominio.interfaces import (
    ClienteRepositoryInterface,
    ContaRepositoryInterface,
)


class RepositorioEmMemoria(ContaRepositoryInterface, ClienteRepositoryInterface):
    """Implementação de repositório em memória para clientes e contas."""

    def __init__(self):
        self.contas = {}
        self.clientes = {}

    def salvar_conta(self, conta):
        """Salva uma conta no dicionário interno."""
        self.contas[conta.numero] = conta

    def obter_conta(self, numero):
        """Obtém uma conta pelo número."""
        return self.contas.get(numero)

    def salvar_cliente(self, cliente):
        """Salva um cliente no dicionário interno."""
        self.clientes[cliente.cpf] = cliente

    def obter_cliente(self, cpf):
        """Obtém um cliente pelo CPF."""
        return self.clientes.get(cpf)
