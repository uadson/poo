'''
Herança:

Uma classe pode herdar os atributos e métodos de outra classe, se tornando 
assim, uma espécie de classe-filha.

O exemplo abaixo será uma herança da classe Car do módulo car.py.


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

'''

# 1. Importando o módulo no qual está inserida a class Car.
from car import Car

''' A função super() indica que a classe-pai é uma superclasse e classe filha
uma subclasse. Ela faz a chamada ao método __init__ da classe pai
e confere todos os atributos da classe-pai.'''

# 2. Criando uma nova classe que herdará os atributos e métodos da classe-pai Car
class EletricCar(Car):
	""" Representa aspectos específicos de veículos elétricos."""
	def __init__(self, marca, modelo, ano):
		"""Inicializa os atributos da classe-pai."""
		super().__init__(marca, modelo, ano)
		# definindo atributos e métodos da subclasse
		self.bateria = 70


	def descricao_bateria(self):
		"""Exibe uma frase que descreve a capacidade da bateria."""
		print(f'Este carro tem uma bateria de {self.bateria}-KWh')


if __name__ == '__main__':
	meu_tesla = EletricCar('tesla', 'modelo s', 2016)

	print(meu_tesla.obter_descricao_carro())
	meu_tesla.descricao_bateria()