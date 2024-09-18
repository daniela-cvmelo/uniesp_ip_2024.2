
def funcao_processamento():

    qtd_ferro = float(input('Digite a quantidade de ferro: '))  
    qtd_ouro = float(input('Digite a quantidade de ouro: ')) 

    total_liga_metalica = qtd_ferro + qtd_ouro

    if (qtd_ferro/total_liga_metalica) >= 0.7:

        print('A sua armadura será legal!')

    else:
        print('Essa armadura vai quebrar!')

if __name__ == '__main__':

    
    print("--- --- Iniciando o programa --- ---")

    funcao_processamento()

    print("--- --- Fim do programa --- ---")


