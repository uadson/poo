class Pessoa:
    olhos = 2

    def __init__(self, *filhos, nome=None, idade=37):
        self.nome = nome
        self.idade = idade
        self.filhos = list(filhos)

    def cumprimentar(self):
        return f'Olá {id(self)}'

    @staticmethod
    def metodo_estatico():
        return 42
    
    @classmethod
    def nome_e_atributos_de_classe(cls):
        return f'{cls} - olhos {cls.olhos}'

class Homem(Pessoa):
    pass



if __name__ == '__main__':
    uadson = Pessoa(nome='Uadson')
    emile = Pessoa(uadson, nome='Emile')

    print(Pessoa.cumprimentar(uadson))
    print(id(uadson))
    print(uadson.cumprimentar())
    print(uadson.nome)
    print(uadson.idade)
    for filho in emile.filhos:
        print(filho.nome)
    print(uadson.metodo_estatico())
    print(Pessoa.nome_e_atributos_de_classe())
    
    print()
    
    castro = Homem(uadson, emile, nome='Castro')
    print(Homem.cumprimentar(castro))
    print(id(castro))
    print(castro.cumprimentar())
    print(castro.nome)
    print(castro.idade)
    for filho in castro.filhos:
        print(filho.nome, end=' ')
    print('\n', castro.metodo_estatico())
    print(Homem.nome_e_atributos_de_classe())

    print()

    print(isinstance(castro, Pessoa))
    print(isinstance(castro, Homem))

    pessoa = Pessoa()

    print(isinstance(pessoa, Pessoa))
    print(isinstance(pessoa, Homem))

