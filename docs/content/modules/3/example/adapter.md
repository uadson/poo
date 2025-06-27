# 6. Adapter Pattern
**Catetoria**: _Estrutural_

**Problema** : Como integrar uma classe ou sistema com uma interface diferente, sem precisar alterar sua implementação?

## Quando usar?
Nosso projeto atualmente usa um repositório em memória com métodos como:
```python
salvar_conta(conta)
obter_conta(numero)
```
Imagine agora que você precise:

* Usar um arquivo JSON para persistência

* Conectar a um banco de dados SQLite

* Chamar uma API REST externa

Essas fontes podem ter interfaces diferentes, mas queremos que o resto do sistema continue funcionando sem mudanças.

**O Adapter serve para traduzir uma interface externa para o formato que o sistema espera.**

### Conceito:
O padrão Adapter converte a interface de uma classe para outra que o sistema espera. Isso permite reutilizar código que não seria compatível diretamente.

#### Aplicando Adapter no projeto
Vamos criar um repositório de contas em JSON e adaptar ele para a mesma interface usada pelo sistema.

 1. Um repositório que não segue a interface
```python
# infra/json_storage.py
import json
import os

class ContaStorageJSON:
    """Simula persistência em JSON (interface diferente)."""

    def __init__(self, caminho="contas.json"):
        self.caminho = caminho
        if not os.path.exists(caminho):
            with open(caminho, "w") as f:
                json.dump({}, f)

    def salvar(self, conta_dict):
        with open(self.caminho, "r") as f:
            dados = json.load(f)
        dados[conta_dict["numero"]] = conta_dict
        with open(self.caminho, "w") as f:
            json.dump(dados, f)

    def buscar_por_numero(self, numero):
        with open(self.caminho, "r") as f:
            dados = json.load(f)
        return dados.get(numero)
```
 2. Criamos o Adapter
```python
# infra/adapters.py
from domain.interfaces import ContaRepositoryInterface
from domain.entities import ContaCorrente, ContaPoupanca, Cliente
from infra.json_storage import ContaStorageJSON

class ContaJSONAdapter(ContaRepositoryInterface):
    """Adapter para usar ContaStorageJSON com a interface esperada."""

    def __init__(self):
        self.storage = ContaStorageJSON()

    def salvar_conta(self, conta):
        conta_dict = {
            "numero": conta.numero,
            "cpf": conta.cliente.cpf,
            "tipo": conta.__class__.__name__,
            "saldo": conta.saldo
        }
        self.storage.salvar(conta_dict)

    def obter_conta(self, numero):
        dados = self.storage.buscar_por_numero(numero)
        if not dados:
            return None
        # reconstrução simples, assume ContaCorrente por padrão
        cliente = Cliente("Desconhecido", dados["cpf"])
        return ContaCorrente(dados["numero"], cliente)
```
3. Uso no código principal
```python
# main.py
from infra.adapters import ContaJSONAdapter

repo = ContaJSONAdapter()  # troca o repositório sem mudar o resto
conta = ContaCorrente("0001", cliente)
repo.salvar_conta(conta)
```


### Benefícios do Adapter no projeto
| Vantagem                   | Explicação                                  |
| -------------------------- | ------------------------------------------- |
| **Reutilização de código** | Pode usar bibliotecas externas              |
| **Desacoplamento total**   | O resto do sistema não precisa mudar        |
| **Fácil expansão**         | Adicione adapter para SQLite, API etc.      |
| **Integração limpa**       | Traduz interfaces diferentes para uma comum |


### Finalizando
Com isso, fechamos os 6 design patterns principais aplicados ao sistema bancário:

✅ Singleton – única instância (repos)

✅ Factory – criação de contas

✅ Strategy – saque com regras diferentes

✅ Observer – notificações e logs

✅ Decorator – log e segurança sem acoplamento

✅ Adapter – adaptando persistências externas

