class Motor:
    """
    Classe que representa um motor de um carro.
    """

    def __init__(self, tipo):
        """
        Inicializa o motor com um tipo específico.

        Args:
            tipo (str): O tipo do motor (ex: "V6", "V8").
        """
        self.tipo = tipo

    def ligar(self):
        """
        Liga o motor.

        Returns:
            value (str): Motor (self.tipo) ligado!
        """
        return f'Motor {self.tipo} ligado!'


# Composição
class Carro:
    def __init__(self, marca, modelo, tipo_motor):
        """
        Inicializa o carro com uma marca, modelo e um motor.

        Args:

            marca (str): A marca do carro.
            modelo (str): O modelo do carro.
            tipo_motor (str): O tipo do motor do carro.
        """
        self.marca = marca
        self.modelo = modelo
        self.motor = Motor(tipo_motor)  # Carro "tem um" Motor

    def dirigir(self):
        """
        Liga o motor e retorna uma mensagem indicando que o carro está pronto para dirigir.

        Returns:

            value (str): Mensagem indicando que o carro está pronto para dirigir.
        """
        return f'{self.motor.ligar()} Carro {self.marca} {self.modelo} pronto para dirigir!'


# Agregação / Relação
class Biblioteca:
    def __init__(self, nome):
        """
        Inicializa a biblioteca com um nome.

        Args:

            nome (str): O nome da biblioteca.
        """
        self.nome = nome
        self.livros = []  # Livros podem existir independentemente da biblioteca

    def adicionar_livro(self, livro):
        """
        Adiciona um livro à biblioteca.

        Args:

            livro (str): O título do livro a ser adicionado.
        """
        self.livros.append(livro)

    def listar_livros(self):
        """
        Lista todos os livros na biblioteca.

        Returns:

            value (list): Lista de livros na biblioteca.
        """
        return f'Livros na biblioteca {self.nome}: {", ".join(str(livro) for livro in self.livros)}'


class Livro:
    def __init__(self, titulo, autor):
        """
        Inicializa o livro com um título e um autor.

        Args:

            titulo (str): O título do livro.
            autor (str): O autor do livro.
        """
        self.titulo = titulo
        self.autor = autor

    def __str__(self):
        """
        Retorna uma representação em string do livro.

        Returns:

            value (str): Representação do livro.
        """
        return f'{self.titulo} por {self.autor}'


# Exemplo de uso
carro = Carro('Ford', 'Focus', 'Gasolina')
print(carro.dirigir())

livro1 = Livro('1984', 'George Orwell')
livro2 = Livro('O Pequeno Príncipe', 'Antoine de Saint-Exupéry')
biblioteca = Biblioteca('Minha Biblioteca')
biblioteca.adicionar_livro(livro1)
biblioteca.adicionar_livro(livro2)
print(biblioteca.listar_livros())
