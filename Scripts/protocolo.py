from datetime import date

class Autuado:
    def __init__(self, nome, insc, cpf, cnpj):
        self.nome = nome
        self.insc = insc
        self.cpf = cpf
        self.cnpj = cnpj

    def __str__(self):
        return (
            f'''
            {self.nome},
            {self.insc},
            {self.cpf},
            {self.cnpj}
            '''
        )
class Categoria:
    def __init__(self, codigo, nome, numero, data_emissao, origem, descricao):
        self.codigo = codigo
        self.nome = nome
        self.numero = numero
        self.data_emissao = data_emissao
        self.origem = origem
        self.descricao = descricao

    def __str__(self):
        return f'''
        {self.codigo},
        {self.nome},
        {self.numero},
        {self.data_emissao},
        {self.origem},
        {self.descricao}
        '''

class Andamento:
    def __init__(self, codigo, nome, data):
        self.codigo = codigo
        self.nome = nome
        self.data = data

    def __str__(self):
        return (
            f'''
            {self.codigo},
            {self.nome},
            {self.data}
            '''
        )

class Protocolo:
    def __init__(self, numero, data_criacao, autuado, categoria, andamento):
        self.numero = numero
        self.data_criacao = data_criacao
        self.autuado = autuado
        self.categoria = categoria
        self.andamento = andamento

    def __str__(self):
        return(
            f'''
            {self.numero},
            {self.data_criacao},
            {self.autuado},
            {self.categoria},
            {self.andamento}
            '''
        )

if __name__ == '__main__':
    data = date.today()

    autuado = Autuado('uadson', '123456', '00300400511', '--')
    categoria = Categoria('01', 'auto de infracao', '233445', '2020-12-15', 'DPFISC', 'Lorem Lupsum')
    andamento = Andamento('01', 'prazo para defesa', data)
    processo = Protocolo('00000001', data, autuado, categoria, andamento)

    print(processo)

# output

'''00000001,
2021-01-28,

uadson,
123456,
00176085114,
--
,

01,
auto de infracao,
233445,
15-12-2020,
DPFISC,
Lorem Lupsum
,

01,
prazo para defesa,
2021-01-28'''
