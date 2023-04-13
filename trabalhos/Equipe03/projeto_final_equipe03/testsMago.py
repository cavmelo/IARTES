import pytest

from mago import Mago
from monstro import Monstro


@pytest.fixture
def mago():
    pato = Mago('Pato', 'Patolino')
    return pato


@pytest.fixture
def inimigo():
    gag = Monstro('comum', 'Gaguinho', 1)
    return gag


class TestMago:

    def test_mago_usar_poder_invalido(self, mago):
        mago.usar_poder('Reviver')
        assert mago.poder == 'Disparar raios'

    def test_mago_usar_poder_aprendido(self, mago):
        mago.usar_poder('Encantamento')
        assert mago.poder == 'Encantamento'
        assert mago.atk == 3.30

    def test_mago_atacar_sem_sucesso(self, mago, inimigo):
        mago.atacar(inimigo, 5)
        assert inimigo.hp == 11

    def test_mago_atacar_sucesso(self, mago, inimigo):
        mago.atacar(inimigo, 9)
        assert inimigo.hp == 10
