# Calcular a nota no curso com certo número de alunos
#
# Para cada aluno, Ler K notas(reais) e K pesos (inteiros)
# Cada nota tem um peso definido como uma entrada
# Caso de teste:
# 1) peso positivo
# 2) notas no intervalo de [0,10]

def validar_notas(notas, pesos):
    executa = True
    msg_erro: str = "\n"
    i = 0
    while executa == True and i < len(notas):
        if notas[i] < 0 or notas[i] > 10:
            executa = False
            msg_erro = "Nota %d tem valor inválido" % (i+1)
        if pesos[i] <= 0:
            executa = False
            msg_erro = msg_erro + "Peso %d tem valor inválido!" % (i+1)

        i = i + 1
    return executa, msg_erro


def calcular_media(notas, pesos):
    temp_nota = 0.0
    temp_peso = 0
    for i in range(0, len(notas)):
        temp_nota = temp_nota + (notas[i] * pesos[i])
        temp_peso = temp_peso + pesos[i]

    media_final: float = temp_nota / temp_peso

    return media_final


def ler_notas(nro_notas):
    notas = []
    for i in range(0, nro_notas):
        nota = float(input())
        notas.append(nota)

    return notas


def ler_pesos(nro_pesos):
    pesos = []
    for i in range(0, nro_pesos):
        peso = int(input())
        pesos.append(peso)

    return pesos


def main():
    nro_alunos = int(input())
    nro_notas = int(input())
    nro_pesos = nro_notas

    pesos = ler_pesos(nro_pesos)
    # while nro_alunos > 0 :
    for i in range(0, nro_alunos):
        notas = ler_notas(nro_notas)
        executa, msg_erro = validar_notas(notas, pesos)
        if executa:
            media = calcular_media(notas, pesos)
            print("%.2f" % media)
        else:
            print("Entrada de dados inválida!")
            print(msg_erro)

    #    nro_alunos = nro_alunos - 1


if __name__ == "__main__":
    main()
