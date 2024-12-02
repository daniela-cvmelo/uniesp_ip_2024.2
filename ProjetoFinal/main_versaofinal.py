import requests
from time import sleep
from loguru import logger
from deep_translator import GoogleTranslator

URL = 'https://api.adviceslip.com/advice'

def menu():
    print('\nVeja as opções:')
    print('\n1. Quero receber novos conselhos!')
    print('2. Quero ver os conselhos recebidos!')
    print('3. Quero salvar estes conselhos em um arquivo!')
    print('4. Quero ver os conselhos que acabei de salvar no arquivo!')
    print('5. Quero mostrar estes conselhos em inglês para um gringo!')
    print('6. Pronto, estou satisfeito! Vou "mimbora"!')

    opcao = input('\nEscolha uma das opções digitando o seu número: ')
    return opcao

def busca_conselho(URL):
    try:
        resposta_conselho = requests.get(URL)
        id_conselho = resposta_conselho.json()['slip']['id']
        texto_conselho = resposta_conselho.json()['slip']['advice']
        if id_conselho and texto_conselho:
            return id_conselho, texto_conselho
        else:
            logger.error('\nID ou texto do conselho não foram encontrados.')
            return None
    except requests.exceptions.RequestException as bug:
        logger.error(f'\nErro ao acessar a API: {bug}')
        return None

def traduzir_conselho(advice):
    try:
        return GoogleTranslator(source='english', target='portuguese').translate(advice)
    except Exception as bug:
        logger.error(f'\nErro ao traduzir o conselho: {bug}')
        return None

def salvar_txt_conselho(conselhos, nome_txt='conselhos.txt'):
    try:
        with open(nome_txt, 'a', encoding='utf-8') as txt:
            for conselho in conselhos:
                txt.write(f'ID {conselho[0]}: {conselho[1]}\n')
        print(f'\nEstes conselhos foram salvos na pasta do programa com o nome "{nome_txt}"!')
    except Exception as bug:
        logger.error(f'\nErro ao salvar o arquivo: {bug}')
        return None

def ler_ultimas_linhas(nome_txt='conselhos.txt', n_linhas=10):
    try:
        with open(nome_txt, 'r', encoding='utf-8') as txt:
            todas_as_linhas = txt.readlines()
            return todas_as_linhas[-n_linhas:]
    except FileNotFoundError:
        print("\nArquivo não encontrado.")
        return None
    except Exception as bug:
        logger.error(f'\nErro ao ler o arquivo: {bug}')
        return None

print('\nSeja bem-vindo, Seu Zé! Quer alguns conselhos?')

def main():
    conselhos_recebidos = []
    n_conselhos = 0

    while True:
        opcao = menu()

        if opcao == '1':
            conselhos_recebidos = []
            
            while True:
                try:
                    n_conselhos = int(input('\nQuantos conselhos você quer receber? '))
                    if n_conselhos < 0:
                        print('\nPor favor, insira um número válido!')
                    elif n_conselhos == 0:
                        print('\nZero conselhos? Então, vamos voltar ao menu!')
                        break
                    else:
                        break
                except ValueError:
                    print('\nPor favor, insira um número válido!')

            if n_conselhos > 0:
                for i in range(n_conselhos):
                    logger.info(f'Ciclo {i + 1} de chamada de API iniciado')
                    conselho = busca_conselho(URL)
                    if conselho:
                        conselhos_recebidos.append(conselho)
                    else:
                        print(f'\nConselho {i + 1}: Não foi possível obter o conselho.')
                    sleep(1)
                print('Conselhos recebidos com sucesso!')

        elif opcao == '2':
            if conselhos_recebidos:
                print('\nConselhos recebidos agora:\n')
                for id_conselho, texto_conselho in conselhos_recebidos:
                    print(f'ID {id_conselho}: {traduzir_conselho(texto_conselho)}')
            else:
                print('\nNenhum conselho recebido ainda.')

        elif opcao == '3':
            if conselhos_recebidos:
                conselhos_traduzidos = [
                    (id_conselho, traduzir_conselho(texto_conselho)) 
                    for id_conselho, texto_conselho in conselhos_recebidos
                ]
                salvar_txt_conselho(conselhos_traduzidos)
            else:
                print('\nNenhum conselho recebido para salvar!')
        
        elif opcao == '4':
            if n_conselhos > 0:
                conselhos_salvos = ler_ultimas_linhas(nome_txt='conselhos.txt', n_linhas=n_conselhos)
                if conselhos_salvos:
                    print('\nEstes são os conselhos que acabamos de salvar:\n')
                    for conselho in conselhos_salvos:
                        print(conselho.strip())
                else:
                    print('\nNenhum conselho salvo no arquivo.')
            else:
                print('\nNenhum conselho foi solicitado!')

        elif opcao == '5':
            if conselhos_recebidos:
                print('\nPassa esses conselhos em inglês aí pro gringo:\n')
                for id_conselho, texto_conselho in conselhos_recebidos:
                    print(f'ID {id_conselho}: {texto_conselho}')
            else:
                print('\nNenhum conselho recebido ainda.')
        
        elif opcao == '6':
            print('\nEncerrando o programa! Até mais!\n')
            break
        
        else:
            print('\nOpção inválida. Tente de novo!')

if __name__ == '__main__':
    main()
