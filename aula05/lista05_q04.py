def funcao_processamento():

    qtd_moeda_25centavos = float(input('Digite a quantidade de moedas de 25 centavos: '))
    qtd_moeda_50centavos = float(input('Digite a quantidade de moedas de 50 centavos: ')) 
    qtd_moeda_1real = float(input('Digite a quantidade de moedas de 1 real: ')) 
    
    total_moedas = int(qtd_moeda_25centavos + qtd_moeda_50centavos + qtd_moeda_1real)

    print('A quantidade total de moedas é de: ', total_moedas, 'moedas')
       
if __name__ == '__main__':

    
    print("--- --- Iniciando o programa --- ---")

    funcao_processamento()

    print("--- --- Fim do programa --- ---")