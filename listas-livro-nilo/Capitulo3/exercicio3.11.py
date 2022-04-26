"""Faça um programa que solicite o preço de uma mercadoria e o percentual de desconto. Exiba o valor do desconto e o preço a pagar."""

preco_mercadoria = float(input("Informe o preço da mercadoria: "))
desconto = float(input("Informe o valor do desconto em %: "))

valor_desconto = preco_mercadoria * desconto / 100
novo_preco = preco_mercadoria - valor_desconto

print(f"\nO valor do desconto foi de R${valor_desconto}")
print(f"O novo preço da mercadoria é de R${novo_preco}")

