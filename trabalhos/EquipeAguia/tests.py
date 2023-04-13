from pessoa import Funcionario, Professor, Tecnico


class TestFuncionario(object):

    def test_get_nome(self):
        f = Funcionario("joao", "13/02/1989", "(92)99305-6687", "123456", "administrativo", "03/04/2019")
        assert f.get_nome() == "joao"

    def test_get_data_nascimento(self):
        f = Funcionario("joao", "13/02/1989", "(92)99305-6687", "123456", "administrativo", "03/04/2019")
        assert f.get_data_nascimento() == "13/02/1989"

    def test_get_telefone(self):
        f = Funcionario("joao", "13/02/1989", "(92)99305-6687", "123456", "administrativo", "03/04/2019")
        assert f.get_telefone() == "(92)99305-6687"

    def test_get_matricula(self):
        f = Funcionario("joao", "13/02/1989", "(92)99305-6687", "123456", "administrativo", "03/04/2019")
        assert f.get_matricula() == "123456"

    def test_get_departamento(self):
        f = Funcionario("joao", "13/02/1989", "(92)99305-6687", "123456", "administrativo", "03/04/2019")
        assert f.get_departamento() == "administrativo"

    def test_get_data_admissao(self):
        f = Funcionario("joao", "13/02/1989", "(92)99305-6687", "123456", "administrativo", "03/04/2019")
        assert f.get_data_admissao() == "03/04/2019"

    def test_set_nome(self):
        f = Funcionario("joao", "13/02/1989", "(92)99305-6687", "123456", "administrativo", "03/04/2019")
        f.set_nome("maria")
        assert f.get_nome() == "maria"

    def test_set_data_nascimento(self):
        f = Funcionario("joao", "13/02/1989", "(92)99305-6687", "123456", "administrativo", "03/04/2019")
        f.set_data_nascimento("14/01/1991")
        assert f.get_data_nascimento() == "14/01/1991"

    def test_set_telefone(self):
        f = Funcionario("joao", "13/02/1989", "(92)99305-6687", "123456", "administrativo", "03/04/2019")
        f.set_telefone("(92)99971-7247")
        assert f.get_telefone() == "(92)99971-7247"

    def test_set_matricula(self):
        f = Funcionario("joao", "13/02/1989", "(92)99305-6687", "123456", "administrativo", "03/04/2019")
        f.set_matricula("258147")
        assert f.get_matricula() == "258147"

    def test_set_departamento(self):
        f = Funcionario("joao", "13/02/1989", "(92)99305-6687", "123456", "administrativo", "03/04/2019")
        f.set_departamento("pedagogico")
        assert f.get_departamento() == "pedagogico"

    def test_set_data_admissao(self):
        f = Funcionario("joao", "13/02/1989", "(92)99305-6687", "123456", "administrativo", "03/04/2019")
        f.set_data_admissao("05/06/2010")
        assert f.get_data_admissao() == "05/06/2010"

    def test_desativar_funcionario(self):
        f = Funcionario("joao", "13/02/1989", "(92)99305-6687", "123456", "administrativo", "03/04/2019")
        assert f.desativar_funcionario() == False

    def test_reativar_funcionario(self):
        f = Funcionario("joao", "13/02/1989", "(92)99305-6687", "123456", "administrativo", "03/04/2019")
        assert f.reativar_funcionario() == True


