class ListaCompras:
    forma_pagamento = {
        1: 'dinheiro',
        2: 'cartão',
        3: 'bitcoin',
    }

    def __init__(self, *itens, nome=None):
        self.nome = nome
        self.itens = list(itens)
    
    @staticmethod
    def tabela():
        return '-' * 42

    @classmethod
    def pagar(cls, select):
        return cls.forma_pagamento.get(select)        

if __name__ == '__main__':
    objetoA = ListaCompras(nome='Arroz')
    objetoB = ListaCompras(nome='Feijão')
    objetoC = ListaCompras(nome='Carne')
    objetoD = ListaCompras(nome='Tomate')
    objetoE = ListaCompras(nome='Batata')

    objetoLista = ListaCompras(
        objetoA, 
        objetoB, 
        objetoC, 
        objetoD, 
        objetoE, 
        nome='Lista de Compras'
    )

    print(ListaCompras.tabela())

    print(objetoLista.nome)
    for item in objetoLista.itens:
        print(item.nome)

    print(ListaCompras.tabela())
    
    print('Forma de Pagamento:')
    for k, v in objetoLista.forma_pagamento.items():
        print(k, v)
    print(ListaCompras.tabela())
    select = int(input('Selecione uma forma de pagamento: '))
    print(f'Forma de pagamento selecionada: {ListaCompras.pagar(select)}')

    print(objetoLista.tabela())

'''
output

Lista de Compras

Arroz
Feijão
Carne
Tomate
Batata
'''