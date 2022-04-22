"""Desafio 01: o que esse pequeno trecho de código faz?

O trecho abaixo recebe a distância a ser percorrida e a velocidade média de um em que o trajeto será feito para cálcular o tempo em horas necessário."""

distancia = float(input("Digite a distância em km: "))

velocidade_media = float(input("Digite a velocidade média em km/h: "))

tempo_total_horas = distancia / velocidade_media

print(f"\nO tempo estimado é de {tempo_total_horas:.2f} horas")



