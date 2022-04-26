"""Faça um programa que receba a temperatura média de cada mês do ano e armazene-as em uma lista. 
Em seguida, calcule a média anual das temperaturas e mostre a média calculada juntamente com todas as temperaturas acima da média anual, e em que mês elas ocorreram (mostrar o mês por extenso)
"""
meses = (
        "Janeiro", 
        "Fevereiro", 
        "Março", 
        "Abril", 
        "Maio", 
        "Junho", 
        "Julho", 
        "Agosto", 
        "Setembro",
        "Outubro", 
        "Novembro", 
        "Dezembro"
)

temperaturas = []

for mes in meses:

    temperatura = float(input(f"Informe a temperatura em C do mês {mes}: "))
    temperaturas.append(temperatura)

media_anual = sum(temperaturas) / len(temperaturas)

print(f"\nA média de temperatura anual foi de {media_anual:0.2f} C.")

print(f"\nMeses com temperatura acima da média anual: ")
for indice, temperatura in enumerate(temperaturas): 
    if temperatura > media_anual: 
        print(f"{meses[indice]} - {temperatura} C")

