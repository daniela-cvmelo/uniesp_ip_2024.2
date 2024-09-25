#  Questão 3. Adivinhação de Animais 

#  a.  Descrição:  Imagine  que  você  é  um  mago  que  pode  adivinhar  o  animal  favorito  das  pessoas.  Crie 
#  um   programa   que   pergunte   à   pessoa   se   seu   animal   favorito   é   mamífero   ou   réptil.   Se   for 
#  mamífero,  o  programa  deve  sugerir  que  é  um  cachorro;  se  for  réptil,  o  programa  deve  sugerir 
#  que é uma tartaruga.  
#  b. Conceito: Desvio condicional composto, variáveis.



def classe_animal():

    print('Digite o seu tipo de animal favorito: ')
    print('1 - Mamífero \n2 - Réptil')
    opcao = int(input('Qual a sua opção? '))

    if opcao == 1:
        print('Você prefere mamíferos!')
    else:
        print('Você prefere répteis!')


if __name__ == '__main__':

    
    print("--- --- Iniciando o programa --- ---")

    classe_animal()

    print("--- --- Fim do programa --- ---")


