class Pessoa:
    # atributos de instância
    def __init__(self, nome, idade, comendo=False, falando=False):
        self.nome = nome
        self.idade = idade 
        self.comendo = comendo 
        self.falando = falando
    
    # método 
    def comer(self, alimento):
        if self.comendo:
            print(f'{self.nome} já está comendo.')
            return

        print(f'{self.nome} está comendo {alimento}.')
        self.comendo = True

    def parar_comer(self):
        if not self.comendo:
            print(f'{self.nome} não está comendo.')
            return
        
        print(f'{self.nome} parou de comer.')
        self.comendo = False

if __name__ == '__main__':
    # instâncias da classe Pessoa
    p1 = Pessoa('Luiz', 29)
    p1.comer('Maçã')
    p1.parar_comer()
    p1.comer('Maçã')