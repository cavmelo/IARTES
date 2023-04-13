import pytest
from Atuadores import AtuadorHidraulico, AtuadorPneumatico
from ComponentesEletromecanicos import ComponentesEletromecanicos, Sensores, Atuadores
from Sensores import SensorTemperatura, SensorPressao


class Test(object):

    def test_set_funcao_sensor(self):
        teste_Sensor = Sensores()
        teste_Sensor.set_funcao('medir')
        assert teste_Sensor.get_funcao() == 'medir'

    def test_estado_inicial_construtor_sensor(self):
        sensor = Sensores()
        assert sensor.get_estado() == 'Sensor desligado'
    
    def test_construtor_sensores_com_param(self):
        sensor = Sensores(10, 15)
        assert sensor.get_valorLido() == 10 and sensor.get_valorMaximo() == 15
    
    def test_sensor_set_valor_maximo(self):
        sensor = Sensores()
        sensor.set_valorMaximo(20)
        assert sensor.get_valorMaximo() == 20
    
    def test_ligar_sensor(self):
        sensor = Sensores()
        sensor.ligar()
        assert sensor.get_estado() == 'Sensor ligado'

    def test_deligar_sensor(self):
        sensor = Sensores()
        sensor.desligar()
        assert sensor.get_estado() == 'Sensor desligado'

    #--------------------------------------- TESTES SENSOR TEMPERATURA ------------------------------------------------------------------------
        
    def test_estado_sensor_temperatura_ligado(self):
        sensor_temp = SensorTemperatura()
        sensor_temp.ligar()
        assert sensor_temp.get_estado() == 'Sensor de temperatura ligado'

    def test_estado_sensor_temperatura_desligado(self):
        sensor_temp = SensorTemperatura()
        sensor_temp.desligar()
        assert sensor_temp.get_estado() == 'Sensor de temperatura desligado'
    
    def test_grandeza_sensor_temp(self):
        sensor_temp = SensorTemperatura()
        sensor_temp.set_valorLido('32')
        sensor_temp.set_grandeza('C')
        assert sensor_temp.medir() == '32C'

    def test_valor_sensor_temperatura_maior_range(self):
        sensor_temp = SensorTemperatura()
        sensor_temp.set_valorLido('150')
        sensor_temp.set_grandeza('C')
        assert sensor_temp.medir() == 'ERRO TEMPERATURA MAIOR QUE RANGE'

    def test_valor_sensor_temperatura_com_espaco(self):
        sensor_temp = SensorTemperatura()
        sensor_temp.set_valorLido('1 0')
        sensor_temp.set_grandeza('C')
        assert sensor_temp.medir() == 'ERRO TEMPERATURA DEVE SER NUMÉRICA'
    
    def test_grandeza_sensor_temperatura_incorreta(self):
        sensor_temp = SensorTemperatura()
        sensor_temp.set_valorLido('10')
        sensor_temp.set_grandeza('K')
        assert sensor_temp.medir() == 'GRANDEZA DEVE SER EM CELSIUS'

    #--------------------------------------- TESTES SENSOR PRESSÃO ------------------------------------------------------------------------ 
    
    def test_estado_sensor_pressao_ligado(self):
        sensor_pres = SensorPressao()
        sensor_pres.ligar()
        assert sensor_pres.get_estado() == 'Sensor de pressão ligado'

    def test_estado_sensor_pressao_desligado(self):
        sensor_pres = SensorPressao()
        sensor_pres.desligar()
        assert sensor_pres.get_estado() == 'Sensor de pressão desligado'
    
    def test_grandeza_sensor_pressao(self):
        sensor_pres = SensorPressao()
        sensor_pres.set_valorLido('5')
        sensor_pres.set_grandeza('Pa')
        assert sensor_pres.medir() == '5Pa'

    def test_valor_sensor_pressao_maior_range(self):
        sensor_pressao = SensorPressao()
        sensor_pressao.set_valorLido('150')
        sensor_pressao.set_grandeza('Pa')
        assert sensor_pressao.medir() == 'ERRO PRESSÃO MAIOR QUE RANGE'
    
    def test_valor_sensor_pressao_com_espaco(self):
        sensor_pressao = SensorPressao()
        sensor_pressao.set_valorLido('1 0')
        sensor_pressao.set_grandeza('Pa')
        assert sensor_pressao.medir() == 'ERRO PRESSAO DEVE SER NUMÉRICA'
    
    def test_grandeza_sensor_pressao_incorreta(self):
        sensor_pressao = SensorPressao()
        sensor_pressao.set_valorLido('10')
        sensor_pressao.set_grandeza('Hz')
        assert sensor_pressao.medir() == 'GRANDEZA DEVE SER EM Pa'
    

