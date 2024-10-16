import random

def jogo_adivinhacao():
    numero_secreto = random.randint(1, 100)
    tentativas = 0
    
    print("Bem-vindo ao jogo de adivinhação!")
    print("Tente adivinhar o número entre 1 e 100.")
    
    while True:
        palpite = int(input("Digite seu palpite: "))
        tentativas += 1
        
        if palpite < numero_secreto:
            print("Mais alto!")
        elif palpite > numero_secreto:
            print("Mais baixo!")
        else:
            print(f"Parabéns! Você adivinhou o número em {tentativas} tentativas.")
            break

jogo_adivinhacao()
