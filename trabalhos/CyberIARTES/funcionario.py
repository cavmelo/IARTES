from abc import ABC, abstractmethod
#from asyncio.windows_events import NULL

class Funcionario(object):
    
    def __init__(self, idade:int = 0, nome:str = None, matricula:str = None):
        self._idade = idade
        self._nome = nome
        self._matricula = matricula   

    def set_idade(self, idade:int):
        
        if not isinstance(idade, int):
            return False
        else: 
            self._idade = idade
            return True
        
    def get_idade(self):
        return self._idade

    def set_nome(self, nome:str):
        if not isinstance(nome, str) or nome==' ':
                return False
        else: 
            self._nome = nome
            return True

    def get_nome(self):
        return self._nome

    # A Matricula tem obrigatoriamente 6 caracteres 
    def set_matricula(self, matricula:str):
        if not isinstance(matricula, str) or matricula==' ':
            return False
        elif matricula.__len__() != 6:
            return False
        else: 
            self._matricula = matricula
            return True   

    def get_matricula(self):
        return self._matricula

    @abstractmethod
    def pegar_funcionario(self):
        return "Funcionario Contratado"

    def maiorIdade(self):
        if self._idade >= 18:
            return True
        else:
            return False

    @abstractmethod
    def pagamento_funcionario(self):
        pass

class FuncionarioRH(Funcionario):
    def __init__(self, nome:str = None, matricula:str = None, idade:int = 0, qtde_palestras:int = 0):
        super().__init__(nome, matricula, idade)
        self._qtde_palestras = qtde_palestras

    def set_qtde_palestras(self, qtde_palestras:int):
        
        if not isinstance(qtde_palestras, int):
            return False
        else: 
            self._qtde_palestras = qtde_palestras
            return True
        
    def get_qtde_palestras(self):
        return self._qtde_palestras
        

    def registrar_palestra(self):
        self.set_qtde_palestras(self.get_qtde_palestras() + 1)
        return True
    

class FuncionarioTI(Funcionario):
    def __init__(self, nome:str = None, matricula:str = None, idade:int = 0, id_computador:str = None, senha_rede:str = None):
        super().__init__(nome, matricula, idade)
        self._senha_rede = senha_rede
        self._id_computador = id_computador

    # A senha deve ter no minimo 6 caracteres
    def set_senha_rede(self, senha_rede:str):
        
        if not isinstance(senha_rede, str):
            return False
        elif senha_rede.__len__() < 6:
            return False
        else: 
            self._senha_rede = senha_rede
            return True
        
    def get_senha_rede(self):
        return self._senha_rede

    #Id do computador sao de 7 digitos
    def set_id_computador(self, id_computador:str):
        if not isinstance(id_computador, str):
            return False
        elif id_computador.__len__()!=7:
            return False
        else: 
            self._id_computador = id_computador
            return True
        

    def get_id_computador(self):
        return self._id_computador

    #@abstractmethod
    def logar_rede(self, senha):
        if self.get_senha_rede() == senha:
            return True
        else:
            return False


class Psicologa(FuncionarioRH):
    def __init__(self, nome:str = None, matricula:str = None, idade:int = 0 , crp:str = None, sala_atendimento:str = None, qtde_avaliacao:int = 0):
        super().__init__(nome, matricula, idade)
        self._crp = crp
        self._sala_atendimento = sala_atendimento
        self._qtde_avaliacao = qtde_avaliacao

    def set_crp(self, crp:str):
        if not isinstance(crp, str):
            return False
        elif crp.__len__() != 5:
            return False
        else: 
            self._crp = crp
            return True
        

    def get_crp(self):
        return self._crp

    def set_sala_atendimento(self, sala_atendimento):
        if not isinstance(sala_atendimento, str):
            return False
        else: 
            self._sala_atendimento = sala_atendimento
            return True

    def get_sala_atendimento(self):
        return self._sala_atendimento

    def set_qtde_avaliacao(self, qtde_avaliacao):
        if not isinstance(qtde_avaliacao, int):
            return False
        else: 
            self._qtde_avaliacao = qtde_avaliacao
            return True

    def get_qtde_avaliacao(self):
        return self._qtde_avaliacao

    def pagamento_funcionario(self):
        salario = 0
        salario_base = 2000
        if(self.get_sala_atendimento()):
            salario = salario_base * 2
        else:
            salario = salario_base
        return salario

    def avaliar_candidato(self):
        self.set_qtde_avaliacao (self.get_qtde_avaliacao() + 1)
        return True


