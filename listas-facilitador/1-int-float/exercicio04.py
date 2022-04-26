"""Faça um programa que receba do usuário seu peso em kg e altura em metros e imprima o Índice de Massa Corporal (IMC) do usuário"""

peso_kg = float(input("Informe o peso em kg: "))
altura_metros = float(input("Informe a altura em metros: "))

imc = peso_kg / altura_metros ** 2 

print(f"\nO Índice de Massa Corporal (IMC) é : {imc:0.2f}.")
