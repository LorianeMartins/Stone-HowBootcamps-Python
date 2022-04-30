"""Sendo H = 1 + 1/2 + 1/3 + 1/4 + ... + 1/N, faça um programa que calcule o valor de H com N termos."""

n_termos = int(input("Digite uma quantidade de termos: "))

h = 0

for num in range(n_termos):

    decimal = 1 / (num + 1)

    h += decimal

print(f"Valor de H com N termos : {h:0.2f}")
