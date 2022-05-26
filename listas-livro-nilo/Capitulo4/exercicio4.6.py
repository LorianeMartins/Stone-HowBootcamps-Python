"""Escreva um programa que pergunte a distância que um passageiro deseja percorrer em km.
Calcule o preço da passagem, cobrando R$ 0,50 por km para viagens de até de 200 km, e R$
0,45 para viagens mais longas.
"""

distancia = float(input("Informe a distância a ser percorrida em km: "))

if distancia <= 200:

    preco_passagem = 0.50 * distancia

else: 
    preco_passagem = 0.45 * distancia

print(f"O valor da passagem é R${preco_passagem}")