"""Escreva um programa que receba dois números e imprima na tela se o primeiro é divisível pelo segundo."""

numero_a = int(input("Informe um número inteiro A: "))
numero_b = int(input("Informe um número inteiro B: "))

if numero_a % numero_b == 0:
    print(f"{numero_a} é divisível por {numero_b}.")
else:
    print(f"{numero_a} não é divisível por {numero_b}.")