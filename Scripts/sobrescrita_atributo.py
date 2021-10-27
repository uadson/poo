from heranca import Pessoa

'''
class Pessoa:
    ...
    garras = 0
    ...
'''

class Mutante(Pessoa):
    #sobrescrevendo um atributo de classe
    garras = 6


if __name__ == '__main__':
    wolverine = Mutante()
    print(wolverine.__dict__)
    print(wolverine.garras)

'''
OUTPUT

{'nome': None, 'idade': 37, 'filhos': []}
6

'''