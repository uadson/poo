import pytest

from .model import Cliente, Conta


def test_cadastra_cliente():
	cliente = Cliente('nome', 'sobrenome','cpf')
	assert cliente.nome == 'nome'


def test_cadastra_cliente():
	cliente = Cliente('nome', 'sobrenome', 'cpf')
	assert cliente.cpf == 12345678900


def test_cadastra_conta():
	conta = Conta()
	assert conta.numero == 1234-5
