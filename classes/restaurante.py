class Restaurant():
	def __init__(self, restaurant_name, cuisine_type):
		self.restaurant_name = restaurant_name
		self.cuisine_type = cuisine_type

	def describe_restaurant(self):
		print(f'Bem Vindos ao {self.restaurant_name.title()}!')
		print(f'Experimente o melhor da cozinha {self.cuisine_type.title()}!')

	def open_restaurant(self):
		print(f'ABERTO!')


if __name__ == '__main__':
	restaurant = Restaurant('Manggiare', 'Italiana')

	steak_food = Restaurant('Kernel', 'Grelhados')

	tequilas_bar = Restaurant('hermanos', 'mexicana')

	greco_romain = Restaurant('greco', 'mediterrânea')

	print(f'Nome do Restaurante: {restaurant.restaurant_name}')
	print(f'Tipo de Cozinha: {restaurant.cuisine_type}\n')

	restaurant.describe_restaurant()
	restaurant.open_restaurant()

	print()

	steak_food.describe_restaurant()
	tequilas_bar.describe_restaurant()
	greco_romain.describe_restaurant()

