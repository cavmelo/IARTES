from ServicosDeEquipamentos import ServicosDeEquipamentos


class Impressora(ServicosDeEquipamentos):
    def __init__(self, multifuncional, tombamento, modelo, os):
        super().__init__(tombamento, modelo, os)
        self.multifuncional = multifuncional

    def get_multifuncioal(self):
        return self.multifuncional

    def set_multifuncinal(self, multifuncional):
        self.multifuncional = multifuncional

    def imprimir(self):
        print('Impressora imprimiu')
        return 'Impressora imprimiu'

    def digitalizar(self):
        print('Impressora digitaizou')
        return 'Impressora digitalizou'

    def substituir(self, nvmodelo, nvtombamento):
        return super().substituir(nvmodelo, nvtombamento)
