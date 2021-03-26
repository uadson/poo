from model import Banco, Conta, Cliente

nubank = Banco(cod=260, nome='Nubank')
bb = Banco(cod=1, nome='Banco do Brasil')
itau = Banco(cod=341, nome='Itaú')
santander = Banco(cod=33, nome='Santander')

bancos = {
    'nubank': nubank,
    'bb': bb,
    'itau': itau,
    'santander': santander,
}