# Superclasse ou classe Pai
class Animal:
    """
    Classe base para representar um animal.
    Contém métodos e atributos comuns a todos os animais.
    """

    def __init__(self, nome):
        """
        Método construtor que inicializa o nome do animal.

        Args:

            nome (str): Nome do animal.
        """
        self.nome = nome

    def fazer_som(self):
        """
        Método que deve ser implementado pelas subclasses para fazer um som específico.

        Returns:

            value (str): Som do animal.
        """
        raise NotImplementedError('Subclasses devem implementar este método.')


# Subclasse ou classe Filha
class Cachorro(Animal):
    """
    Classe que representa um cachorro, herdando da classe Animal.
    Implementa o método fazer_som para retornar o som específico de um cachorro.
    """

    def __init__(self, nome, raca):
        """
        Método construtor que inicializa o nome do cachorro.

        Args:

            nome (str): Nome do cachorro.
        """
        super().__init__(nome)
        self.raca = raca

    def fazer_som(self):  # Sobrescrever o método da classe pai
        """
        Método que retorna o som do cachorro.

        Returns:

            value (str): Som do cachorro.
        """
        return f'{self.nome} late: Au Au'


# Subclasse ou classe Filha
class Gato(Animal):
    """
    Classe que representa um gato, herdando da classe Animal.
    Implementa o método fazer_som para retornar o som específico de um gato.
    """

    def fazer_som(self):
        """
        Método que retorna o som do gato.

        Returns:

            value (str): Som do gato.
        """
        return f'{self.nome} mia: Miau Miau'


# Herança múltipla
class Voa:
    """
    Classe que representa a capacidade de voar.
    Esta classe pode ser usada como mixin para adicionar comportamento de voo a outras classes.
    """

    @staticmethod
    def voar():
        """
        Método que retorna uma mensagem indicando que o animal pode voar.

        Returns:

            value (str): Mensagem de voo.
        """
        return 'Este animal pode voar.'


class Nada:
    """
    Classe que representa a capacidade de nadar.
    Esta classe pode ser usada como mixin para adicionar comportamento de natação a outras classes.
    """

    @staticmethod
    def nadar():
        """
        Método que retorna uma mensagem indicando que o animal pode nadar.

        Returns:

            value (str): Mensagem de natação.
        """
        return 'Este animal pode nadar.'


class Pato(Animal, Voa, Nada):
    """
    Classe que representa um pato, herdando da classe Animal e mixins Voa e Nada.
    Implementa o método fazer_som para retornar o som específico de um pato.
    """

    def __init__(self, nome):
        """
        Método construtor que inicializa o nome do pato.

        Args:

            nome (str): Nome do pato.
        """
        super().__init__(nome)  # Chama o construtor da primeira superclasse
        # no MRO que tenha __init__

    def fazer_som(self):
        """
        Método que retorna o som do pato.

        Returns:

            value (str): Som do pato.
        """
        return f'{self.nome} grasna: Quack Quack'


# Exemplo de uso das classes
if __name__ == '__main__':
    # Criando instâncias das classes
    cachorro = Cachorro('Rex', 'Labrador')
    gato = Gato('Mia')
    pato = Pato('Donald')

    # Chamando os métodos das instâncias
    print(cachorro.fazer_som())  # Rex late: Au Au
    print(gato.fazer_som())  # Mia mia: Miau Miau
    print(pato.fazer_som())  # Donald grasna: Quack Quack

    # Verificando se o pato pode voar e nadar
    print(pato.voar())  # Este animal pode voar.
    print(pato.nadar())  # Este animal pode nadar.
    # Verificando o tipo das instâncias
    print(isinstance(cachorro, Animal))  # True
    print(isinstance(gato, Animal))  # True
    print(isinstance(pato, Animal))  # True
    print(isinstance(pato, Voa))  # True
    print(isinstance(pato, Nada))  # True
    print(isinstance(pato, Cachorro))  # False
    print(isinstance(pato, Gato))  # False
    print(isinstance(cachorro, Cachorro))  # True
    print(isinstance(gato, Gato))  # True
    print(isinstance(pato, Pato))  # True

    print(Pato.__mro__)  # Mostra a ordem de resolução de métodos (MRO)
