#from codecs import ascii_encode
from funcionario import *

class TestFuncionario(object):
    #Teste do metodo que verifica se o funcionário é maior de idade.
    def testMaiorIdade (self):
        func = FuncionarioRH(25,'nome', '121314', 0)
        assert func.maiorIdade() == True
        func.set_idade(16)
        assert func.maiorIdade() == False

    #Teste de validação da idade inserida.
    def testValidarIdade(self):
        func = Funcionario()
        assert func.set_idade(25) == True
        assert func.set_idade("25") == False
    
    #Teste de uma coleta do atributo idade
    def testPegarIdade (self):
        func = FuncionarioRH(25,'nome', '121314', 0)
        assert func.get_idade() == 25

    #Teste de validação de um nome inserido.
    def testValidarNome(self):
        func = Funcionario()
        assert func.set_nome("Joao Paulo") == True
        #assert func.set_nome('4na K0zan') == False
        assert func.set_nome(3443) == False
        assert func.set_nome(' ') == False
    
    #Teste de uma coleta do atributo nome.
    def testPegarNome (self):
        func = FuncionarioRH(25,'nome', '121314', 0)
        assert func.get_nome() == 'nome'

    #Teste de validação de uma matrícula inserida.
    def testValidarMatricula(self):
        func = Funcionario()
        assert func.set_matricula('N1420B') == True
        assert func.set_matricula('N1420B1') == False
        assert func.set_matricula(344334) == False
        assert func.set_matricula(' ') == False
    
    #Teste de uma coleta do atributo matrícula.
    def testPegarMatricula (self):
        func = FuncionarioRH(25,'nome', '121314', 0)
        assert func.get_matricula() == '121314'

    #Teste de validação do método de contratação de funcionario.
    def testPegarFuncionario (self):
        func = Funcionario()
        assert func.pegar_funcionario() == 'Funcionario Contratado'
    
    #Teste que verifica a meta de contratação do funcionário de RH.
    def testMetaContratacao(self):
        func = Recrutadora()
        assert func.set_meta_contratacao(100) == True
        assert func.set_meta_contratacao("25") == False
    
    #Teste de uma inserção e coleta do atributo meta de contratação.
    def testPegaMetaContratacao(self):
        func = Recrutadora()
        func.set_meta_contratacao(100)
        assert func.get_meta_contratacao() == 100

    #Teste que valida uma inserção incorreta do atributo qtsd contratação.
    def testQtdContratacao(self):
        func = Recrutadora()
        assert func.set_qtd_contratacao(100) == True
        assert func.set_qtd_contratacao("25") == False
    
    #Teste de uma inserção e coleta do atributo qtd contratação.
    def testPegaQtdContratacao(self):
        func = Recrutadora()
        func.set_qtd_contratacao(45)
        assert func.get_qtd_contratacao() == 45
    
    #Teste que verifica a contratação de uma novo funcionário usando o metodo recrutar funcionário.
    def testRecrutarFuncionario (self):
        func = Recrutadora()
        func.set_qtd_contratacao(45)
        assert func.recrutar_funcionario() == True
        assert func.get_qtd_contratacao() == 46
    
    #Teste que verifica o método que permite ao funcionário de RH palestrar.
    def testpalestrar (self):
        func = FuncionarioRH()
        assert  func.registrar_palestra() == True

    #Teste que verifica a utilização da senha de rede do funcionário de TI.
    def testSenhaRede(self):
        func = FuncionarioTI()
        assert func.set_senha_rede("P@ssw0rd123") == True
        assert func.set_senha_rede("P@ssw") == False
        assert func.set_senha_rede(1231342) == False

    #Teste que verifica uma inserção e consumo do atributo de senha de rede.
    def testPegarSenhaRede(self):
        func = FuncionarioTI()
        func.set_senha_rede("P@ssw0rd123")
        assert func.get_senha_rede() == "P@ssw0rd123"

    #Teste que verifica a inserção do atributo id computador.
    def testIdComputador(self):
        func = FuncionarioTI()
        assert func.set_id_computador("PC00007") == True
        assert func.set_id_computador("PC0007") == False
        assert func.set_id_computador("PCdojunior") == False
        assert func.set_id_computador(1231342) == False

    #Teste que verifica coleta do atributo id computador. 
    def testPegarIdComputador(self):
        func = FuncionarioTI()
        func.set_id_computador("PC00007")
        assert func.get_id_computador() == "PC00007"

    #Teste que verifica o método que autentica o funcionário de Ti na rede. 
    def testLogarRede(self):
        func = FuncionarioTI()
        func.set_senha_rede("P@ssw0rd123")
        assert  func.logar_rede("P@ssw0rd123") == True
    
    #Teste que verifica a inserção do atributo crp.
    def testCrp(self):
        func = Psicologa()
        assert func.set_crp("10646") == True
        assert func.set_crp("106468") == False
        assert func.set_crp("1064") == False
        assert func.set_crp(10646) == False
        assert func.set_crp(1231342) == False

    #Teste que verifica a coleta do atributo crp.
    def testPegarCrp(self):
        func = Psicologa()
        func.set_crp("10646")
        assert func.get_crp()=="10646"

    #Teste que verifica a inserção do atributo sala de atendimento do funcionário psicologo. 
    def testSalaAtendimento(self):
        func = Psicologa()
        assert func.set_sala_atendimento("Sala 2") == True
        assert func.set_sala_atendimento(2) == False
    
    #Teste que verifica a coleta do atributo sala de atendimento do funcionário psicologo.
    def testPegarSalaAtendimento(self):
        func = Psicologa()
        func.set_sala_atendimento("Sala 2")   
        assert func.get_sala_atendimento() == "Sala 2" 

    #Teste que verifica a inserção do tipo de recrutamento. 
    def testTipoRecrutamento(self):
        func = Recrutadora()
        assert func.set_tipo_recrutamento("Tech") == True
        assert func.set_tipo_recrutamento(" ") == False
        assert func.set_tipo_recrutamento(12) == False
    
    #Teste que verifica a coleta do atributo tipo de recrutamento.
    def testPegaTipoRecrutamento(self):
        func = Recrutadora()
        func.set_tipo_recrutamento("Tech")
        assert func.get_tipo_recrutamento()=="Tech"

    #Teste que verifica a inserção dos tipos de vagas disponíveis.
    def testVagasDisponiveis(self):
        func = Recrutadora()
        assert func.set_vagas_disponiveis(["QA","Developer","Psicologo"]) == True
        assert func.set_vagas_disponiveis("QA") == False

    #Teste que verifica a coleta do atributo de vagas disponíveis.
    def testPegarVagasDisponiveis(self):
        func = Recrutadora()
        func.set_vagas_disponiveis(["QA","Developer","Psicologo"])
        assert func.get_vagas_disponiveis() ==["QA","Developer","Psicologo"]

    #Teste que verifica a inserção do tipo de linguagem.
    def testLinguagem(self):
        func = Desenvolvedor()
        assert func.set_linguagem(["Java","Python","JavaScript"]) == True
        assert func.set_linguagem("Java") == False
        assert func.set_linguagem(12) == False
    
    #Teste que verifica a coleta do tipo de linguagem.
    def testPegaLinguagem(self):
        func = Desenvolvedor()
        func.set_linguagem(["Java","Python","JavaScript"])
        assert func.get_linguagem() == ["Java","Python","JavaScript"]

    #Teste que verifica a inserção do atributo senioridade.
    def testSenioridade(self):
        func = Desenvolvedor()
        assert func.set_senioridade("Pleno") == True
        assert func.set_senioridade(12) == False

    #Teste que verifica a coleta de tipo de senioridade.
    def testPegaSenioridade(self):
        func = Desenvolvedor()
        func.set_senioridade("Pleno")
        assert func.get_senioridade() == "Pleno"

    #Teste que verifica a inserção do atributo setor.
    def testSetor(self):
        func = Suporte()
        assert func.set_setor("Redes") == True
        assert func.set_setor(27951) == False

    #Teste que verifica a coleta do atributo setor.
    def testPegaSetor(self):
        func = Suporte()
        func.set_setor("Redes")
        assert func.get_setor() == "Redes"

    #Teste que verifica a inserção do atributo especialidade.
    def testEspecialidade(self):
        func = Suporte()
        assert func.set_especialidade("Seguranca") == True
        assert func.set_especialidade(27951) == False

    #Teste que verifica a coleta do atributo especialidade.
    def testPegaEspecialidade(self):
        func = Suporte()
        func.set_especialidade("Seguranca")
        assert func.get_especialidade() == "Seguranca"
    