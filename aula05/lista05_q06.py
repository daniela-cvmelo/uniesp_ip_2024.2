#  Questão 6. Campeonato de Corrida de Dragões 
#  
#  a.   Descrição:   Em   um   campeonato   de   corrida   de   dragões,   cada   dragão   corre  uma  determinada 
#  distância   em   um   certo   tempo.  Crie  um  programa  que  receba  a  distância  e  o  tempo  de  dois 
#  dragões   diferentes   e   determine   qual   dragão   é   mais   rápido,   ou   se   ambos   têm   a   mesma 
#  velocidade.  
#  b. Conceito: Operadores aritméticos, operadores relacionais, desvio condicional composto.


def corrida_dragoes():

    distancia_dragao1 = float(input('Digite a distância que o dragão 1 corre (em quilômetros): '))
    tempo_dragao1 = float(input('Digite o tempo (em horas): '))
    distancia_dragao2 = float(input('Digite a distância que o dragão 2 corre (em quilômetros): ')) 
    tempo_dragao2 = float(input('Digite o tempo (em horas): '))
    
    velocidade_dragao1 = float(distancia_dragao1 / tempo_dragao1)
    velocidade_dragao2 = float(distancia_dragao2 / tempo_dragao2)

    if velocidade_dragao1 > velocidade_dragao2:
        print('O dragão 1 é mais rápido!')
    elif velocidade_dragao1 == velocidade_dragao2:
            print('A velocidade deles é igual')
    else:
        print('O dragão 2 é mais rápido!') 
         
       
if __name__ == '__main__':

    
    print("--- --- Iniciando o programa --- ---")

    corrida_dragoes()

    print("--- --- Fim do programa --- ---")

    #Se nessa questão a distância fosse considerada a mesma para os dois, então a variável distância deveria ser constante. Para ser
    #constante o nome precisa ser em caixa alta