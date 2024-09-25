#  Questão 9. Escolha de Feitiços 
 
#  a.   Descrição:   Um   mago   tem   três   feitiços:   fogo,   água   e   terra.   Crie   um  programa  que  receba  a 
#  escolha  do  usuário  (1  para  fogo,  2  para  água,  3  para  terra)  e  use  o  comando  match-case  para 
#  exibir o feitiço escolhido.  
#  b. Conceito: Match-case, variáveis.





def elemento_favorito():

    print('Um mago possui três feitiços: ')
    print('1 - Fogo \n2 - Água \n3 - Terra')
    opcao = int(input('Escolha qual o seu elemento preferido:' ))

    match opcao:
        case 1:
            print('Você escolheu o elemento Fogo')
        case 2:
            print('Você escolheu o elemento Água')
        case 3:
            print('Você escolheu o elemento Terra')
        case _:
            print('Opção inválida')

   
if __name__ == '__main__':

    
    print("--- --- Iniciando o programa --- ---")

    elemento_favorito()

    print("--- --- Fim do programa --- ---")
