# Código principal para iniciar um programa de Python
# Criação de uma função (função de processamento do programa)
def funcao_processamento():
    # Valores aleatórios
    X = int(input('Digite os passos até X: '))
    Y = int(input('Digite os passos até Y: '))
    # Soma da quantidade de passos
    qtd_passos = X + Y
    # Apresentação do resultado
    print(f'A quantidade de passos para o pirata será de {qtd_passos}')

#  Esse if está identificando se o nome do programa abaixo é main
if __name__ == '__main__':

    # Mensagem de início do programa
    print("--- --- Iniciando o programa --- ---")

    # Processamento realizado pelo programa
    funcao_processamento()

    # Mensagem de fim do programa
    print("--- --- Fim do programa --- ---")


