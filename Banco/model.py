from datetime import datetime

class Banco:
     
     def __init__(self, cod, nome):

         self.cod = int(cod)
         self.nome = nome

class Conta:
    
    data_atual = datetime.strftime(datetime.now(), '%d%m%y')

    def __init__(self, banco, numero, saldo):
        
        self.banco = banco
        self.numero = numero
        self.saldo = saldo

    @ classmethod
    def registrar(cls):
        
        print(f'Transação realizada em {cls.data_atual}')    
        print(f'Saldo em conta: R$ {self.saldo}')

        return

class Cliente:

    def __init__(self, nome, cpf, conta):

        self.nome = nome
        self.cpf = cpf
        self.conta = conta

    def depositar(self, valor):
        
        print(f'{valor} depositado com sucesso!')
        
        return valor

    def sacar(self):
        pass