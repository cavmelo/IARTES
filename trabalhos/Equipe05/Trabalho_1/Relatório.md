![img_3.png](img_3.png)
## Relatório Trabalho Final 

Equipe 05: 

Isaias Abner Lima Saraiva, Alcemir Ribeiro, Thayler Rai Lima



1. Introdução:

O trabalho apresenta um classe abstrata Raiz chamada FigurasGeométricas, na qual tem duas subclasses: Triangulo e
Quadrado. Dentro de cada classe serão apresentados método Construtor para apresentar atributos, métodos Getters e
Setters destes atributos, método de validação de triangulo, método de validação do quadrado.

Para elaboração do trabalho foi estudado conceitos de POO (Programação Orientada a Objetos) em python, TDD
(Desenvolvimento Orientado a Testes), requisitos de validação de figuras geométricas: Triangulo, e Quadrado.

2. Conceito e Abordagem de Herança durante o Trabalho Final:

A Herança é um conceito em Programação Orientada a Objeto, que determina que uma classe (filha) pode herdar atributos
e métodos de uma outra classe (pai) e, assim, evitar que haja muita repetição de código.

Este Conceito será implementado no Trabalho, onde haverá uma Classe Pai chamada FigurasGeométricas, e duas classes
filhas chamadas Triangulo e Quadrado, que deve herdar métodos da classe Pai.

![img_17.png](img_17.png)

Encapsulamento é a proteção dos atributos ou métodos de uma classe, em Python
existem somente o public e o private e eles são definidos no próprio nome do atributo
ou método. Polimorfismo, em Python, é a capacidade que uma subclasse tem de ter métodos com o mesmo nome de sua
superclasse, e o programa saber qual método deve ser invocado, especificamente.


O primeiro passo no desenvolvimento do trabalho foi criar a Classe Raiz – Abstrata
chamada FigurasGeometricas.
### Na Class FigurasGeometricas, foi criado um Método Abstract chamado get_calculo_área.
Este método vai ser sobrescrito nas subclasses criadas.

```
from abc import ABC, abstractmethod


class FigurasGeometricas(ABC):
    @abstractmethod
    def get_calculo_area(self):
        pass
```
Após a criação da class FigurasGeometricas foi criada a classe Triangulo, na qual herda o método
abstract get_calculo_área. Foi criado dentro da class Triangulo o Construtor com os atributos: a b, c (Equivalente
ao lado A, B, e C do Triangulo), base, altura, área, arestas.

```
class Triangulo(FigurasGeometricas):

    def __init__(self, a: object, b: object, c: object, base: object, altura: object, area: object, arestas: object) -> object:
        self.a = a
        self.b = b
        self.c = c
        self.base = base
        self.altura = altura
        self.area = area
        self.arestas = arestas
        pass
```


Foi criado métodos de Getters e Setters de 3 atributos Base, Altura e arestas.

```
# Método GET Atributo BASE
    @property
    def base(self):
        return self._base

    # Método SET Atributo BASE
    @base.setter
    def base(self, base):
        self._base = base

    # Método SET Atributo ALTURA
    @property
    def altura(self):
        return self._altura

    # Método GET Atributo ALTURA
    @altura.setter
    def altura(self, altura):
        self._altura = altura

    # Método SET Atributo Arestas
    @property
    def arestas(self):
        return self._arestas

    # Método GET Atributo Arestas
    @arestas.setter
    def arestas(self, arestas):
        self._arestas = arestas
```
--Os métodos Getters e Setters são utilizados em programação orientada a objetos em Python para adicionar lógica de validação
em torno de obter e definir um valor.

Para fazer a validação foi criado os métodos validar_Triangulo, esse
método foi criado para testar se os valores de cada lado a, b e c são
válidos (se formam um triangulo).
Para se obter um triangulo, o valor de cada lado deve ser menor que
a soma dos outros 2 lados.

O programa possui uma condicional afirmando:

Se o lado A for menor que (ladoA + ladoC)

Se lado B for menor que (ladoA + ladoC)

Se ladoC for menor que (ladoA + ladoB)

Então Retorna Verdadeiro


