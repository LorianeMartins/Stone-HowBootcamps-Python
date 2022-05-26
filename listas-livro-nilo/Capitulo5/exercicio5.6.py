"""Altere o programa anterior para exibir os resultados no mesmo formato de uma tabuada: 2x1 = 2,
2x2 = 4, …
"""
inteiro = int(input("Digite um número e obtenha a tabuada desse número: "))

for num in range(1, 11, 1):

    resultado = num * inteiro

    print(f"{num} x {inteiro} = {resultado}")
