from ComponentesEletromecanicos import Atuadores


class AtuadorPneumatico(Atuadores):
    def __init__(self):
        super().__init__()

    def ligar(self):
        self.set_estado('Pistão pneumático ligado')

    def desligar(self):
        self.set_estado('Pistão pneumático desligado')

    def avancar(self):
        self.set_posicao('Fim do pistão pneumático')

    def recuar(self):
        self.set_posicao('Início do pistão pneumático')

class AtuadorHidraulico(Atuadores):
    def __init__(self):
        super().__init__('Início da prensa hidráulica', 'óleo')

    def ligar(self):
        self.set_estado('Prensa hidráulica ligada')

    def desligar(self):
        self.set_estado('Prensa hidráulica desligada')

    def avancar(self):
        self.set_posicao('Fim da prensa hidráulica')

    def recuar(self):
        self.set_posicao('Início da prensa hidráulica')
