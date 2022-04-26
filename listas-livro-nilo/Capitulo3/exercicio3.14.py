"""Escreva um programa que pergunte a quantidade de km percorridos por um carro alugado pelo usuário, assim como a quantidade de dias pelos quais o carro foi alugado. Calcule o preço a pagar, sabendo que o carro custa R$ 60 por dia e R$ 0,15 por km rodado.
"""

qtd_dias = int(input("Informe a quantidade de dias de uso do carro: "))
qtd_km = float(input("Informe a quantidade de km rodados com o carro: "))

preco_a_pagar = (qtd_dias * 60) + (0.15 * qtd_km)

print(f"\nO preço a pagar pelo aluguel do carro é de R${preco_a_pagar}")
