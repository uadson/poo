from abc import ABC, abstractmethod  # Para classes abstratas


# Polimorfismo (Duck Typing)
class Pato:
    """
    Classe que representa um pato.
    Implementa o método fazer_som para retornar o som específico de um pato.
    """

    @staticmethod
    def fazer_som():
        """
        Método que retorna o som do pato.

        Returns:
            value (str): Som do pato.
        """
        return "Quack Quack"


class Cachorro:
    """
    Classe que representa um cachorro.
    Implementa o método fazer_som para retornar o som específico de um cachorro.
    """

    @staticmethod
    def fazer_som():
        """
        Método que retorna o som do cachorro.

        Returns:
            value (str): Som do cachorro.
        """
        return "Au Au"


def fazer_som_do_animal(animal):
    """
    Função que recebe um animal e retorna o som dele.

    Args:
        animal (object): Objeto que implementa o método fazer_som.

    Returns:
        value (str): Som do animal.
    """
    return animal.fazer_som()


pato = Pato()
cachorro = Cachorro()
print(fazer_som_do_animal(pato))  # Saída: Quack Quack
print(fazer_som_do_animal(cachorro))  # Saída: Au Au


# Abstração
class Forma(ABC):
    """
    Classe abstrata que representa uma forma geométrica.
    Contém um método abstrato calcular_area que deve ser implementado pelas subclasses.
    """

    @abstractmethod
    def calcular_area():
        """
        Método abstrato que deve ser implementado pelas subclasses para calcular a área da forma.

        Returns:
            value (float): Área da forma.
        """
        pass

    @abstractmethod
    def calcular_perimetro():
        """
        Método abstrato que deve ser implementado pelas subclasses para calcular o perímetro da forma.

        Returns:
            value (float): Perímetro da forma.
        """
        pass

    @abstractmethod
    def obter_nome():
        """
        Método que retorna o nome da forma.

        Returns:
            value (float): Nome da forma.
        """
        return "Forma Geométrica"


class Circulo(Forma):
    """
    Classe que representa um círculo, herdando da classe Forma.
    Implementa os métodos calcular_area e calcular_perimetro.
    """

    def __init__(self, raio):
        """
        Método inicializador.

        Attributes:
            raio (float): Raio do círculo.
        """
        self.raio = raio

    def calcular_area(self):
        """
        Método que calcula a área do círculo.

        Returns:
            value (float): Área do círculo.
        """
        return 3.14 * (self.raio**2)

    def calcular_perimetro(self):
        """
        Método que calcula o perímetro do círculo.

        Returns:
            value (float): Perímetro do círculo.
        """
        return 2 * 3.14 * self.raio


# Obs.: Não é possível instanciar a classe Forma diretamente, pois é abstrata.
# circulo = Forma() # TypeError: Can't instantiate abstract class Forma with abstract methods calcular_area,
# calcular_perimetro

circulo = Circulo(5)
print(circulo.calcular_area())  # Saída: 78.5
print(circulo.calcular_perimetro())  # Saída: 31.400000000000002
print(circulo.obter_nome())  # Saída: Forma Geométrica
