
## Relatório Final Trabalho 2
Equipe 05: 

Isaias Abner Lima Saraiva, Alcemir Ribeiro, Thayler Rai Lima

1. Introdução:

O trabalho apresenta um classe abstrata Raiz chamada Cargos, na qual tem duas subclasses: Engenheiro e
Medico. Dentro de cada classe serão apresentados método Construtor para apresentar atributos, métodos Getters e
Setters destes atributos, método de validação de Cargo para a classe Engenheiro e a classe Medico.

Para elaboração do trabalho foi estudado conceitos de POO (Programação Orientada a Objetos) em python, TDD
(Desenvolvimento Orientado a Testes), requisitos de validação de Cargos: Engenheiro, e Medico.

2. Conceito e Abordagem de Herança durante o Trabalho Final:

A Herança é um conceito em Programação Orientada a Objeto, que determina que uma classe (filha) pode herdar atributos
e métodos de uma outra classe (pai) e, assim, evitar que haja muita repetição de código.

Este Conceito será implementado no Trabalho, onde haverá uma Classe Pai chamada Cargos, e duas classes
filhas chamadas: Class Engenheiro e Class Medico, que deve herdar métodos da classe Pai.
![img.png](img.png)

Encapsulamento é a proteção dos atributos ou métodos de uma classe, em Python
existem somente o public e o private e eles são definidos no próprio nome do atributo
ou método. Polimorfismo, em Python, é a capacidade que uma subclasse tem de ter métodos com o mesmo nome de sua
superclasse, e o programa saber qual método deve ser invocado, especificamente.

O primeiro passo no desenvolvimento do trabalho foi criar a Classe Raiz – Abstrata
chamada Cargos.
Na Class Cargos, foi criado um Método Abstract chamado validar_cargo.
Este método vai ser sobrescrito nas subclasses criadas.

```
class Cargos(ABC):
    @abstractmethod
    def validar_cargo(self):
        pass
    pass
```
Após a criação da class Cargos foi criada a classe Engenheiro, na qual herda o método
abstract validar_cargo. Foi criado dentro da class Engenheiro o Construtor com os atributos: salario , salarioBase, formacao, nivel.
```
  def __init__(self, salario: object, salarioBase: object, formacao: object, nivel: object) -> str:
        """

        :type formacao: str
        """

        self.salario = salario
        self.salarioBase = salarioBase
        self.nivel = nivel
        self.formacao = formacao
        pass
```
Foram criados os métodos de Getters e Setters dos atributos:
```
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
```
Os métodos Getters e Setters são utilizados em programação orientada a objetos em Python para adicionar lógica de validação
em torno de obter e definir um valor.
Para fazer a validação foi criado os métodos validar_Cargo, no qual segue a seguinte lógica:

Se formacao = 'Engenheiro' e nivel 'Superior Completo' Então

Retorna: Verdadeiro

```
 def validar_cargo(formacao, nivel):
        if formacao == 'Engenharia' and nivel == 'Superior Completo':
            return True

    @formacao.setter
    def formacao(self, value):
        self._formacao = value
```
A segunda Class criada foi a Medico, dentro da class foi criado os atributos: salario , salarioBase, formacao, nivel.
```
class Medico(Cargos):
    def __init__(self, formacao: object, salario: object, salarioBase: object, nivel) -> object:
        self._formacao = formacao
        self.formacao = formacao
        self.salario = salario
        self.nivel = nivel
        self.salarioBase = salarioBase
```
Foram criados os métodos de Getters e Setters dos atributos:

```
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
```
Logo após os Getters e Setters, foi sobrescrito o metodo validar_Cargos:

que segue a seguinte lógica:

Se formacao for diferente de 'Medicina' e nivel for igual a 'Superior Completo' então
Retorna Falso

```
    def validar_cargo(self, formacao, nivel):
        if formacao != 'Medicina' and nivel == 'Superior Completo':
            return False
        pass
```
Os casos de Testes foram criados para validar se o Cargo é Engenheiro ou Médico.

```
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
```

Executando os comandos:

coverage run source =. m pytest tests.py

coverage report show missing

Obteve se o seguinte resultado:
```
PS C:\Users\isaias.saraiva\PycharmProjects\pythonTrabalhoFinal> coverage run --source=. -m pytest tests.py 
===================================================================================== test session starts =====================================================================================
platform win32 -- Python 3.10.7, pytest-7.1.3, pluggy-1.0.0         
rootdir: C:\Users\isaias.saraiva\PycharmProjects\pythonTrabalhoFinal
collected 2 items

tests.py ..                                                                                                                                                                              [100%]

====================================================================================== 2 passed in 0.03s ======================================================================================
PS C:\Users\isaias.saraiva\PycharmProjects\pythonTrabalhoFinal> 

```

```
PS C:\Users\isaias.saraiva\PycharmProjects\pythonTrabalhoFinal>  coverage report --show-missing            
Name           Stmts   Miss  Cover   Missing
--------------------------------------------
main.py           71     71     0%   2-116
tests.py          28      1    96%   41
validador.py      73     18    75%   11, 30, 35, 40, 45, 50, 55, 66-67, 85, 90, 95, 100, 105, 110, 115-117
--------------------------------------------
TOTAL            172     90    48%
PS C:\Users\isaias.saraiva\PycharmProjects\pythonTrabalhoFinal> 
```

Durante o desenvolvimento do trabalho, foi estudado conceitos e desenvolvido prática sobre Programação Orientada a Objetos,
A equipe procurou desenvolver os conhecimentos adquiridos durante as aulas Contudo a equipe também buscou materiai s
referente a conceitos de TDD Desenvolvimento orientado por testes
Alguns
conceitos e práticas que foram desenvolvidos Herança, polimorfismo, POO, e a Sintaxe da linguagem Python.

Python/Conceitos básicos/Encapsulamento Wikilivros (wikibooks.org)

Polimorfismo em Python Python Progressivo

Utilizando herança no Python | Blog TreinaWeb