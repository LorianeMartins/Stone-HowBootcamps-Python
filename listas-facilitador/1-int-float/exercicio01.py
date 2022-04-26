"""Faça um programa que receba dois números inteiros do usuário, A e B e imprima 
na tela as seguintes operações:
- A soma de A e B;
- A diferença quando se subtrai B de A;
- O produto (multiplicação) entre A e B;
- O quociente (parte inteira da divisão) quando se divide A por B;
- O resto da divisão entre A e B;
- O resultado de log10 de A;
- O resultado de A elevado a B
Dica!
Para calcular o log10, utilize a função log10 do módulo math conforme 
exemplo abaixo
>>> from math import log10
>>> log10(100)
2.0
"""

from math import log10

numero_a = int(input("Informe um número inteiro A: "))
numero_b = int(input("Informe um número inteiro B: "))

print(f"A soma entre A e B é {numero_a + numero_b}.")
print(f"\nA diferença entre A e B é {numero_a - numero_b}.")
print(f"\nO produto entre A e B é {numero_a * numero_b}.")
print(f"\nO quociente de quando se divide A por B é {numero_a // numero_b}.")
print(f"\nO resto da divisão de A por B é {numero_a % numero_b}.")
print(f"\nO resultado de log10 de A é: {log10(numero_a)}")
print(f"\nO resultado de A elevado a B é {numero_a ** numero_b}.")

