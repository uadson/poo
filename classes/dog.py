class Dog():
	""" Uma tentativa simples de modelar um cachorro."""

	# atributos
	def __init__(self, name, age):
		"""Inicializa os atributos name e age."""
		self.name = name
		self.age = age

	# métodos
	def sit(self):
		"""Simula um cachorro sentando em resposta a um comando."""
		print(f'{self.name.title()} is now sitting.')

	def roll_over(self):
		"""Simula um cachorro rolando em resposta a um comando."""
		print(f'{self.name.title()} rolled over!')


if __name__ == '__main__':
	my_dog = Dog('willie', 6)
	your_dog = Dog('lucy', 3)
	
	print(f"My dog's name is {my_dog.name.title()}.")
	print(f"My dog is {str(my_dog.age)} years old.")
	my_dog.sit()

	print(f"\nYour dog's name is {your_dog.name.title()}.")
	print(f'Your dog is {str(your_dog.age)} years old.')
	your_dog.sit()


