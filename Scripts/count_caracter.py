"""Função utilizada para contar caracteres utilizando uma estrutura de 
listas para armazenar os dados.
"""


def count_caracter(word):
	# ordenando as letras
	order = sorted(word)

	# definindo primeiro caracter
	first = order[0]

	# definindo uma nova lista que irá receber os novos valores
	resultado = []
	# contador
	count = 1
	# loop for para fazer a contagem
	for char in order[1:]:
		# se o próximo caracter for igual ao anterior
		if char == first:
			# acrescenta-se a quantidade
			count += 1
		else:
			# serão adicionados à lista a letra e a quantidade
			resultado.append(first)
			resultado.append(count)
			# caso contrário a variável first recebe o valor de char
			first = char
			# o contador é redefinido para 1
			count = 1

	resultado.append(first)
	resultado.append(count)
	
	return resultado


"""Função utilizada para contar caracteres utilizando uma estrutura de 
dicionário para armazenar os dados.
#Conteúdo extraído do livro Pense Python 2 Edição
"""


def histogram(word):
	# tabela que receberá os caracteres como chave e a quantidade
	# em que esse caractere aparece na palavra como valor
	table = {}

	# para cada caracter da palavra:
	for caracter in word:
		# se o caracter não existe na tabela:
		if caracter not in table:
			# esse caracter recebe 1 como quantidade
			table[caracter] = 1
		else:
			# se o caracter existe, acrescenta uma unidade
			table[caracter] += 1		
	return table


if __name__ == '__main__':

	# lista
	print('Lista:')
	print(count_caracter('abacate'))

	# dicionário
	print('Dicionário:')
	print(histogram('abacate'))
