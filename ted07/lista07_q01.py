# def notas_aluno():

#     nota = float(input('Insira a nota do aluno: '))
#     print('Quando terminar de digitar as notas, digite -1 para encerrar o programa')
    
#     number = 0

#     while number != -1:
#         print(f'A nota foi {nota}')
#         if number == -1:
#             break
#         number = number + 1

# if __name__ == '__main__':
    
#     notas_aluno()



#     def media_notas():

#         nota = float(input('Insira a nota do aluno: '))
#         print('Quando terminar de digitar as notas, digite -1 para encerrar o programa')
#         soma_notas = 0
#         contador = 0
    
#         while number != -1:
#             print(f'A nota foi {nota}')
#         soma_notas +=notas
#         contador +=1
#         if number == -1:
#             break
        

# if __name__ == '__main__':
    
#     media_notas()




def funcao_principal():

    soma_notas = 0
    contador = 0
    
    nota = float(input("Digite uma nota válida entre 0 e 10 (digite -1 quando não tiver mais notas): "))
    
    while nota != -1:
        soma_notas += nota
        contador += 1
        nota = float(input("Digite uma nota válida entre 0 e 10 (digite -1 quando não tiver mais notas): "))

    if contador > 0:
        media = soma_notas / contador
        print(f"A média das notas é: {media:.2f}")
    else:
        print("Nenhuma nota válida foi inserida.")

if __name__ == '__main__':

    print("\n--- --- Início do programa! --- ---\n")
    funcao_principal()
    print("\n--- --- Fim do programa! --- ---\n")