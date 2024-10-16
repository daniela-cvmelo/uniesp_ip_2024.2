def contar_vogais_consoantes():
    frase = input("Digite uma frase: ")
    vogais = "aeiouAEIOU"
    num_vogais = 0
    num_consoantes = 0
    
    for char in frase:
        if char.isalpha():
            if char in vogais:
                num_vogais += 1
            else:
                num_consoantes += 1
    
    print(f"Número de vogais: {num_vogais}")
    print(f"Número de consoantes: {num_consoantes}")

contar_vogais_consoantes()
