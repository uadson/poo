# Trabalhando com classes e instâncias


class Car():
	"""Uma tentativa simples de representar um carro."""
	def __init__(self, marca, modelo, ano):
		"""Inicializa os atributos que descrevem um carro."""
		self.marca = marca
		self.modelo = modelo
		self.ano = ano
		# definindo um valor default para um atributo
		self.leitura_hodometro = 0


	# 1	
	def obter_descricao_carro(self):
		"""Devolve um nome descritivo, formatado de modo elegante."""
		nome_completo = f'{str(self.ano)} {self.marca} {self.modelo}'

		return nome_completo.title()

	
	# 2	
	def ler_hodometro(self):
		"""Exibe uma frase que mostra a milhagem do carro."""
		print(f'Este carro possui {self.leitura_hodometro} quilômetros rodados.')

	
	# 3
	def atualizar_hodometro(self, quilometragem):
		"""Define o valor de leitura do hodômetro com o valor especificado.
		   Rejeita a alteração se for tentativa de definir um valor menor para 
		   o hodômetro.
		"""
		if quilometragem >= self.leitura_hodometro:
			self.leitura_hodometro = quilometragem
		else:
			print('Você não pode reduzir o valor da quilometragem!')


	# 4
	def incrementando_valores(self, km):
		""" Soma a quantidade especificada ao valor de leitura do hodômetro."""
		if km > 0:
			self.leitura_hodometro += km
		else:
			print('Você não pode reduzir o valor da quilometragem!')


if __name__ == '__main__':
	meu_carro = Car('honda', 'hrv', 2020)

	
	# 1
	print(meu_carro.obter_descricao_carro())
	# 2
	meu_carro.ler_hodometro()

	# Saída:
	#2020 Honda Hrv
	#Este carro possui 0 quilômetros rodados.
	

	# modificando o valor de um atributo diretamente
	meu_carro.leitura_hodometro = 23
	meu_carro.ler_hodometro()

	#Saída:
	#Este carro possui 23 quilômetros rodados.

	
	# modificando o valor de um atributo com um método
	# 3
	meu_carro.atualizar_hodometro(23)
	meu_carro.ler_hodometro()

	#Saída:
	#Este carro possui 23 quilômetros rodados.


	# incrementando o valor de um atributo com um método
	# 4
	meu_carro_usado = Car('subaru', 'outback', 2013)
	print(meu_carro_usado.obter_descricao_carro())


	meu_carro_usado.atualizar_hodometro(23500)
	meu_carro_usado.ler_hodometro()


	meu_carro_usado.incrementando_valores(100)
	meu_carro_usado.ler_hodometro()

	#Saída:
	#2013 Subaru Outback
	#Este carro possui 23500 quilômetros rodados.
	#Este carro possui 23600 quilômetros rodados.