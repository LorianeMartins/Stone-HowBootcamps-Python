"""Faça um programa que imprima na tela se um dado ano é bissexto ou não de acordo com as regras na ordem abaixo:
1.	Um ano que é divisível por 400 é bissexto.
2.	Dos anos que não entram na regra 1, se o ano for divisível por 100 então ele não é bissexto.
3.	Dos anos que não entram na regra 2, se o ano for divisível por 4 então ele é um ano bissexto.
4.	Todos os outros anos não são bissextos"""

ano = int(input("Informe um ano: "))

if ano % 400 == 0:
    print(f"{ano} é bissexto.")
elif ano % 100 == 0:
    print(f"{ano} não é bissexto.")
elif ano % 4 ==0:
    print(f"{ano} é bissexto.")
else:
    print(f"{ano} não é bissexto.")

# Também daria para ter usado True ou False. 