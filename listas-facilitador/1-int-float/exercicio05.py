"""
Escreva um programa que leia do usuário um número de 4 dígitos e imprima a 
soma destes dígitos. Exemplo, se o usuário digitar 3141 seu programa deverá 
imprimir na tela 3 + 1 + 4 + 1 = 9.
"""
numero = input("Informe um número de 4 dígitos:")

while len(numero) != 4 or not numero.isnumeric():

    numero = input("Informe um número de 4 dígitos:")

soma = int(numero[0]) + int(numero[1]) + int(numero[2]) + int(numero[3])

print(f"\nA soma entre os dígitos do número informado é : {soma}")