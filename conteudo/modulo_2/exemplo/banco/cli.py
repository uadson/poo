from dominio.entidades import Cliente, ContaCorrente
from infra.repositorio_memoria import RepositorioEmMemoria

repo = RepositorioEmMemoria()

# Criar cliente
cliente = Cliente("Maria", "123")
repo.salvar_cliente(cliente)

# Criar conta corrente
conta = ContaCorrente("0001", cliente, limite=1000)
repo.salvar_conta(conta)

# Depositar e sacar
conta.depositar(500)
conta.sacar(200)

print(f"Saldo atual: R${conta.saldo:.2f}")
