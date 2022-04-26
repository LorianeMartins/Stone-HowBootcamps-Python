"""
Escreva um programa que converta uma temperatura digitada em °C em °F. A fórmula para essa conversão é:

     9 × C
 F = ----- + 32
       5
"""

temperatura_celsius = float(input("Informe a temperatura em °C: "))

temperatura_farenheint = (9 * temperatura_celsius / 5) + 32

print(f"\nA temperatura em Farenheint é de {temperatura_farenheint}°F.")