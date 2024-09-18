def funcao_processamento():

    qtd_agua = float(input('Digite a quantidade de água restante: '))
    distancia_oasis = float(input('Digite a distância que falta até chegar ao oasis: ')) 
    
    if distancia_oasis * 2 <= qtd_agua:
        print('Você tem água suficiente para chegar ao seu destino')

    else:
        print('Sua água vai acabar antes de você chegar ao seu destino')
 
       
if __name__ == '__main__':

    
    print("--- --- Iniciando o programa --- ---")

    funcao_processamento()

    print("--- --- Fim do programa --- ---")