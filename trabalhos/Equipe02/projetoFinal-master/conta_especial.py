from conta_comum import ContaComum


class ContaEspecial(ContaComum):

#Construtor
    def __init__(self, limite_conta=0.0):
        self.limite_conta = limite_conta


        # getter
        def get_limite_conta(self):
            return self._limite_conta



        # setter
        def set_limite_conta(self, limite_conta):
            self._limite_conta = limite_conta



    def jurosConta(self,saldo):

        if saldo < 0:
            saldo = saldo + (saldo * -0.05) * -10
            print(saldo)
            return saldo
        else:
            return saldo

