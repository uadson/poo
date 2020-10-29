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
		self.tanque = 0


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


	# 5
	def abastecer(self, litros):
		""" Define uma quantidade de combustível para abastecimentos."""
		if litros >= 0 and litros < 40:
			self.tanque = litros
			print(f'Automóvel abastecido com {self.tanque} litros de combustível')
		else:
			print('Você precisa abastecer!')
			print('Tanque de combustível com capacidade para 40 litros.')



class Bateria():
	"""Uma tentativa simples de modelar uma bateria para um carro elétrico."""
	def __init__(self, capacidade = 70):
		"""Inicializa os atributos da bateria."""
		self.capacidade = capacidade


	def especificar_bateria(self):
		"""Exibe uma frase que descreve a capacidade da bateria."""
		print(f'Este carro tem uma bateria de capacidade de {self.capacidade}-KWh')


	def obter_autonomia(self):
		'''Exibe uma frase sobre a distância que o carro é capaz de percorrer
		com essa bateria.'''
		if self.capacidade == 70:
			autonomia = 240
		elif self.capacidade == 85:
			autonomia = 270

		message = f'''Este carro tem um autonomia de aproximadamente {autonomia}
quilômetros com a carga da bateria completa.'''


		print(message)


	def atualizar_bateria(self):
		if self.capacidade != 85:
			self.capacidade = 85

		print(f'Este carro tem uma bateria de capacidade de {self.capacidade}-KWh')

		
class EletricCar(Car):
	""" Representa aspectos específicos de veículos elétricos."""
	def __init__(self, marca, modelo, ano):
		"""Inicializa os atributos da classe-pai."""
		super().__init__(marca, modelo, ano)
		self.bateria = Bateria()


	def abastecer(self):
		"""Um carro elétrico não precisa de um tanque de combustível."""
		print('Este carro é elétrico e não precisa de combustível.')


