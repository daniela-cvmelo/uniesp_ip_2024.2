def arquivo_txt():

    lista_vingadores = open("vingadores.txt", "r", encoding="utf-8-sig")
    print(lista_vingadores.read())
    lista_vingadores.close()
    

if __name__ == '__main__':

    print("--- --- Iniciando o programa --- ---") 

    arquivo_txt() 

    print("--- --- Fim do programa --- ---") 

