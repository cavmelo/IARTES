class Pessoa(object):

#Construtor
    def __init__(self, nome='', endereco='', cep='', telefone='', renda=0.0, situacao=True):
        self.nome = nome
        self.endereco = endereco
        self.cep = cep
        self.telefone = telefone
        self.renda = renda
        self.situacao = situacao

        # getter
        def get_nome(self):
            return self._nome

        def get_endereco(self):
            return self._endereco

        def get_cep(self):
            return self._cep

        def get_telefone(self):
            return self._telefone

        def get_renda(self):
            return self._renda

        def get_situacao(self):
            return self._situacao
        # setter
        def set_nome(self, nome):
            self._nome= nome

        def set_endereco(self, endereco):
            self._endereco = endereco

        def set_cep(self, cep):
            self._cep = cep

        def set_telefone(self, telefone):
            self._telefone = telefone

        def set_renda(self, renda):
            self._renda = renda

        def set_situacao(self, situacao):
            self._situacao = situacao

        def validarInscricao(self,dados):
            pass

