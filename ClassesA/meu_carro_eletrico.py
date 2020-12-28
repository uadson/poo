from car import *


meu_tesla = EletricCar('tesla', 'modelo s', 2016)

print(meu_tesla.obter_descricao_carro())

#Saída:
#2016 Tesla Modelo S

meu_tesla.abastecer()
meu_tesla.bateria.especificar_bateria()
meu_tesla.bateria.obter_autonomia()
meu_tesla.bateria.atualizar_bateria()

