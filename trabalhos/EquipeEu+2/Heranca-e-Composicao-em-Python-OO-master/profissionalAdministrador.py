from profissao import Pessoa

class ProfissionalAdministrador(Pessoa):
  def __init__(self, conselho, nome, idade, cpf, telefone):
    self.__cra = Pessoa().set_conselho()
    super().__init__(conselho, nome, idade, cpf, telefone)

  def get_cra(self):
    return self.__cra

  def set_cra(self, cra):
    self.__cra = cra