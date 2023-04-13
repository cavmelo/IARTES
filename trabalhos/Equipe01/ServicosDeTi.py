from abc import ABC


class ServicosDeTi(ABC):
    def __init__(self, os):
        self.os = os

    def get_os(self):
        return self.os

    def set_os(self, os):
        if not isinstance(os, int):
            print("os inválida!")
        elif os == 0:
            print("os inválida!")
        elif os > 9999:
            print("os inválida!")
        else:
            self.os = os
