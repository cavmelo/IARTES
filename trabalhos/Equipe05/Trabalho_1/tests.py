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
"""
    def testFormatoQuadrado(self):
        qua: Quadrado = Quadrado(self.base, self.altura, self.area)
        qua.base = 3
        self.assertTrue(qua.validar_quadrado())

"""
if __name__ == '__main__':
    unittest.main()
"""
    def test_formato_valido(self, altura, base, area, ladoA, ladoB, ladoC):
        v = val.Triangulo(altura, base, area, ladoA, ladoB, ladoC)
        v.ladoA = 0.2
        v.ladoB = 0.4
        v.ladoC = 10.5
        v.area = 10.5
        v.base = 5.4
        v.altura = 43.8

        assert v.validar_triangulo(ladoA, ladoB, ladoC, area, base, altura) == True

    def test_cod_area_invalido(self, base, altura, area ):
        v = val.Quadrado(base, altura, area)
        v.area = 'wclkwc'
        v.area = 1
        v.base = 'dkfcnslkfnd'
        v.base = 2
        v.altura = 'wknjcodwnc'
        v.altura = 2
        assert v.validar_quadrado(base, altura, area) == False

    def test_format_cod_area_invalido(self, base, altura, area):
        v = val.Quadrado(base, altura, area)
        v.area = 10.5
        v.base = 5.4
        v.altura = 43.8
        assert v.validar_quadrado(base, altura, area) == False

"""
