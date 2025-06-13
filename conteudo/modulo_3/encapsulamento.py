class Encapsulamento:
    """
    Classe que demonstra o encapsulamento em Python.
    O encapsulamento é uma prática de programação que restringe o acesso a certos componentes de um objeto,
    protegendo seus dados internos e métodos de serem acessados diretamente de fora da classe.
    """

    def __init__(self, publico, protegido, privado):
        """
        Método construtor que inicializa os atributos publico, protegido e privado.

        Args:

        publico (str): Um atributo publico, não será encapsulado.
        protegido (str): Um atributo que será encapsulado.
        privado (str): Um atributo que será encapsulado.
        """
        # Atributos de instância
        # Atributo público
        self.publico = publico
        # Atributo protegido
        self._protegido = protegido
        # Atributo privado
        self.__privado = privado

    def metodo_publico(self):
        """
        Método para acessar o atributo público.
        Este método é público e pode ser chamado de fora da classe.

        Returns:

            value (str): O valor do atributo público.
        """
        return f'Valor público: {self.publico}'

    def _metodo_protegido(self):
        """
        Método getter para acessar o atributo protegido.

        Returns:

            value (str): O valor do atributo protegido.
        """
        return f'Valor protegido: {self._protegido}'

    def __metodo_privado(self):
        """
        Método setter para modificar o atributo privado.

        Returns:

            value (int): O valor do atributo privado.
        """
        return f'Valor privado: {self.__privado}'

    # Propriedades (Getters e Setters)
    @property
    def valor_protegido(self):
        return self._protegido

    @property
    def valor_privado(self):
        return self.__privado

    @valor_privado.setter
    def valor_privado(self, valor):
        if valor > 0:
            self.__privado = valor
        else:
            print('O valor do atributo privado deve ser maior que zero.')


# Exemplo de uso da classe
if __name__ == '__main__':
    # Criando uma instância da classe
    encapsulamento = Encapsulamento('Atributo Público', 'Atributo Protegido', 10)

    # Acessando o atributo público
    print(encapsulamento.metodo_publico())

    # Acessando o atributo protegido (não recomendado, mas possível)
    print(encapsulamento._metodo_protegido())

    # Acessando o atributo privado (não recomendado, mas possível)
    print(encapsulamento._Encapsulamento__metodo_privado())

    # Usando propriedades
    print(encapsulamento.valor_protegido)
    print(encapsulamento.valor_privado)

    # Modificando o valor do atributo privado
    encapsulamento.valor_privado = 20
    print(encapsulamento.valor_privado)
    # Tentando modificar o valor do atributo privado para um valor inválido
    encapsulamento.valor_privado = -5  # Deve imprimir uma mensagem de erro
    print(encapsulamento.valor_privado)
    # Acessando o atributo privado diretamente (não recomendado)
    # print(encapsulamento.__privado)  # Isso causaria um erro, pois é privado
    # Acessando o atributo protegido diretamente (não recomendado)
    # print(encapsulamento._protegido)  # Isso é possível, mas não recomendado
    # Acessando o atributo público diretamente
    print(encapsulamento.publico)  # Isso é permitido, pois é público
