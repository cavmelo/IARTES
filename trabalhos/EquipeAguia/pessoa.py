from abc import ABC, abstractmethod


class Pessoa(ABC):
    _nome: str
    _data_nascimento: str
    _telefone: str
    def __init__(self, nome, data_nascimento, telefone):
        self._nome = nome
        self._data_nascimento = data_nascimento
        self._telefone = telefone

    @abstractmethod
    def set_nome(self):
        pass

    @abstractmethod
    def set_data_nascimento(self):
        pass

    @abstractmethod
    def set_telefone(self):
        pass

    @abstractmethod
    def get_nome(self):
        pass

    @abstractmethod
    def get_data_nascimento(self):
        pass

    @abstractmethod
    def get_telefone(self):
        pass


class Funcionario(Pessoa):

    def __init__(self, nome, data_nascimento, telefone,
                 matricula, departamento, data_admissao):
        super().__init__(nome, data_nascimento, telefone)
        self._matricula = matricula
        #departamento são dois:
        #   administrativo (todos que não são professores);
        #   pedagogico (todos os professores)
        self._departamento = departamento
        self._data_admissao = data_admissao
        #esta variável "ativo" é uma variável implícita, o funcionário ao ser cadastrado no sistema nasce com o __ativo = True
        self._ativo = True

    def set_nome(self, nome):
        self._nome = nome

    def set_data_nascimento(self, data_nascimento):
        self._data_nascimento = data_nascimento

    def set_telefone(self, telefone):
        self._telefone = telefone

    def set_matricula(self, matricula):
        self._matricula = matricula

    def set_departamento(self, departamento):
        self._departamento = departamento

    def set_data_admissao(self, data_admissao):
        self._data_admissao = data_admissao

    def get_nome(self):
        return self._nome

    def get_data_nascimento(self):
        return self._data_nascimento

    def get_telefone(self):
        return self._telefone

    def get_matricula(self):
        return self._matricula

    def get_departamento(self):
        return self._departamento

    def get_data_admissao(self):
        return self._data_admissao

    def desativar_funcionario(self):
        self._ativo = False
        print("A pessoa foi desativada com sucesso")
        return self._ativo

    def reativar_funcionario(self):
        self._ativo = True
        print("A pessoa foi reativada com sucesso")
        return self._ativo

    def salario(self):
        pass

class Professor(Funcionario):
    def __init__(self, nome, data_nascimento, telefone, matricula, departamento, data_admissao,
                 carga_horaria, titulo, area_de_atuacao):
        super().__init__(nome, data_nascimento, telefone, matricula, departamento, data_admissao)
        #atributo carga horária vai ser preenchido por:
        #   horas semanais;
        #   DE (dedicação exclusiva)
        self._carga_horaria = carga_horaria
        self._titulo = titulo
        self._area_de_atuacao = area_de_atuacao

    def set_carga_horaria(self, carga_horaria):
        self._carga_horaria = carga_horaria

    def set_titulo(self, titulo):
        self._titulo = titulo

    def set_area_de_atuacao(self, area_de_atuacao):
        self._area_de_atuacao = area_de_atuacao

    def get_carga_horaria(self):
        return self._carga_horaria

    def get_titulo(self):
        return self._titulo

    def get_area_de_atuacao(self):
        return self._area_de_atuacao

    # def salario(self,carga_horaria):
    #     # 40,00 a hora-aula
    #     hora_aula = 40.00
    #     if carga_horaria == "DE" or "D.E." or "de" or "d.e." or "D.e." or "d.E." or "De" or "dE":
    #         return hora_aula * 200
    #     else:
    #         return int(carga_horaria[:2]) * hora_aula * 4

    def salario(self, carga_horaria, titulo):
        if titulo == "Especialista":
            # 55,00 a hora-aula
            hora_aula = 55.00
            if carga_horaria == "DE" or "D.E." or "de" or "d.e." or "D.e." or "d.E." or "De" or "dE":
                return hora_aula * 200
            else:
                return int(carga_horaria[:2]) * hora_aula * 4
        elif titulo == "Mestre":
            # 60,00 a hora-aula
            hora_aula = 60.00
            if carga_horaria == "DE" or "D.E." or "de" or "d.e." or "D.e." or "d.E." or "De" or "dE":
                return hora_aula * 200
            else:
                return int(carga_horaria[0:2]) * hora_aula * 4
        elif titulo == "Doutor":
            # 80,00 a hora-aula
            salario = 0
            hora_aula = 80.00
            if carga_horaria == "DE" or "D.E." or "de" or "d.e." or "D.e." or "d.E." or "De" or "dE":
                salario =  hora_aula * 200
            else:
                salario = int(carga_horaria) * hora_aula * 4
            return salario
        else:
            # 40,00 a hora-aula
            hora_aula = 40.00
            if carga_horaria == "DE" or "D.E." or "de" or "d.e." or "D.e." or "d.E." or "De" or "dE":
                return hora_aula * 200
            else:
                return int(carga_horaria[:2]) * hora_aula * 4

class Tecnico(Funcionario):
    def __init__(self, nome, data_nascimento, telefone, matricula, departamento, data_admissao,
                 cargo, chefia, qualificacao):
        super().__init__(nome, data_nascimento, telefone, matricula, departamento, data_admissao)
        # Cargo ocupado pelo técnico
        self.cargo = cargo
        # Se o técnico tem função de chefia
        self.chefia = chefia
        # Qualificação de ensino do técnico para saber as possibilidades
        # de inclusão em outras áreas da escola (ensino médio, técnico, graduação...)
        self.qualificacao = qualificacao

    def set_cargo(self, cargo):
        self.cargo = cargo

    def set_chefia(self, chefia):
        self.chefia = chefia

    def set_qualificacao(self, qualificacao):
        self.qualificacao = qualificacao

    def get_cargo(self):
        return self.cargo

    def get_chefia(self):
        return self.chefia

    def get_qualificacao(self):
        return self.qualificacao

    def salario(self):
        if self.qualificacao == "medio":
            # 15,00 a hora-trabalhada
            hora_trabalhada = 15.00
            if self.chefia:
                return hora_trabalhada * 200
            else:
                return hora_trabalhada * 160
        elif self.qualificacao == "graduado":
            # 20,00 a hora-trabalhada
            hora_trabalhada = 20.00
            if self.chefia:
                return hora_trabalhada * 200
            else:
                return hora_trabalhada * 160
        elif self.qualificacao == "especialista":
            # 25,00 a hora-trabalhada
            hora_trabalhada = 25.00
            if self.chefia:
                return hora_trabalhada * 200
            else:
                return hora_trabalhada * 160
        elif self.qualificacao == "mestre":
            # 30,00 a hora-trabalhada
            hora_trabalhada = 30.00
            if self.chefia:
                return hora_trabalhada * 200
            else:
                return hora_trabalhada * 160
        elif self.qualificacao == "doutor":
            # 40,00 a hora-trabalhada
            hora_trabalhada = 40.00
            if self.chefia:
                return hora_trabalhada * 200
            else:
                return hora_trabalhada * 160