import validador as val

def main():
    v = val.Validador()
    base_dados = []
    for i in range(0,1000):
        telefone = input("Informe Telefone: ")
        nome = input("Informe nome: ")
        idade = int(input("Informe a idade: "))
        cpf = input("Informe CPF: ")
        conselho = input("Informe o número do registro no seu conselho profissional: ")
        cra = input("Informe o número de registro no Conselho Regional de Administração: ")
        crea = input("Informe o número de registro no CREA: ")

        if not v.validar_telefone(telefone):
            print("Telefone Inválido")
        elif not v.validar_nome(nome):
            print("Nome Inválido")
        elif not v.validar_idade(idade):
            print("Idade Inválida")
        elif not v.validar_cpf(cpf):
            print("CPF Inválido")
        elif not v.validar_conselho(conselho):
            print("Número de Registro de Conselho Inválido")
        elif not v.validar_cra(cra):
            print("CRA Inválido")
        elif not v.validar_crea(crea):
            print("CREA Inválido")
        else:
            entrada = {"telefone":telefone, "nome": nome, "idade": idade, "cpf": cpf, "conselho": conselho, "cra": cra, "crea": crea}
            base_dados.append(entrada)


if __name__ == "__main__":
    main()