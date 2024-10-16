def converter_decimal_para_binario(numero):
    if numero == 0:
        return "0"
    binario = ""
    while numero > 0:
        resto = numero % 2
        binario = str(resto) + binario
        numero = numero // 2
    return binario

numero = int(input("Digite um número decimal para converter para binário: "))
resultado = converter_decimal_para_binario(numero)
print(f"A representação binária de {numero} é {resultado}.")
