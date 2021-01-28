class ListaCompras:

    def __init__(self, *itens, nome=None):
        self.nome = nome
        self.itens = list(itens)

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

    print(objetoLista.nome)
    
    print()

    for item in objetoLista.itens:
        print(item.nome)

'''
output

Lista de Compras

Arroz
Feijão
Carne
Tomate
Batata
'''