class TestProfessor(object):

    def test_get_nome(self):
        p = Professor("joao", "13/02/1989", "(92)99305-6687", "123456", "pedagogico", "03/04/2019",
                      "DE", "Especialista", "Ciências Naturais")
        assert p.get_nome() == "joao"

    def test_get_data_nascimento(self):
        p = Professor("joao", "13/02/1989", "(92)99305-6687", "123456", "pedagogico", "03/04/2019",
                      "DE", "Especialista", "Ciências Naturais")
        assert p.get_data_nascimento() == "13/02/1989"

    def test_get_telefone(self):
        p = Professor("joao", "13/02/1989", "(92)99305-6687", "123456", "pedagogico", "03/04/2019",
                      "DE", "Especialista", "Ciências Naturais")
        assert p.get_telefone() == "(92)99305-6687"

    def test_get_matricula(self):
        p = Professor("joao", "13/02/1989", "(92)99305-6687", "123456", "pedagogico", "03/04/2019",
                      "DE", "Especialista", "Ciências Naturais")
        assert p.get_matricula() == "123456"

    def test_get_departamento(self):
        p = Professor("joao", "13/02/1989", "(92)99305-6687", "123456", "pedagogico", "03/04/2019",
                      "DE", "Especialista", "Ciências Naturais")
        assert p.get_departamento() == "pedagogico"

    def test_get_data_admissao(self):
        p = Professor("joao", "13/02/1989", "(92)99305-6687", "123456", "pedagogico", "03/04/2019",
                      "DE", "Especialista", "Ciências Naturais")
        assert p.get_data_admissao() == "03/04/2019"

    def test_get_carga_horaria(self):
        p = Professor("joao", "13/02/1989", "(92)99305-6687", "123456", "pedagogico", "03/04/2019",
                      "DE", "Especialista", "Ciências Naturais")
        assert p.get_carga_horaria() == "DE"

    def test_get_titulo(self):
        p = Professor("joao", "13/02/1989", "(92)99305-6687", "123456", "pedagogico", "03/04/2019",
                      "DE", "Especialista", "Ciências Naturais")
        assert p.get_titulo() == "Especialista"

    def test_get_area_de_atuacao(self):
        p = Professor("joao", "13/02/1989", "(92)99305-6687", "123456", "pedagogico", "03/04/2019",
                      "DE", "Especialista", "Ciências Naturais")
        assert p.get_area_de_atuacao() == "Ciências Naturais"

    def test_set_nome(self):
        p = Professor("joao", "13/02/1989", "(92)99305-6687", "123456", "pedagogico", "03/04/2019",
                      "DE", "Especialista", "Ciências Naturais")
        p.set_nome("maria")
        assert p.get_nome() == "maria"

    def test_set_data_nascimento(self):
        p = Professor("joao", "13/02/1989", "(92)99305-6687", "123456", "pedagogico", "03/04/2019",
                      "DE", "Especialista", "Ciências Naturais")
        p.set_data_nascimento("25/08/1999")
        assert p.get_data_nascimento() == "25/08/1999"

    def test_set_telefone(self):
        p = Professor("joao", "13/02/1989", "(92)99305-6687", "123456", "pedagogico", "03/04/2019",
                      "DE", "Especialista", "Ciências Naturais")
        p.set_telefone("(92)99552-6365")
        assert p.get_telefone() == "(92)99552-6365"

    def test_set_matricula(self):
        p = Professor("joao", "13/02/1989", "(92)99305-6687", "123456", "pedagogico", "03/04/2019",
                      "DE", "Especialista", "Ciências Naturais")
        p.set_matricula("258147")
        assert p.get_matricula() == "258147"

    def test_set_departamento(self):
        p = Professor("joao", "13/02/1989", "(92)99305-6687", "123456", "pedagogico", "03/04/2019",
                      "DE", "Especialista", "Ciências Naturais")
        p.set_departamento("administrativo")
        assert p.get_departamento() == "administrativo"

    def test_set_data_admissao(self):
        p = Professor("joao", "13/02/1989", "(92)99305-6687", "123456", "pedagogico", "03/04/2019",
                      "DE", "Especialista", "Ciências Naturais")
        p.set_data_admissao("05/04/2014")
        assert p.get_data_admissao() == "05/04/2014"

    def test_set_carga_horaria(self):
        p = Professor("joao", "13/02/1989", "(92)99305-6687", "123456", "pedagogico", "03/04/2019",
                      "DE", "Especialista", "Ciências Naturais")
        p.set_carga_horaria("20h")
        assert p.get_carga_horaria() == "20h"

    def test_set_titulo(self):
        p = Professor("joao", "13/02/1989", "(92)99305-6687", "123456", "pedagogico", "03/04/2019",
                      "DE", "Especialista", "Ciências Naturais")
        p.set_titulo("Mestre")
        assert p.get_titulo() == "Mestre"

    def test_set_area_de_atuacao(self):
        p = Professor("joao", "13/02/1989", "(92)99305-6687", "123456", "pedagogico", "03/04/2019",
                      "DE", "Especialista", "Ciências Naturais")
        p.set_area_de_atuacao("Ciências Exatas")

    def test_calcular_salario_especialista(self):
        p = Professor("joao", "13/02/1989", "(92)99305-6687", "123456", "pedagogico", "03/04/2019",
                      "DE", "Especialista", "Ciências Naturais")
        carga_horaria = p.get_carga_horaria()
        titulo = p.get_titulo()
        assert p.salario(carga_horaria,titulo) == 11000.00

    def test_calcular_salario_mestre(self):
        p = Professor("joao", "13/02/1989", "(92)99305-6687", "123456", "pedagogico", "03/04/2019",
                      "DE", "Mestre", "Ciências Naturais")
        carga_horaria = p.get_carga_horaria()
        titulo = p.get_titulo()
        assert p.salario(carga_horaria,titulo) == 12000.00

    def test_calcular_salario_doutor(self):
        p = Professor("joao", "13/02/1989", "(92)99305-6687", "123456", "pedagogico", "03/04/2019",
                      "DE", "Doutor", "Ciências Naturais")
        carga_horaria = p.get_carga_horaria()
        titulo = p.get_titulo()
        assert p.salario(carga_horaria,titulo) == 16000.00

    def test_calcular_salario_graduado(self):
        p = Professor("joao", "13/02/1989", "(92)99305-6687", "123456", "pedagogico", "03/04/2019",
                      "DE", "Graduado", "Ciências Naturais")
        carga_horaria = p.get_carga_horaria()
        titulo = p.get_titulo()
        assert p.salario(carga_horaria,titulo) == 8000.00

