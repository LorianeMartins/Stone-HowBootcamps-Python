"""Faça um programa que calcule o aumento de um salário. Ele deve solicitar o valor do salário e a porcentagem do aumento. Exiba o valor do aumento e do novo salário."""

salario = float(input("Informe o salário: "))
aumento = float(input("Informe o aumento em %: "))

valor_aumento = salario * aumento / 100
novo_salario = salario + valor_aumento

print(f"\nO aumento foi de R${valor_aumento}")
print(f"\nO novo salário é de R${novo_salario}")