from conta_comum import ContaComum


class ContaPoupanca(ContaComum):

#Construtor
    def __init__(self, dt_aniversario=''):
        self.dt_aniversario = dt_aniversario


        # getter
        def get_dt_aniversario(self):
            return self._dt_aniversario



        # setter
        def set_dt_aniversario(self, dt_aniversario):
            self._dt_aniversario = dt_aniversario


    def rendeConta(self, dt_aniversario, saldo):
        if saldo > 10 and saldo < 100:
            return True
        else:
            return False

