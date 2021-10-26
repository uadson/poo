class Cliente:

    def __init__(self, nome, sobrenome, cpf):

        self.nome = nome
        self.sobrenome = sobrenome
        self.cpf = cpf


class Conta:

    def __init__(self, numero, cliente, saldo, limite=100):

        self.numero = numero
        self.titular = cliente
        self.saldo = saldo
        self.limite = limite

    def __str__(self):
        return f"""
        Conta  : {self.numero}
        Titular: {self.titular}
        Saldo  : {self.saldo}
        Limite : {self.limite}
        """
        
    def extrato(self):

        if self.saldo <= 0:
            saldo_total = self.limite
        else:
            saldo_total = self.saldo + self.limite
        
        print(f"""
        Conta           : {self.numero}
        Titular         : {self.titular}
        Saldo           : R$ {float(self.saldo):.2f}
        Limite          : R$ {float(self.limite):.2f}
        ----------------------------------------
        Saldo Total     : R$ {float(saldo_total):.2f}
        """)
        print()

    
    def deposita(self, valor):
        self.saldo += valor

    
    def saca(self, valor):
        if self.saldo < valor:
            return False
        else:
            self.saldo -= valor
            return True

    def transfere_para(self, destino, valor):
        retirou = self.saca(valor)

        if retirou == False:
            return False
        else:
            destino.deposita(valor)
            return True    
