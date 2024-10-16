def gerar_tabuada():
    numero = int(input("Digite um número para gerar a tabuada: "))
    
    print(f"Tabuada do {numero}:")
    for i in range(1, 11):
        resultado = numero * i
        print(f"{numero} x {i} = {resultado}")
        
gerar_tabuada()
