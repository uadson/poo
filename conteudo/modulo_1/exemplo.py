from abc import ABC, abstractmethod


# ==================================
# Cliente (simples entidade)
# ==================================
class Cliente:
    """
    Representa um cliente do banco, com nome e CPF.
    """

    def __init__(self, nome, cpf):
        self.nome = nome
        self.cpf = cpf


# ==================================
# Conta (classe abstrata)
# ==================================
class Conta(ABC):
    """
    Representa uma conta bancária genérica.

    Encapsulamento: _numero, _cliente, _saldo são atributos privados.
    """

    def __init__(self, numero, cliente):
        self._numero = numero
        self._cliente = cliente
        self._saldo = 0.0

    @property
    def saldo(self):
        """
        Retorna o saldo da conta.
        """
        return self._saldo

    @abstractmethod
    def sacar(self, valor):
        """
        Método abstrato para sacar dinheiro da conta.
        Deve ser implementado pelas subclasses.
        """
        pass

    def depositar(self, valor):
        """
        Deposita um valor na conta.
        """
        if valor > 0:
            self._saldo += valor
            print(f'Depósito de R${valor:.2f} realizado com sucesso.')
        else:
            print('Valor de depósito inválido.')


# ==================================
# ContaCorrente (herda de Conta)
# ==================================
class ContaCorrente(Conta):
    """
    Representa uma conta corrente.
    """

    def __init__(self, numero, cliente, limite=500):
        super().__init__(numero, cliente)
        self._limite = limite

    def sacar(self, valor):
        """
        Saque de dinheiro da conta corrente.
        """
        if valor <= self._saldo + self._limite:
            self._saldo -= valor
            print(f'Saque de R${valor:.2f} realizado com sucesso.')
        else:
            print('Saldo insuficiente.')


# ==================================
# ContaPoupanca (herda de Conta)
# ==================================
class ContaPoupanca(Conta):
    """
    Representa uma conta poupança.
    """

    def sacar(self, valor):
        """
        Saque de dinheiro da conta poupança.
        """
        if valor <= self._saldo:
            self._saldo -= valor
            print(f'Saque de R${valor:.2f} realizado com sucesso.')
        else:
            print('Saldo insuficiente.')


# =====================================
# Agencia (composição dentro de Banco)
# =====================================
class Agencia:
    """
    Representa uma agência bancária.
    """

    def __init__(self, numero):
        self.numero = numero
        self.contas = []

    def adicionar_conta(self, conta):
        """
        Adiciona uma conta à agência.
        """
        self.contas.append(conta)
        print(f'Conta {conta._numero} adicionada à agência {self.numero}.')


# =====================================
# Banco (Agregação)
# =====================================
class Banco:
    """
    Representa um banco com agências e contas.
    """

    def __init__(self, nome):
        self.nome = nome
        self.agencias = []
        self.clientes = []

    def adicionar_cliente(self, cliente):
        """
        Adiciona um cliente ao banco.
        """
        self.clientes.append(cliente)
        print(f'Cliente {cliente.nome} adicionado ao banco {self.nome}.')

    def adicionar_agencia(self, agencia):
        """
        Adiciona uma agência ao banco.
        """
        self.agencias.append(agencia)
        print(f'Agência {agencia.numero} adicionada ao banco {self.nome}.')

    def criar_conta_corrente(self, cliente, agencia_num, numero_conta, limite=500):
        """
        Cria uma conta corrente para um cliente em uma agência.
        """
        agencia = self._buscar_agencia(agencia_num)
        if agencia:
            conta = ContaCorrente(numero_conta, cliente, limite)
            agencia.adicionar_conta(conta)
            print(f'Conta corrente {numero_conta} criada para o cliente {cliente.nome}.')
            return conta

    def criar_conta_poupanca(self, cliente, agencia_num, numero_conta):
        """
        Cria uma conta poupança para um cliente em uma agência.
        """
        agencia = self._buscar_agencia(agencia_num)
        if agencia:
            conta = ContaPoupanca(numero_conta, cliente)
            agencia.adicionar_conta(conta)
            print(f'Conta poupança {numero_conta} criada para o cliente {cliente.nome}.')
            return conta

    def _buscar_agencia(self, numero):
        """
        Busca uma agência pelo número.
        """
        for agencia in self.agencias:
            if agencia.numero == numero:
                return agencia
        print(f'Agência {numero} não encontrada.')
        return None


# =====================================
# Exemplo de uso do sistema bancário
# =====================================


def exemplo_de_uso():
    """Função principal para demonstrar o uso do sistema bancário."""
    # Criando o banco
    banco = Banco('Banco Exemplo')

    # Adicionando clientes
    cliente1 = Cliente('Alice', '123.456.789-00')
    cliente2 = Cliente('Bob', '987.654.321-00')
    banco.adicionar_cliente(cliente1)
    banco.adicionar_cliente(cliente2)

    # Adicionando agências
    agencia1 = Agencia('001')
    agencia2 = Agencia('002')
    banco.adicionar_agencia(agencia1)
    banco.adicionar_agencia(agencia2)

    # Criando contas
    conta_corrente_alice = banco.criar_conta_corrente(cliente1, '001', 'CC001', limite=1000)
    conta_poupanca_bob = banco.criar_conta_poupanca(cliente2, '002', 'CP001')

    # Operações nas contas
    conta_corrente_alice.depositar(500)
    conta_corrente_alice.sacar(200)
    print(f'Saldo da conta corrente de Alice: R${conta_corrente_alice.saldo:.2f}')

    conta_poupanca_bob.depositar(300)
    conta_poupanca_bob.sacar(100)
    print(f'Saldo da conta poupança de Bob: R${conta_poupanca_bob.saldo:.2f}')


if __name__ == '__main__':
    exemplo_de_uso()
