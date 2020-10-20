class Restaurant():
	def __init__(self, restaurant_name, cuisine_type):
		self.restaurant_name = restaurant_name
		self.cuisine_type = cuisine_type
		self.number_served = 0 


	def describe_restaurant(self):
		print(f'Bem Vindos ao {self.restaurant_name.title()}!')
		print(f'Experimente o melhor da cozinha {self.cuisine_type.title()}!')


	def open_restaurant(self):
		print(f'ABERTO!')


	def set_number_served(self):
		print(f'Número de pessoas atendidas: {self.number_served}')


	def increment_number_served(self, served):
		self.number_served += served
		

if __name__ == '__main__':
	restaurant = Restaurant('Manggiare', 'Italiana')
	restaurant.number_served = 35
	

	print(f'Nome do Restaurante: {restaurant.restaurant_name}')
	print(f'Tipo de Cozinha: {restaurant.cuisine_type}\n')


	restaurant.describe_restaurant()
	restaurant.open_restaurant()
	restaurant.set_number_served()


	restaurant.increment_number_served(30)
	restaurant.set_number_served()