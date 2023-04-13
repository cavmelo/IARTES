from heroi import Heroi


class Guerreiro(Heroi):

    def __init__(self, raca: str, nome: str):
        super().__init__(raca, nome)
        self.arma = 'Punhos'
        self.hp_max = 10
        self.hp = self.hp_max

    @property
    def arma(self):
        return self._arma

    @arma.setter
    def arma(self, arma_guerreiro):
        self._arma = arma_guerreiro

    def equipar(self, nova_arma: str) -> None:
        armas_possiveis = ['Punhos', 'Adaga', 'Arco e flecha', 'Espada']
        if isinstance(nova_arma, str) and nova_arma.capitalize() in armas_possiveis:
            print(f'{self.nome} equipou {nova_arma.capitalize()}')
            self.arma = nova_arma.capitalize()
            self.atk = self.atk * (1 + armas_possiveis.index(self.arma) / 10)
        else:
            print('Arma invalida.')

    def atacar(self, inimigo, sucesso) -> None:
        if sucesso in range(6, 11):
            inimigo.hp -= self.atk
            print(f'{self.nome} atacou com {self.arma}. Dano causado: {self.atk} HP.')
        else:
            print(f'Ataque de {self.nome} sem efeito.')