class TestTecnico(object):
    # Como os métodos getters e setters da classe Funcionário já foram testados duas vezes (Funcionário e Professor)
    # nesta classe só testaremos os getters e setters que são exclusivos da classe Técnico
    def test_cargo(self):
        t = Tecnico("joao", "13/02/1989", "(92)99305-6687", "123456", "pedagogico", "03/04/2019",
                      "secretario", True, "especialista")
        assert t.get_cargo() == "secretario"

    def test_get_chefia(self):
        t = Tecnico("joao", "13/02/1989", "(92)99305-6687", "123456", "pedagogico", "03/04/2019",
                      "secretario", True, "especialista")
        assert t.get_chefia() == True

    def test_get_qualificacao(self):
        t = Tecnico("joao", "13/02/1989", "(92)99305-6687", "123456", "pedagogico", "03/04/2019",
                      "secretario", True, "especialista")
        assert t.get_qualificacao() == "especialista"

    def test_calcular_salario_medio(self):
        t = Tecnico("joao", "13/02/1989", "(92)99305-6687", "123456", "pedagogico", "03/04/2019",
                    "secretario", True, "medio")
        # qualificacao = t.get_qualificacao()
        # chefia = t.get_chefia()
        assert t.salario() == 3000.00

    def test_calcular_salario_graduado(self):
        t = Tecnico("joao", "13/02/1989", "(92)99305-6687", "123456", "pedagogico", "03/04/2019",
                    "secretario", True, "graduado")
        # qualificacao = t.get_qualificacao()
        # chefia = t.get_chefia()
        assert t.salario() == 4000.00

    def test_calcular_salario_especialista(self):
        t = Tecnico("joao", "13/02/1989", "(92)99305-6687", "123456", "pedagogico", "03/04/2019",
                    "secretario", True, "especialista")
        # qualificacao = t.get_qualificacao()
        # chefia = t.get_chefia()
        assert t.salario() == 5000.00

    def test_calcular_salario_mestre(self):
        t = Tecnico("joao", "13/02/1989", "(92)99305-6687", "123456", "pedagogico", "03/04/2019",
                    "secretario", True, "mestre")
        # qualificacao = t.get_qualificacao()
        # chefia = t.get_chefia()
        assert t.salario() == 6000.00

    def test_calcular_salario_doutor(self):
        t = Tecnico("joao", "13/02/1989", "(92)99305-6687", "123456", "pedagogico", "03/04/2019",
                    "secretario", True, "doutor")
        # qualificacao = t.get_qualificacao()
        # chefia = t.get_chefia()
        assert t.salario() == 8000.00