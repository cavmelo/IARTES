from abc import ABC, abstractclassmethod
from dadosPessoas import DadosPessoas


class Pessoa(ABC):

    def __init__(self, nome, idade, cpf, telefone):
        self.__nome = nome
        self.__idade = idade
        self.__cpf = cpf
        self.__telefone = telefone

    def get_conselho(self):
        pass

    def get_nome(self):
        pass

    def get_idade(self):
        pass

    def get_cpf(self):
        pass

    def get_telefone(self):
        pass

    def set_conselho(self):
        pass

    def set_nome(self, nome):
        pass

    def set_idade(self, idade):
        pass

    def set_cpf(self, cpf):
        pass

    def set_telefone(self, telefone):
        pass
