"""Escreva um programa que leia dois números. Imprima o resultado da multiplicação do primeiro
pelo segundo. Utilize apenas os operadores de soma e subtração para calcular o resultado.
Lembre-se de que podemos entender a multiplicação de dois números como somas sucessivas de
um deles. Assim, 4 × 5 = 5 + 5 + 5 + 5 = 4 + 4 + 4 + 4 + 4.
"""

num_a = int(input("Informe um valor inteiro para o número a: "))
num_b = int(input("Informe um valor inteiro para o número b: "))

soma = 0 
for _ in range(num_a):
    
    soma += num_b

print(f"O produto entre os números é: {soma}")
