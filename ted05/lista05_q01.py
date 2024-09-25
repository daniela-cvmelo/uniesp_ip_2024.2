#  Questão 1. O Tesouro Escondido 
#  a.  Descrição:  Um  mapa  do  tesouro  tem  duas  partes,  A  e  B.  A  primeira  parte  está  escondida  no  X 
#  número   de   passos   para   o   norte,   e   a  segunda  no  Y  número  de  passos  para  o  leste.  Crie  um 
#  programa   que   receba   os   valores   de   X   e   Y   e   calcule   a   distância   total   que   o   pirata   precisa 
#  percorrer para chegar ao tesouro (soma de X e Y).  
#  b. Conceito: Operadores aritméticos, variáveis. 

def bau_tesouro():
    
    X = int(input('Digite os passos até X: '))
    Y = int(input('Digite os passos até Y: '))
 
    qtd_passos = X + Y
    
    print(f'A quantidade de passos para o pirata será de {qtd_passos}')


if __name__ == '__main__':

    
    print("--- --- Iniciando o programa --- ---")

    
    bau_tesouro()

  
    print("--- --- Fim do programa --- ---")


