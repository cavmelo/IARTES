import pytest

from guerreiro import Guerreiro
from monstro import Monstro


@pytest.fixture
def guerreiro():
    perna = Guerreiro('Coelho', 'Pernalonga')
    return perna


@pytest.fixture
def inimigo():
    piu = Monstro('comum', 'Piu-piu', 1)
    return piu


class TestGuerreiro:

    def test_guerreiro_equipar_arma_invalida(self, guerreiro):
        guerreiro.equipar('Pistola')
        assert guerreiro.arma == 'Punhos'

    def test_guerreiro_equipar_arma_valida(self, guerreiro):
        guerreiro.equipar('adaga')
        assert guerreiro.arma == 'Adaga'
        assert guerreiro.atk == 1.10

    def test_guerreiro_atacar_sem_sucesso(self, guerreiro, inimigo):
        guerreiro.atacar(inimigo, 5)
        assert inimigo.hp == 11

    def test_guerreiro_atacar_sucesso(self, guerreiro, inimigo):
        guerreiro.atacar(inimigo, 9)
        assert inimigo.hp == 10
