from monstro import Monstro


class Orc(Monstro):

    def __init__(self, tipo: str, nome: str, funcao: str, nivel: int):
        self.funcao = funcao
        super().__init__(tipo, nome, nivel)

    @property
    def funcao(self):
        return self._funcao

    @funcao.setter
    def funcao(self, funcao_orc):
        self._funcao = funcao_orc

    def emboscar(self, inimigo) -> None:
        self.atk *= 1.50
        inimigo.hp -= self.atk
        print(f'A emboscada de {self.nome} funcionou'
              f'Resta apenas {inimigo.hp} HP para {inimigo.nome}.')
