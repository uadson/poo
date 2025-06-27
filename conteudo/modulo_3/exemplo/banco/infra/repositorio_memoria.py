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
            cls._instancia = super().__new__(cls)
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
