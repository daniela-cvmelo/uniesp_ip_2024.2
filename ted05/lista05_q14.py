#  Questão 14. O Julgamento do Sábio 
#  
#  a.  Descrição:  Um  sábio  está  julgando  um  duelo  entre  dois  guerreiros.  Ele  quer  saber  qual  guerreiro 
#  deve   ser   considerado   vencedor,   com  base  em  suas  habilidades  de  ataque  e  defesa.  Crie  um 
#  programa  que  receba  os  valores  de  ataque  e  defesa  dos  dois  guerreiros  e  determine  o  vencedor 
#  (aquele  com  maior  soma  de  ataque  e  defesa).  Se  houver  empate,  o  programa  deve  considerar  a 
#  defesa como critério de desempate.  
#  b. Conceito: Operadores aritméticos, relacionais, desvio condicional aninhado.

def melhor_guerreiro():


    print('=> Olá Sábio! Vamos descobrir qual o guerreiro mais poderoso!\n=> Siga as instruções abaixo e irei indicar para você qual o melhor entre eles!')
    
    ataque_guerreiro1 = int(input('*Digite o valor de ataque do guerreiro 1: '))
    defesa_guerreiro1 = int(input('*Digite o valor de defesa do guerreiro 1: '))
    ataque_guerreiro2 = int(input('*Digite o valor de ataque do guerreiro 2: '))
    defesa_guerreiro2 = int(input('*Digite o valor de defesa do guerreiro 2: '))
    
    poder_guerreiro1 = ataque_guerreiro1 + defesa_guerreiro1
    poder_guerreiro2 = ataque_guerreiro2 + defesa_guerreiro2
    
   
    if poder_guerreiro1 != poder_guerreiro2:
        if poder_guerreiro1 > poder_guerreiro2:
            print('O guerreiro 1 é o mais forte!')
        if poder_guerreiro2 > poder_guerreiro1:
            print('O guerreiro 2 é o mais forte!')
    else:
        print('Houve um empate entre eles! Escolha outro critério para ser usado como desempate!')    
       
if __name__ == '__main__':

    
    print("--- --- Iniciando o programa --- ---")

    melhor_guerreiro()

    print("--- --- Fim do programa --- ---")