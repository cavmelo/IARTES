from heroi import Heroi


class Mago(Heroi):

    def __init__(self, raca: str, nome: str):
        super().__init__(raca, nome)
        self.poder = 'Disparar raios'
        self.hp_max = 10
        self.hp = self.hp_max

    @property
    def poder(self):
        return self._poder

    @poder.setter
    def poder(self, poder_mago):
        self._poder = poder_mago

    def usar_poder(self, novo_poder: str) -> None:
        poderes_aprendidos = ['Parar o tempo', 'Disparar raios',
                              'Bola de fogo', 'Encantamento']
        if isinstance(novo_poder, str) and novo_poder.capitalize() in poderes_aprendidos:
            print(f'{self.nome} equipou {novo_poder.capitalize()}')
            self.poder = novo_poder.capitalize()
            self.atk = self.atk * (3 + poderes_aprendidos.index(self.poder) / 10)
        else:
            print('Arma invalida.')

    def atacar(self, inimigo, sucesso) -> None:
        if sucesso in range(6, 11):
            inimigo.hp -= self.atk
            print(f'{self.nome} atacou com {self.poder}. Dano causado: {self.atk} HP.')
        else:
            print(f'Ataque de {self.nome} sem efeito.')
