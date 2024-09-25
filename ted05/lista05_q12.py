#  Questão 12. A Batalha Final 
#  
#  a.  Descrição:  Um  herói  precisa  decidir  qual  arma  usar  na  batalha  final.  Ele  tem  três  armas:  uma 
#  espada,   um   arco   e   uma   lança.   Cada   arma   tem   um   poder   de   ataque   e  uma  durabilidade.  A 
#  escolha  deve  considerar  que  o  poder  de  ataque  seja  maior  que  50  e  a  durabilidade  maior  que 
#  70.   Crie   um   programa   que   receba   os   valores   de   ataque   e   durabilidade   das   três   armas   e 
#  determine  qual  é  a  mais  adequada.  Se  nenhuma  atender,  o  programa  deve  sugerir  que  o  herói 
#  busque uma nova arma.  
#  b. Conceito: Operadores lógicos, relacionais, desvio condicional aninhado.

def arma_elegivel():


    print('=> Bem vindo guerreiro! Você chegou na batalha final e precisa escolher qual arma irá usar!\n=> Siga as instruções abaixo e irei indicar para você qual a arma mais poderosa que você possui!')
    print('=> Primeiro vamos verificar se cada arma cumpre os requisitos mínimos e é elegível a ser a melhor arma:')

    ataque_espada = int(input('*A espada possui no mínimo 50 de ataque? 1 - SIM, 2 - NÃO: '))
    durabilidade_espada = int(input('*A espada possui no mínimo 70 de durabilidade? 1 - SIM, 2 - NÃO: '))
    ataque_lanca = int(input('*A lança possui no mínimo 50 de ataque? 1 - SIM, 2 - NÃO: '))
    durabilidade_lanca = int(input('A lança possui no mínimo 70 de durabilidade? 1 - SIM, 2 - NÃO: '))
    ataque_arco = int(input('O arco possui no mínimo 50 de ataque? 1 - SIM, 2 - NÃO: '))
    durabilidade_arco = int(input('O arco possui no mínimo 70 de durabilidade? 1 - SIM, 2 - NÃO: '))
    
    poder_espada = ataque_espada + durabilidade_espada
    poder_lanca = ataque_lanca + durabilidade_lanca
    poder_arco = ataque_arco + durabilidade_arco
  

    if ataque_espada == 1 and durabilidade_espada == 1:
        print('A espada é uma arma elegível')
    else:
        print('A espada não é uma arma elegível')
    if ataque_lanca == 1 and durabilidade_lanca == 1:
        print('A lança é uma arma elegível')
    else:
        print('A lança não é uma arma elegível')
    if ataque_arco == 1 and durabilidade_arco == 1:
        print('O arco é uma arma elegível')
    else:
        print('O arco não é uma arma elegível')

    # if poder_espada == 2 and poder_lanca == 2 and poder_arco == 2:
    # else:
    #     print('Nenhuma dessas armas cumpre os requisitos mínimos para poder ser elegível! Busque novas armas!')  

if __name__ == '__main__':

    print("--- --- Determinando a elegibilidade das armas --- ---")

    arma_elegivel()

    print("--- --- Se as armas foram elegíveis, prossiga para o próximo passo --- ---")


def comparando_armas ():
  
    print('=>Agora vamos comparar as armas:')

    ataque_espada = int(input('*Digite o valor de ataque da espada: '))
    durabilidade_espada = int(input('*Digite o valor de durabilidade da espada: '))
    ataque_lanca = int(input('*Digite o valor de ataque da lança: '))
    durabilidade_lanca = int(input('*Digite o valor de durabilidade da lança: '))
    ataque_arco = int(input('*Digite o valor de ataque do arco: '))
    durabilidade_arco = int(input('*Digite o valor de durabilidade do arco: '))

    poder_espada = ataque_espada + durabilidade_espada
    poder_lanca = ataque_lanca + durabilidade_lanca
    poder_arco = ataque_arco + durabilidade_arco

    if poder_espada >= 120 or poder_lanca >= 120 or poder_arco >= 120:
        if poder_espada > poder_lanca and poder_espada > poder_arco:
            print('A espada é a melhor arma para você usar!!!')
        if poder_lanca > poder_espada and poder_lanca > poder_arco:
            print('A lança é a melhor arma para você usar!!!')
        if poder_arco > poder_espada and poder_arco > poder_lanca:
            print('O arco é a melhor arma para você usar!!!')
        elif poder_espada == poder_lanca == poder_arco:
            print('Todas as armas são iguais, pode escolher qualquer uma para a batalha!')
    else:
        print('As armas não tem como serem comparadas por não terem atingido os requisitos mínimos')


  
if __name__ == '__main__':

    
    print("--- --- Comparando as armas--- ---")

    comparando_armas()

    print("--- --- Parabéns, você descobriu a melhor arma para usar na Batalha Final!--- ---")