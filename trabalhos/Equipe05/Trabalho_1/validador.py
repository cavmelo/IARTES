# This is a sample Python script.
from abc import ABC, abstractmethod


class FigurasGeometricas(ABC):
    @abstractmethod
    def get_calculo_area(self):
        pass


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

    def get_calculo_area(self, area):
        if self.validar_triangulo() == True:
            self.area = self.base * self.altura /2
        return self.area

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




class Quadrado(FigurasGeometricas):
    def __init__(self, area_qua: object, base_qua: object, arestas_qua: object, altura_qua: object) -> object:
        self.area_qua = area_qua
        self.base_qua = base_qua
        self.altura_qua = altura_qua
        self.arestas_qua = arestas_qua

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

    # Método para calculo de área
    def get_calculo_area(self, area_qua):
        if self.validar_quadrado() == True:
            self.area_qua = self.base_qua * self.altura_qua
        return self.area_qua

    def validar_quadrado(self, base_qua, altura_qua, area_qua):

        if base_qua and altura_qua and area_qua == float:
            return True


