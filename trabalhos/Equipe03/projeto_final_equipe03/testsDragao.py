import pytest

from dragao import Dragao
from guerreiro import Guerreiro


@pytest.fixture
def dragao():
    drag = Dragao('Spyro', 20)
    return drag


@pytest.fixture
def inimigo():
    perna = Guerreiro('Coelho', 'Pernalonga')
    return perna


class TestDragao:

    def test_dragao_mover_posicao_invalida(self, dragao):
        assert dragao.mover(-1, 2) == 'Posicao invalida.'
        assert dragao.mover(1, -2) == 'Posicao invalida.'
        assert dragao.mover(-1, -2) == 'Posicao invalida.'

    def test_dragao_mover_posicao_valida(self, dragao):
        assert dragao.mover(1, 2) == f'Dragao {dragao.nome} voou até a posicao (1, 2).'

    def test_dragao_cuspir_fogo(self, dragao, inimigo):
        dragao.cuspir_fogo(inimigo)
        assert inimigo.hp == 0.00
