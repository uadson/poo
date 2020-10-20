from time import sleep


class User():
	def __init__(self, first_name, last_name, age, login_attempts):
		self.first_name = first_name
		self.last_name = last_name
		self.age = age
		self.login_attempts = login_attempts


	def describe_user(self):
		print(f'Nome: {self.first_name.title()}.')
		print(f'Sobrenome: {self.last_name.title()}.')
		print(f'Idade: {self.age}.')

	def greet_user(self):
		print('Seja bem vindo(a)!')

	def increment_login_attempts(self):
		self.login_attempts += 1

	def reset_login_attempts(self):
		self.login_attempts = 0


if __name__ == '__main__':
	user1 = User('uadson', 'emile', 37, 1)

	user1.greet_user()
	user1.describe_user()


	user2 = User('uadson', 'emile', 37, 0)


	print('Logando...')

	sleep(3)

	for i in range(0, 9):
		user2.increment_login_attempts()

	print(f'Quantidade de logins: {user2.login_attempts}')

	print('Resetando logins...')

	sleep(3)
	
	user2.reset_login_attempts()

	print(f'Quantidade de logins: {user2.login_attempts}')