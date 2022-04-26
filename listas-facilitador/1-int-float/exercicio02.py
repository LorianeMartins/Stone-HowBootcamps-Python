"""Faça um programa que receba a base e altura de um triângulo e imprima a área 
dele.
Dica!
A área de um triângulo é dada pela seguinte fórmula abaixo
𝑎𝑟𝑒𝑎 = 𝑏𝑎𝑠𝑒 𝑥 𝑎𝑙𝑡𝑢𝑟𝑎
       ------------
            2
"""
base = float(input("Informe o valor da base do triângulo em cm: "))
altura = float(input("Informe o valor da altura do triângulo em cm: "))

area_triangulo = (base * altura) / 2

print(f"\nA área do triângulo é {area_triangulo} cm².")
