"""Em um determinado país, as tarifas de táxi consistem em uma tarifa básica de R$4,00 mais R$0,25 para cada 140 metros percorridos.
Escreva uma função que receba a distância percorrida (em quilômetros) como único parâmetro e retorna a tarifa total como único resultado.
Escreva um programa que demonstre o uso da sua função."""



def tarifa_total(distancia: float) -> float:

    tarifa = 4 + (0.25 * distancia * 1000 / 140)

    return tarifa

print("\n #### Calcule a tarifa do táxi ####")

distancia = float(input("Informe a distância percorrida em km: "))

tarifa_taxi = tarifa_total(distancia)

print(f"A tarifa do táxi a ser paga é R${tarifa_taxi:0.2f}")