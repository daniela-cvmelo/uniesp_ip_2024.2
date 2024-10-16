def desenhar_quadrado(n):
    for i in range(n):
        print('|' * n)

tamanho = int(input("Digite o tamanho do quadrado: "))
desenhar_quadrado(tamanho)
