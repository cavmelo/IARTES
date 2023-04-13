from monstro import Monstro


class Dragao(Monstro):

    def __init__(self, nome: str, nivel: int):
        self.tipo = 'chefe'
        super().__init__(self.tipo, nome, nivel)

    def mover(self, pos_x, pos_y) -> str:
        if pos_x >= 0 and pos_y >= 0:
            return self.voar(pos_x, pos_y)
        else:
            return f'Posicao invalida.'

    def voar(self, pos_x, pos_y) -> str:
        return f'Dragao {self.nome} voou até a posicao ({pos_x}, {pos_y}).'

    def cuspir_fogo(self, inimigo) -> None:
        inimigo.hp = 0.00
        print(f'Dragao {self.nome} atacou com fogo. {inimigo.nome} foi eliminado.')
