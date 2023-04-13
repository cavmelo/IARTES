import re

from pessoa import Pessoa


class PessoaFisica(Pessoa):

#Construtor
    def __init__(self, cpf='', rg='', dependentes=False):
        self.cpf = cpf
        self.rg = rg
        self.dependentes = dependentes

        # getter
        def get_cpf(self):
            return self._cpf

        def get_rg(self):
            return self._rg

        def get_dependentes(self):
            return self._dependentes

        # setter
        def set_cpf(self, cpf):
            self._cpf= cpf

        def set_rg(self, rg):
            self._rg = rg

        def set_dependentes(self, dependentes):
            self._dependentes = dependentes

    #Metodos
    #Polimorfismo, utizando o metodo da classe Pessoa
    def validarInscricao(self,cpf):
        # Verificar a formatação do CPF
        if not (re.match(r'\d{3}\.\d{3}\.\d{3}-\d{2}', cpf)):
            return False
        else:
            # Obter os numeros, sem digitos
            cpf_numeros = [int(digito) for digito in cpf if digito.isdigit()]
            # Verificar se o CPF tem 11 digitos ou se todos os numeros sao iguais
            if (len(cpf_numeros) != 11 or len(set(cpf_numeros)) == 1):
                return False

            # Validar o primeiro dígito verificador:
            soma = sum(a * b for a, b in zip(cpf_numeros[0:9], range(10, 1, -1)))
            digito_esperado = (soma * 10 % 11) % 10
            if cpf_numeros[9] != digito_esperado:
                return False

            # Validar o segundo dígito verificador:
            soma = sum(a * b for a, b in zip(cpf_numeros[0:10], range(11, 1, -1)))
            digito_esperado = (soma * 10 % 11) % 10
            if cpf_numeros[10] != digito_esperado:
                return False

        return True