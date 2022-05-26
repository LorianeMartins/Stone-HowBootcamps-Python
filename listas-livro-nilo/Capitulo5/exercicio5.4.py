"""Modifique o programa anterior para imprimir de 1 até o número digitado pelo usuário, mas,
dessa vez, apenas os números ímpares.
"""

numero = int(input("Informe um número: "))

for num in range(1, numero, 1):

    if num % 2 != 0: 
        print(num)
