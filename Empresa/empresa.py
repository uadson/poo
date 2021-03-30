from datetime import datetime
import pandas as pd


class Endereco:
	"""Representação de um registro de endereço
	"""
  def __init__(self):
    self.cidade = str()
    self.uf = str()

end = Endereco()
end.cidade = 'Goiânia'
end.uf = 'Goiás'

endereco = {
    'Cidade': end.cidade,
    'Estado': end.uf
}

df_end = pd.DataFrame(endereco, index= [1])

print(df_end)

class Pessoa(Endereco):
	"""Representação de um registro de pessoa física, com herança
	da classe Endereco.
	"""
  def __init__(self):
    self.__nome = str()
    self.__telefone = str()
    self.__email = str()
    super().__init__()

pess1 = Pessoa()

pess1.__nome = 'Uadson'
pess1.__telefone = '62 9999-8888'
pess1.__email = 'email@email.com.br'
pess1.cidade = end.cidade
pess1.uf = end.uf

pessoa = {
    'Nome': pess1.__nome,
    'Telefone': pess1.__telefone,
    'Email': pess1.__email,
    'Cidade': pess1.cidade,
    'Estado': pess1.uf
}

df_pessoa = pd.DataFrame(pessoa, index= [1])

print(df_pessoa)

class Produto:
	"""Representação de registro de um produto.
	"""
  def __init__(self):
    self.cod = str()
    self.marca = str()
    self.modelo = str()

prod = Produto()

prod.cod = '001'
prod.marca = 'LeveNovo'
prod.modelo = '1234'

produto = {
    'Código': prod.cod,
    'Marca': prod.marca,
    'Modelo': prod.modelo
}

df_produto = pd.DataFrame(produto, index = [1])

print(df_produto)

class Cliente(Pessoa):
	"""Representação de um cadastro de cliente, com herança
	da Classe Pessoa.
	"""
  def __init__(self):
    self.cod = str()
    self.__cnpj = str()
    self.__cpf = str()
    super().__init__()

cli = Cliente()

cli.cod='001'
cli.__cpf = '123.456.789-10'
cli.__nome = pess1.__nome
cli.__telefone = pess1.__telefone
cli.__email = pess1.__email
cli.cidade = pess1.cidade
cli.uf = pess1.uf

cliente = {
    'Código': cli.cod,
    'Nome': cli.__nome,
    'CPF': cli.__cpf,
    'Telefone': cli.__telefone,
    'Email': cli.__email,
    'Cidade': cli.cidade,
    'Estado': cli.uf
}

df_cliente = pd.DataFrame(cliente, index = [1])

print(df_cliente)

class Funcionario(Pessoa):
	"""Representação de um cadastro de Funcionário, herdando 
	da classe Pessoa, os seus atributos.
	"""
  def __init__(self):
    self.cod = str()
    self.salario = float()
    self.dependentes = int()
    self.cargo = str()
    super().__init__()

func1 = Funcionario()
func1.__nome = 'Feitosa'
func1.__telefone = '62 8787-9898'
func1.__cpf = '111.222.333-44'
func1.__email = 'feitosa@email.com.br'
func1.cargo = 'Vendedor'
func1.cod = '0237'
func1.dependentes = '2'
func1.cidade = pess1.cidade
func1.uf = pess1.uf
func1.salario = 4500.00

funcionario = {
    'Código': func1.cod,
    'Nome': func1.__nome,
    'Telefone': func1.__telefone,
    'CPF': func1.__cpf,
    'Email': func1.__email,
    'Dependentes': func1.dependentes,
    'Cidade': func1.cidade,
    'Estado': func1.uf,
    'Cargo': func1.cargo,
    'Salário': func1.salario
}

df_funcionario = pd.DataFrame(funcionario, index = [1])

print(df_funcionario)

class Fornecedor(Cliente):
	"""Representação de um cadastro de um Fornecedor, herdando 
	da Classe Cliente, os seus atributos.
	"""
  def __init__(self):
    super().__init__()

forn1 = Fornecedor()
forn1.__nome = 'UF Informática'
forn1.__cnpj = '12.345.678/0001-90'
forn1.cidade = pess1.cidade
forn1.uf = pess1.uf
forn1.cod = '4037'
forn1.__telefone = '62  7878-8787'
forn1.__email = 'fornecedor@fornecedor.com.br'

fornecedor = {
    'Código': forn1.cod,
    'Nome': forn1.__nome,
    'Telefone': forn1.__telefone,
    'Email': forn1.__email,
    'CNPJ': forn1.__cnpj,
    'Cidade': forn1.cidade,
    'Estado': forn1.uf
}

df_fornecedor = pd.DataFrame(fornecedor, index = [1])

print(df_fornecedor)

class Venda:
	"""Representação de uma ordem de venda
	"""
  def __init__(self):
    self.id = 0
    self.cod = str()
    self.nome_cliente = str()
    self.doc_cliente = str()
    self.prod = str()
    self.valor = float()
    self.cod_vendedor = str()
    self.nome_vendedor = str()
    self.fornecedor = str()

  def confirmar(self):
  	"""Após confirmação da venda, incremeta-se o valor do id
  	"""
    self.id += 1

comp = Venda()
comp.cod = '0001'
comp.nome_cliente = cli.__nome
comp.doc_cliente = cli.__cpf
comp.prod = prod.marca
comp.fornecedor = forn1.__nome
comp.valor = 2500
comp.cod_vendedor = func1.cod
comp.confirmar()
comp.id

compra = {
    'Id': comp.id,
    'Código': comp.cod,
    'Cliente': comp.nome_cliente,
    'CPF': comp.doc_cliente,
    'Produto': prod.marca,
    '(Código)Vendedor': func1.cod,
    '(Nome)Vendedor': func1.__nome,
    'Fornecedor': comp.fornecedor,
    'Valor': comp.valor
}

df_compra = pd.DataFrame(compra, index = [1])

print(df_compra)

# Criando um novo produto

class Notebook(Produto):
	"""Representação de um cadastro de um Notebook, herdando da 
	Classe Produto, os seus atributos
	"""
  def __init__(self):
    self.caractisticas = []
    super().__init__()

# Cadastrando o Produto

laptop = Notebook()
laptop.cod = '002'
laptop.marca = 'Zell'
laptop.modelo = 'Lostro'
laptop.caractisticas = ['Core I5']

notebook = {
    'Código': laptop.cod,
    'Marca': laptop.marca,
    'Modelo': laptop.modelo,
    'Características': laptop.caractisticas
}

df_notebook = pd.DataFrame(notebook, index = [1])

print(df_notebook)

# Cadastrando um cliente

cliente1 = Cliente()

cliente1.cod = '0014'
cliente1.__nome = 'Emile'
cliente1.__telefone = '62 5454-5656'
cliente1.__cpf = '987.654.321.00'
cliente1.__email = 'emile@emile.com.br'
cliente1.cidade = 'Aparecidade de Goiânia'
cliente1.uf = 'Goiás'

emile = {
    'Código': cliente1.cod,
    'Nome': cliente1.__nome,
    'Telefone': cliente1.__telefone,
    'CPF': cliente1.__cpf,
    'Email': cliente1.__email,
    'Cidade': cliente1.cidade,
    'Estado': cliente1.uf
}

df_emile = pd.DataFrame(emile, index = [1])

print(df_emile)