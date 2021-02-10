from unittest import TestCase

from carro import Motor


class CarroTestCase(TestCase):
    def teste_velocidade_inicial(self):
        motor = Motor()
        # assertEqual(valor_esperado = 0, valor_obtido = ?)
        # teste = se o valor obtido é igual o valor esperado.
        self.assertEqual(0, motor.velocidade)

    def teste_acelerar(self):
        motor = Motor()
        motor.acelerar()
        # teste = se ao acelerar o valor da velocidade incrementado em 1
        self.assertEqual(1, motor.velocidade)

# comando : python -m unittest