#  Questão 5. Jornada no Deserto 

#  a.  Descrição:  Um  explorador  está  cruzando  um  deserto.  Ele  precisa  saber  se  a  quantidade  de  água 
#  que  tem  é  suficiente  para  chegar  ao  próximo  oásis.  Ele  calcula  que  precisa  de  2  litros  de  água 
#  para   cada   quilômetro.   Crie   um   programa   que   receba   a   quantidade   de   água   disponível   e   a 
#  distância até o oásis, e informe se a água é suficiente. 
#  b. Conceito: Operadores aritméticos, desvio condicional simples.




def quantidade_agua():

    qtd_agua = float(input('Digite a quantidade de água restante: '))
    distancia_oasis = float(input('Digite a distância que falta até chegar ao oasis: ')) 
    
    if distancia_oasis * 2 <= qtd_agua:
        print('Você tem água suficiente para chegar ao seu destino')

    else:
        print('Sua água vai acabar antes de você chegar ao seu destino')
 
       
if __name__ == '__main__':

    
    print("--- --- Iniciando o programa --- ---")

    quantidade_agua()

    print("--- --- Fim do programa --- ---")