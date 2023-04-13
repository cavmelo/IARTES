from abc import ABC, abstractmethod


class Personagem(ABC):
    def __init__(self, nome: str):
        self.nome = nome
        self.nivel = 1

    @abstractmethod
    def lutar(self, inimigo, acao) -> None: pass

    @abstractmethod
    def mover(self, pos_x, pos_y) -> None: pass

    @abstractmethod
    def atacar(self, inimigo, sucesso) -> None: pass

    @abstractmethod
    def defender(self, inimigo, sucesso) -> None: pass
