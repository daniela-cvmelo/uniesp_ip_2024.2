Faça um algoritmo para ler 10 números e armazenar em um vetor VET, verificar e escrever se existem
números repetidos no vetor VET e em que posições se encontram.


VET = [0] * 10


for i in range(10):
    VET[i] = int(input(f"Digite o número na posição {i}: "))


repeticoes = {}


for i in range(10):
    numero = VET[i]
   
    if numero not in repeticoes:
    
        posicoes = []
        for j in range(10):
            if VET[j] == numero:
                posicoes += [j]  
        
        if len(posicoes) > 1:
            repeticoes[numero] = posicoes  


if repeticoes:
    print("Números repetidos e suas posições:")
    for numero in repeticoes:
        posicoes = repeticoes[numero]
        print(f"Número {numero} encontrado nas posições: {posicoes}")
else:
    print("Não existem números repetidos no vetor.")

