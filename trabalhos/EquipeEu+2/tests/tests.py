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

class TestCPF(object):
    def test_cpf_tamanho(self):
        v = val.Validador()
        assert v.validar_cpf("47763052082") == True
        assert v.validar_cpf("4776305208") == False

    def test_cpf_digito(self):
        v = val.Validador()
        assert v.validar_cpf("47763052082") == True
        assert v.validar_cpf("47763052081") == False

    def test_cpf_valido(self):
        v = val.Validador()
        assert v.validar_cpf("47763052082") == True
        assert v.validar_cpf("47763052083") == False


class TestIdade(object):
    def test_idade(self):
        v = val.Validador()
        assert v.validar_idade(25) == True


class TestNome(object):
    def test_nome(self):
        v = val.Validador()
        assert v.validar_nome('Andre Vieira dos Santos') == True


class TestConselho(object):
    def test_conselho(self):
        v = val.Validador()
        assert v.validar_conselho('12345678') == True


class TestCRA(object):
    def test_cra(self):
        v = val.Validador()
        assert v.validar_cra('123456') == True
        assert v.validar_cra('1234567') == False


class TestCREA(object):
    def test_crea(self):
        v = val.Validador()
        assert v.validar_crea('12345678') == True

