class DadosPessoas():

    def __init__(self, conselho, nome, idade, cpf, telefone):
        self.__telefone = telefone

    def get_conselho(self):
        return self.__conselho

    def get_nome(self):
        return self.__nome

    def get_idade(self):
        return self.__idade

    def get_cpf(self):
        return self.__cpf

    def get_telefone(self):
        return self.__telefone

    def set_conselho(self):
        return self.__conselho

    def set_nome(self, nome):
        self.__nome = nome

    def set_idade(self, idade):
        self.__idade = idade

    def set_cpf(self, cpf):
        self.__cpf = cpf

    def set_telefone(self, telefone):
        self.__telefone = telefone
