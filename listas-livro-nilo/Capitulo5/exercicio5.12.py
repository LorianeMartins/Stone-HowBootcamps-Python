"""Altere o programa anterior de forma a perguntar também o valor depositado mensalmente. Esse
valor será depositado no início de cada mês, e você deve considerá-lo para o cálculo de juros do
mês seguinte."""

deposito = float(input("Informe o valor do depósito em R$: "))
taxa = float(input("Informe a taxa de juros mensal da poupança em %: "))
deposito_mensal = float(input("Informe o valor do depósito mensal em R$: "))

valor_final = deposito

for mes in range(1, 25):

    valor_final += (valor_final * (taxa/100)) + deposito_mensal

    print(f"mês {mes}: R${valor_final:0.2f}")

ganho_juros = valor_final - deposito

print(f"O valor ganho com os juros da poupança foi R${ganho_juros:0.2f}")