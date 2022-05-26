"""Escreva um programa que pergunte o depósito inicial e a taxa de juros de uma poupança. Exiba
os valores mês a mês para os 24 primeiros meses. Escreva o total ganho com juros no período.
"""

deposito = float(input("Informe o valor do depósito em R$: "))
taxa_juros = float(input("Informe a taxa de juros mensal da poupança em %: "))

for mes in range(25):

    valor_final = deposito * ((1 + (taxa_juros/100)) ** mes)

    print(f"mês {mes}: R${valor_final:0.2f}")

ganho_juros = valor_final - deposito

print(f"O valor ganho com os juros da poupança foi R${ganho_juros:0.2f}")