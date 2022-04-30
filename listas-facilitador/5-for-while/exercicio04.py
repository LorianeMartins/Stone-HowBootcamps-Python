"""Uma aroximação para o valor de pi pode ser calculado a partir da fórmula abaixo (uma série infinita):
pi≈3+4/2x3x4-4/4x5x6+4/6x7x8-4/8x9x10+4/10x11x12-4/12x13x14+⋯
Escreva um programa que calcule o número pi com 15 aproximações. 
A primeira aproximação deve considerar apenas o primeiro termo da série, ou seja 3. 
A segunda aproximação deve considerar a soma até o segundo termo, e assim por diante!"""

denominador = 0

numerador = 0

pi = 0

for aprox in range(15): 

    if aprox == 0:
        pi += 3
        continue

    if aprox % 2 != 0:
        numerador = 4 

    else: 
        numerador = -4 

    aprox = aprox * 2
    denominador = aprox * (aprox + 1) * (aprox + 2)

    pi += numerador / denominador


print(f"\nO valor de pi com 15 aproximações: {pi}")

    