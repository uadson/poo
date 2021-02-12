from heranca import Pessoa


'''
class Pessoa:
    ...
    def cumprimentar(self):
        return f'Olá, meu nome é {self.nome}.'
'''
class Homem(Pessoa):
    def cumprimentar(self):
        #return f'{super().cumprimentar()} Aperto de Mão.'
        metodo_classe_pai = super().cumprimentar()
        return f'{metodo_classe_pai} Aperto de Mão.'


if __name__ == '__main__':
    uadson = Homem(nome='Uadson')
    print(uadson.cumprimentar())