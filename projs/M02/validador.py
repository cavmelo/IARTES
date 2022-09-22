
def ano_bissexto(ano):
    return False

def validar_data(data):
    dia = int(data[:2])
    mes = int(data[3:5])
    ano = int(data[6:])
    meses_de_31 = (1, 3, 5, 7, 8, 10, 12)
    meses_de_30 = (4, 6, 9, 11)

    ano_valido = False
    if ano > 0 and len(data[6:])==4:
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
            if mes in meses_de_30:
                dia_valido = True
        elif dia == 29:
            if mes != 2:
                dia_valido = True
            elif mes == 2 and ano_bissexto(ano):
                dia_valido = True
        else:
            dia_valido = True

    data_valida = False
    if ano_valido and mes_valido and dia_valido:
        data_valida = True

    #return dia_valido, mes_valido, ano_valido
    return data_valida

# (92)999679090
def validar_telefone(telefone):
    cod_area = (11, 12, 19, 65, 68, 92, 93)
    telefone_valido = True
    if len(telefone) != 13:
        telefone_valido = False
    elif len(telefone[4:]) != 9:
        telefone_valido = False
    elif telefone[0] != '(' or telefone[3] != ')':
        telefone_valido = False
    elif int(telefone[1:3]) not in cod_area:
        telefone_valido = False

    return telefone_valido

def main():
    base_dados = []
    for i in range(0,1000):
        telefone = input("Informe Telefone: ")
        data = input("Informe data: ")
        if not validar_telefone(telefone):
            print("Telefone Inválido")
        elif not validar_data(data):
            print("Data inválida")
        else:
            entrada = {"telefone":telefone, "data": data}
            base_dados.append(entrada)


if __name__ == "__main__":
    main()