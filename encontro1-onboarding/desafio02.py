"""Desafio 02: o que esse pequeno trecho de código faz? 

    Esse pequeno trecho de código recebe como entrada o quantidade de quilômetros percorridos por um carro e a quantidade de dias em que esse foi utilizado. A partir disso calcula o valor a ser pago pelo uso do carro com base em operações matemáticas de preço por dia e preço por km. 

"""
qtd_km = int(input("Digite a quantidade de quilômetros percorridos: "))

qtd_dias = int(input("Digite quantos dias você ficou com o carro: "))

preco_por_dia = 60
preco_por_km = 0.15

preco_total_km = qtd_km * preco_por_km
preco_total_dia = qtd_dias * preco_por_dia

preco_a_pagar = preco_total_km + preco_total_dia

print(f"Total a pagar: R$ {preco_a_pagar:7.2f}")



