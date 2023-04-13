class Movimento(object):

#Construtor
    def __init__(self, tipo_mov=0, dt_mov='', hr_mov='', valor_mov=0.0):
        self.tipo_mov = tipo_mov
        self.dt_mov = dt_mov
        self.hr_mov = hr_mov
        self.valor_mov = valor_mov
        
        # getter

    def get_tipo_mov(self):
        return self._tipo_mov

    def get_dt_mov(self):
        return self._dt_mov

    def get_hr_mov(self):
        return self._hr_mov

    def get_valor_mov(self):
        print("teste",self._valor_mov)
        return self._valor_mov

        # setter
    def set_tipo_mov(self, tipo_mov):
        self._tipo_mov = tipo_mov

    def set_dt_mov(self, dt_mov):
        self._dt_mov = dt_mov

    def set_hr_mov(self, hr_mov):
        self._hr_mov = hr_mov

    def set_valor_mov(self, valor_mov):
        self._valor_mov = valor_mov

    def regMovimento(self, tipo_mov, val_mov):
        return 0

    def cenMovimento(self, dt_mov):
        dia = int(dt_mov[:2])
        mes = int(dt_mov[2:4])
        ano = int(dt_mov[4:])
        meses_de_31 = (1, 3, 5, 7, 8, 10, 12)
        meses_de_30 = (4, 6, 9, 11)

        ano_valido = False
        if ano > 0 and len(dt_mov[4:])==4:
            ano_valido = True

        mes_valido = False
        if mes > 0 and mes < 13:
            mes_valido = True

        dia_valido = False
        if dia > 0 and dia < 32:
            if dia == 31:
                if mes in meses_de_31:
                    dia_valido = True
            elif dia == 30:
                if mes in meses_de_30 or mes in meses_de_31:
                    dia_valido = True
            elif dia == 29:
                if mes != 2:
                    dia_valido = True
                elif mes == 2 and (ano % 4 == 0 and ano % 100 != 0) or (ano % 400 == 0):
                    dia_valido = True        
            else:
                dia_valido = True

        data_valida = False
        if ano_valido and mes_valido and dia_valido:
            data_valida = True

        return data_valida
