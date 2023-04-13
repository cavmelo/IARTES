from ServicosDeSoftware import ServicosDeSoftware


class SwInterno(ServicosDeSoftware):
    def __init__(self, linguagem, versao, nome, os):
        super().__init__(versao, nome, os)
        self.linguagem = linguagem

    def get_linguagem(self):
        return self.linguagem

    def set_linguagem(self, linguagem):
        self.linguagem = linguagem

    def implementar(self):
        print('Software Implementado')
        return 'Software Implementado'
