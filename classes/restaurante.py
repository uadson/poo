class Restaurante():
	def __init__(self, nome, cozinha):
		self.nome = nome
		self.cozinha = cozinha
		self.pessoas_servidas = 0 


	def descrever_restaurante(self):
		print(f'Bem Vindos ao {self.nome.title()}!')
		print(f'Experimente o melhor da cozinha {self.cozinha.title()}!')


	def abrir_restaurante(self):
		print(f'ABERTO!')


	def config_num_pessoas(self):
		print(f'Número de pessoas atendidas: {self.pessoas_servidas}')


	def add_num_pessoas(self, servicos):
		self.pessoas_servidas += servicos
		

if __name__ == '__main__':
	restaurante = Restaurante('Manggiare', 'Italiana')
	restaurante.pessoas_servidas = 35
	

	print(f'Nome do Restaurante: {restaurante.nome}')
	print(f'Tipo de Cozinha: {restaurante.cozinha}\n')


	restaurante.descrever_restaurante()
	restaurante.abrir_restaurante()
	restaurante.config_num_pessoas()


	restaurante.add_num_pessoas(30)
	restaurante.config_num_pessoas()