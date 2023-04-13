from Computador import Computador
from Impressora import Impressora
from ServicosDeEquipamentos import ServicosDeEquipamentos
from ServicosDeSoftware import ServicosDeSoftware
from ServicosDeTi import ServicosDeTi
from SwExterno import SwExterno
from SwInterno import SwInterno


class TestServicosDeTi(object):
    def test_get_os(self):
        s = ServicosDeTi(1234)
        assert s.get_os() == 1234

    def test_set_os(self):
        s = ServicosDeTi(2222)
        s.set_os(3333)
        assert s.get_os() == 3333

    def test_os_zero(self):
        s = ServicosDeTi(self)
        assert s.set_os(0000) is None

    def test_os_letra(self):
        s = ServicosDeTi(self)
        assert s.set_os('a234') is None

    def test_os_vazio(self):
        s = ServicosDeTi(self)
        assert s.set_os('') is None

    def test_os_tamanho(self):
        s = ServicosDeTi(self)
        assert s.set_os(12345) is None


class TestServicoDeSoftware(object):
    def test_get_ssw(self):
        s = ServicosDeSoftware('V.01', 'SoftwarePlus', 1234)
        assert s.get_os() == 1234
        assert s.get_nome() == "SoftwarePlus"
        assert s.get_versao() == 'V.01'

    def test_set_ssw(self):
        s = ServicosDeSoftware('V.01', 'SoftwarePlus', 1234)
        s.set_versao('V.01.1')
        s.set_nome("OutroSoftware")
        s.set_os(1900)
        assert s.get_versao() == 'V.01.1'
        assert s.get_nome() == "OutroSoftware"
        assert s.get_os() == 1900


class TestSwInternoExterno(object):
    def test_get_set_sw_int(self):
        si = SwInterno('python', 'V.01.2', 'SoftwarePlus', 1234)
        si.set_linguagem('Cobol')
        si.set_os(4444)
        si.set_versao("V4.4.4")
        si.set_nome('NovoSoftware')
        assert si.get_linguagem() == 'Cobol'
        assert si.get_os() == 4444
        assert si.get_versao() == 'V4.4.4'
        assert si.get_nome() == "NovoSoftware"

    def test_sw_interno_implementar(self):
        si = SwInterno('python', 'V.01.2', 'SoftwarePlus', 1234)
        assert si.implementar() == 'Software Implementado'

    def test_get_set_sw_ext(self):
        se = SwExterno('EmpresaGoogle', 'V.01.2', 'SoftwarePlus', 1234)
        se.set_os(2100)
        se.set_versao("V4.4.4")
        se.set_nome('NovoSoftware')
        se.set_proprietario('Motorola')
        assert se.get_proprietario() == 'Motorola'
        assert se.get_os() == 2100
        assert se.get_versao() == 'V4.4.4'
        assert se.get_nome() == "NovoSoftware"

    def test_sw_externo_internalizar(self):
        se = SwExterno('EmpresaGoogle', 'V.01.2', 'SoftwarePlus', 1234)
        assert se.internalizar() == 'Software Internalizado'


class TestServicosDeEquipametos(object):
    def test_get_set_equipamento(self):
        s = ServicosDeEquipamentos(1023, 'HP', 1234)
        s.set_tombamento(7005)
        s.set_os(2211)
        s.set_modelo('Xiaomi')
        assert s.get_modelo() == 'Xiaomi'
        assert s.get_tombamento() == 7005
        assert s.get_os() == 2211

    def test_equipamento_substituido(self):
        e = ServicosDeEquipamentos(1023, 'HP', 1234)
        result = e.substituir("OutroEquipa", 1300)
        test = 'Novo Modelo: ' + e.get_modelo() + ', Novo Tombamento:' + str(e.get_tombamento())
        assert result == test

    class TestSeImpressora(object):
        def test_get_set_impressora(self):
            i = Impressora(True, 1234, 'Epson', 6587)
            i.set_multifuncinal(False)
            assert i.get_multifuncioal() == False

        def test_impressora_substituido(self):
            i = Impressora(True, 1075, "HP", 1700)
            result = i.substituir("XiamioImpress", 1300)
            test = 'Novo Modelo: ' + i.get_modelo() + ', Novo Tombamento:' + str(i.get_tombamento())
            assert result == test

        def test_impressora_digitalizar(self):
            i = Impressora(True, 1075, "HP", 1700)
            assert i.digitalizar() == 'Impressora digitalizou'

        def test_impressora_imprimir(self):
            i = Impressora(True, 1075, "HP", 1700)
            assert i.imprimir() == 'Impressora imprimiu'

    class TestSeComputador(object):
        def test_get_set_computador(self):
            c = Computador('Linux', 2587, 'Lenovo', 4587)
            c.set_sistema_operacional('Windows Vista')
            assert c.get_sistema_operacional() == 'Windows Vista'

        def test_computador_acessar_site(self):
            c = Computador('Linux', 2587, 'Lenovo', 4587)
            assert c.acessar_sites() == 'Computador acessou site'

        def test_computador_editar_arquivos(self):
            c = Computador('Linux', 2587, 'Lenovo', 4587)
            assert c.editar_arquivos() == 'Computador editou arquivo'

        def test_substituir_computador(self):
            c = Computador('Linux', 2587, 'Lenovo', 4587)
            result = c.substituir('MAC', 1300)
            test = 'Novo Modelo: ' + c.get_modelo() + ', Novo Tombamento:' + str(c.get_tombamento())
            assert result == test
