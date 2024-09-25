#  Questão 15. Portal de Viagem no Tempo 
#  
#  a.  Descrição:  Um  cientista  está  criando  um  portal  de  viagem  no  tempo  que  só  pode  ser  ativado  se 
#  todos   os   parâmetros   estiverem   corretos:   energia   acima   de   80%,   coordenadas   de   destino 
#  precisas,  e  o  tempo  ajustado  corretamente.  Crie  um  programa  que  receba  esses  valores  e  use 
#  operadores  lógicos  para  verificar  se  o  portal  pode  ser  ativado.  Se  qualquer  parâmetro  estiver 
#  incorreto, o programa deve indicar qual é o problema.  
#  b. Conceito: Operadores lógicos, relacionais, desvio condicional aninhado. 

def portal():


    print('=> Olá Cientista! Vamos verificar se o portal pode ser ativado!\n=> Siga as instruções abaixo para iniciarmos a verificação!')
    
    nivel_energia = int(input('*Digite o valor do nível de energia entre 0 e 1 (sendo 1 = 100%): '))
    coordenadas_destino = int(input('As coordenadas de destino são: 1 - Precisas ou 2 - Imprecisas?: '))
    ajuste_tempo = int(input('O tempo foi ajustado corretamente? 1 - SIM ou 2 - NÃO: '))
        
    ativacao_portal = nivel_energia + coordenadas_destino + ajuste_tempo
     
   
    if ativacao_portal != 10:
        if nivel_energia < 8:
            print('O nível de energia não está adequado. Ele precisa estar em 80%')
        if coordenadas_destino != 1:
            print('As coordenadas estão erradas, ajuste para coordenadas precisas')
        if ajuste_tempo !=1:
            print('Ajuste o tempo corretamente')
    else:
        print('Todos os parâmetros estão corretos, o portal pode ser ativado!')    
       
if __name__ == '__main__':

    
    print("--- --- Iniciando o programa --- ---")

    portal()

    print("--- --- Fim do programa --- ---")