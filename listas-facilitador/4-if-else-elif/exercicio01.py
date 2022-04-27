"""Escreva um programa que diga se um número dado pelo usuário é par ou ímpar."""

numero = int(input("Informe um número inteiro: "))

if numero % 2 != 0:
    print(f"{numero} -> número ímpar")
else:
    print(f"{numero} -> número par")