--O método validar_Escaleno tem como objetivo informar se o triangulo possui três lados diferentes.

Se o lado A for diferente do ladoB e ladoA for diferente do ladoC e ladoB for diferente do ladoC:

Então retorna Verdadeiro

```
 def validar_Triangulo(self):
        if self.a < (self.b + self.c):
            if self.b < (self.a + self.c):
                if self.c < (self.a + self.b):
                    return True

    def validar_Escaleno(self):
        if self.a != self.b and self.a != self.c and self.b != self.c:
            return True
        else:
            return False
```
--O método validar_Isosceles tem como objetivo informar se o
triangulo possui quaisquer dois lados iguais.

O programa possui uma condicional afirmando:

Se o ladoA for igual ao ladoB:

Então retorna verdadeiro

Se o ladoA for igual ao ladoC:

Então Retorna Verdadeiro

Se o ladoB for igual ao ladoC

Então Retorna Verdadeiro

Senão

Retorna Falso


--
O método validar_Equilatero tem como objetivo informar se o
triangulo possui três lados iguais.

O programa possui uma condicional afirmando:

Se o ladoA igual ao ladoB e ladoA for igual ao ladoC e ladoB for igual ao ladoC

Retorna Verdadeiro

Senão

Retorna Falso

```
    def validar_Isosceles(self):
        if self.a == self.b:
            return True
        elif self.a == self.c:
            return True
        elif self.b == self.c:
            return True
        else:
            return False

    def validar_Equilatero(self):
        if self.a == self.b and self.a == self.c and self.b == self.c:
            return True
        else:
            return False
```
--O métodoget_calculo_área tem como objetivo realizar o calculo
da área de um triangulo

Base x Altura / 2

Antes de realizar o calculo possui uma estrutura de condicional:

Se o método validar_triangulo for verdadeiro

Então Calcule a área do triangulo: base * altura / 2

Retorna Resultado de área

```
    def get_calculo_area(self, area):
        if self.validar_triangulo() == True:
            self.area = self.base * self.altura /2
        return self.area
```

### A segunda Class criada foi a Quadrado, dentro da class foi criado os atributos área_qua base_qua arestas_qua
altura_qua
```
class Quadrado(FigurasGeometricas):
    def __init__(self, area_qua: object, base_qua: object, arestas_qua: object, altura_qua: object) -> object:
        self.area_qua = area_qua
        self.base_qua = base_qua
        self.altura_qua = altura_qua
        self.arestas_qua = arestas_qua
```

--Foi criado métodos de Getters e Setters de 3 atributos Base, Altura e arestas.
```
# Método GET Atributo BASE
    @property
    def base_qua(self):
        return self._base_qua

    # Método SET Atributo BASE
    @base_qua.setter
    def base_qua(self, base_qua):
        self._base_qua = base_qua

    # Método SET Atributo ALTURA
    @property
    def altura_qua(self):
        return self._altura_qua

    # Método GET Atributo ALTURA
    @altura_qua.setter
    def altura(self, altura_qua):
        self._altura_qua = altura_qua

    @property
    def arestas_qua(self):
        return self._arestas_qua

    # Método GET Atributo Arestas
    @arestas_qua.setter
    def arestas_qua(self, arestas_qua):
        self._arestas_qua = arestas_qua
```
--Os métodos Getters e Setters são utilizados em programação
orientada a objetos em Python para adicionar lógica de validação
em torno de obter e definir um valor.

--Os método validar_quadrado foi criado para realizar a validação dos dados de entrada se são float

A lógica implementada é a seguinte:

Se a base e altura e área == float

Retorna Verdadeiro

```
    def validar_quadrado(self, base_qua, altura_qua, area_qua):

        if base_qua and altura_qua and area_qua == float:
            return True
```

--Os método get_calcular_área foi criado para realizar o calculo da área de um quadrado que equivale.

Area = base altura

A lógica implementada é a seguinte:

Se o resultado do método validar_quadrado for igual a Verdadeiro

Então realiza o calculo: área = base * altura

Retorna area


