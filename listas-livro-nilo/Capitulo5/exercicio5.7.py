"""Modifique o programa anterior de forma que o usuário também digite o início e o fim da tabuada,
em vez de começar com 1 e 10.
"""
inteiro = int(input("Digite um número e obtenha a tabuada desse número: "))
inicio = int(input("Digite o número pelo qual se inicia a tabuada: "))
fim = int(input("Digite o número no qual termina a tabuada: "))

for num in range(inicio, fim + 1, 1):

    resultado = num * inteiro

    print(f"{num} x {inteiro} = {resultado}")