import unittest
from typing import Type

from validador import Engenheiro, Medico


class MyCalcTest(unittest.TestCase):

    formacao: Type[str]
    nivel: Type[str]

    def __init__(self, methodName: str = ...):
        """

        :type methodName: str
        """
        super().__init__(methodName)
        self.salarioBase = None
        self.formacao = None
        self.salario = None
        self.nivel = None


    def testEhEngenheiro(self):
        Eng: Engenheiro = Engenheiro(self.formacao, self.salario, self.nivel, self.formacao)
        Eng.formacao = 'Engenharia'
        Eng.salario = 10400, 00
        Eng.nivel = 'Superior Completo'
        Eng.salarioBase = 1300, 00
        self.assertTrue(Eng.validar_cargo)

    def testEhMedico(self):
        Me = Medico(self.salario, self.salarioBase, self.formacao, self.nivel)
        Me.formacao = 'Medicina'
        Me.salario = 18200
        Me.nivel = 'Superior Completo'
        Me.salarioBase = 1300
        self.assertTrue(Me.validar_cargo)

if __name__ == '__main__':
    unittest.main()
