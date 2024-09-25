#  Questão 8. Calculadora de Bônus 
#  
#  a.  Descrição:  Um  rei  deseja  distribuir  bônus  aos  seus  cavaleiros  com  base  em  suas  conquistas.  Se 
#  um  cavaleiro  completou  mais  de  10  missões,  ele  recebe  um  bônus  de  100  moedas  de  ouro.  Se 
#  completou  entre  5  e  10  missões,  recebe  50  moedas  de  ouro.  Se  completou  menos  de  5,  recebe 
#  10  moedas  de  ouro.  Crie  um  programa  que  receba  o  número  de  missões  completadas  e  informe 
#  o valor do bônus.  
#  b. Conceito: Desvio condicional aninhado, operadores relacionais.





def recompensas():

    numero_missoes = int(input('Digite o número de missões completadas: '))
        
    if numero_missoes > 5:
        if numero_missoes >5 and numero_missoes <10:
            print('Você receberá 50 moedas de ouro')
        if numero_missoes > 10:
            print('Você receberá 100 moedas de ouro')
    else:
        print('Você irá receber 10 moedas de ouro')    
       
if __name__ == '__main__':

    
    print("--- --- Iniciando o programa --- ---")

    recompensas()

    print("--- --- Fim do programa --- ---")