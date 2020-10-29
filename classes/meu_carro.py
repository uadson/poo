from car import Car


meu_carro = Car('honda', 'hrv', 2020)


# 1
print(meu_carro.obter_descricao_carro())
# 2
meu_carro.ler_hodometro()

# Saída:
#2020 Honda Hrv
#Este carro possui 0 quilômetros rodados.


# modificando o valor de um atributo diretamente
meu_carro.leitura_hodometro = 23
meu_carro.ler_hodometro()

#Saída:
#Este carro possui 23 quilômetros rodados.


# modificando o valor de um atributo com um método
# 3
meu_carro.atualizar_hodometro(23)
meu_carro.ler_hodometro()

#Saída:
#Este carro possui 23 quilômetros rodados.


# incrementando o valor de um atributo com um método
# 4
meu_carro_usado = Car('subaru', 'outback', 2013)
print(meu_carro_usado.obter_descricao_carro())


meu_carro_usado.atualizar_hodometro(23500)
meu_carro_usado.ler_hodometro()


meu_carro_usado.incrementando_valores(100)
meu_carro_usado.ler_hodometro()

#Saída:
#2013 Subaru Outback
#Este carro possui 23500 quilômetros rodados.
#Este carro possui 23600 quilômetros rodados.

meu_carro.abastecer(35)

#Saída:
# Automóvel abastecido com 35 litros de combustível.

