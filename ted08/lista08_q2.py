# Construa uma matriz A de tamanho 10 x 10 com valores inteiros e randômicos. Depois:
# a. Imprima o resultado da soma de todos os valores da matriz no terminal;
# b. E, criei uma nova matriz B, no qual cada item seja o valor da matriz A * 3;


import random


A = [[random.randint(1, 100) for _ in range(10)] for _ in range(10)]


soma_total = 0
for linha in A:
    for valor in linha:
        soma_total += valor


print("Soma de todos os valores da matriz A:", soma_total)


B = [[A[i][j] * 3 for j in range(10)] for i in range(10)]


print("\nMatriz A:")
for linha in A:
    print(linha)

print("\nMatriz B (cada elemento de A multiplicado por 3):")
for linha in B:
    print(linha)
