'''
Herança:

Uma classe pode herdar os atributos e métodos de outra classe, se tornando 
assim, uma espécie de classe-filha.

O exemplo abaixo será uma herança da classe Car do módulo car.py.

Vamos importar a classe Car do módulo car.py e criar uma classe-filha
EletricCar.'''


from car import Car
from battery import Bateria


class EletricCar(Car):
	""" Representa aspectos específicos de veículos elétricos."""
	def __init__(self, marca, modelo, ano):
		"""Inicializa os atributos da classe-pai."""
		super().__init__(marca, modelo, ano)
		self.bateria = Bateria()


	def abastecer(self):
		"""Um carro elétrico não precisa de um tanque de combustível."""
		print('Este carro é elétrico e não precisa de combustível.')

	    
if __name__ == '__main__':
	meu_tesla = EletricCar('tesla', 'modelo s', 2016)

	print(meu_tesla.obter_descricao_carro())

	#Saída:
	#2016 Tesla Modelo S

	meu_tesla.abastecer()
	meu_tesla.bateria.especificar_bateria()
	meu_tesla.bateria.obter_autonomia()

''' A função super() indica que a classe-pai é uma superclasse e classe filha
uma subclasse. Ela faz a chamada ao método __init__ da classe pai
e confere todos os atributos da classe-pai.'''


'''Sobreescrevendo métodos da classe-pai
		
Pode ser que algum método da classe-pai não se enquadre no que se quer modelar
com a classe-filha. É possível sobreescrever tal método, apenas definindo um 
método na classe-filha com o mesmo nome do método da classe-pai.

Exemplo:

Há um método na classe-pai Car chamado abastecer().
Um carro elétrico não precisa de um tanque de combustível, logo o metódo 
pode ser sobreescrito.'''


'''Instâncias como atributos

Quando a quantidade de atributos e métodos começam a ficar extensos, 
uma maneira prática de otimizar a manutenção do código, é dividí-lo 
em partes menores.

Exemplo:
Atributos e métodos relacionados à bateria do nosso carra elétrico, 
podem ser transferidos para uma classe chamada Bateria e assim usar
uma instância de Bateria como atributo da classe EletricCar sem que 
está fique entulhada de código. 

Para isso importamos o módulo battery.py no qual a classe Bateria está.'''

