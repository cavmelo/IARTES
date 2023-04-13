import pytest

from orc import Orc
from guerreiro import Guerreiro


@pytest.fixture
def orc():
    orc = Orc('comum', 'Baldur', 'comandante', 5)
    return orc


@pytest.fixture
def inimigo():
    perna = Guerreiro('Coelho', 'Pernalonga')
    return perna


class TestOrc:

    def test_orc_emboscar(self, orc, inimigo):
        orc.emboscar(inimigo)
        assert inimigo.hp == 6.25
