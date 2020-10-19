class Pessoa():

	def __init__(self, name, age, cpf):

		self.name = name
		self.age = age
		self.cpf = cpf

	
if __name__ == '__main__':
	p1 = Pessoa('uadson', 37, '21238493084')

	print(f'My name is {p1.name.title()}.')
	print(f'I have {p1.age} years old.')
	print(f'My cpf is {p1.cpf[0:3]}.{p1.cpf[3:6]}.{p1.cpf[5:8]}-{p1.cpf[8:10]}')