from ServicosDeSoftware import ServicosDeSoftware


class SwExterno(ServicosDeSoftware):
    def __init__(self, proprietario, versao, nome, os):
        super().__init__(versao, nome, os)
        self.proprietario = proprietario

    def get_proprietario(self):
        return self.proprietario

    def set_proprietario(self, proprietario):
        self.proprietario = proprietario

    def internalizar(self):
        print('Software Internalizado')
        return 'Software Internalizado'
