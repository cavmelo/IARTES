import pytest

from heroi import Heroi
from monstro import Monstro


@pytest.fixture
def heroi():
    perna = Heroi('Coelho', 'Pernalonga')
    return perna


@pytest.fixture
def inimigo():
    piu = Monstro('comum', 'Piu-piu', 1)
    return piu


class TestHeroi:
    def test_heroi_mover_posicao_invalida(self, heroi):
        assert heroi.mover(1, -2) == 'Posicao invalida'
        assert heroi.mover(-1, 2) == 'Posicao invalida'
        assert heroi.mover(-1, -2) == 'Posicao invalida'

    def test_heroi_mover_posicao_valida(self, heroi):
        assert heroi.mover(1, 2) == f'{heroi.nome} moveu-se para a posicao (1, 2).'

    def test_heroi_lutar(self, heroi, inimigo):
        assert heroi.lutar(inimigo, 1) == 'Turno finalizado'
        assert heroi.lutar(inimigo, 2) == 'Turno finalizado'
        assert heroi.lutar(inimigo, 3) == 'Turno finalizado'

    def test_heroi_atacar_sem_sucesso(self, heroi, inimigo):
        heroi.atacar(inimigo, 5)
        inimigo.hp == 10

    def test_heroi_atacar_sucesso(self, heroi, inimigo):
        heroi.atacar(inimigo, 6)
        inimigo.hp == 9

    def test_heroi_defender_sem_sucesso(self, heroi, inimigo):
        heroi.defender(inimigo, 5)
        assert heroi.hp == 9.5

    def test_heroi_defender_sucesso(self, heroi, inimigo):
        heroi.defender(inimigo, 8)
        assert heroi.hp == 10

    def test_heroi_fugir_chefe(self, heroi, inimigo):
        inimigo.tipo = 'chefe'
        assert heroi.fugir(inimigo, 10) == f'Impossivel fugir de {inimigo.nome}.'

    def test_heroi_fugir_sem_sucesso(self, heroi, inimigo):
        inimigo.nivel = 8
        assert heroi.fugir(inimigo, 7) == f'{heroi.nome} nao pode fugir agora.'
        assert heroi.fugir(inimigo, 11) == f'{heroi.nome} nao pode fugir agora.'

    def test_heroi_fugir_sucesso(self, heroi, inimigo):
        assert heroi.fugir(inimigo, 8) == f'{heroi.nome} fugiu da luta.'
        assert heroi.fugir(inimigo, 9) == f'{heroi.nome} fugiu da luta.'
        assert heroi.fugir(inimigo, 10) == f'{heroi.nome} fugiu da luta.'

    def test_heroi_evoluir_nivel_max_atingido(self, heroi):
        heroi.hp = 5
        heroi.nivel = 10
        assert heroi.nivel == 10
        assert heroi.hp == 5
        assert heroi.atk == 1

    def test_heroi_evoluir_sucesso(self, heroi):
        heroi.hp = 2
        heroi.evoluir()
        assert heroi.nivel == 2
        assert heroi.hp == 11
        assert heroi.atk == 1.5
