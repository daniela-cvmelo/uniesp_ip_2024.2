#  Questão 4. Contagem de Moedas 
#  
#  a.  Descrição:  Um  colecionador  de  moedas  tem  3  tipos  de  moedas:  de  1  real,  de  50  centavos  e  de 
#  25  centavos.  Escreva  um  programa  que  receba  a  quantidade  de  cada  tipo  de  moeda  e  calcule  o 
#  valor total que o colecionador tem.  
#  b. Conceito: Operadores aritméticos, tipos de dados (float). 



def quantidade_moedas():

    qtd_moeda_25centavos = float(input('Digite a quantidade de moedas de 25 centavos: '))
    qtd_moeda_50centavos = float(input('Digite a quantidade de moedas de 50 centavos: ')) 
    qtd_moeda_1real = float(input('Digite a quantidade de moedas de 1 real: ')) 
    
    total_moedas = int(qtd_moeda_25centavos + qtd_moeda_50centavos + qtd_moeda_1real)

    print('A quantidade total de moedas é de: ', total_moedas, 'moedas')
       
if __name__ == '__main__':

    
    print("--- --- Iniciando o programa --- ---")

    quantidade_moedas()

    print("--- --- Fim do programa --- ---")