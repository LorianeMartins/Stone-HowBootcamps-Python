"""Escreva um programa que calcule o tempo de uma viagem de carro. Pergunte a distância a percorrer e a velocidade média esperada para a viagem.
"""

distancia = float(input("Informe a distância a ser percorrida em km: "))
velocidade_media = float(input("Informe a valocidade média do carro em km/h: "))

tempo = velocidade_media / distancia

print(f"\nO tempo da viagem será de {tempo} h.")