# CLI ou interface gráfica
## Script de exemplo para demonstrar a criação e interação com as entidades do sistema bancário.

### Este script executa as seguintes ações:
- 1 Cria uma instância de `RepositorioEmMemoria`.
- 2 Cria um `Cliente`.
- 3 Salva o cliente no repositório.
- 4 Cria uma `ContaCorrente` para o cliente.
- 5 Salva a conta no repositório.
- 6 Realiza operações de depósito e saque na conta.
- 7 Imprime o saldo final da conta no console.

É um exemplo prático de como as camadas de domínio e infraestrutura podem ser utilizadas
em um ponto de entrada da aplicação (neste caso, um simples script CLI).


```python
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
```
:::conteudo.modulo_2.exemplo.banco.cli