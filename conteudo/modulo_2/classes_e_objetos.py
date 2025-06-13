class MinhaClasse:
    """
    Um blueprint ou molde para criar objetos.
    Define as características (atributos) e os
    comportamentos (métodos) que os objetos podem ter.
    """

    # Atributos de classe
    atributo_de_classe = "Este é um atributo de classe"

    def __init__(self, atributo_de_instancia):
        """
        Método construtor que inicializa os atributos de instância.

        Args:

            self: Referência à instância atual.
            atributo_de_instancia (str): Um atributo específico para cada instância.
        """
        self.atributo_de_instancia = atributo_de_instancia

    def metodo_de_instancia(self):
        """
        Método que pode ser chamado em uma instância da classe.

        Args:

            self: Referência à instância atual.

        Returns:

            value (str): Uma string representando o comportamento do método.
        """
        return f"Este é um método de instância. Atributo de instância: {self.atributo_de_instancia}"

    @classmethod
    def metodo_de_classe(cls):
        """
        Método de classe que pode ser chamado na classe, não em uma instância.

        Args:

            cls: Referência à classe atual.

        Returns:

            value (str): Uma string representando o comportamento do método de classe.
        """
        return (
            f"Este é um método de classe. Atributo de classe: {cls.atributo_de_classe}"
        )

    @staticmethod
    def metodo_estatico():
        """
        Método estático que não depende de instância ou classe.

        Returns:

            value (str): Uma string representando o comportamento do método estático.
        """
        return "Este é um método estático. Não depende de instância ou classe."


# Exemplo de uso da classe
if __name__ == "__main__":
    # Criando uma instância da classe
    objeto = MinhaClasse("Atributo de Instância 1")

    # Acessando o atributo de instância
    print(objeto.atributo_de_instancia)

    # Chamando o método de instância
    print(objeto.metodo_de_instancia())

    # Chamando o método de classe
    print(MinhaClasse.metodo_de_classe())

    # Chamando o método estático
    print(MinhaClasse.metodo_estatico())

    # Criando outro objeto da mesma classe
    objeto2 = MinhaClasse("Atributo de Instância 2")

    # Acessando o atributo de instância do segundo objeto
    print(objeto2.atributo_de_instancia)

    # Chamando o método de instância do segundo objeto
    print(objeto2.metodo_de_instancia())

    # Verificando o atributo de classe
    print(MinhaClasse.atributo_de_classe)
