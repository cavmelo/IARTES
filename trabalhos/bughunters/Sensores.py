from ComponentesEletromecanicos import Sensores

class SensorTemperatura(Sensores):
    def __init__(self):
        super().__init__()

    def ligar(self):
        self.set_estado('Sensor de temperatura ligado')
    def desligar(self):
        self.set_estado('Sensor de temperatura desligado')

    def medir(self):
        if(self.get_valorLido().isdigit() != True):
            print('Valor invalido')
            return 'ERRO TEMPERATURA DEVE SER NUMÉRICA'
        
        elif(int(self.get_valorLido()) > 100):
            print('Valor invalido')
            return 'ERRO TEMPERATURA MAIOR QUE RANGE'
        elif(self.get_grandeza() != 'C'):
            print('Valor invalido')
            return 'GRANDEZA DEVE SER EM CELSIUS'
        else:
            return self.get_valorLido() + self.get_grandeza()

class SensorPressao(Sensores):

    def __init__(self):
        super().__init__()

    def set_grandeza(self, grandeza):
        self.grandeza = grandeza
    def get_grandeza(self):
        return self.grandeza

    def set_estado(self,estado):
        self.estado = estado
    def get_estado(self):
        return self.estado

    def ligar(self):
        self.set_estado('Sensor de pressão ligado')
    def desligar(self):
        self.set_estado('Sensor de pressão desligado')

    def medir(self):
        if(self.get_valorLido().isdigit() != True):
            print('Valor invalido')
            return 'ERRO PRESSAO DEVE SER NUMÉRICA'
        
        elif(int(self.get_valorLido()) > 100):
            print('Valor invalido')
            return 'ERRO PRESSÃO MAIOR QUE RANGE'
        
        elif(self.get_grandeza() != 'Pa'):
            print('Valor invalido')
            return 'GRANDEZA DEVE SER EM Pa'
        else:
            return self.get_valorLido() + self.get_grandeza()