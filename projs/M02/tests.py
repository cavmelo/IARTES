import validador as val

class TestTelefone(object):
    def test_ddd_invalido(self):
        v = val.Validador()
        telefone = '(9)999664444'
        assert v.validar_telefone(telefone) == False

    def test_tam_invalido(self):
        v = val.Validador()
        assert v.validar_telefone('92999984567') == False

    def test_cod_area_invalido(self):
        v = val.Validador()
        assert v.validar_telefone('(45)999984567') == False

    def test_format_cod_area_invalido(self):
        v = val.Validador()
        assert v.validar_telefone('(4)5999984567') == False

class TestData(object):
    def test_data_dia_invalido(self):
        v = val.Validador()
        assert v.validar_data("00/09/2022") == False
        assert v.validar_data("32/09/2022") == False

    def test_data_mes_invalido(self):
        v = val.Validador()
        assert v.validar_data("28/13/2022") == False

    def test_data_mes_31_dias(self):
        v = val.Validador()
        assert v.validar_data("31/04/2022") == False
        assert v.validar_data("31/03/2022") == True

    def test_data_mes_fevereiro(self):
        v = val.Validador()
        assert v.validar_data("31/02/2022") == False
        assert v.validar_data("30/02/2022") == False
        assert v.validar_data("29/02/2022") == False

    def test_data_mes_fevereiro_bissexto(self):
        v = val.Validador()
        assert v.validar_data("29/02/2022") == False
        assert v.validar_data("29/02/2020") == True

    def test_data_mes_30_dias(self):
        v = val.Validador()
        assert v.validar_data("30/03/2022") == True
        assert v.validar_data("30/04/2022") == True
