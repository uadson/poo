from database import *


print('Código \t\t Banco')
print('-' * 50)

for k, v in bancos.items():
    print(f'{v.cod:3}\t\t\t   {v.nome}')
