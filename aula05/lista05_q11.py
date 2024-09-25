#  Questão 11. Decisão da Coroa Real: 
 
#  a. Descrição: O conselho real precisa tomar uma decisão crítica: selecionar o próximo governante entre três candidatos, 
#  baseado na sua pontuação em uma série de provas. Crie um programa  que  receba  as  notas  dos  três  candidatos
#  e  determine  qual  deles  teve  a  maior  média. Caso  duas  ou  mais  médias  sejam  iguais,
#  o  programa  deve  exibir  uma  mensagem  informando que há um empate.  
#  b. Conceito: Operadores aritméticos, relacionais, desvio condicional aninhado.

def governante():

    nota_candidato1 = int(input('Digite a nota do candidato 1: '))
    nota_candidato2 = int(input('Digite a nota do candidato 2: '))
    nota_candidato3 = int(input('Digite a nota do candidato 3: '))

    media_candidato1 = nota_candidato1 / 3
    media_candidato2 = nota_candidato2 / 3
    media_candidato3 = nota_candidato3 / 3
        
    if media_candidato1 != media_candidato2 and media_candidato1 != media_candidato3:
        if media_candidato1 > media_candidato2 and media_candidato1 > media_candidato3:
            print('O candidato 1 é o novo governante do reino')
        if media_candidato2 > media_candidato1 and media_candidato2 > media_candidato3:
            print('O candidato 2 é o novo governante do reino')
        if media_candidato3 > media_candidato1 and media_candidato3 > media_candidato2:
            print('O candidato 3 é o novo governante do reino')
    else:
        print('Deu empate entre os candidatos')    
       
if __name__ == '__main__':

    
    print("--- --- Iniciando o programa --- ---")

    governante()

    print("--- --- Fim do programa --- ---")