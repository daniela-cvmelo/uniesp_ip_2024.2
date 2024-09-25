#  Questão 13. Sistema de Defesa de Castelos 
#  
#  a. Descrição: O   sistema   de   defesa   de   um   castelo   mágico   precisa   estar  sempre  ativo  quando  o 
#  exército  do  rei  está  fora.  Crie  um  programa  que  receba  a  posição  do  exército  (dentro  ou  fora 
#  do castelo) e use match-case para ativar ou desativar o sistema de defesa automaticamente.  
#  b. Conceito: Match-case, operadores lógicos, desvio condicional. 

def defesa_castelo():

    posicao_exercito = input('Qual é a posição do exército do Rei? \n1 - dentro do castelo \n2 - fora do castelo')
    opcao = int(input('Escolha sua opção:' ))

    match opcao:
        case 1:
            print('O sistema de defesa foi desativado')
        case 2:
            print('O sistema de defesa foi ativado')
        case _:
            print('Opção inválida')

   
if __name__ == '__main__':

    
    print("--- --- Iniciando o programa --- ---")

    defesa_castelo()

    print("--- --- Fim do programa --- ---")