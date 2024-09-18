def funcao_processamento():

    distancia_dragao1 = float(input('Digite a distância que o dragão 1 corre (em quilômetros): '))
    tempo_dragao1 = float(input('Digite o tempo (em horas): '))
    distancia_dragao2 = float(input('Digite a distância que o dragão 2 corre (em quilômetros): ')) 
    tempo_dragao2 = float(input('Digite o tempo (em horas): '))
    
    velocidade_dragao1 = float(distancia_dragao1 / tempo_dragao1)
    velocidade_dragao2 = float(distancia_dragao2 / tempo_dragao2)

    if velocidade_dragao1 > velocidade_dragao2:
        print('O dragão 1 é mais rápido!')

    else:
        print('O dragão 2 é mais rápido!')  
       
if __name__ == '__main__':

    
    print("--- --- Iniciando o programa --- ---")

    funcao_processamento()

    print("--- --- Fim do programa --- ---")