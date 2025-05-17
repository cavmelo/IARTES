def main():
    nomes=['maria', 'pedro', 'carlos', 'tereza']
    for primeiro in nomes:
        print(primeiro)

    if 'maria' in nomes:
        print('sim')
    else:
        print('não')

    pessoas=[{'nome':'pedro','idade':10},{'nome':'joca','idade':13}]
    pessoas.append({'nome':'carlos','idade':15})
    for pessoa in pessoas:
        print(pessoa['idade'])

    quadrados = [i*i for i in range(0,100)]  
    print(quadrados)    

    meu_nome='Cesar Augusto Viana Melo'
    
    separados = meu_nome.split()
    do_meio = separados[1:len(separados)-1]
    iniciais = " ".join([x[0]+"." for x in do_meio])

    print(separados[0], iniciais , separados[-1] )
if __name__== '__main__':
    main()
