from ServicosDeEquipamentos import ServicosDeEquipamentos


class Computador(ServicosDeEquipamentos):
    def __init__(self, sistema_operacional, tombamento, modelo, os):
        super().__init__(tombamento, modelo, os)
        self.sistema_operacional = sistema_operacional

    def get_sistema_operacional(self):
        return self.sistema_operacional

    def set_sistema_operacional(self, sistema_operacional):
        self.sistema_operacional = sistema_operacional

    def acessar_sites(self):
        print('Computador acessou site')
        return 'Computador acessou site'

    def editar_arquivos(self):
        print('Computador editou arquivo')
        return 'Computador editou arquivo'

    def substituir(self, nvmodelo, nvtombamento):
        return super().substituir(nvmodelo, nvtombamento)
