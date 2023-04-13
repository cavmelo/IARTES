import movimento
import conta_comum
import conta_poupanca
import conta_especial
import pessoa_fisica
import pessoa_juridica


class TestGeral(object):

    #Testar a classe Movimento
    def test_regMovimento_invalido(self):
        mov = movimento.Movimento()
        assert mov.regMovimento(0,0) == 0

    def test_regMovimento_valido(self):
        mov = movimento.Movimento()
        assert mov.regMovimento(0,0)  == 0

    def test_cenMovimento_invalido(self):
        mov = movimento.Movimento()
        assert mov.cenMovimento("29020001") == False

    def test_cenMovimento_valido(self):
        mov = movimento.Movimento()
        assert mov.cenMovimento('30092002')  == True
        
#Testar a classe ContaComum
    def test_contaComum_abrirConta_Valido(self):
        conta = conta_comum.ContaComum()
        assert conta.abrirConta("2221") == True

    def test_contaComum_abrirConta_Invalido(self):
        conta = conta_comum.ContaComum()
        assert conta.abrirConta('2221') == False

    def test_contaComum_fecharConta_Valido(self):
        conta = conta_comum.ContaComum()
        assert conta.fecharConta('2221') == True

    def test_contaComum_fecharConta_Invalido(self):
        conta = conta_comum.ContaComum()
        assert conta.fecharConta('2221') == False

    def test_contaComum_saldoConta_Invalido(self):
        conta = conta_comum.ContaComum()
        assert conta.saldoConta(10) == True

    def test_contaComum_saldoConta_valido(self):
        conta = conta_comum.ContaComum()
        assert conta.saldoConta(0) == False

# Testar a classe ContaPoupanca
    def test_contaPoupanca_rendeConta_invalido(self):
        cp = conta_poupanca.ContaPoupanca()
        assert cp.rendeConta(10102002,99) == True

    def test_contaPoupanca_rendeConta_valido(self):
        cp = conta_poupanca.ContaPoupanca()
        assert cp.rendeConta(10102002,100) == False

# Testar a classe ContaEspecial
    def test_contaEspecial_jurosConta_valido(self):
        ce = conta_especial.ContaEspecial()
        assert ce.jurosConta(100)==100
        
    def test_contaEspecial_jurosConta_invalido(self):
        ce = conta_especial.ContaEspecial()
        assert ce.jurosConta(-10)== -15

# Testar a classe PessoaFisica

    def test_cpf_invalido(self):
        pf = pessoa_fisica.PessoaFisica()
        assert pf.validarInscricao('523.493.873-252') == False
        assert pf.validarInscricao('333.333.333-33') == False
        assert pf.validarInscricao('53.493.873-252') == False
        assert pf.validarInscricao('32.964.120-86') == False
        assert pf.validarInscricao('323.9642.120-86') == False
        assert pf.validarInscricao('323.964.12-86') == False
        assert pf.validarInscricao('323.964.120-8') == False
        assert pf.validarInscricao('323.964.1201-86') == False
        assert pf.validarInscricao('52.43.87-2') == False
        assert pf.validarInscricao('523493.873-25') == False
        assert pf.validarInscricao('523.493873-25') == False
        assert pf.validarInscricao('523.493.87325') == False
        assert pf.validarInscricao('52349387325') == False
        assert pf.validarInscricao('5234938325') == False
        assert pf.validarInscricao('787.309.530-33') == False
        assert pf.validarInscricao('529.982.247-22') == False


    def test_cpf_valido(self):
        pf = pessoa_fisica.PessoaFisica()
        assert pf.validarInscricao('323.964.120-86') == True
        assert pf.validarInscricao('787.309.530-49') == True


#Testar a classe PessoaJurica
    def test_cnpj_valido(self):
        cpnj = pessoa_juridica.PessoaJuridica()
        assert cpnj.validarInscricao('28298106000132') == True
        cpnj.validarInscricao('28298106000132') == True
        assert cpnj.validarInscricao('90306453000133') == True
        assert cpnj.validarInscricao('82671952000100') == True
        assert cpnj.validarInscricao('31049514000165') == True
        assert cpnj.validarInscricao('77437514000133') == True

    def test_cnpj_invalido(self):
        cpnj = pessoa_juridica.PessoaJuridica()
        assert cpnj.validarInscricao('09434053000198') == False
        assert cpnj.validarInscricao('0943000198') == False
        assert cpnj.validarInscricao('09434053000198') == False
        assert cpnj.validarInscricao('12222222222') == False
        assert cpnj.validarInscricao('0') == False
        assert cpnj.validarInscricao('123456789012345') == False
        assert cpnj.validarInscricao('90306453000103') == False
        assert cpnj.validarInscricao('90306453000130') == False
        assert cpnj.validarInscricao('55555555555555') == False
