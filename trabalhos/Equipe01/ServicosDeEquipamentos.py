from ServicosDeTi import ServicosDeTi


class ServicosDeEquipamentos(ServicosDeTi):

    def __init__(self, tombamento, modelo, os):
        super().__init__(os)
        self.tombamento = tombamento
        self.modelo = modelo

    def get_tombamento(self):
        return self.tombamento

    def set_tombamento(self, tombamento):
        self.tombamento = tombamento

    def get_modelo(self):
        return self.modelo

    def set_modelo(self, modelo):
        self.modelo = modelo

    def substituir(self, modelo, tombamento):
        self.set_modelo(modelo)
        self.set_tombamento(tombamento)
        result = 'Novo Modelo: ' + self.get_modelo() + ', Novo Tombamento:' + str(self.get_tombamento())
        return result

    # def substituir(self, modelo, tombamento):
    #     self.
    #     return self.modelo + " Substituíd@"


