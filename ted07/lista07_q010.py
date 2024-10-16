import random

def lancar_dados(vezes):
    resultados = []
    for _ in range(vezes):
        resultado = random.randint(1, 6)
        resultados.append(resultado)
        print(f"Lançamento {_+1}: {resultado}")
    return resultados

vezes = int(input("Quantas vezes você quer lançar o dado? "))
resultados = lancar_dados(vezes)
print(f"Resultados dos lançamentos: {resultados}")
