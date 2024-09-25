#  Questão 10. A Caverna dos Desafios 
#  
#  a.  Descrição:  Um  aventureiro  encontrou  uma  caverna  cheia  de  portas,  cada  uma  com  um  número 
#  de  1  a  5.  Atrás  de  cada  porta  há  um  desafio.  Crie  um  programa  que  receba  o  número  da  porta 
#  escolhido pelo aventureiro e use match-case para mostrar qual desafio ele enfrentará.  
#  b. Conceito: Match-case, operadores relacionais.



def caverna_desafios():

    nome_aventureiro = input('Digite seu nome: ')
    print(f'Bem vindo(a) {nome_aventureiro}, você chegou a uma caverna com várias portas, cada porta apresenta um desafio diferente!')
    print('Você tem 5 opções de desafios a sua frente: \n1 - Desafio A \n2 - Desafio B \n3 - Desafio C \n4 - Desafio D \n5 - Desafio E')
    opcao = int(input('Escolha qual o desafio que você quer enfrentar:' ))

    match opcao:
        case 1:
            print('Você escolheu o desafio do "Labirinto de Madeira"')
        case 2:
            print('Você escolheu o desafio do "Desfiladeiro Escuro"')
        case 3:
            print('Você escolheu o desafio do "Jogo de Cartas"')
        case 4:
            print('Você escolheu o desafio do "Enigma do Sábio"')
        case 5: 
            print('Você escolheu o desafio da "Sala Secreta"')
        case _:
            print('Opção inválida')

   
if __name__ == '__main__':

    
    print("--- --- Iniciando o programa --- ---")

    caverna_desafios()

    print("--- --- Fim do programa --- ---")