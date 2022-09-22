import validador as val

def main():
    v = val.Validador()
    base_dados = []
    for i in range(0,1000):
        telefone = input("Informe Telefone: ")
        data = input("Informe data: ")
        if not v.validar_telefone(telefone):
            print("Telefone Inválido")
        elif not v.validar_data(data):
            print("Data inválida")
        else:
            entrada = {"telefone":telefone, "data": data}
            base_dados.append(entrada)


if __name__ == "__main__":
    main()