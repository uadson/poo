class Pessoa:
	def __init__(self):
		self.nome = 'Uadson'

	def __str__(self):
		return self.nome


class Idade:
	def __init__(self):
		self.idade = 37


class Evolucao(Idade):

	def __init__(self):
		self.nome = Pessoa()
		super().__init__()
		
		self.evolui = [self.nome.nome, self.idade]

	def atualiza(self):
		self.idade += 1

		self.evolui.append(self.nome.nome)
		self.evolui.append(self.idade)

		return self.evolui


if __name__ == '__main__':
	pessoa = Evolucao()

	print(pessoa.evolui)
	
	pessoa.atualiza()

	print(pessoa.evolui)

	pessoa.atualiza()

	print(pessoa.evolui)