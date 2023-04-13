from random import randint

from personagem import Personagem


class Monstro(Personagem):

    def __init__(self, tipo: str, nome: str, nivel: int):
        super().__init__(nome)
        self.tipo = tipo.lower()
        self.nivel = nivel
        self.hp_max = 10 + nivel
        self.hp = self.hp_max
        self.atk = self.nivel*0.50

    @property
    def tipo(self):
        return self._tipo

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

    @tipo.setter
    def tipo(self, tipo_monstro):
        self._tipo = tipo_monstro.lower()

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
        sucesso = randint(0, 10)
        if acao == 1:
            self.atacar(inimigo, sucesso)
            return 'Turno finalizado'
        elif acao == 2:
            self.defender(inimigo, sucesso)
            return 'Turno finalizado'
        else:
            self.curar()
            return 'Turno finalizado'

    def atacar(self, inimigo, sucesso) -> None:
        if sucesso in range(5, 11):
            inimigo.hp -= self.atk
            print(f'{self.nome} atacou. Dano causado: {self.atk} HP.')
        else:
            print(f'Ataque de {self.nome} sem efeito.')

    def defender(self, inimigo, sucesso) -> None:
        if sucesso in range(6, 11):
            print(f'{self.nome} defendeu.')
        else:
            self.hp -= inimigo.atk
            print(f'Tentativa de defesa de {self.nome} falhou. Dano tomado: {inimigo.atk} HP.')

    def curar(self) -> None:
        cura = self.hp + self.hp_max * 0.25
        if self.hp == self.hp_max:
            msg = f'{self.nome} curou-se mas sem efeito.'
        elif cura >= self.hp_max:
            self.hp = self.hp_max
            msg = f'{self.nome} curou-se e agora possui {self.hp:.2f} HP.'
        else:
            self.hp = cura
            msg = f'{self.nome} curou-se e agora possui {self.hp:.2f} HP.'
        print(msg)