```
    def get_calculo_area(self, area_qua):
        if self.validar_quadrado() == True:
            self.area_qua = self.base_qua * self.altura_qua
        return self.area_qua
```
Os casos de Testes foram criados para validar se os dados de entrada lado A, lado B, e lado C são
equivalentes á um triângulo Essa foi a primeira validação.
Outro caso de Teste implementado foi validar se o triângulo equivale á um Equilatero que é um tipo de
triângulo que possui os três lados congruentes (mesma medida).
```
import unittest

from validador import Triangulo, Quadrado


class MyCalcTest(unittest.TestCase):


    def __init__(self, methodName: str = ...):
        super().__init__(methodName)
        self.arestas = None
        self.area = None
        self.altura = None
        self.base = None
        self.c = None
        self.b = None
        self.a = None

    def testEhTriangulo(self):
        tri = Triangulo(self.a, self.b, self.c, self.base, self.altura, self.area, self.arestas)
        tri.a = 3
        tri.b = 4
        tri.c = 5
        self.assertTrue(tri.validar_Triangulo())

    def testEhEquilatero(self):
        tri = Triangulo(self.a, self.b, self.c, self.base, self.altura, self.area, self.arestas)
        tri.a = 4
        tri.b = 4
        tri.c = 4
        self.assertTrue(tri.validar_Equilatero())
```
Além disso foi implementado também validação se o triângulo é do tip o Isosceles que
apresenta três lados, sendo dois deles congruentes (mesma medida).

Por ultimo foi implementado se o triângulo é classificado como Escaleno onde a medida de
seus lados são diferentes entre si.
```
    def testEhIsosceles(self):
        tri = Triangulo(self.a, self.b, self.c, self.base, self.altura, self.area, self.arestas)

        tri.a = 3
        tri.b = 3
        tri.c = 5
        self.assertTrue(tri.validar_Isosceles())

        tri.a = 3
        tri.b = 5
        tri.c = 3
        self.assertTrue(tri.validar_Isosceles())

        tri.a = 5
        tri.b = 3
        tri.c = 3
        self.assertTrue(tri.validar_Isosceles())

    def testEhEscaleno(self):
        tri = Triangulo(self.a, self.b, self.c, self.base, self.altura, self.area, self.arestas)
        tri.a = 3
        tri.b = 4
        tri.c = 5
        self.assertTrue(tri.validar_Escaleno())
```
Executando os comandos:

coverage run source =. m pytest tests.py

coverage report show missing

Obteve se o seguinte resultado:
```
PS C:\Users\isaias.saraiva\PycharmProjects\pythonExercicio> coverage run --source=. -m pytest tests.py
===================================================================================== test session starts ===================================================================================== 
platform win32 -- Python 3.10.7, pytest-7.1.3, pluggy-1.0.0
rootdir: C:\Users\isaias.saraiva\PycharmProjects\pythonExercicio
collected 4 items                                                                                                                                                                               

tests.py ....                                                                                                                                                                            [100%] 

====================================================================================== 4 passed in 0.05s ====================================================================================== 
PS C:\Users\isaias.saraiva\PycharmProjects\pythonExercicio>  coverage report --show-missing
Name           Stmts   Miss  Cover   Missing
--------------------------------------------
main.py           81     81     0%   2-132
tests.py          48      1    98%   65
validador.py      89     25    72%   8, 26, 36, 46, 54-56, 68, 78, 84, 91-94, 99, 104, 109, 114, 118, 123, 127-129, 133-134
--------------------------------------------
TOTAL            218    107    51%
PS C:\Users\isaias.saraiva\PycharmProjects\pythonExercicio> 


```
### Condiderações Finais e Referências

Durante o desenvolvimento do trabalho, foi estudado conceitos e desenvolvido prática sobre Programação Orientada a Objetos,
A equipe procurou desenvolver os conhecimentos adquiridos durante as aulas Contudo a equipe também buscou materiai s
referente a conceitos de TDD Desenvolvimento orientado por testes
Alguns
conceitos e práticas que foram desenvolvidos Herança, polimorfismo, POO, e a Sintaxe da linguagem Python.

Python/Conceitos básicos/Encapsulamento Wikilivros (wikibooks.org)

Polimorfismo em Python Python Progressivo

Utilizando herança no Python | Blog TreinaWeb