class Recrutadora(FuncionarioRH):
    def __init__(self, nome:str = None, matricula:str = None, idade:int = 0, meta_contratacao:int = 0 , qtd_contratacao:int= 0 , tipo_recrutamento:str = None, vagas_disponiveis:list = None):
        super().__init__(nome, matricula, idade)
        self._meta_contratacao = meta_contratacao
        self._qtd_contratacao = qtd_contratacao
        self._tipo_recrutamento = tipo_recrutamento
        self._vagas_disponiveis = vagas_disponiveis

    def set_meta_contratacao(self, meta_contratacao:int):
        if not isinstance(meta_contratacao, int):
            return False
        else: 
            self._meta_contratacao = meta_contratacao
            return True
        
    def get_meta_contratacao(self):
        return self._meta_contratacao

    def set_qtd_contratacao(self, qtd_contratacao:int):
        if not isinstance(qtd_contratacao, int):
            return False
        else: 
            self._qtd_contratacao = qtd_contratacao
            return True
        

    def get_qtd_contratacao(self):
        return self._qtd_contratacao

    #@abstractmethod
    def recrutar_funcionario(self):
        self.set_qtd_contratacao(self.get_qtd_contratacao() +1)
        return True


    def set_tipo_recrutamento(self, tipo_recrutamento):
        if not isinstance(tipo_recrutamento, str) or tipo_recrutamento == " ":
            return False
        else: 
            self._tipo_recrutamento = tipo_recrutamento
            return True
        

    def get_tipo_recrutamento(self):
        return self._tipo_recrutamento

    def set_vagas_disponiveis(self, vagas_disponiveis):
        if not isinstance(vagas_disponiveis, list):
            return False
        else: 
            self._vagas_disponiveis = vagas_disponiveis
            return True
        
    def get_vagas_disponiveis(self):
        return self._vagas_disponiveis

    def pagamento_funcionario(self):
        salario = 0
        salario_base = 2000
        if self.meta_alcancada():
            salario = salario_base * 4
        else:
            salario = salario_base * 1.5
        return salario

    def meta_alcancada(self):
        if (self.get_qtd_contratacao() >= self.get_meta_contratacao()):
            return True
        else:
            return False    

class Desenvolvedor(FuncionarioTI):
    def __init__(self, nome:str = None, matricula:str  = None, idade:int = 0, senha_rede:str  = None, id_computador:str  = None, linguagem:list  = None, senioridade:str  = None, qtde_projetos:int = 0):
        super().__init__(nome, matricula, idade, senha_rede, id_computador)
        self._linguagem = linguagem
        self._senioridade = senioridade
        self._qtde_projetos = qtde_projetos

    def set_linguagem(self, linguagem:list):
        if not isinstance(linguagem, list):
            return False
        else: 
            self._linguagem = linguagem
            return True
        
    def get_linguagem(self):
        return self._linguagem

    def set_senioridade(self, senioridade:str):
        if not isinstance(senioridade, str):
            return False
        else: 
            self._senioridade = senioridade
            return True

    def get_senioridade(self):
        return self._senioridade

    def set_qtde_projetos(self, qtde_projetos):
        if not isinstance(qtde_projetos):
            return False
        else: 
            self._qtde_projetos = qtde_projetos
            return True

    def get_qtde_projetos(self):
        return self._qtde_projetos
    
    def pagamento_funcionario(self):
        salario = 0
        salario_base = 3000
        if(self.get_senioridade == "JR"):
            salario = salario_base
        if(self.get_senioridade == "PL"):
            salario = salario_base * 2
        if(self.get_senioridade == 'SR'):
            salario = salario_base * 3
        return salario
    
    def registrar_projetos(self):
        self.set_qtde_projetos (self.get_qtde_projetos() + 1)
        return True

class Suporte(FuncionarioTI):
    def __init__(self, nome:str  = None , matricula:str  = None, idade:int = 0, senha_rede:str  = None, id_computador:str  = None, setor:str  = None, especialidade:str  = None, qtde_atendimento:int = 0):
        super().__init__(nome, matricula, idade, senha_rede, id_computador)
        self._setor = setor
        self._especialidade = especialidade
        self._qtde_atendimento = qtde_atendimento


    def set_setor(self, setor:str):
        if not isinstance(setor, str):
            return False
        else: 
            self._setor = setor
            return True
        
    def get_setor(self):
        return self._setor

    def set_especialidade(self, especialidade:str):
        if not isinstance(especialidade, str):
            return False
        else: 
            self._especialidade = especialidade
            return True
        
    def get_especialidade(self):
        return self._especialidade

    def set_qtde_atendimento(self, qtde_atendimento:int):
        
        if not isinstance(qtde_atendimento, int):
            return False
        else: 
            self._qtde_atendimento = qtde_atendimento
            return True
        
    def get_qtde_atendimento(self):
        return self._qtde_atendimento

    def pagamento_funcionario(self):
        salario = 0
        salario_base = 3000
        if(self.get_setor == "seguranca"):
            salario = salario_base * 2
        else:
            salario = salario_base * 1.5
        return salario
    
    def registrar_atendimento(self):
        self.set_qtde_atendimento(self.get_qtde_atendimento() + 1)
        return True