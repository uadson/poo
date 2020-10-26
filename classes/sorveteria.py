from restaurante import Restaurante


class StandSorveteria(Restaurante):
	def __init__(self, nome):
		self.nome = nome
		self.sabores = list()

	def mostrar_sabores(self, *sabor):
		self.sabores.append(sabor)
		print(f'Lista de sabores: {self.sabores}')

	def descrever_restaurante(self):
		print(f'Bem Vindos ao {self.nome.title()}!')
	

if __name__ == '__main__':
	sorveteria = StandSorveteria('gelatto')
	sorveteria.descrever_restaurante()
	sorveteria.abrir_restaurante()
	sorveteria.mostrar_sabores('chocolate', 'creme', 'napolitano')


