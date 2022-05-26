"""Escreva um programa que pergunte o salário do funcionário e calcule o valor do aumento. Para
salários superiores a R$ 1.250,00, calcule um aumento de 10%. Para os inferiores ou iguais, de
15%.
"""

salario = float(input("Informe o salário do funcionário: "))

if salario > 1250: 

    aumento = 0.1 
    salario_novo = salario + (salario * aumento)

else: 
    aumento = 0.15
    salario_novo = salario + (salario * aumento)

print(f"Salário do funcionário: R${salario}")
print(f"Aumento no salário do funcionário: {aumento * 100}%")
print(f"Novo salário do funcionário: R${salario_novo}")
