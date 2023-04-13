from ServicosDeTi import ServicosDeTi


class ServicosDeSoftware(ServicosDeTi):
    def __init__(self, versao, nome, os):
        super().__init__(os)
        self.versao = versao
        self.nome = nome

    def get_versao(self):
        return self.versao

    def set_versao(self, versao):
        self.versao = versao

    def get_nome(self):
        return self.nome

    def set_nome(self, nome):
        self.nome = nome
