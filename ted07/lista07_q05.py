def fibonacci(n):
    seq = [0, 1]
    while len(seq) < n:
        seq.append(seq[-1] + seq[-2])
    return seq[:n]

n = int(input("Digite o número de termos da sequência de Fibonacci que deseja gerar: "))
resultado = fibonacci(n)
print(f"Os primeiros {n} números da sequência de Fibonacci são: {resultado}")
