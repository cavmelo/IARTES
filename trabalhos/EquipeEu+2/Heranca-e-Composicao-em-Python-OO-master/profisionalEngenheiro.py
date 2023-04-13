from pessoa import Pessoa

class Profissional(Pessoa):
  def __init__(self, nome, idade, cpf, telefone, conselho):
      super().__init__(nome, idade, cpf, telefone)
      self.__conselho = conselho
      
  def get_conselho(self):
      return self.__conselho
  
    

class Engenheiro(Profissional):

    def __init__(self, crea, nome, idade, cpf, telefone):
        super().__init__(nome, idade, cpf, telefone, crea)

    def get_conselho(self, formato):
        crea = self.get_conselho()
        return 'CREA %s´ % crea

    def set_crea(self, crea):
        self.set_conselho(crea)
