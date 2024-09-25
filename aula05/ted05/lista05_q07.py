#  Questão 7. Classificação de Plantas Mágicas 
#  
#  a.  Descrição:  Um  botânico  está  classificando  plantas  mágicas  em  uma  floresta.  Ele  quer  saber  se 
#  uma  planta  é  pequena  (menos  de  1  metro),  média  (entre  1  e  3  metros),  ou  grande  (mais  de  3 
#  metros). Crie um programa que receba a altura da planta e informe a sua classificação.  
#  b. Conceito: Operadores relacionais, desvio condicional aninhado.


def planta():

    tamanho_planta = float(input('Digite a altura da planta (em metros): '))
        
    if tamanho_planta > 1:
        if tamanho_planta >1 and tamanho_planta <3:
            print('Sua planta é média')
        if tamanho_planta >3:
            print('Sua planta é grande')
    
    else:
        print('Sua planta é pequena')    
       
if __name__ == '__main__':

    
    print("--- --- Iniciando o programa --- ---")

    planta()

    print("--- --- Fim do programa --- ---")