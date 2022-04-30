"""Neste exercício, você criará um programa que calcula a média de uma coleção de valores inseridos pelo usuário e imprime-a na tela. 
O usuário digitará 0 como um valor para indicar que nenhum outro valor será fornecido. 
Atenção!
Como o 0 é um valor de condição de parada, ele não deve entrar no cálculo da média!"""


valores = []

while 0 not in valores : 

    valor = int(input("Digite um valor (ou 0 para encerrar): "))

    if valor == 0:
        
        break

    else: 

       valores.append(valor)


if not valores: 

    print("Nenhum valor encontrado.")

else: 
    print(f"\nA média dos valores é {sum(valores) / len(valores)}")

    







