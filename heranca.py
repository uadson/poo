class Pessoa:
    olhos = 2
    garras = 0

    def __init__(self, *filhos, nome=None, idade=37):
        self.nome = nome
        self.idade = idade
        self.filhos = list(filhos)

    def cumprimentar(self):
        return f'Olá, meu nome é {self.nome}.'

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

    Pessoa.olhos = 3
    print(emile.olhos)
    print(Pessoa.cumprimentar(uadson))
    print(id(uadson))
    print(uadson.cumprimentar())
    print(uadson.nome)
    # atributo dinâmico
    uadson.sobrenome = 'Feitosa'
    print(uadson.sobrenome)
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

    #atributo especial para conferir todas os atributos de instância
    # __dict__

    print()
    print(uadson.__dict__)
    print(emile.__dict__)

    # removendo atributo dinâmico
    del emile.filhos
    print(emile.__dict__)
    print(castro.__dict__)

'''
OUTPUT

3
Olá, meu nome é Uadson.
140270192883504
Olá, meu nome é Uadson.
Uadson
Feitosa
37
Uadson
42
<class '__main__.Pessoa'> - olhos 3

Olá, meu nome é Castro.
140270192883264
Olá, meu nome é Castro.
Castro
37
Uadson Emile 
 42
<class '__main__.Homem'> - olhos 3

True
True
True
False

{'nome': 'Uadson', 'idade': 37, 'filhos': [], 'sobrenome': 'Feitosa'}
{'nome': 'Emile', 'idade': 37, 'filhos': [<__main__.Pessoa object at 0x7f933304f730>]}
{'nome': 'Emile', 'idade': 37}
{'nome': 'Castro', 'idade': 37, 'filhos': [<__main__.Pessoa object at 0x7f933304f730>, <__main__.Pessoa object at 0x7f933304f6d0>]}
'''