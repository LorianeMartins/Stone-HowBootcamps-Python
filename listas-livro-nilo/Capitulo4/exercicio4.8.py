"""Escreva um programa que leia dois números e que pergunte qual operação você deseja realizar.
Você deve poder calcular soma (+), subtração (-), multiplicação (*) e divisão (/). Exiba o
resultado da operação solicitada"""

num_a = float(input("Informe um número a: "))
num_b = float(input("Informe um número b: "))

operacao = input("Informe um operação (+), (-), (*) ou (/): ")

if operacao == "+":
    resultado = num_a + num_b

elif operacao == "-":
    resultado = num_a - num_b

elif operacao == "*":
    resultado = num_a * num_b

elif operacao == "/":
    resultado = num_a / num_b 

else: 
    print("Operação inválida!")
    resultado = 0

print(f"A operação escolhida foi {operacao} e o resultado é {resultado}")