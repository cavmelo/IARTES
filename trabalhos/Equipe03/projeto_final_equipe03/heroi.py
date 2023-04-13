from random import randint

from personagem import Personagem


class Heroi(Personagem):

    def __init__(self, raca: str, nome: str):
        super().__init__(nome)
        self.raca = raca
        self.hp_max = 10
        self.hp = 10
        self.atk = 1

    @property
    def raca(self):
        return self._raca

    @property
    def nome(self):
        return self._nome

    @property
    def nivel(self):
        return self._nivel

    @property
    def hp(self):
        return self._hp

    @property
    def hp_max(self):
        return self._hp_max

    @property
    def atk(self):
        return self._atk

    @raca.setter
    def raca(self, raca_heroi):
        self._raca = raca_heroi

    @nome.setter
    def nome(self, nome_personagem):
        self._nome = nome_personagem

    @nivel.setter
    def nivel(self, nivel_personagem):
        self._nivel = nivel_personagem

    @hp.setter
    def hp(self, hp_personagem):
        self._hp = hp_personagem

    @hp_max.setter
    def hp_max(self, hp_max_up):
        self._hp_max = hp_max_up

    @atk.setter
    def atk(self, atk_personagem):
        self._atk = atk_personagem

    def mover(self, pos_x, pos_y) -> str:
        if pos_x >= 0 and pos_y >= 0:
            return f'{self.nome} moveu-se para a posicao ({pos_x}, {pos_y}).'
        else:
            return f'Posicao invalida'

    def lutar(self, inimigo, acao) -> str:
        print(f'Lutando com {inimigo.nome}:\n'
              f'1. Atacar\n'
              f'2. Defender\n'
              f'3. Fugir')
        sucesso = randint(0, 10)
        if acao == 1:
            self.atacar(inimigo, sucesso)
            return 'Turno finalizado'
        elif acao == 2:
            self.defender(inimigo, sucesso)
            return 'Turno finalizado'
        elif acao == 3:
            self.fugir(inimigo, sucesso)
            return 'Turno finalizado'
        else:
            self.lutar(inimigo, sucesso)

    def atacar(self, inimigo, sucesso) -> None:
        if sucesso in range(6, 11):
            inimigo.hp -= self.atk
            print(f'{self.nome} atacou. Dano causado: {self.atk} HP.')
        else:
            print(f'Ataque de {self.nome} sem efeito.')

    def defender(self, inimigo, sucesso) -> None:
        if sucesso in range(7, 11):
            print(f'{self.nome} defendeu.')
        else:
            self.hp -= inimigo.atk
            print(f'Tentativa de defesa de {self.nome} falhou. Dano tomado: {inimigo.atk} HP.')

    def fugir(self, inimigo, sucesso) -> str:
        if inimigo.tipo == 'chefe':
            return f'Impossivel fugir de {inimigo.nome}.'
        elif sucesso in range(inimigo.nivel, 11):
            return f'{self.nome} fugiu da luta.'
        else:
            return f'{self.nome} nao pode fugir agora.'

    def evoluir(self) -> None:
        if self.nivel < 10:
            self.nivel += 1
            self.atk += 0.50
            self.hp_max += self.nivel - 1
            self.hp = self.hp_max
            print(f'{self.nome} subiu para o nivel {self.nivel}.')
        else:
            print(f'{self.nome} ja esta no nivel maximo.')
