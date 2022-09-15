def main():
    pasta = "/Users/cesar/data/professional/consulting/IARTES/repo/projs/M01/"
    arq_nome = "codecoverage.repo"
    f = open(pasta + arq_nome, 'r')

    cabecalho = f.readline()
    separador = f.readline()
    modulo = f.readline()
    while modulo != separador:
        lista = modulo.split()
        # for item in lista:
        #     print(item)
        print(lista[0], int(lista[3].split("%")[0]))
        modulo = f.readline()

    consolidado = f.readline()


if __name__ == '__main__':
    main()
