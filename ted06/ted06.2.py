def convite_vingadores():

    convite_festa = open("convite_festa.txt", "w")
    convite_festa.write("Todos os Vingadores estão convidados para a festa na minha casa!")
    convite_festa.close()

    convite_festa = open("convite_festa.txt", "r")
    print(convite_festa.read())

if __name__ == '__main__':

    print("--- --- Iniciando o programa --- ---") 

    convite_vingadores() 

    print("--- --- Fim do programa --- ---") 



























# def funcao_processamento():

#     arquivo = open("vingadores.txt", "r", encoding="utf-8-sig") # Uso do comando open() para abrir o arquivo txt e aramazenar na variável arquivo. O arquivo está com uma sequência de bytes BOM "invisível" no seu início para caracterizá-lo como utf8 que está causando a impressão de um caractere extra na primeira linha. Adicionar o parâmetro encoding faz com que o Python leia corretamente, ignorando o caractere extra.
    
#     linha = arquivo.readline() # Uso do comando readline() para ler uma linha por vez, armazenando na variável linha.
    
#     while linha: # Uso do loop while para executar uma ação a cada linha lida.
        
#         personagem = linha.strip() # Com o strip(), eu removo quebras de linha e espaços extras no início e final de cada linha do arquivo, e armazeno na variável personagem.
#         print(f"Olá, {personagem}, venha para a festa dos Vingadores na minha casa!") # Mensagem convite.
#         linha = arquivo.readline()

#     arquivo.close() # Fecho o arquivo txt.

# if __name__ == '__main__':

#     print("\n--- --- Iniciando o programa --- ---\n") # Mensagem de início do programa

#     funcao_processamento() # Processamento realizado pelo programa

#     print("\n--- --- Fim do programa --- ---\n") # Mensagem de fim do programa