from itertools import cycle

from pessoa import Pessoa


class PessoaJuridica(Pessoa):

#Construtor
    def __init__(self, cnpj='', razao_social='', nome_fantasia=''):
        self.cnpj = cnpj
        self.razao_social = razao_social
        self.nome_fantasia = nome_fantasia

        # getter
    def get_cnpj(self):
        return self._cnpj

    def get_razao_social(self):
        return self._razao_social

    def get_nome_fantasia(self):
        return self._nome_fantasia

        # setter
    def set_cnpj(self, cnpj):
        self._cnpj= cnpj

    def set_razao_social(self, razao_social):
        self._razao_social = razao_social

    def set_nome_fantasia(self, nome_fantasia):
        self._nome_fantasia = nome_fantasia

#Metodos
#Polimorfismo, utizando o metodo da classe Pessoa
    def validarInscricao(self, cnpj):
        LENGTH_CNPJ = 14
        if len(cnpj) != LENGTH_CNPJ:
            #print("teste1", cnpj)
            return False

        if cnpj in (c * LENGTH_CNPJ for c in "1234567890"):
            #print("teste2", cnpj)
            return False

        cnpj_r = cnpj[::-1]
        for i in range(2, 0, -1):
            cnpj_enum = zip(cycle(range(2, 10)), cnpj_r[i:])
            dv = sum(map(lambda x: int(x[1]) * x[0], cnpj_enum)) * 10 % 11
            if cnpj_r[i - 1:i] != str(dv % 10):
                return False

        #print("testeTrue", cnpj)
        return True
