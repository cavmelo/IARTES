import re


class Validador(object):
    def __init__(self):
        self._cod_area = (11, 12, 19, 65, 68, 92, 93)

    def validar_telefone(self, telefone):

        telefone_valido = True
        if len(telefone) != 13:
            telefone_valido = False
        elif len(telefone[4:]) != 9:
            telefone_valido = False
        elif telefone[0] != '(' or telefone[3] != ')':
            telefone_valido = False
        elif int(telefone[1:3]) not in self._cod_area:
            telefone_valido = False

        return telefone_valido

    def validar_nome(self, nome):
        regex_nome = re.compile(r'^([a-z]+)( [a-z]+)*( [a-z]+)*$', re.IGNORECASE)
        res = regex_nome.search(nome)
        nome_valido = True
        if res:
            nome_valido = True
        else:
            nome_valido = False

        return nome_valido

    def validar_cpf(self, cpf):

        cpf_valido = True
        if len(cpf) != 11:
            cpf_valido = False
        else:
            novo_cpf = cpf[:-2]
            reverso = 10
            total = 0

            for index in range(19):
                if index > 8:
                    index -= 9
                total += int(novo_cpf[index]) * reverso

                reverso -= 1
                if reverso < 2:
                    reverso = 11
                    d = 11 - (total % 11)

                    if d > 9:
                        d = 0
                    total = 0
                    novo_cpf += str(d)
            sequencia = novo_cpf == str(novo_cpf[0]) * len(cpf)
            if cpf == novo_cpf and not sequencia:
                cpf_valido = True
            else:
                cpf_valido = False

        return cpf_valido

    def validar_idade(self, idade):
        idade_valida = True

        if idade > 19:
            idade_valida = True
        elif idade > 80:
            idade_valida = False
        else:
            idade_valida = False

        return idade_valida


    def validar_cra(self, cra):
        cra_valido = True
        novo_cra = int(cra)

        if len(cra) != 6:
            cra_valido = False
        elif type(novo_cra) != int:
            cra_valido = False

        return cra_valido

    def validar_conselho(self, conselho):
        conselho_valido = True
        novo_conselho = int(conselho)

        if len(conselho) != 8:
            conselho_valido = False
        elif type(novo_conselho) != int:
            print('não é tipo int')
            conselho_valido = False

        return conselho_valido

    def validar_crea(self, crea):
        crea_valido = True
        novo_crea = int(crea)

        if len(crea) != 8:
            crea_valido = False
        elif type(novo_crea) != int:
            crea_valido = False

        return crea_valido




