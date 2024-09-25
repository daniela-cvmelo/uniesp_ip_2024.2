# Função principal para verificar se a água é suficiente
def verificar_agua_suficiente(agua_disponivel, distancia_ate_oasis):
    # Calcula a quantidade de água necessária
    agua_necessaria = distancia_ate_oasis * 2  # 2 litros por quilômetro

    # Verifica se a água disponível é suficiente
    if agua_disponivel >= agua_necessaria:
        print("A quantidade de água é suficiente para chegar ao oásis.")
    else:
        print("A quantidade de água NÃO é suficiente para chegar ao oásis.")

# Receber a quantidade de água disponível
agua_disponivel = float(input("Digite a quantidade de água disponível (em litros): "))

# Receber a distância até o oásis
distancia_ate_oasis = float(input("Digite a distância até o oásis (em quilômetros): "))

# Chamar a função para verificar se a água é suficiente
verificar_agua_suficiente(agua_disponivel, distancia_ate_oasis)
