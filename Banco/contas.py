from model import Cliente, Conta


cliente1 = Cliente('Uadson', 'Feitosa', '111.222.333-44')

cliente2 = Cliente('Emile', 'Castro', '555.666.777-88')

conta1 = Conta('1234-5', cliente1.nome, 1000)

conta2 = Conta('6789-0', cliente2.nome, 2000)

print(conta1.titular)
print()

print(conta2.titular)
print()
