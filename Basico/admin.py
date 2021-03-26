from user import User

class Permissoes():
	def __init__(self):
		self.privilegios = [
		'adicionar', 
		'excluir',
		'alterar',
		'bloquear',
		]


	def mostrar_privilegios(self):
		print('Permissões do Usuário:')
		print(self.privilegios)


class Admin(User):
	def __init__(self, first_name, last_name, age, login_attempts):
		
		super().__init__(first_name, last_name, age, login_attempts)

		self.permissoes = Permissoes()

if __name__ == '__main__':
	usuario = Admin('uadson', 'emile', 37, 0)

	usuario.describe_user()
	usuario.permissoes.mostrar_privilegios()

