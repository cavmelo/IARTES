from profissao import Pessoa


class ProfissionalContador(Pessoa):

    def __init__(self, conselho, nome, idade, cpf, telefone):
        self.__crc = Pessoa().set_conselho()
        super().__init__(conselho, nome, idade, cpf, telefone)

    def get_crc(self):
        return self.__crc

    def set_crc(self, crc):
        self.__crc = crc
