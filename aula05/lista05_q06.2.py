def calcular_velocidade_dragao(distancia, dragao1, dragao2):

    if vel_dga1 > vel_dga2:
        print('O dragão 1 é o mais veloz')
    elif vel_dga2 > vel_dga1:
        print('O dragão 2 não é o mais veloz')
    else:
        print('Os dois dragoes tem a mesma velocidade')


if __name__ == '__main__':
    DISTANCIA = 1000

    dragao1 = float(input('Digite o tempo do dragão 1: '))
    dragao2 = float(input('Digite o tempo do dragão 2: '))

    calcular_velocidade_dragao(DISTANCIA, dragao1, dragao2),