#------------------------------------------------TESTS ATUADORES -----------------------------------------------------------------------
    def test_set_funcao_atuador(self):
        atuador = Atuadores()
        atuador.set_funcao('atuar')
        assert atuador.get_funcao() == 'atuar'
    
    def test_estado_inicial_construtor_atuador(self):
        atuador = Atuadores()
        assert atuador.get_estado() == 'Atuador desligado'

    def test_construtor_atuadores_com_param(self):
        atuador = Atuadores('Início do atuador', 'Ar')
        assert atuador.get_posicao() == 'Início do atuador' and atuador.get_atuador() == 'Ar'
    
    def test_set_atuador(self):
        atuador = Atuadores()
        atuador.set_atuador('Ar')
        assert atuador.get_atuador() == 'Ar'

    def test_set_posicao_avancar(self):
        atuador = Atuadores()
        atuador.avancar()
        assert atuador.get_posicao() == 'Fim do Atuador'
    
    def test_set_posicao_recuar(self):
        atuador = Atuadores()
        atuador.recuar()
        assert atuador.get_posicao() == 'Início do Atuador'

    def test_ligar_atuador(self):
        atuador = Atuadores()
        atuador.ligar()
        assert atuador.get_estado() == 'Atuador ligado'

    def test_deligar_atuador(self):
        atuador = Atuadores()
        atuador.desligar()
        assert atuador.get_estado() == 'Atuador desligado'
 
#------------------------------------------------TESTS ATUADOR PNEUMATICO -----------------------------------------------------------------------
    def test_estado_atuador_pneumatico_ligado(self):
        atuador_pneu = AtuadorPneumatico()
        atuador_pneu.ligar()
        assert atuador_pneu.get_estado() == 'Pistão pneumático ligado'

    def test_estado_atuador_pneumatico_desligado(self):
        atuador_pneu = AtuadorPneumatico()
        atuador_pneu.desligar()
        assert atuador_pneu.get_estado() == 'Pistão pneumático desligado'

    def test_posicao_atuador_pneumatico_avancar(self):
        atuador_pneu = AtuadorPneumatico()
        atuador_pneu.avancar()
        assert atuador_pneu.get_posicao() == 'Fim do pistão pneumático'
    
    def test_posicao_atuador_pneumatico_recuar(self):
        atuador_pneu = AtuadorPneumatico()
        atuador_pneu.recuar()
        assert atuador_pneu.get_posicao() == 'Início do pistão pneumático'



# ---------------------------- TESTS ATUADOR HIDRAULICO ----------------------------

    def test_estado_atuador_hidraulico_ligado(self):
        atuador_hidra = AtuadorHidraulico()
        atuador_hidra.ligar()
        assert atuador_hidra.get_estado() == 'Prensa hidráulica ligada'

    def test_estado_atuador_hidraulico_desligado(self):
        atuador_hidra = AtuadorHidraulico()
        atuador_hidra.desligar()
        assert atuador_hidra.get_estado() == 'Prensa hidráulica desligada'

    def test_posicao_atuador_hidraulico_avancar(self):
        atuador_hidra = AtuadorHidraulico()
        atuador_hidra.avancar()
        assert atuador_hidra.get_posicao() == 'Fim da prensa hidráulica'
    
    def test_posicao_atuador_hidraulico_recuar(self):
        atuador_hidra = AtuadorHidraulico()
        atuador_hidra.recuar()
        assert atuador_hidra.get_posicao() == 'Início da prensa hidráulica'

