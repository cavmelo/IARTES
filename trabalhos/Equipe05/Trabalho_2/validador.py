# This is a sample Python script.
from abc import ABC, abstractmethod
from typing import Any




class Cargos(ABC):
    @abstractmethod
    def validar_cargo(self):
        pass
    pass
class Engenheiro(Cargos):

    def __init__(self, salario: object, salarioBase: object, formacao: object, nivel: object) -> str:
        """

        :type formacao: str
        """

        self.salario = salario
        self.salarioBase = salarioBase
        self.nivel = nivel
        self.formacao = formacao
        pass

    # Método GET Atributo escolaridade
    @property
    def formacao(self):
        return self._formacao

    # Método SET Atributo escolaridade
    @formacao.setter
    def base(self, formacao):
        self._formacao = formacao

    # Método SET Atributo salario
    @property
    def salario(self):
        return self._salario

    # Método GET Atributo salario
    @salario.setter
    def altura(self, salario):
        self._salario = salario

    # Método SET Atributo nivel
    @property
    def nivel(self):
        return self._nivel

    # Método GET Atributo nivel
    @nivel.setter
    def arestas(self, nivel):
        self._nivel = nivel

    @salario.setter
    def salario(self, value):
        self._salario = value

    @nivel.setter
    def nivel(self, nivel):
        self._nivel = nivel

    def validar_cargo(formacao, nivel):
        if formacao == 'Engenharia' and nivel == 'Superior Completo':
            return True

    @formacao.setter
    def formacao(self, value):
        self._formacao = value


class Medico(Cargos):
    def __init__(self, formacao: object, salario: object, salarioBase: object, nivel) -> object:
        self._formacao = formacao
        self.formacao = formacao
        self.salario = salario
        self.nivel = nivel
        self.salarioBase = salarioBase

        # Método GET Atributo escolaridade
        @property
        def formacao(self):
            return self._formacao

        # Método SET Atributo escolaridade
        @formacao.setter
        def formacao(self, formacao):
            self._formacao = formacao

        # Método SET Atributo salario
        @property
        def salario(self):
            return self._salario

        # Método GET Atributo salario
        @salario.setter
        def altura(self, salario):
            self._salario = salario

        # Método SET Atributo nivel
        @property
        def nivel(self):
            return self._nivel

        # Método GET Atributo nivel
        @nivel.setter
        def arestas(self, nivel):
            self._nivel = nivel



    def validar_cargo(self, formacao, nivel):
        if formacao != 'Medicina' and nivel == 'Superior Completo':
            return False
        pass
