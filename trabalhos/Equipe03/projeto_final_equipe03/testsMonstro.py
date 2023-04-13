import pytest

from heroi import Heroi
from monstro import Monstro


@pytest.fixture
def monstro():
    piu = Monstro('comum', 'Piu-piu', 1)
    return piu


@pytest.fixture
def inimigo():
    perna = Heroi('Coelho', 'Pernalonga')
    return perna


class TestMonstro:
    def test_monstro_mover_posicao_invalida(self, monstro):
        assert monstro.mover(1, -2) == 'Posicao invalida'
        assert monstro.mover(-1, 2) == 'Posicao invalida'
        assert monstro.mover(-1, -2) == 'Posicao invalida'

    def test_monstro_mover_posicao_valida(self, monstro):
        assert monstro.mover(1, 2) == f'{monstro.nome} moveu-se para a posicao (1, 2).'

    def test_monstro_lutar(self, monstro, inimigo):
        assert monstro.lutar(inimigo, 1) == 'Turno finalizado'
        assert monstro.lutar(inimigo, 2) == 'Turno finalizado'
        assert monstro.lutar(inimigo, 3) == 'Turno finalizado'

    def test_monstro_atacar_sem_sucesso(self, monstro, inimigo):
        monstro.atacar(inimigo, 4)
        inimigo.hp == 10

    def test_monstro_atacar_sucesso(self, monstro, inimigo):
        monstro.atacar(inimigo, 6)
        inimigo.hp == 9.5

    def test_monstro_defender_sem_sucesso(self, monstro, inimigo):
        monstro.defender(inimigo, 5)
        assert monstro.hp == 10

    def test_monstro_defender_sucesso(self, monstro, inimigo):
        monstro.defender(inimigo, 8)
        assert monstro.hp == 11

    def test_monstro_curar_quandop_hp_max(self, monstro):
        monstro.curar()
        monstro.hp == 11

    def test_monstro_curar_ultrapassa_hp_max(self, monstro):
        monstro.hp = 9
        monstro.curar()
        monstro.hp == 11

    def test_monstro_curar_hp_baixo(self, monstro):
        monstro.hp = 1
        monstro.curar()
        monstro.hp == 3.75
