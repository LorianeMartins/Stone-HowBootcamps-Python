"""No exercício 02 você calculou a área de um triângulo a partir da sua base e altura. Faça um programa que receba os 3 lados de um triângulo (s1, s2 e s3) e calcule sua área. 
Compare a resposta com o exercício acima, dada das mesmas entradas. 
Os resultados devem ser idênticos.
"""

s1 = float(input("Informe o lado 1 do triângulo em cm: "))
s2 = float(input("Informe o lado 2 do triângulo em cm: "))
s3 = float(input("Informe o lado 3 do triângulo em cm: "))

s = (s1 + s2 + s3) / 2

area = (s * (s - s1) * (s - s2) * (s - s3)) ** (1 / 2)

print(f"\nA área do triângulo é {area} cm².")
