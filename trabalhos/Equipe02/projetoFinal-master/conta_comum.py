class ContaComum(object):

    global lista_contas
    lista_contas = []

    # Construtor
    def __init__(self, nro_conta=0, dt_abertura='', dt_encerramento='', saldo=0.0):
        self.nro_conta = nro_conta
        self.dt_abertura = dt_abertura
        self.dt_encerramento = dt_encerramento
        self.saldo = saldo

    
    # getter   
    def get_nro_conta(self):
        return self._nro_conta

    def get_dt_abertura(self):
        return self._dt_abertura

    def get_dt_encerramento(self):
        return self._dt_encerramento

    def get_saldo(self):
        return self._saldo

    # setter
    def set_nro_conta(self, nro_conta):
        self._nro_conta = nro_conta

    def set_dt_abertura(self, dt_abertura):
        self._dt_abertura = dt_abertura

    def set_dt_encerramento(self, dt_encerramento):
        self._dt_encerramento = dt_encerramento

    def set_saldo(self, saldo):
        self._saldo = saldo

    def abrirConta(self, nro_conta):
        if nro_conta in lista_contas:
            return False
        else:
            lista_contas.append(nro_conta)
            return True

    def fecharConta(self, nro_conta):
        if nro_conta in lista_contas:
            lista_contas.remove(nro_conta)
            return True
        else:
            return False

    def saldoConta(self, saldo):
        if saldo > 1:
            return True
        else:
            return False
