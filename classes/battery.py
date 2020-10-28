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