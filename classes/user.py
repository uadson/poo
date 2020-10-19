class User():
	def __init__(self, first_name, last_name, age):
		self.first_name = first_name
		self.last_name = last_name
		self.age = age


	def describe_user(self):
		print(f'Nome: {self.first_name.title()}.')
		print(f'Sobrenome: {self.last_name.title()}.')
		print(f'Idade: {self.age}.')

	def greet_user(self):
		print('Seja bem vindo(a)!')


if __name__ == '__main__':
	user1 = User('uadson', 'emile', 37)

	user1.greet_user()
	user1.describe_user()
